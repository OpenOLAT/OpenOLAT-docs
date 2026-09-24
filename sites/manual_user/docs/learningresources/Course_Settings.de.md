# Kurseinstellungen {: #course_settings}

Die Konfigurationen, die den Kurs als Ganzes betreffen, nehmen Sie vor unter:<br>
`Kurs > Administration > Einstellungen`

Das Menü "Einstellungen" steht Besitzer:innen des Kurses, Lernressourcenverwalter:innen und Administrator:innen zur Verfügung, ausserdem Personen, denen in der [Mitgliederverwaltung](../learningresources/Members_management.de.md) das Recht "Kurseditor" erteilt wurde.

![Kurseinstellungen über den Eintrag Einstellungen im Menü Administration geöffnet, mit einem Tab je Einstellungsbereich](assets/course_settings_menu_v2_de.png){ class="shadow lightbox" }

:octicons-device-camera-video-24: **Video-Einführung**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank”}

!!! info "Wichtig"

    Jede [Lernressource](../learningresources/index.de.md) verfügt über ein Menü "Einstellungen", nicht nur Kurse.

    Die Einstellungen von herkömmlichen und [Lernpfadkursen](../learningresources/Learning_path_course.de.md) variieren leicht.

    Über die Tabs "Info", "Metadaten", "Durchführung" und "Freigabe" können Sie Informationen angeben, die in der [Kursinfoseite](../learningresources/Info_page.de.md) sichtbar werden.

## Steckbrief

Name | Kurseinstellungen
---------|----------
Verfügbar seit | Release 13.0 (OO-3706)


## Tab Info {: #info}

![Tab "Info" aktiv in den Kurseinstellungen](assets/course_settings_tab_info_v1_de.png){ class="shadow lightbox" }

Hier definieren Sie Informationen über den Kurs bzw. die Lernressource. Dazu zählen: 

* Titel
* Kennzeichen (Eine externe Kennung, die in der Kursübersicht angezeigt wird. Z.B. die Bezeichnung aus dem Vorlesungsverzeichnis oder einem gedruckten Kurskatalog.) 
* Teaser (Textzeile/Begriff)
* Kursbeschreibung
* Beschreibung der Lernziele
* Voraussetzungen
* Anforderungen für eine Bescheinigung
* Titelbild
* Teaser-Film

Diese Infos sind für Interessierte auch ohne Kurszugang unter (Kurs-)Info sichtbar. 
Unter dem hier definierten Titel erscheint die Lernressource in der alphabetischen Kursliste und ist für Anfragen über die Suchmaske relevant.

[Mehr über das **Einrichten der Infoseite** >](../learningresources/Course_Settings_Info.de.md)<br>
[Mehr über die **Inhalte der Infoseite** >](../learningresources/Info_page.de.md)<br>
[Zum Seitenanfang ^](#course_settings)



## Tab Metadaten {: #metadata}

![Tab "Metadaten" aktiv in den Kurseinstellungen](assets/course_settings_tab_metadata_v1_de.png){ class="shadow lightbox" }

Metadaten enthalten Schlagwörter, die den Kurs beschreiben. Anhand der Metadaten kann Ihr Kurs z.B. besser gefunden werden. Sie sind optional und müssen nicht zwingend ausgefüllt werden.

Metadaten eines Kurses sind

* Typ der Lernressource (in diesem Fall: Kurs)
* ID-Nummer des Kurses
* Ersteller des Kurses
* Autor:innen / Namen der Lehrenden des Kurses
* Fachbereiche (aus der Taxonomy)
* Durchführungsformat (Blendend Learning, Selbststudium, ...)
* Hauptsprache
* geschätzter Zeitaufwand zur Bearbeitung
* Lizenz

[Zu den Details >](../learningresources/Course_Settings_Metadata.de.md)<br>
[Mehr über **Metadaten** >](../basic_concepts/Full_Text_Search.de.md#metadata)<br>
[Zum Seitenanfang ^](#course_settings)


## Tab Durchführung {: #execution}

![Tab "Durchführung" aktiv in den Kurseinstellungen](assets/course_settings_tab_execution_v1_de.png){ class="shadow lightbox" }

Hier können Sie 

* den Durchführungszeitraum des Kurses definieren, 
* das "[Absenzmanagement](../area_modules/Absence_Management.de.md)" einschalten und weiter konfigurieren (sofern in der System-Administration unter `Administration > Module > Termine / Absenzen` eingeschaltet), 
* existierende herkömmliche Kurse in Lernpfadkurse konvertieren 
* bzw. bei [Lernpfadkursen](Learning_path_course.de.md) definieren, wie der Lernfortschritt berechnet wird, anhand der Anzahl der Kursbausteine oder anhand der Bearbeitungsdauer der Kursbausteine.

[Zu den Details >](../learningresources/Course_Settings_Execution.de.md)<br>
[Zum Seitenanfang ^](#course_settings)


## Tab Freigabe {: #share}

![Tab "Freigabe" aktiv in den Kurseinstellungen](assets/course_settings_tab_share_v1_de.png){ class="shadow lightbox" }

Im Tab "Freigabe" definieren Sie, wie und für wen ein Kurs oder eine Lernressource freigegeben wird. 

* Ob der Zugang nur für ausgewählte Mitglieder möglich ist, der Kurs selbst gewählt und gebucht werden kann oder der Zugang ganz offen steht 
* Wann Teilnehmer:innen aus dem Kurs austreten können
* Ob ggf. nur administrative Rollen einer bestimmten Organisationseinheit Zugriff erhalten
* Ob und wie andere Autor:innen auf den Kurs zugreifen können
* Ob externe OER-Kataloge und Suchmaschinen Informationen erhalten
* Ob ein Angebot im Katalog zum Kurs gemacht wird und wenn ja, welches
* Ob der Kurs auch von einem anderen LMS aus via LTI genutzt werden kann

[Details zum **Tab Freigabe** >](Course_Settings_Share.de.md)<br>
[Mehr zur **Freigabe** >](Access_configuration.de.md)<br>
[Zum Seitenanfang ^](#course_settings)


## Tab Katalog (gilt nur für Katalog Version 1) {: #catalog}

![Tab "Katalog" aktiv in den Kurseinstellungen](assets/course_settings_tab_catalog_v1_de.png){ class="shadow lightbox" }

Über den Button "In Katalog einfügen" kann die Lernressource in den Katalog eingetragen und einer oder mehreren vordefinierten Kategorien zugeordnet werden. Um den Kurs oder die Lernressource in mehrere Katalogbereiche einzutragen, muss der Schritt wiederholt werden. Anschliessend erscheinen alle Katalogeinträge hier im Tab "Katalog" und können hier auch wieder entfernt werden.

Der gesamte OpenOlat [Katalog (Version 1)](../area_modules/Courses.de.md) ist für alle Benutzer:innen im Menü "Kurse" einsehbar.

Tragen Sie Ihre Kurse erst in den Katalog ein, wenn diese fertiggestellt sind und für die Benutzer:innen sichtbar sein sollen.

[Zum Seitenanfang ^](#course_settings)


## Tab Nutzungsbedingungen {: #disclaimer}

![Tab "Nutzungsbedingungen" aktiv in den Kurseinstellungen](assets/course_settings_tab_disclaimer_v1_de.png){ class="shadow lightbox" }

Hier können 

* frei definierbare kursbezogene **Nutzungsbedingungen** 
* und eine kursbezogene **Datenschutzerklärung** 

aktiviert und hinterlegt werden. Startet eine Person den Kurs, muss sie zunächst die Bedingungen akzeptieren, ansonsten ist ein Kurszugang nicht möglich. Für jeden eingeschalteten Text erfassen Sie einen Titel, die Bedingungen und die Beschriftung der Checkbox, die zum Akzeptieren angekreuzt wird. Eine zweite Checkbox ist möglich.

In der [Mitgliederverwaltung](../learningresources/Members_management.de.md) sehen Sie im Bereich "Einwilligungen" welche Personen die Bedingungen bereits akzeptiert haben.

![Nutzungsbedingungen und Datenschutzerklärung einzeln einschaltbar, je mit Titel, Bedingungen und bis zu zwei Checkbox-Beschriftungen, im Tab Nutzungsbedingungen](assets/disclaimer_course_DE.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#course_settings)


## Tab Layout {: #layout}

![Tab "Layout" aktiv in den Kurseinstellungen](assets/course_settings_tab_layout_v1_de.png){ class="shadow lightbox" }

Im Tab Layout bestimmen Sie, wie der Kurs aussieht und wie sich Teilnehmende darin bewegen. Hier kann

* eine **Layoutvorlage** für einen Kurs ausgewählt, 
* die **Kursnavigation** näher bestimmt 
* und der **Stil der Kursbausteine** definiert werden.

Welche **Layoutvorlagen** zur Auswahl stehen, bestimmt das Systemlayout (Theme), das für Ihre ganze OpenOlat-Instanz gilt. Die Vorlage "Standard" ist immer vorhanden. Ein einheitliches Erscheinungsbild für alle Kurse (Farben, Schriften, Logo) wird deshalb zentral über ein individuelles Systemlayout umgesetzt, siehe [Darstellung, Layout](../../manual_admin/administration/Customizing.de.md#layout). Für einen einzelnen Kurs wählen Sie die Option "Eigene Konfiguration festlegen": Dort legen Sie Schriftart und Farben für Text, Überschriften, Links, Menü und Toolbox fest und laden ein Logo hoch. Darüber hinaus können Sie im [Ablageordner](../learningresources/Storage_folder.de.md) des Kurses im Ordner "courseCSS" eigene CSS-Dateien hinterlegen, die dann in der Auswahl als "Aus Kursablageordner" erscheinen.

Im Bereich "**Navigation**" kann die Sichtbarkeit des Menüs und der Krümelnavigation eingestellt werden. In Lernpfadkursen legen Sie zusätzlich fest, ob im Menü die Icons und der Pfad angezeigt werden ("Icons im Menu anzeigen", "Pfad im Menu anzeigen"). Je nach linearem oder flexiblem Szenario bietet sich die eine oder andere Variante an.

![Kursmenü mit Pfad und Icons: Statussymbole an einer Linie links, vor jedem Titel das Symbol des Kursbausteins](assets/lp_icons_DE.png){ class="shadow lightbox" }
![Kursmenü ohne Pfad und Icons: nur die Titel der Kursbausteine, Statussymbole rechts](assets/no_lp_no_icons_DE.png){ class="shadow lightbox" }

Im Bereich "**Standard Stil Kursbausteine**" können Sie die Basisdarstellung der Kursbausteine definieren und z.B. ein eigenes Hintergrundbild hochladen oder ein Hintergrundbild aus der Bibliothek wählen, den Stil des Bildes definieren, sowie bei Bedarf eine Farbkategorie zuordnen. In der Vorschau sehen Sie die Auswirkungen.

[Zum Seitenanfang ^](#course_settings)


## Tab Toolbar {: #toolbar}

![Tab "Toolbar" aktiv in den Kurseinstellungen](assets/course_settings_tab_toolbar_v1_de.png){ class="shadow lightbox" }

Hier schalten Sie die Toolbar in der Kopfzeile des Kurses ein oder aus und definieren, welche konkreten einzelnen Werkzeuge in der Toolbar den Kursteilnehmer:innen angezeigt werden.


[Zu den Details >](../learningresources/Course_Settings_Toolbar.de.md)<br>
[Zum Seitenanfang ^](#course_settings)


## Tab Bewertung {: #assessment}

![Tab "Bewertung" aktiv in den Kurseinstellungen](assets/course_settings_tab_assessment_v1_de.png){ class="shadow lightbox" }

Im Tab Bewertung können Sie folgende Aspekte aktivieren bzw. konfigurieren:

* Kurs-Bewertung mit Punkten: Summe, Durchschnitt, gewichtet
* Anforderungen für das Bestehen des Kurses 
* die Rolle der Betreuenden im Bewertungsprozess
* Leistungsnachweise aktivieren und konfigurieren
* Kreditpunkte aktivieren und konfigurieren
* Kurs-Zertifikate aktivieren, konfigurieren und auch eine Rezertifizierung einrichten
* die Vergabe von Badges aktivieren


!!! info "Wichtig"

    Bei herkömmlichen Kursen sind im Bewertungs-Tab nur die Einstellungen für Leistungsnachweise, Zertifikate und Badges verfügbar. Die Konfiguration für das Bestehen erfolgt im Kurseditor auf dem obersten Kursbaustein im Tab "Punkte". Einen Fortschritt gibt es bei herkömmlichen Kursen nicht.


[Zu den Details >](../learningresources/Course_Settings_Assessment.de.md)<br>
[Zu den Details der **Zertifikate** >](../learningresources/Course_Settings_Assessment.de.md#certificate)<br>
[Zu den Details der **Rezertifizierung** >](../learningresources/Course_Settings_Assessment.de.md#recertification)<br>
[Zum Seitenanfang ^](#course_settings)


## Tab Optionen {: #options}

![Tab "Optionen" aktiv in den Kurseinstellungen](assets/course_settings_tab_options_v1_de.png){ class="shadow lightbox" }

Hier aktivieren Sie je nach Bedarf

* ein kurspezifisches [Glossar](../learningresources/Using_Additional_Course_Features.de.md) 
* einen [Ressourcenordner](../learningresources/index.de.md) zu Ihrem Kurs
* einen speziellen Ordner für Betreuer:innen
* To-dos für Betreuer:innen

Falls Sie Benutzer:in mit einer administrativen Rolle sind (Lernressourcenverwalter:in, Administrator:in), werden Ihnen hier zusätzlich noch spezielle Optionen angezeigt:

* Einladung externe Benutzer:innen für Kursbesitzer:innen mit Autorenrecht aktivieren
* die "LTI 1.3"-Freigabe für Kursbesitzer:innen mit Autorenrecht aktivieren


[Details zum Tab Optionen > ](../learningresources/Course_Settings_Options.de.md)<br>
[Zum Seitenanfang ^](#course_settings)


## Weiterführende Informationen {: #further_information}

[Kurs-Administration: Übersicht >](../learningresources/Administration.de.md)<br>
[Kurs erstellen >](../learningresources/Creating_Course.de.md)

[Zum Seitenanfang ^](#course_settings)
