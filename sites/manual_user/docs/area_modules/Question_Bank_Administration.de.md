# Fragenpool: Administration {: #question_bank_administration}

## Konfiguration durch Poolverwalter:innen {: #pool_manager}

Poolverwalter:in ist eine [Rolle](../basic_concepts/Roles_Rights.de.md), die Administrator:innen oder Rollenverwalter:innen OpenOlat-Benutzer:innen zuweisen.

Poolverwalter:innen haben das Recht, organisatorische Aspekte des Fragenpools zu ändern. Sie haben jedoch keinen Einfluss auf den Inhalt des Fragenpools und der einzelnen Pools.

Die Administration des Fragenpools umfasst fünf Bereiche zur Organisation des Fragenpools. Administrator:innen sehen alle fünf. Poolverwalter:innen sehen die Bereiche, für die ihnen die System-Administration das Recht erteilt hat, im Abschnitt "Rechte Poolverwalter:in" unter: `Administration > e-Assessment > Fragenpool`. Mehr dazu unter [e-Assessment Administration: Fragenpool](../../manual_admin/administration/eAssessment_Question_bank.de.md).

  * Beurteilungsprozess
  * Fachbereich
  * Pool-Verwaltung
  * Fragetyp
  * Stufe

---

### Beurteilungsprozess [:octicons-tag-16:{ title="ab Release 12.3 (OO-3111)" }](https://track.frentix.com/issue/OO-3111){:target="_blank"} {: #assessment_process}

![Bereich Administration mit Beurteilungsprozess markiert, rechts die Einstellungen Beurteilungsmethode, Anzahl Beurteilungen pro Frage, Sterne-Untergrenze und Sichtbarkeit von finalen Fragen](assets/question_bank_administration_assessment_process_v1_de.png){ class="shadow lightbox" title="Seite Beurteilungsprozess im Bereich Administration" }

Hier legen Sie fest, wann eine Frage den Status "Final" erhält, falls für sie ein Beurteilungsprozess gestartet wurde. Liegt bei der Beurteilungsmethode "Untergrenze" eine Bewertung unterhalb der hier angegebenen Untergrenze, setzt OpenOlat die Frage auf "Revision".

[Zum Seitenanfang ^](#question_bank_administration)

---

### Fachbereich {: #subject}

![Seite Fachbereich mit dem Button Neue Taxonomieebene erstellen und der Tabelle mit Ebene, Kennzeichen, Externe ID und Unterebenen, so sehen Sie, wie Fachbereiche verschachtelt sind](assets/question_bank_administration_subject_v2_de.png){ class="shadow lightbox" title="Seite Fachbereich im Bereich Administration · 2026.11.02" }

Mit Fachbereichen verschlagworten Sie Fragen (Items) nach ihrem Fach. OpenOlat zeigt die Fachbereiche in einer hierarchischen Struktur. Diese bildet z.B. in Ausbildungsorganisationen mögliche Studiengänge ab, in der Privatwirtschaft eventuell Organisationseinheiten.

Hinter den Fachbereichen steht eine [Taxonomie](../../manual_admin/administration/Modules_Taxonomy.de.md). Neue Fachbereiche fügen Sie mit der Schaltfläche "Neue Taxonomieebene erstellen" oder mit "Taxonomieebenen importieren" hinzu. Bestehende Fachbereiche bearbeiten Sie ebenfalls hier.

Damit eine Frage in den Beurteilungsprozess gegeben werden kann, muss ein Fachbereich angegeben werden. Die Beurteilung übernehmen Fachexpert:innen, die in diesem Bereich Kompetenz besitzen. Weil auch die Expert:innen einem Fachbereich zugeordnet sind, lassen sich Frage und Expert:in so einander zuordnen.

[Zum Seitenanfang ^](#question_bank_administration)

---

### Pool-Verwaltung {: #pool}

![Seite Pool-Verwaltung mit dem Button Pool erstellen und der Tabelle zweier Pools mit der Checkbox Öffentlich, Name, Bearbeiten, Besitzer:innen und Löschen](assets/question_bank_administration_pool_admin_v1_de.png){ class="shadow lightbox" title="Seite Pool-Verwaltung im Bereich Administration" }

Ein Pool ist eine Sammlung von Fragen im Fragenpool, über die Autor:innen Testfragen untereinander austauschen.

Neue Pools fügen Sie mit der Schaltfläche "Pool erstellen" hinzu. Bestehende Pools bearbeiten oder löschen Sie in der Tabelle der Pools.

Pools können entweder öffentlich sein (und stehen damit automatisch allen Autor:innen zur Verfügung) oder nicht öffentlich. Bei einem nicht öffentlichen Pool beschränken Sie den Zugriff auf ausgesuchte Personen, zum Beispiel auf die Mitarbeiter:innen einer Abteilung.

![Symbol Pool](assets/share_pool_64_0_434343_none.png){ class="aside-right lightbox" }

Diese Personen fügen Sie dem Pool über den Link "Besitzer:innen" hinzu. Pools erscheinen im Bereich "Freigaben" mit dem nebenstehenden Icon.

![Symbol Gruppenfreigabe](assets/group.png){ class="aside-right lightbox" }

Pools erstellen nur Administrator:innen und Poolverwalter:innen mit dem Recht für die Pool-Verwaltung. Für einen selbst gewählten Personenkreis geben Autor:innen ihre Fragen stattdessen für eine OpenOlat-Gruppe frei. Solche Gruppenfreigaben erscheinen mit dem nebenstehenden Icon.

![Bereich Freigaben mit zwei Pools und einer Gruppe, die Symbole für Pool und Gruppenfreigabe sind markiert](assets/question_bank_administration_pool_type_v1_de.png){ class="shadow lightbox" title="Bereich Freigaben im Fragenpool" }

[Zum Seitenanfang ^](#question_bank_administration)

**Pool erstellen**

![Dialog Pool erstellen mit Name und Öffentlich, dahinter der Button Pool erstellen und die Spalten Bearbeiten und Besitzer:innen, so sehen Sie, wo Sie einen Pool anlegen und ändern](assets/question_bank_administration_pool_create_v2_de.png){ class="shadow lightbox" title="Dialog Pool erstellen in der Pool-Verwaltung · 2026.11.02" }

* **"Pool erstellen"**: Die Schaltfläche öffnet den Dialog "Pool erstellen".
* **"Name"**: Geben Sie den Namen des neuen Pools ein.
* **"Öffentlich"**: Legen Sie fest, ob der Pool öffentlich (für alle Autor:innen sichtbar) oder privat sein soll. Bei einem privaten Pool legen Sie unter "Besitzer:innen" fest, welche Benutzer:innen Zugriff auf den Pool erhalten.
* **"Bearbeiten"**: Für bestehende Pools ändern Sie hier den Namen und die Sichtbarkeit.
* **"Besitzer:innen"**: Fügen Sie Besitzer:innen hinzu oder entfernen Sie diese.

[Zum Seitenanfang ^](#question_bank_administration)

---

### Fragetyp {: #type}

Der Fragetyp gibt an, wie eine Frage aufgebaut ist und wie Teilnehmende sie beantworten, zum Beispiel Single Choice, Lückentext oder Hotspot. Welche Fragetypen OpenOlat bietet, beschreibt die Seite [Test Fragetypen](../learningresources/Test_question_types.de.md).

Beim Erstellen einer Frage wählen Sie ihren Fragetyp. Beim Bearbeiten und beim Import bestimmt OpenOlat ihn selbst aus dem Aufbau der Frage. Ändern lässt er sich nicht. Die [Detailansicht](Item_Detailed_View.de.md#metadata_item_analysis) einer Frage zeigt ihn im Metadatum "Typ" im Bereich "Itemanalyse". In den Fragenlisten finden Sie die Fragen eines Typs mit dem Filter "Typ".

**Fragetyp beim Import**

Beim Import einer ZIP-Datei oder eines Tests aus dem Autorenbereich erkennt OpenOlat den Fragetyp jeder Frage aus ihrem Inhalt. Sie müssen nichts angeben.

Beim [Excelimport](Question_Bank_Import_Questions.de.md#excelimport) legt die Zeile "Type" den Fragetyp fest. Ohne diese Zeile und einen der zehn Werte aus der Vorlage übernimmt OpenOlat die Frage nicht als eigene Frage. Prüfen Sie deshalb vor dem Import, dass jede Frage mit der Zeile "Type" beginnt. Der Schritt "Übersicht" des Imports zeigt, welche Fragen OpenOlat mit welchem Fragetyp erkannt hat.

[Zum Seitenanfang ^](#question_bank_administration)

---

### Stufe {: #level}

![Seite Stufe mit dem Button Stufe erstellen und den drei Stufen Grundstufe, Aufbaustufe und Expertenstufe mit Übersetzung und Löschen](assets/question_bank_administration_level_v1_de.png){ class="shadow lightbox" title="Seite Stufe im Bereich Administration" }

Mit Stufen ordnen Sie Fragen zusätzlich ein, vergleichbar mit einer Schwierigkeitsstufe. Hier erstellen Sie die Stufen, die den Ausbildungsleveln in Ihrem Kontext entsprechen.

Die Stufe einer Frage weisen Sie in der [Detailansicht](Item_Detailed_View.de.md#metadata_general) im Metadatum "Stufe" unter "Allgemein" zu. So ordnen Sie zum Beispiel die Schwierigkeit einer Frage einer Stufe zu.

Beispiele für Stufen im schulischen Kontext sind:

* Unterstufe
* Oberstufe
* Gymnasium
* Bachelor
* Master 

In einem Unternehmenskontext könnten Stufen so aussehen:

* ohne Berufsausbildung
* mit Berufsausbildung
* Führungsfunktion
* Administration
* Kader
* Management

Neue Stufen erstellen Sie mit dem Button "Stufe erstellen" rechts oben.

Übersetzen Sie jede Stufe in jede Sprache, die in Ihrer OpenOlat-Instanz eingeschaltet ist. Klicken Sie dazu in der Spalte "Übersetzung" auf die Zeile der Stufe. Der Dialog "Übersetzung" zeigt ein Feld für jede eingeschaltete Sprache. Tragen Sie den Namen der Stufe in jeder Sprache ein und klicken Sie auf "OK".

[Zum Seitenanfang ^](#question_bank_administration)

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Rollen und Rechte: Übersicht >](../basic_concepts/Roles_Rights.de.md)<br>
[e-Assessment Administration: Fragenpool >](../../manual_admin/administration/eAssessment_Question_bank.de.md)<br>
[Modul Taxonomie >](../../manual_admin/administration/Modules_Taxonomy.de.md)<br>
[Test Fragetypen >](../learningresources/Test_question_types.de.md)<br>
[Fragenpool: Detailansicht einer Frage und Metadaten >](Item_Detailed_View.de.md)<br>
[Fragenpool: Fragen importieren >](Question_Bank_Import_Questions.de.md)

**Weiterführend**<br>
[Fragenpool: Beurteilungsprozess >](Question_Bank_Review_Process.de.md)<br>
[Fragenpool: Freigabemöglichkeiten >](Question_Pool_Sharing_Options.de.md)

[Zum Seitenanfang ^](#question_bank_administration)
