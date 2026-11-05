# Audio aufnehmen

## Voraussetzungen {: #requirements}

* Wenn in OpenOlat Audios aufgenommen werden sollen, muss zunächst ein Mikrofon verfügbar sein. Es muss grundsätzlich im Device aktiviert worden sein.

* Damit das Mikrofon auch in OpenOlat für Aufnahmen genutzt werden kann, muss es für OpenOlat frei gegeben sein. 

* *Nur macOS:* In anderen Browsern als Safari muss die allgemeine Erlaubnis zur Verwendung des Mikrofons erteilt werden. Stellen Sie diese Berechtigung auf dem Mac für die Browser ein, die Sie für OpenOlat verwenden:<br>
  `System Settings > Privacy & Security > Microphone`

* Auf der Gegenseite muss in OpenOlat die **Möglichkeit zu Audioaufnahmen** durch Systemadministrator:innen in der System-Administration aktiviert worden sein:<br>
  `Administration > Module > Audio/Video-Aufnahme`

## Wo können in OpenOlat Audios aufgenommen werden? :octicons-tag-16:{ title="ab Release 17.1 (OO-6327)" } {: #audios_recording}

### Aufnahme im Media Center

Öffnen Sie das **persönliche Menü** durch Klick auf das kleine Bild oder Dreieck rechts oben.
Öffnen Sie darin dann das Media Center.

Unter den Möglichkeiten zum Hinzufügen neuer Mediendateien befindet sich auch **"Audio aufzeichnen"**.

![Markierter Eintrag Audio aufzeichnen im Menü des Buttons Mediendatei hinzufügen](assets/audio_recording_mediacenter_v3_de.png){ class="shadow lightbox" title="Media Center im persönlichen Menü" }

### Aufnahme im Kursbaustein Seite

Im Kursbaustein Seite kann innerhalb eines Layout-Elements auch ein Audio eingefügt werden. 

![Markiertes Element Audio im Menü des Buttons Inhalt hinzufügen](assets/audio_recording_page_v3_de.png){ class="shadow lightbox" title="Kursbaustein Seite im Bearbeitungsmodus" }

Hat man sich dafür entschieden, erscheint ein Popup zur Auswahl eines vorhandenen Audios. Im Popup befindet sich zusätzlich ein Button zur Aufnahme eines eigenen Audios.

![Markierter Button Audio aufnehmen neben dem Button Audio hinzufügen](assets/audio_recording_page_add_v3_de.png){ class="shadow lightbox" title="Dialog Audio auswählen" }

### Aufnahme im Kursbaustein HTML-Seite

Der in OpenOlat verwendete HTML-Editor (Tiny) wird auch für das Einfügen und Aufzeichnen von Audios verwendet. Die Option zum Aufzeichnen eines Audios befindet sich unter den Werkzeugen, die auch zum Einfügen bereits vorhandener Medien verwendet werden.  

![Markiertes Mikrofon-Symbol zum Aufzeichnen eines Audios in der Symbolleiste](assets/audio_recording_html_editor_v3_de.png){ class="shadow lightbox" title="HTML-Editor im Kurseditor" }

!!! note "Hinweis"

    Im HTML-Editor sind Audioaufnahmen zwar prinzipiell möglich, an manchen Stellen werden bei Aufruf des Editors aber aus verschiedenen Gründen nicht alle Bearbeitungsmöglichkeiten angeboten. Es kann also sein, dass beim Aufruf des HTML-Editors die Option zum Aufzeichnen eines Audios angeboten wird, bei einem Aufruf von anderer Stelle aus nicht. 

### Aufnahme im Kursbaustein Aufgabe

Die Möglichkeit zu Audioaufnahmen in einer Aufgabe ist in den Workflow eingebettet. Sie finden die Recording-Funktion im Arbeitsschritt, wo das Audio als Aufgabenstellung oder Musterlösung eingefügt werden soll.

![Markierter Eintrag Audio aufnehmen im Menü des Buttons Aufgabe erstellen](assets/audio_recording_task_create_task_v3_de.png){ class="shadow lightbox" title="Tab Aufgabenstellung des Kursbausteins Aufgabe" }

![Markierter Eintrag Audio aufnehmen zum Erstellen einer Musterlösung](assets/audio_recording_task_create_solution_v3_de.png){ class="shadow lightbox" title="Tab Musterlösung des Kursbausteins Aufgabe" }

Für Audioaufnahmen, die im Kursbaustein "Aufgabe" aufgezeichnet werden, besteht aktuell keine Möglichkeit zur Speicherung und Verlinkung im Media Center.

### Aufnahme im Kursbaustein Gruppenaufgabe

Die Audioaufnahme im Kursbaustein "Gruppenaufgabe" funktioniert wie im Kursbaustein "Aufgabe".

## Wo werden die Audioaufnahmen gespeichert? {: #save_audio_recordings}

**Innerhalb eines Kursbausteins aufgenommene Audios** werden auch bei diesem Kursbaustein gespeichert. 
Die Aufnahmen sind nicht im Autorenbereich, Ablageordner oder im Media Center aufgeführt (Ausnahme: Kursbaustein Seite).

![Markierte Audiodatei audio01.m4a in der Liste der Aufgaben](assets/audio_recording_task_storage_v3_de.png){ class="shadow lightbox" title="Tab Verwalten des Kursbausteins Aufgabe" }

Wird dagegen die **Audioaufnahme im Media Center** gestartet, wird das Audio auch im Media Center gespeichert.

## In welchem Format und welcher Qualität werden Aufnahmen gespeichert? {: #audio_format_quality}

In OpenOlat gemachte Audioaufnahmen werden immer als **m4a-Dateien** gespeichert. Dies ist dadurch begründet, dass nur das m4a-Format von allen Browsern unterstützt wird.

Die Aufnahmequalität ist vorgegeben (mono, 44 kHz).

Systemadministrator:innen können in der System-Administration eine lokale Audio-Konvertierung aktivieren unter<br>
  `Administration > Module > Audio/Video-Aufnahme > Tab Aufnahmekonfigurationen`<br>
(Siehe auch den [Artikel im Administrations-Handbuch](../../manual_admin/administration/Modules_Audio_Video_Recording.de.md#audioaufzeichnung-aktivieren).)

## Wie viel Speicherplatz steht für meine Audios zur Verfügung? {: #audio_storage}

Bsp.: Media Center<br>
In der linken unteren Ecke sehen Sie den verfügbaren Speicherplatz (für das gesamte Media Center) und wie viel davon bereits belegt ist. Der verfügbare Platz kann von den Administrator:innen bestimmt werden.

![Markierte Anzeige des belegten und verfügbaren Speicherplatzes unten links](assets/audio_recording_space_v3_de.png){ class="shadow lightbox" title="Media Center im persönlichen Menü" }

## Wie lassen sich Audioaufnahmen exportieren? {: #audio_export}

### Download aus dem Kursbaustein Aufgabe und Gruppenaufgabe

Sowohl Audioaufnahmen aus Aufgabenstellung als auch Audioaufnahmen in der Musterlösung können direkt im Kursbaustein heruntergeladen werden. Verwenden Sie dazu die Option unter den 3 Punkten am Ende einer Zeile. 

![Vier Schritte zum Herunterladen einer Audioaufnahme, zuletzt der Eintrag Datei herunterladen im Menü mit den 3 Punkten](assets/audio_recording_task_download_v3_de.png){ class="shadow lightbox" title="Tab Verwalten des Kursbausteins Aufgabe" }

### Download aus dem Media Center

Wählen und öffnen Sie im Media Center das gewünschte Audio. Unter dem Button mit den 3 Punkten finden Sie die Option zum Herunterladen.

![Markierter Menüpunkt Herunterladen im Menü mit den 3 Punkten einer Audiodatei](assets/audio_recording_mediacenter_download_v3_de.png){ class="shadow lightbox" title="Detailansicht einer Mediendatei im Media Center" }

!!! note "Hinweis"

    Ein Audio, das innerhalb eines Kursbausteins aufgenommen wurde, wird **nicht** im Ablageordner des Kurses abgelegt.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Audio-/Video-Recording](../../manual_admin/administration/Modules_Audio_Video_Recording.de.md)

[zum Seitenanfang ^](#audio-aufnehmen)
