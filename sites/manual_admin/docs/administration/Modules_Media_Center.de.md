# Modul Media Center {: #module_media_center}


Administrator:innen konfigurieren das Media Center in der System-Administration unter:<br>
`Administration > Module > Media Center`

![Konfigurationsseite des Moduls Media Center mit den Abschnitten Lizenzen, Taxonomie und Freigaben](assets/modules_media_center_admin_v2_de.png){ class="shadow lightbox" }

Den Speicherplatz (Quota) des Media Centers legt dieses Modul nicht selbst fest. Die Quota stellen Sie unter `Administration > Core Konfiguration > Dateien und Ordner` ein.

Siehe auch [Dateien und Ordner](Files_and_Folders.de.md#files_and_folders_quotas).<br>
[Zum Seitenanfang ^](#module_media_center)

---


## Lizenzen {: #licences}

Falls unter `Administration > Core Konfiguration > Lizenzen` die Verwendung von Lizenzen für das Media Center vorgesehen ist, kann anschliessend durch diese Checkbox die Lizenzangabe zum Pflichtfeld für alle ins Media Center hochgeladenen oder erstellten Medien gemacht werden.

[Mehr zur Verwendung von Lizenzen >](Licenses.de.md)<br>
[Zum Seitenanfang ^](#module_media_center)

---


## Taxonomie {: #taxonomy}

Alle Inhalte des Media Centers können einer Taxonomie zugeordnet werden (Metadaten). Da OpenOlat mehrere Taxonomien nebeneinander verwalten kann, muss in der Administration bestimmt werden, welche Taxonomien im Media Center verwendet werden sollen. 

Weitere Informationen finden Sie im Kapitel [Taxonomie](Modules_Taxonomy.de.md).

[Zum Seitenanfang ^](#module_media_center)

---


## Freigaben {: #shares}

Werden Inhalte im Media Center abgelegt, können sie zur Verwendung durch andere freigegeben werden. Welche Freigabemöglichkeiten den Autor:innen und anderen Rollen zur Verfügung stehen, legen Administrator:innen im Abschnitt "Freigaben" fest.


| Meine Rolle           | Wenn "Benutzer"<br>durch Admins erlaubt wurde | Wenn "Kurse"<br>durch Admins erlaubt wurde | Wenn "Gruppen"<br> durch Admins erlaubt wurde | Wenn "Organisation"<br> durch Admins erlaubt wurde |
| ----------------- | ---------------------| ------ | ------ | ------------ |
| Ich bin Benutzer:in (ohne zusätzliche Rollen)| Ich kann Mitbenutzer:innen Zugriff geben, wenn sie zu Organisationseinheiten gehören, in denen sie zur Nutzung des Media Centers berechtigt sind. | Ich kann Mitbenutzer:innen in allen Kursen Zugriff geben, wenn sie dort Besitzer:in sind. | Ich kann Mitbenutzer:innen in allen Gruppen Zugriff geben, wenn die Mitbenutzer:innen Gruppenmitglieder sind. | Teilen/Freigabe von Mediendateien ist nicht möglich |
| Ich bin Autor:in | Ich kann Mitbenutzer:innen Zugriff geben, wenn sie zu Organisationseinheiten gehören, in denen sie zur Nutzung des Media Centers berechtigt sind. | Ich kann Mitbenutzer:innen in allen Kursen Zugriff geben, wenn sie dort Besitzer:in sind. | Ich kann Mitbenutzer:innen in allen Gruppen Zugriff geben, wenn die Mitbenutzer:innen Gruppenmitglieder sind. | Teilen/Freigabe von Mediendateien ist nicht möglich |
| Ich bin Lernressourcenverwalter:in | Ich kann Mitbenutzer:innen Zugriff geben, wenn sie zu Organisationseinheiten gehören, in denen sie zur Nutzung des Media Centers berechtigt sind. | Ich kann Mitbenutzer:innen in allen Kursen ihrer Organisationseinheiten Zugriff geben, wenn sie dort berechtigt sind, das Media Center zu nutzen. | Ich kann Mitbenutzer:innen in allen Gruppen Zugriff geben, wenn die Mitbenutzer:innen Gruppenmitglieder sind. | Ich kann Mitbenutzer:innen aus allen Organisationseinheiten Zugriff geben, wenn sie dort berechtigt sind, das Media Center zu nutzen. |
| Ich bin Administrator:in  | Ich kann Mitbenutzer:innen Zugriff geben, wenn sie zu Organisationseinheiten gehören, in denen sie zur Nutzung des Media Centers berechtigt sind.| Ich kann Mitbenutzer:innen in allen Kursen ihrer Organisationseinheiten Zugriff geben, wenn sie dort berechtigt sind, das Media Center zu nutzen. | Ich kann Mitbenutzer:innen in allen Gruppen Zugriff geben. | Ich kann Mitbenutzer:innen aus allen Organisationseinheiten Zugriff geben, wenn sie dort berechtigt sind, das Media Center zu nutzen. |


[Zum Seitenanfang ^](#module_media_center)

---


## Weiterführende Informationen {: #further_information}

[Dateien und Ordner >](Files_and_Folders.de.md)<br>
[Lizenzen >](Licenses.de.md)<br>
[Modul Taxonomie >](Modules_Taxonomy.de.md)<br>
[Media Center Konzept >](../../manual_user/basic_concepts/Media_Center_Concept.de.md)<br>
[Media Center im persönlichen Menü >](../../manual_user/personal_menu/Media_Center.de.md)

[Zum Seitenanfang ^](#module_media_center)
