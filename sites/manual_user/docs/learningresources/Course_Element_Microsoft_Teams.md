# Course Element "Microsoft Teams" {: #microsoft_teams}

## Profile

Name | Microsoft Teams
---------|----------
Icon | :o_icon_o_vc_icon:
Available since | Release 15.4
Functional group | Communication and collaboration
Purpose | Integration of the Microsoft Teams web conferencing software 
Assessable | no
Specialty / Note | Microsoft Teams is commercial software. To use the course element, a separate license and server hosting is required.


:octicons-device-camera-video-24: **Video Introduction (German)**: [Microsoft Teams](<https://www.youtube.com/embed/eyHOaF-ujuE>){:target="_blank"}

## Software functions {: #software_functions}

Microsoft Teams enables virtual rooms for synchronous meetings with webcam and audio support.


## System requirements {: #system_requirements}

MS Teams can be used both as an app and in the MS Edge browser.

!!! tip "Recommendation"

    For full use of all features, in particular the **breakout rooms**, the MS Teams **desktop app** on Windows or macOS is recommended. Not all features are available in the web browser or on Linux, iOS, and Android.

## Roles in MS Teams {: #teams_roles}

There are three roles in an MS Teams meeting:

| Role | Who | Rights |
|------|-----|--------|
| **Organizer** | Automatically the person who starts the online meeting first, exactly one person per meeting | Create breakout rooms, meeting settings, full control |
| **Presenter** | All persons according to the **Presenters** setting of the online meeting (see [Moderator options in detail](#moderator_options)) | Share screen, manage content |
| **Attendee** | All other participants | Listen and watch |

!!! warning "Note: First Joiner = Organizer"

    The first person to start an online meeting automatically receives the **Organizer** role, regardless of the **Presenters** setting in OpenOlat. This role cannot be changed or reassigned afterwards, neither in OpenOlat nor in Microsoft Teams.

    In **permanent reservations** with rotating coaches, only the person who started the meeting first has permanent access to advanced features such as breakout rooms. If a different person is to act as organizer, a new online meeting must be created.

## Create online meetings with closed course editor [:octicons-tag-16:{ title="from Release 15.4 (OO-5124)" }](https://track.frentix.com/issue/OO-5124) {: #closed_editor_configuration}

So that participants can enter a Microsoft Teams meeting directly from the course, course owners and coaches create online meetings for it. This is done in the running course, not in the course editor. Open the course element "Microsoft Teams", then open the selection **Add online-meeting** in the tab **Meeting management**:<br>
`Course element "Microsoft Teams" > Meeting management > Add online-meeting`

### Variants when creating online meetings {: #meeting_variants}

The selection **Add online-meeting** offers four variants:

  * **Add online-meeting**: a single online meeting with a start and an end.
  * **Add permanent meeting room**: an online meeting without a date that is permanently open. The variant only appears if the system administration has left the option [Online-Meetings without date/permanent](../../manual_admin/administration/Teams_module.md#permanent_meetings) set to "On". "On" is the default. [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9666)" }](https://track.frentix.com/issue/OO-9666)
  * **Add daily recurring meeting**: one online meeting per working day, Monday to Friday, in a selected period.
  * **Add weekly recurring meeting**: one online meeting per week in a selected period.

Each variant creates separate online meetings, for recurring meetings one per date. In the tab **Meeting management**, the link **Edit** opens each online meeting individually. For past online meetings, **View** appears there instead.

## Add online meeting: The settings in detail {: #add_meeting}

### Configuration Online Meeting

  *  **Name**: Name of the online meeting. Mandatory field.
  *  **Creator**: The name of the person who creates the online meeting is displayed automatically.
  *  **Description**: Description of the online meeting. It appears in the detail view of the online meeting before participants join the meeting.
  *  **Main presenter**: The name of a person can be entered here. The name of the person who creates the online meeting is pre-filled.
  *  **Guests**: The checkbox **allowed** lets persons who are not logged in take part in the meeting. This option is only visible if the course is publicly accessible and guest access is enabled.
  *  **Access external users**: A meeting reference, a unique word without special characters. OpenOlat generates a link from it that you share with external persons, e.g. by e-mail. If the field is left empty, access via the link is deactivated.
  *  **Show room bookings**: Calendar view for checking booked online meetings.
  *  **Participants may open the meeting**: :octicons-tag-16:{ title="from Release 15.4.1 (OO-5250)" } Participants with a Microsoft account of the institution may open the meeting with limited presentation permissions, without a coach being present.
  *  **Presenters**: Determines who receives the **Presenter** role in MS Teams (see [Roles in MS Teams](#teams_roles)). Mandatory field.

#### Moderator options in detail {: #moderator_options}

| OO setting | Who becomes Presenter in Teams |
|---|---|
| **Role coach** | Only course coaches and owners; all other participants become Attendees |
| **Organisation** | All users of the Azure organisation automatically receive the Presenter role when joining |
| **Everyone** | All participants become Presenters |

!!! info "Important"

    The settings of an online meeting can only be changed as long as it has not been started. After that, the form only displays the settings. To apply different presenter settings, a new online meeting must be created.

#### For online meetings with a date

  *  **Start**: Date and time at which the online meeting begins.
  *  **Prep time (min.)**: Time in minutes before the start during which owners and coaches can already start and enter the online meeting. For participants, the online meeting only opens at the start.
  *  **End**: Date and time at which the online meeting ends.
  *  **Follow-up (min.)**: Follow-up time during which the meeting can be extended for all persons.

!!! info "Important"

    For daily or weekly recurring online meetings, you also define **Start recurring date** and **End recurring date**. In the next step, the wizard lists all dates of this period. There you can delete individual dates or add dates via **Add online-meeting**.

In the configuration of an online meeting, the link **Show room bookings** opens an overview of all booked Microsoft Teams online meetings of the instance, both when creating and when editing. This makes it easier to identify time bottlenecks or heavy system load at an early stage and, if necessary, to select another date.

In the tab **Online-meetings**, you open a specific online meeting.

## Breakout Rooms {: #breakout_rooms}

Breakout rooms can only be created and managed by the **Organizer** of a meeting (see [Roles in MS Teams](#teams_roles)).

**Supported platforms:** Breakout rooms are only available in the Teams desktop app on Windows and macOS: not in the web browser and not on mobile devices.

**Restrictions on participant assignment:** The following persons cannot be assigned to breakout rooms:

  * Persons with a Teams Free account
  * Persons on unsupported devices (e.g. CVI conferencing devices)
  * Offline participants or persons with an outdated Teams version

**Further restrictions:** Breakout rooms are not available for cancelled or deleted meetings, in private or shared channels, or when restricted by admin policies.

**Capacity:** A maximum of 300 participants per meeting is supported. If this limit is exceeded, the breakout room function is automatically disabled. Rooms expire after 60 days of inactivity.

## Display in the course calendar {: #calender_view}

If you want to keep track of the online meetings of the course, you find them in the course calendar. OpenOlat automatically enters every online meeting with a date that is created in the course element there. The calendar entry contains a link that leads directly to the online meeting. Participants can subscribe to the course calendar.

!!! info "Important"
    Only appointments with a defined start and end date appear in the course calendar. Permanent reservations without a date are not displayed in the calendar.

  :octicons-device-camera-video-24: **Video Introduction (German)**: [Subscriptions](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

## Participant view {: #participant_perspective}

When a participant opens the course element, two lists appear: **Current and upcoming online-meetings** and **Past online-meetings**. Online meetings without a date are marked in the column **Without date** and always appear in the first list. A click on **Select** opens the detail view of the respective online meeting.

![Two lists with current and past online meetings, columns Name, Without date, Start, End and Select link](assets/course_element_teams_overview_v1_de.png){ class="shadow lightbox" title="Overview in the Microsoft Teams course element" }

**Join the online-meeting** opens the meeting in Microsoft Teams in a new window. As long as nobody has started the online meeting, the button is not active for participants. Owners and coaches see **Start the online-meeting** in its place. Whether participants may also open the meeting without a coach depends on the configuration of the online meeting (see above).

![Join the online-meeting button, next to it the name under which the person joins the meeting](assets/course_element_teams_join_v1_de.png){ class="shadow lightbox" title="Detail view of an online meeting" }

!!! warning "Attention"

    When meetings have expired, joining is no longer possible. Recordings are not available in OpenOlat; recordings made directly in Microsoft Teams are only accessible via Microsoft Teams.

## Troubleshooting {: #troubleshooting}

For application-specific issues, Microsoft's official help is available:

[Microsoft Help: Troubleshoot in Microsoft Teams](https://support.microsoft.com/en-us/teams/platform/troubleshoot-in-microsoft-teams){:target="_blank"}

## Further information {: #further_information}

**Mentioned on this page**<br>
[Microsoft Teams module >](../../manual_admin/administration/Teams_module.md)<br>
[Microsoft Help: Troubleshoot in Microsoft Teams](https://support.microsoft.com/en-us/teams/platform/troubleshoot-in-microsoft-teams){:target="_blank"}

**Further reading**<br>
[Virtual classrooms >](../basic_concepts/Virtual_classrooms.md)<br>
[Course Element "Zoom" >](zoom/index.md)<br>
[Events and Absences >](../basic_concepts/Events_and_Absences.md)<br>
[Using Group Tools >](../groups/Using_Group_Tools.md)

**youtube**<br>
[Microsoft Teams](<https://www.youtube.com/embed/eyHOaF-ujuE>)<br>
[Subscriptions](<https://www.youtube.com/embed/h9gOqt7TR7Q>)

[To the top of the page ^](#microsoft_teams)
