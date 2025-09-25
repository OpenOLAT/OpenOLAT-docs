# Course Element "Appointment scheduling" {: #appointment_scheduling}


## Profile

Name | Appointment scheduling
---------|----------
Icon | ![Appointment scheduling Icon](assets/dateentry.png){ class=size24 }
Available since | 
Functional group | Administration and organisation
Purpose | Scheduling and enrolment for specific joint appointments
Assessable | No
Specialty / Note |



The scheduling course element can be used to organize registrations for fixed dates as well as appointment scheduling. Among other things, you can specify whether multiple dates can be selected, whether the number of participants is limited, whether it is visible who has registered, and whether a virtual classroom installed in the OpenOlat instance (e.g., BigBlueButton or Teams) should be assigned.

## In the course editor

The course element is added in the course editor. The permissions for specific groups of people are defined in the "Configuration" tab. This allows you to define whether course owners and/or course coaches are considered organizers of the events, whether they receive email notifications, whether participants are allowed to comment on their choices, and who is authorized to edit an event (e.g., people with a specific role, individual participants, or a specific group).

If the selection of dates should only be possible within a certain time window, the time specifications must be entered accordingly in the course editor in the "Learning Path" tab or, in the case of conventional courses, the visibility or access must be configured accordingly.

## Configure occasion (closed course editor)

The actual configuration and setup of the selectable dates takes place in the course run with the editor closed. The "Create event" button is used to first create a new appointment booking or appointment scheduling, perform the basic configuration, and enter the first dates. Additional dates can be added later using "Add appointment". Dates that have already been created can be edited at any time using the three-dot menu.

### Configure occasion

First, click on **"Create event"**. An "event" is a compilation of several dates that can be selected.

The configuration menu appears and you can specify the following aspects: 

![Anlass erstellen, Konfiguration](assets/Terminplanung_Anlass_erstellen_20.jpg)

 **Title:** Enter the name of the appointment here, e.g. "Reconciliation closing meeting", "Kick-off meeting" etc. The entry is required (mandatory field).

 **Description:** Explain the appointment selection in more detail.

 **Type:** Decide if it is a date determination for a common date or an enrollment for one or more dates from a selection, e.g. lab dates.

 **Configuration:** Decide whether the participants are allowed to select only one or several appointments and whether the names of the participants are visible for other participants. In the case of "Appointment booking", you can also define whether the organizer have to confirm the appointment.

 **Organizer:** Define here who will be displayed as the organizer of the event.

 **Location:** Enter the location of the event here.

 **Max. Participants:** You can limit the number of members for an appointment (only for "Enrolment").

**Type of appointment:** You can create appointments based on duration, based on a start and end date, or recurring by specific days of the week. The selection makes it easier for you to create additional appointments.

!!! info "Info"

    If "Duration" is selected, when adding further appointments, the appointments will be preconfigured on the same day and the clock times will be adjusted according to the duration.

    If Start/End is selected, the selected times are retained and you only need to adjust the date for new entries.

 **Appointments:**  The concrete election dates are entered here. Click on the "+ sign" to add new dates. By clicking on the "- sign", dates are deleted again.

 **Online meeting:** The options are: No, no online appointment or one directly selects the desired tool BigBlueButton or Teams, provided that Virtual Classrooms have been activated by the administrator.

!!! tip "Tip"

    If BigBlueButton or Teams is activated, a BigBlueButton or Teams room can be added and further configured for the selected appointments. In this case, "online" is automatically displayed for the location.

A created "occasion" can later be edited, duplicated or deleted by clicking on the cogwheel. The number of participants for the event can also be restricted to certain groups. An export of the participants for an event is also possible.

![occasion.png](assets/Terminplanung_anlass.jpg)

## Organize appointments

The specific dates of already created schedules/appointments can be viewed in more detail via the "View appointments" link and edited by the course owner or coach. Here you can add, delete, rebook participants, adjust the description, change appointments or confirm appointments.

![find_appointment.png](assets/Terminfindung_punkte.jpg)

## Participant view

By clicking on the course element, participants are shown all, future or selected dates and a selection is possible via the link "**Select**". Filtering for dates with free places can also be done via the filter function.

![appointment.png](assets/Terminfindung.png)

![Next apppointment](assets/Terminplanung18_Terminanzeige_en.png)
