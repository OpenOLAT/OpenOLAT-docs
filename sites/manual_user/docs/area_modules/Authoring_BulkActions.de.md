# Autorenbereich - Sammelaktionen {: #authoring_bulk_actions}

Sobald Sie in der ersten Spalte der Tabelle eine Lernressource auswählen, erscheinen über der Tabelle zusätzliche Buttons, von "E-Mail versenden" bis "Löschen". Mit ihnen führen Sie Aktionen für die ausgewählten Lernressourcen gemeinsam durch, also für mehrere Lernressourcen auf einmal (Bulk Actions).<br>
Diese Buttons sind nicht sichtbar, wenn nicht mindestens eine Lernressource ausgewählt ist. Die Buttons für Sammelaktionen und das Menü unter den 3 Punkten sehen Autor:innen, Lernressourcenverwalter:innen und Administrator:innen.

Bei Klick auf die 3 Punkte am Ende einer Tabellenzeile erscheint ein Menü mit Aktionen nur für die Lernressource dieser Zeile.

![Buttons für Sammelaktionen über der Tabelle und das geöffnete 3-Punkte-Menü einer Zeile mit Einstellungen, Kurseditor und Mitgliederverwaltung zuoberst](assets/autorenbereich_buttons_fuer_ressourcenauswahl_v2_de.png){ class="shadow lightbox" title="Tab Meine Einträge im Autorenbereich · 2026.09.28" }

!!! tip "Tipp"

    Wenn Sie die **Checkbox in der Titelzeile der Tabelle** wählen, werden alle Lernressourcen auf einmal ausgewählt. Verteilt sich die Tabelle auf mehrere Seiten, öffnet die Checkbox ein Menü: "Alle Zeilen der Seite auswählen" wählt die Lernressourcen der angezeigten Seite aus, "Alle ... Zeilen auswählen" alle Lernressourcen der Tabelle.

    ![Angehakte Checkbox in der Titelzeile markiert, alle Zeilen der Tabelle sind ausgewählt und die Buttons für Sammelaktionen erscheinen](assets/autorenbereich_buttons_fuer_ressourcenauswahl2_v2_de.png){ class="shadow lightbox" title="Tab Meine Einträge im Autorenbereich · 2026.09.28" }

---

### E-Mail versenden [:octicons-tag-16:{ title="ab Release 11.5 (OO-2674)" }](https://track.frentix.com/issue/OO-2674){:target="_blank"} {: #send_mail}

Wählen Sie die gewünschten Lernressourcen aus und klicken Sie auf "E-Mail versenden". Es öffnet sich ein Dialog. Sie können nun definieren, an wen die E-Mail verschickt werden soll. Mögliche Empfänger:innen sind **alle Kursbesitzer:innen, alle Kursbetreuer:innen und alle Teilnehmenden**.

Fügen Sie einen Betreff und die gewünschte Nachricht hinzu. Bei Bedarf kann noch ein Anhang und eine Kopie für den Absender ergänzt werden.

!!! info "Wichtig"

    Sie können die E-Mail an alle Kurse schicken, die Ihnen angezeigt werden. Dazu gehören auch Kurse, welche für **alle Autor:innen** sichtbar sind. Sie müssen also nicht zwingend Mitglied des Kurses sein, um diese Funktion zu nutzen.

### Status ändern [:octicons-tag-16:{ title="ab Release 17.1 (OO-5011)" }](https://track.frentix.com/issue/OO-5011){:target="_blank"} {: #change_status}

Wählen Sie den Publikationsstatus aus, der für alle ausgewählten Lernressourcen gelten soll und klicken Sie auf "Ändern".

### Besitzer:innen bearbeiten [:octicons-tag-16:{ title="ab Release 15.4 (OO-5025)" }](https://track.frentix.com/issue/OO-5025){:target="_blank"} {: #modify_owners}

Hier werden Ihnen alle **Besitzer:innen der ausgewählten Lernressourcen** angezeigt. Sie können diese gleichzeitig aus mehreren Kursen entfernen oder auch neue Besitzer:innen den ausgewählten Lernressourcen hinzufügen. Eine E-Mailbenachrichtigungsoption schliesst die Bearbeitung ab.

### Metadaten und Einstellungen [:octicons-tag-16:{ title="ab Release 17.2 (OO-6441)" }](https://track.frentix.com/issue/OO-6441){:target="_blank"} {: #metadata_settings}

Gehören mehrere Lernressourcen zusammen, etwa die Kurse einer Weiterbildungsreihe, **vereinheitlichen** Sie ihre **Metadaten** und Einstellungen in einem Durchgang, statt jede Lernressource einzeln zu bearbeiten. Nach Klick auf "Metadaten und Einstellungen" öffnet sich der Assistent (Wizard) "Einstellungen bearbeiten". Er ändert nur die ausgewählten Lernressourcen, bei denen Sie Besitzer:in, Lernressourcenverwalter:in oder Administrator:in sind.

Im ersten Schritt "Bereiche" wählen Sie aus, was Sie bearbeiten wollen. Der Assistent führt danach nur durch die gewählten Bereiche und schliesst mit dem Schritt "Übersicht", der die geplanten Änderungen auflistet. In "Metadaten", "Autorenrechte", "Durchführung" und "Toolbar" übernimmt OpenOlat nur die Felder, bei denen Sie das Kontrollkästchen "Ändern" markieren. Lassen Sie in "Metadaten" oder "Durchführung" ein markiertes Feld leer, werden die bestehenden Daten gelöscht.

Die Bereiche in der Reihenfolge des Assistenten:

* "Metadaten": "Autor:innen / Durchführung mit", "Durchführungsformat" (nur bei Kursen, z.B. "Prüfungskurs"), "Hauptsprache", "Zeitaufwand", "Lizenz" (bei eingeschalteten Lizenzen) und "Freigabe OER-Kataloge und Suchmaschinen" (bei eingeschaltetem Modul OAI-PMH).
* "Fachbereiche": Fachbereiche hinzufügen oder entfernen. Bei eingeschaltetem Katalog heisst der Bereich "Fachbereiche / Katalog".
* "Administrative Freigabe": Organisationen hinzufügen oder entfernen, siehe [Bereich "Administrative Freigabe"](#bulk_administrative_access).
* "Autorenrechte": die Rechte "Referenzieren", "Kopieren" und "Exportieren" für alle anderen Autor:innen hinzufügen oder entfernen.
* "Durchführung": "Durchführungszeitraum" und "Durchführungsort" einheitlich setzen.
* "Toolbar": Werkzeuge der Toolbar ein- oder ausschalten.

"Durchführung" und "Toolbar" bietet der Assistent nur an, wenn mindestens ein Kurs ausgewählt ist, und übernimmt die Änderungen nur bei Kursen.

#### Bereich "Administrative Freigabe" {: #bulk_administrative_access}

Sollen mehrere Lernressourcen einer anderen Organisation zugeordnet werden, etwa nach einer Umstrukturierung, passen Sie ihre Administrative Freigabe hier für alle gleichzeitig an. Was die Administrative Freigabe bewirkt, beschreibt die Seite [Kurseinstellungen - Tab Freigabe](../learningresources/Course_Settings_Share.de.md#section_share). Den Bereich gibt es nur, wenn das Modul Organisationen eingeschaltet ist.

![Markierte Felder Organisation hinzufügen und Organisation entfernen, hier für 2 Lernressourcen](assets/autorenbereich_sammelaktion_administrative_freigabe_v1_de.png){ class="shadow lightbox" title="Schritt Administrative Freigabe im Assistenten Einstellungen bearbeiten" }

Der Bereich hat zwei Felder:

* "Organisation hinzufügen" bietet die Organisationen an, in denen Sie Autor:in, Lernressourcenverwalter:in oder Administrator:in sind.
* "Organisation entfernen" bietet die Organisationen an, denen die ausgewählten Lernressourcen zugeordnet sind.

Eine Lernressource bleibt immer mindestens einer Organisation zugeordnet. OpenOlat entfernt eine Organisation deshalb nur, wenn der Lernressource danach noch eine ihrer bisherigen Organisationen bleibt. Wählen Sie nur Organisationen zum Entfernen aus und bliebe eine Lernressource danach ohne Organisation, zeigt der Bereich den Hinweis "Einige Organisationen können nicht aus den Lernressourcen entfernt werden, da sie die einzige Organisation der Lernressource sind."

Eine Organisation, die Sie im selben Durchlauf hinzufügen, zählt dabei nicht mit. Wählen Sie die neue Organisation zum Hinzufügen und die bisherige zum Entfernen, fügt OpenOlat die neue hinzu und behält die bisherige, ohne einen Hinweis anzuzeigen. Um Lernressourcen in eine andere Organisation zu verschieben, führen Sie den Assistenten deshalb zweimal aus:

1. Wählen Sie im ersten Durchlauf unter "Organisation hinzufügen" die neue Organisation und schliessen Sie den Assistenten ab.
2. Wählen Sie im zweiten Durchlauf unter "Organisation entfernen" die bisherige Organisation.

Administrator:innen ordnen Kurse zudem in der System-Administration im Tab "Lernressourcen" einer Organisation zu, beschrieben unter [Modul Organisationen](../../manual_admin/administration/Modules_Organisations.de.md#edit_learning_resources).

### Kopieren {: #copy}

Mit dem **Button "Kopieren" über der Tabelle** können Sie **mehrere Lernressourcen** kopieren.<br>
Durch Anklicken von "Kopieren" im **Menü, das unter den 3 Punkten am Ende einer Zeile erscheint**, kopieren Sie eine **einzelne Lernressource**. (Die Lernressource dieser Tabellenzeile.)

Wählen Sie eine oder mehrere Lernressourcen aus um sie zu kopieren. Beispielsweise zur Wiederverwendung für ein neues Semester oder um eine Sicherheitskopie zu erstellen.

Kopierte Lernressourcen befinden sich anschliessend im Tab "Meine Einträge". Der Zusatz ("Kopie") wird dem Titel hinzugefügt. Der Titel kann aber anschliessend nach Wunsch geändert werden.

### Löschen {: #delete}

Eine Lernressource kann nur von den Besitzer:innen der Lernressource sowie Lernressourcenverwalter:innen und Administrator:innen gelöscht werden.

Mit dem **Button über der Tabelle** können Sie schnell **mehrere Lernressourcen auf einmal** löschen.<br>
Wollen Sie nur eine **einzelne Lernressource** löschen, können Sie auch auf die **3 Punkte am Ende der betreffenden Tabellenzeile** klicken und dann auf die Option "Löschen".

Sie müssen diese Aktion zur Sicherheit noch einmal im Menü bestätigen. Die Besitzer:innen der Lernressource werden, sofern konfiguriert, per E-Mail benachrichtigt.

Nach dem Löschen erscheinen die Lernressourcen nur noch im [Tab "**Gelöscht**"](../area_modules/Authoring.de.md#authoring-deleted) (Papierkorb-Funktion) für die jeweiligen Besitzer:innen sowie Lernressourcenverwalter:innen und Administrator:innen.

Als Besitzer:in können Sie gelöschte Lernressourcen wiederherstellen. Das dauerhafte Löschen der Lernressourcen ist nur durch Administrator:innen oder Lernressourcenverwalter:innen möglich.

### Lernressource öffnen {: #open_resource}

Ein Klick auf den **Titel** einer Lernressource öffnet die entsprechende Ressource.

### Einstellungen [:octicons-tag-16:{ title="ab Release 21.1 (OO-9780)" }](https://track.frentix.com/issue/OO-9780){:target="_blank"} {: #settings}

Wollen Sie die Angaben einer Lernressource ändern, öffnen Sie ihre Einstellungen direkt aus der Tabelle. Klicken Sie dazu im Menü unter den 3 Punkten auf "Einstellungen". OpenOlat öffnet die Einstellungen der Lernressource im Tab "Metadaten". Die Informationen, die auf der Infoseite erscheinen, etwa Beschreibung, Lernziele und Voraussetzungen, bearbeiten Sie im Tab "Info".

Die Infoseite selbst öffnen Sie in der Lernressource über den Link "Infoseite" in der Toolbar.

Mehr dazu finden Sie auf der Seite "[Infoseite einrichten](../learningresources/Course_Settings_Info.de.md#configure_info)".

### Editor öffnen {: #open_editor}

Um den Inhalt einer Lernressource zu bearbeiten, öffnen Sie ihren Editor direkt aus der Tabelle. Der Eintrag im Menü unter den 3 Punkten nennt den Editor beim Namen: bei einem Kurs "Kurseditor", bei einem Test "Testeditor", bei einem Formular "Formulareditor" und bei einem Video "Videoeditor". Bei allen übrigen Lernressourcen, etwa CP-Lerninhalt, Wiki, Blog, Podcast oder Glossar, heisst der Eintrag "Inhalt editieren".

Den Eintrag sehen Sie nur bei Lernressourcen, die sich bearbeiten lassen und die weder im Status "Beendet" noch im Papierkorb sind.

Denselben Editor öffnet das Stiftsymbol in der Spalte "Inhalt editieren". Diese Spalte blenden Sie bei Bedarf selbst ein, siehe [Spalten konfigurieren](Authoring.de.md#configure_columns). Der Tooltip des Symbols nennt den Editor beim Namen.

### Weitere Optionen für einzelne Lernressourcen {: #row_menu}

Ein Klick auf die **3 Punkte** am Ende einer Tabellenzeile öffnet ein Menü mit mehreren Optionen.

Aktionen im Menü unter den 3 Punkten beziehen sich immer auf die **einzelne Lernressource** dieser Zeile. Mit den Buttons über der Tabelle führen Sie dagegen Aktionen für **mehrere Lernressourcen** aus.

Die Einträge "Einstellungen", der Eintrag zum Editor und "Mitgliederverwaltung" erscheinen nur, wenn Sie Besitzer:in der Lernressource, Lernressourcenverwalter:in oder Administrator:in sind.

### Mitgliederverwaltung {: #members_management}

Hier organisieren Sie die Mitglieder einer Lernressource. Mehr Informationen dazu finden Sie im Kapitel [Mitgliederverwaltung](../learningresources/Members_management.de.md).

### Inhalt exportieren {: #export_content}

Hiermit exportieren Sie Ihre Lernressourcen als ZIP-Datei, zum Beispiel als Backup oder für den Import in einem anderen System.

### Als Lernpfad duplizieren {: #duplicate_as_learning_path}

Handelt es sich in der Tabellenzeile um einen herkömmlichen Kurs, zeigt das Menü zusätzlich die Option "Als Lernpfad duplizieren" an. Ein neuer, konvertierter [Lernpfad-Kurs](../learningresources/Learning_path_course.de.md) wird als Kopie erstellt, die Ursprungsversion bleibt als herkömmlicher Kurs erhalten.

### Kopieren mit Wizard [:octicons-tag-16:{ title="ab Release 16.0 (OO-4416)" }](https://track.frentix.com/issue/OO-4416){:target="_blank"} {: #copy_with_wizard}

Handelt es sich in der Tabellenzeile um einen Lernpfad-Kurs, zeigt das Menü zusätzlich die Option "Kopieren mit Wizard" an.

[Zum Seitenanfang ^](#authoring_bulk_actions)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kurseinstellungen - Tab Freigabe >](../learningresources/Course_Settings_Share.de.md)<br>
[Modul Organisationen >](../../manual_admin/administration/Modules_Organisations.de.md)<br>
[Autorenbereich - Übersicht >](Authoring.de.md)<br>
[Kurseinstellungen - Tab Info >](../learningresources/Course_Settings_Info.de.md)<br>
[Mitgliederverwaltung >](../learningresources/Members_management.de.md)<br>
[Lernpfadkurs - Überblick >](../../manual_user/learningresources/Learning_path_course.de.md)

**Weiterführend**<br>
[Kurs erstellen >](../../manual_user/learningresources/Creating_Course.de.md)<br>
[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../../manual_how-to/my_first_course/my_first_course.de.md)<br>
[Kursbausteine im Kurseditor >](../../manual_user/learningresources/General_Configuration_of_Course_Elements.de.md)<br>
[Wie kann ich meine Kurse durch Suchmaschinen finden lassen? >](../../manual_how-to/oai_pmh/oai_pmh.de.md)

[Zum Seitenanfang ^](#authoring_bulk_actions)
