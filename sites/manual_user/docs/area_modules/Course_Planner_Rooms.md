# Course Planner: Room management [:octicons-tag-16:{ title="from Release 21.0 (OO-9570)" }](https://track.frentix.com/issue/OO-9570){:target="_blank"} {: #course_planner_rooms}


## What's the purpose of Room management in the Course Planner? {: #purpose}

You see at a glance which rooms are booked for the events of your courses and where bookings overlap.

The "Room management" area shows you the room scheduling and the rooms your organisation is responsible for. The information is available to you for reading in the Course Planner, without visiting the administration.

[To the top of the page ^](#course_planner_rooms)

---

## Who has access? [:octicons-tag-16:{ title="from Release 21.0.3 (OO-9721)" }](https://track.frentix.com/issue/OO-9721){:target="_blank"} {: #access_roles}

Room management in the Course Planner is available to two roles:

* Administrator
* Course planner

All other roles do not see the area, including Product owner, Element owner and Principal. Course owner, Master coach, Coach and Participant work on running the course, not on its organisational planning.

Both roles read the information. You create and change rooms and buildings in the system administration, as an administrator too. The complete overview of rights can be found in the [rights matrix](../area_modules/Course_Planner.md#rights_matrix) of the Course Planner.

[To the top of the page ^](#course_planner_rooms)

---

## Where can I find Room management? {: #access}

You will find Room management in the Course Planner under<br>
`Course Planner > Tools > Room management`

!!! tip "Requirement"

    Room management is only available if the module "Rooms" has been activated by a system administrator. If the area is not available, please contact your system administrator or the support of your OpenOlat instance.

[To the top of the page ^](#course_planner_rooms)

---

## Room Scheduling {: #room_scheduling}

Under "Room Scheduling" you see every booking that has arisen from the events of your courses.

A booking arises as soon as you assign a room to an event. It also arises when you copy an implementation together with its events: [Adopt room bookings when copying](Course_Planner_Implementations.md#copy_rooms) [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9710)" }](https://track.frentix.com/issue/OO-9710){:target="_blank"}

Above the table you select the period of the display: "Today and upcoming", "Last 3 months" or "Custom" with a timerange of your own.

Use the pre-defined tabs "All", "Today", "Upcoming" and "With warnings" as well as the filters by building and room to narrow down the display. A full-text search is also available. Above the table on the right you switch between table and calendar; the calendar offers the views "Month", "Week", "Day" and "Year". The switch appears as soon as the display holds at least one booking. Via "Open in Course Planner" you jump from a booking to the corresponding event in the Course Planner; the event opens in a new browser tab. [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9641)" }](https://track.frentix.com/issue/OO-9641){:target="_blank"}

![All room bookings with date, time, reference, building, event, number of participants and seats, warnings as an icon at the start of the row, in the Room Scheduling of the room management](assets/course_planner_rooms_scheduling_table_v1_en.png){ class="shadow lightbox" }

### Details of a booking {: #booking_details}

For every booking you see which course, which teachers and which rooms belong to it.

To do so, expand the row of the table. The detail view shows the title and the reference of the event with its status badge, any warnings highlighted, the subjects as well as date, time, number of participants, absences and compulsory presence. A location appears if one is recorded for the event. Below it you find the teachers, the corresponding course as a course card and the booked rooms as room cards. If more than one room is booked, the room of the expanded row is shown under "Room", the others under "More rooms for this booking".

![Key values, teacher and two room cards, the first under Room, the second under More rooms for this booking, in the expanded row of a booking](assets/course_planner_rooms_scheduling_details_v1_en.png){ class="shadow lightbox" }

### View a booking in the calendar [:octicons-tag-16:{ title="from Release 21.0.3 (OO-9715)" }](https://track.frentix.com/issue/OO-9715){:target="_blank"} {: #booking_callout}

A click on a booking in the calendar shows you which event occupies the room.

In the calendar, every booking appears as a calendar entry labelled with the reference of the room and the title of the event, preceded by the time. Its colour is the colour of the building. A click on the calendar entry opens the "Booking" window with the reference of the room and its description, the title of the event with its reference, the date and the time. Via "Open in Course Planner" you reach the event in the Course Planner.

The window is available in every calendar view of the room management: in the room scheduling, in the room list and in the calendar of a single room row. In the table view, the expanded row leads to the [details of a booking](#booking_details) instead.

![The Booking window with the reference of the room, event, date, time and the action Open in Course Planner, above a booking in the year view](assets/course_planner_rooms_scheduling_callout_v1_en.png){ class="shadow lightbox" }

![The switch between table and calendar view with the views Month, Week, Day and Year, here the month view with the bookings in the calendar, in the Room Scheduling of the room management](assets/course_planner_rooms_scheduling_calendar_v1_en.png){ class="shadow lightbox" }

### Warnings {: #warnings}

You can tell from a booking whether room and event match.

In the table, the column "Warnings" points this out. In the calendar, the calendar entry carries a warning triangle in addition to the colour of its building. There are three warnings:

* **Double booking**: "The room "..." is double-booked during this period!"
* **Not enough seats**: "There aren't enough seats!" if the number of participants exceeds the number of seats.
* **Inactive room**: "The room "..." is inactive!"

[To the top of the page ^](#course_planner_rooms)

---

## Rooms {: #rooms}

Under "Rooms" you see which rooms are available to you and how heavily they are booked.

The list holds the rooms your organisation is responsible for. Use the pre-defined tabs "All" and "Relevant" as well as the filters by status (active/inactive), building and room to narrow down the display. A full-text search is also available. Here, too, you switch to the calendar above the table on the right.

For each room you see, among other things, the building, the "Occupancy rate" (utilisation of the current month) and the "Next event". Via "Calendar" you open the occupancy of the room, via "Details" a preview of the room with location and map. Via the building link you reach the building concerned.

In the calendar of a single room row, too, a click on a booking opens the ["Booking" window](#booking_callout).

![The accessible rooms with reference, description, status, seats, building, occupancy and next event, plus a calendar and a details icon per row, in the room list of the room management](assets/course_planner_rooms_list_v1_en.png){ class="shadow lightbox" }

!!! info "Deleted rooms in the administration"

    Room management of the Course Planner holds the active and the inactive rooms. Deleted rooms appear in the system administration under:<br>
    `Administration > Modules > Rooms > Rooms`<br>
    There, the "Deleted" tab lists the deleted rooms.

[To the top of the page ^](#course_planner_rooms)

---

## Manage rooms and buildings {: #admin_edit}

!!! info "Editing only in the administration"

    Creating, editing and deleting rooms and buildings takes place in the system administration under `Administration > Modules > Rooms` and requires administrative rights. There you find "Settings", "Room Scheduling", "Rooms" and "Buildings". [Manage rooms (administration) >](../../manual_admin/administration/Modules_Rooms.md)

[To the top of the page ^](#course_planner_rooms)

---

## Further information {: #further_information}

[Course Planner: Overview >](../area_modules/Course_Planner.md)<br>
[Course Planner: Implementations >](Course_Planner_Implementations.md)<br>
[Course Planner: Events >](../area_modules/Course_Planner_Events.md)<br>
[Module Rooms (Administration) >](../../manual_admin/administration/Modules_Rooms.md)

[To the top of the page ^](#course_planner_rooms)
