import os, re, sys, fileinput, getopt, shutil, csv, html2text
from os import walk


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
				for line in file:
					attachment = re.findall('../../download/attachments/(\d*)/([^\)]*)\)',line)
					if len(attachment) > 1:
						print(attachment,filename)
					elif attachment:
						print(attachment)



def convertMigrateAssets(filename, targetDir, sourceDir):
	if not targetDir.endswith('/'):
		targetDir = targetDir + '/'
	if not sourceDir.endswith('/'):
		sourceDir = sourceDir + '/'
	# 1) search all assets
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
		for line in file:
			attachment = re.search('../../download/(\w*)/(\d*)/([^\)]*)\)',line)
			if attachment:
				type = attachment.group(1)
				number = attachment.group(2)
				assetname = attachment.group(3)
				assetname_spaced = assetname.replace('%20', ' ').replace('%C3%A4','ä')
				#print(type, number, assetname)
				# 2) copy all assets
				oldasset_spaced = sourceDir + type + '/' + number + '/' + assetname_spaced
				newasset_spaced = targetDir + assetname_spaced
				shutil.copyfile(oldasset_spaced, newasset_spaced)
				# 3) replace asset path in file
				oldasset = '../../download/' + type + '/' + number + '/' + assetname
				newasset = targetDir + assetname
				print(line.replace(oldasset, newasset), end='')
			else:
				print(line, end='')
			# fix header size


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
			print('migrate_assets.py -a <mdfile> <confluencedownloaddir> <assetdir>')
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
			file = arg
			targetDir = args[0]
			sourceDir = args[1]
			convertMigrateAssets(file, targetDir, sourceDir)
			
			
			

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

