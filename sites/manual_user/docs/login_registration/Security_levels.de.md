# Sicherheitsstufen


## Welche Sicherheitsstufen gibt es?

Passkey ist Teil eines dreistufigen Sicherheitskonzeptes in OpenOlat:

**Stufe 1: nur Passwort**<br>
**Stufe 2: nur Passkey**<br>
**Stufe 3: Passkey + Passwort**<br>


## Durch Administrator:innen gesetzte Sicherheitsstufen

Für manche Rollen macht eine höhere Sicherheitsstufe Sinn, z.B. für Benutzerverwalter:innen oder Administrator:innen.
In OpenOlat kann deshalb für jede Rolle separat eine minimal erforderliche Sicherheitsstufe eingestellt werden.

![security_levels_v1_de.png](assets/security_levels_v1_de.png){ class=" shadow lightbox" }


## Sicherheitsstufen wechseln

Administrator:innen können die Erlaubnis erteilen, dass Benutzer:innen die Sicherhheitsstufe beim Login selbst bestimmen können.

Die Umstellung kann gemacht werden **im persönlichen Menü** unter **"Passwort"**.

![security_levels_user_settings_v1_de.png](assets/security_levels_user_settings_v1_de.png){ class=" shadow lightbox" }

Wird für das Höherstufen ein Passkey benötigt, können die Benutzer:innen den Passkey selbst generieren. (Ebenfalls im persönlichen Menü unter **"Passwort"**)

Wenn Benutzer:innen ihre Sicherheitsstufe selbst ändern dürfen, ist prinzipiell ein Erhöhen oder Herunterstufen möglich. Ob ein Herunterstufen möglich ist, hängt aber von der Vorgabe der Administrator:innen ab.

Die minimale Stufe wird von Administrator:innen gesetzt. Wenn z.B. Stufe 2 für die Rolle Benutzerverwalter:in vorgeschrieben wird, kann ein/eine Benutzerverwalter:in nicht auf Stufe 1 (nur Passwort) herunterstufen, sondern nur zwischen Stufe 2 (nur Passkey) und Stufe 3 (2-Faktoren-Authentifizierung) wählen.
