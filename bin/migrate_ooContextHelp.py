import os, re, sys, fileinput, getopt, shutil, csv, html2text
from os import walk
from urllib.parse import unquote
from pathlib import Path

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

def lookupByPageId(orig):
	idmatch = re.search("pageId=(\d*)", orig)
	if idmatch:
		id = idmatch.group(1)
	path = confluencePath + 'pages/viewpage.action﹖pageId=' + id + '.html'
	if os.path.exists(path):
		file = open(path, "r+", encoding='utf-8', errors='ignore')
		match = re.search('<a href="viewpage.action%EF%B9%96pageId=' + id + '.html">(.*)</a>', file.read())
		if match:
			name = match.group(1)
			return name	
		file.close()
	

def lookupFilename(orig):
	cleaned = unquote(orig)
	cleaned = cleanFilename(cleaned)
	mappings = open(projectPath + 'bin/16.1-mapping.csv', 'r', encoding="utf-8")
	reader = csv.reader(mappings, delimiter=',', quotechar='"')
	for pair in reader:
		de = pair[0]
		en = pair[1]
		if de == '': 
			continue
		if en == '':
			continue
		if cleaned == de:
			newName = cleaned.replace(cleaned, en + '.de')
			newName = newName.replace(' ', '_')
			return newName
		elif cleaned == en:
			newName = cleaned.replace(cleaned, en)
			newName = newName.replace(' ', '_')
			return newName
#		else:
#			print(cleaned)
#			return cleaned


def listCHelpDir(dir, replace):
	export = open("ooCHelpReferences.csv", 'w', newline='', encoding='UTF8')
	writer = csv.writer(export)
	writer.writerow(["Call", "Search", "Page", "Anchor", "NewPage", "NewAnchor", "Replacement"])
	exportNotFount = open("ooCHelpReferences_notFound.csv", 'w', newline='', encoding='UTF8')
	writerNotFound = csv.writer(exportNotFount)
	writerNotFound.writerow(["Call", "Search", "Page", "Anchor", "NewPage", "NewAnchor", "Replacement"])

	for entry in recurse_findDirs(dir):
		filename = entry.path
		if filename.endswith('.html') or filename.endswith('.java'):
			listCHelpFile(filename, replace, writer, writerNotFound)
			
	export.close()

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



def listCHelpFile(filename, replace, writer, writerNotFound):
	allPages = list(findAllPages(projectPath))
	with fileinput.FileInput(filename, inplace=replace) as file:
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


def main(argv):
	try:
		opts, args = getopt.getopt(argv,"l:")
	except getopt.GetoptError:
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-l"):
			# Only list found context helps, read-only
			path = ooPath + arg
			if os.path.isdir(path):
				listCHelpDir(path, False)
			else:
				listCHelpFile(path, False)
			

if __name__ == "__main__":
	main(sys.argv[1:])
