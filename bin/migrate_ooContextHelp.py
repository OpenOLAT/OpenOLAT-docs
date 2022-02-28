import os, re, sys, fileinput, getopt, shutil, csv, html2text
from os import walk
from urllib.parse import unquote
from pathlib import Path

from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import urllib.request

#Home

#confluencePath = '/Users/gnaegi/Desktop/us.sitesucker.mac.sitesucker/confluence.openolat.org/'
projectPath = '/Users/gnaegi/OpenOLAT-docs/'
#ooPath = '/Users/gnaegi/workspace/OpenOLAT/src/main/java/'

#Office
confluencePath = '/Users/gnaegi/Desktop/us.sitesucker.mac.sitesucker_full/confluence.openolat.org/'
projectPath = '/Users/gnaegi/workspace/OpenOLAT-docs/'
ooPath = '/Users/gnaegi/workspace/openolat-lms/src/main/java/'

def recurse_findDirs(path):
	for entry in os.scandir(path):
		if entry.is_dir(follow_symlinks=False):
			yield from recurse_findDirs(entry.path)
		elif entry.is_file(follow_symlinks=False):
			yield entry
		else:
			raise NotImplemented()

def findAllPages(dir):
	for entry in recurse_findDirs(dir):
		filename = entry.path
		if filename.endswith('.md'):
			filename = filename.split('OpenOLAT-docs/')[1]
			parts = filename.split('/')
			#print(parts)
			yield parts
	

def cleanFilename(name):
	name = name.replace(' / ', '_')
	name = name.replace(': ','_')
	name = name.replace('+',' ')
	name = name.replace('﹕','')
	name = name.replace(':','')
	name = name.replace('  ',' ')
	name = name.replace(' ','_')
	name = name.replace('... ','').lstrip()
	return name

def listCHelpDir(dir):
	export = open("ooCHelpReferences.csv", 'w', newline='', encoding='UTF8')
	writer = csv.writer(export)
	writer.writerow(["Call", "Search", "Page", "Anchor", "NewPage", "NewAnchor", "Replacement"])
	exportNotFount = open("ooCHelpReferences_notFound.csv", 'w', newline='', encoding='UTF8')
	writerNotFound = csv.writer(exportNotFount)
	writerNotFound.writerow(["Call", "Search", "Page", "Anchor", "NewPage", "NewAnchor", "Replacement"])

	for entry in recurse_findDirs(dir):
		filename = entry.path
		if filename.endswith('.html') or filename.endswith('.java'):
			listCHelpFile(filename, writer, writerNotFound)
			
	export.close()

def listCHelpFile(filename, writer, writerNotFound):
	allPages = list(findAllPages(projectPath))
	with fileinput.FileInput(filename, inplace=False) as file:
		for idx, line in enumerate(file):
			newline = line
			matches = re.findall('(setFormContextHelp\(("([^#"]*)[#]{0,1}([^"]*)")\))',line)
			convertAndWriteCSV(matches, writer, writerNotFound, allPages)
			matches = re.findall('(contextHelpWithWrapper\(("([^#"]*)[#]{0,1}([^"]*)")\))',line)
			convertAndWriteCSV(matches, writer, writerNotFound, allPages)
			matches = re.findall('(contextHelpJSCommand\(("([^#"]*)[#]{0,1}([^"]*)")\))',line)
			convertAndWriteCSV(matches, writer, writerNotFound, allPages)
			matches = re.findall('(contextHelpLink\(("([^#"]*)[#]{0,1}([^"]*)")\))',line)
			convertAndWriteCSV(matches, writer, writerNotFound, allPages)
			matches = re.findall('(getManualProvider\(\)\.getURL\((\s*[^,]*\s*,\s*"([^#"]*)[#]{0,1}([^"]*)")\))',line)
			convertAndWriteCSV(matches, writer, writerNotFound, allPages)



def convertAndWriteCSV(matches, writer, writerNotFound, allPages):
	for match in matches:
		if (match[2].startswith("$")) or match[2] == '': print("Skipping variable usage", match)
		else:
			cleaned = cleanFilename(match[2])
			replacementPath = findReplacementPage(cleaned, allPages)
			result = list(match)
			if replacementPath:
				result.append(replacementPath)
				if match[3]:
					newAnchor = match[3][1:]
					result.append(newAnchor)
					result.append('"' + replacementPath + '#' + newAnchor + '"')
				else:
					result.append('')
					result.append('"' + replacementPath + '"')
				writer.writerow(result)
			else:
				writerNotFound.writerow(result)

def findReplacementPage(targetPage, allPages):
	for page in allPages:
		if page[len(page)-1].endswith(".de.md"):
			continue
		elif not page[len(page)-1].endswith(".md"):
			continue
		# continue only with en files
#		print(page[len(page)-1].split(".")[0],targetPage)
		if page[len(page)-1].split(".")[0] == targetPage:
			replacement = ''
			for part in page:
				if part == 'docs' or part == 'sites':
					continue
				replacement = replacement + part.split(".")[0] + '/'
#				print(replacement)
			if len(replacement) > 0:
				return replacement


def replaceCHelpDirXX(dir, mappings, doReplace):
	## for all html and java files...
	executor = ThreadPoolExecutor(max_workers=100)
	allDirs = recurse_findDirs(dir)
	future_replaced = {executor.submit(replaceCHelpFile,entry.path, mappings, doReplace): entry for entry in allDirs}
	for future in concurrent.futures.as_completed(future_replaced):
		entry = future_replaced[future]
		found = future.result()
		print(found)

def replaceCHelpDir(dir, mappings, doReplace):
	## for all html and java files...
	for entry in recurse_findDirs(dir):
		filename = entry.path
		if filename.endswith('.html') or filename.endswith('.java'):
			replaceCHelpFile(filename, mappings, doReplace)


def replaceCHelpFile(filename, mappings, doReplace):
	if filename.endswith('.html') or filename.endswith('.java'):
#		mappings = open(projectPath + 'ooCHelpReferences_finalMapping.csv', 'r', encoding="utf-8")
		mapper = csv.reader(mappings, delimiter='\t', quotechar="'")
		## go though all lines of the file...
		found = 0
		replacement = ''
		with fileinput.FileInput(filename, inplace=False) as file:
			for idx, line in enumerate(file):
				## and check if the line contains a mapped string...
				mappings.seek(0)
				newLine = line
				for cHelpReference in mapper:
					oldValue = cHelpReference[0]
					if oldValue == "Call":
						continue
					newValue = cHelpReference[6]
					newLine = line.replace(oldValue, newValue)
					if (newLine != line):
						found += 1;
						break
				replacement = replacement + newLine

		if found > 0:
			if doReplace:
				print("Replaced cHelp in", filename)
				#shutil.copyfile(filename, filename + '.bak')
				text_file = open(filename, "w")
				text_file.write(replacement)
				text_file.close()
			return (found, filename)
		else:
			return found


###################################

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"l:r:")
	except getopt.GetoptError:
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-l"):
			# Only list found context helps, read-only
			path = ooPath + arg
			if os.path.isdir(path):
				listCHelpDir(path)
			else:
				listCHelpFile(path)
		if opt in ("-r"):
			# Only list found context helps, read-only
			path = ooPath + arg
			mappings = open(projectPath + 'ooCHelpReferences_finalMapping.csv', 'r', encoding="utf-8")
			if os.path.isdir(path):
				replaceCHelpDir(path, mappings, True)
			else:
				replaceCHelpFile(path, mappings, True)
			mappings.close()



if __name__ == "__main__":
	main(sys.argv[1:])
