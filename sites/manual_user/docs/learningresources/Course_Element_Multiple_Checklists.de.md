# Assistent "Mehrere Checklisten" {: #multiple_checklists}

Brauchen Sie dieselbe Checkliste mehrmals, etwa für verschiedene Termine oder um denselben Gegenstand zu verschiedenen Zeitpunkten zu prüfen, legt der Assistent "Mehrere Checklisten" alle in einem Durchgang an, gebündelt als ein Kapitel im Kursmenü. Sie erstellen die Checkboxen einmal als Vorlage, und der Assistent erzeugt daraus bis zu 12 Kursbausteine "Checkliste" unter einem gemeinsamen Kursbaustein "Struktur".

## Steckbrief

Name | Mehrere Checklisten
---------|----------
Icon | :o_icon_o_icon_wizard:
Verfügbar seit | Release 9.4 (OO-937)
Funktionsgruppe | Wissensüberprüfung
Verwendungszweck | Assistent, der nach einer gemeinsamen Vorlage in einem Schritt bis zu 12 Checklisten anlegt
Legt an | je Checkliste: Kursbaustein ["Checkliste"](Course_Element_Checklist.de.md), bis zu 12<br>für alle Checklisten zusammen: ein Kursbaustein ["Struktur"](Course_Element_Structure.de.md)

## Alle Checklisten in einem Kapitel {: #structure}

Der Assistent legt die Checklisten nicht einzeln ins Kursmenü, sondern bündelt sie wie in einem Ordner unter einem Kursbaustein "Struktur". So erscheinen sie im Kursmenü als ein Kapitel, und Sie verschieben sie gemeinsam. In herkömmlichen Kursen fasst der Kursbaustein "Struktur" auf Wunsch auch die Punkte aller Checklisten zusammen und zeigt an, ob die Teilnehmenden bestanden haben. Das legen Sie im [vierten Schritt](#step_structure) fest.

## Mehrere Checklisten anlegen [:octicons-tag-16:{ title="ab Release 9.4 (OO-937)" }](https://track.frentix.com/issue/OO-937){:target="_blank"} {: #create}

Den Assistenten nutzt, wer den Kurseditor öffnen darf: Kursbesitzer:innen, Administrator:innen, Lernressourcenverwalter:innen und Personen mit dem [Kursrecht "Kurseditor"](../learningresources/Members_management.de.md#additional_rights). Er steht in herkömmlichen Kursen und in Lernpfadkursen zur Verfügung.

Klicken Sie im Kurseditor auf "Kursbausteine einfügen" und in der Gruppe "Wissensüberprüfung" auf "Mehrere Checklisten". Der Eintrag steht direkt nach "Checkliste". Es öffnet sich ein Fenster mit dem Titel "Checklisten".<br>
`Kurs > Administration > Kurseditor > Kursbausteine einfügen > Wissensüberprüfung > Mehrere Checklisten`

Der Assistent führt Sie durch vier Schritte.

### Schritt 1: Checklistenvorlage {: #step_template}

Erstellen Sie mit "Checkbox hinzufügen" die Checkboxen, die jede Checkliste erhalten soll. Die Felder einer Checkbox sind dieselben wie im [Tab "Checkboxen"](Course_Element_Checklist.de.md#tab_checkboxes) einer einzelnen Checkliste. Die Vorlage braucht mindestens eine Checkbox.

### Schritt 2: Konfiguration {: #step_configuration}

Legen Sie unter "Titel" den gemeinsamen Titel fest. Jede Checkliste erhält diesen Titel mit ihrer Laufnummer, etwa "Labor 1", "Labor 2". Unter "Anzahl Checklisten" wählen Sie zwischen 1 und 12.

Die übrigen Felder gelten für alle Checklisten, etwa ob Punkte vergeben werden oder wann eine Checkliste als bestanden gilt. Sie entsprechen dem [Tab "Konfiguration"](Course_Element_Checklist.de.md#tab_configuration) einer einzelnen Checkliste.

### Schritt 3: Titel und Datum {: #step_titles}

Der Assistent zeigt die Checklisten mit ihren Titeln aus Schritt 2. Passen Sie jeden Titel bei Bedarf an; ein Titel darf bis zu 32 Zeichen lang sein. Setzen Sie je Checkliste ein "Abgabedatum", sperrt OpenOlat die Checkliste ab diesem Zeitpunkt für Teilnehmende. Lassen Sie das Feld leer, bleibt die Checkliste ohne Abgabedatum.

### Schritt 4: Strukturdaten {: #step_structure}

Geben Sie "Titel", "Titel im Kursmenü" und "Beschreibung" des Kursbausteins "Struktur" ein, unter dem die Checklisten stehen. Der "Titel im Kursmenü" ist die kurze Form, die das Kursmenü anzeigt. Mehr dazu unter [Tab "Titel und Beschreibung"](General_Configuration_of_Course_Elements.de.md#desc). In Lernpfadkursen zeigt dieser Schritt nur diese drei Felder.

In herkömmlichen Kursen legen Sie hier zusätzlich fest, ob der Kursbaustein "Struktur" die Ergebnisse der Checklisten zusammenfasst: Mit "Summe Checklisten" zählt er die Punkte zusammen. Mit "Bestanden / Nicht bestanden ausgeben" zeigt er an, ob die Teilnehmenden bestanden haben, entweder über eine "Punkteschwelle für Bestanden" oder mit "Von Bausteinen übernehmen". Mehr dazu unter [Kursbaustein "Struktur"](Course_Element_Structure.de.md#score).

## Was der Assistent anlegt {: #result}

Der Assistent hängt einen Kursbaustein "Struktur" ans Ende des Kurses und legt die Checklisten darunter an. [Verschieben](Deleting_Moving_and_Copying_Course_Elements.de.md) Sie den Kursbaustein "Struktur" danach an die gewünschte Stelle im Kursmenü; die Checklisten wandern mit. Jede Checkliste können Sie anschliessend einzeln bearbeiten, etwa den Titel oder das Abgabedatum. Was die Einstellungen bewirken und wie Sie Checklisten bewerten, steht unter [Kursbaustein "Checkliste"](Course_Element_Checklist.de.md). Teilnehmende sehen die neuen Kursbausteine, sobald Sie den Kurs [publizieren](Using_additional_Course_Editor_Tools.de.md#publish).

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kursbaustein "Checkliste" >](Course_Element_Checklist.de.md)<br>
[Mitgliederverwaltung >](../learningresources/Members_management.de.md)<br>
[Kursbausteine im Kurseditor >](General_Configuration_of_Course_Elements.de.md)<br>
[Kursbaustein "Struktur" >](Course_Element_Structure.de.md)<br>
[Löschen, Verschieben und Kopieren von Kursbausteinen >](Deleting_Moving_and_Copying_Course_Elements.de.md)<br>
[Kurseditorwerkzeuge >](Using_additional_Course_Editor_Tools.de.md)

**Weiterführend**<br>
[Bewertung von Kursbausteinen >](../learningresources/Assessment_of_course_modules.de.md)<br>
[Assistent "Mehrere HTML-Seiten" >](Course_Element_Multiple_HTML_Pages.de.md)

[Zum Seitenanfang ^](#multiple_checklists)
