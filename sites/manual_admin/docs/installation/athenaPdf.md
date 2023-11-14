# Install AthenaPDF


!!! warning
	Please note that AthenaPDF is no longer maintained by its developers. It is recommended to use [Gotenberg](../installation/gotenbergPdf.md) as an alternative PDF service in OpenOlat.

## PDF Service

OpenOlat can generate PDFs, e.g. for downloadable test results documents or certificates. 
In order to generate those PDFs, a PDF service must be installed and properly in the OpenOlat administration section. This page describes hot wo setup 
[AthenaPDF](https://www.athenapdf.com) for this purpose. 

AthenaPDF allows us to use HTML as the description language for PDFs and to style the PDF with simple print CSS rules 
using the powerful Google Chrome render engine. 

A benefit of this approach is that the styling of the generated PDFs can easily be customised using the theme mechanism. 

## Get AthenaPDF

Download [AthenaPDF](https://www.athenapdf.com) from the [AthenaPDF GitHub repository](https://github.com/arachnys/athenapdf/tree/master/weaver).

## Run AthenaPDF in Docker

Start AthenaPDF as a docker container with a command like this:

	docker run --shm-size 2G -p 8090:8080 -d --security-opt seccomp=unconfined -e WEAVER_MAX_CONVERSION_QUEUE=5000 -e WEAVER_MAX_WORKERS=10 -e WEAVER_AUTH_KEY=<my auth key> -e WEAVER_ATHENA_CMD='athenapdf --stdout --delay 5000' --restart always arachnysdocker/athenapdf-service

- `--delay 5000` depends on the complexity of math formulas used in tests when printing test results
- `-d --security-opt seccomp=unconfined-d --security-opt seccomp=unconfined` is of course not recommended but often necessary

Make sure you have enough RAM assigned to the docker container. 

## Configure OpenOlat

Open `Administration > External Tools > PDF generator` 

- The URL is the URL of your docker container
- The key is the `<my auth key>` that you used in the launch command above

![](assets/oo-admin-athenapdf.png){ class="lightbox" }


## Security
 
Make sure the AthenaPDF docker is only reachable by the IP address of your OpenOlat instance and to block all other requests. The PDF service is only
use by OpenOlat to generate the PDF, the delivery of the PDFs is done by OpenOlat. Client never need to call AthenaPDF. 
