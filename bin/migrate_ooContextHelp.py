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
	for entry in recurse_findDirs(dir):
		filename = entry.path
		if filename.endswith('.html') or filename.endswith('.java'):
			listCHelpFile(filename, replace)

def listCHelpFile(filename, replace):
	allPages = list(findAllPages(projectPath))
	with fileinput.FileInput(filename, inplace=replace) as file:
		for idx, line in enumerate(file):
			newline = line
#			print(line)
			#setFormContextHelp(String url)
			#$r.contextHelpWithWrapper("$off_chelp_url")
			#$r.contextHelpJSCommand(String page)
			#$r.contextHelpLink(String page)
			#getManualProvider().getURL(locale, page)
			
#			references = re.findall('(setFormContextHelp\("([^#"]*)[#]{0,1}([^"]*)"\))',line)
#			references = re.findall('(contextHelpWithWrapper\("([^#"]*)[#]{0,1}([^"]*)"\))',line)
#			references = re.findall('(contextHelpJSCommand\("([^#"]*)[#]{0,1}([^"]*)"\))',line)
#			references = re.findall('(contextHelpLink\("([^#"]*)[#]{0,1}([^"]*)"\))',line)
			references = re.findall('(getManualProvider\(\)\.getURL\(\s*[^,]*\s*,\s*"([^#"]*)[#]{0,1}([^"]*)"\))',line)
			for ref in references:
				print(ref)
				'''
				# don't change external references
				if (ref[1].startswith('http')):
					continue
				name = os.path.basename(ref[1])
				type = ref[2]
				hash = ''
				if len(ref) > 2:
					hash = ref[3]

				# skip md files for now TODO later
				if type == 'html':
					# fallback to pagees
					if ('viewpage.action' in name):
						name = lookupByPageId(name)
					if (not name):
						if not replace:
							print("*** ERROR1 ***", ref[0])
#							TODO manual treatment
						continue
					clean = cleanFilename(name)
					lookup = lookupFilename(clean)
					if lookup:
						lookup = lookup + '.md'
						replacementPath = findReplacementPath(filename, lookup, allPages)
						if replacementPath:
							line = line.replace(ref[0],'(' + replacementPath + hash + ')')
							if not replace:
#								print(1,ref[0], ' in ', filename)
#								print(2,replacementPath)
#								print(3,line)
								print(filename, type, name, '\t\t', hash, clean, lookup, replacementPath)
#								print(filename, type, name, '\t\t', hash, clean, lookup)

					elif not replace:
						print("*** ERROR2 ***", ref[0])
#						TODO manual treatment
				'''
			if replace:
				print(line, end='')

def findReplacementPath(filePath, targetPage, allPages):
	print('\n' + filePath + ' §' + targetPage + '§', len(allPages))
	for page in allPages:
		#print(page[len(page)-1])
		if page[len(page)-1] == targetPage:

			file = filePath.split('/')
			myPage = page
			# remove stuff that does not appear in URL
			if 'docs' in file: file.remove('docs')
			if 'sites' in file: file.remove('sites')
			if 'docs' in myPage: myPage.remove('docs')
			if 'sites' in myPage: myPage.remove('sites')
			"""
			print(myPage)
			print(file)
			"""

			newPath = ''
			i = 0
			branched = False
			while i < len(myPage) and i < len(file):
				pageElem = myPage[i]
				fileElem = file[i]
				i += 1
				if fileElem == pageElem and not branched:
					if pageElem == targetPage:
						newPath = targetPage
					else:
						continue
				else:
					branched = True
					if len(newPath) == 0:
						newPath = pageElem
					else:
						newPath = '../' + newPath + '/' + pageElem
			
#			print('XXX', targetPage, newPath)
			return newPath


def main(argv):
	assetDir = 'assets/'
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"l:r:p:")
	except getopt.GetoptError:
		print('migrate_assets.py -l')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-l"):
			# Only list found context helps, read-only
			path = ooPath + arg
			if os.path.isdir(path):
				listCHelpDir(path, False)
			else:
				listCHelpFile(path, False)
		'''
		if opt in ("-r"):
			# Replace found references
			path = arg
			if os.path.isdir(path):
				listReferencesDir(path, True)
			else:
				listReferences(path, True)
		if opt in ("-p"):
			# List all the pages from the dictionary
			path = arg
			if os.path.isdir(path):
				for entry in findAllPages(path):
					print(entry)
		'''

			

if __name__ == "__main__":
	main(sys.argv[1:])
