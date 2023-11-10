# Passkey

## Was ist Passkey?

* Passkey ist ein digitaler Schlüssel, kein Passwort.
* Dieser Schlüssel wird indivuell für ein bestimmtes Gerät erstellt und dann im Browser oder Gerät gespeichert. Er ist also gerätegebunden, nicht personengebunden.
* Wurde Passkey einmal erstellt, ist kein Passwort mehr erforderlich, das man vergessen könnte oder das gestohlen werden könnte. Sie müssen sich also lediglich Zutritt zu Ihrem Gerät verschaffen können (z.B. mit Fingerprint oder Gesichtserkennung). Alle weiteren Zugänge zu mit Passkey gesicherten Applikationen werden dann vom Gerät aus geprüft und gewährt.
* Der Passkey ist jedoch kein Generalschlüssel für alle Applikationen, in denen man sich anmelden möchte. Jeder Account hat seinen eigenen Passkey. 
* Bei einer Anmeldung treten ihr Gerät und der angefragte Server in Kontakt und klären untereinander (anhand des Passkeys), ob der Zugriff gewährt werden kann. Der eigentliche Schlüssel (Private Key) verlässt dabei das Gerät nicht. Deshalb gilt Passkey als besonders sicher. 

!!! info "Weitere Informationen"

    Zu Passkey und seine Funktionsweise finden Sie viele Einträge im Netz, z.B.
    
    * [passkey.org](https://passkey.org)
    * [Wikipedia-Eintrag zu Fido/Passkey](https://de.wikipedia.org/wiki/FIDO2#Passkey)
    * [loginwithfido.com](https://loginwithfido.com)


## Passkey aktivieren {: #activate}

Die Aktivierung von Passkey in OpenOlat erfolgt durch die Administrator:innen. Mit der Aktivierung wird bestimmt, dass Passkey verwendet werden kann oder muss.

Die **Erstellung** des Passkeys geschieht dann aber durch den/die Benutzer:innen auf den jeweiligen Geräten. (In OpenOlat im **persönlichen Menü** unter **"Passwort"**.) Administrator:innen können Passkeys lediglich entfernen. 

Passkey kann rollenbasiert konfiguriert werden und ist Teil eines dreistufigen Sicherheitskonzeptes in OpenOlat:

**Stufe 1: nur Passwort**<br>
**Stufe 2: nur Passkey**<br>
**Stufe 3: Passkey + Passwort** (2-Stufen-Authentifizierung)<br>

Ist in OpenOlat eine Sicherheitsstufe mit Passkey konfiguriert worden, dann werden die Benutzer:innen bei der nächsten Anmeldung angehalten, einen Passkey zu erstellen und diesen zukünftig für die Anmeldung zu verwenden.


!!! note "Hinweis"

    Für bestimmte Rollen (z.B. Benutzerverwalter:innen und Administrator:innen) wird Stufe 2 empfohlen.


## Was sind Recovery Keys?

Wenn kein Passwort mehr vorhanden ist, kann es auch nicht mehr von Administrator:innen zurückgesetzt werden.  Wurde in OpenOlat Passkey als alleinige Authentifizierungsmethode aktiviert, können keine Passwörter mehr vergeben werden. (Bei 2-Faktoren-Authentifizierung dagegen schon, zusätzlich zu Passkey.)

Geht der Schlüssel trotzdem einmal verloren, benötigt es einen Ersatzschlüssel. Bei Passkey ist der Ersatzschlüssel jedoch keine Kopie des Originalschlüsses (Private Key). Recovery Keys sind Einmal-Passwörter, die kein zweites Mal verwendet werden können.


## Neue Recovery Keys anfordern

Die Recovery Keys können **im persönlichen Menü** unter **"Passwort"** angefordert werden.

!!! note "Hinweis"

    Wurden neue Recovery Keys bestellt, sind alle alten ungültig, auch wenn sie noch nie benutzt wurden.