# Folder concept {: #folders}

In :octicons-tag-24: Release 19, the folder component has been completely revised and some of the views and working methods have changed.

## Different folder types {: #folder_types}

### Personal folder {: #personal_folder}

The personal folder can be found in the personal tools in the [personal menu](../personal_menu/index.md). From Release 19, it can be found in the [File Hub](../personal_menu/File_Hub.md).

It offers the option of storing individual files independently of courses or resource folders. 

Within the personal folder, a distinction is made between a **private** and a **public** area. Files in the private folder are only visible to the respective person, while files in the public area can be read and downloaded by all users in the system via the business card.

!!! hint "Tipp"

    To view the business cards of other OpenOlat users, select **Person search** in the personal menu and search for the desired person using the search mask.


[See the details about personal folders (up until Release 18) >](../personal_menu/Personal_folders.md)<br>
[See the details about the file hub >](../personal_menu/File_Hub.md)<br>
[To the top of the page ^](#folders)

---


### Storage folder {: #storage_folder}

Files used in a course can be stored in the storage folder of this course. 

You can access the course via **Administration > Files > Storage folder** or via the [File Hub](../personal_menu/File_Hub.md) under "Courses".

Files can also be uploaded here, for example, which are to be linked and accessed later within the course from a page.


[See the details >](../learningresources/Storage_folder.md)<br>
[To the top of the page ^](#folders)


### Resource folder {: #resource_folder}

Files that are to be used in several courses can be uploaded to a resource folder. This allows them to be edited centrally and only in one place.

To use the resource folder within a course, it must be integrated via **Administration > Settings > Options tab**. You will then find the new folder "shared folder" in the storage folder of the course and have access to the files of the resource folder there. Only one resource folder can be used per course.

The cross-course "resource folder" is a learning resource and is therefore also listed in "Authoring" and can be edited there. 

[See the details >](../learningresources/Resource_Folder.md)<br>
[To the top of the page ^](#folders)


### Course element "Folder" {: #course_element_folder}

The [course element "Folder"](../learningresources/Course_Element_Folder.md) is a storage option within a course or group. Course tutors and course owners can make files available for download there. Course participants can also be granted the right to upload files.

[See the details >](../learningresources/Course_Element_Folder.md)<br>
[To the top of the page ^](#folders)


### Course element "Participant folder" {: #course_element_participant_folder}

The [course element "Participant folder"](../learningresources/Course_Element_Participant_Folder.md) enables the exchange of files between individual participants and coaches. Two subfolders are available for this purpose. One is the "Participants folder", which participants can use to submit files to coaches. The other is the "Coach return order", in which the coaches can return files to all participants simultaneously or individually.

[See the details >](../learningresources/Course_Element_Participant_Folder.md)<br>
[To the top of the page ^](#folders)


### Folder in "Task" and "Group task" {: #course_element_task}

Within the workflow of a [course element "Task"](../learningresources/Course_Element_Task.md) and ["Group task"](../learningresources/Course_Element_Grouptask.md), various documents are uploaded and downloaded by coaches or participants: Assignment, submitted documents, returned documents, revised documents and sample solution. 
Folders are available for all files within the course element, which are only accessible within the course element.

[See the details >](../learningresources/Course_Element_Task.md#workflow)<br>
[To the top of the page ^](#folders)


### Folder for members of a group (Group folder) {: #group_folder}

Within a group, group members can exchange documents in the shared group folder. Files can be uploaded, created and downloaded there. Further structuring with subfolders is also possible.

Group folders can also be accessed via the [File Hub](../personal_menu/File_Hub.md). The File Hub automatically recognizes whether you are a member of a group and which group folders are therefore displayed in the File Hub. 

Access to a group folder is always linked to membership of the relevant group.

[See the details >](../groups/Using_Group_Tools.md)<br>
[To the top of the page ^](#folders)


### Folder for coahces (Coach folders) {: #coach_folder}

A folder can be set up within a course that is only accessible to the coaches of this course. Documents can be exchanged there, for example, or files relating to the course that should not be accessible to participants can simply be stored there.

This folder is set up under **Administration > Settings > Options tab > "Coach settings"** section. 

A subfolder from the course storage folder can be used or a new folder can be created automatically (_coachdocuments).

The folder can then be opened under **Administration > Coach documents**.
The folder can also be accessed via [File Hub](../personal_menu/File_Hub.md) by selecting the course.

[See the details >](../learningresources/Course_Settings_Options.md)<br>
[To the top of the page ^](#folders)


### Archive {: #archive}

If an entire course is archived or only a partial archive is created from some course elements, these are stored in the File Hub in the "Course archive" folder.

[See the details >](../learningresources/Course_Archiving.md)<br>
[To the top of the page ^](#folders)


### Document pool {: #documentpool}

The document pool is also displayed in the File Hub as a folder in which different files are stored. However, metadata is added to the files here (e.g. taxonomy). It is therefore not a pure file storage in a file system, although files can be transferred to the document pool via WebDAV, for example.

[See the details >](../basic_concepts/File_Hub_Concept.md#dokumentenpool)<br>
[To the top of the page ^](#folders)



## View {: #view}

Use the buttons above the list to switch between

* hierarchical view with folders and
* only files in the view

=== "Hierarchical view with folders"

    ![folder_concept_view_folder_v1_de.png](assets/folder_concept_view_folder_v1_de.png){ class="shadow lightbox" title=" " }

=== "Only files in the view"

    ![folder_concept_view_files_v1_de.png](assets/folder_concept_view_files_v1_de.png){ class="shadow lightbox" title=" " }

!!! hint "Hint"

    In the crumb trail below the buttons, you can always see which folder you are currently in. Click on a section in the crumb trail to jump directly to this level.



## Search {: #search}

The search function in folders is looking for

* File names,
* Description and
* Creator

in the current folder and its subfolders.
(It is currently not a full-text search, i.e. no search within Word files, for example.)


## File status {: #status}

The file status can be found in the **"File status"** column. (If the column is not visible, it can be displayed using the gear icon.)

If a file is currently being edited, it receives the **status "Being edited"**.

The **status "locked"** can be set in the metadata. You edit the metadata under the 3 dots at the end of a line.

When a file is uploaded, it is first marked with a **label as "New"**. (This helps with immediate "further processing", such as moving or copying). The label is only displayed to the person who uploaded the file. It disappears as soon as the folder has been exited.


## Working with files {: #work_with_files}

### Actions via menu
To move, copy, download, pack (zip) or delete files, you will find selection options **under the 3 dots** at the end of a line (right-hand edge of a list).

### Drag & drop
Files can also be moved to a selected target field using **drag & drop** with the mouse.

### Multi file upload
It is also possible to select several files and move them together to the target field.

### Mass actions
As soon as at least one checkbox is selected at the beginning of a line in a list, buttons with available options (download, move, etc.) appear above the list.

If you select the checkbox in the header, all list entries are selected and highlighted. This allows you to quickly edit several entries at the same time.


## Paper basket {: #paper_basket}

The files in the paper basket can be deleted automatically after a certain period of time. The retention period in the paper basket and automatic deletion is set by the administrator.




!!! info "Note" 

    The folder component is used in the following OpenOlat areas:
    
    - Shared Folder
    - Course Documents Folder
    - Course Logs Archive
    - Library Module
    - Project broker
    - Collaboration Tools
    - Taxonomy / Lost & Found
    - Participant Folder

