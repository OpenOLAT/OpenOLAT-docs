# Externe Werkzeuge - Übersicht

![admin_external_tools_overview_v1_de.png](assets/admin_external_tools_overview_v1_de.png){ class="shadow lightbox aside-right-lg" }


In diesem Bereich können die OpenOlat Administratoren diverse externe Tools
ein- und ausschalten und je nach Tool bestimmte Basiseinstellungen, die
systemweit gelten, einrichten. Zu den Tools gehören mehrere virtuelle
Klassenzimmer sowie Dokumenten Tools, Analyse Werkzeuge und ein PDF Generator.

## BigBlueButton {: #bbb}

[Administrative Konfiguration](BigBlueButton_module.de.md) von BigBlueButton

## OpenMeetings {: #openmeetings}

In der OpenOlat Systemadministration können Sie das OpenMeetings-Modul
konfigurieren und die Funktionalität freischalten. Um das OpenMeetings-Modul
zu konfigurieren, geben Sie in im Tab "Konfiguration" die URL des
OpenMeetings-Servers, sowie den zuvor in OpenMeetings angelegten Benutzernamen
des Webservices und das zugehörige Passwort ein.  Speichern Sie die Daten
anschließend und drücken Sie die Schaltfläche "Serververbindung testen" um die
Verbindungsdaten zu überprüfen.

Wenn das Modul eingeschaltet und die Verbindungsparameter zum OpenMeetings-
Server korrekt sind, können in OpenOlat an den folgenden Stellen OpenMeetings-
Räume erzeugt und genutzt werden:

  * In Kursen mit dem Kursbaustein OpenMeetings. Jeder Kursbaustein erzeugt einen entsprechenden Raum auf dem OpenMeetings-Server.
  * In Gruppen mit dem Gruppenwerkzeug OpenMeetings. Jede Gruppe hat ihren eigenen OpenMeetings-Raum zur Verfügung der wie alle anderen Gruppenwerkzeuge verwendet werden kann.

Im Tab "Räume" erhalten Administratoren einen Überblick über die in OpenOlat
angelegten OpenMeetings Räume.

## Adobe Connect {: #adobe_connect}

Aktivierung und Konfiguration von Adobe Connect, sofern Lizenz vorhanden.

## Microsoft Teams {: #_microsoft_teams}

tbd

## Microsoft SharePoint / OneDrive {: #microsoft_sharepoint}

Um im File Hub das Schreiben und Kopieren von Dateien von und nach SharePoint und OneDrive zu ermöglichen, müssen diese beiden Tools aktiviert werden. (Sie können einzeln aktiviert werden.)


## Zoom {: #zoom}

The Zoom integration lets you manage and start Zoom meetings.

Lerne, wie man die [Zoom Integration aktiviert und konfiguriert](Zoom.de.md). 

## LTI 1.3 {: #lti}

Hier kann LTI 1.3 aktiviert und näher konfiguriert werden z.B. können externe
LTI Plattformen und Tools verbunden werden.

Diese LTI Version befindet sich aktuell in der Versuchsphase.

## GoToTraining {: #go_to_training}

Aktivierung und Konfiguration sofern Lizenz vorhanden.

## vitero {: #vitero}

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

## JupyterHub {: #jupyter}

tbd

## card2brain {: #card2brain}

tbd

## Edubase/Edubook {: #edubase}

Aktivierung und Konfiguration sofern Lizenz vorhanden.

## Youtube API {: #youtube_api}

Eingabe, Entfernung oder Prüfen des API Schlüssels.

## Opencast {: #opencast}

Aktivierung und Konfiguration sofern Lizenz vorhanden

## MediaSite {: #mediasite}

Aktivierung von MediaSite. MediaSite ist eine automatisierte Videoplattform
für Videoaufzeichnung, Videomanagement und Untertitelung. Das OpenOlat
Mediasite-Modul ermöglicht es Ihnen, MediaSite-Inhalte als Einzelpräsentation,
Kanal oder Modul in Kurse zu integrieren. Weitere Informationen finden Sie in
der Dokumentation von [MediaSite](https://mediasite.com/).

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

Weitere Information sind auf der [Webseite](https://edu-sharing.com/) von edu-
sharing zu finden.

## Dokumenteneditoren {: #dokumenteneditoren}

tbd

## draw.io  {: #draw_io}

tbd

## Analytics {: #analytics}

Möglichkeit, externe Analyse Services zu aktivieren.

## KI Modul {: #ki_modul}

tbd

## PDF Generator

In OpenOlat können an verschiedenen Orten PDFs erzeugt werden, z.B. Zertifikate, Testresultatet, Mitgliederlisten oder ähnliches. 
Diese Funktionen stehen nur zur Verfügung, wenn einer der untenstehenden PDF Servcies konfiguriert ist. 

### Gotenberg (empfohlen)

Gotenberg ist ein PDF Generator der auf Google Chrome oder Chromium basiert und es ist Docker basiert.

Mehr Informationen über Gotenberg befinden sich auf [Gotenberg](https://gotenberg.dev/docs/about) und [GitHub](https://github.com/gotenberg/gotenberg).

Wie Sie den AthenaPDF-Service installieren und konfigurieren erfahren Sie im [Installationshandbuch](../installation/gotenbergPdf.md).

### Athena PDF (veraltet)

[AthenaPDF](https://www.athenapdf.com) ist ein
PDF Generator der auf Electron und Docker basiert. Diese Implementation
benutzt den Micro Service Variant. 

Mehr Informationen zu AthenaPDF finden Sie unter
[GitHub](https://github.com/arachnys/athenapdf/tree/master/weaver).

Wie Sie den AthenaPDF-Service installieren und konfigurieren erfahren Sie im [Installationshandbuch](../installation/athenaPdf.md). 

  

