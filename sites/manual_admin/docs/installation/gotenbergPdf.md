# Install Gotenberg PDF

## PDF Service

OpenOlat can generate PDFs, e.g. for downloadable test results documents or certificates. 
In order to generate those PDFs, a PDF service must be installed and properly in the OpenOlat administration section. 
We use [Gotenberg](https://gotenberg.dev/docs/about) for this purpose. 


[Gotenberg](https://gotenberg.dev/docs/about) is a Docker-powered stateless API for PDF files containing all required dependencies in it's docker image.

It scales smoothly and works nicely in a distributed context. It provides multipart/form-data endpoints for converting numerous document formats into PDF files.

## Run Gotenberg in Docker

Start Gotenberg as a docker container with a command similar to this:

`docker run -itd -p 8080:3000 --restart always gotenberg/gotenberg:7`

This will download everything necessary, and start the container which will then be reachable on port 8080.

## Configure OpenOlat

Open `Administration > External Tools > PDF generator`

Choose Gotenberg as Generator. The URL is the URL of your docker container and port.

## Security

Make sure the Gotenberg docker container is only reachable by the IP address of your OpenOlat instance, all other requests should be blocked. The PDF service is only used by OpenOlat to generate the PDF, the delivery of the PDFs is done by OpenOlat. Clients never need to call Gotenberg directly.
