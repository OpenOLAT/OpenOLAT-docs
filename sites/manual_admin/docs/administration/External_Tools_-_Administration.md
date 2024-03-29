# External Tools - Administration

![](assets/externe_Werkzeuge_16.png){ class="shadow lightbox aside-right-lg" }

In this area, the OpenOlat administrators can switch various external tools on
and off and, depending on the tool, configure certain basic settings that
apply system-wide. The tools include several virtual classrooms as well as
document tools, analysis tools and a PDF generator.

## BigBlueButton

[BigBlueButton module](BigBlueButton_module.md)

## OpenMeetings

In the OpenOlat system administration you can configure the OpenMeetings
module and activate the functionality. To configure the OpenMeetings module,
enter the URL of the OpenMeetings server in the tab "Configuration", as well
as the username of the web service previously created in OpenMeetings and the
corresponding password. Then save the data and press the "Check the
connection" button to check the connection data.

If the module is switched on and the connection parameters to the OpenMeetings
server are correct, OpenOlat can create and use OpenMeetings rooms in the
following locations:

  * In courses with the course element OpenMeetings. Each course element creates a corresponding room on the OpenMeetings server.
  * In groups with the OpenMeetings group tool. Each group has its own OpenMeetings room that can be used like any other group tool.

The tab "Rooms" gives administrators an overview of the OpenMeetings rooms
created in OpenOlat.
  

## Adobe Connect

Activation and configuration of Adobe Connect, if license available.

## Zoom

The Zoom integration lets you manage and start Zoom meetings.

Learn how to [activate and configure the Zoom integration](Zoom.md). 

## LTI 1.3

Here LTI 1.3 can be activated and configured in more detail e.g. external LTI
platforms and tools can be connected.

This LTI version is currently in the trial phase.

## GoToTraining

Activation and configuration if license available.

## vitero {: #vitero}

In order to use the vitero connection, you must have a vitero license and make
the following settings in the administration environment:

A valid vitero license must exist and the access data for the Web Service API
must be entered in the administration environment.

Under "Time Zone OLAT Server" you can set the time zone of your OLAT system.
This is necessary to synchronize the times of the appointments with the vitero
system.

You will receive the following information from your vitero or OLAT
administrator: "URL vitero server", "Web service username", "Web service
password" and "Customer identifier".

Once you have entered the password, select the "Test server connection" button
to check the configuration and the connection to the vitero server. Then you
can save the configuration and use vitero in your courses.

Please note that user accounts are automatically created for the OLAT
connection on the vitero server. Any existing user accounts and appointments
will not be considered.

## Edubase/Edubook

Activation and configuration if license available.

## Youtube API

Enter, remove or check API key.

## MediaSite

Activation of MediaSite. MediaSite is an automated video platform for video
recording, video management and subtitling. The OpenOlat Mediasite module
allows you to integrate MediaSite content into courses as a single
presentation, channel, or module. For more information, see the
[MediaSite](https://mediasite.com/) documentation.

## edu-sharing

Edu-sharing is a software for networking learning platforms, exchanging
learning content, metadata and tools and making them searchable in an
education cloud and usable in all connected systems. In the administration the
module can be activated in general and the use of edu-sharing as course
element can be enabled.

Configuration takes place in four steps:  
1. Enter and save configuration values.  
2. Generate and save keys.  
3. Import and save the edu-sharing repositoiry public key.  
4. In edu-sharing: Connect OpenOlat as an application. URL with metadata:  

	https://your.openolat.domain/olat/edusharing/metadata

Further information can be found on the [website](https://edu-sharing.com/) of
edu-sharing.

## Analytics

Possibility to activate external analytics services.

## PDF Generator

In OpenOlat PDFs can be created in various places, e.g. certificates, test results, member lists or similar. 
These functions are only available if one of the PDF services below is configured. 

### Gotenberg (recommended)

Gotenberg is a PDF Generator based on Google Chrome or Chromium, and it is docker based.

More information on Gotenberg can be found at [Gotenberg](https://gotenberg.dev/docs/about) and [GitHub](https://github.com/gotenberg/gotenberg).

To learn more about how to install and configure the Gotenberg service please visit the [installation manual](../installation/gotenbergPdf.md)..



### Athena PDF (outdated)

AthenaPDF is a
PDF generator based on Electron and Docker. This implementation uses the
Variant micro service. 

More information on AthenaPDF can be found at
[GitHub](https://github.com/arachnys/athenapdf/tree/master/weaver).

To learn more about how to install and configure the AthenaPDF service please visit
the [installation manual](../installation/athenaPdf.md). 


