# Externe Werkzeuge: Übersicht {: #ext_tools}

![admin_external_tools_overview_v1_de.png](assets/admin_external_tools_overview_v1_de.png){ class="shadow lightbox aside-left-lg" }


In diesem Bereich können die OpenOlat-Administrator:innen diverse externe Tools ein- und ausschalten (z.B. mehrere virtuelle Klassenzimmer) und je nach Tool bestimmte Basiseinstellungen einrichten, die systemweit gelten.


## BigBlueButton {: #bbb}

BigBlueButton ist eine Software, welche Online-Konferenzen ermöglicht oder als virtueller Klassenraum dienen kann.
Um Webkonferenzen mit BigBlueButton in OpenOlat zu ermöglichen, muss BBB in der Administration aktiviert und konfiguriert worden sein.
 
[Zu den Details >](BigBlueButton_module.de.md)<br>
[Zum Seitenanfang ^](#ext_tools)



## OpenMeetings [:octicons-tag-16:{ title="ab Release 8.3.0 (OO-406)" }](https://track.frentix.com/issue/OO-406){:target="_blank"} {: #openmeetings}

OpenMeetings ist eine Webkonferenz-Lösung.

In der OpenOlat Systemadministration können Sie das OpenMeetings-Modul
konfigurieren und die Funktionalität freischalten. Geben Sie im Tab "Konfiguration" die URL des OpenMeetings-Servers ein, sowie den zuvor in OpenMeetings angelegten Benutzernamen des Webservices und das zugehörige Passwort. Speichern Sie die Daten anschliessend und drücken Sie die Schaltfläche "Serververbindung testen" um die Verbindungsdaten zu überprüfen.

Wenn das Modul eingeschaltet und die Verbindungsparameter zum OpenMeetings-
Server korrekt sind, können in OpenOlat an den folgenden Stellen OpenMeetings-
Räume erzeugt und genutzt werden:

  * In Kursen mit dem Kursbaustein OpenMeetings. Jeder Kursbaustein erzeugt einen entsprechenden Raum auf dem OpenMeetings-Server.
  * In Gruppen mit dem Gruppenwerkzeug OpenMeetings. Jede Gruppe hat ihren eigenen OpenMeetings-Raum zur Verfügung der wie alle anderen Gruppenwerkzeuge verwendet werden kann.

Im Tab "Räume" erhalten Administratoren einen Überblick über die in OpenOlat
angelegten OpenMeetings Räume.

[Zum Seitenanfang ^](#ext_tools)



## Adobe Connect [:octicons-tag-16:{ title="ab Release 14.0 (OO-3887)" }](https://track.frentix.com/issue/OO-3887){:target="_blank"} {: #adobe_connect}

Adobe Connect ist die Webkonferenzlösung aus der Adobe-Produktlinie.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.

[Zum Seitenanfang ^](#ext_tools)



## Microsoft Teams [:octicons-tag-16:{ title="ab Release 15.4 (OO-5124)" }](https://track.frentix.com/issue/OO-5124){:target="_blank"} {: #_microsoft_teams}

Microsoft Teams ist die Webkonferenz-Lösung von Microsoft. Nach der Aktivierung können Autor:innen den [Kursbaustein "Microsoft Teams"](../../manual_user/learningresources/Course_Element_Microsoft_Teams.de.md) in ihren Kursen einsetzen.

**Voraussetzungen für die Aktivierung:**

* Ein Microsoft 365 Tenant (Microsoft Entra ID bzw. Azure) mit den erforderlichen Microsoft Teams Lizenzen.
* Die Zugangsdaten zum Tenant (Application (client) ID, Client secret, Tenant GUID) werden auf Serverebene in der OpenOlat-Konfiguration hinterlegt. Bei gehosteten Instanzen übernimmt dies der frentix Support.

**Voraussetzungen für die Nutzung:**

* Benutzer:innen melden sich in OpenOlat mit ihrem Microsoft-Konto der Organisation an (Azure-Login). Dies ist Voraussetzung, um Meetings eröffnen zu können: OpenOlat erstellt die Online-Termine über die Microsoft Graph API im Namen der angemeldeten Person.

**Konfiguration in der Administration:**

* Modul "Microsoft Teams" aktivieren.
* Unter "Aktivieren für" festlegen, wo Microsoft Teams verwendet werden darf: Kursbaustein "Microsoft Teams", Kurs Termine, Kursbaustein "Terminplanung", Gruppen und Betreuer:innen-Chat.

Zusätzlich stehen in der Administration die Tabs "Online-Termine" (Übersicht aller Termine der Instanz) und "Kalender" (Raumbuchungen) zur Verfügung.

Wie die Rollen Organizer, Presenter und Attendee in einem Teams-Meeting vergeben werden und was die Moderator-Einstellung bewirkt, finden Sie im Benutzerhandbuch im Abschnitt [Rollen in MS Teams](../../manual_user/learningresources/Course_Element_Microsoft_Teams.de.md#teams_roles).

[Zum Seitenanfang ^](#ext_tools)



## Microsoft SharePoint / OneDrive [:octicons-tag-16:{ title="ab Release 19.0.0 (OO-7510)" }](https://track.frentix.com/issue/OO-7510){:target="_blank"} {: #microsoft_sharepoint}

Um im OpenOlat File Hub und OpenOlat Media Center das Schreiben und Kopieren von Dateien von und nach SharePoint und OneDrive zu ermöglichen, müssen diese beiden Tools aktiviert werden. (Sie können einzeln aktiviert werden.)

Voraussetzung ist, dass die erforderlichen Lizenzen vorhanden sind.

[Zu den Details >](SharePoint_OneDrive.de.md)<br>
[Zum Seitenanfang ^](#ext_tools)



## Zoom [:octicons-tag-16:{ title="ab Release 17.0.0 (OO-6187)" }](https://track.frentix.com/issue/OO-6187){:target="_blank"} {: #zoom}

Zoom ist eine Software, in welcher Videokonferenzen, Meetings und Webinare durchgeführt werden können.
Um Zoom Meetings in OpenOlat zu ermöglichen, muss Zoom in der Administration aktiviert und konfiguriert worden sein. 

[Zu den Details >](Zoom.de.md)<br>
[Zum Seitenanfang ^](#ext_tools)



## LTI 1.3 [:octicons-tag-16:{ title="ab Release 15.5.0 (OO-5205)" }](https://track.frentix.com/issue/OO-5205){:target="_blank"} {: #lti}

Hier kann LTI 1.3 aktiviert und näher konfiguriert werden. So können z.B. externe LTI Plattformen und Tools verbunden werden.

[Zu den Details >](LTI_Integrations.de.md)<br>
[Zum Seitenanfang ^](#ext_tools)



## GoToTraining [:octicons-tag-16:{ title="ab Release 10.5 (OO-1944)" }](https://track.frentix.com/issue/OO-1944){:target="_blank"} {: #go_to_training}

GoToTraining ist eine virtuelle Schulungsplattform.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.

[Website GoToTraining >](https://www.goto.de/training)<br>
[Zum Seitenanfang ^](#ext_tools)



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


[Website vitero >](https://www.vitero.com/de)<br>
[Zum Seitenanfang ^](#ext_tools)



## JupyterHub [:octicons-tag-16:{ title="ab Release 18.0.0 (OO-6901)" }](https://track.frentix.com/issue/OO-6901){:target="_blank"} {: #jupyter}

JupyterHub dient der Bereitstellung von Jupyter-Images für Lernende.


[Benutzerhandbuch: Kursbaustein JupyterHub >](../../manual_user/learningresources/Course_Element_JupyterHub.de.md)<br>
[Zum Seitenanfang ^](#ext_tools)



## card2brain [:octicons-tag-16:{ title="ab Release 11.5 (OO-2699)" }](https://track.frentix.com/issue/OO-2699){:target="_blank"} {: #card2brain}

card2brain ist eine Software für das Lernen mit einem Lernkartei-System.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.


[Website card2brain >](https://card2brain.ch/de)<br>
[Zum Seitenanfang ^](#ext_tools)



## Edubase/Edubook [:octicons-tag-16:{ title="ab Release 12.2 (OO-2916)" }](https://track.frentix.com/issue/OO-2916){:target="_blank"} {: #edubase}

Edubase ist eine E-Book-Plattform.

Eine Aktivierung und Konfiguration kann vorgenommen werden, wenn die erforderlichen Lizenzen vorhanden sind.


[Website Edubase >](https://www.edubase.ch)<br>
[Zum Seitenanfang ^](#ext_tools)



## YouTube API [:octicons-tag-16:{ title="ab Release 14.1 (OO-4086)" }](https://track.frentix.com/issue/OO-4086){:target="_blank"} {: #youtube_api}

Eingabe, Entfernung oder Prüfen des API Schlüssels. Der Schlüssel wird verwendet, um beim Einbinden von YouTube-Videos Metadaten wie Titel, Beschreibung und Lizenz automatisch zu übernehmen.

[Zum Seitenanfang ^](#ext_tools)



## Opencast [:octicons-tag-16:{ title="ab Release 15.2 (OO-4836)" }](https://track.frentix.com/issue/OO-4836){:target="_blank"} {: #opencast}

Opencast ist eine Open Source Software zur Planung, Aufzeichnung und Veröffentlichung audiovisueller Lerninhalte, insbesondere für die Aufzeichnung und Distribution von Lehrveranstaltungen.

Nach der Aktivierung können die API-, LTI-Konfiguration vorgenommen werden. Auch BigBlueButton-Recordings aus OpenOlat können verwendet werden.

[Zum Seitenanfang ^](#ext_tools)



## MediaSite [:octicons-tag-16:{ title="ab Release 16.0.4 (OO-5492)" }](https://track.frentix.com/issue/OO-5492){:target="_blank"} {: #mediasite}

Aktivierung von MediaSite. MediaSite ist eine automatisierte Videoplattform
für Videoaufzeichnung, Videomanagement und Untertitelung. Das OpenOlat
Mediasite-Modul ermöglicht es Ihnen, MediaSite-Inhalte als Einzelpräsentation,
Kanal oder Modul in Kurse zu integrieren. 

Das MediaSite-Modul lässt sich über LTI 1.1 oder LTI 1.3 mit dem MediaSite-Server verbinden [:octicons-tag-16:{ title="ab Release 21.0 (OO-9291)" }](https://track.frentix.com/issue/OO-9291){:target="_blank"}. Für LTI 1.3 wählen Sie im Feld **LTI-Version** die Version 1.3 und hinterlegen die Felder **LTI 1.3 Client ID** und **LTI 1.3 Deployment ID** sowie die vom MediaSite-Server benötigten Endpunkt-URLs. Verbindungen über LTI 1.1 bleiben unverändert nutzbar.


[Dokumentation zu MediaSite >](https://mediasite.com/)<br>
[Zum Seitenanfang ^](#ext_tools)



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


[Website edu-sharing >](https://edu-sharing.com/)<br>
[Zum Seitenanfang ^](#ext_tools)



## Dokumenteneditoren [:octicons-tag-16:{ title="ab Release 14.0 (OO-4009)" }](https://track.frentix.com/issue/OO-4009){:target="_blank"} {: #dokumenteneditoren}

Zur Bearbeitung von Office-Dokumenten können in OpenOlat verschiedene Tools verwendet werden:

* ONLYOFFICE
* Microsoft Office

Voraussetzung ist jeweils, dass die erforderlichen Lizenzen vorhanden sind.

[Zum Seitenanfang ^](#ext_tools)



## draw.io [:octicons-tag-16:{ title="ab Release 18.1.0 (OO-7090)" }](https://track.frentix.com/issue/OO-7090){:target="_blank"} {: #draw_io}

draw.io ist ein Online-Werkzeug zur Erstellung von Diagrammen, das in OpenOlat in vielen Stellen eingesetzt werden kann, z.B. in Projekten, im Portfolio, im Kursbaustein "Datei", im Media Center bzw. an vielen Stellen an denen neue Dokumente erstellt werden können. In draw.io können auch mehrere Personen kooperativ an einem Diagramm arbeiten. Um draw.io zu nutzen, muss die Funktion in der Administration eingerichtet werden. 


[Website draw.io >](https://www.drawio.com)<br>
[Zum Seitenanfang ^](#ext_tools)



## Analytics [:octicons-tag-16:{ title="ab Release 12.3 (OO-3243)" }](https://track.frentix.com/issue/OO-3243){:target="_blank"} {: #analytics}

Hier besteht die Möglichkeit, externe Analyse Services zu aktivieren, wie z.B. Google Analytics.

[Zum Seitenanfang ^](#ext_tools)



## KI Modul [:octicons-tag-16:{ title="ab Release 19.0.0 (OO-7787)" }](https://track.frentix.com/issue/OO-7787){:target="_blank"} {: #ai_modul}

Hier aktivieren und konfigurieren Sie die Werkzeuge der Künstlichen Intelligenz, die in OpenOlat eingebunden werden können. 

[Zu den Details >](External_Tools_AI.de.md)<br>
[Zum Seitenanfang ^](#ext_tools)



## PDF Generator [:octicons-tag-16:{ title="ab Release 13.2 (OO-3784)" }](https://track.frentix.com/issue/OO-3784){:target="_blank"} {: #pdf_generator}

In OpenOlat können an verschiedenen Orten PDFs erzeugt werden, z.B. Zertifikate, Testresultate, Mitgliederlisten oder ähnliches. 
Diese Funktionen stehen nur zur Verfügung, wenn ein PDF-Service konfiguriert ist. 


### Gotenberg (empfohlen) [:octicons-tag-16:{ title="ab Release 17.2.4 (OO-6886)" }](https://track.frentix.com/issue/OO-6886){:target="_blank"} {: #gotenberg}

Gotenberg ist ein PDF Generator der auf Google Chrome oder Chromium basiert und es ist Docker basiert.

Mehr Informationen über Gotenberg befinden sich auf [Gotenberg](https://gotenberg.dev/docs/getting-started/introduction) und [GitHub](https://github.com/gotenberg/gotenberg).

Wie Sie den Gotenberg PDF-Service installieren und konfigurieren erfahren Sie im [Installationshandbuch](../installation/gotenbergPdf.md).


### Athena PDF (veraltet) {: #athena}

[AthenaPDF](https://www.athenapdf.com) ist ein
PDF Generator der auf Electron und Docker basiert. Diese Implementation
benutzt den Micro Service Variant. 

Mehr Informationen zu AthenaPDF finden Sie unter
[GitHub](https://github.com/arachnys/athenapdf/tree/master/weaver).

Wie Sie den AthenaPDF-Service installieren und konfigurieren erfahren Sie im [Installationshandbuch](../installation/athenaPdf.md). 

[Zum Seitenanfang ^](#ext_tools)

 

