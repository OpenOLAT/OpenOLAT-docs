# Sicherheitsstufen {: #security_levels}


## Welche Sicherheitsstufen gibt es? [:octicons-tag-16:{ title="ab Release 18.1 (OO-7180)" }](https://track.frentix.com/issue/OO-7180) {: #levels}

[Passkey](Passkey.de.md) ist Teil eines dreistufigen Sicherheitskonzeptes in OpenOlat:

**Stufe 1 - Passwort**: Anmeldung nur mit Passwort<br>
**Stufe 2 - Passkey**: Anmeldung nur mit Passkey<br>
**Stufe 3 - Passwort & Passkey (2FA)**: Anmeldung mit Passwort und Passkey (2-Faktor-Authentifizierung)

Zusätzlich können Systemadministrator:innen den [One Time Code](One_Time_Code.de.md) aktivieren. Benutzer:innen ohne hinterlegten Passkey bestätigen ihre Anmeldung dann mit einem Bestätigungscode per E-Mail. [:octicons-tag-16:{ title="ab Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509)


## Durch Systemadministrator:innen gesetzte Sicherheitsstufen {: #admin_levels}

Für manche Rollen macht eine höhere Sicherheitsstufe Sinn, z.B. für Benutzerverwalter:innen oder Administrator:innen. In OpenOlat kann deshalb für jede Rolle separat eine minimal erforderliche Sicherheitsstufe eingestellt werden. Systemadministrator:innen legen die Stufe pro Rolle in der System-Administration fest unter:<br>
`Administration > Login > Passwort und Authentifizierung > Tab "Authentifizierung"`

Mit dem Button "Alle Rollen auf Stufe… setzen" lässt sich eine Stufe für alle Rollen gleichzeitig übernehmen.

![Markiert die Tabelle mit der Mindeststufe 1 bis 3 je Rolle und den Button "Alle Rollen auf Stufe… setzen"](assets/security_levels_v2_de.png){ class="shadow lightbox" title="Tab Authentifizierung im Menü Passwort und Authentifizierung · 2026.10.31" }


## Sicherheitsstufen wechseln {: #change_level}

Systemadministrator:innen können mit der Option "Sicherheitsstufe selbständig erhöhen" die Erlaubnis erteilen, dass Benutzer:innen ihre Sicherheitsstufe selbst bestimmen.

Die Umstellung erfolgt mit dem Button "Sicherheitsstufe wechseln" unter:<br>
`Persönliches Menü > Passwort`

![Markiert den Button "Sicherheitsstufe wechseln" neben der aktuellen Stufe und den Stufen, zu denen das Konto wechseln kann](assets/security_levels_user_settings_v2_de.png){ class="shadow lightbox" title="Seite Passwort im persönlichen Menü · 2026.10.31" }

Wird für das Höherstufen ein Passkey benötigt, können die Benutzer:innen den Passkey selbst generieren, ebenfalls unter `Persönliches Menü > Passwort`.

Wenn Benutzer:innen ihre Sicherheitsstufe selbst ändern dürfen, ist prinzipiell ein Erhöhen oder Herunterstufen möglich. Ob ein Herunterstufen möglich ist, hängt aber von der Vorgabe der Systemadministrator:innen ab.

Die minimale Stufe wird von Systemadministrator:innen gesetzt. Wenn z.B. Stufe 2 für die Rolle Benutzerverwalter:in vorgeschrieben wird, kann eine Benutzerverwalter:in nicht auf Stufe 1 (nur Passwort) herunterstufen, sondern nur zwischen Stufe 2 (nur Passkey) und Stufe 3 (2-Faktor-Authentifizierung) wählen.


## Weiterführende Informationen {: #further_information}

[Passkey >](Passkey.de.md)<br>
[One Time Code >](One_Time_Code.de.md)

[Zum Seitenanfang ^](#security_levels)
