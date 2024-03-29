# Communication and Collaboration
Get more info on [Virtual classrooms](../course_elements/Virtual_classrooms.md)

## Course Element: Wiki {: #wiki}
![Wiki icon](../assets/wiki_icon.png)

Use a Wiki to easily create learning content together with your course participants. A Wiki is suitable for doing group work; it can serve as documentation tool or as some sort of knowledge base for your studies and projects.

The course element "Wiki" helps you to embed a Wiki in your course. Just click on "Select, create or import Wiki" in the tab "**Wiki learning content**" to assign a Wiki already existing or to create a new one. The chapter ["Creating Wikis"](../resource_wiki/Four_Steps_to_Your_Wiki.md) will tell you how to do so step by step. If you have not already selected a Wiki yet the title **Selected Wiki** will show the message _No Wiki selected_.

If you have already added a Wiki its name will appear in the field. In order to change the assignment of a Wiki click on "Replace Wiki" in the tab "Wiki learning content" before selecting another Wiki.

In the tab "Wiki learning content" you configure the user permissions of the Wiki. Here you can set that not only owners but also maintainers and participants may edit Wiki articles. By default all course participants have read and write permission in a Wiki. Only that OpenOlat user who has created the page or OpenOlat users who are registered as owners in a wiki will be allowed to delete wiki pages.

In the chapter "Learning Activities in Courses" section ["Wiki"](../learningresources/Course_Element_Wiki.md), you will find more information on how to adapt the Wiki syntax, how to create new pages, and how to view different versions of a Wiki page.

!!! warning "Attention"

    If you can't find the "Wiki" course element in the course editor, it was disabled by a system administrator.

##  Course Element: Forum {: #forum}

![Forum icon](../assets/forum_icon.png)

With the course element "Forum" you can easily enable asynchronous online discussions for different purposes in your course. For example, course participants could write posts with questions about the content of the course and answer each other's questions, or you could initiate a technical discussion or implement specific forum-based online methods. In the chapter "Learning Activities in Courses" you will get further information on opening topics and replying to questions; see section ["Forum"](../learningresources/Working_with_Forums.md). Generally all course participants have read and write permission in a forum. All course authors and tutors dispose of the option to moderate a forum additionally.

A course author can also use the forum to notify course participants in the short term. Just configure your forum in the tab "Access" accordingly, i.e. that only course authors have write permission.

!!! tip "Tip"

    Advise your course participants on subscribing to the forum to be up-to-date.
   
### Tab Configuration
Here you can set the user rights of the forum and define which course roles are allowed to create forum posts. You can choose between coaches, participants and guests. You can also define whether coaches are allowed to moderate the forum and whether pseudonymized postings are allowed in the forum. In the case of pseudonymized forums, the posters can choose a pseudonym themselves. Once a pseudonym has been created, it will always remain active in the forum, but can be changed or switched off as required. The pseudonym can be protected by a user with a password, so that only this user can use this pseudonym. Without password protection the same pseudonym can be used by several users. Furthermore, it can be set that the use of a pseudonym is activated by default. To do this, select the checkbox "Pseudonym activated in individual forum posts".

![Configuration options for forum](assets/forum_config.png){ class="shadow" }

**Moderation rights**
All course owners and [coaches](../basic_concepts/coach.md) have the following additional moderation rights. You can:

  * Editing and deleting all posts in a forum; attaching files.
  * Prioritizing threads (sticky): a certain discussion subject will always appear on top of a list.
  * Closing discussion: it will no longer be possible to reply to a certain discussion subject.
  * Hiding discussion: a certain subject will no longer appear in the forum list.
  * Displaying discussion: hidden subject will be displayed anew.
  * Filter for persons: on the forum's overview page posts of every single course participant can be displayed.
  * Archiving forum: posts (as MS Word) and attached files will be zipped before storing them in your personal folder.

Persons with moderation rights can also move forum topics or individual posts. On the one hand, contributions can be moved to another topic of the same forum, on the other hand, entire forum topics or contributions can be moved to another forum. All forum posts underneath are moved and are no longer visible in the original forum. It is possible to move topics and posts to another forum both in the same course and in other courses. The moved thread can be created as a new discussion thread. In the last step of the move, an email can be sent to all users affected by the move, with the information where the forum is now moved to.

!!! warning "Attention"

    Forum posts can also be moved to forums in which the creator of the post has no access.

Besides the course element "Forum" there is also the possibility to display a central forum for the entire course in the [course toolbar](../learningresources/Using_Additional_Course_Features.md). Das bietet sich häufig an, wenn der Kurs nur ein Forum umfasst, das permanent zur Verfügung stehen soll. However, no further settings such as pseudonymization or assignment of moderation rights can be made here.
  
##  Course Element: File Dialog {: #file_dialog}
![File dailog icon](../assets/file_dialog_icon.png)

The course element File Dialog can be understood as a combination of forum and folder. The course element "File dialog" provides you with preset discussion forums; in contrast to an ordinary forum, dialogs here are explicitly based on certain documents. Use such a file dialog to let your course participants discuss e.g. scientific articles or papers.

In the editor in the tab "Files" or in the runtime files can be uploaded in the storage of the file dialog with "Upload file". Afterward they can be looked up and downloaded by the course participants. The related discussion forum is created automatically and opens with a click on "Show". The different columns give an overview who uploaded which file when.

Who besides the course owner can take which actions will be defined in the course editor in the user permissions of the tab "Configuration".

### Tab Configuration
Here you can set the user rights of the module and define which course roles are allowed to upload files and create discussion topics. In addition, you can define who is allowed to create forum posts in the respective discussion topics. You can choose between coaches and participants. It can also be set here whether coaches are allowed to moderate the file discussion.

![Configuration options for file dialog](assets/file_dialog_config.png){ class="shadow" }

!!! warning "Achtung"

    A discussion can only begin when a corresponding file has been uploaded.

##  Course Element: Participant folder {: #participant_folder}
![Participant folder icon](../assets/participant_folder_icon.png)


The course element "Participant folder" allows you to exchange files between
participants and coaches. With the creation of the course element there are
two folders available. On one side this is the drop box where participants can
upload files for the coaches. On the other side it is the return box where
coaches can upload files for all participants together or individually.
Im Prinzip verbergen sich hinter diesem Kursbaustein zwei (Kursbaustein) Ordner einmal mit Schreibberechtigung und einmal ohne, die jedoch nur für Betreuende und einen einzelnen Teilnehmer sichtbar sind. 

!!! info

    A similar configuration of file delivery + file return by coaches can also be     implemented with the course element ["Task"](Course_Element_Task.md), only that the possibilities of the task element are much more comprehensive and complex and here also an evaluation or allocation of points can be made.
The course element "Participant folder" allows you to exchange files between participants and coaches. With the creation of the course element there are two folders available. On one side this is the drop box where participants can upload files for the coaches. On the other side it is the return box where coaches can upload files for all participants together or individually.

### Folder settings
In the folder settings configurations for the drop box and the return box can be made. By default both folders are enabled and delete and override is enabled for the participants. For the drop box some more configurations can be made.

Delete and override can be unenabled. This means that the participants cannot delete any files. Uploaded files stay in the drop box coercively. Further a time interval can be defined. The upload in the drop box is only possible in this time frame. Out of this time frame files can only be downloaded.

If the participant's folder is activated, the participants can upload files or create them directly in OpenOlat. If the administrator of the OpenOlat instance has activated further document editors, it is also possible to create further file formats such as Word, Excel or PowerPoint files.
In the folder settings configurations for the drop box and the return box can
be made. By default both folders are enabled and delete and override is enabled for the participants. 

Additionally the number of files can be limited. As soon as this number is reached no writing tools are available anymore. This means that uploaded files cannot be moved, copied, zipped or unzipped anymore. But they can be deleted, if this option is enabled. If desired only the drop box or only the return box can be enabled.

In the Template Settings tab, subfolders can also be created for both the Submission and Return folders to create a continuous folder structure. For example, a return folder could include a subfolder for content feedback and one for supplemental files, or a submission folder could reflect some desired structure for the submissions. 
  

!!! warning "Attention"

    As for all upload areas, there is a memory limit for the participant folder. The file upload limits set by the administrator and the entire folder limit are displayed when you try to upload a file.


### Tab Template Einstellungen

In the Template Settings tab, subfolders can be created for both the submission folder and the return folder, creating a continuous folder structure for all participants. For example, a return folder could include a subfolder for content feedback and one for supplemental files, or a submission folder could reflect some desired structure for the submissions. 

!!! warning 

    The subfolders created here cannot be renamed later. Only a deletion and a new creation is possible. In the course run, when you try to rename these subfolders, copies of the subfolders with new names will be created.


##  Course Element: Participant list {: #participant_list}
![group.png](../assets/participant_list_icon.png)

In the participant list, the members of the course can be made visible to everyone. Unlike the [member management](../learningresources/Members_management.md) course tool, which is only visible for course owners, the course element "Participant list" provides a list of all course members to those OpenOlat users allowed to open the respective course. Members are listed depending on their role within the course as either course administrator, coach or participant. Select the user groups to be displayed to course users.

![Configuration options for paricipant list](assets/participant_list_config.png){ class="shadow" }

By linking the member names to their OpenOlat visiting card as well as the
OpenOlat mail service, this course element facilitates contacting your fellow
course members directly from within the course. In the course editor you can
determine whether the e-mail function should be available for all course
participants or just for course owners and coaches. Use the "Send e-mail"
button in the course view to send mails to multiple user (groups). If
required, external mail addresses can also be added.

The course view also offers, apart from the mail function, the online instant
messaging status of listed course participants. A click on the status icon
opens the chat window.

Finally it can be defined, who is allowed to download the participant list as
Excel or to print it. Again it is differentiated between coach and owner or
all users.

!!! info 

    A similar function is available in the toolbar with the "List of participants" tool. However, no further configurations can be made here.   

  

By linking the member names to their OpenOlat visiting card as well as the OpenOlat mail service, this course element facilitates contacting your fellow course members directly from within the course. In the course editor you can determine whether the e-mail function should be available for all course participants or just for course owners and coaches. Use the "Send e-mail" button in the course view to send mails to multiple user (groups). If required, external mail addresses can also be added.

The course view also offers, apart from the mail function, the online instant messaging status of listed course participants. A click on the status icon opens the chat window.

Finally it can be defined, who is allowed to download the participant list as Excel or to print it. Again it is differentiated between coach and owner or all users.