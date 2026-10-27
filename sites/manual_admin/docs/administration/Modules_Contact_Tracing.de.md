# Modul Kontaktverfolgung {: #contact_tracing}

Mit diesem Modul unterstützt OpenOlat die Kontaktverfolgung an den physischen Orten einer Institution.

> **Wikipedia: _"_** _Als Kontaktpersonennachverfolgung (Englisch: Contact
> Tracing), oder auch nur als Kontaktverfolgung, bezeichnet man im Rahmen der
> Umgebungsuntersuchung das Nachverfolgen von Kontaktpersonen, sowie das
> aktive Ermitteln von Personen, die Kontakt zu einem Erkrankten hatten und
> infiziert sein könnten."_

## Übersicht und Praxiseinsatz [:octicons-tag-16:{ title="ab Release 15.3 (OO-4971)" }](https://track.frentix.com/issue/OO-4971){:target="_blank"} {: #overview_practical}

Das Modul Kontaktverfolgung funktioniert mit den folgenden fünf Schritten:

  1. **Standorte** erfassen, einzeln oder per Import
  2. **QR-Codes** erzeugen und an den Standorten anbringen
  3. **Registrierung** von OpenOlat-Benutzer:innen oder Gästen an den Standorten
  4. **E-Mail-Bestätigung** nach der Registrierung
  5. **Report** der Daten bei einer behördlichen Anfrage

OpenOlat speichert die Daten datenschutzkonform und löscht sie nach der Aufbewahrungsfrist, die Sie festlegen, automatisch.

### OOacademy-Video (Kontaktverfolgung im Praxiseinsatz)

<iframe width="300" height="200" src="https://www.youtube.com/embed/4fO16U6iaiU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Aktivierung des Moduls {: #module_activation}

Das Modul "Kontaktverfolgung" öffnen Administrator:innen und Systemadministrator:innen in der System-Administration unter:<br>
`Administration > Module > Kontaktverfolgung`

Im Tab "Konfiguration" aktivieren Sie das Modul mit "Kontaktverfolgung aktiviert" und legen die "Aufbewahrungsfrist" sowie die "Standardaufhaltedauer" fest. Im Bereich "Fragebogen" bestimmen Sie die optionalen und verbindlichen Felder, im Bereich "Nachrichten und Texte" die Texte "Einleitung zur Registrierung", "Bestätigungsmail zur Registrierung" und "QR Code Anweisungen".

Sobald das Modul aktiviert ist, erscheinen die Tabs "Standorte" und "Report". Im Tab "Standorte" erfassen Sie einen einzelnen Standort mit "Standort hinzufügen". Der Dialog "Neuen Standort hinzufügen" enthält dieselben Angaben wie die Spalten der Vorlage für den Import (siehe unten).

![Felder Referenz bis Tisch, Sitzplatz, QR ID mit den Buttons zum Generieren der ID, QR Text und Gäste](assets/Standort_hinzufuegen.png){ class="shadow lightbox" title="Dialog Neuen Standort hinzufügen" }

## Standorte importieren [:octicons-tag-16:{ title="ab Release 15.3.1 (OO-5008)" }](https://track.frentix.com/issue/OO-5008){:target="_blank"} {: #import_locations}

Viele Standorte erfassen Sie schneller mit einer Excel-Liste als einzeln. Klicken Sie im Tab "Standorte" auf "Standorte importieren". Im Schritt "Daten eingeben" laden Sie neben der Beschriftung "Vorlage" über den Link "Download Excel Vorlage" die Vorlage herunter. Sie enthält die Kopfzeile mit den Spalten in der Reihenfolge, die der Import verlangt: "Referenz", "Titel", "Gebäude", "Raum", "Sektor", "Tisch", "Sitzplatz", "Gäste", "QR ID" und "QR Text". Darunter stehen zwei Standorte als Beispiel. Die Spaltennamen erscheinen in der Sprache Ihrer Benutzeroberfläche. Unter "Anweisungen" öffnet "Beispiel zeigen" ein ausgefülltes Muster.

Tragen Sie Ihre Standorte in die Vorlage ein, kopieren Sie alle Zeilen ausser der Kopfzeile und fügen Sie sie in das Feld "Standorte" ein. In den Spalten "Sitzplatz" und "Gäste" steht "on" für ja oder "off" für nein. "QR ID" und "QR Text" sind freiwillig, den QR Text können Sie mit HTML formatieren. Bleibt die Spalte "QR ID" leer, erzeugt OpenOlat die ID nach der Auswahl im Feld "QR ID": "Numerische ID generieren" oder "Lesbare ID generieren".

Im Schritt "Vorschau der Standorte" wählen Sie die Standorte aus, die Sie importieren. Neue Standorte sind vorausgewählt. Hat ein Standort eine QR ID, die es schon gibt, markiert die Vorschau ihn mit einem Warndreieck. Wählen Sie ihn aus, aktualisiert der Import den bestehenden Standort.

## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Module: Übersicht >](Modules.de.md)<br>
[Importvorlagen >](../../manual_user/basic_concepts/Import_Templates.de.md)

**youtube**<br>
[Kontaktverfolgung im Praxiseinsatz](<https://www.youtube.com/embed/4fO16U6iaiU>)

[Zum Seitenanfang ^](#contact_tracing)
