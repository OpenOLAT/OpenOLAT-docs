# Shibboleth {: #shibboleth}

!!! info "frentix-Kund:innen"
    Die Anbindung an Shibboleth ist Teil der Serverkonfiguration. Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix die Änderung.

Hochschulen, die zu einer Shibboleth-Föderation gehören, prüfen die Anmeldung ihrer Angehörigen selbst. Eine Föderation ist ein Verbund von Hochschulen, die diese Anmeldungen gegenseitig anerkennen, etwa die Föderation von SWITCH in der Schweiz. Mit Shibboleth melden sich diese Personen bei OpenOlat mit dem Konto ihrer Heimathochschule an. OpenOlat erhält dabei kein Passwort, sondern nur die Attribute, die die Hochschule freigibt, etwa Name, E-Mail-Adresse und Studiengang. Sie verwalten in OpenOlat keine Passwörter, und neue Angehörige der Hochschule erhalten ihr Konto beim ersten Login.

Ist Shibboleth eingeschaltet, finden Systemadministrator:innen die Seite in der System-Administration unter:<br>
`Administration > Login > Shibboleth`


## Was die Serverkonfiguration festlegt {: #server_configuration}

Die Serverkonfiguration ist die Konfigurationsdatei der Installation, die Seite in der Administration nennt sie "OpenOlat-Konfigurationsdatei". Diese Datei pflegt die Stelle, die OpenOlat betreibt. Die Basiskonfiguration steht dort: die Anbindung an die Föderation, welche Attribute OpenOlat in welche Profilfelder übernimmt und welcher Organisation neue Konten zugeordnet werden. Die Seite in der Administration weist darauf mit dem Satz "Die Shibboleth-Basiskonfiguration muss in der OpenOlat-Konfigurationsdatei vorgenommen werden." hin.

Eine Änderung an der Basiskonfiguration gilt erst ab dem nächsten Neustart. Ohne eingeschaltetes Shibboleth fehlt der Eintrag "Shibboleth" im Menü `Administration > Login`.

Je nach Serverkonfiguration zeigt die Login-Seite für Shibboleth eine Auswahl der Hochschule über den Auswahldienst von SWITCH oder eine einfache Anmeldemaske, die zur Anmeldung bei der Hochschule weiterleitet. Die Seite in der Administration ist in beiden Fällen dieselbe.

[Zum Seitenanfang ^](#shibboleth)


## Erster Login {: #first_login}

Meldet sich eine Person zum ersten Mal über Shibboleth an, führt OpenOlat sie durch eine Registrierung und legt ihr Konto an. Bei jedem weiteren Login gleicht OpenOlat das Profil mit den freigegebenen Attributen ab. Ist das Konto inaktiv, reaktiviert OpenOlat es beim Login automatisch, siehe [Deaktivierung und Reaktivierung](Life_cycles_-_Administration/index.de.md#account_reactivation). [:octicons-tag-16:{ title="ab Release 15.2.8 (OO-5045)" }](https://track.frentix.com/issue/OO-5045)

Ob sich ein einzelnes Konto über Shibboleth anmeldet, sehen Administrator:innen im Reiter "Authentifizierungen" des Kontos:<br>
`Benutzerverwaltung > "Konto der Person" > Reiter "Authentifizierungen"`<br>
Mehr dazu unter [Kontoeinstellungen verwalten](../usermanagement/Configure_User.de.md).

[Zum Seitenanfang ^](#shibboleth)


## Attribute Access Control [:octicons-tag-16:{ title="ab Release 10.3.3 (OO-1588)" }](https://track.frentix.com/issue/OO-1588) {: #attribute_access_control}

Nicht jede Person, die sich bei ihrer Hochschule anmelden kann, soll OpenOlat nutzen. Mit "Attribute Access Control aktivieren" lassen Sie nur Personen hinein, deren Attribute einen zugelassenen Wert tragen, zum Beispiel nur Angehörige einer bestimmten Hochschule oder eines Studiengangs.

Sie legen bis zu zwei Attribute fest:

- **Shibboleth-Attribut 1:** der Name des Attributs, das OpenOlat prüft, so wie die Anbindung Ihrer Installation es an OpenOlat übergibt.
- **Gültige Werte für Attribut 1:** die zugelassenen Werte, getrennt durch Zeilenumbruch, Komma oder Semikolon. Gross- und Kleinschreibung spielen keine Rolle.
- **Shibboleth-Attribut 2** und **Gültige Werte für Attribut 2:** ein zweites Attribut mit seinen Werten, nach demselben Muster.

Eine Person erhält Zugang, wenn eines der beiden Attribute einen der zugelassenen Werte trägt. Allen anderen zeigt OpenOlat die Meldung "Sie dürfen nicht auf OpenOlat einloggen." OpenOlat prüft die Attribute bei jeder Anmeldung über Shibboleth, auch bei Personen, die schon ein Konto haben.

Welche Attribute eine Hochschule liefern kann, legt die Föderation fest. Bei SWITCH heisst die Föderation "Switch edu-ID Federation", ihre Attribute beschreibt die "Switch edu-ID Attribute Specification". Für eine Zugangsbeschränkung eignen sich zum Beispiel diese zwei Attribute:

- **swissEduPersonHomeOrganization:** die Domain der Heimorganisation der Person, etwa ethz.ch. Damit lassen Sie nur Angehörige bestimmter Hochschulen hinein.
- **eduPersonAffiliation:** die Art der Zugehörigkeit, etwa student, staff oder faculty. Damit lassen Sie zum Beispiel nur Personen mit dem Wert student hinein.

Im Feld "Shibboleth-Attribut 1" steht der Name, unter dem die Anbindung Ihrer Installation das Attribut an OpenOlat übergibt. Er kann vom Namen in der Föderation abweichen, etwa "Shib-SwissEP-HomeOrganization" statt swissEduPersonHomeOrganization. Den genauen Namen erfahren Sie von der Stelle, die OpenOlat betreibt.

[Zum Seitenanfang ^](#shibboleth)


## Direktlink für SSO-Zugang [:octicons-tag-16:{ title="ab Release 10.3.4 (OO-1651)" }](https://track.frentix.com/issue/OO-1651) {: #direct_link}

Soll die Anmeldung über Shibboleth direkt von der Website Ihrer Hochschule aus starten, setzen Sie dort den "Direktlink für SSO-Zugang" ein. SSO (Single Sign-on) heisst: Die Person meldet sich einmal bei ihrer Hochschule an und ist damit auch in OpenOlat angemeldet. Die Seite zeigt diese Adresse an. Sie führt ohne Umweg über die Login-Seite von OpenOlat zur Anmeldung über Shibboleth.

[Zum Seitenanfang ^](#shibboleth)


## Shibboleth und Switch edu-ID {: #switch_eduid}

Switch edu-ID ist ein persönliches Konto bei SWITCH, das einer Person auch nach einem Wechsel der Hochschule bleibt. Bei Shibboleth meldet sich die Person dagegen mit dem Konto ihrer Hochschule an. Sie binden Switch edu-ID als Cloud-Login an, nicht über Shibboleth, siehe [Cloud-Login: Switch edu-ID](Login_Cloud_Login.de.md#switch_eduid). Shibboleth und Switch edu-ID können nebeneinander eingeschaltet sein.

[Zum Seitenanfang ^](#shibboleth)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Lebenszyklen: Übersicht >](Life_cycles_-_Administration/index.de.md)<br>
[Kontoeinstellungen verwalten >](../usermanagement/Configure_User.de.md)<br>
[Cloud-Login >](Login_Cloud_Login.de.md)

**Weiterführend**<br>
[Login: Übersicht >](Login/index.de.md)<br>
[LDAP >](Login_LDAP.de.md)<br>
[Login-Seite >](../../manual_user/login_registration/Login_Page.de.md)

[Zum Seitenanfang ^](#shibboleth)
