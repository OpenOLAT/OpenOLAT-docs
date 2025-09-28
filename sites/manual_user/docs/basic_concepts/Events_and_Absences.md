# Events and Absences {: #events_and_absences}

## What types of events are there in OpenOlat?

There are basically two types of events in OpenOlat:

- Basic events (without the option to record absences)
- Events with absences (appointments in the course; they appear in the Course Planner and absence management)<br>
Lecturers can also be booked for these dates. (Only coaches can be made lecturers.)

|                           | basic event | Event with absence |
| ------------------------- |:-----------------:|:--------------------:|
|[Events in Course Planner](../area_modules/Course_Planner_Events.md)|   |x|
|[Events in the Absence management](#access_absences)|   |x|
|[Events in Projects](../area_modules/Project_Schedule.md)| x |  | 
|[Events in (Project) To-dos](../area_modules/Project_Schedule.md)| x |  | 
|[Events in Personal Menu](../personal_menu/To-Dos.md)| x | x | 
|[Events in Calendars](../personal_menu/Calendar.md#create_entry)| x | x | 
|[Events in BigBlueButton](../../manual_admin/administration/BigBlueButton_module.md#tab_online-meetings)| x |  | 
|[Events in Microsoft Teams](../learningresources/Course_Element_Microsoft_Teams.md#raum-konfigurieren-bei-geschlossenem-kurseditor)| x |  | 

[To the top of the page ^](#events_and_absences)

---

## Which absences can be administrated? {: #administrated_absences}

!!! info "General note"

    Administrators can configure the options in absence management in great detail. If one of the options described is not available to you, please contact your administrator.


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

1. the **general activation and configuration** of absence management by administrators at:<br>
   **Administration > Module > Events and absences**<br>
   [More about that >](../../manual_admin/administration/Modules_Events_and_Absences.md)


2. the **configuration** of absence management in a **course**<br>
    **Administration > Settings > Tab "Implementations" > Section "Configuration event and absence mnagement in course"**<br>
    [More about that >](../learningresources/Course_Settings_Execution.md#config_event_and_absence_management)


3. the **recording and management** of absences in a **course** by **course owners**<br>
    Recording and administration is carried out in Run Mode (i.e., at runtime, not in the editor) by course owners at:<br>
    **Administration > Events and absences > Tab Members**<br>
    [More about that >](../learningresources/Events_and_absences.md)

4. the **recording and management** of absences in a **course** by **coaches**<br>
    Recording and administration by coaches takes place at:<br>
    **Toolbar > Events**<br>
    [More about that >](../learningresources/Toolbar_Events.md)

5. the overview of **personal absences**<br>
    You and all participants can find your personal absences in your personal menu. Here, administration is only possible to a limited extent and for yourself, e.g., in the form of deregistration.<br>
    [More about that >](../personal_menu/Absences.md)


6.  the **cross-course absence recording** by coachess<br>
    Coaches can find the option to record absences in various courses in the<br>
    **Coaching tool > Button "Events/Absences"**.<br>
    [More about that >](../area_modules/Coaching.md)


7. **cross-course absence management** by authorized persons with the role of absence administrator:.<br>
    Administration includes, for example, processing exemptions and appeals. This administrative task goes beyond simple data entry and is therefore assigned to a separate role. Authorized users can find the tools in the<br>
   **Header menu: Absence management**<br>
   [Mehr dazu >](../area_modules/Absence_Management.md)

[To the top of the page ^](#events_and_absences)

---


## Further information {: #further_information}

[Activation and configuration of absence management by administrators >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Configuring absence management in a course >](../learningresources/Course_Settings_Execution.md#config_event_and_absence_management)<br>
[Recording and managing absences in a course by course owners >](../learningresources/Events_and_absences.md)<br>
[Recording and managing absences in a course by coaches >](../learningresources/Toolbar_Events.md)<br>
[Personal absences >](../personal_menu/Absences.md)<br>
[Cross-course absence recording in the coaching tool >](../area_modules/Coaching.md)<br>
[Cross-course absence management by absence administrators >](../area_modules/Absence_Management.md)<br>


[To the top of the page ^](#events_and_absences)

---