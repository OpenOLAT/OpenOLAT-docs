# Passkey

## Was ist Passkey?

* Passkey ist ein digitaler Schlüssel, kein Passwort.
* Dieser Schlüssel wird indivuell für ein bestimmtes Gerät erstellt und dann im Browser oder Gerät gespeichert. Er ist also gerätegebunden, nicht personengebunden.
* Wurde Passkey einmal erstellt, ist kein Passwort mehr erforderlich, das man vergessen könnte oder das gestohlen werden könnte. Sie müssen sich also lediglich Zutritt zu Ihrem Gerät verschaffen können (z.B. mit Fingerprint oder Gesichtserkennung). Alle weiteren Zugänge zu mit Passkey gesicherten Applikationen werden dann vom Gerät aus geprüft und gewährt.
* Der Passkey ist jedoch kein Generalschlüssel für alle Applikationen, in denen man sich anmelden möchte. Jeder Account hat seinen eigenen Passkey. 
* Bei einer Anmeldung treten ihr Gerät und der angefragte Server in Kontakt und klären untereinander (anhand des Passkeys), ob der Zugriff gewährt werden kann. Der eigentliche Schlüssel (Private Key) verlässt dabei das Gerät nicht. Deshalb gilt Passkey als besonders sicher. 

## Wie funktioniert Passkey?

tbd

Grafiken

## Passkey aktivieren

Die Aktivierung von Passkey erfolgt durch Administrator:innen.

screen

## Was sind Recovery Keys?

Wenn kein Passwort mehr vorhanden ist, kann es auch nicht mehr von Administrator:innen zurückgesetzt werden. 
Wurde in OpenOlat Passkey als alleinige Authentifizierungsmethode aktiviert, können keine Passwörter mehr vergeben werden. (Bei 2-Faktoren-Authentifizierung dagegegen schon, zusätzlich zu Passkey.)

Geht der Schlüssel trotzdem einmal verloren, benötigt es einen Ersatzschlüssel. Bei Passkey ist der Ersatzschlüssel jedoch keine Kopie des Originalschlüsses (Private Key).
Recovery Keys sind Einmal-Passwörter, die kein zweites Mal verwendet werden können.


## Neue Recovery keys anfordern

tbd

!!! note "Hinweis"

    Wurden neue Recovery Keys bestellt, sind alle alten ungültig, auch wenn sie noch nie benutzt wurden.