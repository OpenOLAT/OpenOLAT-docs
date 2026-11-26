# Kurs-Administration: Übersicht {: #course_administration}

![Menü "Administration" eines Lernpfadkurses mit seinen Optionen, von Einstellungen und Mitgliederverwaltung über Kursstatistiken und Kopieren bis Über diesen Kurs und Löschen](../assets/course_administration_v5_de.png){ class="shadow lightbox aside-left-lg" }

:octicons-device-camera-video-24: **Video-Einführung**: [Admin-Funktionen](<https://www.youtube.com/embed/rWPcz6udUrI>){:target="_blank"}


Wollen Sie einen Kurs aufbauen, einrichten oder auswerten, öffnen Sie im Kurs links oben den Button "Administration". Das Menü bündelt alles, was Sie vor und während der Durchführung am Kurs bearbeiten, konfigurieren und verwalten. Als Besitzer:in des Kurses sehen Sie alle Menüpunkte, ebenso Administrator:innen und [Lernressourcenverwalter:innen](../../basic_concepts/Roles/index.de.md#org) der Organisation, der der Kurs angehört. Zu den wichtigsten zählen der [Kurseditor](../General_Configuration_of_Course_Elements.de.md) und die [Einstellungen](../Course_Settings/index.de.md).

[Betreuer:innen](../../basic_concepts/Roles/index.de.md#coach) sehen den Button "Administration" ebenfalls, im Menü aber nur die Menüpunkte für die Betreuung, zum Beispiel das [Bewertungswerkzeug](../Assessment_tool_overview/index.de.md). Personen mit einzelnen Rechten aus dem [Bereich "Rechte" der Mitgliederverwaltung](../Members_management.de.md#section_rights) sehen die Menüpunkte zu diesen Rechten.

!!! info "Wichtig"

    Manche Menüpunkte erscheinen nur, wenn die zugehörige Funktion in OpenOlat eingeschaltet ist. Fehlt Ihnen ein Menüpunkt, wenden Sie sich an Ihre Organisation.


Andere Lernressourcen haben ebenfalls ein Menü "Administration", mit weniger Menüpunkten. Welche es sind, hängt von der Art der Lernressource ab.

Wozu jeder Menüpunkt dient und wo er beschrieben ist, zeigt der Abschnitt [Menüpunkte](#menu_items).


## Kurs-Administration und System-Administration {: #course_vs_system_administration}

In OpenOlat heissen zwei Menüs "Administration": das Menü in einem geöffneten Kurs und der Menüpunkt in der Hauptnavigation. Steht in einer Anleitung nur "Administration", ist deshalb nicht sofort klar, wo Sie suchen. Kennen Sie den Unterschied, finden Sie eine Einstellung auf Anhieb und wissen, ob eine Änderung nur einen Kurs betrifft oder die ganze OpenOlat-Instanz.

![System-Administration gilt für die ganze Instanz, Kurs-Administration nur für den geöffneten Kurs](../assets/course_vs_system_administration_v1_de.svg){ class="shadow lightbox" title="Zwei Menüs namens Administration · 2026.11.12" }

Die Kurs-Administration öffnen Sie im Kurs links oben mit dem Button "Administration". Alles, was Sie dort ändern, gilt nur für diesen einen Kurs: Sie verwalten zum Beispiel die Mitglieder, bauen den Kurs im Kurseditor auf oder legen unter `Kurs > Administration > Einstellungen` seine Einstellungen fest.

Welche Menüpunkte Sie sehen, hängt von Ihrer Rolle und Ihren Rechten im Kurs ab: Besitzer:innen sehen alle, Betreuer:innen weniger, Personen mit einzelnen Rechten aus der Mitgliederverwaltung die Menüpunkte zu diesen Rechten. Zwei Personen im selben Kurs sehen deshalb verschiedene Menüpunkte, wenn ihre Rollen oder Rechte verschieden sind. Den Button "Administration" zeigt OpenOlat, sobald Ihre Rolle oder ein Recht mindestens einen Menüpunkt freigibt. Den Menüpunkt "Einstellungen" sehen Besitzer:innen und Personen mit dem Recht "Kurseditor". Rechte erteilen die Besitzer:innen im [Bereich "Rechte" der Mitgliederverwaltung](../Members_management.de.md#section_rights).

Die System-Administration erreichen Systemadministrator:innen über den Menüpunkt "Administration" in der Hauptnavigation; nur sie sehen diesen Menüpunkt. Was sie dort einstellen, gilt für die ganze OpenOlat-Instanz und damit für alle Kurse. So schalten sie zum Beispiel unter `Administration > Module` die [Module](../../../manual_admin/administration/Modules/index.de.md) ein und legen unter `Administration > Module > Kurs` die [Standardeinstellungen](../../../manual_admin/administration/Modules_Course.de.md#default_settings) fest, mit denen neue Kurse starten. Brauchen Sie eine Funktion, die nur die System-Administration einschalten kann, wenden Sie sich an Ihre Organisation.

Im Handbuch erkennen Sie am Klickweg, welches Menü gemeint ist. Ein Klickweg in die Kurs-Administration beginnt mit dem Kurs: `Kurs > Administration > Einstellungen`. Ein Klickweg in die System-Administration beginnt mit "Administration", und der Satz davor nennt die System-Administration, zum Beispiel: in der System-Administration unter `Administration > Module > Kurs`. Andere Lernressourcen haben ein eigenes Menü "Administration", ihr Klickweg beginnt mit der Lernressource, zum Beispiel `Test > Administration > Einstellungen`.

[Zum Seitenanfang ^](#course_administration)


---

## Menüpunkte {: #menu_items}

Suchen Sie einen Menüpunkt, sagt Ihnen die Übersicht in einem Satz, wozu er dient, und führt Sie mit dem Link zu seiner Beschreibung. Die Tabellen folgen dem Menü "Administration": Jede Tabelle entspricht einer Gruppe, die das Menü mit einer Linie abtrennt, in derselben Reihenfolge wie dort. Im Menü tragen die Gruppen keinen Titel; die Titel über den Tabellen sagen, wozu die Menüpunkte einer Gruppe dienen.

**Kurs einrichten und Mitglieder verwalten**

| Menüpunkt | Wozu |
|---|---|
| [Einstellungen](../Course_Settings/index.de.md) | Alles festlegen, was den Kurs als Ganzes betrifft. Einstellungen eines einzelnen Kursbausteins legen Sie im Kurseditor fest. |
| [Mitgliederverwaltung](../Members_management.de.md) | Sehen, wer Zugriff auf den Kurs hat, und weitere Personen und Gruppen zu Mitgliedern machen. |

**Inhalte aufbauen**

| Menüpunkt | Wozu |
|---|---|
| [Kurseditor](../General_Configuration_of_Course_Elements.de.md) | Den Kurs aufbauen: Kursbausteine hinzufügen und konfigurieren. |
| [Dateien](../Storage_folder.de.md) | Den Ablageordner des Kurses öffnen und den Speicherverbrauch des Kurses prüfen. Dateien, die Sie mit anderen teilen, verwalten Sie im [File Hub](../../personal_menu/File_Hub.de.md) oder im [Media Center](../../personal_menu/Media_Center.de.md). |

**Kurs durchführen und Teilnehmende betreuen**

| Menüpunkt | Wozu |
|---|---|
| [Bewertungswerkzeug](../Assessment_tool_overview/index.de.md) | Die Teilnehmenden in allen bewertbaren Kursbausteinen bewerten, zum Beispiel mit Punkten oder bestanden/nicht bestanden, und ihnen Feedback geben. Nicht zu verwechseln mit dem Kursbaustein "Bewertung". |
| [To-dos](../Course_todos.de.md) | To-dos zum Kurs erstellen und an alle Teilnehmenden oder an einzelne Personen vergeben. |
| [Badges](../OpenBadges.de.md) | Badges des Kurses erstellen, vergeben und anzeigen. Ein Badge ist ein digitales Lernabzeichen für ein erreichtes Ziel. Der Menüpunkt erscheint, wenn Badges in OpenOlat eingeschaltet sind und der Kurs Badges vergibt. |
| [Unterlagen Betreuer:innen](../Coach_Files.de.md) | Dateien in einem gemeinsamen Ordner ablegen, auf den nur Betreuer:innen und Besitzer:innen zugreifen. Den Ordner schalten Sie in den Kurseinstellungen im [Tab "Optionen"](../Course_Settings_Options.de.md) ein. |
| [Termine und Absenzen](../Events_and_absences.de.md) | Termine und Absenzen der Teilnehmenden verwalten. |
| [Erinnerung](../Course_Reminders.de.md) | E-Mails an Personen im Kurs automatisch versenden, sobald Bedingungen zutreffen, die Sie festlegen. |
| [Prüfungsverwaltung](../Assessment_Management/index.de.md) | Den Prüfungsmodus und die Prüfungseinsicht konfigurieren. Im Prüfungsmodus öffnen Teilnehmende zum Beispiel nur bestimmte Kursbausteine. |
| [Datenerhebungsvorschau](../../../manual_admin/administration/Modules_Quality_Management.de.md) | Einsehen, welche Datenerhebungen, etwa Befragungen, das Qualitätsmanagement zum Kurs plant. Planen und bearbeiten können sie nur Qualitätsverwalter:innen. Den Menüpunkt zeigt OpenOlat, wenn Systemadministrator:innen das Qualitätsmanagement und seine Datenerhebungsvorschau eingeschaltet haben. |
| [Lernbereich](../Learning_Areas.de.md) | Lernbereiche erstellen und bearbeiten. Ein Lernbereich fasst mehrere Gruppen des Kurses zusammen. |
| [Kurs DB](#course_DB) | Angaben einzelner Personen speichern, die kein Kursbaustein erfasst. Beschrieben weiter unten auf dieser Seite. |

**Auswerten, sichern und weiterverwenden**

| Menüpunkt | Wozu |
|---|---|
| [Kursstatistiken](../Statistics_Course.de.md) | Die Zugriffe auf den Kurs auswerten. Betreuer:innen und weitere Mitglieder brauchen dafür das Recht "Statistiken". |
| [Teststatistiken](../Statistics_Test.de.md) | Die Tests des Kurses anonymisiert auswerten. Der Menüpunkt erscheint, sobald der Kurs einen Kursbaustein "Test" enthält. Betreuer:innen sehen ihn ohne zusätzliches Recht. |
| [Fragebogen Statistiken](../Statistics_Survey.de.md) | Die Umfragen des Kurses anonymisiert auswerten. Der Menüpunkt erscheint, sobald der Kurs einen Kursbaustein "Umfrage" enthält. Betreuer:innen sehen ihn ohne zusätzliches Recht. |
| [Archivierung & Reports](../Course_Archiving/index.de.md) | Die Daten des Kurses als Gesamtarchiv oder Teilarchiv sichern und Reports herunterladen, etwa die Kursresultate und die Mitgliedschaften. |
| [Angebotsarten](../Offer_Types.de.md) | Die Buchungsaufträge einsehen, also wer den Kurs über welches Angebot gebucht hat. Ein Angebot legt fest, wie Personen den Kurs im Katalog buchen, etwa "Frei verfügbar" oder mit "Zugangscode". Angebote erstellen Sie in den Kurseinstellungen im [Tab "Freigabe"](../Course_Settings_Share/index.de.md). |
| [Kopieren](../Course_Copy.de.md) | Den Kurs mit Struktur, Ordnerinhalten, HTML-Seiten und Gruppennamen kopieren. Benutzerdaten wie Forenbeiträge und Gruppenmitglieder bleiben im Original. |
| [Kopieren mit Wizard](../Course_Copy_Wizard.de.md) | Beim Kopieren auswählen, welche Elemente die Kopie übernimmt. Der Menüpunkt erscheint nur in [Lernpfadkursen](../Learning_path_course/index.de.md). |
| [Als Template speichern](../Course_Copy_Template.de.md) | Den Kurs als Template speichern: als Vorlage, aus der Sie mit "Als Kurs instanziieren" neue Kurse erstellen, etwa für die Durchführungen im Course Planner. |
| [Als Kurs instanziieren](#instantiate_as_course) | Aus einem Template einen neuen Kurs erstellen. Beschrieben weiter unten auf dieser Seite. |
| [Als Lernpfad duplizieren](#duplicate_as_learning_path) | Einen herkömmlichen Kurs als Lernpfadkurs kopieren. Beschrieben weiter unten auf dieser Seite. |
| [Inhalt exportieren](../Export_Content.de.md) | Den Kurs als ZIP-Datei herunterladen, als Sicherungskopie oder für den Import in eine andere OpenOlat-Instanz. |

**Angaben zum Kurs nachschlagen**

| Menüpunkt | Wozu |
|---|---|
| [Über diesen Kurs](../Technical_Information_on_Resources_and_Usage.de.md) | Nachschlagen, welche ID der Kurs hat, wer ihn erstellt hat und wem er gehört, dazu den externen Link und die Produkte im Course Planner, in denen der Kurs eingebunden ist. Den Menüpunkt sehen Besitzer:innen des Kurses, Lernressourcenverwalter:innen und Administrator:innen. |

**Kurs löschen**

| Menüpunkt | Wozu |
|---|---|
| [Löschen](../Course_Delete.de.md) | Den Kurs in den Papierkorb verschieben. Dabei entfernt OpenOlat alle Benutzerdaten. Liegt der Kurs im Papierkorb, steht an dieser Stelle der Menüpunkt "Wiederherstellen". |

[Zum Seitenanfang ^](#course_administration)


## Kurs DB [:octicons-tag-16:{ title="ab Release 8.1.4 (OO-313)" }](https://track.frentix.com/issue/OO-313){:target="_blank"} {: #course_DB}

!!! info "Kontakt"

    Die Kurs DB ist Teil der Serverkonfiguration und im Auslieferungszustand ausgeschaltet. Für eine Änderung wenden Sie sich an Ihre Organisation.

Soll ein Kurs Angaben einzelner Personen speichern, die kein Kursbaustein erfasst, etwa die Bestätigung, dass jemand einen Text gelesen hat, oder die Antworten einer selbst gebauten Umfrage, legen Sie dafür in der Kurs DB (Kurs Datenbank) eine Datenbank an. Eine Seite im Kurs, zum Beispiel ein Kursbaustein "HTML-Seite", schreibt und liest die Werte je Person über die [REST-Schnittstelle](../../../manual_admin/administration/REST_API.de.md) von OpenOlat, also über Adressen, die ein Skript in der Seite aufruft, meist JavaScript. Das Skript schreibt eine Person mit Programmierkenntnissen; die Kurs DB stellt nur die Datenbank bereit.

Mit "Neue Datenbank erstellen" legen Sie eine Datenbank mit einem Namen an. OpenOlat zeigt danach bei jeder Datenbank die URL, unter der die Seite die Werte ablegt; diese Adresse setzt das Skript ein. Mit "Exportieren" laden Sie die Werte aller Personen als Excel-Datei herunter. "Zurücksetzen" leert die Datenbank, "Löschen" entfernt sie.

Den Menüpunkt sehen Besitzer:innen des Kurses, Lernressourcenverwalter:innen und Administrator:innen sowie Mitglieder mit dem Recht ["Kurs Datenbank"](../Members_management.de.md#right_course_db), sobald die Kurs DB auf Ihrer OpenOlat-Instanz eingeschaltet ist.

[Zum Seitenanfang ^](#course_administration)


## Als Kurs instanziieren [:octicons-tag-16:{ title="ab Release 20.2 (OO-8897)" }](https://track.frentix.com/issue/OO-8897){:target="_blank"} {: #instantiate_as_course}

Haben Sie ein Template vorbereitet, erstellen Sie daraus mit diesem Menüpunkt einen neuen Kurs. Ein Wizard führt Sie durch die Erstellung.

Den Menüpunkt gibt es nur in Kursen mit dem Verwendungszweck "Template". Dort steht er an der Stelle von "Als Template speichern". Sie sehen ihn, wenn Sie den Kurs kopieren dürfen, also wenn das Menü auch "Kopieren" zeigt.

[Zu den Details >](../Creating_Course.de.md#purpose)<br>
[Zum Seitenanfang ^](#course_administration)


## Als Lernpfad duplizieren {: #duplicate_as_learning_path}

Wollen Sie einen herkömmlichen Kurs als Lernpfadkurs weiterführen, zum Beispiel einen Kurs, der vor OpenOlat 15 entstanden ist, erstellen Sie mit diesem Menüpunkt eine Kopie als Lernpfadkurs. Der ursprüngliche Kurs bleibt unverändert erhalten. Wie beim [Kopieren](../Course_Copy.de.md) übernimmt die Kopie Struktur und Inhalte; Benutzerdaten wie Forenbeiträge und Gruppenmitglieder bleiben im Original.

Im Dialog "Als Lernpfad duplizieren" geben Sie den "Titel der Lernressource" der Kopie an, auf Wunsch auch das "Kennzeichen der Lernressource", etwa eine Kursnummer, und wählen das Kursdesign. Beide Kursdesigns ergeben einen Lernpfadkurs: "Mit Lernpfad" führt die Teilnehmenden in einer festen Reihenfolge durch den Kurs, "Mit Lernfortschritt" zeigt den Fortschritt ohne feste Reihenfolge. "Duplizieren und konvertieren" erstellt die Kopie. [:octicons-tag-16:{ title="ab Release 20.2 (OO-8967)" }](https://track.frentix.com/issue/OO-8967){:target="_blank"}

Den Menüpunkt gibt es nur in herkömmlichen Kursen. Im Menü folgt er auf "Als Template speichern", in einem herkömmlichen Kurs mit dem [Verwendungszweck](../Creating_Course.de.md#purpose) "Template" auf "Als Kurs instanziieren". Sie sehen ihn, wenn Sie den Kurs kopieren dürfen, also wenn das Menü auch "Kopieren" zeigt. Denselben Dialog öffnen Sie in den Kurseinstellungen im [Tab "Durchführung"](../Course_Settings_Execution.de.md#course_type) mit dem Button "Als Lernpfad duplizieren".

!!! tip "Tipp"

    Wollen Sie den Kurs als Lernpfadkurs weiterführen, ohne seinen Ablauf zu ändern, wählen Sie in den meisten Fällen "Mit Lernfortschritt". Die Teilnehmenden bearbeiten den Kurs dann ohne feste Reihenfolge, so frei, wie sie sich im herkömmlichen Kurs bewegt haben. Die Reihenfolge ändern Sie bei Bedarf später im Kurseditor der Kopie, im obersten Kursbaustein, der den Titel des Kurses trägt.

    [Gäste](../../basic_concepts/guest_access.de.md), also Personen ohne OpenOlat-Konto, haben keinen Zugang zu Lernpfadkursen. Bietet Ihr herkömmlicher Kurs einen Gastzugang, gilt er für die Kopie nicht.

[Zum Seitenanfang ^](#course_administration)


## Weiterführende Informationen {: #further_information}

[Toolbar >](../Course_Settings_Toolbar.de.md)<br>
[Toolbar: Infoseite >](../Info_page.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../../basic_concepts/Roles/index.de.md)

**youtube**<br>
[Admin-Funktionen](<https://www.youtube.com/embed/rWPcz6udUrI>)

[Zum Seitenanfang ^](#course_administration)


