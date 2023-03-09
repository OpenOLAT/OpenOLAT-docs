# Install imageMagick

## Image Thumbnail Service

OpenOlat can generate preview thumbnail images for PDFs etc. The preview images are shown in various places, for example in the folder component. 

The thumbnail service works out-of-the box in a vanilla OpenOlat installation using a java based implementation. 
However, this default installation has its limits: for example, it can not create thumbails for PDF files and when resizing images that uses alpha transparency, the transparency is lost. And after all, the java implementation is slow. 
For best user experience it is thus recommended to delegate the image resize task to a service that runs natively in the operating system. 
We use the well known linux tool **imageMagick** in combination with **ghostscript** for this. 

## Get imageMagick and Ghostscript

Depending on your system, download imageMagick and ghostscript from their websites:
- [imageMagick](https://imagemagick.org)
- [ghostscript](https://www.ghostscript.com)

On apt based systems (Debian, Ubuntu..) install the tools as follows:

	apt update
	apt install imagemagick ghostscript


## Adjust the read/write policy for PDF files

To create thumbnails from PDFs it is necessary to configure imageMagick. Depending on the version of ImageMagick, edit the corresponding policy.xml, either with the command

	nano /etc/ImageMagick-6/policy.xml

or

	nano /etc/ImageMagick-7/policy.xml

In this file, search for the line

`<policy domain="coder" rights="none" pattern="PDF" />`

and change the rights from **none** to **read|write**

`<policy domain="coder" rights="read|write" pattern="PDF" />`


## Configure OpenOlat

In your `olat.local.properties` enable the imageMagick thumbnail provider: 

	thumbnail.provider=magick
	thumbnail.magick.path=/usr/bin/

Adjust the path `/usr/bin` to wherever you installed imageMagick. 


!!! tip
	Don't forget to restart OpenOlat to activate the service. 