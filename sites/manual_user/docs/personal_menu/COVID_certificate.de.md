# Persönliche Konfiguration: COVID-Zertifikat {: #covid_certificate}

![Abschnitt Konfiguration im persönlichen Menü mit den Einträgen Profil, Einstellungen und Passwort, der Eintrag Profil ist ausgewählt](assets/pers_menu_profile_v1_de.png){ class="aside-right lightbox"}

![Symbol Profil](assets/icon_profile.png)

Sofern Administrator:innen das COVID-Zertifikat in der System-Administration unter `Administration > Module > COVID-Zertifikat` aktiviert haben, finden Benutzer:innen im persönlichen Menü unter "Profil" den Tab "COVID-Zertifikat". Hier fügen Sie ein neues persönliches COVID-Zertifikat hinzu oder sehen den Status Ihres bestehenden Zertifikats ein. Der Tab erscheint nur in Ihrem eigenen Profil.

![Türkis markierter Tab COVID-Zertifikat rechts neben den Tabs Profil und Meine Visitenkarte, im Profil des persönlichen Menüs](assets/pers_menu_profile_covid_v1_de.png){ class="shadow lightbox" }

!!! info "Wichtig"

    Das Zertifikat selbst wird **nicht** gespeichert. OpenOlat speichert nur das Datum, bis zu dem der Nachweis gültig ist.

:octicons-device-camera-video-24: **Video-Einführung**: [COVID-Zertifikate in OpenOlat](<https://www.youtube.com/embed/863v3ug_QaM>){:target="_blank"}

## COVID-Zertifikat hinzufügen {: #add_covid_certificate}

Klicken Sie auf "Neues COVID-Zertifikat hinzufügen".

Unter "Automatisch" scannen Sie den QR-Code Ihres Zertifikats mit "QR-Code scannen" oder laden das Zertifikat mit "Zertifikat importieren" als Bild oder PDF hoch (maximal 10 MB). Die Validierung erfolgt automatisch, siehe [Validierungsstatus](#validation_status). Die Option "Automatisch" steht nur zur Verfügung, wenn Administrator:innen das Scannen von COVID-Zertifikaten eingeschaltet haben.

Funktioniert das automatische Hinzufügen **nicht**, wählen Sie "Manuell". Dort geben Sie den Zertifikatstyp an (Impfung, Genesung, PCR-Test, Antigen-Schnelltest oder Arztzeugnis) sowie das zugehörige Datum. Manuell erfasste Daten werden nicht automatisch validiert, siehe [Validierungsstatus](#validation_status).

In beiden Fällen bestätigen Sie, dass alle Angaben der Wahrheit entsprechen. Mit der Option "E-Mail-Erinnerung vor Ablauf des Zertifikats erhalten" benachrichtigt Sie OpenOlat per E-Mail, bevor Ihr Zertifikat abläuft.

![Karte COVID-Zertifikat mit Name und Benutzername, roter 3G-Statusanzeige mit Kreuz und aktueller Uhrzeit sowie dem Button Neues COVID-Zertifikat hinzufügen, im Tab COVID-Zertifikat des Profils](assets/Bildschirmfoto 2021-10-01 um 17.01.19.png){ class="shadow lightbox" }

## Validierungsstatus {: #validation_status}

Die Statusanzeige zeigt neben der Farbe die aktuelle Uhrzeit.

### Grün

![Grüne 3G-Statusanzeige mit Häkchen und aktueller Uhrzeit: validiertes Zertifikat](assets/Bildschirmfoto%202021-10-01%20um%2017.05.13.png){ class="shadow lightbox" }

Ihr Zertifikat ist validiert und gültig.

### Orange

![Orange 3G-Statusanzeige mit Fragezeichen und aktueller Uhrzeit: hinterlegtes, noch nicht validiertes Zertifikat](assets/Bildschirmfoto%202021-10-01%20um%2017.03.01.png){ class="shadow lightbox" }

Sie haben Daten hinterlegt, diese sind jedoch noch nicht validiert.

Haben Sie Ihr Zertifikat manuell hinzugefügt, ist der Status immer Orange.

Wenden Sie sich an die 3G-Beauftragten Ihrer Organisation, um Ihr Zertifikat validieren zu lassen oder wenn die automatische Erfassung nicht funktioniert hat.

### Rot

![Rote 3G-Statusanzeige mit Kreuz und aktueller Uhrzeit: kein gültiges Zertifikat hinterlegt](assets/Bildschirmfoto%202021-10-01%20um%2017.02.23.png){ class="shadow lightbox" }

Es ist kein Zertifikat hinterlegt, das Zertifikat ist abgelaufen oder die automatische Erfassung des Zertifikats konnte nicht abgeschlossen werden.

Vorname, Nachname und Geburtsdatum auf dem Zertifikat müssen mit Ihren Benutzerdaten in OpenOlat übereinstimmen, andernfalls erhalten Sie eine Meldung.

Wenden Sie sich an die 3G-Beauftragten Ihrer Organisation, wenn Sie Probleme beim Hinzufügen Ihres COVID-Zertifikats haben.

## Weiterführende Informationen {: #further_information}

[Persönliche Konfiguration >](Personal_Configuration.de.md)<br>
[Persönliche Konfiguration: Profil >](Profile.de.md)<br>
[Module: Übersicht (Administrationshandbuch) >](../../manual_admin/administration/Modules.de.md)

**youtube**<br>
[COVID-Zertifikate in OpenOlat](<https://www.youtube.com/embed/863v3ug_QaM>)

[Zum Seitenanfang ^](#covid_certificate)
