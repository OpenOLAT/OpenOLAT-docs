# Modul Organisationen {: #organisations}


Das Modul "Organisationen" ist optional in OpenOlat verfügbar. Es wird in der System-Administration unter `Administration > Module > Organisationen` aktiviert.

!!! tip "Aktivierung"

    Kunden von frentix kontaktieren für die Aktivierung bitte: [contact@frentix.com](mailto:contact@frentix.com). Nach der Aktivierung können diverse zusätzliche Einstellungen für die systemweite Konfiguration vorgenommen werden. Bei Systemen mit dem fx-Release werden diese Anpassungen durch frentix vorgenommen.

    **Nicht Hosting-Kunde von frentix?** Fragen Sie Ihren Systembetreiber!



## Tab Konfiguration {: #tab_configuration}

![Aktivierung des Moduls Organisationen, der E-Mail-Domänen-Zuordnung und der rechtlichen Dokumente](assets/organisations_tab_config_v2_de.png){ class="shadow lightbox" title="Tab Konfiguration im Modul Organisationen" }

Im Tab Konfiguration schalten Sie das Modul und seine Zusatzfunktionen ein, die Ihre Organisation braucht. Der Tab enthält

* die Aktivierung des Moduls Organisationsstrukturen
* die Aktivierung der E-Mail-Domänen-Zuordnung (nur aktivierbar bei aktiviertem Modul Organisationen)
* die Aktivierung des Ordners für rechtliche Dokumente
* die Aktivierung der [Debitorennummer](#customer_number) (nur sichtbar bei aktiviertem Modul Organisationen)
* den Abschnitt "Status", in dem Informationen für Administrator:innen angezeigt werden

Im Modul "Organisationen" kann die Unternehmensstruktur abgebildet werden. Anschliessend können Rollen, Rechte und Sichtbarkeit von Kursen und Inhalten von der Zugehörigkeit zu einer bestimmten Organisationseinheit abhängig gemacht werden.

Auch die Möglichkeit zur Selbstregistration von Kursteilnehmer:innen kann von der Zugehörigkeit zu einer bestimmten Organisationseinheit abhängig gemacht werden. Diese Einschränkung wird vorgenommen, indem die Mail-Adresse neuer Benutzer:innen mit den hinterlegten E-Mail-Domänen abgeglichen und automatisch einer bestimmten Organisationseinheit zugeordnet wird.

### Debitorennummer [:octicons-tag-16:{ title="ab Release 21.1 (OO-9736)" }](https://track.frentix.com/issue/OO-9736){:target="_blank"} {: #customer_number}

Stellt Ihre Organisation Kurse in Rechnung, verbindet die Debitorennummer jede Buchung mit der Person oder Organisation, die Ihre Buchhaltung dafür führt. Die Debitorennummer ist die Nummer, unter der die Buchhaltung eine Person oder eine Organisation führt. Steht sie im Export der Buchungsaufträge, ordnet die Buchhaltung jede Buchung ohne Nachschlagen dem richtigen Konto zu.

Sie schalten die Debitorennummer im Tab "Konfiguration" ein, im Abschnitt "Debitorennummer" mit dem Schalter "Debitorennummer aktivieren". Der Abschnitt erscheint erst, wenn das Modul Organisationen eingeschaltet ist. Standardmässig ist der Schalter aus.

Ist der Schalter ein, steht das Feld "Debitorennummer" an drei Orten zur Verfügung:

* im Reiter "Profil" eines Kontos in der Benutzerverwaltung, siehe [Kontoeinstellungen verwalten](../usermanagement/Configure_User.de.md#profile)
* im Tab [Metadaten](#edit_metadata) einer Organisation
* bei einer [Rechnungsadresse](#edit_billing_adresses) einer Organisation

Das Feld ist nie ein Pflichtfeld und nimmt beliebigen Text an. Erfasste Nummern zeigt OpenOlat im Course Planner in der [Mitgliederliste einer Durchführung](../../manual_user/area_modules/Course_Planner_Implementations.de.md#tab_members) und in der Rechnungsadresse eines Buchungsauftrags. Der [Report Buchungsaufträge](../../manual_user/area_modules/Reports_BookingOrders.de.md) enthält drei zusätzliche Spalten: die Debitorennummer der Person, die der Rechnungsadresse und die der Organisation, zu der die Rechnungsadresse gehört.

Schalten Sie die Debitorennummer wieder aus, verschwindet das Feld aus allen Formularen. Die erfassten Nummern bleiben gespeichert, OpenOlat zeigt sie aber nicht mehr an und exportiert sie nicht.


[Zum Seitenanfang ^](#organisations)

---

## Tab Organisationsstruktur {: #tab_structure}

Im Tab "Organisationsstruktur" finden sich die bereits erstellten Organisationen mit ihren Unterorganisationen als Baumstruktur dargestellt.

### Neue Organisationen erstellen und bearbeiten {: #create_and_edit}

![Baumstruktur der Organisationen mit ihren Unterorganisationen](assets/organisations_tab_structure_v2_de.png){ class="shadow lightbox" title="Tab Organisationsstruktur im Modul Organisationen" }

Neue Organisationen können über den Button "Neue Organisation erstellen" rechts oben oder bei bestehenden Organisationen durch Klick auf die 3 Punkte und "Unterorganisation erstellen" hinzugefügt werden. Beide Dialoge enthalten dieselben Felder wie der Tab [Metadaten](#edit_metadata).

Ist die [Debitorennummer](#customer_number) eingeschaltet, blenden Sie in der Liste der Organisationen über "Spalten auswählen" die Spalte "Debitorennummer" ein. Standardmässig ist sie ausgeblendet.

Eine bestehende Organisation verschieben Sie mit Klick auf die 3 Punkte und "Organisation verschieben". Im Fenster wählen Sie die Organisation, unter der sie künftig liegen soll, und bestätigen mit "Organisation verschieben". Ihre Unterorganisationen ziehen mit. Fehlt "Organisation verschieben" unter den 3 Punkten, ist das Verschieben gesperrt: bei der [Standardorganisation](#edit_metadata) immer, bei anderen Organisationen durch ein externes System, das die Organisation verwaltet. Das Fenster bietet nur Organisationen an, unter denen der [Organisationstyp](#tab_types) der verschobenen Organisation erlaubt ist. Rollen, die die Organisation von ihrer bisherigen übergeordneten Organisation geerbt hat, entfallen; die vererbten Rollen der neuen übergeordneten Organisation kommen hinzu. Die Rechte, die Sie in der verschobenen Organisation für [Linienvorgesetzte](#edit_linemanager) und [Ausbildungsverantwortliche](#edit_education_manager) gesetzt haben, setzt OpenOlat beim Verschieben zurück. Notieren Sie sie vorher und setzen Sie sie nach dem Verschieben neu.

!!! info "Nach oben verschieben Sie in zwei Schritten"

    Eine Organisation lässt sich nicht direkt in eine Organisation verschieben, die in der Baumstruktur über ihr liegt. OpenOlat meldet dann "Eine Organisation kann nicht in eine ihr über- oder untergeordnete Organisation verschoben werden." Verschieben Sie die Organisation zuerst in eine Organisation, die weder über ihr noch unter der Zielorganisation liegt, und von dort in die Zielorganisation. frentix-Kund:innen können diesen Zwischenschritt nicht selbst ausführen und wenden sich an den frentix Support: [support@frentix.com](mailto:support@frentix.com)

Wird in der Baumstruktur eine Organisation ausgewählt, können ihre Metadaten und weitere Zuordnungen angepasst oder ergänzt werden.

![Ordner für rechtliche Dokumente](assets/organisations_tab_structure_legal_documents_v1_de.png){ class="shadow lightbox" title="Tab Rechtliche Dokumente einer Organisation" }

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Rechtliche Dokumente"`<br>
Ist der Ordner unter `Administration > Module > Organisationen > Tab "Konfiguration"` aktiviert worden, wird dieses Tab für Administrator:innen und andere administrative Rollen angezeigt. Administrator:innen können darin Dokumente zu organisationsspezifischen Belangen ablegen. Andere administrative Rollen haben nur Lesezugriff. [:octicons-tag-16:{ title="ab Release 20.0 (OO-8233)" }](https://track.frentix.com/issue/OO-8233){:target="_blank"}



### Metadaten {: #edit_metadata}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Metadaten"`
![Markiertes Feld Bezeichnung mit dem ausgegrauten Wert default-org, darunter das Feld Name mit dem Wert OpenOlat](assets/organisations_edit_tab_metadata_v2_de.png){ class="shadow lightbox" title="Tab Metadaten der Standardorganisation · 2026.10.02" }

Im Tab "Metadaten" pflegen Sie die Angaben, an denen eine Organisation in OpenOlat erkannt wird. Neben der Bezeichnung und dem Namen können ein Standort und eine Beschreibung eingetragen werden. Ist die [Debitorennummer](#customer_number) eingeschaltet, steht zwischen Standort und Beschreibung zusätzlich das Feld "Debitorennummer". Die ID und die Externe ID zeigt OpenOlat nur an, sie lassen sich hier nicht ändern. Ausserdem erfolgt hier die Zuordnung des Organisationstyps (wie im Tab "Organisationstypen" definiert). Wird bei der Erstellung jede Organisation mit einem entsprechenden Organisationstyp verknüpft, kann so eine hierarchische Struktur aufgebaut werden. Eine Organisation, die gleichzeitig mehreren übergeordneten Organisationen angehört, lässt sich nicht abbilden.

Bei Organisationen, die Administrator:innen selbst erstellt haben, lassen sich Bezeichnung und Name jederzeit ändern. Gesperrt sind die beiden Felder nur, wenn ein externes System die Organisation verwaltet. Ein solches System kann über die [REST API](REST_API.de.md) auch die Debitorennummer einer Organisation setzen und das Feld dabei sperren.

Anders bei der Standardorganisation, die das Bild zeigt: Ihre Bezeichnung ist immer gesperrt, ihr Name nicht. OpenOlat legt die Standardorganisation beim ersten Start mit dem Namen "OpenOLAT" und der Bezeichnung "default-org" an und sperrt dabei das Feld "Bezeichnung". OpenOlat erkennt die Standardorganisation an dieser Bezeichnung, deshalb bleibt das Feld auch später gesperrt. Den Namen können Administrator:innen jederzeit im Tab "Metadaten" ändern, etwa in den Namen der eigenen Organisation. Im Bild trägt sie den geänderten Namen "OpenOlat". Kurse, Lernressourcen und Rollen bleiben beim Umbenennen unverändert zugeordnet. Verschieben oder löschen lässt sich die Standardorganisation nicht.

!!! note "Hinweis"

    Gleicht Ihr OpenOlat die Organisationen mit LDAP-Gruppen ab, ordnet es jeder LDAP-Gruppe die Organisation zu, deren Bezeichnung, Name oder Externe ID dem Namen der Gruppe entspricht. Gross- und Kleinschreibung spielen dabei keine Rolle. Wählen Sie für die Standardorganisation deshalb keinen Namen, den auch eine LDAP-Gruppe trägt. Sonst verwaltet LDAP die Mitglieder der Standardorganisation.



### Kontenverwaltung {: #edit_account_managment}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Kontenverwaltung"`
![Rollenauswahl beim Hinzufügen eines Kontos](assets/organisations_edit_tab_account_management_v1_de.png){ class="shadow lightbox" title="Tab Kontenverwaltung einer Organisation" }

Im Tab "Kontenverwaltung" erhält man eine Liste mit den aktuell dieser Organisationseinheit zugeordneten Benutzer:innen. Ebenso können bestehende Benutzer:innen wieder entfernt werden.

Mit dem Button "Konto hinzufügen" können weitere Benutzer:innen einer bestimmten Rolle hinzugefügt werden. Hierfür wird aus den aufgelisteten Rollen die gewünschte ausgewählt. Im anschliessenden Dialog kann nach Benutzer:innen gesucht werden.  Entsprechend der Auswahl können sie hinzugefügt werden. Auch das Hinzufügen von mehreren Benutzer:innen ist möglich.

Jeder Stufe der Organisation können Mitglieder verschiedenster Rollen zugeordnet werden. 

Die **Rollen-Zuordnung** ist möglich

  * auf einer spezifischen Organisation
  * auf einer spezifischen Organisation und allen dieser Organisation untergeordneten Organisationsstrukturen



### Lernressourcen {: #edit_learning_resources}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Lernressourcen"`
![Button "Kurse hinzufügen" über der noch leeren Liste der zugeordneten Kurse](assets/organisations_edit_tab_learning_resources_v1_de.png){ class="shadow lightbox" title="Tab Lernressourcen einer Organisation" }

Im Tab "Lernressourcen" sehen Sie, welche Kurse der Organisation direkt zugeordnet sind, und passen diese Zuordnung an. Über "Kurse hinzufügen" kann in einem Dialog nach weiteren eigenen und verfügbaren Kursen gesucht werden, um diese der Organisation zuzuordnen. Um Kurse wieder zu entfernen, markieren Sie die Zeilen in der Liste und klicken auf "Entfernen". OpenOlat fragt im Dialog "Lernressourcen entfernen" nach, bevor es die Zuordnung aufhebt.

"Kurse hinzufügen" findet nur Kurse. Tests, Videos und andere Lernressourcen ordnen Sie einer Organisation in der Administrativen Freigabe der Lernressource zu, beschrieben unter [Kurseinstellungen - Tab Freigabe](../../manual_user/learningresources/Course_Settings_Share.de.md#section_share). Für mehrere Lernressourcen gleichzeitig gibt es die [Sammelaktion im Autorenbereich](../../manual_user/area_modules/Authoring_BulkActions.de.md#bulk_administrative_access).

!!! warning "Achtung"

    OpenOlat prüft beim Entfernen nicht, ob der Kurs danach noch einer anderen Organisation zugeordnet ist. Wollen Sie einen Kurs in eine andere Organisation verschieben, klicken Sie deshalb zuerst in der neuen Organisation auf "Kurse hinzufügen". Erst danach entfernen Sie den Kurs in der bisherigen Organisation mit "Entfernen".

Die **Zuordnung von Bildungsprodukten** erfolgt im Course Planner in der jeweiligen Durchführung.


### Linienvorgesetzte [:octicons-tag-16:{ title="ab Release 15.3 (OO-4915)" }](https://track.frentix.com/issue/OO-4915){:target="_blank"} {: #edit_linemanager}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Linienvorgesetzte"`
![Rechte-Checkboxen für die Rolle Linienvorgesetzte:r](assets/organisations_edit_tab_line_management_v1_de.png){ class="shadow lightbox" title="Tab Linienvorgesetzte:r einer Organisation" }

Die Rechte, die Linienvorgesetzten zugeteilt werden, können für jede Organisationseinheit separat definiert werden. 


### Ausbildungsverantwortliche [:octicons-tag-16:{ title="ab Release 20.0 (OO-7839)" }](https://track.frentix.com/issue/OO-7839){:target="_blank"} {: #edit_education_manager}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Ausbildungsverantwortliche"`
![Rechte-Checkboxen für die Rolle Ausbildungsverantwortliche](assets/organisations_edit_tab_education_manager_v1_de.png){ class="shadow lightbox" title="Tab Ausbildungsverantwortliche einer Organisation" }

Die Rechte, die Ausbildungsverantwortlichen zugeteilt werden, können für jede Organisationseinheit separat definiert werden. 


### Rechnungsadressen [:octicons-tag-16:{ title="ab Release 20.0 (OO-8212)" }](https://track.frentix.com/issue/OO-8212){:target="_blank"} {: #edit_billing_adresses}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "Rechnungsadressen"`
![Noch leere Liste der Rechnungsadressen, darüber der Button Erstellen](assets/organisations_edit_tab_billing_addresses_v1_de.png){ class="shadow lightbox" title="Tab Rechnungsadressen einer Organisation" }

Bucht eine Person ein Angebot mit Rechnung, wählt sie eine Rechnungsadresse ihrer Organisation aus, statt die Adresse selbst einzugeben. Diese Rechnungsadressen hinterlegen Sie hier je Organisation mit "Erstellen". Zur Auswahl stehen der Person die aktiven Rechnungsadressen der Organisationen, in denen sie Benutzer:in ist.

Der Tab erscheint nur, wenn die Angebotsart "Rechnung" eingeschaltet ist. Sie wählen sie in der System-Administration unter "Verfügbare Angebotsart" aus:<br>
`Administration > Core Konfiguration > Zugangskontrolle`, siehe [Core Konfiguration](Core_functions.de.md).

Eine Rechnungsadresse besteht aus den Feldern "Identifikator", "Name / Firma", "Zusatz / Abteilung", "Adresszeile 1" bis "Adresszeile 4", "Postfach", "Region", "PLZ", "Ort" und "Land". Pflichtfelder sind "Identifikator", "Name / Firma", "Adresszeile 1", "Ort" und "Land".

Ist die [Debitorennummer](#customer_number) eingeschaltet, hat eine Rechnungsadresse einer Organisation zusätzlich das Feld "Debitorennummer". Persönliche Rechnungsadressen haben dieses Feld nicht, ebenso wenig eine Adresse, die erst beim Buchen über "Andere Organisationsadresse" eingegeben wird. Ist eine Nummer erfasst, steht sie als erste Zeile der Rechnungsadresse, überall wo OpenOlat die Adresse anzeigt: in der Detailansicht eines Buchungsauftrags im Course Planner, bei der Auswahl der Rechnungsadresse während der Buchung mit Rechnung und in den [eigenen Buchungsaufträgen](../../manual_user/personal_menu/Bookings.de.md) der Teilnehmer:innen.


### E-Mail-Domänen-Zuordnung {: #edit_mail_domain}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > "Name der Organisation" > Tab "E-Mail-Domänen-Zuordnung"`
![Liste der E-Mail-Domänen-Zuordnungen](assets/organisations_edit_tab_email_domain_v1_de.png){ class="shadow lightbox" title="Tab E-Mail-Domänen-Zuordnung einer Organisation" }

Zu jeder Organisation kann eine E-Mail-Domäne angegeben werden, anhand derer die Zugehörigkeit von Benutzer:innen zu dieser Organisationseinheit geprüft werden kann. Dies ist dann von Bedeutung, wenn sich Benutzer:innen selbst für Kurse anmelden können, die Kurse jedoch nur für eine bestimmte Organisationseinheit verfügbar sein sollen.

[Zum Seitenanfang ^](#organisations)

---

## Tab Organisationstypen {: #tab_types}

![Liste der Organisationstypen mit Bezeichnung und Name](assets/organisations_tab_types_v1_de.png){ class="shadow lightbox" title="Tab Organisationstypen im Modul Organisationen" }

Die Organisationstypen definieren, welche Elemente eine Organisationsstruktur enthalten kann und geben diesen Elementen eine nähere Bedeutung. Die Typen können dabei auch eine hierarchische Struktur abbilden, dies ist allerdings nicht zwingend. Ein Beispiel für Organisationstypen ist `Firma --> Bereich --> Abteilung`.

Über "Organisationstyp erstellen" können weitere Typen angelegt werden. Neben der Bezeichnung (Kennzeichen) und dem Namen kann eine Beschreibung angegeben werden. Es ist an dieser Stelle möglich, per CSS Klasse ein nur für diesen Organisationstyp geltendes Layout zu hinterlegen. Zudem können dem neuem Organisationstyp bereits bestehende Typen untergeordnet werden.


[Zum Seitenanfang ^](#organisations)

---

## Tab E-Mail-Domänen-Zuordnungen [:octicons-tag-16:{ title="ab Release 20.0 (OO-8178)" }](https://track.frentix.com/issue/OO-8178){:target="_blank"} {: #tab_mail_domain_assignment}

!!! info "Sichtbarkeit"

    Dieser Tab wird nur angezeigt, wenn die E-Mail-Domänen-Zuordnung im Tab "Konfiguration" aktiviert wurde.

![Liste der E-Mail-Domänen je Organisation](assets/organisations_tab_mail_domains_v1_de.png){ class="shadow lightbox" title="Tab E-Mail-Domänen-Zuordnungen im Modul Organisationen" }

Existieren Organisationseinheiten, kann die Selbstregistration auf bestimmte E-Mail-Domänen eingeschränkt werden. Neue Benutzer:innen werden dann basierend auf ihrer E-Mail-Domäne automatisch einer Organisationseinheit zugeordnet und nur für Inhalte/Kurse dieser Organisationseinheit zur Selbstregistration zugelassen.

[Zum Seitenanfang ^](#organisations)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kontoeinstellungen verwalten >](../usermanagement/Configure_User.de.md)<br>
[Course Planner: Durchführungen >](../../manual_user/area_modules/Course_Planner_Implementations.de.md)<br>
[Reports: Buchungsaufträge >](../../manual_user/area_modules/Reports_BookingOrders.de.md)<br>
[REST API >](REST_API.de.md)<br>
[Kurseinstellungen - Tab Freigabe >](../../manual_user/learningresources/Course_Settings_Share.de.md)<br>
[Autorenbereich - Sammelaktionen >](../../manual_user/area_modules/Authoring_BulkActions.de.md)<br>
[Core Konfiguration: Übersicht >](Core_functions.de.md)<br>
[Persönliche Werkzeuge: Buchungsaufträge >](../../manual_user/personal_menu/Bookings.de.md)

**Weiterführend**<br>
[Rollen zuweisen >](../usermanagement/Assign_roles.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../../manual_user/basic_concepts/Roles.de.md)<br>
[Selbstregistration >](Login_Self-Registration.de.md)

[Zum Seitenanfang ^](#organisations)