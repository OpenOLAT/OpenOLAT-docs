# Course Planner: Import/Export - Referenz {: #import_export_reference}

Diese Seite listet alle Fehler- und Warnungsmeldungen sowie die detaillierten Feldregeln des [Import-Assistenten](Course_Planner_Import_Export.de.md) auf. Sie richtet sich an Personen, die grössere oder komplexere Importe vorbereiten.

## Objekttypen und Rollen {: #enum_reference}

Die Spalte "Objekttyp" in der Excel-Datei verwendet folgende feste Werte:

| Wert | Bedeutung |
|---|---|
| IMPL | Durchführung |
| ELEM | Element |
| TMPL | Template |
| COURSE | Kurs |
| EVENT | Termin |

Die Spalte "Rolle" im Sheet "Mitgliedschaften" verwendet folgende feste Werte:

| Wert | Bedeutung |
|---|---|
| PARTICIPANT | Teilnehmer:in |
| COACH | Betreuer:in |
| MASTER_COACH | Klassenlehrer:in |
| COURSE_OWNER | Kursbesitzer:in |
| ELEM_OWNER | Elementbesitzer:in |

Die Felder "Absenzen", "Kalender" und "Fortschritt" akzeptieren die Werte "ON", "OFF" und (bei Elementen und Durchführungen) "DEFAULT".

[zum Seitenanfang ^](#import_export_reference)

---

## Fehler- und Warnungscodes {: #errors_warnings_reference}

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
| E12 | Der Elementtyp ist als Durchführung nicht zulässig |
| E13 | Das übergeordnete Element darf keine Unterelement besitzen |
| E14 | Das übergeordnete Element darf keine Unterelement von diesem Elemententyp besitzen |
| E15 | Das Element darf keinen Inhalt haben |
| E16 | Das Element darf nur 1 Kurs/Template enthalten |
| E17 | Das Element darf keine Templates haben |
| E19 | Die Lernressource hat den falschen Verwendungszweck |
| E21 / E24 | \<Spaltenüberschrift\>: Existiert in "\<Sheet\>" nicht |
| E22 | \<Spaltenüberschrift\>: Kann aufgrund von Fehlern in "\<Sheet\>" nicht importiert werden |
| E23 | \<Spaltenüberschrift\>: Wurde in "\<Sheet\>" ignoriert |
| E25 | Passwort: Muss für bestehende Benutzer:innen leer sein |
| (ohne Code) | Bei Import-Kennzeichen-Konflikten: Beide Bezeichnungen müssen gleich sein |
| (ohne Code) | Konto-Ablaufdatum: Das Datum muss in der Zukunft liegen |


### Warnungen

| Code | Meldung |
|---|---|
| W1 | \<Spaltenüberschrift\>: "\<Wert\>" ist kein gültiger Wert. Änderung wird nicht übernommen |
| W2 | \<Spaltenüberschrift\>: Wert ist zu lang und wird entsprechend gekürzt |
| W3 | Das Element wurde in der Zwischenzeit aktualisiert |
| W4 | \<Spaltenüberschrift\>: Ungültiges Format. Änderung wird nicht übernommen |
| W5 | \<Spaltenüberschrift\>: \<Wert\> existiert nicht. Änderung wird nicht übernommen |
| W7 | \<Spaltenüberschrift\>: \<Wert\> wurde geändert. Änderung wird nicht übernommen |


[zum Seitenanfang ^](#import_export_reference)

---

## Attribut-Regeln je Sheet {: #attribute_rules}

### Sheet "Produkte" {: #rules_products}

| Attribut | Pflicht | Aktualisierbar | Mögliche Meldung |
|---|---|---|---|
| Titel | Ja | Ja | E2 (leer), W2 (zu lang), Änderung wird erkannt |
| Ext. Ref. | Ja | Nein | E2 (leer), E3 (nicht eindeutig), E7 (zu lang) |
| ORG - Kennzeichen | Ja | Nein | E1 (keine Berechtigung), E2 (leer), E4 (existiert nicht), E5 (Wert darf nicht geändert werden) |
| Absenzen | Ja | Ja | E2 (leer), E6 (bei Neuanlage kein gültiger Wert), W1 (bei Update kein gültiger Wert), Änderung wird erkannt |
| Beschreibung | Nein | Ja | W2 (zu lang), Änderung wird erkannt |
| Zuletzt geändert | Nein | Nein | W3 (Element seit Export bereits aktualisiert) |

### Sheet "Durchführungen" (IMPL / ELEM / TMPL / COURSE / EVENT) {: #rules_implementations}

| Attribut | Pflicht | Aktualisierbar | Mögliche Meldung |
|---|---|---|---|
| PROD - Ext. Ref. | Ja | Nein | E2, E1, E4 |
| IMPL - Ext. Ref. | Ja | Nein | E2, E4 |
| Objekttyp | Ja | Nein | E2, E6, E5 |
| Level | Ja (ausser IMPL) | Nein | E2, E5, E8 (kein übergeordnetes Element bei ELEM) |
| Titel | Ja | Ja | E2, W2, Änderung wird erkannt |
| Ext. Ref. | Ja | Nein | E2, E7, E3 (je nach Objekttyp), zusätzlich E1/E4/E19 bei TMPL/COURSE |
| Status | Ja (ausser EVENT) | Ja | E2, E6, W1, Änderung wird erkannt |
| Datum/Zeit Beginn und Ende | Ja bei EVENT | Ja | E2 (EVENT), E9 (ungültiges Format), E10 (Zeitraum ungültig), W4, Änderung wird erkannt |
| Einheit | Ja bei EVENT | Ja | E2, E6, Änderung wird erkannt |
| REF - Ext. Ref. | Ja bei EVENT mit Kurs | Nein | E2, E5, E4 |
| Ort | Nein | Ja | W2, Änderung wird erkannt |
| ELEM Typ - Ext. Ref. | Ja bei IMPL/ELEM | Nein | E2, E3, E4 |
| Kalender / Absenzen / Fortschritt | Ja bei IMPL/ELEM/TMPL/COURSE | Ja | E2, E6, W1, Änderung wird erkannt |
| Fachbereiche | Nein | Ja | E4 (bei Neuanlage), W5 (bei Update), Änderung wird erkannt |
| Zuletzt geändert | Nein | Nein | W3 |

**Zusätzliche Struktur-Regeln** (abhängig von der Konfiguration des jeweiligen Elementtyps):

| Objekttyp | Regel | Meldung bei Verstoss |
|---|---|---|
| IMPL | Elementtyp muss "Als Durchführung zulässig" erlauben | E12 |
| ELEM | Elementtyp mit deaktiviertem "Verbund-Typ" darf keine Unterelemente haben | E13 |
| ELEM | Elementtyp mit definierten Subtypen darf nur passende Unterelemente haben | E14 |
| TMPL / COURSE | Elementtyp ohne Inhalt erlaubt keine Zuordnung | E15 |
| TMPL / COURSE | Element darf nur von einem Kurs/Template referenziert werden | E16 |
| TMPL | Elementtyp mit unbegrenzten Kursen erlaubt keine Templates | E17 |
| EVENT | Element muss auf einen Kurs referenzieren | nicht im Code gefunden, siehe Hinweis oben |

### Sheet "Mitgliedschaften" {: #rules_memberships}

| Attribut | Pflicht | Mögliche Meldung |
|---|---|---|
| PROD - Ext. Ref. / IMPL - Ext. Ref. / Ext. Ref. | Ja | E2, E7, E1, bei Neuanlage zusätzlich E21/E22/E23 |
| Rolle | Ja | E2, E6 |
| Anmeldename | Ja | E2, bei Neuanlage zusätzlich E21/E22/E23 |

Mitgliedschaften können nur neu angelegt, nicht aktualisiert werden.

### Sheet "Benutzer:innen" {: #rules_users}

| Attribut | Pflicht (bei Neuanlage) | Mögliche Meldung |
|---|---|---|
| Anmeldename | Ja | E2, E6, bei Neuanlage zusätzlich E21/E22 |
| Vorname | Ja | E2, E7, W7 (bei bestehenden Benutzer:innen geändert) |
| Nachname | Ja | E2, E7, W7 |
| E-Mail | Ja, ausser wenn Systemeinstellung "E-Mail obligatorisch" deaktiviert ist | E2, E6, W7 |
| ORG-Zugehörigkeit | Ja | E2, E1, E4, W7 |
| Passwort | Nein | E25 (muss bei bestehenden Benutzer:innen leer sein), E6 (bei Neuanlage ungültiger Wert) |
| Konto-Ablaufdatum | Nein | Muss bei Neuanlage in der Zukunft liegen, sonst Fehlermeldung; bei Änderung an bestehenden Konten W7 |

Benutzer:innen können nur neu angelegt, nicht aktualisiert werden.

[zum Seitenanfang ^](#import_export_reference)

---

## Weitere Informationen {: #further_information}

[Course Planner: Import / Export >](Course_Planner_Import_Export.de.md)<br>

[zum Seitenanfang ^](#import_export_reference)
