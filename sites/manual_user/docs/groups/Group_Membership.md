# Become a group member {: #group_membership}

There are various ways in which people can become a member of a group. The following questions arise:

**Who adds the member to the group?**

Possible options are:

1)	The person adds themselves
2)	The group coach adds members
3)	Administrative roles such as user managers or group managers add people
4)	Automatic assignment via an external system

**Where does the assignment take place?**

Possible options are:

* a)	Directly in the group
* b)	In a course associated with the group
* c)	In other OpenOlat system areas
* d)	Outside OpenOlat

Both aspects can be combined as follows:

## 1a) The person adds themselves to the specific group {: #by_yourself}

![Highlighted "Join" button for a bookable group with access code in the list of published groups](assets/group_membership_offer_v1_de.png){ class="shadow lightbox" title="Published groups tab in the Groups area" }

For this, group coaches set up an offer in the group, under: `Group > Administration > Share`

![Button "Add offer" with the options Access code and Freely available, below it the notice that no offer has been created yet](assets/Gruppe_Freigabe.png){ class="shadow lightbox" title="Share tab of the group" }

Several options are available for the offer:

"Freely available" creates a booking without a password. Interested users join the group directly after booking. With the "Access code" option, a password is set for access and the user must enter the previously communicated password when booking. This is useful if not everyone should be given access to a group, but people should add themselves. Depending on the configuration by the system administrators, the "PayPal Checkout" option is also available. With this offer, the resource can be booked for a fee via PayPal.

![Choice between the offers Freely available and Access code and the paid PayPal Checkout](assets/Gruppe_Angebot_hinzufuegen.png){ class="shadow lightbox" title="Add offer dialog" }

**Where do users find groups they can book?**

Users find groups with offers in the "Published groups" tab. With a click on "Join" they book an offer and become members of the group.

![Highlighted "Join" button for a bookable group with access code in the list of published groups](assets/group_membership_offer_v1_de.png){ class="shadow lightbox" title="Published groups tab in the Groups area" }


**Overbooking** {: #overbooking}

If the group size has been limited, participants who want to join a group in which all places are already taken can be placed on a waiting list. (See [Create groups](Create_Groups.md#foreseen-number-of-participants)).

In the event of overbooking, corresponding notices appear, e.g.:

![Notice "Free places for group participants: -1 of 3 (overbooked)" above the member list](assets/group_membership_overbooking1_v1_de.png){ class="shadow lightbox" title="Members tab of the group" }

[To the top of the page ^](#group_membership)

## 2a) Group coaches add people directly to the group {: #add_groupmember}

As a group coach, select or create the desired group and open in it: `Group > Administration > Members`. There you add further participants and coaches with "Add member".

![Button "Add member" with the entry "Invite external members" above the member list, above it the settings for displaying members](assets/Gruppe_Mitglied_hinzufuegen1.png){ class="shadow lightbox" title="Members tab of the group" }

OpenOlat authors additionally have the "bulk search" available when adding members. This way, people whose OpenOlat ID or email address is known can be added directly and quickly.
Authors also have the option of inviting "external members" who do not yet have an OpenOlat account into the group. To do this, the specific email addresses of the persons must be entered.

### Adding a person to several groups at once {: #add_several_groupmembers}

Group coaches can also add a person directly to several groups, e.g. if an assignment to several groups is necessary for a study programme. To do this, go to the group area and select all groups to which the person is to be added. The prerequisite is that you are also a coach of the respective groups. Several buttons appear.

![Three selected groups, above them the buttons for the selection, among them "Manage members"](assets/Mehrere_Gruppen_waehlen.png){ class="shadow lightbox" title="My groups tab in the Groups area" }

Select "Manage members" here. A pop-up menu opens in which the members of all selected groups are listed together. Use the corresponding buttons to add further participants or coaches to all selected groups or to place them on the waiting list.

![Buttons "Add coach", "Add participant" and "Add to waiting list" above the members of the selected groups](assets/Gruppen_Konten_verwalten_TN_hinzufuegen.png){ class="shadow lightbox" title="Manage members dialog" }

The group membership may then still need to be confirmed. If you look in the member administration in one of the courses, you may find a corresponding note. Whether such confirmation by the new group members is required can be specified by system administrators.
![Highlighted role "Group member (Acceptance pending)" for a newly added member](assets/group_membership_confirm_when_several_members_added_v1_de.png){ class="shadow lightbox" title="Members tab of the group" }

[To the top of the page ^](#group_membership)

## 1b) The person adds themselves to a group within a course

Courses and groups can be linked to each other. If this is the case, people can also add themselves to a group at certain points within the course.

Specifically, this works via the course elements ["Enrolment"](../learningresources/Course_Element_Enrolment.md) and ["Topic Assignment"](../learningresources/Course_Element_Topic_Assignment.md). With these course elements, an OpenOlat group is created automatically. When people select a topic or enrol in a group, they are automatically added to the corresponding group.

![List of learning groups with occupied places, status and an "Enrol" link per group](assets/Kurs_Einschreibung.png){ class="shadow lightbox" title="Enrolment course element in the course" }

[To the top of the page ^](#group_membership)




## 2b) Course owners add people to a course-related group

Groups can also be linked to courses. If this is the case, course owners or persons with the right to use the course's "member administration" can also create and add groups there.

![Buttons "Create group" and "Add group" above the list of the course's groups](assets/Kurs_Mitgliederverwaltung.png){ class="shadow lightbox" title="Groups submenu of the members management" }

Via the displayed group name, you can access the group and then, as described under 2a), add people as a group coach.

Another option in the course is via the course's member list: `Members management > Members`. Here you can assign one or more course members to course-specific groups.

![Course roles of a member and below them the groups of the course, each with a checkbox for coach, participant and waiting list](assets/Mitglied_bearbeiten_Gruppe.png){ class="shadow lightbox" title="Edit member dialog in the members management" }

If you select several course members, for example, they can be assigned as participants or coaches to all groups available in the course via the "Edit" button that appears.

![Three selected groups, above them the buttons for the selection, among them "Manage members"](assets/Mehrere_Gruppen_waehlen.png){ class="shadow lightbox" title="My groups tab in the Groups area" }

![Three steps Edit member, Review changes and E-Mail Notification, plus a tick and a cross per group for coach, participant and waiting list](assets/MehrereMitglieder_bearbeiten.png){ class="shadow lightbox" title="Edit member dialog for several course members" }

The changes are then displayed again for review and an email notification can also be sent.


[To the top of the page ^](#group_membership)

## 3c) Assigned by persons with OpenOlat system roles

Certain people who are not group coaches of a group themselves can also add group members at an administrative level. This includes people with the OpenOlat role of group manager, user manager or administrator.

### Adding group membership in the user administration {: #add_groupmembers_in_usermanagement}

User managers can view existing group memberships and add new ones after opening the profile of a specific person in the "Groups" tab.

![Highlighted tab "Groups" with the "Add to groups" button, no group membership yet](assets/group_membership_by_user_management_v1_de.png){ class="shadow lightbox" title="Account profile in the user management" }

### Adding group membership in the group administration

Group managers additionally have the "Group management" tab in the group area and see all groups there. Similar to their own groups, people can also be added to the groups via this tab.

![Three phases of the group life cycle above the list of all groups in the system](assets/Gruppenverwaltung.png){ class="shadow lightbox" title="Group management tab in the Groups area" }

[To the top of the page ^](#group_membership)


## 4d) Automatically created group memberships - managed {: #add_groupmembers_automatically}

!!! info "Contact"

    If you have questions, contact your organisation.

If certain people are already grouped together in another system (e.g. HR software), these group memberships can also be mapped in OpenOlat. However, this requires middleware (Syncher), which can then automatically assign users to specific OpenOlat groups.

[To the top of the page ^](#group_membership)


---


## Accept or decline membership requests [:octicons-tag-16:{ title="from Release 20.3 (OO-9156)" }](https://track.frentix.com/issue/OO-9156){:target="_blank"} {: #reservation}

If you have been assigned to a course, group or educational product with a reservation requirement, the notification box **"Accept membership requests"** automatically appears in the group area. The box is collapsible and shows a card view with one entry per group.

The notification box is displayed as long as there are pending requests. It informs you that you have been invited to a group and prompts you to accept or decline the membership request.

**Example view** of the notification box for an invited user:
![Notification box "Accept membership requests" with the "Accept" and "Decline" buttons](assets/groups_membership_request_v1_en.png){ class="shadow lightbox" title="Dialog when logging in the first time" }

The following actions are available for each pending request:

- **Accept** (checkmark icon): Accepts the membership request. You are added as a member of the group.
- **Decline** (X icon, red): Declines the membership request.
- **Details**: Opens a lightbox with the description and the membership list of the group.

!!! note "Note"

    The notification box also appears on first login if both course and group requests are pending. In this case you see both panels (course and group) at the same time. Use the "Later" action to postpone processing to a later time.

Membership requests can also be accepted or declined directly on the info page of a course or educational product. There, the notification box is not collapsible.

For system administrators: [System-wide configuration of the invitation >](../../manual_admin/administration/Modules_Groups.md#data_privacy)

[To the top of the page ^](#group_membership)


---


## Further information {: #further_information}

[Create groups >](Create_Groups.md)<br>
[Using group tools >](Using_Group_Tools.md)<br>
[Leave a group >](Leave_a_Group.md)<br>
[Configure LTI Share for groups >](LTI_Share_groups.md)<br>
[System-wide configuration of the groups >](../../manual_admin/administration/Modules_Groups.md)<br> ...for system administrators

[To the top of the page ^](#group_membership)
