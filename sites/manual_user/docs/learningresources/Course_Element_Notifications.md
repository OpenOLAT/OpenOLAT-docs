# Course Element "Notifications" {: #notification}


## Profile

Name | Notifications
---------|----------
Icon | :o_icon_o_infomsg_icon:
Available since | New edition with release 18
Functional group | Administration and organisation
Purpose | Notifications in the course structure (course menu)
Assessable | no
Specialty / Note |



:octicons-device-camera-video-24: **Video Introduction (German)**: [Notifications](<https://www.youtube.com/embed/3tAj19Avfkk>){:target="_blank"}

This course element allows you to embed notifications in the course structure. These notifications are visible both in the course and under `Personal tools > Subscriptions` in the notifications of each individual participant. The message can be either a short info text or extensive information added as a file attachment (by default, max. 5 MB).

A message can be published immediately or at a later point in time and additionally sent by e-mail. How to choose the recipients is described in the section [Writing and sending a message](#create_notification).

## Configuration in the course editor Tab "Notification configuration" {: #configuration_notification}

 **Display:** The maximum number of days determines how long notifications shall be displayed in your course (in days). The maximum number of messages determines how many messages shall be displayed simultaneously in your course.

 **Subscribe automatically:** By default, this course element is automatically subscribed to by participants. This option can be deactivated here so that participants can subscribe to notifications manually.

:octicons-device-camera-video-24: **Video Introduction (German)**: [Subscriptions](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

In the "Permissions" section, you can define which course roles are allowed to create and manage messages. Owners can generally create and manage messages.

Messages can be viewed in the personal menu under `Personal tools > Subscriptions`, see also the page [Subscriptions](../personal_menu/Subscriptions.md). The number of displayed messages can be set in the course editor.

By default, only coaches and owners are allowed to create messages. However, all participants may read messages. In the "Notification configuration" tab, you can adjust this setting according to your wishes.

!!! info "Important"

    The number of characters for the message is limited to 32,000. You will
    receive information about the number of characters already used in the lower
    right corner of the message editor. If the permitted number of characters is
    exceeded, a corresponding message is displayed. Attention: The number of actual
    characters specified differs from the number of visible characters, as the
    actual number of HTML code is used.

!!! tip "Tip"

    An element with similar functions, but without specific configuration, can also be found in the toolbar. This is the "[Info messages](../learningresources/Using_Additional_Course_Features.md)".

## Writing and sending a message [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9594)" }](https://track.frentix.com/issue/OO-9594) {: #create_notification}

Whoever writes a message decides in the same process who learns about it: only the subscribers or, in addition, selected members by e-mail, down to a single group.

The button "Create info message" opens a wizard with two steps. In the first step, you write the message and define under "Publication" whether it appears immediately ("Immediately") or only at a chosen point in time ("Individual date").

In the second and last step, you choose between two options under "Notification":

- **Subscription**: OpenOlat notifies only the subscribers of the messages.
- **Subscription & E-Mail**: OpenOlat also notifies the subscribers and additionally sends an e-mail on publication.

The selection "E-Mail recipient" only appears with "Subscription & E-Mail":

- **All members**: The e-mail goes to all owners, coaches and participants of the course, including the members of assigned groups and elements of the Course Planner (CPL). The number in brackets shows how many people that is.
- **Individual members**: You select the recipients yourself. The selection "Subscribers" stands on its own: with "All subscribers", everyone who has subscribed to the messages receives the e-mail, regardless of their role in the course.

Which selection appears under "Individual members" depends on whether groups or elements of the Course Planner are assigned to the course. If the course has neither an active group nor an element of the Course Planner, a single selection "Members" appears with the options "All owners", "All coaches" and "All participants".

If at least one active group or one element of the Course Planner is assigned to the course, the selection is structured by roles:

- **Owners**: "All owners".
- **Coaches**: "All coaches" reaches the coaches of the course and of all assigned groups and elements. "All course coaches" reaches only the coaches enrolled directly in the course. In addition, there is one option "All group coaches" per group and one option "All CPL coaches" per element, each with the name of the group or element.
- **Participants**: the same structure with "All participants", "All course participants", "All group participants" and "All CPL participants".

This way, an announcement that only concerns the course goes with "All course participants" to the participants enrolled directly in the course, without also sending the e-mail to the participants of the assigned groups. The same selection is available in the toolbar tool "Info messages".

## Further information {: #further_information}

**Mentioned on this page**<br>
[Subscriptions >](../personal_menu/Subscriptions.md)<br>
[Using Additional Course Features >](../learningresources/Using_Additional_Course_Features.md)

**Further reading**<br>
[Members management >](../learningresources/Members_management.md)<br>
[Using Group Tools >](../groups/Using_Group_Tools.md)<br>
[Course Planner: Overview >](../area_modules/Course_Planner.md)

**youtube**<br>
[Mitteilungen](<https://www.youtube.com/embed/3tAj19Avfkk>)<br>
[Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>)

[To the top of the page ^](#notification)
