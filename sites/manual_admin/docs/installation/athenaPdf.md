# Install AthenaPDF

## PDF Service

OpenOlat can generate PDF's such as downloadable test results overview or certificates to name a few. 

In order to generate those PDF's a PDF service must be installed and configured properly. We use [AthenaPDF](https://www.athenapdf.com) for this purpose. 

AthenaPDF allows us to use HTML as the description language for PDF's and to style the PDF with simple print CSS rules 
using the powerful Google Chrome render engine. 

A benefit of this approach is that the styling of the generated PDF's can easily be customised using the theme mechanism. 

## Get AthenaPDF

[AthenaPDF](https://www.athenapdf.com) can be downloaded from the [AthenaPDF GitHub repository](https://github.com/arachnys/athenapdf/tree/master/weaver).


## Run AthenaPDF in Docker

Start AthenaPDF as a docker container with a command like this:

	docker run -e WEAVER_MAX_CONVERSION_QUEUE=5000 -e WEAVER_MAX_WORKERS=10 -e WEAVER_AUTH_KEY=<my auth key> --restart always arachnysdocker/athenapdf-service

## Configure OpenOlat

Open `Administration > External Tools > PDF generator` 

- The URL is the URL of your docker container
- The key is the `<my auth key>` that you used in the launch command above

![](assets/oo-admin-athenapdf.png){ class="lightbox" }


