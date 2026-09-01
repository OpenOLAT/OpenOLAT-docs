# Events and Absences {: #events_and_absences}

## What types of events are there in OpenOlat? {: #event_types}

There are basically two types of events in OpenOlat:

- Basic events (entries in calendars)
- Events with additional options: They appear in [Courses](../learningresources/Events_and_absences.md), in the [Course Planner](../area_modules/Course_Planner.md), and in [Absence Management](../area_modules/Absence_Management.md).
These events can be linked to online meetings, and it is possible to record absences. Coaches can also be scheduled for these events. (Note: Only coaches can be designated as teachers.)<br>
Events with additional options can have the status "Scheduled", "Running", "Done" or "Cancelled".<br>
If you do not have the necessary permissions, your view of events may be restricted. 


|                           | Basic event | Event with additional options |
| ------------------------- |:-----------------:|:--------------------:|
|[Events in courses](../learningresources/Events_and_absences.md#edit_events)|   |x|
|[Events in course element appointment scheduling](../learningresources/Course_Element_Appointment_Scheduling.md)|   |x|
|[Events in Course Planner](../area_modules/Course_Planner_Events.md)|   |x|
|[Events in the Absence management](#access_absences)|   |x|
|[Events in Projects](../area_modules/Project_Schedule.md)| x |  | 
|[Events in (Project) To-dos](../area_modules/Project_Schedule.md)| x |  | 
|[Events in Personal Menu](../personal_menu/To-Dos.md)| x | x | 
|[Events in Calendars](../personal_menu/Calendar.md#create_entry)| x |  | 
|[Events in BigBlueButton](../../manual_admin/administration/BigBlueButton_module.md#tab_online-meetings)| x |  | 
|[Events in Microsoft Teams](../learningresources/Course_Element_Microsoft_Teams.md#raum-konfigurieren-bei-geschlossenem-kurseditor)| x |  | 

[To the top of the page ^](#events_and_absences)

---

### Which events (with additional options) are displayed? {: #event_conditions}

The visibility of events generally depends on

- whether the “Events/Absences” module is globally enabled in the administration panel
- whether the “Events” focus element is displayed
- whether there are actually any relevant events
- whether the event should be visible to the role

[To the top of the page ^](#events_and_absences)

---

### Where are the events with additional options displayed? {: #event_display}

Participants can view their events in the **Toolbar** of the course under the "Events" icon. They only see their own events and cannot record absences.

Events are also displayed on the various **dashboards** of the coaches.

**Event widgets** are available on the overview pages, such as those in the Coaching Tool and the Course Planner.

Which information an event list contains depends on the area:

- In the **Course Planner** the list serves the planning. There is no absence management there.
- In the **Coaching Tool** coaches see the events of all their courses and also record the absences there.
- In the **Toolbar of a course** participants only see their own events with the information relevant to them.

[To the top of the page ^](#events_and_absences)

---

### What statuses can events have in OpenOlat? {: #event_status}

Events with additional options (e.g., in the Course Planner or Coaching Tool) have one of the following status values:

- Scheduled
- Running
- Done
- Cancelled

The next upcoming event carries the label "Scheduled next" instead of "Scheduled".

In the event lists, the status is shown in the "Status" column.

[To the top of the page ^](#events_and_absences)

---


## Which absences can be administrated? {: #administrated_absences}

!!! info "General note"

    Administrators can configure the settings in [Absence Management](../area_modules/Absence_Management.md) in great detail. If any of the options described are not available to you, please contact your administrator.

!!! info "General note"

    In OpenOlat, absences are recorded as a matter of principle, not attendance.


### Absences {: #absences_categories}

The presence or absence of participants can be recorded in the following categories:

- Present
- Excused absence
- Unexcused absence
- Dispensed

Absences are usually recorded during attendance checks by the **coaches**.

**Participants** can find their recorded absences in the [personal menu](../personal_menu/Absences.md).

An **attendance rate** is calculated from the recorded absences. By comparing this with a specified permitted **absence rate** (e.g., 80%), it can be calculated whether a course can be considered attended.

### Cancellations {: #abcenses_cancellations}

Participants may be allowed to sign out in advance in the [personal menu](../personal_menu/Absences.md#tab-sign-out-dispense).

### Excused Absences {: #excused_absences}

It can be set system-wide that excused absences are counted as "present" for the calculation of the attendance rate.

### Dispense {: #dispensations}

There are various reasons why a participant may not be able to or required to attend a specific part of a course. In this case, an exemption can be arranged.

### Appeals {: #appeals}

Participants have the opportunity to appeal against a decision made by coaches, e.g., a supposedly unexcused absence. Appeals are also recorded in OpenOlat.

[To the top of the page ^](#events_and_absences)

---


## Where can I find the absence management? {: #access_absences}

A distinction must be made between

1. the **general activation and configuration** of absence management by administrators in the system administration at:<br>
   `Administration > Module > Events and absences`<br>
   [More about that >](../../manual_admin/administration/Modules_Events_and_Absences.md)


2. the **configuration** of absence management in a **course**<br>
    The configuration of the event and absence management for a specific course is done by the course owners in the course administration:<br>
    `Course > Administration > Settings > Tab "Execution" > Section "Configuration event and absence management in course"`<br>
    [More about that >](../learningresources/Course_Settings_Execution.md#config_event_and_absence_management)


3. the **recording and management** of absences in a **course** by **course owners**<br>
    Recording and administration is carried out in Run Mode (i.e., at runtime, not in the editor) by course owners at:<br>
    `Course > Administration > Events and absences > Tab "Participants"`<br>
    [More about that >](../learningresources/Events_and_absences.md)

4. the **recording and management** of absences in a **course** by **coaches**<br>
    Recording and administration by coaches takes place at:<br>
    `Toolbar > Events`<br>
    [More about that >](../learningresources/Toolbar_Events.md)

5. the overview of **personal absences**<br>
    You and all participants can find your personal absences in your personal menu. Here, administration is only possible to a limited extent and for yourself, e.g., in the form of deregistration.<br>
    [More about that >](../personal_menu/Absences.md)


6.  the **cross-course absence recording** by coaches<br>
    Coaches can find the option to record absences in various courses in the<br>
    `Coaching tool > Button "Events/Absences"`<br>
    [More about that >](../area_modules/Coaching.md)


7. **cross-course absence management** by authorized persons with the role of absence administrator:.<br>
    Administration includes, for example, processing exemptions and appeals. This administrative task goes beyond simple data entry and is therefore assigned to a separate role. Authorized users can find the tools in the<br>
   `Header menu > Absence management`<br>
   [More about that >](../area_modules/Absence_Management.md)

[To the top of the page ^](#events_and_absences)

---


## Further information {: #further_information}

[Activation and configuration of absence management by administrators >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Configuring absence management in a course >](../learningresources/Course_Settings_Execution.md)<br>
[Recording and managing absences in a course by course owners >](../learningresources/Events_and_absences.md)<br>
[Recording and managing absences in a course by coaches >](../learningresources/Toolbar_Events.md)<br>
[Personal absences >](../personal_menu/Absences.md)<br>
[Cross-course absence recording in the coaching tool >](../area_modules/Coaching.md)<br>
[Cross-course absence management by absence administrators >](../area_modules/Absence_Management.md)<br>


[To the top of the page ^](#events_and_absences)

---