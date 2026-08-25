# Course Planner: Room management [:octicons-tag-16:{ title="from Release 21.0 (OO-9570)" }](https://track.frentix.com/issue/OO-9570){:target="_blank"} {: #course_planner_rooms}


## What's the purpose of Room management in the Course Planner? {: #purpose}

The "Room management" area in the Course Planner gives you a read-only overview of the room scheduling and the rooms in your organisational area of responsibility. This lets you see at a glance which room bookings exist for the events of your courses, where there are conflicts, and which rooms are available to you, without having to visit the administration.

[To the top of the page ^](#course_planner_rooms)

---

## Who has access? {: #access_roles}

Room management in the Course Planner is available to the following roles:

* Administrator
* Course planner
* Product owner
* Principal
* Element owner

Course owner, Master coach, Coach and Participant do not see Room management. Their role relates to running the course, not to its organisational planning.

The view is read-only for all roles listed: creating, editing or deleting rooms and buildings is not possible in the Course Planner, not even for administrators. The complete overview of rights can be found in the [rights matrix](../area_modules/Course_Planner.md#rights_matrix) of the Course Planner.

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

The segment "Room Scheduling" shows you all room bookings as an overview. Bookings arise from the events of your courses to which a room has been assigned. They also arise when you copy an implementation together with its events: [Adopt room bookings when copying](Course_Planner_Implementations.md#copy_rooms) [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9710)" }](https://track.frentix.com/issue/OO-9710){:target="_blank"}

Above the table you select the period of the display: "Today and upcoming", "Last 3 months" or "Custom" with a timerange of your own.

Use the pre-defined tabs "All", "Today", "Upcoming" and "With warnings" as well as the filters by building and room to narrow down the display. A full-text search is also available. In addition to the table view there is a calendar view with the views "Month", "Week", "Day" and "Year". Via "Open in Course Planner" you jump from a booking to the corresponding event in the Course Planner. Each row can be expanded to show the details of the booking.

The column "Warnings" draws attention to conflicts:

* **Double booking**: "The room "..." is double-booked during this period!"
* **Not enough seats**: "There aren't enough seats!" if the number of participants exceeds the number of seats.
* **Inactive room**: "The room "..." is inactive!"

![All room bookings with date, time, reference, building, event, number of participants and seats, warnings as an icon at the start of the row, in the Room Scheduling segment of the room management](assets/course_planner_rooms_scheduling_table_v1_en.png){ class="shadow lightbox" }

![The switch between table and calendar view with the views Month, Week, Day and Year, here the month view with the bookings in the calendar, in the Room Scheduling segment of the room management](assets/course_planner_rooms_scheduling_calendar_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#course_planner_rooms)

---

## Rooms {: #rooms}

The segment "Rooms" shows you the rooms you have access to through your organisational affiliation.

Use the pre-defined tabs "All" and "Relevant" as well as the filter by status (active/inactive), building and room to narrow down the display. A full-text search is also available. In addition to the table view there is a calendar view.

For each room you see, among other things, the building, the "Occupancy rate" (utilisation of the current month) and the "Next event". An icon opens the "Calendar" of the room with its occupancy, and "Details" opens a read-only preview of the room with location and map. Via the building link you jump directly to the building concerned.

![The accessible rooms with reference, description, status, seats, building, occupancy and next event, plus a calendar and a details icon per row, in the Rooms segment of the room management](assets/course_planner_rooms_list_v1_en.png){ class="shadow lightbox" }

!!! info "No deleted filter"

    In Room management of the Course Planner, deleted rooms are not shown. They only appear in the system administration under:<br>
    `Administration > Modules > Rooms > Rooms`<br>
    There, the "Deleted" tab lists the deleted rooms.

[To the top of the page ^](#course_planner_rooms)

---

## Manage rooms and buildings {: #admin_edit}

!!! info "Editing only in the administration"

    Creating, editing and deleting rooms and buildings takes place in the system administration under `Administration > Modules > Rooms` and requires administrative rights. The segments there are called "Settings", "Room Scheduling", "Rooms" and "Buildings". [Manage rooms (administration) >](../../manual_admin/administration/Modules_Rooms.md)

[To the top of the page ^](#course_planner_rooms)

---

## Further information {: #further_information}

[Course Planner: Overview >](../area_modules/Course_Planner.md)<br>
[Course Planner: Events >](../area_modules/Course_Planner_Events.md)<br>
[Manage rooms (administration) >](../../manual_admin/administration/Modules_Rooms.md)<br>

[To the top of the page ^](#course_planner_rooms)
