# Login-Konzept

Grundsätzlich gibt es 2 Login-Konzepte, die einzeln oder kombiniert angewendet werden können:

* Lokale Authentifizierung
* Externe Authentifizierung


## Lokale Authentifizierung

Bei der lokalen Authentifizierung werden Name und Passwort in OpenOlat (lokal) gespeichert.

## Externe Authentifizierung

Bei der externen Authentifizierung wird das Passwort NICHT in OpenOlat gespeichert, sondern in einem externen Tool gesetzt und gespeichert.
OpenOlat fragt bei dem externen Tool nach, ob dieser Anmeldenamen zum Zutritt berechtigt ist (LDAP, oAuth, Shibboleth).

## Kombinierte lokale und externe Authentifizierung

Bei der Kombination von lokaler und externer Authentifizierung wird sowohl ein in OpenOlat gespeichertes Passwort benötigt, als auch eine Abfrage von OpenOlat bei einem externen Tool durchgeführt.

* Ist das lokal gespeicherte Passwort okay?
* Bestätigt das externe Tool, dass der angemeldete Name zum Zugriff berechtigt ist?

Wenn beide Faktoren erfüllt sind, wird der Zugang frei gegeben.

## Passkey

Passkey ist eine Alternative zu Passwörtern. Anstelle der Eingabe eines Passworts durch eine Person wird ein im Gerät gespeicherter Key verwendet. (Gerätegebundene statt personengebundene Authentifizierung.)

Genaueres finden Sie in einem [separaten Abschnitt](../login_registration/Passkey.de.md) hier im Handbuch.

## One Time Code [:octicons-tag-16:{ title="ab Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509)

Der One Time Code ist ein weiteres Verfahren für eine zweite Sicherheitsstufe beim Login. Nach Eingabe von Benutzername und Passwort erhalten Kontoinhaber:innen einen 8-stelligen Bestätigungscode per E-Mail und schliessen die Anmeldung mit diesem Code ab. Der One Time Code lässt sich unabhängig von Passkey aktivieren und dient bei aktivem Passkey als Ausweichlösung für Konten ohne hinterlegten Passkey.

Genaueres finden Sie im [separaten Abschnitt One Time Code](../login_registration/One_Time_Code.de.md) hier im Handbuch.

