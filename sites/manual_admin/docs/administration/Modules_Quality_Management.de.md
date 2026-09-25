# Modul Qualitätsmanagement {: #Modules_Quality_Management}

Das Modul "Qualitätsmanagement" ist ein Zusatzmodul. 
Es muss zunächst von einem/einer Administrator:in aktiviert werden.

Die Konfiguration des Moduls erfolgt durch Administrator:innen in der System-Administration unter<br>
`Administration > Module > Qualitätsmanagement`.

![Qualitätsmanagement in der System-Administration: Schalter für Modul, Verbesserungsvorschlag, Datenerhebungsvorschau und Massnahmen To-Dos, dazu E-Mail-Felder für Absender und Empfänger](assets/modules_quality_management_v1_de.png){ class="shadow lightbox" }

## Einstellungen Qualitätsmanagement {: #settings_qm}

Mit der ersten Checkbox wird das gesamte Modul aktiviert.

Die optionale Mailadresse kann für eine individuelle Anpassung verwendet werden:<br>
Bei jeder Datenerhebung wird definiert, an wen Mails automatisch verschickt werden.
Die Mails werden grundsätzlich von OpenOlat mit der Standardadresse (no-reply) verschickt.
Durch Angabe einer anderen E-Mail in diesem Abschnitt, kann diese Adresse übersteuert werden.
Im Feld "Absender Name" legen Sie den angezeigten Namen des Absenders fest.


## Einstellungen Verbesserungsvorschlag [:octicons-tag-16:{ title="ab Release 13.0 (OO-3740)" }](https://track.frentix.com/issue/OO-3740) {: #settings_improvement}

Wird die Option aktiviert, wird unter dem Menüpunkt Qualitätsmanagement die Option zur Erstellung von Verbesserungsvorschlägen angezeigt. Die dort erstellten Mails werden an die hier angegebene Mailadresse geschickt.


## Datenerhebungsvorschau [:octicons-tag-16:{ title="ab Release 18.2 (OO-7399)" }](https://track.frentix.com/issue/OO-7399) {: #data_collection_preview}

Diese Vorschau wird nach der Aktivierung angezeigt

* in Kursen
* in Produkten
* im Modul "Qualitätsmanagement"

Wird die Option aktiviert, ist für Kursbesitzer:innen im Menü der Kursadministration die Option "Datenerhebungsvorschau" angezeigt. Dort können die geplanten Erhebungen eingesehen werden, die diesen Kurs betreffen. Für Kursbesitzer:innen ist diese Vorschau rein informativ. Eine Bearbeitung ist lediglich für Qualitätsmanager:innen möglich.

Siehe [Benutzerhandbuch](../../manual_user/learningresources/Data_Collection_Previews.de.md)

Ausserdem kann die Datenerhebungsvorschau in Produkten aufgerufen werden und zeigt dort alle Erhebungen, die eines der Elemente betreffen.

Die Datenerhebungsvorschau im Modul "Qualitätsmanagement" bezieht sich auf alle geplanten Erhebungen (nicht nur auf einzelne Kurse). 


## Massnahmen To-dos [:octicons-tag-16:{ title="ab Release 18.0 (OO-6781)" }](https://track.frentix.com/issue/OO-6781) {: #to_do}

In OpenOlat können an verschiedenen Stellen To-dos erstellt werden (Projekte, Aufgaben, usw.). Im Qualitätsmanagement redet man in der Regel eher von "Massnahmen" als Reaktion auf Erkenntnisse aus einer oder mehreren Erhebungen. Eine "Massnahme" im Qualitätsmanagement ist ein To-do. 

Wird diese Option aktiviert, können Qualitätsmanager:innen To-dos (Massnahmen) erstellen.


## Aktivierung des Bereichs {: #site_activation}

Damit Qualitätsmanager:innen das Qualitätsmanagement in der Hauptnavigation finden, braucht es neben dem aktivierten Modul auch den aktivierten [Bereich](../../manual_user/area_modules/index.de.md) "Qualitätsmanagement". Sie aktivieren ihn in der System-Administration unter:<br>
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