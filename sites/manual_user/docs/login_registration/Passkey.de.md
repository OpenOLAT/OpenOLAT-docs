# Passkey {: #passkey}

## Was ist Passkey?

* Passkey ist ein digitaler Schlüssel, kein Passwort.
* Dieser Schlüssel wird individuell für ein bestimmtes Gerät erstellt und dann im Browser oder Gerät gespeichert. Er ist also gerätegebunden, nicht personengebunden.
* Ist Passkey einmal erstellt, ist kein Passwort mehr erforderlich, das man vergessen könnte oder das gestohlen werden könnte. Sie müssen sich also lediglich Zutritt zu Ihrem Gerät verschaffen können (z.B. mit Fingerprint oder Gesichtserkennung). Alle weiteren Zugänge zu mit Passkey gesicherten Applikationen werden dann vom Gerät aus geprüft und gewährt.
* Der Passkey ist jedoch kein Generalschlüssel für alle Applikationen, in denen man sich anmelden möchte. Jeder Account hat seinen eigenen Passkey.
* Bei einer Anmeldung treten Ihr Gerät und der angefragte Server in Kontakt und klären untereinander (anhand des Passkeys), ob der Zugriff gewährt werden kann. Der eigentliche Schlüssel (Private Key) verlässt dabei das Gerät nicht. Deshalb gilt Passkey als besonders sicher.

!!! info "Weitere Informationen"

    Zu Passkey und seiner Funktionsweise finden Sie viele Einträge im Internet, z.B.

    * [passkey.org](https://passkey.org)
    * [Wikipedia-Eintrag zu Fido/Passkey](https://de.wikipedia.org/wiki/FIDO2#Passkey)
    * [loginwithfido.com](https://loginwithfido.com)


## Passkey aktivieren {: #activate}

Die Aktivierung von Passkey in OpenOlat erfolgt durch die Administrator:innen. Mit der Aktivierung wird bestimmt, dass Passkey verwendet werden kann oder muss.

Die **Erstellung** des Passkeys geschieht dann aber durch die Benutzer:innen auf den jeweiligen Geräten, in OpenOlat unter `Persönliches Menü > Passwort`. Administrator:innen können Passkeys lediglich entfernen.

Passkey kann rollenbasiert konfiguriert werden und ist Teil eines dreistufigen Sicherheitskonzeptes in OpenOlat:

**Stufe 1: nur Passwort**<br>
**Stufe 2: nur Passkey**<br>
**Stufe 3: Passkey + Passwort** (2-Faktor-Authentifizierung)<br>

Details dazu auf der Seite [Sicherheitsstufen](Security_levels.de.md).

Ist in OpenOlat eine Sicherheitsstufe mit Passkey konfiguriert, werden die Benutzer:innen bei der nächsten Anmeldung angehalten, einen Passkey zu erstellen und diesen zukünftig für die Anmeldung zu verwenden. Je nach Konfiguration lässt sich dieser Schritt einige Male überspringen; OpenOlat zeigt an, wie oft das noch möglich ist.

Hat die Administration zusätzlich den One Time Code aktiviert, können sich Kontoinhaber:innen ohne hinterlegten Passkey weiterhin mit Passwort und einem Bestätigungscode per E-Mail anmelden. [:octicons-tag-16:{ title="ab Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509) Details dazu auf der Seite [One Time Code](One_Time_Code.de.md).


!!! note "Hinweis"

    Für bestimmte Rollen (z.B. Benutzerverwalter:innen und Administrator:innen) wird Stufe 2 empfohlen.


## Was sind Recovery Keys?

Wenn kein Passwort mehr vorhanden ist, kann es auch nicht mehr von Administrator:innen zurückgesetzt werden. Ist in OpenOlat Passkey als alleinige Authentifizierungsmethode aktiviert, können keine Passwörter mehr vergeben werden. (Bei 2-Faktor-Authentifizierung dagegen schon, zusätzlich zu Passkey.)

Geht der Schlüssel trotzdem einmal verloren, braucht es einen Ersatzschlüssel. Bei Passkey ist der Ersatzschlüssel jedoch keine Kopie des Originalschlüssels (Private Key). Recovery Keys sind Einmal-Passwörter, die kein zweites Mal verwendet werden können.


## Neue Recovery Keys anfordern

Neue Recovery Keys erstellen Sie unter `Persönliches Menü > Passwort` mit dem Button "Neue Recovery Keys erstellen".

!!! note "Hinweis"

    Werden neue Recovery Keys erstellt, sind alle alten ungültig, auch wenn sie noch nie benutzt wurden.

Benutzerverwalter:innen und Administrator:innen können Ihnen zudem einen temporären Recovery Key schicken: in der Benutzerverwaltung im Tab "Passwort" mit "Recovery Key senden". OpenOlat schickt den Key an die hinterlegte E-Mail-Adresse. Er ist 2 Stunden gültig und erlaubt eine einmalige Anmeldung.


## Passkey für mehrere Geräte

Gehen Sie dazu in folgenden Schritten vor:

1. Einrichten von Passkey auf dem Hauptgerät<br>
Administrator:innen können rollenspezifisch Passkeys verlangen. Benutzer:innen können die Sicherheitsstufe auch selbst erhöhen, wenn die Administration das erlaubt.<br>`Persönliches Menü > Passwort`

2. Recovery Keys speichern<br>(nur zur einmaligen Verwendung)

3. Ist Passkey aktiviert, verlangt OpenOlat bei der ersten Anmeldung die Erstellung eines Passkeys (Private Key). Dieser ist gerätespezifisch und wird nur auf dem Gerät gespeichert.

4. Wechseln Sie nun das Gerät und melden Sie sich auf dem anderen Gerät an. Dort erscheint eine Meldung, dass für die Anmeldung ein Passkey erforderlich ist.

5. Klicken Sie auf "Recovery Key benutzen" und melden Sie sich mit einem Recovery Key an. So kommen Sie vom anderen Gerät aus in OpenOlat.

6. Damit es nicht jedes Mal erneut einen Recovery Key braucht, gehen Sie nach der Anmeldung auf dem neuen Gerät wieder zu `Persönliches Menü > Passwort`. Dort steht wieder der Button "Passkey erstellen" zur Verfügung.

7. Erzeugen Sie mit dem Button einen neuen Passkey. Es wird ein weiterer Private Key für das aktuelle Gerät erstellt.

8. Die verschiedenen Passkeys/Geräte sind dann unter `Persönliches Menü > Passwort` aufgelistet.


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[passkey.org >](https://passkey.org)<br>
[Wikipedia-Eintrag zu Fido/Passkey >](https://de.wikipedia.org/wiki/FIDO2#Passkey)<br>
[loginwithfido.com >](https://loginwithfido.com)<br>
[Sicherheitsstufen >](Security_levels.de.md)<br>
[One Time Code >](One_Time_Code.de.md)

**Weiterführend**<br>
[Passwort >](Password.de.md)<br>
[Persönliche Konfiguration: Passwort >](../personal_menu/Password.de.md)<br>
[Login-Konzept >](Login_Concept.de.md)

[Zum Seitenanfang ^](#passkey)
