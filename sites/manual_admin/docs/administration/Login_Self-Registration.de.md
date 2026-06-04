# Selbstregistration  {: #self-registration}

## Tab Konfiguration {: #tab_configuration}

![login_self_registration_tab1_v1_de.png](assets/login_self_registration_tab1_v1_de.png){ class="shadow lightbox" }


### Abschnitt "Konfiguration"

Mit dem Toggle-Button wird grundsätzlich erlaubt, ob eine Selbstregistration möglich ist.


### Abschnitt "Selbstregistrierung"

**Auf Loginseite anzeigen**<br>
Die Möglichkeit zur Selbstregistration kann schon auf der Loginseite angeboten werden.
Wird die Option dort nicht angezeigt, kann die Selbstregistration z.B. erfolgen, nachdem im Katalog ein entsprechendes Angebot gewählt wurde.


**Schritt Kontoüberprüfung**<br>
In einem optionalen Schritt kann ab :octicons-tag-24: Release 20 geprüft werden, ob Benutzer:innen bereits ein OpenOlat-Konto besitzen. Benutzer:innen, die bereits ein Konto haben, sollen ihr altes Konto weiter benutzen können, wenn sie es möchten. 
Wird durch Administrator:innen die Prüfoption ausgewählt, werden die bereits bekannten Benutzer:innen nach einem bestehenden Konto gefragt und es wird ein Support-Formular zur Verfügung gestellt.

**Schritt E-Mail Validierung**<br>
Bei der Selbstregistration eingegebene E-Mail-Adressen werden auf ihre Gültigkeit überprüft.<br>
Variante: Die Validierung kann auch durch das Organisationsmodul gesteuert werden.


### Abschnitt "Einschränkung auf Domäne"

Die Festlegung der Domänen wird im Organisationsmodul vorgenommen. <br>
Siehe [Modul Organisationen >](../administration/Modules_Organisations.de.md)


### Abschnitt "Gültigkeitsdauer der Logindaten"

Die Gültigkeitsdauer der Logindaten kann separat für das GUI und die REST-API angegeben werden.


[Zum Seitenanfang ^](#self-registration)

---


## Tab Kontoeinstellungen {: #tab_account_settings}

![login_self_registration_tab2_v1_de.png](assets/login_self_registration_tab2_v1_de.png){ class="shadow lightbox" }


### Abschnitt "Konfiguration Konto"

Bei neuen Konten werden die hier eingetragenen Konfigurationen übernommen:

**Heimatorganisation der Benutzer:innen:**<br>
Neue Benutzer:innen werden automatisch der hier angegebenen Organisation zugeordnet. Weitere Zuordnungen können später in der Benutzerverwaltung vorgenommen werden.

**Kontostatus:**<br>
**Aktiv:** Nach der Selbstregistration steht OpenOlat sofort zur Verfügung.<br>
**Ausstehend:** Ein:e Administrator:in oder ein:e Benutzerverwalter:in muss das Konto nach der Selbtregistration noch freischalten.<br>
**Ausstehend, wenn eines der folgenden Kontoattribute zutrifft:**  Wenn eine der Bedingungen vorliegt, wird das Konto mit Status "Ausstehend" angelegt. Trifft keine der Bedingungen zu, wird der Kontostatus "aktiv" vergeben.

**E-Mail für ausstehende Konten:**<br>
Für das Prüfen und Freischalten von Konten mit Status "ausstehend" kann die Mailadresse einer verantwortlichen Person angegeben werden (sinnvollerweise Administrator:innen oder Benutzerverwalter:innen).

**In Kurse buchen**<br>
Ist die Option aktiviert, können die Personen, die sich selbst registrieren, automatisch zu Mitgliedern der angegebenen Kurse gemacht werden. 

**Kursliste:**<br>
Die Möglichkeit zur Angabe mehrerer Kurse bezieht sich auf die Option "In Kurse buchen".

**Kontoablauf in Tagen**<br>
Die hier gemachte Angabe entspricht der Angabe in der Benutzerverwaltung. Die Angabe wird bei Selbstregistration dort übernommen.


### Abschnitt "Kontoattribute"

Nach der Selbstregistrierung kann einem Kontoattribut optional ein Standardwert zugewiesen werden. Dies kann genutzt werden um selbstregistrierte Benutzer:innen einfach zu erkennen und dadurch z.B. von LDAP-Benutzer:innen zu unterscheiden.


[Zum Seitenanfang ^](#self-registration)

---


## Tab Externe Einbindung {: #tab_configuration}

![login_self_registration_tab3_v1_de.png](assets/login_self_registration_tab3_v1_de.png){ class="shadow lightbox" }

### Abschnitt "Externe Einbindung"

**Code für die Registrierung**<br>

Der Aufruf zur Selbstregistration kann mit der hier angegebenen URL direkt angesteuert werden.

Verwendungsbeispiel:<br>
Wenn auf der Startseite die Option "Selbtregistration" nicht anzeigezeigt werden soll, können potenzielle Benutzer:innen mit der hier angegebenen URL zur Selbstregistration eingeladen werden.

[Zum Seitenanfang ^](#self-registration)

