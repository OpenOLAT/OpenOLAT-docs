# Course Element "Microsoft Teams"

## Profile

Name | Microsoft Teams
---------|----------
Icon | :fontawesome-solid-tv:
Available since | 
Functional group | Communication und collaboration
Purpose | Integration of the Microsoft Teams web conferencing software 
Assessable | no
Specialty / Note | Microsoft Teams is commercial software. To use the course element, a separate license and server hosting is required.


## Software functions {: #software_functions}

Microsoft Teams enables virtual rooms for synchronous meetings with webcam and audio support.


## System requirements {: #system_requirements}

MS Teams can be used both as an app and in the MS Edge browser.

!!! tip "Recommendation"

    For full use of all features – in particular **breakout rooms** – the MS Teams **desktop app** on Windows or macOS is recommended. Not all features are available in the web browser or on Linux, iOS, and Android.

## Roles in MS Teams {: #teams_roles}

There are three roles in an MS Teams meeting:

| Role | Who | Rights |
|------|-----|--------|
| **Organizer** | Automatically the person who enters the meeting first – exactly one person per meeting | Create breakout rooms, meeting settings, full control |
| **Presenter** | All persons configured as moderators | Share screen, manage content |
| **Attendee** | All other participants | Listen and watch |

!!! warning "Note: First Joiner = Organizer"

    The first person to enter a meeting automatically receives the **Organizer** role – regardless of the moderator setting in OpenOlat. This role cannot be changed or reassigned afterwards, neither in OpenOlat nor in Microsoft Teams.

    In **permanent rooms** with rotating coaches, only the person who started the meeting first has permanent access to advanced features such as breakout rooms. If a different person is to act as organizer, a new room must be created.

## Configure room with closed course editor {: #closed_editor_configuration}

In the course, course owners and tutors can add new meetings in the previously created course element Microsoft Teams in the "**Meeting management**" via "**Add online meeting**".

### The following variants are distinguished when creating online meetings: {: #meeting_variants}

* Add single online meeting
* Add permanent reservation
* Add daily recurring online meetings
* Add weekly recurring online meetings

The variants differ only in the creation of the dates. Separate online appointments/reservations are created, which can then be edited in the "**Meeting management**" tab via the "**Edit**" link.

## Add online meeting: The settings in detail {: #add_meeting}

### Configuration Online Meeting

  *  **Name**: Appointment name
  *  **Created by**: The name of the creator is displayed automatically.
  *  **Description**: Appointment description. This information is displayed before the course participants enter the respective meeting room.
  *  **Main moderator**: Here, the name of a person can be entered.
  *  **Access external user**: Enter a code/word here
  *  **Show room bookings**: Calendar view for checking busy online meetings
  *  **Participants may open the meeting**: :octicons-tag-16:{ title="from Release 15.4.1 (OO-5250)" } Participants with a Microsoft account of the institution may open the meeting with limited presentation permissions, without a coach being present.
  *  **Allow guests**: Unauthenticated persons may join the meeting. This option is only visible if the course is publicly accessible and guest access is enabled.
  *  **Moderator**: Determines who receives the **Presenter** role in MS Teams (see [Roles in MS Teams](#teams_roles)).

#### Moderator options in detail {: #moderator_options}

| OO setting | Who becomes Presenter in Teams |
|---|---|
| **Coach/Owner** | Only course coaches and owners; all other participants become Attendees |
| **Organisation** | All users of the Azure organisation automatically receive the Presenter role when joining |
| **All** | All participants become Presenters |

!!! info "Note"

    A room configuration cannot be changed once it has been created. To apply different moderator settings, a new room must be created.

#### **For scheduled rooms**:

  *  **Beginning**: Define the starting time for meetings
  *  **Lead time (Min.)**: Lead time in which the meeting can already be started by the course coaches and owners
  *  **End**: Ending time of the meeting - the maximum duration of a meeting depends on the selected room template
  *  **Follow-up time (Min.)**: Follow-up time in which the meeting can be extended for all persons. A display with the remaining conference time appears.

!!! info "Note"

    For daily or weekly recurring appointments, the start and end date must also be defined. Subsequently, all appointments for this period are displayed and individual appointments can still be deleted from the list or added.

In the configuration of a room, both during the creation as well as later when editing via the link "**Show room bookings**", an overview of all booked Microsoft Teams rooms of the instance can be viewed. This makes it easier to identify time bottlenecks or heavy system load at an early stage and, if necessary, to select another date.

Via the tab "**Online appointments**" you get access to a specific appointment or room.

## Breakout Rooms {: #breakout_rooms}

Breakout rooms can only be created and managed by the **Organizer** of a meeting (see [Roles in MS Teams](#teams_roles)).

**Supported platforms:** Breakout rooms are only available in the Teams desktop app on Windows and macOS – not in the web browser and not on mobile devices.

**Restrictions on participant assignment:** The following persons cannot be assigned to breakout rooms:

  * Persons with a Teams Free account
  * Persons on unsupported devices (e.g. CVI conferencing devices)
  * Offline participants or persons with an outdated Teams version

**Further restrictions:** Breakout rooms are not available for cancelled or deleted meetings, in private or shared channels, or when restricted by admin policies.

**Capacity:** A maximum of 300 participants per meeting is supported. If this limit is exceeded, the breakout room function is automatically disabled. Rooms expire after 60 days of inactivity.

## Calendar view {: #calender_display}

In addition, the online appointments created in the course element will be automatically entered in the course-specific calendar and subscribed to by the participants. You can also quickly move from the calendar to the appointment-based room.

!!! info "Note"
    Only appointments with a defined start and end date appear in the course calendar. Permanent reservations without a date are not displayed in the calendar.

## Participant perspective {: #participant_perspective}

If a course participant calls up an MS Teams course element, they will see an overview of the current, the expired and the permanent rooms, if available. A click on "**Select**" opens the detail view of the respective meeting.

![course_element_teams_overview_v1_de.png](assets/course_element_teams_overview_v1_de.png)

Current sessions can be started by clicking on "**Join meeting**".

![course_element_teams_join_v1_de.png](assets/course_element_teams_join_v1_de.png)

!!! warning "Note"

    When meetings have expired, joining is no longer possible. Recordings are not available in OpenOlat; recordings made directly in Microsoft Teams are only accessible via Microsoft Teams.

## Troubleshooting {: #troubleshooting}

For application-specific issues, Microsoft's official help is available:

[Microsoft Help: Troubleshoot in Microsoft Teams](https://support.microsoft.com/en-us/teams/platform/troubleshoot-in-microsoft-teams){:target="_blank"}
