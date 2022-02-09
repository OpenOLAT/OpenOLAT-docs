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


def previewAssetDetection(sourcedir, confluenceDownloadDir):
	for entry in recurse_findfiles(sourcedir):
		filename = entry.path
		if (filename.endswith('.md')):
			with fileinput.FileInput(filename) as file:
				for idx, line in enumerate(file):
					attachment = re.findall('\(((../)*)download/(.*)/(\d*)/([^\)]*)\)',line)
					if len(attachment) > 1:
						print(idx,attachment,filename)
					elif attachment:
						fullPath = confluenceDownloadDir + '/' + attachment[0][2] + '/' + attachment[0][3] + '/' + unquote(unquote(attachment[0][4]))
						exists = os.path.exists(fullPath)
						if (not exists) :
							print('*** NOT FOUND', filename, fullPath)
						else :
							print(idx,fixFilename(unquote(attachment[0][4])),'\t\t\t', attachment[0])



def fixAllHeadersAndFooters(sourcedir):
	for entry in recurse_findfiles(sourcedir):
		filename = entry.path
		if (filename.endswith('.md')):
			fixHeaderAndFooter(filename)

def fixHeaderAndFooter(filename):
	with fileinput.FileInput(filename, inplace=True) as file:
		skipRestOfFile = False
		for idx, line in enumerate(file):
			if idx == 0:
				if line.startswith('# '):
					line = line.replace('# ','## ')
					title = re.search('^#.*\[(.*)\].*\(.*\)$',line)
					if title:
						print('# ' + title.group(1))
					else:
						print(line, end='')
			else:
				if (line.startswith('  1. [OpenOlat 16.1 Benutzerhandbuch](../OO161DE.html)')):
					skipRestOfFile = True
				elif (line.startswith('  1. [OpenOlat 16.1 User Manual](../OO161EN.html)')):
					skipRestOfFile = True
				if not skipRestOfFile:
					print(line, end='')


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
	os.makedirs(assetDir, exist_ok=True)
	os.makedirs(assetDir + '../bak', exist_ok=True)
	# 1) search all assets
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
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
			attachment = re.search('\(((../)*)download/(\w*)/(\d*)/([^\)]*)\)',line)
			if attachment:
				type = attachment.group(3)
				number = attachment.group(4)
				assetname = attachment.group(5)
				assetname_spaced = unquote(assetname)
				#print(type, number, assetname)
				# 2) copy all assets
				oldasset_spaced = confluenceDownloadDir + type + '/' + number + '/' + assetname_spaced
				newasset_spaced = fixFilename(assetDir + assetname_spaced)
				shutil.copyfile(oldasset_spaced, newasset_spaced)
				# 3) replace asset path in file
				oldasset = attachment.group(1) + 'download/' + type + '/' + number + '/' + assetname
				print(line.replace(oldasset, newasset_spaced), end='')
			else:
				print(line, end='')


def convertMigrateAssetsDirectory(sourcedir, assetDir, confluenceDownloadDir):
	for entry in recurse_findfiles(sourcedir):
		filename = entry.path
		if (filename.endswith('.md')):
			convertMigrateAssets(filename, assetDir, confluenceDownloadDir);


def copyMissingPage(pageId, pageName, assetDir, confluenceDownloadDir):
	if not confluenceDownloadDir.endswith('/'):
		confluenceDownloadDir = confluenceDownloadDir + '/'
	pageDir = confluenceDownloadDir + '../pages/'
	pagePath = pageDir + 'viewpage.action﹖pageId=' + pageId + '.html'
	targetPath = pageName
	if os.path.exists(pagePath) :
		with open(pagePath) as f:
			data = f.read()
			md = html2text.html2text(data)
		with open(targetPath, "w") as f:
			f.write(md)
		os.system("open -a BBEdit " + targetPath)
	else :
		print('page does not exist::', pagePath)


def main(argv):
#	confluenceDownloadDir = '/Users/gnaegi/Desktop/us.sitesucker.mac.sitesucker/confluence.openolat.org/download'
	confluenceDownloadDir = '/Users/gnaegi/Desktop/us.sitesucker.mac.sitesucker_full/confluence.openolat.org/download'
	assetDir = 'assets/'
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"m:M:d:f:a:p:h:H:i:")
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
		elif opt in ("-m"):
			#Convert file to Markdown
			file = arg
			converter = Converter(out_dir='')
			converter.convertFile(file)
		elif opt in ("-M"):
			#Convert files in directory to Markdown
			dir = arg
			converter = Converter(out_dir=dir)
			converter.convert()
		elif opt in ("-p"):
			#Preview asset migration
			dir = arg
			print(dir)
			previewAssetDetection(dir, confluenceDownloadDir)
		elif opt in ("-a"):
			#Migrate assets for files or directories
			if os.path.isdir(arg):
				dir = arg
				convertMigrateAssetsDirectory(dir, assetDir, confluenceDownloadDir)
			else:
				file = arg
				convertMigrateAssets(file, assetDir, confluenceDownloadDir)
		elif opt in ("-h"):
			# Fix header for single file
			file = arg
			fixHeaderAndFooter(file)
		elif opt in ("-H"):
			# Fix headers for all files in directory
			dir = arg
			fixAllHeadersAndFooters(dir)
		elif opt in ("-i"):
			# copy missing page by giving and id
			id = argv[1]
			name = argv[2]
			copyMissingPage(id, name, assetDir, confluenceDownloadDir)

			

if __name__ == "__main__":
	main(sys.argv[1:])
