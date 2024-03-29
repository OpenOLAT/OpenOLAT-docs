# Using Additional Course Features

In the "Administration" → "Settings" tab you can configure the following additional functions.

![](assets/Toolbar1.png){ class="shadow lightbox" }

![](assets/toolbar_b.png){ class="shadow lightbox" }

## Course Search

In addition to a [full text search](../basic_concepts/Full_Text_Search.md) for the total of OpenOlat you can activate a search within a course. You can search for the following elements:

* Title, short title, description of all course elements
* Content of html pages
* Documents in folders
* Title and content of forum entries
* Title and content of notifications
* Wiki entries

## Course Calendar

One calendar can be activated per course. There are two options for integration. The calendar can either be displayed as a [course element](../learningresources/Course_Elements.md) or at a central position at the top of the course toolbar and thus provide a good
overview.

New dates are simply created by clicking on the desired date. Afterwards, the title, description, start and end as well as a location, possible repetitions and visibility can be set. The date then appears in the calendar or in all instances of the course calendar and can be edited by clicking on the date and the "Edit" option.

With the "Edit" option you also get access to further calendar tabs and can set links to course elements or external websites used in the course. If you would like to delete all dates of a course calendar, simply click on the gear symbol in the calendar area and select "Reset calendar".

Course calendars are also automatically transferred to the [personal calendars](../personal_menu/Calendar.md) of course members. Thus all dates can be called up also directly over the personal OpenOlat calendar. The same applies to group calendars. In the case of group calendars, it is possible to set in the group administration which write/read rights the members receive.

By default, only owners of a course have write access to the calendar. Course participants only have read rights, so they cannot write new appointments or edit existing ones. However, if you insert the calendar as a course element, you can configure the permissions.

## Participant list

Here all course owners, coaches and participants of a course can be displayed centrally. Course participants can send e-mails to specific persons, even to individual course members. In contrast to the [course element "Participant list"](../learningresources/Course_Element_Participant_List.md) no further configurations can be made here.

## Participant infos

This tool corresponds to the [course element "Notifications"](../learningresources/Course_Element_Notifications.md). Participants can subscribe to the tool and thus be notified when there is new information. In contrast to the course element no further configurations can be made here.

## E-Mail

Here the course owner can configure to whom the learners can send mails via this link. There are three course roles to choose from: "course owner", "coach", and "participant". A further differentiation is not possible. In case you need more differentiated settings for sending mails to course members you should use the [course element "E-mail"](../learningresources/Course_Element_EMail.md) or the [course element "Participant list"](../learningresources/Course_Element_Participant_List.md).

## Teams Online-Meeting

Similar to the Microsoft Teams course element, rooms for synchronous meetings can be created here.

## BigBlueButton online meetings

Similar to the [course element BigBlueButton](../learningresources/Course_Element_BigBlueButton.md), rooms for synchronous meetings can be created here.

## Blog

Here you can create or import a [blog (learning resource)](../learningresources/Blog.md). Learners can subscribe to the central course blog.

## Wiki

Here you can create or import a [Wiki (learning resource)](../learningresources/Wiki.md). Learners can subscribe to the central Wiki.

## Forum

A central forum can be activated for a course. Course members can subscribe to the forum as usual. However, differentiated settings as in the [course element "Forum"](../learningresources/Course_Element_Forum.md) are not possible here.

## Documents

The teacher can use this link to provide important central documents of the course for download. Students can download the documents, be notified when new documents are available (subscribe) and, if required, send the files by e-mail. However, configuration options are not as extensive as in the [course element "Folder"](../learningresources/Course_Element_Folder.md).

## Course chat

A simple chat room is available as standard in every course. It is suitable for short, synchronous exchanges. Here course members can make live contact with other learners and lecturers, provided they are logged in at the same time.

If the chat is enabled, course visitors will see the link to the course chat in the middle of the course toolbar. When calling up the chat, each course member can decide whether to act under his own name or anonymously in the chat. The default setting is "anonymous".

The history of a course chat is accessible for up to one month. Above the text field, select the desired period. The Chat will be adapted when using a mobile device. Tip: Partially the portrait format is more useful than the landscape format.

!!! tip "Hint"

    If you want to use the chat more intensively, you should drag the chat window to a pleasant size.

## Glossary {: #glossary}

A glossary explains the terms of a course, subject or event to the participants. Glossaries are OpenOlat learning resources that can be used separately or integrated into a course.

The glossaries can be created as learning resources in the author area or directly in the course under "Settings-> Options".

Once a glossary has been integrated into a course, the link to the glossary will appear in the course toolbar. In order to make that glossary visible in the toolbar you have to activate the corresponding tool "Glossary" in the tab "Toolbar".

Enter the desired technical term under "Term". You can also add synonyms. For example, the term "Information Technology" can be supplemented with the synonym "IT". In the tab "Definition" you can then add the concrete definition of the term. Terms that have been entered can also be changed or deleted afterwards.

If you no longer use the glossary or want to integrate another glossary you can make the desired changes in the course or on the info page by using the drop-down menu "Course" via the menu item "[Options](../learningresources/Course_Settings.md)".

In the learning resource "Glossary" you can define in the tab "Write permission" if only owners of that learning resource are allowed to create and edit contributions or if users are granted that right as well. Owners of the learning resource "Glossary" can basically change and delete all glossary entries created. By default new glossary entries can only be made by course owners.

![](assets/glossary_add.png){ class="shadow lightbox" }

![](assets/glossary_permission.png){ class="shadow lightbox" }

If you only want to give certain people, e.g. the participants of a course, the right to write a glossary, you take a different approach. For this purpose, the "[Members management](Members_management.md)" of a course is used. Create a new group there and add the desired persons as participants to that group. Then go to "Rights" in the course's "Members management" and check the box "Glossary tool" for course participants of that group. Now persons in that group can add and modify glossary entries.

!!! info "Note"

    Per course only one glossary is allowed.

!!! warning "Attention"

    The owners of a course are not automatically also owners of the learning resource.  If someone else has created a learning resource "Glossary" he/she will not automatically become owner of the course in which that resource has been integrated. In order to enable other course owners to make modifications you have to set up one of the described permissions or you have to enter the desired course owners as owners of the learning resource "Glossary".

Furthermore, the links to the "[course info](../learningresources/Set_up_info_page.md)" and to the "[Lectures](../learningresources/Lectures_Teacher_view.md)" appear in the course toolbar.  
