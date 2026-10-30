# Modul Qualitätsmanagement {: #Modules_Quality_Management}

Mit dem Qualitätsmanagement planen Qualitätsverwalter:innen Datenerhebungen, werten sie aus und leiten Massnahmen ab. Das Modul ist standardmässig ausgeschaltet. Administrator:innen schalten es in der System-Administration ein und legen dort die zugehörigen Optionen fest:<br>
`Administration > Module > Qualitätsmanagement`

![Schalter für Modul, Verbesserungsvorschlag, Datenerhebungsvorschau und Massnahmen To-Dos, dazu E-Mail-Felder für Absender und Empfänger](assets/modules_quality_management_v1_de.png){ class="shadow lightbox" title="Modul Qualitätsmanagement in der System-Administration" }

## Einstellungen Qualitätsmanagement {: #settings_qm}

!!! info "frentix-Kund:innen"
    Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix die Aktivierung.

Die Checkbox "Qualitätsmanagement" schaltet das Modul ein.

Die E-Mails des Qualitätsmanagements, etwa Einladungen und Erinnerungen zu einer Datenerhebung, verschickt OpenOlat mit der Standardadresse der Instanz (no-reply). An wen sie gehen, legen Sie in jeder Datenerhebung fest. Soll eine eigene Adresse als Absender erscheinen, tragen Sie sie im Feld "Absender E-Mail-Adresse" ein. Im Feld "Absender Name" legen Sie den angezeigten Namen des Absenders fest.


## Einstellungen Verbesserungsvorschlag [:octicons-tag-16:{ title="ab Release 13.0 (OO-3740)" }](https://track.frentix.com/issue/OO-3740) {: #settings_improvement}

Mit einem Verbesserungsvorschlag geben Personen ihr Feedback direkt an die Verantwortlichen weiter. Ist die Checkbox "Verbesserungsvorschlag" gesetzt, bietet die Startseite des Qualitätsmanagements den Link "Verbesserungsvorschlag erstellen" an. Jeder Vorschlag geht als E-Mail an die Adressen im Feld "Empfänger E-Mail-Adressen". In den Feldern "E-Mail Betreff (Vorlage)" und "E-Mail Nachricht (Vorlage)" geben Sie den Betreff und den Text vor, mit denen das Formular des Vorschlags beginnt.


## Datenerhebungsvorschau [:octicons-tag-16:{ title="ab Release 18.2 (OO-7399)" }](https://track.frentix.com/issue/OO-7399) {: #data_collection_preview}

Mit der Datenerhebungsvorschau sehen die Verantwortlichen eines Kurses früh, welche Erhebungen ihren Kurs betreffen werden. Die Checkbox "Datenerhebungsvorschau" ist standardmässig gesetzt. Die Vorschau erscheint dann an drei Orten:

* in Kursen
* in Produkten
* im Modul "Qualitätsmanagement"

Im Kurs erscheint im Menü der Kurs-Administration der Eintrag "Datenerhebungsvorschau" für Besitzer:innen und Betreuer:innen des Kurses sowie für Administrator:innen, Lernressourcenverwalter:innen und Principals. Dort sehen sie die geplanten Erhebungen, die diesen Kurs betreffen. Im Kurs ist die Vorschau rein informativ. Bearbeiten können die Erhebungen nur Qualitätsverwalter:innen.

Siehe [Benutzerhandbuch](../../manual_user/learningresources/Data_Collection_Previews.de.md)

Ausserdem kann die Datenerhebungsvorschau in Produkten im Course Planner aufgerufen werden und zeigt dort alle Erhebungen, die eines der Elemente betreffen.

Die Datenerhebungsvorschau im Modul "Qualitätsmanagement" bezieht sich auf alle geplanten Erhebungen (nicht nur auf einzelne Kurse). 


## Massnahmen To-dos [:octicons-tag-16:{ title="ab Release 18.0 (OO-6781)" }](https://track.frentix.com/issue/OO-6781) {: #to_do}

In OpenOlat können an verschiedenen Stellen To-dos erstellt werden (Projekte, Aufgaben, usw.). Im Qualitätsmanagement redet man in der Regel eher von "Massnahmen" als Reaktion auf Erkenntnisse aus einer oder mehreren Erhebungen. Eine "Massnahme" im Qualitätsmanagement ist ein To-do. 

Ist die Checkbox "Massnahmen To-dos" gesetzt, können Qualitätsverwalter:innen To-dos (Massnahmen) erstellen. Standardmässig ist sie nicht gesetzt.


## Aktivierung des Bereichs {: #site_activation}

Damit Qualitätsverwalter:innen das Qualitätsmanagement in der Hauptnavigation finden, braucht es neben dem aktivierten Modul auch den aktivierten [Bereich](../../manual_user/area_modules/index.de.md) "Qualitätsmanagement". Sie aktivieren ihn in der System-Administration unter:<br>
`Administration > Customizing > Bereiche`

Setzen Sie im Tab "Reihenfolge" in der Zeile "Qualitätsmanagement" die Checkbox in der Spalte "Aktiviert" und legen Sie in der Spalte "Zugang" fest, wer den Bereich in der Hauptnavigation angezeigt bekommt.

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Datenerhebungsvorschau >](../../manual_user/learningresources/Data_Collection_Previews.de.md)<br>
[Bereiche und Module >](../../manual_user/area_modules/index.de.md)

**Weiterführend**<br>
[Customizing: Übersicht >](Customizing.de.md)

[Zum Seitenanfang ^](#Modules_Quality_Management)