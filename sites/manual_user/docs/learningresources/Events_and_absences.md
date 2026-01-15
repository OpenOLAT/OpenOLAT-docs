# Events and absences {: #course_admin_events_and_absences}

Absence management allows attendance lists to be kept online and absences to be documented. Attendance is monitored on a course-by-course basis.

For this purpose, **events** can be created in the course, which can be divided into several **units**. For example, a morning (events) can be divided into several time blocks (units). This makes it possible for participants to be marked as absent for individual units of an event without losing the entire event.

Dates and units are either created by the course owners themselves or synchronized with OpenOlat via an external administration system. All events also appear in the course calendar, provided the course includes a calendar.

Before absence management can be used, it must be activated by the course owner. This can be done under Administration > Settings > Implementation tab. After activation, further settings can be made, and the "Events" option will appear in the toolbar.



## "Events" in the toolbar {: #toolbar_events}

**Course owners** can "add events" and organize absences here. In addition, the "Events and absences" menu appears for course owners in the course administration. The options are largely identical. 

![events_and_absences_adminmenu_v1_de.png](assets/events_and_absences_adminmenu_v1_de.png){ class="shadow lightbox" }

**Course administrators** only see the "Dates" menu in the toolbar, not in the course administration. They also cannot create new dates, only view existing ones and, if activated, record absences. It is also possible to filter by dates for which you are registered as an administrator.   

![events_and_absences_toolbar_for_coach_v1_de.png](assets/events_and_absences_toolbar_for_coach_v1_de.png){ class="shadow lightbox" }

**Participants** see the "Events" menu in the toolbar and can quickly identify synchronous face-to-face or online events, e.g., in the context of blended learning. 

![Teilnehmersicht Toolbar Termine](assets/TN_Termine_Absenzen.jpg){ class="shadow lightbox" }

Participants can find their personal absences under "Personal Tools" in the [Absences menu](../personal_menu/Absences.md).

[To the top of the page ^](#course_admin_events_and_absences)

---

The following section describes in more detail how **course owners** can view dates and absences. 


## Tab Events {: #tab_events}

![Menü Termine für Kursbesitzernde](assets/Termine_Kursbesitzende_20.png){ class="shadow lightbox" }

### Display events {: #display_events}

In the "Events" tab, dates can be added to the course and displayed filtered according to various criteria. If, for example, the date has been assigned to subject areas (taxonomy), it can be filtered according to these. To view details about a date, click on the + at the beginning of the relevant line.

In the 3-point menu at the end of each line, you will find additional options for an event. Here you can edit, copy, delete, mark as a test, create PDF lists, and generate additional downloads for the event. Completed events can also be reopened.


![events_and_absences_tab_events_v1_de.png](assets/events_and_absences_tab_events_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#course_admin_events_and_absences)

---

### Create/Edit event {: #edit_events}

To add further events, use the "Add event" button at the top right above the list in the "Events" tab.

![events_and_absences_tab_events_create1_v1_de.png](assets/events_and_absences_tab_events_create1_v1_de.png){ class="shadow lightbox" }

A pop-up window will open for you to enter all the details for the event.

![events_and_absences_tab_events_create2_v2_de.png](assets/events_and_absences_tab_events_create2_v2_de.png){ class="shadow lightbox" }

**Title**: Give it a meaningful name.

**Characteristic**: The optional specification of a label serves to distinguish between events with the same title.

**Date**: A date must be specified.

**Time**: The time field is also mandatory. This is because calendar entries, for example, can only be displayed correctly if a time is specified.

**Unit**: This specifies how many (time) units this event comprises.<br>
An event can comprise 1–12 units.<br>
Example: An event lasts 2 hours, divided into 4 thematic units (4 x 0.5 hours).

**Place**: This is where you specify where this event will take place. This could be a location or the exact room name, for example.

**Online Meeting**: If the event is to take place online, the meeting can be organized directly from here. You have the option of starting a BigBlueButton, Teams or, for example, Zoom meeting from an event and also accessing it later via "Events".
The online meeting takes over people and descriptions from the event (people, title, time, etc.).
Learners can access it via the calendar or the "Events" icon in the toolbar.

**Subjects**: Here you can assign the event to one or more terms from a stored taxonomy. This makes it easier to find the event later.

**Lecturers**: A course coach must be selected for each event. Only the selected course coach can carry out attendance checks. (Only a person who also has the role of "Coach" can be added as a lecturer.) If a course owner also wishes to take on this role, they must additionally register as a course coach for the course.

**Description**: Here you can optionally add a description for the event.

**Preparation/Follow-up**: If you would like to give participants a pre- or post-assignment for the respective event, you can add it here. It will be displayed in the calendar if the dates are synchronized with the course calendar (Course Administration > Settings > Implementation tab).

**Presence**: If the switch is set to "Off," absence recording is deactivated.

[To the top of the page ^](#course_admin_events_and_absences)

---


### Copy or delete events {: #copy_delete_events}

As soon as at least one event is selected in the first column, buttons for copying and deleting events appear above the list of events.<br>
Alternatively, the options for copying and deleting can be accessed via the three dots at the end of a line.

![events_and_absences_tab_events_copy_v1_de.png](assets/events_and_absences_tab_events_copy_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#course_admin_events_and_absences)

---


### Import events {: #import_events}

It is also possible to import events that have been exported elsewhere in OpenOlat. To do this, click on the small arrow next to the "Create event" button in the "Events" tab.

![events_and_absences_tab_events_import_v1_de.png](assets/events_and_absences_tab_events_import_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#course_admin_events_and_absences)

---


### Cancel events {: #cancel_events}

Events can be canceled using the [event icon in the toolbar](../learningresources/Toolbar_Events.md#cancel_events).

[To the top of the page ^](#course_admin_events_and_absences)

---


### Close events {: #close_events}

Events are closed using the [appointment icon in the toolbar](../learningresources/Toolbar_Events.md#close_events).

[To the top of the page ^](#course_admin_events_and_absences)

---

### Reopen events {: #reopen_events}

A completed event can be reopened by course owners. You will find the option under the three dots in the row of an appointment.

![events_and_absences_reopen_event1_v1_de.png](assets/events_and_absences_reopen_event1_v1_de.png){ class="shadow lightbox"}

[To the top of the page ^](#course_admin_events_and_absences)

---

### Manage teachers {: #manage_teachers}

As soon as at least one date is selected in the first column, the button for managing teachers appears above the list of events.

![events_and_absences_tab_events_teachers1_v1_de.png](assets/events_and_absences_tab_events_teachers1_v1_de.png){ class="shadow lightbox" }

![events_and_absences_tab_events_teachers2_v1_de.png](assets/events_and_absences_tab_events_teachers2_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#course_admin_events_and_absences)

---


### Exclude Participants {: #exclude_participants}

When you open the detailed view of an event (by clicking on the + at the beginning of the relevant line), an icon with three dots is displayed at the bottom. There you will find the option to exclude participants from the selected event.

![events_and_absences_tab_events_exclude_participants_v1_de.png](assets/events_and_absences_tab_events_exclude_participants_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#course_admin_events_and_absences)

---


## Tab Participants {: #tab_participants}

The "Participants" tab provides an overview of all participants in the course or selected groups. (Excluding owners and coaches.)

![events_and_absences_tab_participants1_v1_de.png](assets/events_and_absences_tab_participants1_v1_de.png){ class="shadow lightbox" }

**Initial registration**<br>
The date of initial registration defines when participants started the course.

**Units**<br>
Here you can see how many units this event comprises.

**Present**<br>
The "Present" column calculates the attendance rate for events that have already taken place. For example, if only one event has taken place and the participant was present, 100% will be displayed in the "Attendance" column.<br>
The attendance rate is calculated based on the date of initial registration. Events that took place before the date of initial registration are not included in the calculation.

**Unexcused**<br>

**Excused**<br>

**Dispensed**<br>

**Progress**<br>
Progress is displayed graphically. Green symbolizes attendance, orange symbolizes excused absences, and red symbolizes unexcused absences or missed events.

![attention-icon](assets/attention_434343_64.png){class="size24"}<br>
The attention column with the symbol indicates whether the defined attendance rate has been achieved. If a red exclamation mark is displayed, the required limit has not been reached.

![info](assets/infomessage.png){class=“size24”}<br>
The info column displays information that deviates from the default settings. This could be a personal threshold value or a later course start date, for example. These two options can be defined in the settings (pencil icon). The personal threshold value defines the attendance rate to be achieved for the participant(s) in question. 

[To the top of the page ^](#course_admin_events_and_absences)

---


### Customize the threshold for mandatory attendance {: #personal_rate}

The threshold value for compulsory attendance set for the course can be adjusted individually. To do this, select the relevant person in the Participants tab and click on the edit icon.

![events_and_absences_tab_participants_personal_rate_v1_de.png](assets/events_and_absences_tab_participants_personal_rate_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#course_admin_events_and_absences)

---



## Tab Appeals {: #tab_appeals}

If appeals have been submitted, you can get an overview under this tab as the course owner. Filters help you when there are a large number of appeals.

![events_and_absences_tab_appeals1_v1_de.png](assets/events_and_absences_tab_appeals1_v1_de.png){ class="shadow lightbox" }

Appeals are usually processed by absence administrators, who can access all appeals across courses in the central [cross-course absence management system](../area_modules/Absence_Management.md).

[To the top of the page ^](#course_admin_events_and_absences)

---


## Further information {: #further_information}

[Basic concept Events and Absences >](../basic_concepts/Events_and_Absences.md)<br>
[Activation and configuration of absence management by administrators >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Configuring absence management in a course >](../learningresources/Course_Settings_Execution.md#config_event_and_absence_management)<br>
[Registering and managing absences in a course by coaches>](../learningresources/Toolbar_Events.md)<br>
[Personal absences >](../personal_menu/Absences.md)<br>
[Cross-course absence recording in the coaching tool >](../area_modules/Coaching.md)<br>
[Cross-course absence management by absence administrators>](../area_modules/Absence_Management.md)<br>

[To the top of the page ^](#course_admin_events_and_absences)





