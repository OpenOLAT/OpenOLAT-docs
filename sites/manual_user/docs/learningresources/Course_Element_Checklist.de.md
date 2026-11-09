# Kursbaustein "Checkliste"  {: #course_element_checklist}


## Steckbrief

Name | Checkliste
---------|----------
Icon | :o_icon_o_cl_icon:
Verfügbar seit | Release 9.4
Funktionsgruppe | Wissensüberprüfung
Verwendungszweck | Checkliste mit Funktionen wie z.B. Sperrung der Bearbeitungsmöglichkeit nach Abgabedatum, ausgegraute Checkboxen, die nur Betreuer:innen abhaken können, usw.
Bewertbar | ja
Spezialität / Hinweis | 



Erreichte Ziele, fehlende Aufgaben, richtige oder falsche Lösungen - Checklisten machen dies sichtbar und dadurch für Betreuer:innen auch bewertbar.

Als informationelle Arbeitshilfe, die Teilnehmende dabei unterstützt z.B. kleinere Aufgaben zu erledigen oder Informationen gesichert zu behalten, erlaubt die Checkliste das Führen von z.B. To Do- oder Prüflisten. So können z.B. auch Aufgaben ausserhalb von OpenOlat dokumentiert werden. Sollte dies der Fall sein, finden Sie eventuell Informationen zur Bewertung auf der Startseite der Checkliste.

Wenn eine Checkliste mit einem Abgabedatum versehen wurde, kann diese im Anschluss nicht mehr bearbeitet werden. Unterhalb des Abgabedatums und der Bewertungsinformation steht die eigentliche Liste mit allen Checkboxen, inklusive eventueller Informationen und Dateien zum Download. Erscheint eine Checkbox ausgegraut, können sie entweder nur Betreuer:innen abhaken, oder das Abgabedatum ist bereits abgelaufen.

Es können auch mehrere Checklisten auf einmal hinzugefügt werden. Dieses Vorgehen ist sinnvoll, wenn Sie mehrere identische Checklisten benötigen. Dabei werden mehrere (maximal 12) Bausteine mit denselben Checkelementen erstellt und mit einem Strukturbaustein gebündelt. Für jeden Baustein wird dabei automatisch ein Titel angelegt, Änderungen sind aber möglich. Jeder Baustein kann dann noch mit einem spezifischen Abgabedatum versehen werden.

So können relativ schnell mehrere Checklisten mit identischen Check-Kriterien aber für unterschiedliche Gruppen, für unterschiedliche zu checkende Objekte, für unterschiedliche Veranstaltungstermine oder zur Überprüfung desselben Gegenstandes zu unterschiedlichen Zeitpunkten (Entwicklung) erstellt werden.

## Checkliste erstellen und einrichten [:octicons-tag-16:{ title="ab Release 9.4 (OO-936)" }](https://track.frentix.com/issue/OO-936){:target="_blank"}

Mit dem Kursbaustein "Checkliste" fügen Sie eine Checkliste in Ihren Kurs ein. Pro Kursbaustein erstellen Sie eine Checkliste mit so vielen Checkboxen wie Sie benötigen. Erstellen Sie die einzelnen Checkboxen der Liste im Tab "Checkboxen" über die Schaltfläche "Checkbox hinzufügen". Den Checkboxen können auch Punkte zugeordnet und Dateien zum Download hinzugefügt werden.

## Tab Konfiguration [:octicons-tag-16:{ title="ab Release 17.0 (OO-6458)" }](https://track.frentix.com/issue/OO-6458){:target="_blank"} {: #tab_configuration}

In diesem Tab bestimmen Sie, ob ein Abgabedatum für die Checkliste wirksam sein soll und ob und wie die Teilnehmenden bewertet werden. Je nach gewählten Einstellungen stehen Ihnen unterschiedliche Bewertungsoptionen zur Verfügung. Später bewerten Sie entweder im Kurs bei geschlossenem Kurseditor oder im [Bewertungswerkzeug](../learningresources/Assessment_of_course_modules.de.md) des Kurses.

Der Tab gliedert sich in die Bereiche "Konfiguration der Checkliste", "Konfiguration Bewertung" und "Bewertungsformular". Sind für die Checkliste bereits Bewertungen vorhanden, zeigt OpenOlat die Einstellungen unter "Konfiguration Bewertung" schreibgeschützt an. Bearbeitbar bleiben das Abgabedatum unter "Konfiguration der Checkliste" und der Bereich "Bewertungsformular". Mit "Bearbeitungsmodus aktivieren" machen Sie die Einstellungen wieder bearbeitbar, siehe [Schreibschutz der Bewertungskonfiguration](Course_Elements/index.de.md#assessment_config_read_only). [:octicons-tag-16:{ title="ab Release 21.1 (OO-9647)" }](https://track.frentix.com/issue/OO-9647)

### Konfiguration der Checkliste {: #checklist_configuration}

#### Checkliste bei Abgabedatum für Benutzer:innen sperren {: #lock_checklist}

Wenn dieser Schalter eingeschaltet ist, können Teilnehmende die Checkliste nach Erreichen des Abgabedatums nicht mehr bearbeiten.

#### Abgabedatum {: #deadline}

Das Feld erscheint, wenn "Checkliste bei Abgabedatum für Benutzer:innen sperren" eingeschaltet ist. Legen Sie hier das Datum fest, bis zu dem die Teilnehmenden die Checkliste ausgefüllt haben müssen.

### Konfiguration Bewertung {: #grading_configuration}

#### Punkte vergeben {: #score_granted}

Wenn Sie im Tab "Checkboxen" den einzelnen Checkboxen Punkte zuweisen, erhalten Teilnehmende für jede markierte Checkbox diese Punkte, manuell oder automatisch vergeben. Ist der Schalter ausgeschaltet, vergibt OpenOlat keine Punkte.

#### Minimal erreichbare Punkte {: #min_score}

Geben Sie hier die Anzahl Punkte ein, die Teilnehmende minimal erreichen können. Das Feld erscheint, wenn "Punkte vergeben" eingeschaltet ist.

#### Maximal erreichbare Punkte {: #max_score}

Geben Sie hier die Anzahl Punkte ein, die Teilnehmende maximal erreichen können. Das Feld erscheint, wenn "Punkte vergeben" eingeschaltet ist.

#### Bewertung mit Einstufung/Noten {: #grading}

Ist "Punkte vergeben" eingeschaltet, können Sie zusätzlich eine Bewertungsskala wählen. OpenOlat rechnet die Punkte dann in eine Note um. Mehr dazu auf der Seite [Einstufung/Noten](Assessment_translate_points_in_grades.de.md).

#### Bestanden / Nicht bestanden ausgeben {: #display_passed}

Wenn Sie den Schalter einschalten, sehen die Teilnehmenden "Bestanden" oder "Nicht bestanden". Ist er ausgeschaltet, zeigt OpenOlat keinen Bestanden-Status an. Ist "Bewertung mit Einstufung/Noten" eingeschaltet, erscheint der Schalter nicht: Den Bestanden-Status bestimmt dann die Bewertungsskala.

#### Art der Ausgabe {: #output_type}

Das Feld erscheint, wenn "Bestanden / Nicht bestanden ausgeben" eingeschaltet ist. Mit "Automatisch durch Punkteschwelle" oder "Automatisch bei Anzahl Checkboxen" vergibt OpenOlat den Bestanden-Status automatisch, aufgrund einer Punkteschwelle oder einer bestimmten Anzahl markierter Checkboxen. Mit "Manuell durch Betreuer:in" vergeben Betreuer:innen den Status selbst.

#### Punkteschwelle für Bestanden {: #cut_value}

Geben Sie hier die Anzahl Punkte ein, die Teilnehmende mindestens brauchen, um "Bestanden" zu erhalten. Unterhalb dieser Schwelle erhalten sie "Nicht bestanden". Das Feld erscheint, wenn unter "Art der Ausgabe" die Option "Automatisch durch Punkteschwelle" gewählt ist.

#### Anzahl Checkboxen für Bestanden {: #checks_to_pass}

Geben Sie hier die Anzahl Checkboxen an, die Teilnehmende mindestens markiert haben müssen, um "Bestanden" zu erhalten. Das Feld erscheint, wenn unter "Art der Ausgabe" die Option "Automatisch bei Anzahl Checkboxen" gewählt ist.

#### Bei Kurs-Bewertung berücksichtigen {: #include_in_course_assessment}

In Lernpfadkursen erscheint die Option, sobald "Punkte vergeben" oder "Bestanden / Nicht bestanden ausgeben" eingeschaltet ist. Ist sie ausgeschaltet, bleibt die Checkliste bei der Kurs-Bewertung unberücksichtigt.

#### Skalierungsfaktor für Kurs-Bewertung {: #score_scaling}

Das Feld erscheint, wenn die Kurs-Bewertung die Punkte mit Gewichtung zusammenzählt und "Punkte vergeben" sowie "Bei Kurs-Bewertung berücksichtigen" eingeschaltet sind. OpenOlat multipliziert die Punkte der Checkliste für die Kurs-Bewertung mit diesem Faktor. Mehr dazu unter [Kursbewertung mit Punkten: Summe mit Gewichtung](Course_Settings_Assessment/index.de.md#evaluation_with_points_weighting).

### Bewertungsformular {: #assessment_form}

#### Individueller Kommentar {: #individual_comment}

Wenn Sie diese Checkbox markieren, haben Sie bei der Bewertung die Möglichkeit, jeder teilnehmenden Person einen individuellen Kommentar zu geben.

#### Individuelle Bewertungsdokumente {: #individual_assessment_documents}

Wenn Sie diese Checkbox markieren, können Sie bei der Bewertung jeder teilnehmenden Person Dokumente bereitstellen, zum Beispiel als Feedback.

## Tab Checkboxen [:octicons-tag-16:{ title="ab Release 15.1 (OO-4758)" }](https://track.frentix.com/issue/OO-4758){:target="_blank"} {: #tab_checkboxes}

In diesem Tab erstellen und bearbeiten Sie die Checkboxen, die Teilnehmende oder Betreuer:innen anschliessend abhaken. Klicken Sie auf die Schaltfläche "Checkbox hinzufügen", um eine neue Checkbox zu erstellen. Es öffnet sich ein Formular mit den folgenden Feldern.

### Titel {: #checkbox_title}

Geben Sie hier einen aussagekräftigen kurzen Titel für die Checkbox ein.

### Freigabe {: #checkbox_release}

Mit der Freigabeeinstellung bestimmen Sie, wer die Checkbox markieren kann. "Benutzer:innen und Betreuer:innen" erlaubt sowohl Teilnehmenden als auch Betreuer:innen, die Checkbox zu markieren. Wählen Sie "Nur Betreuer:innen", sehen Teilnehmende die Checkbox, können sie aber nicht markieren.

### Beschriftung {: #checkbox_label}

Sie können zwischen 11 verschiedenen Checkbox-Arten auswählen: Erreicht, Erledigt, Bearbeitet, Erfüllt, Bestanden, Vorgeführt, Kontrolliert, Anwesend, Gelesen, Gesehen und Bestätigt. Wählen Sie die passendste aus.

### Punkte {: #checkbox_points}

Legen Sie fest, ob Punkte für markierte Checkboxen vergeben werden und wie viele.

### Beschreibung {: #checkbox_description}

Die Beschreibung erscheint in der Checkliste zusammen mit dem Titel, der Anzahl Punkte (falls ausgewählt) sowie der gegebenenfalls hochgeladenen Datei rechts von der Checkbox.

### Datei {: #checkbox_file}

Falls benötigt, fügen Sie hier für die Teilnehmenden eine Datei zum Download hinzu.

In der Tabelle des Tabs sehen Sie anschliessend die erstellten Checkboxen im Überblick. Hier ändern Sie auch ihre Reihenfolge.

## Tab Badges [:octicons-tag-16:{ title="ab Release 18.0 (OO-7003)" }](https://track.frentix.com/issue/OO-7003){:target="_blank"}
Haben Kursbesitzer:innen unter `Kurs > Administration > Einstellungen > Tab "Bewertung" > Abschnitt "Badges"` die Vergabe von Badges aktiviert, zeigt der Kurseditor zu diesem Kursbaustein den Tab "Badges". Dort erstellen Sie einen Badge eigens für diesen Kursbaustein.

[Zum Seitenanfang ^](#course_element_checklist)


## Checklisten nutzen und bewerten [:octicons-tag-16:{ title="ab Release 16.1 (OO-5946)" }](https://track.frentix.com/issue/OO-5946){:target="_blank"}

Im Kurs sehen Kursbesitzer:innen und Betreuer:innen beim Kursbaustein die Tabs "Übersicht", "Teilnehmer:innen" und "Vorschau", je nach Konfiguration zusätzlich "Erinnerungen" und "Badges". Teilnehmende ohne Betreuerrechte sehen direkt ihre Checkliste. Wurden den einzelnen Checkboxen Punkte zugeordnet, sind diese für die Lernenden in ihrer Checkliste sichtbar. So sehen die Lernenden direkt, wie sich eine Gesamtpunktzahl zusammensetzt.

Der Tab "Teilnehmer:innen" bietet Ihnen als Kursbesitzer:in oder Betreuer:in eine Übersicht über alle Checklisten der von Ihnen betreuten Teilnehmenden. Falls Sie mehrere Gruppen betreuen, können Sie die Übersichtstabelle nach Gruppen filtern. Im selben Tab bewerten Sie die Checklisten der einzelnen Lernenden, entweder per Person oder über den Button "Per Box Bewertung".

Zusätzlich drucken Sie mit der Schaltfläche "Übersicht als PDF" den aktuellen Stand der Checkliste über alle Teilnehmenden als PDF aus. Im PDF finden Sie die Spalte "Unterschrift", mit der Teilnehmende die Richtigkeit des Dokuments bestätigen.

Die Schaltfläche "Erledigte Checkboxen als PDF" erstellt ein PDF, das pro Checkbox eine Tabelle mit den Teilnehmenden enthält, die diese Checkbox bereits markiert haben.

!!! warning "Achtung"

    Ändern Sie die Checkboxen möglichst erst nach Ablauf des Abgabedatums.

Insgesamt stehen Ihnen vier Wege zur Verfügung, die Checklisten der Teilnehmenden zu bearbeiten.

  1. **Bearbeiten**: Der Link in der Tabelle öffnet die Checkliste der einzelnen Person, in der Sie einzelne Checkboxen markieren. Von dort haben Sie auch direkten Zugriff auf das Bewertungswerkzeug: Öffnen Sie den Tab "Bewertung", um das Bewertungsformular zu erreichen. Die Bewertung ändern Sie ebenfalls im Bewertungswerkzeug.
  2. **Per Box Bewertung**: Die Schaltfläche öffnet eine Liste aller Teilnehmenden, sortiert nach Checkbox. Über eine Dropdown-Liste wählen Sie die gewünschte Checkbox aus. Das senkt die Fehleranfälligkeit gerade bei grossen Checklisten mit vielen Checkboxen.

      Nach Gruppen filtern Sie vorher in der Tabelle der Checklistenverwaltung. Sie können die Tabelle nach Vornamen oder Nachnamen sortieren, um Teilnehmerliste und Checkliste einfacher abzugleichen.

  3. **Editieren**: Die Schaltfläche öffnet die Übersichtstabelle im Bearbeitungsmodus, in dem Sie alle Checkboxen aller Teilnehmenden bearbeiten.
  4. **Bewertungswerkzeug**: Zu guter Letzt wählen Sie Checkboxen einzelner Teilnehmender auch im [Bewertungswerkzeug](../learningresources/Assessment_of_course_modules.de.md) aus oder ab.

## Kursbaustein "Mehrere Checklisten" [:octicons-tag-16:{ title="ab Release 9.4 (OO-937)" }](https://track.frentix.com/issue/OO-937){:target="_blank"} {: #multi}

![Symbol des Kursbausteins Mehrere Checklisten](assets/wizard_434343_64.png)

Sofern vom OpenOlat Admin aktiviert, steht Ihnen auch die Option "Mehrere Checklisten" zur Verfügung.  Mit Hilfe eines Checklisten-Wizards können Sie mehrere Listen derselben Art gleichzeitig erstellen. Sie werden zusammen mit einem Struktur-Kursbaustein als Gruppe am Ende Ihres Kurses hinzugefügt. Den Strukturbaustein und die einzelnen Checklisten können Sie im Anschluss mittels Drag & Drop an die jeweils gewünschte Stelle im Kurs verschieben.

Erstellen Sie im **ersten** Schritt eine Vorlage für die zu erstellende Gruppe an Checklisten indem Sie Art und Anzahl der Checkboxen festlegen, und konfigurieren Sie diese im zweiten Schritt. Alle Listen und Einstellungen können im Anschluss im Kurseditor separat bearbeitet werden.

Im **zweiten** Schritt bestimmen Sie wie viele Checklisten anhand der im ersten Schritt definierten Vorlage erstellt werden sollen. Legen Sie einen Titel fest. Die Checklisten erhalten alle diesen Titel und werden durchnummeriert. Den Titel für jede einzelne Checkliste können Sie im nächsten Schritt anpassen. Hier definieren Sie auch, ob und wie Punkte vergeben oder das Attribut Bestanden vergeben werden soll.

Informationen zu den weiteren Einstellungen finden Sie unter [Tab Konfiguration](#tab_configuration). Wenn Sie die Checklisten mit einem Abgabedatum versehen, können Sie dieses im nächsten Schritt definieren.

Im **dritten** Schritt der Checklisten Sammelfunktion können Sie die Titel der einzelnen Checklisten gemäss Ihren Wünschen anpassen. Hier kann nun das Abgabedatum pro Checkliste definiert werden. Möchten Sie bei einer oder mehreren Checklisten ohne Abgabedatum arbeiten, lassen Sie das Datumsfeld leer.

Im **vierten** Schritt definieren Sie Titel und Beschreibung des übergeordneten Struktur-Kursbausteins. Kurztitel und Titel werden wie gewohnt in der Navigation und der Kurselement-Übersicht angezeigt.

Im unteren Teil des Formulars legen Sie fest, ob der Strukturbaustein Bewertungsinformationen aus den Checklisten anzeigt und wie er sie zusammenfasst. Informationen zum Struktur-Kursbaustein und der Bewertung weiterer Kursbausteine finden Sie im Kapitel Wissensvermittlung - [Strukturbaustein: Punkte](Course_Element_Structure.de.md#score).

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Bewertung von Kursbausteinen >](../learningresources/Assessment_of_course_modules.de.md)<br>
[Kursbausteine im Überblick >](Course_Elements/index.de.md)<br>
[Einstufung/Noten >](../learningresources/Assessment_translate_points_in_grades.de.md)<br>
[Kurseinstellungen - Tab Bewertung >](Course_Settings_Assessment/index.de.md)<br>
[Kursbaustein "Struktur" >](Course_Element_Structure.de.md)

**Weiterführend**<br>
[Badges >](../learningresources/OpenBadges.de.md)

[Zum Seitenanfang ^](#course_element_checklist)
