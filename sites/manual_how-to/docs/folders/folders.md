# Which folders can I use to provide documents? {: #folders}


??? abstract "Goal and content of this guide"

    Do you want to store documents in OpenOlat, or have them stored? This page shows you which folder you can use for which purpose.

??? abstract "Target audience"

    [x] Authors [x] Coaches  [ ] Participants

    [x] Beginners [x] Advanced  [ ] Experts


??? abstract "Expected prior knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)



OpenOlat does not have "the one" folder, but rather about a dozen folder types for different purposes — from course material through submissions to cross-course file maintenance. This overview organizes them **from the author's perspective**:

- what each folder type is used for,
- where you set it up,
- who has access to it,
- and how you work with files in it.

At the end of this article you will find [decision aids](#decision_aid) and possible [stumbling blocks](#stumbling_stones).

---


## Folder types by context

Each folder type belongs to a context:

- **Personal** — Personal folder (containing a private and a public area).
- **Course** — Storage folder · Course element "Folder" · Participant Folder · Folder in the "Task" element · Coach folder · Course archive.
- **Group** — Group folder (access is bound to group membership)
- **Cross-course** — Resource folder (shared folder): maintain once, up to date everywhere.
- **System-wide** — Document pool (with taxonomy and competence control)


---

## At a glance: which folder for what?

| Folder | Purpose | Where to set up / open | Visible to | Upload by participants | Cross-course |
|--------|---------|------------------------|------------|------------------------|--------------|
| **Course element "Folder"** | Provide files for download; optional bulk upload | Course editor → "Folder" element | all course participants | optional | no |
| **Participant Folder** | Submission & return of files per participant | Course editor → "Participant Folder" element | each participant only their own folder + coaches | yes | no |
| **Folder in the "Task" element** | Files in the task workflow (submission, return, solution …) | Course editor → "Task"/"Grouptask" element | only within the element | yes | no |
| **Coach folder** | Storage area accessible only to coaches/owners | Course → Settings → Options | only coaches & owners | no | no |
| **Storage folder** | Background storage of all files used in the course | Course → Administration → Files | only course owners (participants only indirectly) | no | no |
| **Resource folder** | Central files for multiple courses (shared folder) | Authoring + Course → Settings → Options | depending on course/sharing permission | no | yes |
| **Group folder** | Shared file exchange within a group | Group → Tools → activate "Folder" | all group members | yes | bound to the group |
| **Personal folder** | Individual file storage (private / public) | Personal menu → File Hub | only the person themselves | — | person-specific |
| **Document pool** | Document management with taxonomy & competences | Administration (module) + File Hub | competence-/permission-controlled | — | system-wide |
| **Course archive** | Archived course/participant data (ZIP) | File Hub → "Course archive" | course owners | — | no |

[To the top of the page ^](#folders)

---


## Access paths {: #access_path}

The folders can be accessed from various places. Consider what makes sense for your participants given the planned folder content.

Course-specific access path:

- via opening a course element
- via the administration menu (as an author or coach)
- via an icon in the toolbar

Cross-context access path, depending on permission:

- via the File Hub
- via WebDAV


### Opening a folder in the course

In the course, select a "Folder", "Participant Folder" or Task course element.

### Opening a folder in the author or coach role

The Coach folder is found in the course administration, which is shown only to course owners and coaches. The Storage folder of the course is likewise located in the course administration under "Files".

### Opening via an icon in the toolbar

Authors can display a document folder for a course as an icon at the top of the toolbar.

### Opening via the personal menu

The personal folder (with the private and public subfolders) is found in the personal menu.


### File Hub {: #file_hub}

*From Release 19 · global file browser*

Central entry point in the personal menu that lists all folders you are authorized for: course, group, archive and personal folders, resource folders and the document pool.

- **Open:** Personal menu; also Course → Administration → `Files`.
- **Characteristic:** Files are **copied** when transferred (unlike the linking Media Center).
- **Visibility:** Only authorized folders; permission is granted in the source in each case.
- **Convenience:** Multi-file upload via drag & drop.

### WebDAV {: #webdav}

*Network drive access*

Mounts OpenOlat folders as a network drive on your own computer. This is ideal for transferring entire folder structures or many files at once.

- **Folders:** `coursefolders`, `groupfolders`, `home`, `sharedfolders`.
- **Access:** WebDAV link + username/email + (WebDAV) password.
- **WebDAV-capable:** Personal files, group, storage and "Folder" element folders, resource folders.
- **Limits:** quota set by OpenOlat administrators; file names max. 100 characters long; avoid umlauts in folder names; > 50 MB is tricky under Windows.

[To the top of the page ^](#folders)

---


## Controls that are the same in all folders

Since Release 19, all folders use the same revised component. You will find these features in the Storage folder, in course and group folders, in the Course archive, in the Library, Projects and further areas.

- **Two views** — Hierarchical with folders or files only; plus tile and table view with selectable columns. The breadcrumb shows the current level.
- **Search** — By file name, description and creator in the current folder including subfolders (no full-text search within files).
- **File status** — "Being edited", "locked" (via metadata) and a "New" label right after upload.
- **Actions** — In the 3-dot menu: move, copy, download, zip and delete per file.
- **Drag & drop + multi-upload** — Drag several files at once with the mouse onto the target area.
- **Bulk actions** — Select multiple entries via checkboxes and process them together.
- **Create within the folder** — Documents (OnlyOffice: Word/Excel/PowerPoint, diagrams, whiteboard, HTML …), subfolders, video and audio recordings.
- **Metadata & licenses** — Description, lock, license details (e.g. Creative Commons), view counter and direct link per file.
- **Trash can** — Deleted items go to the trash can; administrators set the automatic deletion period.
- **Quota / storage limit** — Limit per file and per folder (admin). Also applies to WebDAV upload.

[To the top of the page ^](#folders)

---


## Storage space (quota) {: #quota}

Every upload area is subject to a quota (per file and total).
- **Quota / storage limit** — Limit per file and per folder (admin). Also applies to WebDAV upload.

The **trash can contents** also count towards the quota. If storage space runs out, please empty the trash can first.

An **adjustment of the available storage space** can be made by administrators. The quota can be set both for specific roles (e.g. all authors get more storage space) and for individuals (e.g. a particular person needs to store many videos).

Use **resource folders** for files that are used multiple times instead of copying them into each course. This saves storage space and keeps content consistent.

[To the top of the page ^](#folders)

---


## The folder types in detail

## Which folders are there?

See also [Folder concept >](../../manual_user/basic_concepts/Folder_Concept.md)

### 1. Course element "Folder"

*Course · Knowledge transfer*

The classic way to provide material for download (slides, scripts). Optionally collaborative too, with upload rights for learners.

- **Location:** "Folder configuration" tab: automatically generated folder under `_courseelementdata` or a folder from the storage or resource folder.
- **Permissions:** Default: owners + coaches may upload; extendable to groups or individuals.
- **Visible:** Content for all course participants.
- **Extras:** Create documents, metadata/licenses, subscription, WebDAV link in the 3-dot menu.

More on the [Folder course element >](../../manual_user/learningresources/Course_Element_Folder.md)


### 2. Participant Folder course element

*Course · Communication & collaboration*

1:1 file exchange between participants and coaches via two subfolders — a drop box and a return box. Everyone sees only their own folder. Assessable.

- **Set up:** Course editor → "Folder settings" tab.
- **Options:** Block deletion/overwriting, submission time window, maximum number of documents.
- **Structure:** "Template settings" tab: uniform subfolders for all participants.
- **Note:** Template subfolders cannot be renamed later (only deleted/recreated).

More on the [Participant Folder course element >](../../manual_user/learningresources/Course_Element_Participant_Folder.md)


### 3. Folders in the "Task" course element

*Course · Task workflow*

Within the "Task" and "Grouptask" elements, several folders are available for the workflow: task description, submitted, returned and revised documents as well as the sample solution — accessible only within the element.

- **Set up:** Course editor → "Task" / "Grouptask" element.
- **When:** For more complex submission processes than with the Participant Folder.

More on the [Task course element >](../../manual_user/learningresources/Course_Element_Task.md)<br>
More on the [Grouptask course element >](../../manual_user/learningresources/Course_Element_Grouptask.md)


### 4. Coach folder

*Course · internal only*

A folder exclusively for coaches and owners — e.g. for internal materials that should not be accessible to participants.

- **Set up:** Settings → Options → "Coach settings".
- **Source:** Existing subfolder from the storage folder or new `_coachdocuments`.
- **Open:** Administration → "Coach documents" or via the File Hub.

More on the [Coach folder >](../../manual_user/learningresources/Course_Settings_Options.md#einstellungen-betreuerinnen)


### 5. Storage folder

*Course · foundation*

The central background storage of a course: this is where all files used in the course physically reside (HTML pages, graphics, materials of the folder elements). Participants access them only indirectly via published elements.

- **Open:** Administration → `Files` (formerly "Storage folder")
- **Auto folders:** `_courseelementdata`, `_sharedfolder`, `_documents`, `_coachdocuments`
- **Structure:** Subfolders can be created freely; structure them sensibly.
- **Note:** Quota per file and total — also applies to upload via WebDAV.

More on the [Storage folder >](../../manual_user/learningresources/Storage_folder.md)

### 6. Resource folder

*Cross-course · learning resource*

The only folder type that provides the same files across multiple courses. Maintain centrally once — changes take effect in all linked courses.

- **Create:** In the Authoring area as its own learning resource (with its own owners).
- **Embed:** Course → Settings → Options; max. 1 per course; appears as `_sharedfolder`.
- **Mode:** Read-only (only referenced) or without write protection — then changes take effect across all courses.
- **Standalone:** Can also be used independently of a course via the "Sharing" tab.

More on the [Resource folder >](../../manual_user/learningresources/Resource_Folderde.md)


### 7. Group folder

*Group · collaboration*

Shared folder for the members of a learning or working group to exchange documents, including subfolders. Access is strictly bound to group membership.

- **Activate:** Group coaches enable the "Folder" tool.
- **Access:** All group members; also via the File Hub, if a member.
- **Extras:** Subscribable; quota adjustable per group.

More on the [Group folder >](../../manual_user/groups/Using_Group_Tools.md)


### 8. Personal folder

*Personal · per person*

The individual file storage of each person, independent of courses. Divided into a private and a public area (the latter viewable via the business card).

- **Open:** Personal menu → File Hub.
- **Areas:** `private` (only me) · `public` (readable via the business card).

Since Release 19, you can find the personal folder in the [personal menu >](../../manual_user/personal_menu.md) in the [File Hub >](../../manual_user/personal_menu/File_Hub.md).

### 9. Document pool

*System-wide · managed*

Not a pure file storage but a document management system: documents are tagged with taxonomy/metadata, and access can be bound to competences. Documents cannot be embedded directly into a course.

- **Visible:** In the File Hub as a folder; optionally as a site in the main navigation.
- **Access:** Competence-/permission-controlled; WebDAV possible.

More on the [Document pool >](../../manual_admin/administration/Modules_Document_pool.md)


### 10. Course archive

*Course · archive*

When archiving an entire course or individual elements, the data is stored as a ZIP in the "Course archive" folder. Contents can be displayed in the File Hub.

- **Open:** File Hub → "Course archive".
- **Content:** Participant data kept separately from the course, stored as a ZIP.

More on the [Course archiving >](../../manual_user/learningresources/Course_Archiving.md#wo-finde-ich-kursarchiv-dateien)

[To the top of the page ^](#folders)

---


## Decision aid {: #decision_aid}

| I want to … | I use … |
|-------------|---------|
| Provide material for download | **→ Course element "Folder"** |
| Collect submissions and return them individually | **→ Participant Folder course element** (if complex: "Task" course element) |
| Jointly maintain files used in multiple courses | **→ Resource folder** |
| As an author, manage all files used in a course | **→ Storage folder** |
| Store internal materials only for coaches | **→ Coach folder** |
| Exchange files jointly within a group | **→ Group folder** |
| Store my own files independently of a course | **→ Personal folder** |
| Upload large amounts / entire folder trees | **→ WebDAV** |
| Get an overview of all my folders in one place | **→ File Hub** |


[To the top of the page ^](#folders)

---


## Stumbling blocks {: #stumbling_stones}

* Subfolders within a folder element exist only there (within that course element). Keep this in mind when building similar structures.

* If further Folder course elements are inserted below a Folder course element in the course menu, these subfolders are not displayed within the parent folder. This is because the separate Folder course elements do not communicate with one another.

* There is no WebDAV access to subfolders within a Folder course element.

* The trash can contents also count towards the quota.

* Please also do not confuse the Structure element with a Folder course element ("Folder" element instead of "Structure" element).

[To the top of the page ^](#folders)

---

## Inserting files {: #insert_files}

Once the desired folders exist, you can there

- upload documents
- create documents directly in the folder
- transfer documents via WebDAV

Which people (OpenOlat roles) may upload or create documents in which folder depends on the respective configurations (permissions granted) by authors or administrators.

Which document formats can be created directly depends on which tools are installed — for example, whether licenses for Microsoft Word and Excel are available for use in OpenOlat. If necessary, contact your administrators.

Also remember that the size of individual files and the total storage of a folder are set by quotas.

[To the top of the page ^](#folders)

---


## Further information {: #further_information}

[Folder concept >](../../manual_user/basic_concepts/Folder_Concept.md)<br>
[Folder course element >](../../manual_user/learningresources/Course_Element_Folder.md)<br>
[Participant Folder course element >](../../manual_user/learningresources/Course_Element_Participant_Folder.md)<br>
[Task course element >](../../manual_user/learningresources/Course_Element_Task.md)<br>
[Grouptask course element >](../../manual_user/learningresources/Course_Element_Grouptask.md)<br>
[Coach folder >](../../manual_user/learningresources/Course_Settings_Options.md#enable-coach-folder)<br>
[Storage folder >](../../manual_user/learningresources/Storage_folder.md)<br>
[Resource folder >](../../manual_user/learningresources/Resource_Folder.md)<br>
[Group folder >](../../manual_user/groups/Using_Group_Tools.md)<br>
[Document pool >](../../manual_admin/administration/Modules_Document_pool.md)<br>
[Course archive >](../../manual_user/learningresources/Course_Archiving.md#where-can-i-find-course-archive-files)<br>
[File Hub >](../../manual_user/personal_menu/File_Hub.md)<br>

[To the top of the page ^](#folders)
