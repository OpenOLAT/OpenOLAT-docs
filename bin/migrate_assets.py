import os, re, sys, fileinput, getopt, shutil, csv, html2text
from os import walk
from urllib.parse import unquote


class Converter:
	def __init__(self, out_dir):
		self.__out_dir = out_dir

	def recurse_findfiles(self, path):
		for entry in os.scandir(path):
			if entry.is_dir(follow_symlinks=False):
				yield from self.recurse_findfiles(entry.path)
			elif entry.is_file(follow_symlinks=False):
				yield entry
			else:
				raise NotImplemented()
	
	def convert(self):
		for entry in self.recurse_findfiles(self.__out_dir):
			path = entry.path
			self.convertFile(path)
            
            
	def convertFile(self, path):
		print(path)
		if not path.endswith(".html"):
			return
		
		print("Converting {}".format(path))
		with open(path) as f:
			data = f.read()

		md = html2text.html2text(data)
		newname = os.path.splitext(path)[0]
		with open(newname + ".md", "w") as f:
			f.write(md)


def recurse_findfiles(path):
	for entry in os.scandir(path):
		if entry.is_dir(follow_symlinks=False):
			yield from recurse_findfiles(entry.path)
		elif entry.is_file(follow_symlinks=False):
			yield entry
		else:
			raise NotImplemented()


def previewAssetDetection(sourcedir):
	for entry in recurse_findfiles(sourcedir):
		filename = entry.path
		if (filename.endswith('.md')):
			with fileinput.FileInput(filename) as file:
				for idx, line in enumerate(file):
					attachment = re.findall('../../download/attachments/(\d*)/([^\)]*)\)',line)
					if len(attachment) > 1:
						print(idx,attachment,filename)
					elif attachment:
#						print(attachment[0])
						print(idx,fixFilename(unquote(attachment[0][1])),'\t\t\t', attachment[0])


def fixFilename(filename):
	if '﹖' in filename:
		splitted = filename.split('﹖')
		name = splitted[0]
		ending = splitted[1][-4:]
		return name + ending
	else:
		return filename


def convertMigrateAssets(filename, assetDir, confluenceDownloadDir):
	if not assetDir.endswith('/'):
		assetDir = assetDir + '/'
	if not confluenceDownloadDir.endswith('/'):
		confluenceDownloadDir = confluenceDownloadDir + '/'
	# 1) search all assets
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
		skipRestOfFile = False
		for idx, line in enumerate(file):
			"""
			if idx > 0:
				if line.startswith('### '):
					line = line.replace('### ','#### ')
				elif line.startswith('## '):
					line = line.replace('## ','### ')
				elif line.startswith('# '):
					line = line.replace('# ','## ')
			"""
			attachment = re.search('../../download/(\w*)/(\d*)/([^\)]*)\)',line)
			if attachment:
				type = attachment.group(1)
				number = attachment.group(2)
				assetname = attachment.group(3)
				assetname_spaced = unquote(assetname)
				#print(type, number, assetname)
				# 2) copy all assets
				oldasset_spaced = confluenceDownloadDir + type + '/' + number + '/' + assetname_spaced
				newasset_spaced = assetDir + assetname_spaced
				shutil.copyfile(oldasset_spaced, fixFilename(newasset_spaced))
				# 3) replace asset path in file
				oldasset = '../../download/' + type + '/' + number + '/' + assetname
				newasset = assetDir + fixFilename(assetname)
				print(line.replace(oldasset, newasset), end='')
			else:
				if (line.startswith('  1. [OpenOlat 16.1 Benutzerhandbuch](../OO161DE.html)')):
					skipRestOfFile = True
				elif (line.startswith('  1. [OpenOlat 16.1 User Manual](../OO161EN.html)')):
					skipRestOfFile = True
				if not skipRestOfFile:
					print(line, end='')



def convertMigrateAssetsDirectory(sourcedir, assetDir, confluenceDownloadDir):
	for entry in recurse_findfiles(sourcedir):
		filename = entry.path
		if (filename.endswith('.md')):
			convertMigrateAssets(filename, assetDir, confluenceDownloadDir);

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"d:f:a:p:",["convertdir=","convertfile="])
	except getopt.GetoptError:
		print('migrate_assets.py -h')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('migrate_assets.py -d <directory>')
			print('migrate_assets.py -f <htmlfile>')
			print('migrate_assets.py -a <mdfile> <assetdir> <confluencedownloaddir> ')
			print('migrate_assets.py -a <mddir> <assetdir> <confluencedownloaddir> ')
			sys.exit()
		elif opt in ("-d", "--convertdir"):
			dir = arg
			converter = Converter(out_dir=dir)
			converter.convert()
		elif opt in ("-f", "--convertfile"):
			file = arg
			converter = Converter(out_dir='')
			converter.convertFile(file)
		elif opt in ("-p"):
			dir = arg
			print(dir)
			previewAssetDetection(dir)
		elif opt in ("-a"):
			assetDir = args[0]
			confluenceDownloadDir = args[1]
			if os.path.isdir(arg):
				dir = arg
				convertMigrateAssetsDirectory(dir, assetDir, confluenceDownloadDir)
			else:
				file = arg
				convertMigrateAssets(file, assetDir, confluenceDownloadDir)
			
			
			

if __name__ == "__main__":
	main(sys.argv[1:])
   
   
   
"""
if __name__ == "__main__":
	de_src = 'src/OO161DE' 
	en_src = 'src/OO161EN' 
	de_pages = []
	en_pages = []
	for (dirpath, dirnames, filenames) in walk(de_src):
		de_pages.extend(filenames)
	for (dirpath, dirnames, filenames) in walk(en_src):
		en_pages.extend(filenames)
	
	mappings = open('16.1-mapping.csv', 'r', encoding="utf-8") 
	reader = csv.reader(mappings, delimiter=',', quotechar='"')

##EN
	for page in en_pages:
		# Reset mappings reader for each page loop
		newpage = page
		newpage = newpage.replace('+',' ')
		newpage = newpage.replace('﹕','')
		newpage = newpage.replace(':','')
		newpage = newpage.replace('  ',' ')
		
		# Check if page exists
		if not os.path.isfile(en_src + '/' + page):
			print('Error resolving::' + page + '::')

		newpage = newpage.replace(' ','_')
		shutil.copyfile(en_src + '/' + page, 'target/' + newpage)


## DE
	for page in de_pages:
		# Reset mappings reader for each page loop
		newpage = page
		newpage = newpage.replace('+',' ')
		newpage = newpage.replace('﹕','')
		newpage = newpage.replace(':','')
		newpage = newpage.replace('  ',' ')
		
		mappings.seek(0)
		for pair in reader:
			de = pair[0]
			en = pair[1]
			if de == '': 
				continue
			if en == '':
				continue
			if newpage == de + '.html':
				newpage = newpage.replace(de + '.html', en + '.de.html')
		
		# Check if we missed a page
		if not newpage.endswith('de.html'):
			print(newpage)

		# Check if page exists
		if not os.path.isfile(de_src + '/' + page):
			print('Error resolving::' + page + '::')

		newpage = newpage.replace(' ','_')	
		shutil.copyfile(de_src + '/' + page, 'target/' + newpage)

		# Check if there is also an EN page
		if not os.path.isfile('target/' + newpage.replace('de.html','html')):
			print('Error resolving EN::' + newpage.replace('de.html','html') + '::')

	mappings.close()

	converter = Converter(out_dir='target/')
	converter.convert()
"""

