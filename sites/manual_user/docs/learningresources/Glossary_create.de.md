# Glossar erstellen {: #glossary_create}

Sollen Teilnehmende die Fachbegriffe eines Kurses nachschlagen können, legen Sie ein Glossar an, erfassen die Begriffe mit ihren Definitionen und binden das Glossar in den Kurs ein. Die Erklärung eines Begriffs lesen die Teilnehmenden dann direkt im Lerninhalt, ohne den Kurs zu verlassen. Ein Glossar erstellen Personen mit der Rolle Autor:in, Lernressourcenverwalter:in oder Administrator:in.

## Wo wird ein neues Glossar erstellt? {: #where}

Ein Glossar erstellen Sie wie andere Lernressourcen im Autorenbereich:<br>
`Autorenbereich > Erstellen > Glossar`

![Aufgeklapptes Menü Erstellen mit dem markierten Eintrag Glossar](assets/glossary_create_authoring_v1_de.png){ class="shadow lightbox" title="Seite Autorenbereich" }

Sie können ein Glossar auch direkt im Kurs erstellen, unter `Kurs > Administration > Einstellungen > Tab "Optionen"`. Der Button "Glossar wählen" öffnet ein Fenster, in dem Sie ein vorhandenes Glossar auswählen oder ein neues Glossar erstellen.

![Tab Optionen der Kurseinstellungen mit dem markierten Button Glossar wählen, über den Sie ein Glossar auswählen oder neu erstellen](assets/glossary_create_settings_v2_de.png){ class="shadow lightbox" title="Tab Optionen in den Kurseinstellungen · 2026.11.09" }

!!! note "Hinweis"

    Im Autorenbereich erstellen Sie beliebig viele Glossare. In einen Kurs binden Sie jeweils ein Glossar ein.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossareinträge erstellen {: #create_entries}

``1.`` Öffnen Sie das Glossar im Autorenbereich: mit einem Klick auf den Titel, auf das Symbol Bearbeiten oder im Drei-Punkte-Menü der Zeile.

![Zeile Glossar mit Titel, Bearbeiten-Symbol und Drei-Punkte-Menü markiert](assets/glossary_authoring_edit_v1_de.png){ class="shadow lightbox" title="Liste im Autorenbereich" }

``2.`` Klicken Sie auf einen der beiden Buttons "Eintrag hinzufügen".

![Zwei Buttons Eintrag hinzufügen markiert, oben rechts und unter dem alphabetischen Register](assets/glossary_add_entry_v1_de.png){ class="shadow lightbox" title="Seite Glossar" }


``3.`` Tragen Sie den Begriff ein. Sie können Synonyme ergänzen, zum Beispiel zum Begriff "Informationstechnologie" das Synonym "IT".

``4.`` Speichern Sie den Begriff. Danach lässt sich der Tab "Definition" öffnen.

![Pflichtfeld Begriff, Feld Synonyme und noch inaktiver Tab Definition](assets/glossary_edit_entry_v1_de.png){ class="shadow lightbox" title="Dialog Begriff hinzufügen" }

``5.`` Im Tab "Definition" erfassen Sie die Erklärung des Begriffs. Eingetragene Begriffe können Sie später ändern oder löschen.

![Aktiver Tab Definition mit Rich-Text-Editor zur Eingabe der Begriffserklärung](assets/glossary_entry_definition_v1_de.png){ class="shadow lightbox" title="Dialog Begriff hinzufügen" }


Auch Lernende können ein Glossar inhaltlich befüllen. Wie Sie allen Benutzer:innen das Schreibrecht geben, beschreibt die Seite [Glossar: Administration](Glossary_administration.de.md#tab_write_permissions).

### Schreibrecht nur für ausgewählte Benutzer:innen {: #write_selected_users}

Sollen nur bestimmte Personen das Glossar bearbeiten, zum Beispiel einige Teilnehmende eines Kurses, vergeben Sie das Schreibrecht über die Mitgliederverwaltung des Kurses. Erstellen Sie dort eine Gruppe und fügen Sie die Personen als Teilnehmer:innen der Gruppe hinzu. Setzen Sie anschliessend im Bereich "Rechte" der Mitgliederverwaltung bei den Teilnehmer:innen der Gruppe den Haken für das Recht "Glossar-Werkzeug". Danach fügen die Personen der Gruppe Glossareinträge hinzu und ändern sie. Was das Recht freigibt, beschreibt der Abschnitt [Glossar-Werkzeug](Members_management.de.md#right_glossary_tool).

!!! info "Wichtig"

    Die Besitzer:innen eines Kurses sind nicht automatisch auch Besitzer:innen der Lernressource "Glossar". Im Kurs bearbeiten sie das eingebundene Glossar trotzdem: Sie öffnen es über das Werkzeug "Glossar" in der Toolbar des Kurses und erstellen, ändern und löschen dort Einträge.

    Öffnen Sie das Glossar dagegen als Lernressource, zum Beispiel im Autorenbereich, bearbeiten nur die Besitzer:innen der Lernressource "Glossar" die Einträge. Sollen weitere Kursbesitzer:innen auch dort arbeiten, tragen Sie sie als Besitzer:innen der Lernressource "Glossar" ein.


[Zum Seitenanfang ^](#glossary_create)

---


## Glossar gestalten {: #design}

Die Definitionen bearbeiten Sie in einem einfachen Editor. Neben Text bietet er zum Beispiel

* Schriftartwahl
* Einrückungen
* Tabellen
* Links

Ob das Glossar die Begriffe über ein alphabetisches Register nach Anfangsbuchstaben gliedert, legen Sie in den Einstellungen des Glossars fest, siehe [Glossar: Administration](Glossary_administration.de.md#tab_register).


[Zum Seitenanfang ^](#glossary_create)

---


## Glossar einbinden {: #integrate}

Ein Glossar binden Sie meist in einen Kurs ein. Teilnehmende sehen die Begriffe dann im Kurs erklärt. Sie können ein Glossar auch eigenständig verwenden und zum Beispiel als eigenes Angebot im Katalog anbieten.

Glossare stehen in jeder OpenOlat-Instanz zur Verfügung, ohne Einstellung in der System-Administration. Einbinden können es alle, welche die [Kurseinstellungen](Course_Settings/index.de.md) öffnen: Besitzer:innen des Kurses, Lernressourcenverwalter:innen und Administrator:innen, ausserdem Personen mit dem Recht "Kurseditor".

``1.`` Öffnen Sie `Kurs > Administration > Einstellungen > Tab "Optionen"`. Wählen Sie das Glossar mit dem Button "Glossar wählen" aus und klicken Sie auf "Speichern".

![Tab Optionen der Kurseinstellungen mit dem markierten Button Glossar wählen, über den Sie ein Glossar auswählen oder neu erstellen](assets/glossary_create_settings_v2_de.png){ class="shadow lightbox" title="Tab Optionen in den Kurseinstellungen · 2026.11.09" }

``2.`` Schalten Sie das Glossar als Werkzeug ein: Checkbox "Glossar" unter `Kurs > Administration > Einstellungen > Tab "Toolbar"`. Erst damit wirkt das Glossar im Kurs: In der Toolbar erscheint das Menü "Glossar", und die Begriffe lassen sich im Lerninhalt erklären.

![Tab Toolbar der Kurseinstellungen mit der markierten, eingeschalteten Checkbox Glossar unter Werkzeuge in Toolbar aktivieren](assets/glossary_settings_toolbar_activate_v2_de.png){ class="shadow lightbox" title="Tab Toolbar in den Kurseinstellungen · 2026.11.09" }

Im Menü "Glossar" der Toolbar wählen Teilnehmende "Glossarbegriffe in Lerninhalt einblenden". Danach zeigt OpenOlat die Erklärung eines Begriffs, sobald sie im Lerninhalt mit der Maus auf den Begriff zeigen. Mehr dazu auf der Seite [Glossar - Verwendung](Glossary_usage.de.md).

!!! note "Hinweis"

    In einen Kurs binden Sie jeweils ein Glossar ein. Im Autorenbereich können mehrere Glossare bestehen, so dass verschiedene Kurse unterschiedliche Glossare verwenden.



Möchten Sie ein anderes Glossar in Ihren Kurs einbinden, wählen Sie es unter `Kurs > Administration > Einstellungen > Tab "Optionen"` mit "Glossar wählen" aus. Verwenden Sie kein Glossar mehr, entfernen Sie es dort mit "Auswahl löschen" und klicken auf "Speichern". Das Glossar selbst bleibt als Lernressource im Autorenbereich erhalten.

[Zum Seitenanfang ^](#glossary_create)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Glossar: Administration >](Glossary_administration.de.md)<br>
[Mitgliederverwaltung >](Members_management.de.md)<br>
[Kurseinstellungen >](Course_Settings/index.de.md)<br>
[Glossar - Verwendung >](Glossary_usage.de.md)

**Weiterführend**<br>
[Glossar >](Glossary/index.de.md)

[Zum Seitenanfang ^](#glossary_create)
