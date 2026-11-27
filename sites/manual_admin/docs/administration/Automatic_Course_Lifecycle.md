# Automatic Course Life Cycle {: #course_lifecycle}

Anyone who runs many courses wants to finish old courses in an orderly way after the course end, move them to the trash and finally delete them permanently, without handling each course individually. The automatic course life cycle does this in a daily run according to the periods you define. Before you save a configuration, OpenOlat shows in a confirmation dialog how many courses it sets to which step. Afterwards you see in the section "Life cycle process" what is running at the moment and what is due in the coming days.

System administrators configure it in the system administration under:<br>
`Administration > Life cycles > Courses`

![Courses are automatically finished, moved to the trash and permanently deleted after the course end, depending on the period; before saving, a confirmation shows the number of affected courses](assets/automatic_course_lifecycle_stages_v1_en.svg){ class="lightbox" title="Life cycle of a course" }


## The three steps {: #steps}

A course leaves operation in three steps, so that a mistake can be undone up to the last step. You switch on each step individually, and each step has its own period.

* **1 Finished**<br>
  "Finished" is a status of the course: the execution is completed, but the course remains in place with its members. Which access participants have to a finished course is defined by a system-wide setting in the [Module Learning resource, Access tab](Modules_Learning_Resource.md#tab_accesss): Read-only or No access. It can be overridden per course under `Course > Administration > Settings > Tab "Options"`. A finished course can be set back to an earlier status, for example "Published".

* **2 Trash**<br>
  In the trash, the course is deleted but still present. OpenOlat removes the coaches, participants and persons on the waiting list, the owners remain registered. The course appears with the status "Trash" under `Authoring > Deleted` and can be restored from there. In the section "Life cycle process", this step is called "Deleted".

* **3 Permanently deleted**<br>
  The last step deletes the course including its data. Afterwards it cannot be restored.


## Configuration {: #configuration}

With the configuration you define which steps the daily run carries out and how long a course waits before each step. The form "Automatic Life-cycle management" contains three checkboxes for this, one per step. As soon as you select a checkbox, a whole number as a mandatory field and a unit appear behind it: Day, Week, Month or Year.

![Switch on the steps Finished, Delete (Trash) and Delete permanently, each with a checkbox, and set the period made of number and unit behind it](assets/automatic_course_lifecycle_config_v2_en.png){ class="shadow lightbox" title="Form Automatic Life-cycle management under Administration > Life cycles > Courses · 2026.11.27" }

* **Finished**<br>
  The checkbox carries the text "change to finished (read only, keep user access)". Which access participants actually have afterwards is defined by the setting for the status "Finished", see [The three steps](#steps). The period counts from the course end ("after the course ends").

* **Delete (Trash)**<br>
  The checkbox carries the text "change to deleted (remove participants, put into trash)". The period also counts from the course end ("after the course ends").

* **Delete permanently**<br>
  The checkbox carries the text "all data is deleted and cannot be restored". The period counts from the day on which the course was moved to the trash ("after the course has been deleted").

The course end is the end date of the execution period in the [Course Settings, Tab Execution](../../manual_user/learningresources/Course_Settings_Execution.md#execution_period). The run does not include courses without an end date. The run includes a course on the day on which its end date plus the period is reached: with "Finished" and a period of 2 weeks, the run sets a course with the end date 13 November to "Finished" on 27 November.

The run sets courses with the status "Preparation", "Review", "Access for coach" or "Published" to "Finished" when their end date plus period has been reached. It moves courses with these statuses and with the status "Finished" to the trash when their end date plus period has been reached. It permanently deletes all learning resources in the trash whose deletion date plus period has been reached, not only courses: also tests, files or course templates that someone has deleted manually. A learning resource that another learning resource still refers to remains in the trash. The run does not set course templates to "Finished" and does not move them to the trash. The run does not include learning resources under external management where an external tool controls finishing or deleting.

So that owners learn when someone finishes or deletes their course manually, the form "Notification after closing / deleting a course" follows below the form "Automatic Life-cycle management". It contains the checkbox "Notify owners about status changes" in the row "Enforce E-mail notifications". The setting takes effect when someone finishes or deletes a course manually, in the authoring area as well as in the course itself: in the confirmation dialog the checkbox for notifying the owners is preselected, and only system administrators can deselect it. The automatic run itself changes the status without sending an e-mail.


## Saving with confirmation and preview [:octicons-tag-16:{ title="from Release 21.0 (OO-9588)" }](https://track.frentix.com/issue/OO-9588) {: #confirmation}

A new configuration can include many courses at once in its first run. That is why OpenOlat shows what it causes before saving. If at least one step is switched on, the button "Save" opens the dialog "Save the lifecycle configuration" with the note: "The lifecycle process starts immediately after saving. The next time the process runs, the courses listed below will be processed automatically."

Under "Impacts", there is one line for each step switched on, with the number of affected courses, for example "12 courses are moved to the trash. Participants are removed. Courses can be restored." OpenOlat calculates the numbers for the configuration you have just entered, before it is saved.

![Marked list Impacts with the number of courses per step (5 Finished, 9 trash, 182 permanently deleted), below it Confirmation and Save and start](assets/automatic_course_lifecycle_confirmation_v2_en.png){ class="shadow lightbox" title="Dialog Save the lifecycle configuration" }

!!! warning "Attention"
    The process starts immediately after you confirm, and in its first run it processes all courses whose period has already passed. On an instance with many old courses, hundreds of courses can land in the trash or be permanently deleted in one go, and the participants lose their access. Check the numbers under "Impacts" before you confirm. If in doubt, switch on only the step "Finished" first and add the other steps once the result is correct.

To save, select the checkbox "I understand the implications and would like to start the lifecycle process with this configuration." under "Confirmation" and click "Save and start". Without this checkmark, the dialog reports "Please confirm." and saves nothing. After the confirmation, OpenOlat saves the configuration and starts the process immediately. If a process is already running, OpenOlat stops it and restarts it with the new configuration.

With "Cancel" or by closing the dialog, OpenOlat saves nothing. The form keeps your entries, so that you can adjust the periods and save again. If all three steps are switched off, OpenOlat saves without a dialog.


## Life cycle process: status and preview [:octicons-tag-16:{ title="from Release 21.0 (OO-9590)" }](https://track.frentix.com/issue/OO-9590) {: #status}

!!! info "frentix customers"
    The daily start time of the run is part of the server configuration and applies after a change only from the next restart of OpenOlat. For frentix customers, their customer advisor at frentix takes care of the change.

After saving, you want to know whether the process is running, how far it has got and what lies ahead for the courses in the coming days. This information appears above the form in the section "Life cycle process", divided into three parts.

![The displays per step count the progress of the run as x of N, and the expanded preview table shows how many courses each step includes in the next run, the next 7 and the next 30 days](assets/automatic_course_lifecycle_status_v3_en.png){ class="shadow lightbox" title="Section Life cycle process under Administration > Life cycles > Courses · 2026.11.27" }

* **Configuration overview**<br>
  "Active sub-processes" names the steps switched on, for example "Finished | Deleted | Delete permanently". "Execution time" names the daily start time of the run, by default "Every day at 5:45 AM". "Next run" names the date and time of the next run, followed by the number of courses it affects. "Last run" names the previous run.

* **Process run**<br>
  The label "Running" or "Scheduled" shows whether the process is working at the moment or waiting for its next start. The three displays "Finished", "Deleted" and "Delete permanently" count the progress per step as "x of N" with a progress bar: N is the number of courses the run processes in this step, x the number already processed. When no run is working, x is 0 and N names the courses of the next run. For a step that is switched off, a dash appears.

* **Preview**<br>
  The table is collapsed and opens with a click on "Preview". For the saved configuration, it counts how many courses each step switched on includes, in the rows "Next run", "Next 7 days" and "Next 30 days". The columns are called "Period", "Finished", "Deleted", "Delete permanently" and "Total".

### Controlling a running process [:octicons-tag-16:{ title="from Release 21.0 (OO-9589)" }](https://track.frentix.com/issue/OO-9589) {: #stop_process}

If you notice during a run that a period is set incorrectly, correct or stop the process without waiting for the end of the run. If you save a changed configuration, OpenOlat stops the running process and restarts it with the new configuration, so a corrected period takes effect immediately. In addition, before each single course the process checks whether the step is still switched on. If you switch a step off, this step stops at the next course instead of processing the old setting to the end. The other steps switched on continue.

Using the button "Stop process" in the part "Process run", you stop the current run immediately, without changing the configuration and without a restart. This gives you time to check the periods calmly. The button is only active while a process is running. The next scheduled run processes the remaining courses.


## Life cycle in the authoring area {: #authoring}

Anyone who wants to get back a course that the run has moved to the trash finds it in the authoring area. It appears with the status "Trash" under `Authoring > Deleted` and can be restored. The execution period remains unchanged: adjust the end date after restoring, otherwise the next run moves the course back to the trash. Administrators and learning resource managers can delete it permanently there. The individual steps are described on the page [Delete (a course or learning resource)](../../manual_user/learningresources/Course_Delete.md) and in the guide [How do I manage lifecycles of groups, courses or user accounts?](../../manual_how-to/lifecycle/lifecycle.md#course_lifecycle).

!!! warning "Attention"
    "Restore" brings back the course with its content, with the status "Finished". Already when the course is moved to the trash, OpenOlat removes the members other than the owners, the links to groups and to elements in the Course Planner, the catalog entries, the "Offer for guests" and the offers "Without booking". These do not come back. The details are listed under [What deleting removes](../../manual_user/learningresources/Course_Delete.md#removed_on_delete).


## Further information {: #further_information}

**Mentioned on this page**<br>
[Module Learning resource >](Modules_Learning_Resource.md)<br>
[Course Settings - Tab Execution >](../../manual_user/learningresources/Course_Settings_Execution.md)<br>
[Delete (a course or learning resource) >](../../manual_user/learningresources/Course_Delete.md)<br>
[How do I manage lifecycles of groups, courses or user accounts? >](../../manual_how-to/lifecycle/lifecycle.md)

**Further reading**<br>
[Life cycles - Overview >](Life_cycles_-_Administration/index.md)<br>
[Automatic Group Life Cycle >](Automatic_Group_Lifecycle.md)<br>
[Authoring - Overview >](../../manual_user/area_modules/Authoring/index.md)

[To the top of the page ^](#course_lifecycle)
