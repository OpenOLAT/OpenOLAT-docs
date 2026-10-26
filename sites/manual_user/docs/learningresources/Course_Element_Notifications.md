# Course Element "Info messages" [:octicons-tag-16:{ title="from Release 21.1 (OO-9761)" }](https://track.frentix.com/issue/OO-9761){:target="_blank"} {: #notification}


## Profile

Name | Info messages
---------|----------
Icon | :o_icon_o_infomsg_icon:
Available since | New edition with release 18
Functional group | Administration and organisation
Purpose | Info messages in the course structure (course menu)
Assessable | no
Specialty / Note |



:octicons-device-camera-video-24: **Video Introduction (German)**: [Info messages](<https://www.youtube.com/embed/3tAj19Avfkk>){:target="_blank"}

With the course element "Info messages", you inform the members of a course at a fixed place in the course menu, for example about a change of date or new documents. The info messages appear in the course and additionally under `User tools > Subscriptions` in the notifications of everyone who has subscribed to them. An info message can be a short text or bring more extensive information as a file attachment (by default, max. 5 MB).

An info message can be published immediately or at a later point in time and additionally sent by e-mail. How to choose the recipients is described in the section [Writing and sending an info message](#create_notification).

## Configuration in the course editor Tab "Info messages configuration" {: #configuration_notification}

In the tab "Info messages configuration", you determine how long and how many info messages the course element shows, whether they are subscribed to automatically and who creates them.

**Display:** The maximum number of days determines how long an info message remains visible in the course. The maximum number of info messages determines how many info messages the course element shows at the same time. By default, these are 90 days and 10 info messages.

**Subscribe automatically:** If "Subscribe to these info messages automatically after reading" is switched on (default), the members of the course subscribe to the info messages as soon as they open the course element. If you switch the option off, participants subscribe to the info messages themselves if needed.

:octicons-device-camera-video-24: **Video Introduction (German)**: [Subscriptions](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

In the "User rights" section, you define which course roles are allowed to create and manage info messages. By default, owners and coaches create and manage the info messages, participants read them. Owners keep both rights in any case.

The members of the course also see subscribed info messages in the personal menu under `User tools > Subscriptions`, see also the page [Subscriptions](../personal_menu/Subscriptions.md).

!!! info "Important"

    An info message is limited to 32,000 characters. In the lower right corner of the text field of the info message, OpenOlat shows how many characters are already used and reports on saving if the limit is exceeded. The HTML code of the info message is counted, which is why the number is higher than the number of visible characters.

!!! tip "Tip"

    For an announcement to the entire course that needs no place in the course menu, the tool of the same name "[Info messages](../learningresources/Using_Additional_Course_Features.md)" in the toolbar is suitable. It cannot be configured: owners and coaches create info messages there, participants subscribe to them themselves if needed. Use the course element if the info messages should appear at a specific place in the course menu or if you want to define display, user rights, automatic subscription and access yourself.

## Writing and sending an info message [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9594)" }](https://track.frentix.com/issue/OO-9594) {: #create_notification}

Whoever writes an info message decides in the same process who learns about it: only the subscribers or, in addition, selected members by e-mail, down to a single group.

The button "Create info message" opens a wizard with two steps. In the first step, you write the info message and define under "Publication" whether it appears immediately ("Immediately") or only at a chosen point in time ("Individual date").

In the second and last step, you choose between two options under "Notification":

- **Subscription**: OpenOlat notifies only the subscribers of the info messages.
- **Subscription & E-Mail**: OpenOlat also notifies the subscribers and additionally sends an e-mail on publication.

The selection "E-Mail recipient" only appears with "Subscription & E-Mail":

- **All members**: The e-mail goes to all owners, coaches and participants of the course, including the members of assigned groups and elements of the Course Planner (CPL). The number in brackets shows how many people that is.
- **Individual members**: You select the recipients yourself. The selection "Subscribers" stands on its own: with "All subscribers", everyone who has subscribed to the info messages receives the e-mail, regardless of their role in the course.

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
