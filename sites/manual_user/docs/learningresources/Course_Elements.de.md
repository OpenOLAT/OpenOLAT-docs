# Kursbausteine

:octicons-device-camera-video-24: **Video-Einführung**: [Was sind Kursbausteine?](<https://www.youtube.com/embed/JM6iSrfkHog>){:target="_blank”}

:octicons-device-camera-video-24: **Video-Einführung**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank”}

In OpenOlat stehen verschiedene Kursbausteine zur Verfügung, mit denen ein Kurs sehr flexibel und modular nach den gewünschten Bedürfnissen aufgebaut werden kann. So können Kursinhalte strukturiert und Inhalte bereitgestellt, kollaboratives Arbeiten und Austausch gefördert, der Wissenstand der Teilnehmenden geprüft sowie organisatorische Belange abgedeckt werden.

## Kursbausteine im Überblick

### Wissensvermittlung

Die folgenden Kursbausteine dienen insbesondere der Bereitstellung und Strukturierung von Kursinhalten. Je nach Baustein können auch bestimmte, extern erstellte Inhalte eingebunden werden.

<!--    [![single page icon](assets/single_page_icon.png){ class=size16 } HTML-Seite](Course_Element_Single_Page.de.md)-->

* [:fontawesome-solid-cubes: Struktur](Course_Element_Structure.de.md)
* [:fontawesome-solid-file-lines: Seite](Course_Element_Page.de.md)
* [:fontawesome-regular-file-lines: HTML-Seite](Course_Element_HTML_Page.de.md)
* [:fontawesome-solid-up-right-from-square: Externe Seite](Course_Element_External_Page.de.md)
* [:fontawesome-solid-box-archive: CP-Lerninhalt](Course_Element_CP_Learning_Content.de.md)
* [:fontawesome-solid-box-archive: SCORM-Lerninhalt](Course_Element_SCORM_Learning_Content.de.md)
* [:fontawesome-regular-file: Dokument](Course_Element_Document.de.md)
* [:fontawesome-regular-folder-open: Ordner](Course_Element_Folder.de.md)
* [:fontawesome-solid-video: Podcast](Course_Element_Podcast.de.md)
* [:fontawesome-solid-bullhorn: Blog](Course_Element_Blog.de.md)
* [:fontawesome-solid-film: Video](Course_Element_Video.de.md)
* [:fontawesome-solid-video: Video Livestream](Course_Element_Video_Livestream.de.md)
* [:octicons-arrow-right-24: Opencast](Course_Element_Opencast.de.md)
* [:octicons-arrow-right-24: edu-sharing](Course_Element_edu_Sharing.de.md)
* [:octicons-arrow-right-24: card2brain](Course_Element_card2brain_Flashcards.de.md)
* [:octicons-arrow-right-24: MediaSite](Course_Element_Mediasite.de.md)
* [:octicons-arrow-right-24: Edubase](Course_Element_Edubase.de.md)
* [:simple-jupyter: JupyterHub](Course_Element_JupyterHub.de.md)

### Wissensüberprüfung

Folgende Kursbausteine können insbesondere zur Wissensüberprüfung eingesetzt werden.

* [:fontawesome-regular-thumbs-up: Bewertung](Course_Element_Assessment.de.md)
* [:fontawesome-solid-bars-progress: Aufgabe](Course_Element_Task.de.md)
* [:fontawesome-solid-bars-progress: Gruppenaufgabe](Course_Element_Grouptask.de.md)
* [:fontawesome-solid-briefcase: Portfolioaufgabe](Course_Element_Portfolio_Task.de.md)
* [:fontawesome-solid-square-pen: Test](Course_Element_Test.de.md)
* [:fontawesome-solid-square-pen: Selbsttest](Course_Element_Self_Test.de.md)
* [:fontawesome-solid-futbol: Übung](Course_Element_Practice.de.md)
* [:octicons-arrow-right-24: Video-Aufgabe](Course_Element_Video_Task.de.md)
* [:material-clipboard-file-outline: Formular](Course_Element_Form.de.md)
* [:fontawesome-solid-sliders: Umfrage](Course_Element_Survey.de.md)
* [:fontawesome-regular-square-check: Checkliste](Course_Element_Checklist.de.md)

Die meisten Kursbausteine der Kategorie Wissensüberprüfung sind bewertbar und es können bei Bedarf Punkte vergeben werden. Dann können weitere Features wie die Addition von Punkten oder die Berechnung von Bestanden / Nicht bestanden für den Kurs, basierend auf den Bewertungen verschiedener Kursbausteine, hinzugefügt werden. Die Berechnung bei herkömmlichen Kursen erfolgt über den Kursbaustein [Struktur](Course_Element_Structure.de.md) bzw. am obersten Kursknoten.

Das Konfigurationstab "Erinnerungen" steht für alle bewertbaren Bausteine der Wissensüberprüfung zur Verfügung. Hier können in Abhängigkeit vom Bearbeitungsstatus des jeweiligen Kursbausteins E-Mails verschickt werden, z.B. wenn zu einem bestimmten Datum eine Aufgabe oder ein Test noch nicht bearbeitet wurde. Die Möglichkeiten sind ähnlich wie im Menü ["Erinnerung"](../learningresources/Course_Reminders.de.md) in der Kurs-Administration.

Unter der Kategorie Wissensüberprüfung sind ausserdem die Kursbausteine "Umfrage" und "Formular" zugeordnet. Diese ermöglichen die Einbindung von OpenOlat [Formularen](../learningresources/Form_Editor.de.md) in den Kurs, um diese für Unterrichtsevaluationen, allgemeine Befragungen, strukturierte Abfragen bestimmter Informationen der Teilnehmenden usw. zu nutzen.

#### Highscore {: #highscore}

Alle bewertbaren Kursbausteine, mit Ausnahme von "Übung" und "Struktur", erhalten zusätzlich das Konfigurationstab "Highscore", wenn am Baustein Punkte vergeben werden. Die Highscore-Darstellung ermöglicht einen spielerischen Vergleich der Teilnehmenden und kann als Motivationsfaktor verstanden werden.

Zuerst muss "Highscore anzeigen" aktiviert werden. Optional kann ein Anfangsdatum hinzugefügt werden, ab welchem der Highscore angezeigt wird. Ohne Angabe des Datums wird der Highscore direkt nach Beenden des Tests angezeigt.

Es kann definiert werden, ob die Benutzerdaten anonymisiert oder mit Vor- und Nachnamen dargestellt werden und welche Elemente des Highscores angezeigt werden sollen. Zur Auswahl stehen die Positionsanzeige, das Siegertreppchen, das Histogramm und die Liste der besten Teilnehmer. Für die Liste kann zudem definiert werden, ob alle Benutzer oder nur eine gewisse Anzahl der besten Benutzer erscheinen sollen. Es muss mindestens eine dieser Optionen ausgewählt werden.

![Highscore](assets/Highscore.png)

### Kommunikation und Kollaboration

Kursbausteine dieser Kategorie werden vor allem für kollaboratives Arbeiten und den Austausch untereinander eingesetzt. Hier sind auch die Bausteine für virtuelle Klassenräume und Online-Meetings zugeordnet.

* [:fontawesome-solid-earth-americas: Wiki](Course_Element_Wiki.de.md)
* [:fontawesome-regular-comments: Forum](Course_Element_Forum.de.md)
* [:material-file-multiple-outline: Dateidiskussion](Course_Element_File_Dialog.de.md)
* [:fontawesome-solid-inbox: Teilnehmer Ordner](Course_Element_Participant_Folder.de.md)
* [:fontawesome-solid-users: Teilnehmerliste](Course_Element_Participant_List.de.md)
* [:fontawesome-solid-desktop: Vitero](Course_Element_vitero.de.md)
* [:fontawesome-solid-desktop: OpenMeetings](Course_Element_OpenMeetings.de.md)
* [:fontawesome-solid-desktop: Adobe Connect](Course_Element_Adobe_Connect.de.md)
* [:fontawesome-solid-desktop: GoToMeeting](Course_Element_GoToMeeting.de.md)
* [:fontawesome-solid-desktop: BigBlueButton](Course_Element_BigBlueButton.de.md)
* [:fontawesome-solid-desktop: Microsoft Teams](Course_Element_Microsoft_Teams.de.md)
* [:fontawesome-solid-desktop: Zoom](Course_Element_Zoom.de.md)

#### Virtuelle Räume

![](assets/vitero.png)

Mit den Kursbausteinen 
[Adobe Connect](Course_Element_Adobe_Connect.de.md), [BigBlueButton](Course_Element_BigBlueButton.de.md), [GoToMeeting](Course_Element_GoToMeeting.de.md), [Microsoft Teams](Course_Element_Microsoft_Teams.de.md), [OpenMeetings](Course_Element_OpenMeetings.de.md), [Vitero](Course_Element_vitero.de.md) und [Zoom](Course_Element_Zoom.de.md) können in OpenOlat unterschiedliche [Virtuelle Klassenzimmer](../course_elements/Virtual_classrooms.de.md) für synchrone Meetings, Video-Konferenzen oder Webinare eingesetzt werden.

Welche Kursbausteine für diese Zwecke verfügbar sind und welche Funktionalitäten jeweils zur Verfügung stehen, hängt von der Konfiguration ihres OpenOlat-Systems ab.

Ein virtueller Raum ermöglicht es, gleichzeitig (synchron) online mit mehreren Personen zusammen zu arbeiten, die geographisch an unterschiedlichen Orten sind. Funktionen von virtuellen Räumen sind unter anderem Live Chat, Audio und Video, Desktop- und Dokumentsharing. Wird ein virtueller Raum mittels eines Kursbausteins betreten, öffnet sich ein neues Browserfenster, in dem die virtuelle Sitzung stattfindet.

Damit Sie alle Funktionalitäten benutzen können, benötigen Sie ein Headset und eine angeschlossene Kamera. Unter Umständen muss, abhängig vom eingesetzten System, noch weitere Software temporär heruntergeladen werden.

### Verwaltung und Organisation

Für organisatorische Belange und zur Verteilung von Informationen eignen sich besonders die nachfolgenden Kursbaussteine.

* [:fontawesome-solid-right-to-bracket: Einschreibung](Course_Element_Enrolment.de.md)
* [:fontawesome-solid-circle-info: Mitteilungen](Course_Element_Notifications.de.md)
* [:fontawesome-regular-envelope: E-Mail](Course_Element_EMail.de.md)
* [:fontawesome-solid-clipboard-list: Themenbörse](Course_Element_Topic_Broker.de.md)
* [:fontawesome-regular-calendar-days: Kalender](Course_Element_Calendar.de.md)
* [:fontawesome-regular-calendar: Terminplanung](Course_Element_Appointment_Scheduling.de.md)

### Andere

Zusätzliche Bausteine finden Sie in der Kategorie "Andere".

* [:fontawesome-solid-up-right-from-square: LTI-Seite](Course_Element_LTI_Page.de.md)
* [:fontawesome-regular-circle: Themenvergabe](Course_Element_Topic_Assignment.de.md)
* [:octicons-link-24: Linkliste](Course_Element_Link_List.de.md)
* [:fontawesome-solid-arrows-turn-right: Auswahl](Course_Element_Selection.de.md)

## Allgemeines zu Kursbausteinen

Alle Kursbausteine verfügen über die Tabs "**Titel und Beschreibung**" sowie "**Layout**". Darüber hinaus gibt es noch bestimmte Tabs die je nach technischem Kurstyp durchgängig vorhanden sind. Der Tab "Lernpfad" existiert nur bei Lernpfad Kursen. Die Tabs "Sichtbarkeit" und "Zugang" existieren nur bei den herkömmlichen Kursen.

Neben den Kursbausteinen gibt es in OpenOlat Kursen noch weitere Tools und Lernressourcen, die zur Ausgestaltung von Kursen verwendet werden können. Hinweise darauf finden Sie in den jeweiligen Kapiteln.

## Leistungsbewertung

Eine Reihe an Kursbausteinen kann entweder zur summativen bzw. formativen Bewertung genutzt werden, oder dient der Fortschrittskontrolle. Die bewertbaren Kursbausteine können im
[Bewertungswerkzeug](../learningresources/Using_Course_Tools.de.md) eingesehen und bearbeitet werden. Weitere Informationen zu diesen Bausteinen finden Sie u.a. im Kapitel [Wissensüberprüfung](../learningresources/Assessment.de.md):

* [Aufgabe](../learningresources/Course_Element_Assessment.de.md) (manuelle Bewertung)
* [Gruppenaufgabe](../learningresources/Assessment.de.md) (manuelle Bewertung)
* [Portfolioaufgabe](../learningresources/Assessment.de.md) (manuelle Bewertung)
* [Checkliste](../learningresources/Assessment.de.md)  (manuelle & automatische Bewertung)
* [Bewertung](../learningresources/Assessment.de.md)  (manuelle Bewertung)
* [LTI](../learningresources/Other.de.md) (automatische Bewertung, wird von LTI-Seite übertragen)
* [SCORM](../learningresources/Knowledge_Transfer.de.md)  (automatische Bewertung, wird durch SCORM-Modul übertragen)
* [Test](../learningresources/Assessment.de.md)  (automatische & manuelle Bewertung)
