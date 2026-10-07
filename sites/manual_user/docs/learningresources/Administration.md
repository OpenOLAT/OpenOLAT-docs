# Course Administration: Overview {: #course_administration}

![Course "Administration" menu of a learning path course with its options, from Settings and Members management via Course statistics and Copy to About this course and Delete](assets/course_administration_v5_en.png){ class="shadow lightbox aside-left-lg" }

:octicons-device-camera-video-24: **Video introduction (German)**: [Admin-Funktionen](<https://www.youtube.com/embed/rWPcz6udUrI>){:target="_blank"}


If you are an **owner** of a course, the "Administration" button is displayed at the top left. There you will find all options for **editing, configuration and administration** of the course, before and during its use. Administrators and learning resource managers of the organisation the course belongs to see the same options. The most important options include the [course editor](#course_editor) and the [settings](#settings).

The "Administration" button is also available for **coaches**. However, fewer options are then displayed, and only those relevant to coaches. In particular, for example, the [assessment tool](#assessment_tool). Persons who have been granted individual rights in the [Rights area of the members management](Members_management.md#section_rights) see the options for these rights.

!!! info "Important"

    Some options are only available if the corresponding feature is activated. If necessary, please contact the administrators of your organisation.


Other learning resources also have the "Administration" menu, but the menu options there are not as extensive. They vary depending on the learning resource.

Below you will find an overview of the "Administration" menu options for **courses**.


---

## Settings {: #settings}

All settings that affect the **course as a whole** are made here. (Settings that only affect a specific course element are made in the course editor after selecting the relevant course element).

[See the details >](Course_Settings.md)<br>
[To the top of the page ^](#course_administration)


## Members management {: #members_management}

In the members management, course owners will find a list of all persons who have access to the course or learning resource. You can grant access to other users and groups here by making someone a member of the course.

[See the details >](Members_management.md)<br>
[To the top of the page ^](#course_administration)


## Course editor {: #course_editor}

In the course editor the course can be edited by adding and configuring course elements.

[See the details >](General_Configuration_of_Course_Elements.md)<br>
[To the top of the page ^](#course_administration)


## Files {: #files}

Some files used in the course are stored in the **storage folder**. This belongs to the course and can be opened here.<br>
(Other files and objects are shared with other users, are stored in other places and can be managed in the File Hub or Media Center).

[See the details about the Storage folder >](Storage_folder.md)<br>
[See the details about the File Hub >](../personal_menu/File_Hub.md)<br>
[See the details about the Media Center >](../personal_menu/Media_Center.md)<br>

### Storage usage [:octicons-tag-16:{ title="from Release 18.0.2 (OO-6938)" }](https://track.frentix.com/issue/OO-6938){:target="_blank"} {: #storage_usage}

When a course grows large or an upload no longer goes through, the storage usage evaluation shows which folders and course elements occupy how much storage and where a quota sets the limit. This shows you where you can clean up and whether you need to request more space.

You open the evaluation in the "Files" area with the :o_icon_o_icon_hdd: "Show memory usage" button at the top right:<br>
`Course > Administration > Files > Show memory usage`

![Show memory usage button highlighted at the top right, above the storage locations of the course](assets/course_admin_files_storage_usage_button_v1_en.png){ class="shadow lightbox" title="Files area of the course administration" }

The "Files" area is visible to owners of the course and to persons who have been granted the "Course editor" right in the [Rights area of the members management](Members_management.md#section_rights).

The storage usage page, titled "Memory usage resources" on screen, shows the values "Total size", "Internal size" and "Number of files" of the course at the top, together with a pie chart showing the share of resources with and without quota. Below, a table lists the storage folder and the course elements in the structure of the course. The search field finds a row by name or type, "Open all" and "Close all" expand and collapse the structure. Each row shows the type, the number of files, the size, the quota and, in the "Currently used" column, a bar showing how much of the quota is occupied. From 80 percent, OpenOlat highlights the bar in color. "Display" opens the folder or the course element of the row. The table can be exported as an Excel file.

![Filters All, Internal with quota and Internal without quota highlighted, below them the Storage folder row with quota and the Edit quota action](assets/course_admin_storage_usage_v1_en.png){ class="shadow lightbox" title="Memory usage resources page of a course" }

Three filters narrow down the table:

* "All": all folders and course elements of the course, including those without files.
* "Internal with quota": the folders with their own quota. These are the storage folder, "Coach files" and "Documents (Toolbar)" as well as the course elements "Folder" and "Participant folder".
* "Internal without quota": the course elements that occupy storage but have no quota of their own. These are "Forum", "File dialog", "Task", "Group task", "Page" and "Topic broker".

If a "Folder" course element uses a folder from the storage folder as its file destination, it does not appear as a separate row. The same applies to "Coach files" and "Documents (Toolbar)" when they use a folder from the storage folder. The files then count towards the storage folder and fall under its quota. For the "Participant folder" course element, the table shows the drop box and the return box for each participant. The quota applies to each of these folders individually.

#### Edit quota {: #storage_usage_edit_quota}

The "Edit quota" action only appears in rows with their own quota: for the storage folder, for "Coach files" and "Documents (Toolbar)" as well as for the course elements "Folder" and "Participant folder". The course elements "Forum", "File dialog", "Task", "Group task", "Page" and "Topic broker" count their usage but have no quota that can be adjusted.

The quota can be changed by [administrators, system administrators and learning resource managers](../basic_concepts/Roles.md#org) of the organisation the course belongs to. Everyone else sees the current values in the "Edit quota" dialog, but no button to save. If you need more space for a folder, contact one of these persons.

The guide ["What measures can I take to reduce storage space consumption?"](../../manual_how-to/reduce_storage_consumption/reduce_storage_consumption.md) describes further ways to reduce storage requirements.

[To the top of the page ^](#course_administration)


## Assessment tool {: #assessment_tool}

The assessment tool (not to be confused with the course element "Assessment") is used to coach and monitor the results of all course participants. Here you have access to all assessable course elements and can, for example, make assessments with points, pass/fail etc. and provide individual feedback.

[See the details >](Assessment_tool_overview.md)<br>
[To the top of the page ^](#course_administration)


## To-dos [:octicons-tag-16:{ title="from Release 18.2 (OO-7039)" }](https://track.frentix.com/issue/OO-7039){:target="_blank"} {: #to-dos}

To-dos relating to a specific course can be created directly here in the course. To-dos can be assigned to all course participants or to individuals.

[See the details >](Course_todos.md)<br>
[To the top of the page ^](#course_administration)


## Badges [:octicons-tag-16:{ title="from Release 18.0 (OO-7003)" }](https://track.frentix.com/issue/OO-7003){:target="_blank"} {: #badges}

If activated, course-related badges can be created, edited and displayed here.

[See the details >](OpenBadges.md)<br>
[To the top of the page ^](#course_administration)


## Coach files [:octicons-tag-16:{ title="from Release 16.0 (OO-5566)" }](https://track.frentix.com/issue/OO-5566){:target="_blank"} {: #coach_files}

If activated, coaches and owners of the course can store files in this shared folder that only they can access.

[See the details >](Coach_Files.md)<br>
[To the top of the page ^](#course_administration)


## Events and Absences [:octicons-tag-16:{ title="from Release 12.0 (OO-2636)" }](https://track.frentix.com/issue/OO-2636){:target="_blank"} {: #events_and_absences_}

Here you will find the tool for the administration of participants' events and absences.

[See the details >](Events_and_absences.md)<br>
[To the top of the page ^](#course_administration)


## Reminders [:octicons-tag-16:{ title="from Release 10.3 (OO-1494)" }](https://track.frentix.com/issue/OO-1494){:target="_blank"} {: #reminders}

The reminder function is used to organize the automatic sending of emails. The sending can be linked to various conditions.

[See the details >](Course_Reminders.md)<br>
[To the top of the page ^](#course_administration)


## Assessment management [:octicons-tag-16:{ title="from Release 10.2 (OO-1349)" }](https://track.frentix.com/issue/OO-1349){:target="_blank"} {: #assessment_management}

This menu option allows you to create, edit and display configurations for assessment modes. For example, you can configure an assessment mode that only allows participants to access certain course elements and also restricts participants from accessing other sources of information.

[See the details about the assessment mode >](Assessment_mode.md)<br>
[See the details about the assessment inspection >](Assessment_inspection.md)<br>
[To the top of the page ^](#course_administration)


## Data collection previews [:octicons-tag-16:{ title="from Release 18.2 (OO-7399)" }](https://track.frentix.com/issue/OO-7399){:target="_blank"} {: #data_collection_previews}

If activated, course owners can view the planned surveys of the **Quality Management** module of the course. This preview is purely informative for course owners. Editing is only possible for quality managers.

[See the details about quality management >](../../manual_admin/administration/Modules_Quality_Management.md)<br>
[To the top of the page ^](#course_administration)


## Learning areas {: #learning_areas}

Several groups of a course can be bundled together with the help of a learning area. The learning areas of the course can be created, displayed and edited under this menu option.

[See the details >](Learning_Areas.md)<br>
[To the top of the page ^](#course_administration)


## Course DB {: #course_DB}

Here you can create a new course-specific database that can store certain course-specific information.

[To the top of the page ^](#course_administration)


## Course statistics {: #course_statistics}

This course function shows you statistics on access to your OpenOlat course. All owners of this course have access to the statistics. Coaches and other members only see the menu item if they have been granted the right "Statistics".

[See the details >](Statistics_Course.md)<br>
[To the top of the page ^](#course_administration)


## Test statistics {: #test_statistics}

The test statistics allow general course-related, anonymized statistical assessment of the OpenOlat tests in a course. All tests contained in the course are displayed. The menu item appears as soon as the course contains a "Test" course element.

[See the details >](Statistics_Test.md)<br>
[To the top of the page ^](#course_administration)


## Survey statistics {: #survey_statistics}

The survey statistics allow you to carry out a general course-related, anonymized statistical assessment of your surveys. The menu item appears as soon as the course contains a "Survey" course element.

[See the details >](Statistics_Survey.md)<br>
[To the top of the page ^](#course_administration)


## Archiving & Reporting {: #archiving_reporting}

Elements of the course can be archived here with the help of a wizard. A complete archive or a partial archive with selected course elements can be created, as well as course results, etc.

[See the details >](Course_Archiving.md)<br>
[To the top of the page ^](#course_administration)


## Offer types {: #offer_types}

In order to offer a course or other learning resource in the catalog, at least one offer is required. However, several different offers can also be created, for which you will find the booking orders here.

[See the details >](Offer_Types.md)<br>
[To the top of the page ^](#course_administration)


## Copy {: #copy}

When copying a course, the complete structure, folder contents, HTML pages and group names (without group members) are copied. However, user data such as forum posts, group members etc. are not copied.

[See the details >](Course_Copy.md)<br>
[To the top of the page ^](#course_administration)


## Copy with wizard [:octicons-tag-16:{ title="from Release 16.0 (OO-4416)" }](https://track.frentix.com/issue/OO-4416){:target="_blank"} {: #copy_wizard}

If you copy a course using the wizard, you can select the elements to be copied. The menu item only appears in learning path courses.

[See the details >](Course_Copy_Wizard.md)<br>
[To the top of the page ^](#course_administration)


## Save as template [:octicons-tag-16:{ title="from Release 20.2 (OO-8896)" }](https://track.frentix.com/issue/OO-8896){:target="_blank"} {: #copy_template}

If an existing course is to be used with the Course Planner for instantiation in implementations, save it as a template.

[See the details >](Course_Copy_Template.md)<br>
[To the top of the page ^](#course_administration)


## Instantiate as course [:octicons-tag-16:{ title="from Release 20.2 (OO-8897)" }](https://track.frentix.com/issue/OO-8897){:target="_blank"} {: #instantiate_as_course}

If you have prepared a template, use this menu item to create a new course from it. A wizard guides you through the creation.

The menu item only exists in courses with the usage "Template". There it takes the place of "Save as template".

[See the details >](Creating_Course.md#purpose)<br>
[To the top of the page ^](#course_administration)


## Duplicate as learning path {: #duplicate_as_learning_path}

Conventional courses (including all courses created before OpenOlat version 15) can be converted into a learning path course using this tool. The original conventional course is retained and a copy is created in which the additional features of a learning path course are added. When converting, the first decision to be made is whether to create the course "With learning path" or "With learning progress".

The function is only available for conventional courses.

!!! tip "Tip"

    If the course is only to be transferred to the current format, the "With learning progress" option is usually the better choice. In this case, the course structure does not have to be edited in a fixed order, which is more in line with the hypermedia structure of the previous course. If necessary, this setting can also be adjusted retrospectively in the course editor of the copied course at the top course element.

    Please note that guests do not have access to learning path courses.

[To the top of the page ^](#course_administration)


## Export content {: #export_content}

Export your learning resources as a ZIP file to get a backup copy or to import the learning resource in another OpenOlat instance.

[See the details >](Export_Content.md)<br>
[To the top of the page ^](#course_administration)


## About this course [:octicons-tag-16:{ title="from Release 21.1 (OO-9760)" }](https://track.frentix.com/issue/OO-9760){:target="_blank"} {: #about}

Here you look up which ID the course has, who created it and who owns it. The window also shows the external link and the products in the Course Planner in which the course is embedded. For other learning resources, you also see which courses use them.

The menu item is visible to the owners of the course, learning resource managers and administrators.

[See the details >](Technical_Information_on_Resources_and_Usage.md)<br>
[To the top of the page ^](#course_administration)


## Delete {: #delete}

When a course is deleted, it is first moved to the trash and all user data is removed. (This also applies to learning resources).

If the course is in the trash, the menu item "Restore" appears in this place.

[See the details >](Course_Delete.md)<br>
[To the top of the page ^](#course_administration)




## Further information {: #further_information}

[Using Additional Course Features >](Using_Additional_Course_Features.md)<br>
[Toolbar: Info page >](Info_page.md)<br>
[Roles and Rights: Which roles are available? >](../basic_concepts/Roles.md)

**youtube**<br>
[Admin-Funktionen](<https://www.youtube.com/embed/rWPcz6udUrI>)

[To the top of the page ^](#course_administration)


