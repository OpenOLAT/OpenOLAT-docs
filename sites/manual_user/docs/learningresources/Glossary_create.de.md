# Glossar erstellen {: #glossary_create}


## Wo wird ein neues Glossar erstellt? {: #where}

Glossare können wie andere Lernressourcen im **Autorenbereich** erstellt werden.

![Aufgeklapptes Menü Erstellen mit dem markierten Eintrag Glossar](assets/glossary_create_authoring_v1_de.png){ class="shadow lightbox" title="Seite Autorenbereich" }

Alternativ kann die Erstellung auch direkt im Kurs unter `Kurs > Administration > Einstellungen > Tab "Optionen"` aufgerufen werden.
Sie finden dort den Button (4), der ein Popup-Fenster öffnet, in dem ein vorhandenes Glossar ausgewählt oder eine neue Glossar-Lernressource erstellt werden kann.

![Nummerierte Klickfolge Administration, Einstellungen, Tab Optionen, Button Glossar wählen](assets/glossary_create_settings_v1_de.png){ class="shadow lightbox" title="Kurseinstellungen" }

!!! note "Hinweis"

    Es können mehrere Glossare im Autorenbereich erstellt werden. Eingebunden werden kann aber pro Kurs jeweils nur 1 Glossar.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossareinträge erstellen {: #create_entries}

``1.`` Gehen Sie in den **Autorenbereich** und öffnen Sie das Glossar. <br>
(Klick auf den Namen oder Klick auf den Edit-Button oder "Edit" unter dem Icon mit den 3 Punkten.)

![Zeile Glossar mit Titel, Bearbeiten-Symbol und Drei-Punkte-Menü markiert](assets/glossary_authoring_edit_v1_de.png){ class="shadow lightbox" title="Liste im Autorenbereich" }

``2.`` Klicken Sie einen der Buttons **"Eintrag hinzufügen"**.

![Zwei Buttons Eintrag hinzufügen markiert, oben rechts und über dem alphabetischen Register](assets/glossary_add_entry_v1_de.png){ class="shadow lightbox" title="Seite Glossar" }


``3.`` Tragen Sie den gewünschten Fachausdruck ein. Sie können auch Synonyme ergänzen. Zum Beispiel kann der Begriff "Informationstechnologie" mit dem Synonym "IT" ergänzt werden. 

``4.`` Speichern Sie den Begriff. Dadurch wird der Tab für die Eingabe der Definition frei geschaltet.

![Pflichtfeld Begriff, Feld Synonyme und noch inaktiver Tab Definition](assets/glossary_edit_entry_v1_de.png){ class="shadow lightbox" title="Dialog Begriff hinzufügen" }

``5.`` Im Tab "Definition" ergänzen Sie dann die konkrete Definition des Begriffs. Eingetragene Begriffe können auch im Nachhinein geändert oder gelöscht werden.

![Aktiver Tab Definition mit Rich-Text-Editor zur Eingabe der Begriffserklärung](assets/glossary_entry_definition_v1_de.png){ class="shadow lightbox" title="Dialog Begriff hinzufügen" }


Auch Lernende können ein Glossar inhaltlich befüllen. Wie Sie allen Benutzer:innen das Schreibrecht geben, beschreibt die Seite [Glossar: Administration](Glossary_administration.de.md#tab_write_permissions).

### Schreibrecht nur für ausgewählte Benutzer:innen {: #write_selected_users}

Möchte man nur bestimmten Personen (z.B. den Teilnehmenden eines Kurses) das Schreibrecht für ein Glossar vergeben, geht man einen anderen Weg. Hierfür wird die Mitgliederverwaltung eines Kurses verwendet. Erstellen Sie dort eine neue Gruppe und fügen Sie die gewünschten Personen als Teilnehmer:innen dieser Gruppe hinzu. Gehen Sie anschliessend in der Mitgliederverwaltung des Kurses in den Bereich "Rechte" und setzen Sie bei den Kursteilnehmer:innen der Gruppe den Haken für das Recht "Glossar-Werkzeug". Nun können die Personen der Gruppe Glossareinträge hinzufügen und ändern. Was das Recht freigibt, beschreibt der Abschnitt [Glossar-Werkzeug](Members_management.de.md#right_glossary_tool).

!!! info "Wichtig"

    Die Besitzer:innen eines Kurses sind nicht automatisch auch Besitzer:innen der Lernressource "Glossar". Im Kurs bearbeiten sie das eingebundene Glossar trotzdem: Sie öffnen es über das Werkzeug "Glossar" in der Toolbar des Kurses und erstellen, ändern und löschen dort Einträge.

    Öffnen Sie das Glossar dagegen als Lernressource, zum Beispiel im Autorenbereich, bearbeiten nur die Besitzer:innen der Lernressource "Glossar" die Einträge. Sollen weitere Kursbesitzer:innen auch dort arbeiten, tragen Sie sie als Besitzer:innen der Lernressource "Glossar" ein.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossar gestalten {: #design}

Die Erklärungen (Definitionen) können mit einem einfachen Editor bearbeitet werden, der neben Text Ergänzungen zulässt, wie

* Schriftartwahl
* Einrückungen
* Tabellen
* Links
* u.a.

Ob das Glossar die Begriffe über ein alphabetisches Register nach Anfangsbuchstaben gliedert, legen Sie in den Einstellungen des Glossars fest, siehe [Glossar: Administration](Glossary_administration.de.md#tab_register).


[Zum Seitenanfang ^](#glossary_create)

---


## Glossar einbinden {: #integrate}

Glossare sind OpenOlat-Lernressourcen, die normalerweise in einen Kurs eingebunden werden. Darüber hinaus ist auch eine Nutzung als Stand-alone-Lernressource möglich. In diesem Fall kann das Glossar dann z.B. auch als eigenständiges Angebot im Katalog angezeigt werden.

Systemadministrator:innen müssen die Glossarfunktion nicht eigens einschalten.

``1.`` Um ein Glossar in einen Kurs einzubinden, wählen Sie im ersten Schritt die Lernressource unter `Kurs > Administration > Einstellungen > Tab "Optionen"` aus.

![Nummerierte Klickfolge Administration, Einstellungen, Tab Optionen, Button Glossar wählen](assets/glossary_create_settings_v1_de.png){ class="shadow lightbox" title="Kurseinstellungen" }

``2.`` Damit das eingebundene Glossar in der Toolbar des Kurses sichtbar wird, muss noch die Anzeige als Werkzeug gewählt werden. Wählen Sie die entsprechende Checkbox unter `Kurs > Administration > Einstellungen > Tab "Toolbar"`.

![Tab Toolbar mit der aktivierten Checkbox Glossar unter Werkzeuge in Toolbar aktivieren](assets/glossary_settings_toolbar_activate_v1_de.png){ class="shadow lightbox" title="Kurseinstellungen" }



!!! note "Hinweis"

    Es kann pro Kurs jeweils nur 1 Glossar eingebunden werden. Im Autorenbereich können dagegen mehrere Glossar-Lernressourcen vorhanden sein, so dass in verschiedenen Kursen unterschiedliche Glossare verwendet werden können.



Wenn Sie das Glossar nicht mehr verwenden oder ein anderes Glossar in Ihren Kurs einbinden möchten, können Sie unter `Kurs > Administration > Einstellungen > Tab "Optionen"` eine andere Glossar-Lernressource auswählen.


---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Glossar: Administration >](Glossary_administration.de.md)<br>
[Mitgliederverwaltung >](Members_management.de.md)

**Weiterführend**<br>
[Glossar verwenden >](../learningresources/Glossary_usage.de.md)

[Zum Seitenanfang ^](#glossary_create)
