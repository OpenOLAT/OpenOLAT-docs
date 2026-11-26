# Login-Konzept {: #login_concept}

Wie Sie sich bei OpenOlat anmelden, hängt davon ab, wer Ihr Passwort verwaltet: OpenOlat selbst oder ein anderes System Ihrer Organisation. OpenOlat unterscheidet deshalb zwei Login-Konzepte, die Ihre Organisation einzeln oder kombiniert einsetzt:

* Lokale Authentifizierung
* Externe Authentifizierung


## Lokale Authentifizierung

Bei der lokalen Authentifizierung speichert OpenOlat Anmeldename und Passwort selbst (lokal).

## Externe Authentifizierung

Bei der externen Authentifizierung verwaltet ein anderes System das Passwort und prüft die Anmeldung. OpenOlat erhält von diesem System die Bestätigung, dass die Person zum Zutritt berechtigt ist. OpenOlat kennt drei solche Verfahren:

- **Cloud-Login:** Ein Identitätsanbieter wie Microsoft, Google oder Switch edu-ID übernimmt die Anmeldung. Das Verfahren beruht auf OAuth 2.0 und OpenID Connect.
- **LDAP:** Die Anmeldung läuft über das Verzeichnis Ihrer Organisation, etwa Active Directory.
- **Shibboleth:** Sie melden sich bei Ihrer Hochschule an.

Welche Verfahren Ihre Organisation anbietet, legen die Systemadministrator:innen fest. Wie sie die Verfahren einrichten, steht im Administrationshandbuch unter [Login: Übersicht](../../manual_admin/administration/Login/index.de.md#login_methods).

## Mehrere Login-Verfahren kombinieren {: #combined_login_methods}

Ihre Organisation kann mehrere Login-Verfahren gleichzeitig einschalten, damit sich jede Personengruppe auf ihrem Weg anmeldet. Jede Person wählt bei der Anmeldung eines dieser Verfahren, ein einziges genügt. Welches Verfahren für Sie gilt, sagt Ihnen Ihre Organisation. Ein Beispiel: Mitarbeitende melden sich über "Microsoft Azure AD" mit dem Konto an, das sie auch für die übrigen Dienste der Organisation verwenden. Externe Personen ohne ein solches Konto melden sich mit ihrem OpenOlat-Passwort an, also über die lokale Authentifizierung.

Die Login-Seite zeigt jedes eingeschaltete Verfahren in einem eigenen Bereich, getrennt durch "oder". Die Identitätsanbieter des Cloud-Logins stehen gemeinsam unter "Bitte wählen Sie Ihren Identitätsanbieter.", jeder mit einem eigenen Button. Für das OpenOlat-Passwort und für LDAP geben Personen Anmeldename und Passwort im selben Formular ein. Personen aus dem LDAP-Verzeichnis verwenden dort das Passwort ihrer Organisation.

Systemadministrator:innen können bei einem Identitätsanbieter die Option "Automatische Umleitung (lokaler Login über /maintenance/)" einschalten. Wer OpenOlat aufruft, landet dann sofort bei der Anmeldung dieses Identitätsanbieters. Die Login-Seite mit den übrigen Verfahren erreichen Personen nur noch über die Adresse von OpenOlat mit dem Zusatz `/maintenance/`, zum Beispiel `https://your.openolat.domain/maintenance/`. Die Umleitung passt deshalb zu Organisationen, in denen sich alle Personen über denselben Identitätsanbieter anmelden.

Wie Systemadministrator:innen die Verfahren einschalten, steht im Administrationshandbuch unter [Login: Übersicht](../../manual_admin/administration/Login/index.de.md#login_methods). Die automatische Umleitung beschreibt die Seite [Cloud-Login](../../manual_admin/administration/Login_Cloud_Login.de.md#automatic_redirect), ebenso wie OpenOlat eine Person beim ersten Login über einen Identitätsanbieter mit ihrem bestehenden Konto verknüpft oder für sie ein neues Konto anlegt.

Einen zusätzlichen Nachweis nach dem Passwort bei derselben Anmeldung (zweiter Faktor), etwa einen Passkey oder einen One Time Code, beschreibt die Seite [Sicherheitsstufen](../login_registration/Security_levels.de.md).

## Passkey [:octicons-tag-16:{ title="ab Release 18.1 (OO-7180)" }](https://track.frentix.com/issue/OO-7180)

Ein Passkey ist ein digitaler Schlüssel, den Ihr Gerät speichert. Je nach Sicherheitsstufe melden Sie sich mit dem Passkey statt mit dem Passwort an oder weisen sich nach dem Passwort zusätzlich damit aus. Der Passkey ist an das Gerät gebunden, Sie müssen sich dafür kein Passwort merken.

Wie Sie einen Passkey erstellen und verwenden, steht auf der Seite [Passkey](../login_registration/Passkey.de.md).

## One Time Code [:octicons-tag-16:{ title="ab Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509)

Der One Time Code ist ein zweiter Faktor beim Login. Nach Eingabe von Anmeldename und Passwort erhalten Kontoinhaber:innen einen 8-stelligen Bestätigungscode per E-Mail und schliessen die Anmeldung mit diesem Code ab. Systemadministrator:innen schalten den One Time Code unabhängig von Passkey ein. Ist Passkey ebenfalls eingeschaltet, dient der One Time Code als Ausweichlösung für Konten ohne hinterlegten Passkey.

Wie die Anmeldung mit dem Code abläuft, steht auf der Seite [One Time Code](../login_registration/One_Time_Code.de.md).

## Weiterführende Informationen {: #further_information}

[Login: Übersicht >](../../manual_admin/administration/Login/index.de.md)<br>
[Cloud-Login >](../../manual_admin/administration/Login_Cloud_Login.de.md)<br>
[Sicherheitsstufen >](../login_registration/Security_levels.de.md)<br>
[Passkey >](../login_registration/Passkey.de.md)<br>
[One Time Code >](../login_registration/One_Time_Code.de.md)<br>
[Login-Seite >](../login_registration/Login_Page.de.md)

[Zum Seitenanfang ^](#login_concept)
