# External Tools - Overview

![admin_external_tools_overview_v1_de.png](assets/admin_external_tools_overview_v1_de.png){ class="shadow lightbox aside-right-lg" }


In this area, the OpenOlat administrators can switch various external tools on
and off (e.g. several virtual classrooms) and, depending on the tool, configure certain basic settings that
apply system-wide.


## BigBlueButton {: #bbb}

Um Webkonferenzen mit BigBlueButton in OpenOlat zu ermöglichen, muss BBB in der Administration aktiviert und konfiguriert worden sein.
 
[View more details >](BigBlueButton_module.md)


## OpenMeetings {: #openmeetings}

OpenMeetings is a solution for web conferences.

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
  

## Adobe Connect {: #adobe_connect}

Adobe Connect ist die Webkonferenzlösung aus der Adobe-Produktlinie.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.


## Microsoft Teams {: #_microsoft_teams}

Die Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.


## Microsoft SharePoint / OneDrive {: #microsoft_sharepoint}

Um im OpenOlat File Hub und OpenOlat Media Center das Schreiben und Kopieren von Dateien von und nach SharePoint und OneDrive zu ermöglichen, müssen diese beiden Tools aktiviert werden. (Sie können einzeln aktiviert werden.)

Voraussetzung ist, dass die erforderlichen Lizenzen vorhanden sind.

[View more details >](SharePoint_OneDrive.md)


## Zoom {: #zoom}

Um Zoom Meetings in OpenOlat zu ermöglichen, muss Zoom in der Administration aktiviert und konfiguriert worden sein. 

[View more details >](Zoom.md)



## LTI 1.3 {: #lti}

Here LTI 1.3 can be activated and configured in more detail e.g. external LTI
platforms and tools can be connected.

[Further details >](LTI_Integrations.de.md)



## GoToTraining {: #go_to_training}

GoToTraining ist eine virtuelle Schulungsplattform.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.

**Further information:**<br>
[Website GoToTraining](https://www.goto.de/training)



## vitero {: #vitero}

Vitero ist ein Werkzeug zur Durchführung von Webkonferenzen bzw. Online-Meetings.

In order to use the vitero connection, you must have a vitero license and make
the following settings in the administration environment:

A valid vitero license must exist and the access data for the Web Service API
must be entered in the administration environment.

Under "Time Zone OLAT Server" you can set the time zone of your OpenOlat system.
This is necessary to synchronize the times of the appointments with the vitero
system.

You will receive the following information from your vitero or OpenOlat
administrator: "URL vitero server", "Web service username", "Web service
password" and "Customer identifier".

Once you have entered the password, select the "Test server connection" button
to check the configuration and the connection to the vitero server. Then you
can save the configuration and use vitero in your courses.

Please note that user accounts are automatically created for the OLAT
connection on the vitero server. Any existing user accounts and appointments
will not be considered.


**Further information:**<br>
[Website vitero](https://www.vitero.com/)


## JupyterHub {: #jupyter}

JupyterHub dient der Bereitstellung von Jupyter-Images für Lernende.

**Weitere Informationen:**<br>
[Benutzerhandbuch: Kursbaustein JupyterHub](../../manual_user/learningresources/Course_Element_JupyterHub.de.md)


## card2brain {: #card2brain}

card2brain ist eine Software für das Lernen mit einem Lernkartei-System.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.

**Weitere Informationen:**<br>
[Website card2brain](https://card2brain.ch/de)


## Edubase/Edubook {: #edubase}

Edubase ist eine E-Book-Plattform.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.

**Weitere Informationen:**<br>
[Website Edubase](https://www.edubase.ch)



## Youtube API {: #youtube_api}

Enter, remove or check API key.


## Opencast {: #opencast}

Opencast ist eine Open Source Software zur Planung, Aufzeichnung und Veröffentlichung audiovisueller Lerninhalte, insbesondere für die Aufzeichnung und Distribution von Lehrveranstaltungen.

Nach der Aktivierung können die API-, LTI-Konfiguration vorgenommen werden. Auch BigBlueButton-Recordings aus OpenOlat können verwendet werden.


## MediaSite {: #mediasite}

Activation of MediaSite. MediaSite is an automated video platform for video
recording, video management and subtitling. The OpenOlat Mediasite module
allows you to integrate MediaSite content into courses as a single
presentation, channel, or module. 

**Further information:**<br>
[Documentation for MediaSite](https://mediasite.com/)


## edu-sharing {: #edusharing}

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

**Further informationen:**<br>
[Website edu-sharing](https://edu-sharing.com/)



## Dokumenteneditoren {: #dokumenteneditoren}

Zur Bearbeitung von Office-Dokumenten können in OpenOlat verschiedene Tools verwendet werden:

* ONLYOFFICE
* Microsoft Office

Voraussetzung ist jeweils, dass die erforderlichen Lizenzen vorhanden sind.


## draw.io  {: #draw_io}

draw.io ist ein Online-Werkzeug zur Erstellung von Diagrammen, das in OpenOlat z.B. in Projekten genutzt werden kann.Voraussetzung ist die Aktivierung.

**Weitere Informationen:**<br>
[Website draw.io](https://www.drawio.com)


## Analytics {: #analytics}

Possibility to activate external analytics services., e.g. Google Analytics.


## KI Modul {: #ki_modul}

Hier aktiveren und konfigurieren Sie die Werkzeuge der Künstlichen Intelligenz, die in OpenOlat eingebunden werden können. 


## PDF Generator

In OpenOlat PDFs can be created in various places, e.g. certificates, test results, member lists or similar. 
These functions are only available if one of the PDF services below is configured. 


### Gotenberg (recommended)

Gotenberg is a PDF Generator based on Google Chrome or Chromium, and it is docker based.

More information on Gotenberg can be found at [Gotenberg](https://gotenberg.dev/docs/about) and [GitHub](https://github.com/gotenberg/gotenberg).

To learn more about how to install and configure the Gotenberg service please visit the [installation manual](../installation/gotenbergPdf.md)..



### Athena PDF (outdated)

[AthenaPDF](https://www.athenapdf.com) is a PDF generator based on Electron and Docker. This implementation uses the
Variant micro service. 

More information on AthenaPDF can be found at
[GitHub](https://github.com/arachnys/athenapdf/tree/master/weaver).

To learn more about how to install and configure the AthenaPDF service please visit
the [installation manual](../installation/athenaPdf.md). 

