# Personal tools: Calendar {: #calendar}

![Entry point to the personal calendar: the Calendar entry heads the list of Personal tools, ahead of Subscriptions, File Hub, Notes and Evidence of achievement](assets/pers_menu_calendar_v3_de.png){ class="aside-right lightbox" }

:fontawesome-regular-calendar-days:

The calendar function is available in various places:

* In the [group](../groups/Using_Group_Tools.md): <br>Access to the group calendar and any external imported calendars.

* In the [course](../area_modules/Courses.md): <br>Access to course dates and access to all calendars of integrated groups. Course calendars can be integrated into a course element as well as into the toolbar.<br>

![The course calendar is reachable in two ways: as the highlighted calendar icon in the course toolbar and as the Calendar entry in the course menu, here in the course Excel-Grundlagen](assets/pers_menu_calendar_course_v1_de.png){ class="shadow lightbox" }

<br>:octicons-device-camera-video-24: **Video Introduction (German)**: [Course calendar](<https://www.youtube.com/embed/tfx6UCYw8t8>){:target="_blank"}

* In the [personal menu](../personal_menu/index.md) [(Personal tools)](../personal_menu/Personal_Tools.md):<br> In addition to your personal appointments, all appointments from the various courses and groups of which you are a member can be combined in your personal calendar. This gives you an overview. External calendars can also be imported according to individual requirements.

![The calendars are nested: the personal calendar encloses the course calendar, which in turn encloses two group calendars. The appointments of the inner calendars are combined outwards](assets/pers_menu_calendar_overview_v1_de.png){ class="shadow lightbox" }


!!! info "Important"

    If you cannot find a calendar in the list of your personal tools, administrators have switched it off in the system administration:<br>
    `Administration > Core functions > Calendar`


[To the top of the page ^](#calendar)

---


## Create / Edit entry {: #create_entry}

To add a new appointment, click in the corresponding calendar field. A pop-up opens for the event details.

![The nine entries of an appointment from top to bottom: Calendar, Subject, All day with Beginning and End, Recurrence, Location, Color, Description, Visibility and Links, below them the Save and Cancel buttons in the Event details dialogue](assets/pers_menu_calendar_details_v1_de.png){ class="shadow lightbox" }

1. If you are a group member, first select the calendar in which you would like to create an appointment (personal calendar or group calendar) in the calendar pull-down menu at the top.

2. The "Event details" must include a subject.

3. A start and end date is also mandatory. The toggle button can be used to hide the time fields and create all-day appointments.

4. For recurrences, select one of the options in the selection field.

5. In the "Location" field you record where the appointment takes place.

6. With the "Color" selection field you give this appointment a color of its own.

7. In the "Description" field you add further details about the appointment.

8. Which details of an appointment are displayed for whom is described in the [Visibility](../personal_menu/Calendar.md#visibility) section.

9. You can only add links after the appointment has been created. Simply save the existing appointment and edit it again. You will then see an "Add link" button under "Links".


Appointments can be subsequently edited or deleted by clicking on the appointment and then on the "Edit" button.

An appointment can also be moved using drag & drop.


!!! info "Important"

    Links to course elements can only be created within the course calendar. All other calendars will display the message: _Link not possible_.



!!! danger "Attention"

    The "Delete this entry" button in the event details deletes the appointment permanently. The appointment cannot be restored!

[To the top of the page ^](#calendar)

---


## Recurring events {: #recurring_events}

In the event details, the desired frequency of recurring appointments can be selected under "Recurrence". As soon as a recurrence is selected, the input field appears with which the end of the series is defined (mandatory field).

![Highlighted are the Recurrence selection field with the value Monday - Friday and next to it the mandatory field ends on with the end date of the series, in the Event details dialogue](assets/pers_menu_calendar_recurrence_v1_de.png){ class="shadow lightbox" }

Serial appointments can also be edited. To do this, click on one of the appointments in the calendar. When saving the adjustment, you can select whether the change applies to all appointments in the series or only to the selected appointment. If all appointments are to be changed, those appointments that have not previously been customized will be changed.

[To the top of the page ^](#calendar)

---


## Visibility {: #visibility}

Specify here who can see the calendar entry.

![Highlighted is the Visibility selection field with the value Private, directly below the Description field in the Event details dialogue](assets/pers_menu_calendar_visibility_v1_de.png){ class="shadow lightbox" }

Depending on the type of calendar (Personal calendar, group calendar, course calendar) the three visibility levels "Private", "Only time information visible" and "Public" have different effects:

|| Personal calendar| Group calendar| Course calendar
---|---|---|---
**Private** | Only the person who created the entry is allowed to view the calendar entry, as the calendar is assigned to that person.| Only members of the group to which this calendar is assigned are allowed to view the calendar entry.| Only members of the course to which this calendar is assigned are allowed to view the calendar entry.
**Only time information visible** | As only the person who created the entry and nobody else can view the entry, these settings have no effect in this context. | All group and course members see the entry with all details. Additionally, all persons registered in OpenOlat or guests with access to the group/the course can see the time of the entry but no further details. | All group and course members see the entry with all details. Additionally, all persons registered in OpenOlat or guests with access to the group/the course can see the time of the entry but no further details.
**Public** | As only the person who created the entry and nobody else can view the entry, these settings have no effect in this context. | All group and course members see the entry with all details. Additionally, all persons registered in OpenOlat or guests with access to the group/the course can see all details of the entry. | All group and course members see the entry with all details. Additionally, all persons registered in OpenOlat or guests with access to the group/the course can see all details of the entry.

[To the top of the page ^](#calendar)

---


## Content {: #content}

The personal calendar displays:

1. The **personal appointments** you entered in this calendar yourself.
2. Other **standalone calendars** that have been selected in the calendar list for the shared view.<br> E.g. a group or course calendar.
3. **Aggregated calendars**<br> Aggregated calendars, for their part, have combined appointments from several different calendars. With aggregated calendars, it should be noted that OpenOlat cannot resolve where the events originally came from. An integrated aggregated calendar does not provide this origin information for the individual appointments, only which calendars are included.

!!! info "Aggregated calendar"

    An aggregated calendar is a collective feed that contains all calendars and their appointments that you have access to. You can use this feed from other applications to add or display all your OpenOlat appointments there. This saves you the work of having to insert each calendar individually (see Integrating calendars below). You can also use the gear icon in the list to import files and calendars and reset the appointments of an entire calendar.

[To the top of the page ^](#calendar)

---


## Calendar list {: #list}

The "Settings" button (small button with the cogwheel icon) opens the calendar list.

![Highlighted is the cogwheel icon in the calendar header, between the print icon and the feed icon: it opens the calendar list](assets/pers_menu_calendar_list_open_v1_de.png){ class="shadow lightbox" }

In the calendar list you will find all calendars that can be displayed in the current calendar (group, course, external and personal).

![The Type column distinguishes the calendars by icon into personal calendar, imported external calendar, course calendar and group calendar, next to it the columns Color, Name, Identifier and Show in the calendar list](assets/pers_menu_calendar_list_v1_de.png){ class="shadow lightbox" }

The "Type" column shows with an icon which kind of calendar it is: personal calendar, group calendar, course calendar or imported external calendar.

You can give the calendars different colors for better differentiation.

For course calendars, the "Identifier" column shows the identifier of the course. For personal and group calendars the column stays empty.

For each of these independent calendars, a toggle button in the "Show" column can be used to set whether the appointments are also displayed in your personal calendar. With the "Show all" and "Hide all" buttons you switch all calendars of the list on or off together. [:octicons-tag-16:{ title="from Release 18.1 (OO-7314)" }](https://track.frentix.com/issue/OO-7314)

Under the feed symbol you will find the URL with which this calendar can be integrated elsewhere.

Editing options are displayed under the icon with the 3 dots at the end of a line if they are independent calendars. (Editing is limited/not possible for aggregated calendars).

[To the top of the page ^](#calendar)

---


## Add calendars to the calendar list {: #add_to_list}

The course and group calendars are added to the calendar list of the personal calendar by default.
If you want to add another independent calendar to the calendar list, use the buttons above the list.

Calendar files (.ics) can be added using the "Import file" button.<br>
Clicking the small arrow next to it reveals the "Import from URL" entry.

![Highlighted is the Import file button at the top right of the calendar list, next to it the opened arrow menu with the Import from URL entry](assets/pers_menu_calendar_list_add_v1_de.png){ class="shadow lightbox" }


!!! info "Please note:"

    Use the buttons above the calendar list to add further **independent calendars** to the calendar list.

    * Another line appears = another independent calendar
    * You can specify in the calendar list whether the appointments in this calendar should be transferred to your personal calendar (activate the toggle button).
    * You can give the calendars different colors.

    The options to add or delete under the 3 dots at the end of a line, on the other hand, only edit this single **(aggregated) calendar**.

    * The calendars imported here do *not* appear in the calendar list, but are included in the now aggregated calendar.
    * You can *not* differentiate by color.

    **Recommendation:**<br> For a better overview, we recommend importing as a separate calendar (import via buttons in the header of the calendar list).



!!! tip "Tip"

    If your calendar appears empty or certain appointments are not displayed despite having been entered, the desired calendar may not be selected in the calendar list. (Toggle button not switched on.)

[To the top of the page ^](#calendar)

---


## Share OpenOlat calendar {: #share}

Using iCal (a standard for managing appointments), you can integrate the various OpenOlat calendars into another calendar, such as the Google calendar. To do this, click the iCal icon :o_icon_o_icon_rss: either in the calendar view or in the corresponding line of the calendar list and copy the iCal link.

[To the top of the page ^](#calendar)

---


## Managed calendar {: #managed}

Other calendars (such as those from the PerformX system) can also be integrated into the OpenOlat calendar as **managed calendars** on Feed. Managed appointments are marked with a lock symbol.


!!! info "Important"

    In course and group calendars, the editing options may differ from the personal calendar.

[To the top of the page ^](#calendar)

---


## Further information

[Course calendar](../learningresources/Using_Additional_Course_Features.md#course-calendar)<br>
[Group calendar](../groups/Using_Group_Tools.md)<br>
[Activate group calendar](../groups/Group_Administration.md#tools)<br>
[Course element Calendar](../learningresources/Course_Element_Calendar.md)<br>
[Activation of the calendar by administrators](../../manual_admin/administration/Core_functions.md#calendar_administration)<br>


[To the top of the page ^](#calendar)
