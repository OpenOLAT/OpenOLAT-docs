# e-Assessment Administration: Zertifikate {: #certificates}

Administrator:innen legen hier fest, wer externe Zertifikate hochladen darf, welche Zertifikatsvorlagen zur Auswahl stehen und wie fehlerhafte Zertifikate repariert werden. Sie finden die Einstellungen in der System-Administration unter:<br>
`Administration > e-Assessment > Zertifikate`

## Tab Zertifikate Konfiguration  {: #tab_config}

In OpenOlat können auch anderweitig erworbene Zertifikate hochgeladen werden. Im Tab "Zertifikate Konfiguration" wird bestimmt, welchen Rollen dies erlaubt ist.

Administrator:innen können ebenfalls einrichten, dass beim Ausstellen eines Zertifikates eine Kopie auch an Linienvorgesetzte oder an eine andere E-Mail-Adresse (z.B. die Personalabteilung) verschickt wird.

![Tab Zertifikate Konfiguration mit den Schaltern für den Upload externer Zertifikate durch Benutzer:innen und Benutzerverwalter:innen sowie für die Kopie an E-Mail-Adresse oder Linienvorgesetzte](assets/e-assessment_certificates_tab_config_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#certificates)

---

## Tab Zertifikate Vorlage  {: #tab_templates}

Wenn Kursbesitzer:innen ein Zertifikat für ihren Kurs ausstellen wollen, nehmen sie dazu eine Einstellung vor unter `Kurs > Administration > Einstellungen > Tab "Bewertung"` im Abschnitt "Zertifikat". Dort kann auch die zu verwendende Zertifikatsvorlage ausgewählt werden. Als Administrator:in können Sie die zur Auswahl stehenden Zertifikatsvorlagen bestimmen.

Die gleiche Auswahl der Zertifikatsvorlagen steht auch in Zertifikatsprogrammen zur Verfügung.

Die mitgelieferte Standardvorlage ist HTML-basiert. HTML-Vorlagen sind die empfohlene Variante; PDF-Formulare funktionieren weiterhin, sollten aber nur eingesetzt werden, wenn der Gotenberg-PDF-Dienst nicht installiert ist. [:octicons-tag-16:{ title="ab Release 21.0 (OO-9585)" }](https://track.frentix.com/issue/OO-9585)

![Tab Zertifikate Vorlage mit der Liste der hochgeladenen Zertifikatsvorlagen und den Aktionen Austauschen und Löschen je Vorlage](assets/e-assessment_certificates_tab_templates_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#certificates)

---


## Tab Wartung [:octicons-tag-16:{ title="ab Release 20.3.7 (OO-9659)" }](https://track.frentix.com/issue/OO-9659) {: #tab_maintenance}

Meldet eine Person, dass ihr Zertifikat als leere PDF-Datei angekommen ist, finden Administrator:innen im Tab "Wartung" alle betroffenen Zertifikate und erzeugen die PDF-Dateien neu. Solche Zertifikate entstehen, wenn der PDF-Dienst im Moment der Ausstellung nicht antwortet: Das Zertifikat gilt als ausgestellt, die Zertifikatsliste zeigt einen Downloadlink, und die Benachrichtigung geht mit leerem Anhang an die Person. In der Zertifikatsliste sind diese Fälle nicht erkennbar.

Die Neuerstellung ersetzt nur die PDF-Datei. Seriennummer, Ausstellungsdatum und Gültigkeitsdauer bleiben unverändert. Auch bei einer Rezertifizierung bleibt das neu erzeugte Zertifikat das aktuelle Zertifikat der Person.

Bevor Sie Zertifikate neu erzeugen, stellen Sie sicher, dass der [PDF-Dienst](External_Tools_-_Administration.de.md#pdf_generator) erreichbar ist. Sonst schlägt auch die Neuerstellung fehl.

![Ein gefundenes fehlerhaftes Zertifikat, darunter die Checkbox für die erneute E-Mail und die Schaltfläche zum Neuerzeugen, im Tab Wartung](assets/e-assessment_certificates_tab_maintenance_v1_de.png){ class="shadow lightbox" }

### Fehlerhafte Zertifikate suchen {: #search_broken_certificates}

1. Grenzen Sie im Feld "Suchbereich" den Zeitraum ein, in dem der PDF-Dienst ausgefallen ist. Lassen Sie beide Datumsfelder leer, prüft OpenOlat alle Zertifikate. Liegt das Startdatum nach dem Enddatum, weist OpenOlat die Suche ab.
2. Klicken Sie **Suchen**. Das "Resultat" meldet "Keine fehlerhaften Zertifikate im gewählten Bereich gefunden" oder die Anzahl der gefundenen Zertifikate.

Die Suche findet Zertifikate, deren PDF-Datei fehlt oder leer ist. Geprüft wird je Person und Kurs oder Zertifikatsprogramm nur das aktuelle Zertifikat.

### PDF-Dateien neu erzeugen {: #regenerate_certificates}

Findet die Suche fehlerhafte Zertifikate, erscheinen die Checkbox "E-Mail erneut an Empfänger senden" und die Schaltfläche **Zertifikate neu erzeugen**.

1. Entscheiden Sie, ob die Personen erneut benachrichtigt werden. Ohne Häkchen ersetzt OpenOlat nur die PDF-Datei, und niemand erhält eine E-Mail. Mit Häkchen verschickt OpenOlat die Benachrichtigung mit dem Zertifikat erneut an die Person. Bei Zertifikaten aus Einzelkursen gehen zusätzlich die Kopien, die im Tab "Zertifikate Konfiguration" eingerichtet sind. Bei Zertifikaten aus Zertifikatsprogrammen erhält nur die Person die E-Mail.
2. Klicken Sie **Zertifikate neu erzeugen**. Der Dialog nennt die Anzahl der Zertifikate und, falls gewählt, der E-Mails. Bestätigen Sie mit **Neu erzeugen** oder **Neu erzeugen und senden**.
3. OpenOlat erzeugt die PDF-Dateien im Hintergrund. Wiederholen Sie die Suche, um das Resultat zu prüfen: Erfolgreich neu erzeugte Zertifikate erscheinen nicht mehr im Resultat.

[Zum Seitenanfang ^](#certificates)

---


## Weiterführende Informationen {: #further_information}

[Externe Werkzeuge: PDF Generator >](External_Tools_-_Administration.de.md)<br>
[Zertifikate im persönlichen Menü >](../../manual_user/personal_menu/Certificates.de.md)<br>
[Zertifikate in Einzelkursen >](../../manual_user/learningresources/Course_Settings_Assessment_Certificate.de.md)<br>
[Zertifikate in Zertifikatsprogrammen >](../../manual_user/area_modules/Course_Planner_Certification_Programs.de.md)<br>
[Reports: Zertifikate >](../../manual_user/area_modules/Reports_Certficates.de.md)

[Zum Seitenanfang ^](#certificates)
