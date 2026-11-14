# Cloud-Login {: #cloud_login}

Viele Organisationen führen die Konten ihrer Personen bereits bei einem Identitätsanbieter, etwa in Microsoft 365, bei Google oder in einem eigenen Keycloak. Mit dem Cloud-Login melden sich diese Personen mit ihrem bestehenden Konto bei OpenOlat an und brauchen kein eigenes OpenOlat-Passwort. Der Identitätsanbieter prüft Anmeldename und Passwort, OpenOlat erhält nur die Bestätigung und die Angaben zur Person, die der Identitätsanbieter freigibt.

Die Anbindungen richten Systemadministrator:innen in der System-Administration ein unter:<br>
`Administration > Login > Cloud-Login`

Die Seite ist immer im Menü, sie setzt keine Serverkonfiguration voraus.


## Authentifizierungsdienst hinzufügen [:octicons-tag-16:{ title="ab Release 10.1 (OO-729)" }](https://track.frentix.com/issue/OO-729) {: #add_provider}

Für die gängigen Identitätsanbieter bringt OpenOlat fertige Anbindungen mit. Sie wählen den Identitätsanbieter aus und tragen die Zugangsdaten ein, die er für OpenOlat ausstellt.

Das Menü "Weitere Aktionen" mit dem Symbol aus drei Punkten oben rechts auf der Seite listet die fertigen Anbindungen, die noch nicht hinzugefügt sind: Google, Facebook, LinkedIn, X (Twitter), Active Directory Federation Services, Microsoft Azure Active Directory, Keycloak, Switch edu-ID und Datenlotsen. Wählen Sie einen Eintrag, erscheint auf der Seite ein Abschnitt für diesen Identitätsanbieter. Hinzugefügte Identitätsanbieter führt das Menü nicht mehr auf.

![Im Menü Weitere Aktionen wählen Sie den Identitätsanbieter zum Hinzufügen, darunter die zwei Wege für einen eigenen OAuth-2.0-Provider](assets/login_cloud_login_add_provider_menu_v1_de.png){ class="shadow lightbox" title="Menü Weitere Aktionen auf der Seite Cloud-Login · 2026.11.12" }

So binden Sie einen Identitätsanbieter an:

1. Registrieren Sie OpenOlat beim Identitätsanbieter als Anwendung. Als Rücksprungadresse geben Sie dort die "Umleitungs-URI" an, die OpenOlat im Abschnitt "Login via OAuth, Cloud-Dienste und soziale Netzwerke" direkt unter dem Menü "Weitere Aktionen" anzeigt.
2. Wählen Sie den Identitätsanbieter im Menü "Weitere Aktionen".
3. Tragen Sie im Abschnitt des Identitätsanbieters die Zugangsdaten ein, die er für OpenOlat ausgestellt hat, etwa "Client ID" und "Client secret". Mit diesen beiden Angaben weist sich OpenOlat beim Identitätsanbieter aus.
4. Klicken Sie auf "Speichern".

Ab dann zeigt die Login-Seite den Identitätsanbieter zur Auswahl. Mit "Entfernen" im Abschnitt des Identitätsanbieters und einer Bestätigung nehmen Sie die Anbindung wieder weg.

### Active Directory Federation Services {: #adfs}

Für die Anmeldung mit einem Microsoft-Konto der Organisation bringt OpenOlat zwei Anbindungen mit. Welche passt, hängt davon ab, wo Ihre Organisation die Konten führt:

- **Microsoft Azure Active Directory:** Die Konten liegen im Clouddienst von Microsoft, den Organisationen mit Microsoft 365 nutzen. Die Einrichtung beschreibt der nächste Abschnitt.
- **Active Directory Federation Services:** Die Organisation betreibt den Anmeldedienst selbst, auf ihren eigenen Windows-Servern.

Im Abschnitt "Active Directory Federation Services" tragen Sie im Feld "OAuth2 endpoint (oAuthEndpoint)" die Adresse des Anmeldedienstes Ihrer Organisation ein, zum Beispiel `https://adfs.openolat.org/adfs/oauth2`, dazu "Client ID" und "Client secret". Das "Client secret" braucht es laut Hinweis im Formular nur für ADFS 2016. Welche Version im Einsatz ist und welche Werte gelten, weiss die Stelle, die den Anmeldedienst Ihrer Organisation betreibt.

Laut [Dokumentation von Microsoft](https://learn.microsoft.com/de-de/windows-server/identity/ad-fs/ad-fs-overview), Stand November 2026, gehört AD FS (Active Directory-Verbunddienste) zu Windows Server, und Microsoft empfiehlt den Wechsel zum Clouddienst Microsoft Entra ID, dem früheren Azure Active Directory. Die Adressen für die Anmeldung über [OAuth 2.0](#authorization_code_flow) liegen bei AD FS unter dem Pfad `/adfs/oauth2/` ([Microsoft: OIDC-Authentifizierung mit AD FS](https://learn.microsoft.com/de-de/SharePoint/security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-adfs)). "Client ID" und "Client secret" entstehen bei AD FS, wenn OpenOlat dort als Client registriert wird; AD FS lässt laut [Microsoft](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adfsod/7fc51569-b46d-4aba-8ae6-bad19cb9951b) nur registrierte Clients zu.

### Microsoft Azure Active Directory [:octicons-tag-16:{ title="ab Release 15.3 (OO-4904)" }](https://track.frentix.com/issue/OO-4904) {: #azure}

Arbeitet Ihre Organisation mit Microsoft 365, melden sich Ihre Mitarbeitenden mit ihrem Microsoft-Konto an. Dafür fügen Sie "Microsoft Azure Active Directory" hinzu. Microsoft hat diesen Dienst in Microsoft Entra ID umbenannt, unter diesem Namen finden Sie ihn bei Microsoft. Auf der Login-Seite heisst der Eintrag "Microsoft Azure AD".

Im Abschnitt "Microsoft Azure Active Directory" tragen Sie drei Angaben ein, die Microsoft für OpenOlat ausstellt: "Client ID", "Client secret" und "Verzeichnis-ID (Mandant)", die Kennung der Microsoft-365-Umgebung Ihrer Organisation. Dafür registrieren Sie OpenOlat zuerst bei Microsoft als App. Danach tragen Sie die drei Angaben in OpenOlat ein und klicken auf "Speichern". Ab dann zeigt die Login-Seite den Eintrag "Microsoft Azure AD". Die Zuordnung von Attributen braucht es bei dieser Anbindung nicht, "Attribute editieren" gibt es nur bei eigenen Providern.

Die Schritte bei Microsoft in den nächsten Absätzen geben die Dokumentation von Microsoft wieder, Stand November 2026. Microsoft kann Menüs und Beschriftungen jederzeit ändern.

#### App bei Microsoft registrieren {: #azure_app_registration}

Laut [Microsoft](https://learn.microsoft.com/de-de/entra/identity-platform/quickstart-register-app) registrieren Sie OpenOlat im Microsoft Entra Admin Center als App unter:<br>
`Entra ID > App-Registrierungen > Neue Registrierung`<br>
Dafür brauchen Sie bei Microsoft mindestens die Rolle "Anwendungsentwickler". Nach der Registrierung zeigt die Seite "Übersicht" der App die Anwendungs-ID (Client-ID). Diese tragen Sie in OpenOlat im Feld "Client ID" ein.

#### Umleitungs-URI bei Microsoft eintragen {: #azure_redirect_uri}

Microsoft schickt die Person nach der Anmeldung nur an eine Adresse zurück, die in der App als Umleitungs-URI eingetragen ist und genau übereinstimmt. Sonst bricht die Anmeldung mit dem Fehler AADSTS50011 ab ([Microsoft: Fehler AADSTS50011](https://learn.microsoft.com/en-us/troubleshoot/entra/entra-id/app-integration/error-code-aadsts50011-redirect-uri-mismatch)). Laut [Microsoft](https://learn.microsoft.com/de-de/entra/identity-platform/how-to-add-redirect-uri) tragen Sie die Adresse ein unter:<br>
`App-Registrierungen > "Ihre App" > Authentifizierung > Umleitungs-URI hinzufügen > Web`<br>
Als Umleitungs-URI geben Sie die "Umleitungs-URI" ein, die OpenOlat auf der Seite Cloud-Login im Abschnitt "Login via OAuth, Cloud-Dienste und soziale Netzwerke" anzeigt, und schliessen bei Microsoft mit "Konfigurieren" ab.

#### Geheimen Clientschlüssel bei Microsoft erzeugen {: #azure_client_secret}

Laut [Microsoft](https://learn.microsoft.com/de-de/entra/identity-platform/howto-create-service-principal-portal) erzeugen Sie den Schlüssel für das Feld "Client secret" unter:<br>
`App-Registrierungen > "Ihre App" > Zertifikate und geheime Schlüssel > geheime Clientschlüssel > Neuer geheimer Clientschlüssel`<br>
Sie geben eine Beschreibung und eine Gültigkeitsdauer ein und klicken auf "Hinzufügen". Microsoft zeigt den Wert des Schlüssels danach nur einmal an. Diesen Wert tragen Sie in OpenOlat im Feld "Client secret" ein. Ein geheimer Clientschlüssel gilt laut [Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials) höchstens 24 Monate, Microsoft empfiehlt weniger als 12 Monate. Erzeugen Sie vor dem Ablauf einen neuen Schlüssel und tragen Sie ihn in OpenOlat ein, sonst scheitert die Anmeldung über Microsoft.

#### Mandant bei Microsoft nachschlagen {: #azure_tenant}

Der Mandant (Tenant) ist die Microsoft-365-Umgebung Ihrer Organisation. Im Feld "Verzeichnis-ID (Mandant)" tragen Sie seine Kennung ein, damit sich nur Personen Ihrer Organisation anmelden. Bleibt das Feld leer, steht die Anmeldung allen Personen mit einem Microsoft-365-Konto offen. Ob OpenOlat für eine solche Person ein neues Konto anlegt, regelt "Kontoerstellung erlauben", siehe [Erster Login und neue Konten](#first_login). Microsoft nennt diese Kennung "Mandanten-ID" und zeigt sie laut [Microsoft](https://learn.microsoft.com/de-de/entra/fundamentals/how-to-find-tenant) im Microsoft Entra Admin Center unter:<br>
`Entra ID > Übersicht > Eigenschaften`<br>
Dafür brauchen Sie bei Microsoft mindestens die Rolle "Globaler Leser".

Sind das Modul "Microsoft Teams" und dessen Funktion "Terminaufzeichnung" eingeschaltet, fragt die Anmeldung über "Microsoft Azure AD" bei Microsoft eine zusätzliche Berechtigung ab, und dafür braucht es die Zustimmung der Administration Ihres Mandanten bei Microsoft, siehe [Modul Microsoft Teams: Funktion "Terminaufzeichnung"](Teams_module.de.md#recording_enabled). [:octicons-tag-16:{ title="ab Release 21.1.1 (OO-9888)" }](https://track.frentix.com/issue/OO-9888)

### Switch edu-ID [:octicons-tag-16:{ title="ab Release 16.2.6 (OO-6252)" }](https://track.frentix.com/issue/OO-6252) {: #switch_eduid}

Switch edu-ID ist ein persönliches Konto bei SWITCH, das einer Person auch nach einem Wechsel der Hochschule bleibt. Hochschulen in der Schweiz binden sie als Cloud-Login an, nicht über [Shibboleth](Login_Shibboleth.de.md). Mit "2-Faktor-Authentifizierung erzwingen" verlangt OpenOlat von Switch edu-ID eine Anmeldung mit zweitem Faktor; Switch edu-ID fragt die Person dann zusätzlich zum Passwort nach diesem Faktor.

### Datenlotsen {: #datenlotsen}

Datenlotsen ist ein Anbieter von Software für den Betrieb von Hochschulen und Akademien, darunter ein Campus-Management-System. Sein Angebot führt der Anbieter heute unter dem Namen octo. Die Anbindung "Datenlotsen" brauchen Sie nur, wenn sich die Personen Ihrer Organisation mit einem Konto aus einem System dieses Anbieters anmelden. Im Abschnitt "Datenlotsen" tragen Sie dann "Client ID" und "Client secret" ein, die der Anbieter für OpenOlat ausstellt, und unter "OAuth2 endpoint" die Adresse, unter der sein Anmeldedienst erreichbar ist.


## Eigenen Provider hinzufügen [:octicons-tag-16:{ title="ab Release 16.2.6 (OO-6267)" }](https://track.frentix.com/issue/OO-6267) {: #own_provider}

Fehlt Ihr Identitätsanbieter in der Liste, binden Sie ihn selbst an, sofern er OpenID Connect oder OAuth 2.0 unterstützt, die offenen Standards für eine Anmeldung über einen Identitätsanbieter. Das Menü "Weitere Aktionen" bietet dafür zwei Wege:

- **OAuth 2.0 Provider hinzufügen:** Sie tragen alle Angaben des Identitätsanbieters von Hand ein, darunter "Provider name", "Display name", "Client Id", "Client secret", "Response type" und die Adressen der Endpunkte. Endpunkte sind die Adressen beim Identitätsanbieter, die OpenOlat bei der Anmeldung aufruft: Unter "Authorization end point" meldet sich die Person an. Über "Token URL" holt OpenOlat danach ein Access Token ab, einen Berechtigungsnachweis für die Angaben zur Person. Ist "User info (optional)" ausgefüllt, ruft OpenOlat mit diesem Token dort weitere Angaben zur Person ab.
- **OAuth 2.0 Provider mit Discovery URL hinzufügen:** Sie geben nur die "URL" ein, unter der der Identitätsanbieter seine Konfiguration veröffentlicht. Mit "Konfiguration laden" übernimmt OpenOlat die übrigen Angaben in das Formular.

### Provider name und Display name {: #provider_name}

Beide Namen legen Sie beim Hinzufügen fest. "Display name" ist die Beschriftung, mit der die Login-Seite den Identitätsanbieter zur Auswahl anbietet. Sie können ihn später im Abschnitt des Providers ändern. "Provider name" ist die interne Kennung der Anbindung: 3 bis 8 Zeichen aus Buchstaben ohne Umlaute, Ziffern, Punkt, Bindestrich und Unterstrich, und jeder Name nur einmal. OpenOlat speichert die Anmeldungen der Personen über diesen Provider unter diesem Namen, deshalb lässt er sich nach dem Hinzufügen nicht mehr ändern.

### Discovery URL {: #discovery_url}

Mit "OAuth 2.0 Provider mit Discovery URL hinzufügen" lädt OpenOlat die Konfiguration des Identitätsanbieters und füllt damit das Formular vor: "Issuer", "Authorization end point", "Token URL", "User info (optional)", "Response type" und "Scopes". Prüfen Sie die Angaben und ergänzen Sie "Provider name", "Display name", "Client Id" und "Client secret". "Client Id" ist dieselbe Angabe, die bei den fertigen Anbindungen "Client ID" heisst. Für "Response type" gilt der Wert "code", siehe [OAuth 2.0 und OpenID Connect](#authorization_code_flow).

Zwei Begriffe stammen aus den Standards: Der Issuer ist die Adresse, mit der sich der Identitätsanbieter ausweist. Scopes sind die Bereiche von Angaben zur Person, die OpenOlat beim Identitätsanbieter anfragt ([OAuth 2.0, RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749), Abschnitt 3.3).

Nach dem Standard [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html), Abschnitt 4, veröffentlicht ein Identitätsanbieter seine Konfiguration unter seiner Issuer-Adresse mit dem Zusatz `/.well-known/openid-configuration`. Die genaue Adresse nennt die Dokumentation des Identitätsanbieters.

### Attribute editieren {: #attribute_mapping}

Mit "Attribute editieren" im Abschnitt des Providers legen Sie fest, welches Attribut des Identitätsanbieters in welches Attribut des OpenOlat-Kontos übernommen wird. Links tragen Sie den Namen des Attributs beim Identitätsanbieter ein, rechts wählen Sie das Attribut in OpenOlat.

Für die Anmeldung braucht OpenOlat mindestens eine Kennung, die die Person beim Identitätsanbieter eindeutig bezeichnet. Liefert der Identitätsanbieter ein Token nach OpenID Connect, nimmt OpenOlat dafür ohne Zuordnung dessen Wert "sub", die Kennung der Person, die nach dem Standard [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html), Abschnitt 2, in jedem solchen Token steht. Sonst ordnen Sie ein solches Attribut dem OpenOlat-Attribut "Identifier" zu. Fehlt die Kennung, bricht die Anmeldung mit der Meldung "Sie konnten nicht identifiziert werden" ab. Damit OpenOlat beim ersten Login ein bestehendes Konto findet, ordnen Sie zusätzlich die E-Mail-Adresse zu, siehe [Erster Login und neue Konten](#first_login). Soll OpenOlat neue Konten ohne Registrierungsdialog anlegen, braucht es auch "Nickname" für den Anmeldenamen und alle Pflichtfelder des Profils.

Die Namen der Attribute legt der Identitätsanbieter fest. Der Standard [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html), Abschnitt 5.1, nennt unter anderem `email` für die E-Mail-Adresse, `given_name` für den Vornamen, `family_name` für den Nachnamen und `preferred_username` für den bevorzugten Anmeldenamen. Welche davon Ihr Identitätsanbieter liefert, steht in seiner Dokumentation.

### OAuth 2.0 und OpenID Connect [:octicons-tag-16:{ title="ab Release 20.2.6 (OO-9287)" }](https://track.frentix.com/issue/OO-9287) {: #authorization_code_flow}

Aus Sicherheitsgründen unterstützt OpenOlat für OpenID-Connect- und OAuth-2.0-Anbindungen ausschliesslich den Authorization Code Flow. Bei diesem Ablauf leitet OpenOlat die Person zur Anmeldung an den Identitätsanbieter weiter. Der Identitätsanbieter schickt sie mit einem Code zurück, den OpenOlat nur einmal einlösen darf. OpenOlat tauscht diesen Code direkt beim Identitätsanbieter gegen das Access Token ein, so läuft das Token nie über den Browser der Person. Beim Anlegen eines Providers über "OAuth 2.0 Provider hinzufügen" oder über die Discovery URL wählen Sie deshalb im Feld "Response type" den Wert "code".

[Zum Seitenanfang ^](#cloud_login)


## Automatische Umleitung [:octicons-tag-16:{ title="ab Release 13.1.1 (OO-3847)" }](https://track.frentix.com/issue/OO-3847) {: #automatic_redirect}

Melden sich alle Personen über denselben Identitätsanbieter an, sparen Sie ihnen den Umweg über die Login-Seite. Mit "Automatische Umleitung (lokaler Login über /maintenance/)" im Abschnitt des Identitätsanbieters öffnet OpenOlat beim Aufruf sofort die Anmeldung des Identitätsanbieters. Die Option steht bei Active Directory Federation Services, Microsoft Azure Active Directory, Keycloak, Switch edu-ID, Datenlotsen und bei eigenen Providern. Schalten Sie sie nur bei einem Identitätsanbieter ein, OpenOlat leitet immer zu einem einzigen weiter.

Die Login-Seite mit dem OpenOlat-Passwort bleibt erreichbar: Rufen Sie die Adresse Ihrer Installation mit dem Zusatz `/maintenance/` auf, zum Beispiel `https://your.openolat.domain/maintenance/`. Diesen Weg brauchen Systemadministrator:innen etwa, wenn der Identitätsanbieter nicht erreichbar ist.


## Erster Login und neue Konten {: #first_login}

Wie OpenOlat eine Person beim ersten Login über einen Identitätsanbieter aufnimmt, legen Sie im Abschnitt "Login via OAuth, Cloud-Dienste und soziale Netzwerke" fest.

Zuerst sucht OpenOlat ein bestehendes Konto: über die E-Mail-Adresse, die der Identitätsanbieter liefert, und danach über den Anmeldenamen, den der Identitätsanbieter liefert. Findet OpenOlat ein Konto, verknüpft es die Anmeldung damit. Die Person behält ihre Kurse und Daten und meldet sich künftig über den Identitätsanbieter an.

Findet OpenOlat kein Konto, entscheidet "Kontoerstellung erlauben":

- **Eingeschaltet:** OpenOlat legt ein neues Konto an. Die Person ergänzt dabei ihre Angaben in einem Registrierungsdialog.
- **Ausgeschaltet:** Die Person sieht die Meldung "Ihr Konto wurde auf dem OpenOlat-Dienst noch nicht angelegt, dies ist notwendig, um sich anmelden zu können. Bitte kontaktieren Sie die Systemadministration." Sie legen das Konto vorher in der Benutzerverwaltung an, siehe [Konto erstellen](../usermanagement/Create_User.de.md).

Ist "Kontoerstellung erlauben" eingeschaltet, erscheinen zwei weitere Optionen:

- **Interaktiven Registrierungsdialog überspringen, wenn möglich:** OpenOlat legt das neue Konto ohne Registrierungsdialog an, sofern der Identitätsanbieter einen gültigen Anmeldenamen und alle Pflichtfelder des Profils liefert. [:octicons-tag-16:{ title="ab Release 15.5.0 (OO-5381)" }](https://track.frentix.com/issue/OO-5381)
- **Disclaimer-Dialog überspringen:** OpenOlat fragt Personen, die sich über einen Identitätsanbieter anmelden, nicht nach der Zustimmung zu den Nutzungsbedingungen.

Mit welchen Verfahren sich ein einzelnes Konto anmeldet, sehen Administrator:innen im Reiter "Authentifizierungen" des Kontos:<br>
`Benutzerverwaltung > "Konto der Person" > Reiter "Authentifizierungen"`<br>
Dort ergänzen oder löschen sie auch einzelne Authentifizierungen, siehe [Kontoeinstellungen verwalten](../usermanagement/Configure_User.de.md).

Welche Meldungen eine Person sieht, wenn die Anmeldung über den Identitätsanbieter scheitert, steht auf der [Login-Seite](../../manual_user/login_registration/Login_Page.de.md#external_login) im Benutzerhandbuch.

[Zum Seitenanfang ^](#cloud_login)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Microsoft: Übersicht über AD FS >](https://learn.microsoft.com/de-de/windows-server/identity/ad-fs/ad-fs-overview)<br>
[Microsoft: OIDC-Authentifizierung mit AD FS >](https://learn.microsoft.com/de-de/SharePoint/security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-adfs)<br>
[Microsoft: OAuth und OpenID Connect bei AD FS >](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adfsod/7fc51569-b46d-4aba-8ae6-bad19cb9951b)<br>
[Microsoft: Anwendung registrieren >](https://learn.microsoft.com/de-de/entra/identity-platform/quickstart-register-app)<br>
[Microsoft: Fehler AADSTS50011 >](https://learn.microsoft.com/en-us/troubleshoot/entra/entra-id/app-integration/error-code-aadsts50011-redirect-uri-mismatch)<br>
[Microsoft: Umleitungs-URI hinzufügen >](https://learn.microsoft.com/de-de/entra/identity-platform/how-to-add-redirect-uri)<br>
[Microsoft: Geheimen Clientschlüssel erstellen >](https://learn.microsoft.com/de-de/entra/identity-platform/howto-create-service-principal-portal)<br>
[Microsoft: Anmeldeinformationen hinzufügen >](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials)<br>
[Microsoft: Mandanten-ID finden >](https://learn.microsoft.com/de-de/entra/fundamentals/how-to-find-tenant)<br>
[Modul Microsoft Teams >](Teams_module.de.md)<br>
[Shibboleth >](Login_Shibboleth.de.md)<br>
[OpenID Connect Discovery >](https://openid.net/specs/openid-connect-discovery-1_0.html)<br>
[OAuth 2.0, RFC 6749 >](https://datatracker.ietf.org/doc/html/rfc6749)<br>
[OpenID Connect Core >](https://openid.net/specs/openid-connect-core-1_0.html)<br>
[Konto erstellen >](../usermanagement/Create_User.de.md)<br>
[Kontoeinstellungen verwalten >](../usermanagement/Configure_User.de.md)<br>
[Login-Seite >](../../manual_user/login_registration/Login_Page.de.md)

**Weiterführend**<br>
[Login: Übersicht >](Login/index.de.md)<br>
[LDAP >](Login_LDAP.de.md)<br>
[Login-Konzept >](../../manual_user/login_registration/Login_Concept.de.md)

[Zum Seitenanfang ^](#cloud_login)
