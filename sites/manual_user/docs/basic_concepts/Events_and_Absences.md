# Events and Absences {: #events_and_absences}

## What types of events are there in OpenOlat? {: #event_types}

There are basically two types of events in OpenOlat:

- Basic events (entries in calendars)
- Events with additional options: They appear in [Courses](../learningresources/Events_and_absences.md), in the [Course Planner](../area_modules/Course_Planner/index.md), and in [Absence Management](../area_modules/Absence_Management.md).
These events can be linked to online meetings, and it is possible to record absences. Teachers can also be booked for these events. (Note: Only coaches can be made teachers.)<br>
Events with additional options can have the status "Scheduled", "Running", "Done" or "Cancelled".<br>
If you do not have the necessary permissions, your view of events may be restricted. 


|                           | Basic event | Event with additional options |
| ------------------------- |:-----------------:|:--------------------:|
|[Events in courses](../learningresources/Events_and_absences.md#edit_events)|   |x|
|[Events in course element appointment scheduling](../learningresources/Course_Element_Appointment_Scheduling.md)|   |x|
|[Events in Course Planner](../area_modules/Course_Planner_Events.md)|   |x|
|[Events in the Absence management](#access_absences)|   |x|
|[Schedule in projects](../area_modules/Project_Schedule.md)| x |  | 
|[Events in (project) to-dos](../area_modules/Project_Schedule.md)| x |  | 
|[Events in the personal menu](../personal_menu/To-Dos.md)| x | x | 
|[Events in Calendars](../personal_menu/Calendar.md#create_entry)| x |  | 
|[Events in BigBlueButton](../../manual_admin/administration/BigBlueButton_module.md#tab_online-meetings)| x |  | 
|[Events in Microsoft Teams](../learningresources/Course_Element_Microsoft_Teams.md#closed_editor_configuration)| x |  | 

[To the top of the page ^](#events_and_absences)

---

### Which events (with additional options) are displayed? {: #event_conditions}

If an event is missing although it has been entered, this list helps you find the cause. The order is the order of checking, from the overarching setting down to the individual role. The visibility of events depends on

- whether the "Events / Absences" module is globally enabled in the system administration: `Administration > Modules > Events / Absences`
- whether the [Event & absence management](../learningresources/Course_Settings_Execution.md#lecture_enabled) is switched on in the course concerned: `Course > Administration > Settings > Tab "Execution"`
- whether the "Events" focus element is displayed
- whether there are actually any relevant events
- whether your own role may see the event

!!! tip "An event is missing from the event lists?"

    Check these causes, the most frequent one first:

    - **Event & absence management switched off in the course**: The event appears in no event list, neither in the course nor in Coaching nor in Absence management. In the Course Planner, it stays visible at the implementation.
    - **Implementation without a course**: The event belongs to an implementation, but to no course. It then only appears in the Course Planner.
    - **Module switched off**: The "Events / Absences" module is switched off in the system administration.
    - **Role without a view of the event**: Your own role may not see the event.

[To the top of the page ^](#events_and_absences)

---

### Where are the events with additional options displayed? {: #event_display}

Participants can view their events in the **Toolbar** of the course under the "Events" icon. They only see their own events and cannot record absences.

Events are also displayed on the various **dashboards** of the coaches.

**Event widgets** are available on the overview pages, e.g. in Coaching and in the Course Planner.

Which information an event list contains depends on the area:

- In the **Course Planner** the list serves the planning. There is no absence management there.
- In **Coaching** coaches see the events of all their courses and also record the absences there.
- In the **Toolbar of a course** participants only see their own events with the information relevant to them.

[To the top of the page ^](#events_and_absences)

---

### What statuses can events have in OpenOlat? {: #event_status}

Events with additional options (e.g. in the Course Planner or in Coaching) have one of the following status values:

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

    Which of these options are available is defined by system administrators in the system administration: `Administration > Modules > Events / Absences`, tab "Configuration". More on this in [Module Events and Absences](../../manual_admin/administration/Modules_Events_and_Absences.md). If any of the options described are not available to you, please contact your system administrators.

!!! info "General note"

    In OpenOlat, absences are recorded as a matter of principle, not attendance.


### Absences [:octicons-tag-16:{ title="from Release 12.0 (OO-2637)" }](https://track.frentix.com/issue/OO-2637) {: #absences_categories}

The presence or absence of participants can be recorded in the following categories:

- Present
- Excused absence
- Unexcused absence
- Dispensed

Absences are usually recorded during attendance checks by the **coaches**.

**Participants** can find their recorded absences in the [personal menu](../personal_menu/Absences.md).

An **attendance rate** is calculated from the recorded absences. By comparing this with a specified permitted **absence rate** (e.g., 80%), it can be calculated whether a course can be considered attended.

### Notices of absence [:octicons-tag-16:{ title="from Release 14.1 (OO-4217)" }](https://track.frentix.com/issue/OO-4217) {: #abcenses_cancellations}

Participants can be allowed to give notice of absence in advance in the [personal menu](../personal_menu/Absences.md#tab_notices_dispensation).

### Excused absences {: #excused_absences}

It can be set system-wide that excused absences are counted as "present" for the calculation of the attendance rate.

### Dispensations {: #dispensations}

There are various reasons why a participant may not be able to or required to attend a specific part of a course. In this case, a dispensation can be set up.

### Appeals {: #appeals}

Participants have the opportunity to appeal against a decision made by coaches, e.g., a supposedly unexcused absence. Appeals are also recorded in OpenOlat.

[To the top of the page ^](#events_and_absences)

---


## Where can I find the absence management? {: #access_absences}

A distinction must be made between

1. the **general activation and configuration** of absence management by system administrators in the system administration at:<br>
   `Administration > Modules > Events / Absences`<br>
   [More about that >](../../manual_admin/administration/Modules_Events_and_Absences.md)


2. the **configuration** of absence management in a **course**<br>
    Course owners configure the event and absence management for their course in the course administration:<br>
    `Course > Administration > Settings > Tab "Execution" > Section "Configuration event and absence management in course"`<br>
    [More about that >](../learningresources/Course_Settings_Execution.md#config_event_and_absence_management)


3. the **recording and management** of absences in a course by course owners<br>
    Course owners record and manage the absences in Run Mode (i.e., at runtime, not in the editor) at:<br>
    `Course > Administration > Events and absences > Tab "Participants"`<br>
    [More about that >](../learningresources/Events_and_absences.md)

4. the **recording and management** of absences in a course by coaches<br>
    Coaches record and manage the absences at:<br>
    `Toolbar > Events`<br>
    [More about that >](../learningresources/Toolbar_Events.md)

5. the overview of **personal absences**<br>
    You and all participants can find your personal absences in your personal menu. Here, administration is only possible to a limited extent and for yourself, e.g. in the form of a notice of absence.<br>
    [More about that >](../personal_menu/Absences.md)


6. the **cross-course absence recording** by coaches<br>
    Coaches find the option to record absences in various courses under:<br>
    `Coaching > Events / Absences`<br>
    [More about that >](../area_modules/Coaching/index.md)


7. the **cross-course absence management** by authorised persons with the role absence manager.<br>
    Administration includes, for example, processing dispensations and appeals. This administrative task goes beyond simple recording and is therefore assigned to a separate role. Authorised persons find the tools in the main navigation under:<br>
   `Absence management`<br>
   [More about that >](../area_modules/Absence_Management.md)

[To the top of the page ^](#events_and_absences)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Events and absences >](../learningresources/Events_and_absences.md)<br>
[Course Planner: Overview >](../area_modules/Course_Planner/index.md)<br>
[Absence management >](../area_modules/Absence_Management.md)<br>
[Course Element "Appointment scheduling" >](../learningresources/Course_Element_Appointment_Scheduling.md)<br>
[Course Planner: Events >](../area_modules/Course_Planner_Events.md)<br>
[Projects - Schedule >](../area_modules/Project_Schedule.md)<br>
[User tools: To-dos >](../personal_menu/To-Dos.md)<br>
[User tools: Calendar >](../personal_menu/Calendar.md)<br>
[BigBlueButton module >](../../manual_admin/administration/BigBlueButton_module.md)<br>
[Course Element "Microsoft Teams" >](../learningresources/Course_Element_Microsoft_Teams.md)<br>
[Course Settings - Tab Execution >](../learningresources/Course_Settings_Execution.md)<br>
[User tools: Absences >](../personal_menu/Absences.md)<br>
[Module Events and Absences >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Toolbar: Events >](../learningresources/Toolbar_Events.md)<br>
[Coaching - Overview >](../area_modules/Coaching/index.md)

**Further reading**<br>
[Coaching - Events and Absences >](../area_modules/Coaching_Events_Absences.md)<br>
[Coaching - People >](../area_modules/Coaching_People.md)

[To the top of the page ^](#events_and_absences)

---