# Modul Organisationen {: #organisations}


Das Modul "Organisationen" ist optional in OpenOlat verfügbar. Es wird in der System-Administration unter `Administration > Module > Organisationen` aktiviert.

!!! tip "Aktivierung"

    Kunden von frentix kontaktieren für die Aktivierung bitte: [contact@frentix.com](mailto:contact@frentix.com). Nach der Aktivierung können diverse zusätzliche Einstellungen für die systemweite Konfiguration vorgenommen werden. Bei Systemen mit dem fx-Release werden diese Anpassung durch frentix vorgenommen.

    **Nicht Hosting-Kunde von frentix?** Fragen Sie Ihren Systembetreiber!



## Tab Konfiguration {: #tab_configuration}

![Aktivierung des Moduls Organisationen, der E-Mail-Domänen-Zuordnung und der rechtlichen Dokumente im Tab Konfiguration](assets/organisations_tab_config_v2_de.png){ class="shadow lightbox" }

Im Tab Konfiguration erfolgt

* die Aktivierung des Moduls Organisationsstrukturen
* die Aktivierung der E-Mail-Domänen-Zuordnung (nur aktivierbar bei aktiviertem Modul Organisationen)
* die Aktivierung des Ordners für rechtliche Dokumente
* den Abschnitt "Status", in dem Informationen für Administrator:innen angezeigt werden

Im Modul "Organisationen" kann die Unternehmensstruktur abgebildet werden. Anschliessend können Rollen, Rechte und Sichtbarkeit von Kursen und Inhalten von der Zugehörigkeit zu einer bestimmten Organisationseinheit abhängig gemacht werden.

Auch die Möglichkeit zur Selbstregistration von Kursteilnehmer:innen kann von der Zugehörigkeit zu einer bestimmten Organisationseinheit abhängig gemacht werden. Diese Einschränkung wird vorgenommen, indem die Mail-Adresse neuer Benutzer:innen mit den hinterlegten E-Mail-Domänen abgeglichen und automatisch einer bestimmten Organisationseinheit zugeordnet wird.


[Zum Seitenanfang ^](#organisations)

---

## Tab Organisationsstruktur {: #tab_structure}

Im Tab "Organisationsstruktur" finden sich die bereits erstellten Organisationen mit ihren Unterorganisationen als Baumstruktur dargestellt.

### Neue Organisationen erstellen und bearbeiten {: #create_and_edit}

![Baumstruktur der Organisationen mit ihren Unterorganisationen im Tab Organisationsstruktur](assets/organisations_tab_structure_v2_de.png){ class="shadow lightbox" }

Neue Organisationen können über den Button "Neue Organisation erstellen" rechts oben oder bei bestehenden Organisationen durch Klick auf die 3 Punkte und "Unterorganisation erstellen" hinzugefügt werden.

Eine bestehende Organisation verschieben Sie mit Klick auf die 3 Punkte und "Organisation verschieben". Im Fenster wählen Sie die Organisation, unter der sie künftig liegen soll, und bestätigen mit "Organisation verschieben". Fehlt "Organisation verschieben" unter den 3 Punkten, sperrt ein externes System das Verschieben. Ihre Unterorganisationen ziehen mit. Das Fenster bietet nur Organisationen an, unter denen der [Organisationstyp](#tab_types) der verschobenen Organisation erlaubt ist. Rollen, die die Organisation von ihrer bisherigen übergeordneten Organisation geerbt hat, entfallen; die vererbten Rollen der neuen übergeordneten Organisation kommen hinzu. Die Rechte, die Sie in der verschobenen Organisation für [Linienvorgesetzte](#edit_linemanager) und [Ausbildungsverantwortliche](#edit_education_manager) gesetzt haben, setzt OpenOlat beim Verschieben zurück. Notieren Sie sie vorher und setzen Sie sie nach dem Verschieben neu.

!!! info "Nach oben verschieben Sie in zwei Schritten"

    Eine Organisation lässt sich nicht direkt in eine Organisation verschieben, die in der Baumstruktur über ihr liegt. OpenOlat meldet dann "Eine Organisation kann nicht in eine ihr über- oder untergeordnete Organisation verschoben werden." Verschieben Sie die Organisation zuerst in eine Organisation, die weder über ihr noch unter der Zielorganisation liegt, und von dort in die Zielorganisation. frentix-Kund:innen können diesen Zwischenschritt nicht selbst ausführen und wenden sich an den frentix Support: [support@frentix.com](mailto:support@frentix.com)

Wird in der Baumstruktur eine Organisation ausgewählt, können ihre Metadaten und weitere Zuordnungen angepasst oder ergänzt werden.

![Ordner für rechtliche Dokumente im Tab "Rechtliche Dokumente" einer Organisation](assets/organisations_tab_structure_legal_documents_v1_de.png){ class="shadow lightbox" }

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Rechtliche Dokumente"`<br>
Ist der Ordner unter `Administration > Module > Organisationen > Tab "Konfiguration"` aktiviert worden, wird dieses Tab für Administrator:innen und andere administrative Rollen angezeigt. Administrator:innen können darin Dokumente zu organisationsspezifischen Belangen ablegen. Andere administrative Rollen haben nur Lesezugriff. [:octicons-tag-16:{ title="ab Release 20.0 (OO-8233)" }](https://track.frentix.com/issue/OO-8233){:target="_blank"}



### Metadata {: #edit_metadata}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Metadata"`
![Bezeichnung und Name als Pflichtfelder, dazu Organisationstyp, Standort und Beschreibung. Tab Metadata einer Organisation](assets/organisations_edit_tab_metadata_v1_de.png){ class="shadow lightbox" }

Im Tab "Metadata" pflegen Sie die Angaben, an denen eine Organisation in OpenOlat erkannt wird. Neben der Bezeichnung und dem Namen können ein Standort und eine Beschreibung eingetragen werden. Die ID und die Externe ID zeigt OpenOlat nur an, sie lassen sich hier nicht ändern.
Ausserdem erfolgt hier die Zuordnung des Organisationstyps (wie im Tab "Organisationstypen" definiert).
Wird bei der Erstellung jede Organisation mit einem entsprechenden Organisationstyp verknüpft, kann so eine hierarchische Struktur aufgebaut werden. Eine Organisation, die gleichzeitig mehreren übergeordneten Organisationen angehört, lässt sich nicht abbilden.

Beim ersten Start legt OpenOlat die Standardorganisation an. Sie trägt den Namen "OpenOLAT" und die Bezeichnung "default-org". Administrator:innen können den Namen im Tab "Metadata" frei ändern, etwa in den Namen der eigenen Organisation. Die Bezeichnung ist gesperrt, weil OpenOlat die Standardorganisation an ihr erkennt. Kurse, Lernressourcen und Rollen bleiben beim Umbenennen unverändert zugeordnet. Löschen oder verschieben lässt sich die Standardorganisation nicht.

!!! note "Hinweis"

    Gleicht Ihr OpenOlat die Organisationen mit LDAP-Gruppen ab, ordnet es jeder LDAP-Gruppe die Organisation zu, deren Bezeichnung, Name oder Externe ID dem Namen der Gruppe entspricht. Gross- und Kleinschreibung spielen dabei keine Rolle. Wählen Sie für die Standardorganisation deshalb keinen Namen, den auch eine LDAP-Gruppe trägt. Sonst verwaltet LDAP die Mitglieder der Standardorganisation.



### Kontenverwaltung {: #edit_account_managment}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Kontenverwaltung"`
![Rollenauswahl beim Hinzufügen eines Kontos im Tab Kontenverwaltung](assets/organisations_edit_tab_account_management_v1_de.png){ class="shadow lightbox" }

Im Tab "Kontenverwaltung" erhält man eine Liste mit den aktuell dieser Organisationseinheit zugeordneten Benutzer:innen. Ebenso können bestehende Benutzer:innen wieder entfernt werden.

Mit dem Button "Konto hinzufügen" können weitere Benutzer:innen einer bestimmten Rolle hinzugefügt werden. Hierfür wird aus den aufgelisteten Rollen die gewünschte ausgewählt. Im anschliessenden Dialog kann nach Benutzer:innen gesucht werden.  Entsprechend der Auswahl können sie hinzugefügt werden. Auch das Hinzufügen von mehreren Benutzer:innen ist möglich.

Jeder Stufe der Organisation können Mitglieder verschiedenster Rollen zugeordnet werden. 

Die **Rollen-Zuordnung** ist möglich

  * auf einer spezifischen Organisation
  * auf einer spezifischen Organisation und allen dieser Organisation untergeordneten Organisationsstrukturen



### Lernressourcen {: #edit_learning_resources}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Lernressourcen"`
![Button "Kurse hinzufügen" über der noch leeren Liste der zugeordneten Kurse. Tab Lernressourcen einer Organisation](assets/organisations_edit_tab_learning_resources_v1_de.png){ class="shadow lightbox" }

Im Tab "Lernressourcen" sehen Sie, welche Kurse der Organisation direkt zugeordnet sind, und passen diese Zuordnung an. Über "Kurse hinzufügen" kann in einem Dialog nach weiteren eigenen und verfügbaren Kursen gesucht werden, um diese der Organisation zuzuordnen. Um Kurse wieder zu entfernen, markieren Sie die Zeilen in der Liste und klicken auf "Entfernen". OpenOlat fragt im Dialog "Lernressourcen entfernen" nach, bevor es die Zuordnung aufhebt.

"Kurse hinzufügen" findet nur Kurse. Tests, Videos und andere Lernressourcen ordnen Sie einer Organisation in der Administrativen Freigabe der Lernressource zu, beschrieben unter [Kurseinstellungen - Tab Freigabe](../../manual_user/learningresources/Course_Settings_Share.de.md#section_share). Für mehrere Lernressourcen gleichzeitig gibt es die [Sammelaktion im Autorenbereich](../../manual_user/area_modules/Authoring_BulkActions.de.md#bulk_administrative_access).

!!! warning "Achtung"

    OpenOlat prüft beim Entfernen nicht, ob der Kurs danach noch einer anderen Organisation zugeordnet ist. Wollen Sie einen Kurs in eine andere Organisation verschieben, klicken Sie deshalb zuerst in der neuen Organisation auf "Kurse hinzufügen". Erst danach entfernen Sie den Kurs in der bisherigen Organisation mit "Entfernen".

Die **Zuordnung von Bildungsprodukten** erfolgt im Course Planner in der jeweiligen Durchführung.


### Linienvorgesetzte [:octicons-tag-16:{ title="ab Release 15.3 (OO-4915)" }](https://track.frentix.com/issue/OO-4915){:target="_blank"} {: #edit_linemanager}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Linienvorgesetzte"`
![Rechte-Checkboxen für die Rolle Linienvorgesetzte:r im Tab Linienvorgesetzte:r](assets/organisations_edit_tab_line_management_v1_de.png){ class="shadow lightbox" }

Die Rechte, die Linienvorgesetzten zugeteilt werden, können für jede Organisationseinheit separat definiert werden. 


### Ausbildungsverantwortliche [:octicons-tag-16:{ title="ab Release 20.0 (OO-7839)" }](https://track.frentix.com/issue/OO-7839){:target="_blank"} {: #edit_education_manager}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Ausbildungsverantwortliche"`
![Rechte-Checkboxen für die Rolle Ausbildungsverantwortliche im Tab Ausbildungsverantwortliche](assets/organisations_edit_tab_education_manager_v1_de.png){ class="shadow lightbox" }

Die Rechte, die Ausbildungsverantwortlichen zugeteilt werden, können für jede Organisationseinheit separat definiert werden. 


### Rechnungsadressen [:octicons-tag-16:{ title="ab Release 20.0 (OO-8212)" }](https://track.frentix.com/issue/OO-8212){:target="_blank"} {: #edit_billing_adresses}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Rechnungsadressen"`
![Liste der Rechnungsadressen mit Button "Erstellen" im Tab Rechnungsadressen](assets/organisations_edit_tab_billing_addresses_v1_de.png){ class="shadow lightbox" }

Für die Kurs- und Seminarverwaltung können hier Rechnungsadressen hinterlegt werden.


### E-Mail-Domänen-Zuordnung {: #edit_mail_domain}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "E-Mail-Domänen-Zuordnung"`
![Liste der E-Mail-Domänen-Zuordnungen im gleichnamigen Tab der Organisation](assets/organisations_edit_tab_email_domain_v1_de.png){ class="shadow lightbox" }

Zu jeder Organisation kann eine E-Mail-Domäne angegeben werden, anhand derer die Zugehörigkeit von Benutzer:innen zu dieser Orgnisationseinheit geprüft werden kann. Die ist dann von Bedeutung, wenn sich Benutzer:innen selbst für Kurse anmelden können, die Kurse jedoch nur für eine bestimmte Organisationseinheit verfügbar sein soll. 

[Zum Seitenanfang ^](#organisations)

---

## Tab Organisationstypen {: #tab_types}

![Liste der Organisationstypen mit Bezeichnung und Name im Tab Organisationstypen](assets/organisations_tab_types_v1_de.png){ class="shadow lightbox" }

Die Organisationstypen definieren, welche Elemente eine Organisationsstruktur enthalten kann und geben diesen Elementen eine nähere Bedeutung. Die Typen können dabei auch eine hierarchische Struktur abbilden, dies ist allerdings nicht zwingend. Ein Beispiel für Organisationstypen ist `Firma --> Bereich --> Abteilung`.

Über "Organisationstyp erstellen" können weitere Typen angelegt werden. Neben der Bezeichnung (Kennzeichen) und dem Namen kann eine Beschreibung angegeben werden. Es ist an dieser Stelle möglich, per CSS Klasse ein nur für diesen Organisationstyp geltendes Layout zu hinterlegen. Zudem können dem neuem Organisationstyp bereits bestehende Typen untergeordnet werden.


[Zum Seitenanfang ^](#organisations)

---

## Tab E-Mail-Domänen-Zuordnungen [:octicons-tag-16:{ title="ab Release 20.0 (OO-8178)" }](https://track.frentix.com/issue/OO-8178){:target="_blank"} {: #tab_mail_domain_assignment}

!!! info "Sichtbarkeit"

    Dieser Tab wird nur angezeigt, wenn die E-Mail-Domänen-Zuordnung im Tab "Konfiguration" aktiviert wurde.

![Liste der E-Mail-Domänen je Organisation im Tab E-Mail-Domänen-Zuordnungen](assets/organisations_tab_mail_domains_v1_de.png){ class="shadow lightbox" }

Existieren Organisationseinheiten, kann die Selbstregistration auf bestimmte E-Mail-Domänen eingeschränkt werden. Neue Benutzer:innen werden dann basierend auf ihrer E-Mail-Domäne automatisch einer Organisationseinheit zugeordnet und nur für Inhalte/Kurse dieser Organisationseinheit zur Selbstregistration zugelassen.

[Zum Seitenanfang ^](#organisations)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kurseinstellungen - Tab Freigabe >](../../manual_user/learningresources/Course_Settings_Share.de.md)<br>
[Autorenbereich - Sammelaktionen >](../../manual_user/area_modules/Authoring_BulkActions.de.md)

**Weiterführend**<br>
[Rollen zuweisen >](../usermanagement/Assign_roles.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../../manual_user/basic_concepts/Roles.de.md)<br>
[Selbstregistration >](Login_Self-Registration.de.md)

[Zum Seitenanfang ^](#organisations)