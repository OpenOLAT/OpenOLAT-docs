import os, re, sys, fileinput, getopt, shutil, csv, html2text
from os import walk
from urllib.parse import unquote
from pathlib import Path


def recurse_findDirs(path):
	for entry in os.scandir(path):
		if entry.is_dir(follow_symlinks=False):
			yield from recurse_findDirs(entry.path)
		elif entry.is_file(follow_symlinks=False):
			yield entry
		else:
			raise NotImplemented()


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
	path = '/Users/gnaegi/Desktop/us.sitesucker.mac.sitesucker/confluence.openolat.org/pages/viewpage.action﹖pageId=' + id + '.html'
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
	mappings = open('/Users/gnaegi/OpenOLAT-docs/bin/16.1-mapping.csv', 'r', encoding="utf-8") 
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


def listReferencesDir(dir):
	for entry in recurse_findDirs(dir):
		filename = entry.path
		if filename.endswith('.md') and 'OpenOLAT_16.1_User_Manual' not in filename:
			listReferences(filename)

def listReferences(filename):
	with fileinput.FileInput(filename) as file:
		for idx, line in enumerate(file):
			#(Personal+menu+and+general+components.html) 
			references = re.findall('\(([^\s\)]*)\.(html|md)(#\S*){0,1}\)',line)
			for ref in references:
				# don't change external references
				if (ref[0].startswith('http')):
					continue
				name = os.path.basename(ref[0])
				type = ref[1]
				hash = ''
				if len(ref) > 2:
					hash = ref[2]

				# skip md files for now TODO later
				if type == 'html':
					# fallback to pagees
					if ('viewpage.action' in name):
						name = lookupByPageId(name)

					clean = cleanFilename(name)
					lookup = lookupFilename(clean)
					if (lookup):
						print(filename, type, name, '\t\t', hash, clean, lookup)
#					else:
#						TODO manual treatment


def main(argv):
	assetDir = 'assets/'
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"l")
	except getopt.GetoptError:
		print('migrate_assets.py -l')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-l"):
			path = args[0]
			if os.path.isdir(path):
				listReferencesDir(path)
			else:
				listReferences(path)
			

			

if __name__ == "__main__":
	main(sys.argv[1:])
