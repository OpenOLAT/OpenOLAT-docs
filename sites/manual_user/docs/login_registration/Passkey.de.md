# Passkey

## Was ist Passkey?

* Passkey ist ein digitaler Schlüssel, kein Passwort.
* Dieser Schlüssel wird indivuell für ein bestimmtes Gerät erstellt und dann im Browser oder Gerät gespeichert. Er ist also gerätegebunden, nicht personengebunden.
* Wurde Passkey einmal erstellt, ist kein Passwort mehr erforderlich, das man vergessen könnte oder das gestohlen werden könnte. Sie müssen sich also lediglich Zutritt zu Ihrem Gerät verschaffen können (z.B. mit Fingerprint oder Gesichtserkennung). Alle weiteren Zugänge zu mit Passkey gesicherten Applikationen werden dann vom Gerät aus geprüft und gewährt.
* Der Passkey ist jedoch kein Generalschlüssel für alle Applikationen, in denen man sich anmelden möchte. Jeder Account hat seinen eigenen Passkey. 
* Bei einer Anmeldung treten ihr Gerät und der angefragte Server in Kontakt und klären untereinander (anhand des Passkeys), ob der Zugriff gewährt werden kann. Der eigentliche Schlüssel (Private Key) verlässt dabei das Gerät nicht. Deshalb gilt Passkey als besonders sicher. 

## Wie funktioniert Passkey?

**Schritt 1:**<br> 
Ein Gerät (z.B. ein Smartphone oder ein PC) erhält einen Passkey (Private Key). Der Private Key wird z.B. von OpenOlat erstellt.
Dieser Schlüssel ist gerätespezifisch und bleibt immer auf dem Gerät (z.B. dem Smartphone) gespeichert. Er verlässt niemals den Sicherheitschip.


**Schritt 2:**<br> 
Mit Hilfe des Private Key wird auf dem Smartphone ein Public Key erstellt. Der Public Key ist mathematisch mit dem Private Key „verwandt“, aber es kann keine Kopie des Private Key daraus hergestellt werden. 

**Schritt 3:**<br>
Der Benutzer möchte mit seinem Gerät (z.B. dem Smartphone, auf dem der Private Key gespeichert ist) eine Applikation auf Server X (eine Website) aufrufen.

**Schritt 4:**<br>
Der Public Key wird an den Server X geschickt.<br>
Soll vom Smartphone eine andere Applikation auf einem anderen Server Y aufgerufen werden, muss der Public Key auch an diesen Server Y geschickt werden. Jede Applikation erhält einen eigenen Public Key. Die Applikationen wissen nicht voneinander, wer sonst noch einen solchen Public Key hat.

**Schritt 5:**<br>
Der Server X formuliert mit Hilfe des Public Keys eine Frage, die nur jemand beantworten kann, der über den Private Key verfügt. Diese Frage heisst „Challenge“ und wird vom Server X an das anfragende Gerät (z.B. das Smartphone) geschickt.

**Schritt 6:**<br>
Mit Hilfe des Private Keys ist das Beantworten der Challenge für das Smartphone kein Problem. Die Antwort (Response) wird vom Smartphone an den fragenden Server X geschickt.

**Schritt 7:**<br>
Der Server kann mit dem öffentlichen Schlüssel (Public Key) nun die Antwort auf Richtigkeit kontrollieren. Er könnte die Antwort aber niemals selbst berechnen. Das geht nur mit Hilfe des Private Keys auf dem Smartphone.<br> 
Ist die Antwort korrekt, gibt der Server grünes Licht: Die Challenge wurde korrekt beantwortet, der Zugriff kann gewährt werden.

**Passkey mit OpenOlat:**<br>
OpenOlat stösst die Erstellung eines Private Keys auf dem Zielgerät an und erhält von dort einen Public Key. (Der Private Key wird nicht ausserhalb des Zielgerätes erstellt und übermittelt.)

Bei künftigen Anmeldungen in OpenOlat von diesem Gerät aus werden dann jedes Mal die Prozessschritte 3-7 automatisch ausgeführt. Das vereinfacht die Anmeldung sehr, denn es wird kein Passwort benötigt. 


## Passkey aktivieren

Die Aktivierung von Passkey in OpenOlat erfolgt durch die Administrator:innen.

Passkey kann rollenbasiert konfiguriert werden und ist Teil eines dreistufigen Sicherheitskonzeptes in OpenOlat:

**Stufe 1: nur Passwort**<br>
**Stufe 2: nur Passkey**<br>
**Stufe 3: Passkey + Passwort**<br>

Ist in OpenOlat eine Sicherheitsstufe mit Passkey konfiguriert worden, dann werden die Benutzer:innen bei der nächsten Anmeldung angehalten, einen Passkey zu erstellen und diesen zukünftig für die Anmeldung zu verwenden.


!!! note "Hinweis"

    Für bestimmte Rollen (z.B. Benutzerverwalter:innen und Administrator:innen) wird Stufe 3 mit einem zusätzlichen Passwort empfohlen.<br> 
    (2-Stufen-Authentifizierung: Passkey + Passwort)


## Was sind Recovery Keys?

Wenn kein Passwort mehr vorhanden ist, kann es auch nicht mehr von Administrator:innen zurückgesetzt werden. 
Wurde in OpenOlat Passkey als alleinige Authentifizierungsmethode aktiviert, können keine Passwörter mehr vergeben werden. (Bei 2-Faktoren-Authentifizierung dagegegen schon, zusätzlich zu Passkey.)

Geht der Schlüssel trotzdem einmal verloren, benötigt es einen Ersatzschlüssel. Bei Passkey ist der Ersatzschlüssel jedoch keine Kopie des Originalschlüsses (Private Key).
Recovery Keys sind Einmal-Passwörter, die kein zweites Mal verwendet werden können.


## Neue Recovery keys anfordern

Die Recovery Keys können **im persönlichen Menü** unter **"Passwort"** angefordert werden.

!!! note "Hinweis"

    Wurden neue Recovery Keys bestellt, sind alle alten ungültig, auch wenn sie noch nie benutzt wurden.