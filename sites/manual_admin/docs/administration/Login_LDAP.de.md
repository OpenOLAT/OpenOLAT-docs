# LDAP {: #ldap}

!!! info "frentix-Kund:innen"
    Die Anbindung an LDAP ist Teil der Serverkonfiguration. Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix die Änderung.

Viele Organisationen führen die Konten ihrer Mitarbeitenden oder Studierenden in einem Verzeichnis wie Active Directory. Mit der LDAP-Anbindung übernimmt OpenOlat die Konten aus diesem Verzeichnis und prüft beim Login Anmeldename und Passwort gegen das Verzeichnis. Personen melden sich auf der Login-Seite mit den Zugangsdaten an, die sie in Ihrer Organisation ohnehin verwenden, und Sie pflegen die Konten an einer Stelle.

Ist LDAP eingeschaltet, finden Systemadministrator:innen die Seite "LDAP Verwaltung" in der System-Administration unter:<br>
`Administration > Login > LDAP`


## Was die Serverkonfiguration festlegt {: #server_configuration}

Die Serverkonfiguration ist die Konfigurationsdatei der Installation. Diese Datei pflegt die Stelle, die OpenOlat betreibt. Die Verbindung zum Verzeichnis steht dort, nicht in der Oberfläche: welcher Verzeichnisserver angebunden ist, in welchen Bereichen des Verzeichnisses OpenOlat Konten sucht und welche Angaben es übernimmt. In der Standardkonfiguration übernimmt OpenOlat Anmeldename, E-Mail-Adresse, Vorname und Nachname. Weitere Profilfelder lassen sich zuordnen. Auf Wunsch übernimmt OpenOlat aus dem Verzeichnis auch Mitgliedschaften in Gruppen und Organisationen sowie Rollen wie Autor:in.

Eine Änderung an dieser Verbindung gilt erst ab dem nächsten Neustart. Ohne eingeschaltetes LDAP fehlt der Eintrag "LDAP" im Menü `Administration > Login`.

Gleicht Ihr OpenOlat Organisationen mit LDAP-Gruppen ab, beachten Sie den Hinweis zur Standardorganisation unter [Modul Organisationen: Metadaten](Modules_Organisations.de.md#edit_metadata).

[Zum Seitenanfang ^](#ldap)


## Synchronisation starten {: #synchronisation}

Die Synchronisation gleicht die Konten in OpenOlat mit dem Verzeichnis ab: Sie legt Konten für neue Personen an und aktualisiert die übernommenen Angaben. In der Standardkonfiguration läuft sie jede Stunde. Meldet sich eine neue Person vor der nächsten Synchronisation an, legt OpenOlat ihr Konto beim Login an.

Im Bereich "Synchronisation starten" zeigt die Seite, wann die "Letzte Synchronisation" lief. Mit "Starte Synchronisation" starten Sie sie sofort, etwa nachdem im Verzeichnis viele Personen hinzugekommen sind.

Einzelne Personen übernehmen Sie auch in der Benutzerverwaltung aus dem Verzeichnis, siehe [Konten aus LDAP oder Azure übernehmen](../usermanagement/Create_User.de.md#import_external_users).

Ob sich ein einzelnes Konto über LDAP anmeldet, sehen Administrator:innen im Reiter "Authentifizierungen" des Kontos:<br>
`Benutzerverwaltung > "Konto der Person" > Reiter "Authentifizierungen"`<br>
Mehr dazu unter [Kontoeinstellungen verwalten](../usermanagement/Configure_User.de.md).

[Zum Seitenanfang ^](#ldap)


## Lebenszyklus Konten {: #account_lifecycle}

Verlässt eine Person Ihre Organisation, verschwindet sie aus dem Verzeichnis. Ihr Konto in OpenOlat bleibt in der Standardkonfiguration bestehen, bis Sie es entfernen. Dafür wählen Sie im Bereich "Lebenszyklus Konten" eine der beiden Aktionen:

- **Inaktivieren:** Die Person kann sich nicht mehr anmelden, das Konto bleibt mit allen Daten erhalten. Mehr dazu unter [Deaktivierung und Reaktivierung](Life_cycles_-_Administration/index.de.md#account_reactivation). [:octicons-tag-16:{ title="ab Release 17.1.5 (OO-6649)" }](https://track.frentix.com/issue/OO-6649)
- **Löschen:** OpenOlat löscht die Konten, siehe [Benutzer:in löschen](../usermanagement/Delete_User.de.md).

Nach dem Klick auf eine der beiden Aktionen listet ein Assistent die Konten, die im Verzeichnis fehlen. Sie wählen die Konten aus und bestätigen.

Bis Sie ein Konto entfernen, kann sich die Person mit dem zuletzt verwendeten Passwort weiter anmelden, wenn OpenOlat eine Kopie des LDAP-Passworts speichert (siehe [Wartungsfunktionen](#maintenance)).

Die Serverkonfiguration kann auch festlegen, dass die Synchronisation solche Konten selbst löscht oder inaktiviert. Damit eine Störung im Verzeichnis nicht alle Konten trifft, ändert die Synchronisation dann nichts, wenn bei der Hälfte oder mehr der OpenOlat-Konten mit LDAP-Anmeldung der Eintrag im Verzeichnis fehlt. Diese Grenze ist der Standardwert der Serverkonfiguration. Wird sie erreicht, entfernen Sie die Konten im Bereich "Lebenszyklus Konten" von Hand.

[Zum Seitenanfang ^](#ldap)


## Wartungsfunktionen {: #maintenance}

Damit sich Personen auch anmelden können, wenn der Verzeichnisserver nicht erreichbar ist, kann OpenOlat beim Login eine Kopie des LDAP-Passworts speichern. Ist diese Kopie in der Serverkonfiguration eingeschaltet, zeigt die Seite den Bereich "Wartungsfunktionen". Mit "Authentifizierungen aus Cache löschen" entfernen Sie die gespeicherten Kopien. Bis sich eine Person wieder erfolgreich über LDAP angemeldet hat und OpenOlat die Kopie neu anlegt, prüft OpenOlat ihre Anmeldung nur gegen das Verzeichnis. Fällt der Verzeichnisserver in dieser Zeit aus, kann sie sich nicht anmelden.

[Zum Seitenanfang ^](#ldap)


## Logging {: #logging}

Läuft eine Synchronisation nicht wie erwartet, finden Sie die Ursache im Bereich "Logging". Er zeigt die Meldungen der LDAP-Anbindung fortlaufend an, etwa den Verlauf einer Synchronisation oder Konten, die im Verzeichnis fehlen.

[Zum Seitenanfang ^](#ldap)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Organisationen >](Modules_Organisations.de.md)<br>
[Konto erstellen >](../usermanagement/Create_User.de.md)<br>
[Kontoeinstellungen verwalten >](../usermanagement/Configure_User.de.md)<br>
[Lebenszyklen: Übersicht >](Life_cycles_-_Administration/index.de.md)<br>
[Benutzer:in löschen >](../usermanagement/Delete_User.de.md)

**Weiterführend**<br>
[Login: Übersicht >](Login/index.de.md)<br>
[Cloud-Login >](Login_Cloud_Login.de.md)<br>
[Shibboleth >](Login_Shibboleth.de.md)

[Zum Seitenanfang ^](#ldap)
