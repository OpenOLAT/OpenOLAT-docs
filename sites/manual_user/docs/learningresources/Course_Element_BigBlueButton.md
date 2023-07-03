# Course Element "BigBlueButton"

## General

!!! info "Hinweis"

    BigBlueButton ist eine Open Source Software (LPGL Lizenz). Um den Kursbaustein zu nutzen ist ein separates Serverhosting erforderlich.

### Type of integration

BigBlueButton enables virtual classrooms with the following functionalities:

  * Webcam and audio support
  * Folienpräsentation z.B. PDF
  * Screen sharing
  * Multi-User Whiteboard
  * Survey functionality
  * Group rooms, group chat
  * private chat
  * shared notes

### System requirements

BigBlueButton is a browser-based software solution and requires no additional plug-ins.  
For full functionality (for moderators and participants) **Google Chrome** or
**Mozilla Firefox** is recommended. On Windows the new version of **Edge with
Chromium Engine** can also be used. It is officially recommended to use
**Google Chrome** for screen sharing or playback of recorded meetings.  
  
## Configuration in the course editor

When integrating BigBlueButton into a course it can be decided whether a
scheduled online meeting can be started by the moderator only or also by
participants. If this option is activated participants will not be able to
enter the meeting until the moderator has started it.

![BBB_access.png](assets/image2020-4-14_11-19-9.png)
  
## Räume erstellen, konfigurieren und betreten 

Folgende Einstellungen erfolgen bei geschlossenem Editor. 

### Tab "Meeting management" 

In the course, tutors can create new events in the BigBlueButton module in the meeting management
via "Add online-meeting". Also, already created appointments can be copied or deleted.

![online_meeting.png](assets/image2020-4-14_11-20-49.png)

The following variants for creating online-meeting are distinguished:

* Add single meeting
    
    Bietet sich z.B. an, wenn es nur einen konkreten Termin für den Kursbaustein geben soll
    * Add permanent meeting room

    Sollte verwendet werden, wenn man einen BBB-Raum haben möchte, der permanent zur Verfügung steht und mehrfach genutzt werden soll.

* Add daily recurring meeting

      Um schnell tägliche Termine zu erstellen.
* Add weekly recurring meeting
     Um schnell wöchentliche Termine, z.B. für Webinar-Serien oder ein Semester zu erstellen.

The variants only differ in the creation of the dates. Separate online-
meetings/reservations are created, which can then be edited separately.
Depending on the configuration of the server, different options can be
available here.

![BBB_creating.png](assets/bbb_creating.png)

Folgende Detaileinstellungen können dabei vorgenommen werden: Die Einstellungen im Detail:

**Configuration of an online-meeting**

  *  **Name**: Name of the event
  *  **Creator:  **The name of the creator is automatically displayed.
  *  **Description**: Description of the event
  *  **Welcome  ** **Message**: Displayed in the BigBlueButton room as a welcome message in the chat for all participants
  *  **Main presenter:** The name of one or more persons can be entered here.
  *  **Slides**: Upload your slides here in advance of the meeting or delete slides that have already been uploaded.
  *  **Room-template**: Selection of the pre-configured room templates (determines number of participants and various default settings in the online meeting)
  *  **Preferred Server:**  Is usually selected automatically.
  *  **Allow meeting recording:** yes or no
  *  **Publish recording automatically for:**  Select the user groups to which you want to provide the recording later.
  *  **Accept user on entry (waiting room):** Here you can decide whether people first land in a waiting room and do not immediately enter the meeting room. If "disabled" is selected, all persons will enter the meeting room directly. Alternatively, it is also possible to configure here that everyone (all users) ends up in the waiting room or only guests and external persons and course participants, on the other hand, can enter the meeting room directly.
  *  **Display:** standard or webcam appointment (depending on the configuration by the BBB administrator)
  *  **External user access:** If this option has been allowed by the administrator, the URL that you can send to external users can be customized here. The link will then also appear for course owners and coaches before the room is entered. Participants will not see the link.
  *  **Password for external users:** Enter a password here that guests, i.e. persons without an OpenOlat account, must enter to access the room.
  *  **Show room bookings** : calendar view for checking occupied online-meetings

Only for scheduled rooms

  *  **Start date:** Geben Sie den Starttermin ein. 
  *  **Prep time (min.)**: 0 to 15 minutes configurable lead time in which the meeting can already be started by the course coach or owner (but not by participants) e.g. for preparing a presentation.
  *  **End date:** End of the meeting - the maximum duration of a meeting depends on the selected room template
  *  **Follow-up (min.)**: 0 to 15 minutes configurable follow-up time. The meeting is automatically extended by the follow-up time for all persons after reaching the end time, a display with the remaining conference time appears.

Only for recurring online-meetings

  *  **Start recurring date** : 1st online-meeting (with weekly repetition this corresponds to the weekday of the series)
  *  **End reccuring date:** End of recurring online-meetings

For recurring online-meetings, the online-meetings can be edited/deleted or
supplemented with free data in the second process step "Date" before creation.

!!! warning "Attention"

    Once a BigBlueButton meeting has been started, i.e. the online room has been opened, the settings on the meeting appointment can no longer be edited!     

### Tab "Online-meetings"

The tab "Online-meetings" gives you access to a specific appointment or room.

Course owners and course coaches can upload their presentation(s) in advance
so that they are available at the start of the meeting. The top document of
the list is displayed directly.

![BBB_präsentation.png](assets/BBB_praesentation.png)

#### Recordings

The recordings of a meeting can be found in the tab "Online Meetings" →
"Finished Online Meetings". Select the appropriate meeting here. Automatically
published recordings are directly selectable here. If the deployment is done
manually, owners and coaches can now define for which target group the
recording should be deployed.

!!! warning "Attention"

    The settings made under "publish" as well as under "delete" are valid for the recording as well as for the download! If you delete an entry, the whole recording will be deleted.

![BBB_recordings.png](assets/bbb_recordings.png)  

## Calendar view

If the course calendar is activated, the recorded online dates are also
available as appointments and can be subscribed to by participants in their
personal calendar.

When configuring a room, an overview of all booked BigBlueButton rooms in the
instance can be viewed both during creation and later when editing using the
"Show room bookings" link. This makes it easier to identify time bottlenecks
or a high system load early on and to choose a different date if necessary.

In addition, the online appointments created in BigBlueButton are
automatically entered into the course-specific calendar. From here, all course
members can quickly reach the correspondingly linked BigBlueButton room.

![calender.png](assets/image2020-4-7_14-14-5.png)  
  
## View for participants

The tab "Online Meetings" gives you access to a specific appointment or room.
When a course participant calls up a BigBlueButton course element, he/she will
see an overview of the current, expired and permanent rooms, if available.  A
click on "Select" will take you to the login area of the respective room.

![BBB_overview.png](assets/BBB_Uebersicht.png)

Current sessions can be started by "Join meeting" and the specific
BigBlueButton room can be accessed.

![BBB_join_meeting.png](assets/BBB_Meeting_beitreten.png)

Once a meeting is over, the rooms can no longer be entered, but you can access
any recordings of the meeting. Coaches and course owners can also delete
recordings here.  
  
## BigBlueButton Room

![BBB_room.png](assets/BBB-Raum.png)

The welcome text displayed can be customized when setting up the room. If the
users have stored a profile picture, this is also displayed in the list of
participants.

Depending on the room settings, different options are available in the room.  

## BigBlueButton for guests 

Depending on the configuration of the BigBlueButton template, the conference
room can be made accessible to non-registered persons without access to
OpenOlat, i.e. external participants (see [guest access](../basic_concepts/guest_access.md)).
The prerequisite for this is that it is a conventional course, not a learning
path course, and that the course itself has also been activated for guests.
Guests can enter a name of their choice during dial-in.

The link will then also appear for course owners and coaches before entering
the room. Participants will not see the link.

![BBB_guests.png](assets/bbb_externe2.png)

In addition, a password can also be generated for guests in the configuration
of the course element, which they must enter before dialing into the room.
Whether this option is available depends on the BBB configuration by the BBB
administration.
  
!!! note "Link to further information"

    BigBlueButton supplier website: <https://bigbluebutton.org/> 