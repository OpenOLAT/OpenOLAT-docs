# Files and Folders {: #files_and_folders}

![core_config_files_and_folders_v1_en.png](assets/core_config_files_and_folders_v1_en.png){ class="aside-right lightbox"}

Für allgemeine Einstellungen/Konfigurationen betreffend Dateien und Ordnern finden Sie hier die Tabs

* [Übersicht](Files_and_Folders.md##files_and_folders_overview)
* [Konfiguration](#files_and_folders_configuration) für Einstellungen zu
    * [Versionierung](#files_and_folders_configuration_versions)
    * [Lizenzen](#files_and_folders_configuration_license)
    * der [endgütligen Löschung des Papierkorbs](#files_and_folders_configuration_trash)
* [Quotas](#files_and_folders_quotas)<br>zur Festlegung des Speicherplatzes für alle Ordner
* [Grosse Dateien](#files_and_folders_large_files)<br>für das Herausfiltern (und evtl. Löschen) besonders grosser Dateien, die die Quota belasten
* [Papierkorb](#files_and_folders_trash)<br>zur Ansicht des Papierkorb-Inhalts

---

## Tab Overview {: #files_and_folders_overview}

![core_config_files_and_folders_tab_overview_v1_en.png](assets/core_config_files_and_folders_tab_overview_v1_en.png){ class="shadow lightbox" }

In the Overview tab, administrators can get a quick overview of the number and
size of OpenOlat files, versions, deleted files and thumbnails, and can take
actions in this regard.

[zum Seitenanfang ^](#files_and_folders)


## Tab Configuration {: #files_and_folders_configuration}

![core_config_files_and_folders_tab_configuration_v1_en.png](assets/core_config_files_and_folders_tab_configuration_v1_en.png){ class="shadow lightbox" }


### Versions {: #files_and_folders_configuration_versions}

In the **"Versions" section**, the maximum number of versions for a file can be
defined.

If versioning is enabled, files are not overwritten but created as a new
version (also called revision). Older versions of a document can be downloaded
and restored if necessary. If files are deleted, they appear in the list of
deleted files and can be restored. If the versioning function is enabled,
files can also be locked, e.g. if a user is working on a document and wants to
prevent another user from creating a new version in the meantime.

Versioning is available in all folders of the system: personal folders, group
folders, course folders, resource folders and course elements "folders".

**Button "Clean up versions"**<br>
The number of versions can be adjusted. If, for example, 5 versions are now
changed to 2 versions, 3 versions per document are superfluous. However, these
are not deleted directly. If you set the number back to 5 versions, they will
become visible again. However, to delete these versions completely, click on
Clean up versions. Afterwards, the versions can no longer be restored.


### Lizenz {: #files_and_folders_configuration_license}

Im **Abschnitt "Lizenz"** kann gewählt werden, ob bei neu erstellten Dateien eine Lizenzangabe gemacht werden muss. Es erscheint dann bei fehlender Lizenzangabe eine Aufforderung zur Angabe des Lzinzgebers und eine Auswahl verschiedener Lizenzierungsmöglichkeiten (z.B. CC BY-N-ND u.a.).


### Trash {: #files_and_folders_configuration_trash}

Im **Abschnitt "Papierkorb"** wird festgelegt, nach welcher Zeit die im Papierkorb liegenden Dateien endgütlig gelöscht werden.

Den aktuellen Inhalt des Papierkorbs sehen Sie im separaten Tab "Papierkorb".

[zum Seitenanfang ^](#files_and_folders)



## Tab Quotas {: #files_and_folders_quotas}

![core_config_files_and_folders_tab_quota_v1_en.png](assets/core_config_files_and_folders_tab_quota_v1_en.png){ class="shadow lightbox" }

In the tab "**Quotas**" the maximum storage size and the upload limit for
certain paths can be defined and adjusted.

The following default values apply system-wide:

System-wide quotas | Scope
---------|----------
::DEFAULT::BLOGSPODCASTS | Learning resources Blog and Podcast
::DEFAULT::COACHFOLDER | Coach folder in the course
::DEFAULT::COURSEDOCUMENTS | Course tool "Documents" (Course menu)
::DEFAULT::COURSEFOLDERS | Course storage folder (without course element subfolders) and Resource folder (Shared folder)
::DEFAULT::GROUPS | Folders in groups
::DEFAULT::NODEFOLDERS | Course element "Folder"
::DEFAULT::NODEPARTFOLDERS | Course element "Participant Folder"
::DEFAULT::POWERUSERS | Personal folder of authors
::DEFAULT::REPOSITORY | Learning resources like content package or tests
::DEFAULT::USERS | Personal folder of users without additional system rights

Individual quotas can also be added. These override the default value and apply, for example, only to a very specific course folder or the personal folder of a very specific user.

Specific Quotas | Scope
---------|----------
/course/10103238456/coursefolder | Course element "Folder" in a specific course
/cts/folders/BusinessGroup/4141565 | Folder in a specific group
/homes/mmusterfrau | Personal folder of the user M. Musterfrau

[zum Seitenanfang ^](#files_and_folders)



## Tab Large Files {: #files_and_folders_large_files}

![core_config_files_and_folders_tab_large_files_v1_en.png](assets/core_config_files_and_folders_tab_large_files_v1_en.png){ class="shadow lightbox" }

In the "**Large Files**" tab, administrators can search specifically for
large files and view more details about them.

Mit dem **Button "Clean up metadata"** wird ein Abgleich zwischen dem File-System und dem in der OpenOlat-Datenbank gespeicherten Abbild vorgenommen. Sollten Unstimmigkeiten vorliegen, wird das Abbild in der Datenbank aktualisiert.

![core_config_files_and_folders_tab_large_files_screen_v1_en.png](assets/core_config_files_and_folders_tab_large_files_screen_v1_en.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#files_and_folders)


## Tab Trash {: #files_and_folders_trash}

![core_config_files_and_folders_tab_trash_v1_en.png](assets/core_config_files_and_folders_tab_trash_v1_en.png){ class="shadow lightbox" }

Alle gelöschten Dateien der Instanz gelangen zunächst in den Papierkorb. Dort werden sie nach einer bestimmten Zeit automatisch gelöscht oder können von Administrator:innen gezielt ausgewählt und sofort endgültig gelöscht werden.

Das Wiederherstellen von Dateien im Papierkorb ist den Personen überlassen, die die Datei in den Papierkorb verschoben ("gelöscht") haben. Sie haben jeweils selbst die Möglichkeit, eine Datei aus dem Papierkorb zurück zu holen.

Die Verweildauer der gelöschten Dateien im Papierkorb bis zur endgültigen Löschung wird unter dem Tab "Konfiguration" bestimmt.

![core_config_files_and_folders_tab_configuration_trash_v1_en.png](assets/core_config_files_and_folders_tab_configuration_trash_v1_en.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#files_and_folders)


---

## Deleted Files (before version 19)

In the "**Deleted Files**" tab, files can be permanently deleted from
specific paths.

## Delete Orphan Versions (before version 19)

All documents which are manually deleted or for which versioning is no longer
available are placed in a kind of recycle bin. (Dieser Papierkorb unterscheidet sich vom Papierkorb ab Version 19.) From there they could be
restored, but they still need the same amount of memory. With Delete Orphan
Versions this recycle bin is deleted. The versions can no longer be restored,
but they also no longer require any memory. 


[zum Seitenanfang ^](#files_and_folders)


