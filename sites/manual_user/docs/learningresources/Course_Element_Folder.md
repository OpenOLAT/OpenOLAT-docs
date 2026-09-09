# Course Element "Folder" {: #folder}

## Profile

Name | Folder
---------|----------
Icon | :o_icon_o_bc_icon:
Available since | New edition with release 19.1
Functional group | Knowledge transfer
Purpose | Provision of files for download (e.g. material for the course)
Assessable | no
Specialty / Note | A similar course element is the course element "Participant folder".


In the course element "Folder" you can offer files to be downloaded. Often folders are used to provide course participants with scripts or slides regarding your course. 
The "folder" can also be configured as a collaborative tool for learners to upload files.

---


## Configuration in the course editor {: #config}

### Tab learning path {: #tab_learning_path}

=== "Learning path tab with fixed times"

    ![Release date and To be edited by with fixed date and time fields, completion criterion Visit course element: Learning path tab with fixed times](assets/course_element_folder_tab_learning_path_v1_de.png){ class="shadow lightbox" }


=== "Learning path tab with relative times"

    ![Relative date enabled, release date and To be edited by set as days after first course visit of the participant: Learning path tab with relative times](assets/course_element_folder_tab_learning_path_relativ_v1_de.png){ class="shadow lightbox" } 


**Implementations**<br>
As with other course elements, you can specify that a "folder" must be opened at least once for it to be considered "completed". 
As a voluntary course element, it does not count towards the calculation of learning progress.
If it is excluded, it will not appear in the menu unless you specify that certain course members are to see this course element in the course menu when exceptions are activated.

**Relative date**<br>
This entry refers to the two following entries. If no relative date is required, fixed dates can (optionally) be entered for "Release date" and "To be processed by". If relative dates are required, reference points such as "x days after first course attendance" can be selected instead of fixed dates.

**Share date**<br>
The course element is visible but not accessible before the release date. It can be opened and worked in from the specified date. If no entry is made, the folder remains permanently available from the release date, provided you have access to the course.

**To be edited by:**<br>
The module can be opened and edited up to the specified date. 
If no entry is made, the folder remains permanently available from the release date, provided you have access to the course.

**Processing time**<br>
Here you can enter how long the author estimates it will take to complete the course element. The processing time specified here is independent of how much time is actually required. However, the estimated time can be used to calculate the learning progress.

**Completion criterion**<br>
Here you determine how the course element is marked as "completed" in the course menu. The options are "Visit course element" and "Confirmation by participant".

---


### Tab folder configuration {: #tab_folder_config}

![Storage location automatically generated or chosen from the course, full-access checkbox enabled for coaches, disabled for participants: Folder configuration tab in the course editor](assets/course_element_folder_tab_folder_config_v1_de.png){ class="shadow lightbox"}


![1](assets/1_green_24.png) **Select folder**<br>
In the tab "Folder configuration" of the course element you define *where* exactly the files of this folder should be stored in the folder of the course. For this, OpenOlat can either generate a folder automatically or select a specific folder from the course folder.

If the option **"Automatically generated folder"** is selected, OpenOlat creates the subfolder "_courselementdata" including a subfolder with the name of the respective course element "folder". All files of the course element are now saved here.

If you select **"Choose folder from course storage"**, you can select an existing folder from the course folder. This is especially useful if you have already uploaded the files you want to make available in a structured way in the course's folder. In the next step, select an existing folder in the storage folder and create a new subfolder in the storage folder. If a resource folder is linked to the course in the [Course settings](../learningresources/Course_Settings.md), this can also be selected. In this case, select "_sharedfolder" from the folders displayed in the storage folder.

<br>

![2](assets/2_green_24.png) **Upload files**<br>
Once you have selected the specific storage location, you can upload or create your files using the "Manage folder" button in the "Upload files" area. 

![Expanded Upload files menu with five options from Add from file hub to Record audio: preview of the folder course element](assets/KB_Ordner_Datei_upload.png){ class="shadow lightbox" }

Access to this file area is also possible when the course editor is closed (see below).

<br>

![3](assets/3_green_24.png) **User rights**

Under "User rights" you can define who can upload and create files in the course element folder. By default, coaches are allowed to upload files in addition to the owners, but not the participants.

The extended configuration can also be used to define the provision of files for specific groups, e.g. for assistants or support staff, or for individual persons only. 

---


## View with closed course editor {: #view_with_editor_closed}

![File list with actions like Download and Zip, columns for file status and license: view with closed course editor](assets/Kursbasutein_Ordner_191a.jpg){ class="shadow lightbox" }

The following options are available to course owners and persons with the appropriate authorization:


### Add files

**Upload files:** Select a file from your hard disk. Click on the small down arrow to see additional options (see screenshot "Upload files"):

 * **Add from file hub:** Access the [File Hub](../personal_menu/File_Hub.md) and your folders and files. You can also access your [Media Center](../personal_menu/Media_Center.md) and upload files directly to the File Hub.

* **Create Document:** Depending on the editors activated (e.g. Word, Excel, PowerPoint, diagrams, whiteboard, text, HTML, CSS, XML), you can create new documents here and add a description, license and other metadata to them.

* **Create folder:** Creates a new subfolder in the course element.

* **Record video:** Record a video with your webcam.

* **Record audio:** Record an audio file.

---


### Further options and adjustments to the course element  {: #further_options}

Users can subscribe to changes in the folder. The view can also be customized by switching between the visual tile view and the detailed table view. In the table view, the displayed columns can be selected to show more details than in the tile view. The search function makes it possible to find files quickly. Deleted documents are moved to the "trash can".

You can display the [WebDAV link](../basic_concepts/Using_WebDAV.md) and update metadata in the 3-dot menu of the course element. 



### Metadata  {: #metadata}

Course owners can edit the specific [metadata](../basic_concepts/Full_Text_Search.md#metadata) of a file via the 3-dot menu of a specific file. 

In addition to the description and lock properties, the license information is particularly relevant. You can use the license information to define a specific license for the document, for example, use one of the existing Creative Commons licenses, enter the licensor, and leave additional information about the publisher, source, publication date, and so on. The license is displayed in a separate column in the folder module. By clicking on the license, the user receives the stored information on the respective license.

The metadata also shows how often a file was called up. There is also a link with which you can directly link the respective file. Whether external persons can also access the file depends on the access settings of the course.

### Edit Files {: #edit_files}

Persons with editing rights can switch directly to editing mode for supported file formats such as docx, xlsx, pptx, draw.io, dwb, txt, html, css and xml by clicking on the file name. The prerequisite for this is that these formats have been activated in the OpenOlat [Administration](../../manual_admin/administration/External_Tools_-_Administration.md).


## Further information {: #further_information}

[Course Settings >](../learningresources/Course_Settings.md)<br>
[Personal tools: File Hub >](../personal_menu/File_Hub.md)<br>
[Personal tools: Media Center >](../personal_menu/Media_Center.md)<br>
[Using WebDAV >](../basic_concepts/Using_WebDAV.md)<br>
[Full-Text Search >](../basic_concepts/Full_Text_Search.md)<br>
[External Tools: Overview >](../../manual_admin/administration/External_Tools_-_Administration.md)<br>
[Learning path course - Course editor >](../../manual_user/learningresources/Learning_path_course_Course_editor.md)

**youtube**<br>
[Subscriptions](<https://www.youtube.com/embed/h9gOqt7TR7Q>)

[To the top of the page ^](#folder)
