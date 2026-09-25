# Modul Media Center {: #module_media_center}


Administrator:innen konfigurieren das Media Center in der System-Administration unter:<br>
`Administration > Module > Media Center`

![Alle Einstellungen des Moduls Media Center auf einer Seite, geöffnet über den markierten Eintrag Media Center im Menü Module der System-Administration](assets/modules_media_center_admin_v2_de.png){ class="shadow lightbox" }

Die Quota (Speicherplatz) des Media Centers legt dieses Modul nicht selbst fest. Die Quota stellen Sie in der System-Administration ein, unter:<br>
`Administration > Core Konfiguration > Dateien und Ordner > Tab "Quotas"`

Siehe auch [Dateien und Ordner](Files_and_Folders.de.md#files_and_folders_quotas).<br>
[Zum Seitenanfang ^](#module_media_center)

---


## Lizenzen {: #licences}

Wer sicherstellen will, dass jedes neue Medium im Media Center eine Lizenzangabe trägt, macht die Lizenz hier zum Pflichtfeld. Dazu aktivieren Sie die Checkbox "Lizenzprüfung bei neuen Medien erzwingen". Sie wirkt, wenn in der System-Administration unter `Administration > Core Konfiguration > Lizenzen` bei "Lizenzen aktivieren in" das Media Center ausgewählt ist.

[Mehr zur Verwendung von Lizenzen >](Licenses.de.md)<br>
[Zum Seitenanfang ^](#module_media_center)

---


## Taxonomie {: #taxonomy}

Alle Inhalte des Media Centers können einer Taxonomie zugeordnet werden (Metadaten). Da OpenOlat mehrere Taxonomien nebeneinander verwalten kann, legen Administrator:innen unter "Verknüpfte Taxonomien" fest, welche Taxonomien im Media Center verwendet werden.

Weitere Informationen finden Sie im Kapitel [Taxonomie](Modules_Taxonomy.de.md).

[Zum Seitenanfang ^](#module_media_center)

---


## Freigaben [:octicons-tag-16:{ title="ab Release 18.1 (OO-7274)" }](https://track.frentix.com/issue/OO-7274) {: #shares}

Werden Inhalte im Media Center abgelegt, können sie zur Verwendung durch andere freigegeben werden. Welche Freigabemöglichkeiten den Autor:innen und anderen Rollen zur Verfügung stehen, legen Administrator:innen im Abschnitt "Freigaben" fest.

Für "Mit Benutzer:in", "Mit Gruppe" und "Mit Kurs" wählen Sie jeweils "Alle" oder "Rollenspezifisch". Mit "Alle" dürfen alle Benutzer:innen auf diesem Weg freigeben, auch ohne zusätzliche Rolle. Mit "Rollenspezifisch" wählen Sie die Rollen Autor:in, Lernressourcenverwalter:in und Administrator:in einzeln aus. "Mit Organisation" steht nur den Rollen Lernressourcenverwalter:in und Administrator:in offen, die Sie dort einzeln auswählen.


| Meine Rolle           | Wenn "Mit Benutzer:in"<br>durch Admins erlaubt wurde | Wenn "Mit Kurs"<br>durch Admins erlaubt wurde | Wenn "Mit Gruppe"<br> durch Admins erlaubt wurde | Wenn "Mit Organisation"<br> durch Admins erlaubt wurde |
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
[Media Center: Konzept >](../../manual_user/basic_concepts/Media_Center_Concept.de.md)<br>
[Persönliche Werkzeuge: Das Media Center >](../../manual_user/personal_menu/Media_Center.de.md)<br>
[Konto konfigurieren >](../usermanagement/Configure_User.de.md)

[Zum Seitenanfang ^](#module_media_center)
