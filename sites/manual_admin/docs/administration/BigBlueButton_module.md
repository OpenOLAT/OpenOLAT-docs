# BigBlueButton module {: #bbb}

The virtual classroom BigBlueButton is activated in the system administration:<br>
`Administration > External tools > BigBlueButton`

This article describes the configuration of multiple BigBlueButton servers, load balancing and setting up system-wide room templates.

Instructions on how to configure individual online meetings for course owners are described in the chapter [Course Element "BigBlueButton"](../../manual_user/learningresources/bigbluebutton/index.md).

---

## Tab "Configuration" {: #tab_config}

  *  **Module "BigBlueButton":** Activation of the functionality
  *  **Activate for:** Activation of the functionality individually for course element "BigBlueButton", course events [:octicons-tag-16:{ title="from Release 20.0.1 (OO-8237)" }](https://track.frentix.com/issue/OO-8237), course element "Appointment scheduling", groups and supervisor chat
  *  **Online-Meetings without date:** Additional option to activate "permanent room reservations" without a date in addition to online meetings. These are not visible in the calendar and count as booked at any time in the limits of the room template.
  *  **Import profile picture:** The profile picture from the OpenOlat user profile is shown as an avatar in the online meeting. Guests and users without a profile picture get no avatar [:octicons-tag-16:{ title="from Release 16.0 (OO-5435)" }](https://track.frentix.com/issue/OO-5435)
  *  **Servers:** In the configuration the available BigBlueButton servers per OpenOlat instance are entered.
  *  **Button "Add server":** [see below for details >](#add_server)
  *  **Recording handler:** Native or Opencast
  *  **Never delete recordings:** The recordings are kept on the external server, even if the online meeting or the course in OpenOlat is deleted. The option only appears if "Opencast" is selected as recording handler [:octicons-tag-16:{ title="from Release 15.3.8 (OO-5170)" }](https://track.frentix.com/issue/OO-5170)
  *  **Default settings for the publication of recordings:** Default setting for who can see new recordings. The available options are "Owners and coaches", "Course / group participants", "All meeting's attendees (without guests)" and "Guests". When creating an online meeting, the default setting can be overridden [:octicons-tag-16:{ title="from Release 20.1.12 (OO-9037)" }](https://track.frentix.com/issue/OO-9037)
  *  **Delete meetings automatically:** x days after meeting end
  *  **Limit of all presentation files per meeting (MB):** Mandatory field with specification of permitted megabytes

![Activation per area, server list, recording handler and deletion period of the online meetings; Configuration tab in the BigBlueButton module](assets/bbb_admin_config_v1_en.png){ class="shadow lightbox" }


### Add BigBlueButton server {: #add_server}

Click on the "Add server" button in the "Configuration" tab to open a pop-up for the details.

  *  **BigBlueButton API URL:** URL of the BBB server
  *  **Shared secret:** API key of the BBB server
  *  **Capacity factor:** Server weighting in load balancing
  *  **Activate server:** Server is available for load balancing
  *  **Manual selection only:** Only manually selected servers are available for load balancing
  *  **Button "Check server connection":** Checks the access to the server specified here.

![API URL and shared secret are mandatory, Check server connection verifies the entries before saving; Add server dialog](assets/bbb_admin_add_server_v1_en.png){ class="shadow lightbox" }


---

## Tab "Servers" {: #tab_server}

The available BigBlueButton servers per OpenOlat instance are displayed here.

![Per server capacity and current load, the filter separates this OpenOlat from all OpenOlats; Servers tab in the BigBlueButton module](assets/bbb_admin_server_v1_de.png){ class="shadow lightbox" }


### Load balancing [:octicons-tag-16:{ title="from Release 14.2.7 (OO-4626)" }](https://track.frentix.com/issue/OO-4626) {: #load_balancing}

The goal is to distribute the generated load of simultaneous online meetings to the available BigBlueButton servers by considering performance parameters (such as the number of videos and the number of participants in the meetings). OpenOlat has an integrated load balancing for this purpose. At the initial start of the online meeting (depending on the configuration by the moderator or the first participant) the server with the lowest load is selected for the meeting. The load is calculated from the different measurement factors and weights the result with the capacity factor.

Use the filter to show the key figures for all OpenOlat instances on the BigBlueButton server ("All OpenOlats") or only for the sessions of this instance ("This OpenOlat").

### Capacity factor {: #capacity_factor}

The capacity factor is recorded with a value between 1 and 100 per server. The calculated number of users on the server is multiplied by the capacity factor. In this count, video users weigh most, then audio users, then viewers. This way, a server with stronger performance (RAM/CPU/disk) adapts to a weaker one.


---

## Tab "Room-templates" {: #tab_room-templates}

The room templates are available for selection when creating a new online meeting. The templates control:

  * The available functions and standard settings in the online meeting.
  * The number of possible simultaneous participants per room.
  * Limits regarding the duration and the number of online rooms available.

Use the "New room template" button to create a new room template. The system templates delivered with OpenOlat (column "System") can be edited but not deleted.

![Per template rooms, participants and duration, system templates without Delete link; Room-templates tab in the BigBlueButton module](assets/bbb_admin_room-templates_v1_de.png){ class="shadow lightbox" }


### Configuration of a room template {: #room_config}

  *  **Room name:** Name of the room template
  *  **Description:** Description of the room template (e.g. learning scenario, field of application)
  *  **Number of participants:** Maximum number of participants (viewers)
  *  **Duration (minutes):** Maximum length of the online meetings
  *  **Enable room-template:** Activated room templates are available in courses/groups for new online meetings and can be chosen by course owners
  *  **Number of rooms:** Maximum number of concurrent rooms of this room template
  *  **Open for external users:** OpenOlat automatically generates a direct link for external users so that they can enter the BigBlueButton room without calling OpenOlat first. The link is displayed in the room configuration and can be changed by course owners or coaches if necessary and passed on to guests.
  *  **Accept joining users:**
     * Disabled (Everyone can enter immediately.)
     * All users (Every entry must be confirmed.)
     * Only guests and external users (Only the entry of guests and external users must be confirmed.)
  *  **Room-template activated for:** Determines which roles can use the room template for new online meetings. If the "Group user" option is activated, the template can also be used and further configured in OpenOlat [groups](../../manual_user/groups/Using_Group_Tools.md).

![Room name, participants and duration define the room, the list at the bottom releases the template per role; room template form](assets/bbb_room_template.png){ class="shadow lightbox" }


### Default settings of the room template

![Each behaviour is a yes-no choice, from webcams only for moderators to lock mode on join; default settings in the room template form](assets/edit-room-template-2.png){ class="shadow lightbox" }


### Default settings for locked participants

![Seven yes-no choices set what the lock disables, from webcam to layout changes; section For locked participants in the room template form](assets/edit-room-template-3.png){ class="shadow lightbox" }


---

## Tab "Online-meetings" {: #tab_online-meetings}

Overview of the configured online meetings with the possibility to switch directly to the course or the group (context) or to delete the online meeting. Use the search to find specific BigBlueButton rooms, mark them and delete them in bulk if necessary.

![All online meetings of the instance with room template, server and context, search field and multiple selection for deletion; Online-meetings tab in the BigBlueButton module](assets/bbb_administration_online-meetings.png){ class="shadow lightbox" }


---

## Tab "Calendar" {: #tab_calendar}

Calendar overview of all recorded online meetings to check times with high occupancy and to display overlaps graphically.

![All online meetings of the instance in the week view, switchable to month, day and year; Calendar tab in the BigBlueButton module](assets/bbb_admin_calendar_v1_de.png){ class="shadow lightbox" }


---

## Further information {: #further_information}

[Course Element "BigBlueButton" >](../../manual_user/learningresources/bigbluebutton/index.md)<br>
[Using Group Tools >](../../manual_user/groups/Using_Group_Tools.md)<br>
[Virtual classrooms >](../../manual_user/basic_concepts/Virtual_classrooms.md)<br>
[Frequently asked questions - BigBlueButton >](../../manual_user/learningresources/bigbluebutton/faq.md)<br>
[Course Element "Appointment scheduling" >](../../manual_user/learningresources/Course_Element_Appointment_Scheduling.md)<br>
[Absence management >](../../manual_user/area_modules/Absence_Management.md)

[To the top of the page ^](#bbb)
