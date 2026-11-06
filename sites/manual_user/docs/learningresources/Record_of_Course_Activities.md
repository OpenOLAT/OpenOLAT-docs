# Record of Course Activities {: #record_of_course_activities}

If you want to understand how a course is used, evaluate the log files: OpenOlat records the course activities of the participants and the course authors in them.

Within a course, you archive the log files in the [Archiving & Reporting](../learningresources/Course_Archiving.md) tool [:octicons-tag-16:{ title="from Release 21.0 (OO-9620)" }](https://track.frentix.com/issue/OO-9620) under:<br>
`Course > Administration > Archiving & Reporting > Log files`

The following log files are available:

* Admin log file, shown as "Administrator's log file (personalized activities of course authors)", with personalized data of the course authors
* Statistics log file, shown as "User's log file (anonymous activities of users)", with pseudonymized data of the participants
* Participants log file, shown as "User's log file (personalized, detailed activities of all users)", with detailed, personalized data of the participants

Owners of the course as well as learning resource managers and administrators of the organisation the course belongs to can archive log files. Owners and learning resource managers choose between the admin log file and the statistics log file. The course right "Archive tool" opens the Archiving & Reporting tool, but not the log files. Persons who only have this course right see the message "You have no rights to archive log files." under Log files.

Use the fields "from" and "to" to limit the log files to a period; both fields are optional. The period includes the day in the "to" field. With "Archive", OpenOlat creates the selected log files and notifies you by e-mail as soon as the ZIP file is ready. The image shows the selection as owners see it.

![Choice between the admin log file and the statistics log file, statistics log file selected, period from and to set](assets/course_archive_reports_logfiles_v2_en.png){ class="shadow lightbox" title="Log files in the Archiving & Reporting tool · 2026.10.02" }

!!! info "Privacy protection"

    For privacy reasons, the participants log file with the personalized data of the participants is only available to administrators of the organisation the course belongs to.

OpenOlat stores the selected log files as a ZIP file (e.g. _CourseLogFiles_2010-01-28_14-55-55.zip_) in the [personal files](../personal_menu/File_Hub.md#personal_files) in the folder `private/archive/"Course title"`. The ZIP file then contains the selected files _course_statistic_log.xlsx_, _course_admin_log.xlsx_ and _course_user_log.xlsx_.

In the file _course_statistic_log.xlsx_, each participant receives an identifier of 32 characters instead of their name (e.g. `e1c7eafdebc3c103fb8959e186326363`), which remains the same within a course. This allows you to track the activities of participant X in course Y, but not to compare them with their activities in course Z, since participant X receives a different identifier in course Z. The identifier is a pseudonym: combined with other information, such as the time of a forum post, it can be linked to a person. Therefore, treat the file as personal data.

The table groups the possible entries of the log file columns "actionCrudType" (database operation), "actionVerb" (action) and "actionObject" (course object handled) alphabetically:

actionCrudType| actionVerb| actionObject
---|---|---
c | add | calendar, chat, course, cpgetfile
r | copy | editor, efficency
u | denied | feed, feeditem, file, folder, forummessage, forumthread
d | do | glossary, gotonode, groupmanagement, group, grouparea, groupareaempty
e | edit | help
|  | exit | layout
|  | hide | node
|  | launch | owner
|  | lock | participant, publisher
|  | move | quota
|  | open | resource, rights, rightsempty
|  | remove | sharedfolder, spgetfile
|  | view | testattempts, testcomment, testid, testscore, testsuccess, tools, toolsempty
|  |  | waitingperson

The column "actionCrudType" groups the actions into basic database operations. For an evaluation, the column "actionVerb" is usually sufficient, as it breaks these operations down further. The values of the column "actionCrudType" mean:

* c = create
* r = retrieve
* u = update
* d = delete
* e = exit

The column "actionVerb" shows which action the person from the column "userName" performed on the course object. The column "actionObject" names this course object, that is, the object that was changed from the database perspective. The columns "parentResName" and "targetResName" name the parent object and the object the action is aimed at.

![Sample entries with the columns creationDate, userName, actionCrudType, actionVerb, actionObject, parentResName and targetResName](assets/course_statistic_log.gif){ class="shadow lightbox" title="Statistics log file course_statistic_log.xlsx" }

An example is the third row in the image:

`u / add / participant / [group name] / [username]`

It means, with the database operation update:

`Add user [username] to [group]`

## Further information {: #further_information}

[Course administration - Archiving & Reports >](../learningresources/Course_Archiving.md)<br>
[User tools: File Hub >](../personal_menu/File_Hub.md)<br>
[Members management >](../learningresources/Members_management.md)

[To the top of the page ^](#record_of_course_activities)
