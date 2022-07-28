# Files and Folders

In the administration in the "[Core functions](Core_functions.md)" area,
settings can also be made regarding the files, including versions and quotas.

In the Overview tab, administrators can get a quick overview of the number and
size of OpenOlat files, versions, deleted files and thumbnails, and can take
actions in this regard.

## Versions

In the "Versions" tab, the maximum number of versions for a file can be
defined.

If versioning is enabled, files are not overwritten but created as a new
version (also called revision). Older versions of a document can be downloaded
and restored if necessary. If files are deleted, they appear in the list of
deleted files and can be restored. If the versioning function is enabled,
files can also be locked, e.g. if a user is working on a document and wants to
prevent another user from creating a new version in the meantime.

Versioning is available in all folders of the system: personal folders, group
folders, course folders, resource folders and course elements 'folders'.

## Quotas

In the tab " **Quotas** " the maximum storage size and the upload limit for
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

## Large Files

In the " **Large Files** " tab, administrators can search specifically for
large files and view more details about them.

## Deleted Files

In the " **Deleted Files** " tab, files can be permanently deleted from
specific paths.

### Delete Orphan Versions:

All documents which are manually deleted or for which versioning is no longer
available are placed in a kind of recycle bin. From there they could be
restored, but they still need the same amount of memory. With Delete Orphan
Versions this recycle bin is deleted. The versions can no longer be restored,
but they also no longer require any memory.  

### Clean up versions:

The number of versions can be adjusted. If, for example, 5 versions are now
changed to 2 versions, 3 versions per document are superfluous. However, these
are not deleted directly. If you set the number back to 5 versions, they will
become visible again. However, to delete these versions completely, click on
Clean up versions. Afterwards, the versions can no longer be restored.

