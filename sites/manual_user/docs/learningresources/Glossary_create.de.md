# Glossar erstellen {: #glossary_create}


## Wo wird ein neues Glossar erstellt? {: #where}

Glossare können wie andere Lernressourcen im **Autorenbereich** erstellt werden.

![Aufgeklapptes Menü Erstellen mit dem markierten Eintrag Glossar, Seite Autorenbereich.](assets/glossary_create_authoring_v1_de.png){ class="shadow lightbox" }

Alternativ kann die Erstellung auch direkt im Kurs unter `Kurs > Administration > Einstellungen > Tab "Optionen"` aufgerufen werden.
Sie finden dort den Button (4), der ein Popup-Fenster öffnet, in dem ein vorhandenes Glossar ausgewählt oder eine neue Glossar-Lernressource erstellt werden kann.

![Nummerierte Klickfolge Administration, Einstellungen, Tab Optionen, Button Glossar wählen in den Kurseinstellungen.](assets/glossary_create_settings_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Es können mehrere Glossare im Autorenbereich erstellt werden. Eingebunden werden kann aber pro Kurs jeweils nur 1 Glossar.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossareinträge erstellen {: #create_entries}

``1.`` Gehen Sie in den **Autorenbereich** und öffnen Sie das Glossar. <br>
(Klick auf den Namen oder Klick auf den Edit-Button oder "Edit" unter dem Icon mit den 3 Punkten.)

![Zeile Glossar mit Titel, Bearbeiten-Symbol und Drei-Punkte-Menü markiert, Liste im Autorenbereich.](assets/glossary_authoring_edit_v1_de.png){ class="shadow lightbox" }

``2.`` Klicken Sie einen der Buttons **"Eintrag hinzufügen"**.

![Zwei Buttons Eintrag hinzufügen markiert, oben rechts und über dem alphabetischen Register, auf der Seite Glossar.](assets/glossary_add_entry_v1_de.png){ class="shadow lightbox" }


``3.`` Tragen Sie den gewünschten Fachausdruck ein. Sie können auch Synonyme ergänzen. Zum Beispiel kann der Begriff "Informationstechnologie" mit dem Synonym "IT" ergänzt werden. 

``4.`` Speichern Sie den Begriff. Dadurch wird der Tab für die Eingabe der Definition frei geschaltet.

![Dialog Begriff hinzufügen mit Pflichtfeld Begriff, Feld Synonyme und noch inaktivem Tab Definition.](assets/glossary_edit_entry_v1_de.png){ class="shadow lightbox" }

``5.`` Im Tab "Definition" ergänzen Sie dann die konkrete Definition des Begriffs. Eingetragene Begriffe können auch im Nachhinein geändert oder gelöscht werden.

![Aktiver Tab Definition mit Rich-Text-Editor zur Eingabe der Begriffserklärung, im Dialog Begriff hinzufügen.](assets/glossary_entry_definition_v1_de.png){ class="shadow lightbox" }


Es kann ermöglicht werden, dass auch Lernende ein Glossar inhaltlich befüllen können.

### Schreibrecht für alle Benutzer:innen

In der Lernressource "Glossar" kann unter `Glossar > Administration > Einstellungen > Tab "Schreibberechtigung"` definiert werden, ob nur die Besitzer:innen der Lernressource Beiträge erstellen und editieren dürfen oder ob auch Benutzer:innen das Recht erhalten.

**Besitzer:innen** der jeweiligen Lernressource "Glossar" können grundsätzlich alle erstellten Glossarbeiträge ändern und löschen. Standardmässig können neue Glossareinträge nur von den Kursbesitzer:innen vorgenommen werden.

Die Auswahl "Schreibberechtigung für alle Benutzer:innen" erlaubt es **allen Systembenutzer:innen** neue Glossarbeiträge zu erstellen.
Wer einen Glossarbeitrag erstellt hat, kann diesen selbst erstellten Beitrag anschliessend auch ändern und wieder löschen. 
Die Besitzer:innen eines Glossars können dagegen alle Beiträge - auch die von anderen Benutzer:innen erstellten - jederzeit ändern oder löschen.

Wenn diese Funktion eingeschaltet ist, wird die jeweilige Urheber:in und die letzte Person, die Änderungen vorgenommen hat, neben dem Glossarbeitrag angezeigt.

![Tab Schreibberechtigung mit Erläuterungstext und der noch deaktivierten Checkbox für die Schreibberechtigung aller Benutzer:innen, in den Glossar-Einstellungen.](assets/glossary_settings_write_v1_de.png){ class="shadow lightbox" }



### Schreibrecht nur für ausgewählte Benutzer:innen

Möchte man nur bestimmten Personen (z.B. den Teilnehmenden eines Kurses) das Schreibrecht für ein Glossar vergeben, geht man einen anderen Weg. Hierfür wird die **Mitgliederverwaltung** eines Kurses verwendet. Erstellen Sie dort eine neue **Gruppe** und fügen Sie die gewünschten Personen als Teilnehmer:innen dieser Gruppe hinzu. Gehen Sie anschliessend in der Mitgliederverwaltung des Kurses in den Bereich **"Rechte"** und setzen Sie bei den Kursteilnehmer:innen der Gruppe den Haken für das Recht **"Glossarwerkzeug"**. Nun können die Personen der Gruppe Glossareinträge hinzufügen und ändern.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossar gestalten {: #design}

Die Erklärungen (Definitionen) können mit einem einfachen Editor bearbeitet werden, der neben Text Ergänzungen zulässt, wie

* Schriftartwahl
* Einrückungen
* Tabellen
* Links
* u.a.

Das alphabetische Register ist für ein lateinisches Alphabet ausgelegt und beinhaltet die Zeichen von A-Z. Für ein Glossar mit anderem Zeichensatz sollte die Checkbox "Register einschalten" deaktiviert werden.

`Glossar > Administration > Einstellungen > Tab "Alphabetisches Register"`

![Tab Alphabetisches Register mit Erläuterungstext und aktivierter Checkbox Register einschalten, in den Glossar-Einstellungen.](assets/glossary_settings_register_v1_de.png){ class="shadow lightbox" }



!!! info "Wichtig"

    Die Besitzer:innen eines Kurses sind nicht automatisch auch Besitzer:innen der Lernressource. Wurde eine Lernressource "Glossar" von einer anderen Person erstellt, können nicht automatisch die Besitzer:innen des Kurses, in dem die Lernressource eingebunden wurde, auch Einträge im Glossar vornehmen.

    Damit die anderen Kursbesitzer:innen Änderungen vornehmen können, muss eine der beschriebenen Berechtigungen eingerichtet werden oder die gewünschten Kursbesitzer:innen müssen auch als Besitzer:innen der jeweiligen Lernressource "Glossar" eingetragen werden.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossar einbinden {: #integrate}

Glossare sind OpenOlat-Lernressourcen, die normalerweise in einen Kurs eingebunden werden. Darüber hinaus ist auch eine Nutzung als Stand-alone-Lernressource möglich. In diesem Fall kann das Glossar dann z.B. auch als eigenständiges Angebot im Katalog angezeigt werden.

Eine generelle Aktivierung der Glossarfunktion durch Administrator:innen ist nicht erforderlich.

``1.`` Um ein Glossar in einen Kurs einzubinden, wählen Sie im ersten Schritt die Lernressource unter `Kurs > Administration > Einstellungen > Tab "Optionen"` aus.

![Nummerierte Klickfolge Administration, Einstellungen, Tab Optionen, Button Glossar wählen in den Kurseinstellungen.](assets/glossary_create_settings_v1_de.png){ class="shadow lightbox" }

``2.`` Damit das eingebundene Glossar in der Toolbar des Kurses sichtbar wird, muss noch die Anzeige als Werkzeug gewählt werden. Wählen Sie die entsprechende Checkbox unter `Kurs > Administration > Einstellungen > Tab "Toolbar"`.

![Tab Toolbar mit der aktivierten Checkbox Glossar unter Werkzeuge in Toolbar aktivieren, in den Kurseinstellungen.](assets/glossary_settings_toolbar_activate_v1_de.png){ class="shadow lightbox" }



!!! note "Hinweis"

    Es kann pro Kurs jeweils nur 1 Glossar eingebunden werden. Im Autorenbereich können dagegen mehrere Glossar-Lernressourcen vorhanden sein, so dass in verschiedenen Kursen unterschiedliche Glossare verwendet werden können.



Wenn Sie das Glossar nicht mehr verwenden oder ein anderes Glossar in Ihren Kurs einbinden möchten, können Sie unter `Kurs > Administration > Einstellungen > Tab "Optionen"` eine andere Glossar-Lernressource auswählen.


---

## Weiterführende Informationen {: #further_information}

[Glossar verwenden >](../learningresources/Glossary_usage.de.md)

[Zum Seitenanfang ^](#glossary_create)
