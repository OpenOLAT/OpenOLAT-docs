# Personal tools: Calendar

![pers_menu_calendar_v1_de.png](assets/pers_menu_calendar_v1_de.png){ class="aside-right lightbox"}

![icon_calendar](assets/icon_calendar.png)

You have threefold access to the calendar:

* in your [personal menu](../personal_menu/index.md): Overview of the dates of all your groups and courses
* in the [group](../groups/Using_Group_Tools.md): Access to the group calendar and any external imported calendars.
* in the [course](../area_modules/Courses.md): Access to course dates and access to all calendars of integrated groups. Calendars can be integrated into courses both in the course run and in the toolbar.

Your personal calendar automatically contains the dates of the courses and groups you are a member of. The course and group calendars are added to the calendar list of the personal calendar and all appointments are displayed together in the personal calendar. You can edit the calendar list and define yourself which calendars are ultimately merged into your personal calendar.

If you cannot find a calendar in the list of your personal tools, this has been switched off system-wide by an administrator.


## Create / Edit entry

* In order to add a new event to your calendar, you have to click inside the appropriate calendar field. 
* If you are a group member you have to first select from the pull-down menu to which calendar (personal calendar or group calendar) you want to add your new event. 
* Events can be edited or deleted by clicking on the event an then "Edit". 
* An event can also be moved by drag and drop.

The "Event details" must include a title as well as a start and end date. You can also add a description, define a recurrence option and the type of visibility. You can also use different colors for different calendars.

!!! info "Note"

    Links to course elements, entries in the library or external documents can only be added in a **second step** after the initial calendar entry creation.
    
    Links to course elements can only be created within the course calendar. All other calendars will display the message: _Link not possible_.

![Calendar linking](assets/calendar_connection_EN.png){ class="shadow lightbox" }

!!! warning "Attention"

    The "Delete this entry" button in the appointment details deletes the appointment permanently. The appointment cannot be restored!

### Recurring events

Recurring events are events, which are repeated regularly over a certain time period. In the event details under "Recurrence" the desired frequency can be chosen. After a date need to be set, which defines the end of the recurrence.

Recurring events can be edited as well. After saving the adaption it can be chosen, if it is valid for the whole recurrence or only this single event. If all events are changed, only these events get changed, which haven't been adapted before.

![Recurring events](assets/recurringevent_EN.png){ class="shadow lightbox" }


### Visibility {: #visibility}

Please determine who may see your calendar's entries.

Depending on the type of calendar (Personal calendar, group calendar, course calendar) the three visibility levels "Private", "Time visible only" and "Public" have different effects:

|| Personal calendar| Group calendar| Course calendar  
---|---|---|---  
**Private** | Only the creator is allowed to view the entry, as it is his or her calendar.| Only group members are allowed to view entries, as it is the calendar of the group. | Only course members are allowed to view entries, as it is the calendar of the course.  
**Time visible only** | As only the creator is allowed to view the entry, these visibility levels have no effect in this context. | All group and course members can view the entries including all details. Additionally all registered OpenOlat users or guests with access to the group or course are allowed to view the time of the entries, but no further details. | All group and course members can view the entries including all details. Additionally all registered OpenOlat users or guests with access to the group or course are allowed to view the time of the entries, but no further details.
**Public** | As only the creator is allowed to view the entry, these visibility levels have no effect in this context. | All group and course members can view the entries including all details. Additionally all registered OpenOlat users or guests with access to the group or course are allowed to view the entries including all details. | All group or course members can see the entry with all the details. In addition, all OpenOlat users or guests with access to the group/course can see all the details of the entry.

### Group calendar in connection with course calendars

In a group calendar group participants will see all entries of group members, no matter if appointments are private or public. If a group is assigned to a course the following entries will be displayed there for group participants: public entries of that group, the group's own group calendar entries of that group member as well as course-specific calendar entries. Persons who are not members of that group will not see the calendar entries of other groups in their course. If several groups are assigned to a course members will only see their own group calendar entries but not those of other groups.

### Calendar list (in the Personal Tools area)

![Calendar settings](assets/calendar.gif){ class="shadow lightbox" }

The "Settings" button (small button with the cogwheel icon) opens the calendar list, in which you can show and hide the individual calendars and specify which calendar should be displayed in which color.

In the calendar list you will find all other calendars integrated into your current calendar (group, course or personal). Click on the color to select a different color. Click on the color to select another color.  Use the "**Visible**" and "**Aggregated**" columns to determine whether the selected calendar should be displayed or whether it should be integrated into the aggregated calendar feed.

The aggregated calendar is a collective feed that contains all calendars and their appointments that you have access to. You can use this feed from other applications to add or display all your OpenOlat appointments there. This saves you the work of having to insert each calendar individually (see Integrating calendars below). You can also use the gear icon in the list to import files and calendars and reset the dates of an entire calendar.

![Calendar list](assets/calendar_list.gif){ class="shadow lightbox" }

If your calendar appears empty or certain appointments are not displayed despite having been entered, the desired calendar may not be selected in the calendar list.

### Calendar integration

Using iCal (a standard for managing appointments), you can integrate the various OpenOlat calendars into another calendar, such as the Google calendar. To do this, click on the iCal icon ![RSS Symbol](assets/icon_rss_small.png){ width=24px } either in the calendar view or in the corresponding line of the calendar list and copy the iCal link. Other calendars, such as those from the PerformX system, can also be integrated into the OpenOlat calendar as managed calendars in this way. Managed appointments are marked with a lock symbol.

!!! info "Note"

    If you cannot find a "Calendar" course element in your OpenOlat instance, this has been switched off system-wide by an administrator.

## Further information

[Course Calender](../learningresources/Using_Additional_Course_Features.md#course-calendar)<br>
[Group Calender](../groups/Using_Group_Tools.md)<br>
[Activate group calender](../groups/Group_Administration.md#tools)<br>
[Course element calender](../learningresources/Course_Element_Calendar.md)<br>
[Activation of calenders by administrators](../../manual_admin/administration/Core_functions.de.md#calender-administration)<br>

