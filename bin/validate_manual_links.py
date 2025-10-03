#!/usr/bin/env python3
"""
Script to validate manual links in the OpenOLAT repository.
Searches for: manual_user, manual_admin, manual_dev, manual_how-to, manual_notes
Validates links against docs.openolat.org and writes results to CSV.

Usage:
    python validate_manual_links.py /path/to/OpenOLAT [--only-errors]

Arguments:
    repo_path: Path to the OpenOLAT repository root
    --only-errors: Only output links where at least one language is not working
"""

import os
import re
import csv
import sys
import argparse
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

patterns = [
    r'manual_user[^"\'\s]*',
    r'manual_admin[^"\'\s]*',
    r'manual_dev[^"\'\s]*',
    r'manual_how-to[^"\'\s]*',
    r'manual_notes[^"\'\s]*',
]

combined_pattern = re.compile("|".join(patterns))


def check_url(url):
    """Check if a URL exists and if anchor exists (returns page_ok, anchor_ok)."""
    try:
        if "#" in url:
            base_url, anchor = url.rsplit("#", 1)
        else:
            base_url = url
            anchor = None

        response = requests.get(base_url, timeout=10, allow_redirects=True)
        page_ok = response.status_code == 200

        anchor_ok = True
        if page_ok and anchor:
            content = response.text.lower()
            anchor_patterns = [
                f'id="{anchor.lower()}"',
                f"id='{anchor.lower()}'",
                f"id={anchor.lower()}",
                f'name="{anchor.lower()}"',
                f"name='{anchor.lower()}'",
            ]
            anchor_ok = any(pattern in content for pattern in anchor_patterns)

        return page_ok, anchor_ok
    except Exception:
        return False, False


def check_link_pair(link, short_filename, line_num):
    """Check both English and German URLs for a link."""
    english_url = f"https://docs.openolat.org/{link}"
    german_url = f"https://docs.openolat.org/de/{link}"

    en_page_ok, en_anchor_ok = check_url(english_url)
    de_page_ok, de_anchor_ok = check_url(german_url)

    english_ok = en_page_ok and en_anchor_ok
    german_ok = de_page_ok and de_anchor_ok

    en_status = (
        "YES"
        if english_ok
        else ("PAGE_MISSING" if not en_page_ok else "ANCHOR_MISSING")
    )
    de_status = (
        "YES" if german_ok else ("PAGE_MISSING" if not de_page_ok else "ANCHOR_MISSING")
    )

    return {
        "filename": short_filename,
        "line": line_num,
        "link": link,
        "english_ok": en_status,
        "german_ok": de_status,
    }


def find_manual_links(repo_root, only_errors=False):
    """Search for manual links in all files under the search directory."""
    search_dir = repo_root / "src" / "main" / "java"

    if not search_dir.exists():
        print(f"Error: Directory {search_dir} does not exist")
        print(f"Make sure {repo_root} is the correct path to the OpenOLAT repository")
        return

    results = []

    for root, dirs, files in os.walk(search_dir):
        for file in files:
            file_path = Path(root) / file

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line_num, line in enumerate(f, 1):
                        matches = combined_pattern.findall(line)
                        for match in matches:
                            clean_match = match.rstrip("\"'\\,;:)")
                            results.append((str(file_path), line_num, clean_match))
            except Exception:
                continue

    if results:
        print(f"Found {len(results)} manual links\n")

        all_matches = []

        for file_path, line_num, link in results:
            full_path = Path(file_path)
            try:
                relative_path = full_path.relative_to(repo_root)
            except ValueError:
                relative_path = full_path.name

            all_matches.append((link, str(relative_path), line_num))

        print(f"Checking {len(all_matches)} matches in parallel...\n")

        csv_data = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_match = {
                executor.submit(check_link_pair, link, filename, line_num): (
                    link,
                    filename,
                    line_num,
                )
                for link, filename, line_num in all_matches
            }

            for future in as_completed(future_to_match):
                link, filename, line_num = future_to_match[future]
                try:
                    result = future.result()

                    if (
                        only_errors
                        and result["english_ok"] == "YES"
                        and result["german_ok"] == "YES"
                    ):
                        continue

                    csv_data.append(result)
                    print(
                        f"✓ {filename}:{line_num} {link}: EN={result['english_ok']}, DE={result['german_ok']}"
                    )
                except Exception as e:
                    print(f"✗ {filename}:{line_num} {link}: Error - {e}")

        if csv_data:
            csv_data.sort(key=lambda x: (x["filename"], x["line"]))

            csv_filename = "manual_links_validation.csv"
            with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["filename", "line", "link", "english_ok", "german_ok"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(csv_data)

            print(f"\n✓ Results written to {csv_filename}")
            print(f"  Total matches: {len(csv_data)}")
            if only_errors:
                print("  (Filtered to show only errors)")
        else:
            print("\n✓ No results to write")
            if only_errors:
                print("  All links are working correctly!")
    else:
        print("No manual links found")


def main():
    """Main function to parse arguments and run the script."""
    parser = argparse.ArgumentParser(
        description="Validate manual links in the OpenOLAT repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate_manual_links.py /path/to/OpenOLAT
  python validate_manual_links.py ~/repositories/OpenOLAT --only-errors
        """,
    )

    parser.add_argument(
        "repo_path", type=str, help="Path to the OpenOLAT repository root"
    )

    parser.add_argument(
        "--only-errors",
        action="store_true",
        help="Only output links where at least one language (EN or DE) is not working",
    )

    args = parser.parse_args()

    repo_root = Path(args.repo_path).expanduser().resolve()

    if not repo_root.exists():
        print(f"Error: Repository path does not exist: {repo_root}")
        sys.exit(1)

    if not repo_root.is_dir():
        print(f"Error: Repository path is not a directory: {repo_root}")
        sys.exit(1)

    print(f"Searching in: {repo_root}")
    if args.only_errors:
        print("Filtering: Only showing errors\n")
    else:
        print("Filtering: Showing all results\n")

    find_manual_links(repo_root, args.only_errors)


if __name__ == "__main__":
    main()
