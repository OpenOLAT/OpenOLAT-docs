# OpenOlat documentation
The OpenOlat documentation is based on MkDocs using the material theme and some plugins. The manual is written using the markdown syntax.

### Resources:  
- [https://daringfireball.net/projects/markdown/](https://daringfireball.net/projects/markdown/)
- [https://www.mkdocs.org](https://www.mkdocs.org)
- [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- [https://github.com/backstage/mkdocs-monorepo-plugin](https://github.com/backstage/mkdocs-monorepo-plugin)
- [https://github.com/ultrabug/mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)


## Document structure

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
	- Normal `xyz.md` files are in DE (default)
	- The corresponding EN version have the `xyz.en.md` file ending
	- The same file pattern applies to images as well.
	- For more info see the [static i18n plugin docu](https://github.com/ultrabug/mkdocs-static-i18n)


## Referencing from OpenOlat

OpenOlat uses the page URL including anchors to link to specific areas of the documentation. Thus, changing page names and anchors must be modified in sync with the corresponding references within the OpenOlat code. The URL is derived from the page file name: `about.md` will lead to the URL `..../about/`

The hierarchical structure of URL's is defined in the `mkdocs.yml` file. 


## Manual versions

The manual is published from the GIT master version on the server in the `/current/` directory. Whenever a new main OpenOlat version is published, the documentation is tagged with the same tag and a branch is created. This docu branch is then published in a version directory like `16.1`.


## Install docu development environment

MkDocs uses the Python programming language. You first need to install python3 and pip3 to use MkDocs. 

*MacOS*: there are several ways to to install MkDocs on MacOS, one simple ways is to use the brew package manager. 
To continue you must first install [brew](https://brew.sh).    

	brew install python

1. Install MkDocs   

	pip3 install mkdocs  

2. Install MkDocs theme  

	pip3 install mkdocs-material

2. Install MkDocs plugins  

	pip3 install mkdocs-monorepo-plugin   
	pip3 install mkdocs-static-i18n


## Local development

When editing the files it is recommended to start a local server to preview the changes. The server reloads the pages on every change.

	cd OpenOLAT-docs  
	python3 -m mkdocs serve

Now open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to navigate and preview. 


## Export site as static HTML files

For publishing the documentation, compile it and publish it on your server. 

	cd OpenOLAT-docs
	python3 -m mkdocs build
	cd site
	scp -r ??* www@yourserver:/path/to/your/webserver/docroot/.
