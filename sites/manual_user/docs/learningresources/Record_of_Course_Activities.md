# Record of Course Activities {: #record_of_course_activities}

OpenOlat records course activities of participants and course authors in log files.

Within a course, the following log files can be downloaded via [data archiving](../learningresources/Course_Archiving.md):

* Admin log file with personalized data of the course authors
* Statistics log file with the anonymized data of the participants
* Participants log file with detailed, personalized data of the participants

![Log file selection with date range and "Archive" button in the "Archiving & Reports" area of the course administration](assets/log_files.png){ class="shadow lightbox" }

!!! info "Privacy protection"

    For privacy reasons, the participants log file with the personalized data of the participants is only available to system administrators.

Course owners and other persons who have the right to archive can save the desired log files as a ZIP file (e.g. _CourseLogFiles_2010-01-28_14-55-55.zip_) in their [personal files](../personal_menu/File_Hub.md#personal_files). The ZIP file then contains the selected files _course_statistic_log.xlsx_, _course_admin_log.xlsx_ and _course_user_log.xlsx_.

Please note that in the file course_statistic_log.xlsx the participants are anonymized as follows:<br>
Each participant receives a randomly generated number (e.g. *7FFBA8C371B1A3DACCF5F12227A75CE82D6C4CE6), which remains constant within a course. This allows you to track the activities of participant X in course Y, but not to compare them with their activities in course Z, since participant X receives a new number in course Z.

Possible entries in the log file columns **actionCrudType** (database operation), **actionVerb** (action) and **actionObject** (course object handled) (grouped alphabetically):

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

The column **actionCrudType** summarizes the actions performed in basic database operations. Since these are further broken down in the actionVerb column, actionCrudType is not further relevant.

Nevertheless, here is the key:

* C=Create
* R=Read / Retrieve
* U=Update / Modify
* D=Delete
* E=Exit

The column **actionVerb** then examines in more detail which action the users under "userName" performed on the course object from the actionObject column. The entry in the **actionObject** column is thus the object that was "changed", at least from a database perspective.

![Sample entries of the statistics log file with the columns creationDate, userName, actionCrudType, actionVerb and actionObject](assets/course_statistic_log.gif){ class="shadow lightbox" }

The third row

`u / add / participant / [group name] / [username]`

is read as follows (database operation: update / modify):

`Add user [username] to [group]`

## Further information {: #further_information}

[Data archiving >](../learningresources/Course_Archiving.md)<br>
[Details on the File Hub >](../personal_menu/File_Hub.md)

[To the top of the page ^](#record_of_course_activities)
