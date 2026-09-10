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

![Organisationsbaum mit Unterorganisationen im Tab Organisationsstruktur](assets/organisations_tab_structure_v2_de.png){ class="shadow lightbox" }

Neue Organisationen können über den Button "Neue Organisation erstellen" rechts oben oder bei bestehenden Organisationen durch Klick auf die 3 Punkte und "Unterorganisation erstellen" hinzugefügt werden.  Es ist auch möglich, das Element im Organisationsbaum zu verschieben bzw. direkt eine neue Unterorganisation zu erstellen.

Wird in der Baumstruktur ein Organisationselement ausgewählt, können die Metadaten des Organisationselementes und weitere Zuordnungen angepasst oder ergänzt werden.

![Ordner für rechtliche Dokumente im Tab "Rechtliche Dokumente" eines Organisationselements](assets/organisations_tab_structure_legal_documents_v1_de.png){ class="shadow lightbox" }

**Tab Organisationsstruktur > Tab "Rechtliche Dokumente"**<br>
Ist der Ordner unter `Administration > Module > Organisationen > Tab "Konfiguration"` aktiviert worden, wird dieses Tab für Administrator:innen und andere administrative Rollen angezeigt. Administrator:innen können darin Dokumente zu organisationsspezifischen Belangen ablegen. Andere administrative Rollen haben nur Lesezugriff.



### Metadaten {: #edit_metadata}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Metadaten"`
![Metadaten eines Organisationselements: Bezeichnung, Name, Organisationstyp, Standort und Beschreibung](assets/organisations_edit_tab_metadata_v1_de.png){ class="shadow lightbox" }

Neben der Bezeichnung und dem Namen kann eine Beschreibung für das Element eingetragen werden.
Ausserdem erfolgt hier die Zuordnung des Organisationstyps (wie im Tab "Organisationstypen" definiert).
Wird bei der Erstellung jedes Organisationselement mit einem entsprechenden Organisationstyp verknüpft, kann so eine hierarchische Struktur aufgebaut werden. Damit ist die Abbildung von Ablauf- und Aufbauorganisationen möglich, eine Matrix-Organisation kann hingegen nicht dargestellt werden.



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
![Liste der zugeordneten Kurse mit Button "Kurse hinzufügen" im Tab Lernressourcen](assets/organisations_edit_tab_learning_resources_v1_de.png){ class="shadow lightbox" }

Im Tab "Lernressourcen" werden dem Organisationselement direkt zugeordnete Kurse angezeigt. Diese können hier auch wieder entfernt werden. Über "Kurse hinzufügen" kann in einem Dialog nach weiteren eigenen und verfügbaren Kursen gesucht werden, um diese dem Organisationselement zuzuordnen.

Die **Zuordnung von Bildungsprogrammen** erfolgt im Course Planner in der jeweiligen Durchführung.


### Linienvorgesetzte {: #edit_linemanager}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Linienvorgesetzte"`
![Rechte-Checkboxen für die Rolle Linienvorgesetzte:r im Tab Linienvorgesetzte:r](assets/organisations_edit_tab_line_management_v1_de.png){ class="shadow lightbox" }

Die Rechte, die Linienvorgesetzten zugeteilt werden, können für jede Organisationseinheit separat definiert werden. 


### Ausbildungsverantwortliche {: #edit_education_manager}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Ausbildungsverantwortliche"`
![Rechte-Checkboxen für die Rolle Ausbildungsverantwortliche im Tab Ausbildungsverantwortliche](assets/organisations_edit_tab_education_manager_v1_de.png){ class="shadow lightbox" }

Die Rechte, die Ausbildungsverantwortlichen zugeteilt werden, können für jede Organisationseinheit separat definiert werden. 


### Rechnungsadressen {: #edit_billing_adresses}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "Rechnungsadressen"`
![Liste der Rechnungsadressen mit Button "Erstellen" im Tab Rechnungsadressen](assets/organisations_edit_tab_billing_addresses_v1_de.png){ class="shadow lightbox" }

Für die Kurs- und Seminarverwaltung können hier Rechnungsadressen hinterlegt werden.


### E-Mail-Domänen-Zuordnung {: #edit_mail_domain}

`Administration > Module > Organisationen > Tab "Organisationsstruktur" > Tab "E-Mail-Domänen-Zuordnung"`
![Liste der E-Mail-Domänen-Zuordnungen im gleichnamigen Tab des Organisationselements](assets/organisations_edit_tab_email_domain_v1_de.png){ class="shadow lightbox" }

Zu jedem Organisationselement kann eine E-Mail-Domäne angegeben werden, anhand derer die Zugehörigkeit von Benutzer:innen zu dieser Orgnisationseinheit geprüft werden kann. Die ist dann von Bedeutung, wenn sich Benutzer:innen selbst für Kurse anmelden können, die Kurse jedoch nur für eine bestimmte Organisationseinheit verfügbar sein soll. 

[Zum Seitenanfang ^](#organisations)

---

## Tab Organisationstypen {: #tab_types}

![Liste der Organisationstypen mit Bezeichnung und Name im Tab Organisationstypen](assets/organisations_tab_types_v1_de.png){ class="shadow lightbox" }

Die Organisationstypen definieren, welche Elemente eine Organisationsstruktur enthalten kann und geben diesen Elementen eine nähere Bedeutung. Die Typen können dabei auch eine hierarchische Struktur abbilden, dies ist allerdings nicht zwingend. Ein Beispiel für Organisationstypen ist `Firma --> Bereich --> Abteilung`.

Über "Organisationstyp erstellen" können weitere Typen angelegt werden. Neben der Bezeichnung (Kennzeichen) und dem Namen kann eine Beschreibung angegeben werden. Es ist an dieser Stelle möglich, per CSS Klasse ein nur für diesen Organisationstyp geltendes Layout zu hinterlegen. Zudem können dem neuem Organisationstyp bereits bestehende Typen untergeordnet werden.


[Zum Seitenanfang ^](#organisations)

---

## Tab E-Mail-Domänen-Zuordnungen {: #tab_mail_domain_assignment}

!!! info "Sichtbarkeit"

    Dieser Tab wird nur angezeigt, wenn die E-Mail-Domänen-Zuordnung im Tab "Konfiguration" aktiviert wurde.

![Liste der E-Mail-Domänen je Organisation im Tab E-Mail-Domänen-Zuordnungen](assets/organisations_tab_mail_domains_v1_de.png){ class="shadow lightbox" }

Existieren Organisationseinheiten, kann die Selbstregistration auf bestimmte E-Mail-Domänen eingeschränkt werden. Neue Benutzer werden dann basierend auf ihrer E-Mail-Domäne automatisch einer Organisationseinheit zugeordnet und nur für Inhalte/Kurse dieser Organisationseinheit zur Selbstregistration zugelassen.

[Zum Seitenanfang ^](#organisations)