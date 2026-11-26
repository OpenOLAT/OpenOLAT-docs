# Course Planner: Import/Export - Referenz {: #import_export_reference}

Zeigt der [Import-Assistent](Course_Planner_Import_Export/index.de.md) bei einer Zelle einen Fehler oder eine Warnung, finden Sie hier, was die Meldung bedeutet und bei welchen Spalten sie auftreten kann. Die Seite listet die Fehler- und Warnungsmeldungen des Import-Assistenten sowie die Regeln für jede Spalte der Excel-Datei. Sie richtet sich an Personen, die grössere oder komplexere Importe vorbereiten.

## Feste Werte und Spaltenpräfixe {: #enum_reference}

Einige Spaltenüberschriften tragen ein Präfix. Es zeigt, auf welches Objekt sich das Kennzeichen bezieht: "PROD" auf das Produkt, "IMPL" auf die Durchführung, "ORG" auf die Organisation und "REF" bei einem Termin auf den Kurs, zu dem der Termin gehört. Die Spalte "Level" enthält die Nummer eines Elements in der Struktur seiner Durchführung. Bei Kursen, Kurstemplates und Terminen steht dort die Nummer des Elements, zu dem sie gehören.

Die Spalte "Objekttyp" in der Excel-Datei verwendet folgende feste Werte:

| Wert | Bedeutung |
|---|---|
| IMPL | Durchführung |
| ELEM | Element |
| TMPL | Kurstemplate |
| COURSE | Kurs |
| EVENT | Termin |

Die Spalte "Rolle" im Sheet "Mitgliedschaft" verwendet folgende feste Werte:

| Wert | Bedeutung |
|---|---|
| PARTICIPANT | Teilnehmer:in |
| COACH | Betreuer:in |
| MASTER_COACH | Klassenlehrer:in |
| COURSE_OWNER | Kursbesitzer:in |
| ELEM_OWNER | Elementbesitzer:in |

Die Spalte "Status" verwendet bei Durchführungen und Elementen (IMPL, ELEM) folgende Werte:

| Wert | Bedeutung |
|---|---|
| PREPARATION | Vorbereitung |
| PROVISIONAL | Provisorisch |
| CONFIRMED | Bestätigt |
| ACTIVE | Aktiv |
| CANCELLED | Abgebrochen |
| FINISHED | Beendet |

Bei Kursen und Kurstemplates (COURSE, TMPL) verwendet sie den Status der Lernressource:

| Wert | Bedeutung |
|---|---|
| PREPARATION | Vorbereitung |
| REVIEW | Review |
| COACHPUBLISHED | Freigabe Betreuer:innen |
| PUBLISHED | Veröffentlicht |
| CLOSED | Beendet |

Gross- und Kleinschreibung spielen beim Status keine Rolle. Termine (EVENT) haben keinen Status.

Die Spalten "Absenzen", "Kalender" und "Fortschritt" akzeptieren die Werte "ON", "OFF" und (bei Elementen und Durchführungen) "DEFAULT". Die Spalte "Einheit" eines Termins akzeptiert eine ganze Zahl von 0 bis 12.

[zum Seitenanfang ^](#import_export_reference)

---

## Fehler- und Warnungscodes {: #errors_warnings_reference}

Der Import-Assistent zeigt jede Meldung zusammen mit der Spaltenüberschrift der betroffenen Zelle. Die Codes in der Spalte "Code" zeigt er nicht an: Sie gelten nur auf dieser Seite und verbinden die Meldungen mit den Tabellen unter [Spaltenregeln je Sheet](#attribute_rules). Die Nummern sind nicht fortlaufend.

Bei E4 findet der Import zum Wert kein passendes Objekt, weder in OpenOlat noch in den Sheets der Datei, zum Beispiel keine Organisation mit diesem Kennzeichen. Prüft OpenOlat einen Anmeldenamen, eine E-Mail-Adresse oder ein Passwort, nennt die Meldung den Grund in eigenem Wortlaut; diese Meldungen stehen nicht in den Listen.

### Fehler

| Code | Meldung |
|---|---|
| E1 | \<Spaltenüberschrift\>: Unzureichende Berechtigungen |
| E2 | \<Spaltenüberschrift\>: Wert erforderlich |
| E3 | \<Spaltenüberschrift\>: Wert nicht eindeutig |
| E4 | \<Spaltenüberschrift\>: \<Wert\> existiert nicht |
| E5 | \<Spaltenüberschrift\>: Dieser Wert darf nicht geändert werden |
| E6 | \<Spaltenüberschrift\>: "\<Wert\>" ist kein gültiger Wert |
| E7 | \<Spaltenüberschrift\>: Wert ist zu lang |
| E8 | \<Spaltenüberschrift\>: Es existiert kein entsprechendes übergeordnetes Element |
| E9 | \<Spaltenüberschrift\>: Ungültiges Format |
| E10 | \<Spaltenüberschrift\>: Ungültiger Zeitraum |
| E11 | \<Spaltenüberschrift\>: Muss für diesen Objekttyp leer sein |
| E12 | ELEM Typ - Kennzeichen: Der Elementtyp ist als Durchführung nicht zulässig |
| E13 | ELEM Typ - Kennzeichen: Das übergeordnete Element darf kein Unterelement besitzen |
| E14 | ELEM Typ - Kennzeichen: Das übergeordnete Element darf kein Unterelement von diesem Elementtyp besitzen |
| E15 | ELEM Typ - Kennzeichen: Das Element darf keinen Inhalt haben |
| E16 | ELEM Typ - Kennzeichen: Das Element darf nur 1 Kurs/Template enthalten |
| E17 | ELEM Typ - Kennzeichen: Das Element darf keine Templates haben |
| E19 | Objekttyp: Die Lernressource hat den falschen Verwendungszweck |
| E21 / E24 | \<Spaltenüberschrift\>: Existiert in "\<Sheet\>" nicht |
| E22 | \<Spaltenüberschrift\>: Kann aufgrund von Fehlern in "\<Sheet\>" nicht importiert werden |
| E23 | \<Spaltenüberschrift\>: Wurde in "\<Sheet\>" ignoriert |
| E25 | Passwort: Muss für bestehende Benutzer:innen leer sein |
| (ohne Code) | IMPL - Kennzeichen: Beide Kennzeichen müssen gleich sein |
| (ohne Code) | Kontoablauf: Das Datum muss in der Zukunft liegen |

### Warnungen

| Code | Meldung |
|---|---|
| W1 | \<Spaltenüberschrift\>: "\<Wert\>" ist kein gültiger Wert. Änderung wird nicht übernommen |
| W2 | \<Spaltenüberschrift\>: Wert ist zu lang und wird entsprechend gekürzt |
| W3 | Das Element wurde in der Zwischenzeit aktualisiert |
| W4 | \<Spaltenüberschrift\>: Ungültiges Format. Änderung wird nicht übernommen |
| W5 | \<Spaltenüberschrift\>: \<Wert\> existiert nicht. Änderung wird nicht übernommen |
| W7 | \<Spaltenüberschrift\>: \<Wert\> wurde geändert. Änderung wird nicht übernommen |
| (ohne Code) | Objekttyp: Die Lernressource hat den Verwendungszweck "Eigenständig". Es wird empfohlen, nur Kurse mit dem Verwendungszweck "Verwendung im Course Planner" zu verwenden. [:octicons-tag-16:{ title="ab Release 20.3.1 (OO-9424)" }](https://track.frentix.com/issue/OO-9424){:target="_blank"} |

Bei W3 übernimmt der Import die Werte der Datei trotzdem und überschreibt die Änderung in OpenOlat.

[zum Seitenanfang ^](#import_export_reference)

---

## Spaltenregeln je Sheet {: #attribute_rules}

Die Tabellen nennen je Spalte, ob sie ausgefüllt sein muss, ob ein Import den Wert ändern kann und welche Meldungen möglich sind. "Änderung wird erkannt" ist keine Meldung: Der Assistent markiert die geänderte Zelle und zeigt unter "Änderung (alt/neu)" den alten und den neuen Wert.

### Sheet "Produkte" [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9191)" }](https://track.frentix.com/issue/OO-9191){:target="_blank"} {: #rules_products}

| Spalte | Pflicht | Aktualisierbar | Mögliche Meldung |
|---|---|---|---|
| Titel | Ja | Ja | E2 (leer), W2 (zu lang), Änderung wird erkannt |
| Kennzeichen | Ja | Nein | E2 (leer), E3 (nicht eindeutig), E7 (zu lang) |
| ORG - Kennzeichen | Ja | Nein | E1 (keine Berechtigung), E2 (leer), E4 (existiert nicht), E5 (Wert darf nicht geändert werden) |
| Absenzen | Ja | Ja | E2 (leer), E6 (kein gültiger Wert; bei Update dieselbe Meldung als Warnung), Änderung wird erkannt |
| Beschreibung | Nein | Ja | Änderung wird erkannt |
| Zuletzt geändert | Nein | Nein | W3 (Element seit Export bereits aktualisiert) |

### Sheet "Durchführungen" (IMPL / ELEM / TMPL / COURSE / EVENT) [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9210)" }](https://track.frentix.com/issue/OO-9210){:target="_blank"} {: #rules_implementations}

| Spalte | Pflicht | Aktualisierbar | Mögliche Meldung |
|---|---|---|---|
| PROD - Kennzeichen | Ja | Nein | E2, E1, E4, E5 (Element gehört zu einem anderen Produkt) |
| IMPL - Kennzeichen | Ja | Nein | E2, E4, E5 (Element gehört zu einer anderen Durchführung), bei IMPL die Meldung "Beide Kennzeichen müssen gleich sein", wenn der Wert vom Kennzeichen der Zeile abweicht |
| Objekttyp | Ja | Nein | E2, E6, E19 (TMPL: Verwendungszweck nicht "Template"; COURSE: Verwendungszweck nicht "Verwendung im Course Planner"), bei COURSE mit Verwendungszweck "Eigenständig" erhalten Administrator:innen statt E19 eine Warnung |
| Level | Ja bei ELEM | Nein | E2 (ELEM), E8 (kein Element mit diesem Level) |
| Titel | Ja | Ja | E2, W2, Änderung wird erkannt |
| Kennzeichen | Ja | Nein | E2, E7, E3 (je nach Objekttyp), zusätzlich E1/E4 bei TMPL/COURSE: Dort ist das Kennzeichen das einer bestehenden Lernressource |
| Status | Ja (ausser EVENT) | Ja | E2, E6, W1, Änderung wird erkannt |
| Datum/Zeit Beginn und Ende | Ja bei EVENT | Ja | E2 (EVENT), E9 (ungültiges Format), E10 (Zeitraum ungültig), E11 (Zeit ausser bei EVENT), W4, Änderung wird erkannt |
| Einheit | Nein | Ja | E6 (kein gültiger Wert; bei Update dieselbe Meldung als Warnung), Änderung wird erkannt |
| REF - Kennzeichen | Ja bei EVENT mit Kurs | Nein | E2, E5, E4 |
| Ort | Nein | Ja | W2, Änderung wird erkannt |
| Räume (nur EVENT) [:octicons-tag-16:{ title="ab Release 21.0.1 (OO-9303)" }](https://track.frentix.com/issue/OO-9303){:target="_blank"} | Nein | Ja | E4 (bei Neuanlage), W5 (bei Update), E9 (Wert nicht im Format "Gebäude-Kennzeichen:Raum-Kennzeichen", auch bei Update), Änderung wird erkannt |
| ELEM Typ - Kennzeichen | Ja bei IMPL/ELEM | Nein | E2, E4, E5, E12 bis E17 (siehe Struktur-Regeln) |
| Kalender / Absenzen / Fortschritt | Ja bei IMPL/ELEM | Ja | E2, E6 (kein gültiger Wert; bei Update dieselbe Meldung als Warnung), Änderung wird erkannt |
| Fachbereiche | Nein | Ja | E4 (bei Neuanlage), W5 (bei Update), Änderung wird erkannt |
| Zuletzt geändert | Nein | Nein | W3 |

**Zusätzliche Struktur-Regeln**

Wie ein Elementtyp konfiguriert ist, legen Administrator:innen in der System-Administration im [Modul Course Planner](../../manual_admin/administration/Modules_Course_Planner.de.md#configuration) fest. Der Import prüft jede Durchführung und jedes Element gegen die Konfiguration seines Elementtyps und meldet einen Verstoss in der Spalte "ELEM Typ - Kennzeichen" der Zeile, deren Elementtyp die Regel verletzt. Als Kurse und Kurstemplates eines Elements zählen die Zeilen COURSE und TMPL, die zu diesem Element gehören.

| Objekttyp | Regel | Meldung bei Verstoss |
|---|---|---|
| IMPL | Ein Elementtyp mit "Verwendung als" "Element" ist als Durchführung nicht zulässig | E12 |
| IMPL / ELEM | Ein Elementtyp, bei dem die Einstellung "Unterelemente" auf "Nein" steht, darf keine Unterelemente haben | E13 |
| ELEM | Der Elementtyp muss beim Elementtyp des übergeordneten Elements in der Einstellung "Kindelemente" ausgewählt sein. Diese Einstellung legt fest, welche Typen darunter erlaubt sind | E14 |
| IMPL / ELEM | Ein Elementtyp mit "Inhalt" "Kein Inhalt" erlaubt keine Kurse und keine Kurstemplates | E15 |
| IMPL / ELEM | Ein Elementtyp mit "Inhalt" "Einzelkurs" erlaubt höchstens einen Kurs und höchstens ein Kurstemplate; ein Kurs und ein Kurstemplate zusammen sind zulässig | E16 |
| IMPL / ELEM | Ein Elementtyp mit "Inhalt" "Kurs-Bundle" erlaubt keine Kurstemplates | E17 |

### Sheet "Mitgliedschaft" [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9224)" }](https://track.frentix.com/issue/OO-9224){:target="_blank"} {: #rules_memberships}

| Spalte | Pflicht | Mögliche Meldung |
|---|---|---|
| PROD - Kennzeichen / IMPL - Kennzeichen / Kennzeichen | Ja, alle drei | E2, E4, E22, E23 |
| Rolle | Ja | E2, E6 |
| Anmeldename | Ja | E2, E21/E24 (Anmeldename fehlt im Sheet "Konten"), E22 (Konto mit Fehlern), E23 (Konto ignoriert) |

Mitgliedschaften können nur neu angelegt, nicht aktualisiert werden.

### Sheet "Konten" {: #rules_users}

| Spalte | Pflicht (bei Neuanlage) | Mögliche Meldung |
|---|---|---|
| Anmeldename | Ja | E2, E7, bei Neuanlage eine Meldung, wenn der Anmeldename nicht zulässig ist, E21/E24 (Anmeldename fehlt im Sheet "Mitgliedschaft") |
| Vorname | Ja | E2, E7, W7 (bei bestehenden Konten geändert) |
| Nachname | Ja | E2, E7, W7 |
| E-Mail | Ja, ausser in den [E-Mail Einstellungen](../../manual_admin/administration/E-Mail_Settings.de.md#email_address) ist die Option "Obligatorisch" ausgeschaltet | E2, E7, eine Meldung, wenn die Adresse ungültig ist oder ein anderes Konto sie bereits verwendet |
| ORG - Zugehörigkeit | Ja | E2, E1, E4, bei bestehenden Konten ohne diese Organisation die Meldung von E5 als Warnung |
| Passwort | Nein | E25 (muss bei bestehenden Konten leer sein), bei Neuanlage eine Meldung, wenn das Passwort die Vorgaben im Tab ["Passwort-Syntax"](../../manual_admin/administration/Login_Password_and_Authentication.de.md#tab-password-syntax) nicht erfüllt |
| Kontoablauf | Nein | Muss bei Neuanlage in der Zukunft liegen, sonst Fehlermeldung; bei Änderung an bestehenden Konten W7 |

Jedes Konto im Sheet "Konten" braucht mindestens eine Zeile im Sheet "Mitgliedschaft", sonst meldet der Import E21/E24. Bestehende Konten dürfen im Sheet stehen, damit ihre Mitgliedschaften importiert werden. Ihre Angaben ändert der Import nicht: Er legt nur neue Konten an und meldet abweichende Werte bestehender Konten als Warnung.

[zum Seitenanfang ^](#import_export_reference)

---

## Weiterführende Informationen {: #further_information}

[Course Planner: Import / Export >](Course_Planner_Import_Export/index.de.md)<br>
[Modul Course Planner >](../../manual_admin/administration/Modules_Course_Planner.de.md)<br>
[E-Mail Einstellungen >](../../manual_admin/administration/E-Mail_Settings.de.md)<br>
[Passwort und Authentifizierung >](../../manual_admin/administration/Login_Password_and_Authentication.de.md)<br>
[Course Planner: Durchführungen >](Course_Planner_Implementations.de.md)<br>
[Importvorlagen >](../basic_concepts/Import_Templates.de.md)

[zum Seitenanfang ^](#import_export_reference)
