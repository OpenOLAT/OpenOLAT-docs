# OpenOlat documentation
The OpenOlat documentation is based on MkDocs using the material theme and some plugins. The manual is written using the markdown syntax.

### Resources:  
- [https://daringfireball.net/projects/markdown/](https://daringfireball.net/projects/markdown/)
- [https://www.mkdocs.org](https://www.mkdocs.org)
- [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- [https://github.com/backstage/mkdocs-monorepo-plugin](https://github.com/backstage/mkdocs-monorepo-plugin)
- [https://github.com/ultrabug/mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)


## File structure

- Landing page:
	- The page structure is defined in the `mkdocs.yml` file within the space
	- Page files are located in `/docs/`
- Sites
	- Contains all the manual sections (release notes, user manual, admin manual tech doc etc)
	- Each site 
	- The page structure is defined in the `mkdocs.yml`file within the space
	- Page files are located in `/docs/` folder within the site
	- For more info see the [monorepo plugin docu](https://github.com/backstage/mkdocs-monorepo-plugin)
- i18n
	- Normal `xyz.md` files are in EN (default) since not all spaces are available in all languages
	- The corresponding DE version have the `xyz.de.md` file ending
	- The same file pattern applies to images as well.
	- For more info see the [static i18n plugin docu](https://github.com/ultrabug/mkdocs-static-i18n)


## Referencing from OpenOlat

OpenOlat uses the page URL including anchors to link to specific areas of the documentation. Thus, changing page names and anchors must be modified in sync with the corresponding references within the OpenOlat code. The URL is derived from the page file name: `about.md` will lead to the URL `..../about/`. 

Normally markdown generates HTML anchors for each title element automatically. This is unhandy when writing a multi-language documentation where not only the link to pages but also the link to the dedicated chapter in the page must be linkable from OpenOlat. Thus, the anchors must be set explicitly using the `attr-listattr-list` markdown extension:
 
	# This is a title {: #this-is-the-anchor-to-this-title }
 

The hierarchical structure of URL's is defined in the `mkdocs.yml` file. 


## Manual versions

The manual is published from the GIT master version on the server in the `/current/` directory. Whenever a new main OpenOlat version is published, the documentation is tagged with the same tag and a branch is created. This docu branch is then published in a version directory like `16.1`.


## Working on the documentation


### Install docu development environment

MkDocs uses the Python programming language. You first need to install python3 and pip3 to use MkDocs. 

*MacOS*: there are several ways to to install MkDocs on MacOS, one simple ways is to use the brew package manager. 
To continue you must first install [brew](https://brew.sh).    

	# Basic Python 3 installation
	brew install python
	
	# Install MkDocs
	pip3 install mkdocs

	#Install MkDocs theme and plugins
	pip3 install mkdocs-material
	pip3 install mkdocs-monorepo-plugin   
	pip3 install mkdocs-static-i18n


### Editors

Any Markdown editor can be used. 

On the Mac the macdown tool is pretty handy and simple to install:

	brew install --cask macdown
	open -a MacDown

### Repository access

TBD


### Local preview

When editing the files it is recommended to start a local server to preview the changes. The server reloads the pages on every change.

	cd OpenOLAT-docs  
	python3 -m mkdocs serve

Now open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to navigate and preview. 


### Export site as static HTML files

For publishing the documentation, compile it and publish it on your server. 

	cd OpenOLAT-docs
	python3 -m mkdocs build
	cd site
	scp -r ??* www@yourserver:/path/to/your/webserver/docroot/.
