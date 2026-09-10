# Selbstregistration  {: #self-registration}

## Tab Konfiguration {: #tab_configuration}

![Tab Konfiguration der Selbstregistration mit den Abschnitten Konfiguration, Selbstregistrierung, Einschränkung auf Domäne und Gültigkeitsdauer der Logindaten](assets/login_self_registration_tab1_v1_de.png){ class="shadow lightbox" }


### Abschnitt "Konfiguration"

Mit dem Toggle-Button wird grundsätzlich erlaubt, ob eine Selbstregistration möglich ist.


### Abschnitt "Selbstregistrierung"

#### Auf Loginseite anzeigen {: #show_on_login_page }

Die Möglichkeit zur Selbstregistration kann schon auf der Loginseite angeboten werden.
Wird die Option dort nicht angezeigt, kann die Selbstregistration z.B. erfolgen, nachdem im Katalog ein entsprechendes Angebot gewählt wurde.


#### Schritt Kontoüberprüfung {: #account_check_step }

In einem optionalen Schritt kann ab :octicons-tag-24: Release 20 geprüft werden, ob Benutzer:innen bereits ein OpenOlat-Konto besitzen. Benutzer:innen, die bereits ein Konto haben, sollen ihr altes Konto weiter benutzen können, wenn sie es möchten. 
Wird durch Administrator:innen die Prüfoption ausgewählt, werden die bereits bekannten Benutzer:innen nach einem bestehenden Konto gefragt und es wird ein Support-Formular zur Verfügung gestellt.

#### Schritt E-Mail Validierung {: #email_validation_step }

Bei der Selbstregistration eingegebene E-Mail-Adressen werden auf ihre Gültigkeit überprüft.<br>
Variante: Die Validierung kann auch durch das Organisationsmodul gesteuert werden.


### Abschnitt "Einschränkung auf Domäne"

Die Festlegung der Domänen wird im Organisationsmodul vorgenommen. <br>
Siehe [Modul Organisationen >](../administration/Modules_Organisations.de.md)


### Abschnitt "Gültigkeitsdauer der Logindaten"

Die Gültigkeitsdauer der Logindaten kann separat für das GUI und die REST-API angegeben werden.

Die Gültigkeitsdauer gilt für die Selbstregistrierung und für den Einladungslink zum Setzen der Zugangsdaten, den Administrator:innen in der Benutzerverwaltung im Tab "Passwort" versenden. Nach Ablauf führt der Link ins Leere. Siehe [Benutzer konfigurieren](../usermanagement/Configure_User.de.md). [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9139)" }](https://track.frentix.com/issue/OO-9139)


[Zum Seitenanfang ^](#self-registration)

---


## Tab Kontoeinstellungen {: #tab_account_settings}

![Tab Kontoeinstellungen der Selbstregistration mit den Abschnitten Konfiguration Konto und Kontoattribute](assets/login_self_registration_tab2_v1_de.png){ class="shadow lightbox" }


### Abschnitt "Konfiguration Konto"

Bei neuen Konten werden die hier eingetragenen Konfigurationen übernommen:

#### Heimatorganisation der Benutzer:innen {: #home_organisation }

Neue Benutzer:innen werden automatisch der hier angegebenen Organisation zugeordnet. Weitere Zuordnungen können später in der Benutzerverwaltung vorgenommen werden.

#### Kontostatus {: #account_status }

**Aktiv:** Nach der Selbstregistration steht OpenOlat sofort zur Verfügung.<br>
**Ausstehend:** Ein:e Administrator:in oder ein:e Benutzerverwalter:in muss das Konto nach der Selbstregistration noch freischalten.<br>
**Ausstehend, wenn eines der folgenden Kontoattribute zutrifft:**  Wenn eine der Bedingungen vorliegt, wird das Konto mit Status "Ausstehend" angelegt. Trifft keine der Bedingungen zu, wird der Kontostatus "aktiv" vergeben.

#### E-Mail Benachrichtigung für ausstehende Konten {: #pending_account_notification }

Für das Prüfen und Freischalten von Konten mit Status "ausstehend" kann die Mailadresse einer verantwortlichen Person angegeben werden (sinnvollerweise Administrator:innen oder Benutzerverwalter:innen).

#### In Kurse buchen {: #book_into_courses }

Ist die Option aktiviert, können die Personen, die sich selbst registrieren, automatisch zu Mitgliedern der angegebenen Kurse gemacht werden. 

#### Kursliste {: #course_list }

Die Möglichkeit zur Angabe mehrerer Kurse bezieht sich auf die Option "In Kurse buchen".

#### Kontoablauf in Tagen {: #account_expiration_days }

Die hier gemachte Angabe entspricht der Angabe in der Benutzerverwaltung. Die Angabe wird bei Selbstregistration dort übernommen.


### Abschnitt "Kontoattribute"

Nach der Selbstregistrierung kann einem Kontoattribut optional ein Standardwert zugewiesen werden. Dies kann genutzt werden um selbstregistrierte Benutzer:innen einfach zu erkennen und dadurch z.B. von LDAP-Benutzer:innen zu unterscheiden.

#### Standardwert aktivieren {: #enable_default_value }

Ist die Option aktiviert, wird dem gewählten Kontoattribut automatisch der angegebene Standardwert zugewiesen.

#### Kontoattribut {: #account_attribute }

Kontoattribut, das den Standardwert erhalten soll.

#### Standardwert {: #default_value }

Wert, der dem gewählten Kontoattribut bei der Selbstregistrierung zugewiesen wird.


[Zum Seitenanfang ^](#self-registration)

---


## Tab Externe Einbindung {: #tab_external_integration}

![Tab Externe Einbindung der Selbstregistration mit dem Feld Code für die Registrierung](assets/login_self_registration_tab3_v1_de.png){ class="shadow lightbox" }

### Abschnitt "Externe Einbindung"

#### Code für die Registrierung {: #registration_code }

Der Aufruf zur Selbstregistration kann mit der hier angegebenen URL direkt angesteuert werden.

Verwendungsbeispiel:<br>
Wenn auf der Startseite die Option "Selbstregistration" nicht angezeigt werden soll, können potenzielle Benutzer:innen mit der hier angegebenen URL zur Selbstregistration eingeladen werden.

[Zum Seitenanfang ^](#self-registration)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Organisationen >](Modules_Organisations.de.md)<br>
[Benutzer konfigurieren >](../usermanagement/Configure_User.de.md)

[Zum Seitenanfang ^](#self-registration)

