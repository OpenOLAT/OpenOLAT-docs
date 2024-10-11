# Externe Werkzeuge - Übersicht

![admin_external_tools_overview_v1_de.png](assets/admin_external_tools_overview_v1_de.png){ class="shadow lightbox aside-right-lg" }


In diesem Bereich können die OpenOlat Administrator:innen diverse externe Tools
ein- und ausschalten (z.B. mehrere virtuelle Klassenzimmer) und je nach Tool bestimmte Basiseinstellungen einrichten, die systemweit gelten.

## BigBlueButton {: #bbb}

Um Webkonferenzen mit BigBlueButton in OpenOlat zu ermöglichen, muss BBB in der Administration aktiviert und konfiguriert worden sein.
 
[Zu den Details >](BigBlueButton_module.de.md)


## OpenMeetings {: #openmeetings}

OpenMeetings ist eine Webkonferenz-Lösung.

In der OpenOlat Systemadministration können Sie das OpenMeetings-Modul
konfigurieren und die Funktionalität freischalten. Geben Sie im Tab "Konfiguration" die URL des OpenMeetings-Servers ein, sowie den zuvor in OpenMeetings angelegten Benutzernamen des Webservices und das zugehörige Passwort.  Speichern Sie die Daten anschließend und drücken Sie die Schaltfläche "Serververbindung testen" um die Verbindungsdaten zu überprüfen.

Wenn das Modul eingeschaltet und die Verbindungsparameter zum OpenMeetings-
Server korrekt sind, können in OpenOlat an den folgenden Stellen OpenMeetings-
Räume erzeugt und genutzt werden:

  * In Kursen mit dem Kursbaustein OpenMeetings. Jeder Kursbaustein erzeugt einen entsprechenden Raum auf dem OpenMeetings-Server.
  * In Gruppen mit dem Gruppenwerkzeug OpenMeetings. Jede Gruppe hat ihren eigenen OpenMeetings-Raum zur Verfügung der wie alle anderen Gruppenwerkzeuge verwendet werden kann.

Im Tab "Räume" erhalten Administratoren einen Überblick über die in OpenOlat
angelegten OpenMeetings Räume.


## Adobe Connect {: #adobe_connect}

Adobe Connect ist die Webkonferenzlösung aus der Adobe-Produktlinie.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.


## Microsoft Teams {: #_microsoft_teams}

Die Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.


## Microsoft SharePoint / OneDrive {: #microsoft_sharepoint}

Um im OpenOlat File Hub und OpenOlat Media Center das Schreiben und Kopieren von Dateien von und nach SharePoint und OneDrive zu ermöglichen, müssen diese beiden Tools aktiviert werden. (Sie können einzeln aktiviert werden.)

Voraussetzung ist, dass die erforderlichen Lizenzen vorhanden sind.

[Zu den Details >](SharePoint_OneDrive.de.md)


## Zoom {: #zoom}

Um Zoom Meetings in OpenOlat zu ermöglichen, muss Zoom in der Administration aktiviert und konfiguriert worden sein. 

[Zu den Details >](Zoom.de.md)


## LTI 1.3 {: #lti}

Hier kann LTI 1.3 aktiviert und näher konfiguriert werden. So können z.B. externe LTI Plattformen und Tools verbunden werden.

[Zu den Details >](LTI_Integrations.de.md)


## GoToTraining {: #go_to_training}

GoToTraining ist eine virtuelle Schulungsplattform.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.

**Weitere Informationen:**<br>
[Website GoToTraining](https://www.goto.de/training)


## vitero {: #vitero}

Vitero ist ein Werkzeug zur Durchführung von Webkonferenzen bzw. Online-Meetings.

Um die vitero Anbindung nutzen zu können müssen Sie über eine vitero Lizenz
verfügen und in der Administrationsumgebung folgende Einstellungen vornehmen:

Es muss eine gültige vitero Lizenz vorhanden sein und in der
Administrationsumgebung die Zugangsdaten für das Web Service API eingetragen
werden.

Unter "Zeitzone OLAT Server" können Sie die Zeitzone Ihres OLAT Systems
einstellen. Dies ist notwendig um die Zeiten der Termine mit dem vitero System
abzugleichen.

Die folgenden Angaben erhalten Sie von Ihrem vitero oder OLAT Administrator:
"URL vitero Server", "Web Service Benutzername", "Web Service Passwort" und
"Kundenidentifikator".

Nach erfolgter Eingabe wählen Sie die Schaltfläche "Serververbindung testen"
um die Konfiguration und die Verbindung zum vitero Server zu prüfen. Danach
können Sie die Konfiguration speichern und vitero in Ihren in Ihren Kursen
nutzen.

Bitte beachten Sie, dass für die OpenOlat Anbindung auf dem vitero Server
automatisch Benutzerkonten eingerichtet werden. Allfällige bereits bestehende
Benutzerkonten und Termine werden nicht berücksichtigt.

**Weitere Informationen:**<br>
[Website vitero](https://www.vitero.com/de)


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


## YouTube API {: #youtube_api}

Eingabe, Entfernung oder Prüfen des API Schlüssels.


## Opencast {: #opencast}

Opencast ist eine Open Source Software zur Planung, Aufzeichnung und Veröffentlichung audiovisueller Lerninhalte, insbesondere für die Aufzeichnung und Distribution von Lehrveranstaltungen.

Nach der Aktivierung können die API-, LTI-Konfiguration vorgenommen werden. Auch BigBlueButton-Recordings aus OpenOlat können verwendet werden.


## MediaSite {: #mediasite}

Aktivierung von MediaSite. MediaSite ist eine automatisierte Videoplattform
für Videoaufzeichnung, Videomanagement und Untertitelung. Das OpenOlat
Mediasite-Modul ermöglicht es Ihnen, MediaSite-Inhalte als Einzelpräsentation,
Kanal oder Modul in Kurse zu integrieren. 

**Weitere Informationen:**<br>
[Dokumentation zu MediaSite](https://mediasite.com/)


## edu-sharing {: #edusharing}

Edu-sharing ist eine Software, um Lernplattformen miteinander zu vernetzen, um
Lerninhalte, Metadaten und Tools auszutauschen und in einer Bildungscloud
auffindbar und in allen angeschlossenen Systemen nutzbar zu machen. In der
Administration kann das Modul generell aktiviert und die Nutzung von edu-
sharing als Kursbaustein freigeschaltet werden.

Die Konfiguration erfolgt in vier Schritten:  
1. Konfigurationswerte eingeben und speichern.  
2. Schlüssel generieren und speichern.  
3. Öffentlicher Schlüssel des edu-sharing Repository importieren und
speichern.  
4. In edu-sharing: OpenOlat als Applikation anbinden. URL mit Metadaten:  

	https://your.openolat.domain/olat/edusharing/metadata

**Weitere Informationen:**<br>
[Website edu-sharing](https://edu-sharing.com/)


## Dokumenteneditoren {: #dokumenteneditoren}

Zur Bearbeitung von Office-Dokumenten können in OpenOlat verschiedene Tools verwendet werden:

* ONLYOFFICE
* Microsoft Office

Voraussetzung ist jeweils, dass die erforderlichen Lizenzen vorhanden sind.


## draw.io  {: #draw_io}

draw.io ist ein Online-Werkzeug zur Erstellung von Diagrammen, das in OpenOlat in vielen Stellen eingesetzt werden kann, z.B. in Projekten, im Portfolio, im Kursbaustein "Datei", im Media Center bzw. an vielen Stellen an denen neue Dokumente erstellt werden können. In draw.io können auch mehrere Personen kooperativ an einem Diagramm arbeiten. Um draw.io zu nutzen, muss die Funktion in der Administration eingerichtet werden. 

**Weitere Informationen:**<br>
[Website draw.io](https://www.drawio.com)


## Analytics {: #analytics}

Hier besteht die Möglichkeit, externe Analyse Services zu aktivieren, wie z.B. Google Analytics.


## KI Modul {: #ki_modul}

Hier aktiveren und konfigurieren Sie die Werkzeuge der Künstlichen Intelligenz, die in OpenOlat eingebunden werden können. 


## PDF Generator

In OpenOlat können an verschiedenen Orten PDFs erzeugt werden, z.B. Zertifikate, Testresultate, Mitgliederlisten oder ähnliches. 
Diese Funktionen stehen nur zur Verfügung, wenn einer der untenstehenden PDF-Services konfiguriert ist. 


### Gotenberg (empfohlen)

Gotenberg ist ein PDF Generator der auf Google Chrome oder Chromium basiert und es ist Docker basiert.

Mehr Informationen über Gotenberg befinden sich auf [Gotenberg](https://gotenberg.dev/docs/about) und [GitHub](https://github.com/gotenberg/gotenberg).

Wie Sie den Gotenberg PDF-Service installieren und konfigurieren erfahren Sie im [Installationshandbuch](../installation/gotenbergPdf.md).


### Athena PDF (veraltet)

[AthenaPDF](https://www.athenapdf.com) ist ein
PDF Generator der auf Electron und Docker basiert. Diese Implementation
benutzt den Micro Service Variant. 

Mehr Informationen zu AthenaPDF finden Sie unter
[GitHub](https://github.com/arachnys/athenapdf/tree/master/weaver).

Wie Sie den AthenaPDF-Service installieren und konfigurieren erfahren Sie im [Installationshandbuch](../installation/athenaPdf.md). 

  

