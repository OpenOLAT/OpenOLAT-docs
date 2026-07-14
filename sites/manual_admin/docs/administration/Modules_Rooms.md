# Module Rooms [:octicons-tag-16:{ title="from Release 21.0 (OO-9460)" }](https://track.frentix.com/issue/OO-9460){:target="_blank"} {: #module_rooms}


With the module "Rooms" you manage physical rooms in buildings centrally in OpenOlat and book them for events in the Course Planner. Location, capacity and occupancy of a room are maintained in one place and are available for event planning.


## Activate the module {: #activation}

The module is activated by a person with an administrative role:<br>
`Administration` > `Rooms` > `Settings`

Use the toggle "Module "Rooms"" to switch on the module. Only then do the segments "Buildings", "Rooms" and "Room Scheduling" appear, as well as the "Room management" area in the Course Planner.

!!! info "Events without rooms"
    If the module is switched off, these views are hidden and no rooms can be booked for events.


## Buildings [:octicons-tag-16:{ title="from Release 21.0 (OO-9522)" }](https://track.frentix.com/issue/OO-9522){:target="_blank"} {: #buildings}

Every room belongs to a building. In the segment "Buildings" you create the buildings of your organisation and maintain their master data. The action "Create" opens the dialog "Create building" with the following details:

* **Reference** (mandatory field): the decisive identification attribute of the building, for example an abbreviation or a house number. It is displayed wherever the building is referenced.
* **Description**: an optional plain-text name such as "Main building". If a description is set, it appears in addition to the reference.
* **Color**: a color for quick recognition of the building in lists and in the calendar.
* **Organisational restriction**: By default, a building is available to the entire organisation. If the toggle is activated, you select under "Administrative access" the organisations for which the building is available.
* **Location**: Under "Address" you enter the postal address. "Find on map" sets the position on the map. Via the map you open the location directly in Apple Maps or Google Maps.
* **Info-URL** and **Additional information**: optional additional details, such as a link to a building page or a note like "Collect the key at reception".

A building has the status "Active", "Inactive" or "Deleted". If a building is deactivated, all of its rooms become inactive as well. Deleting is only possible for an inactive building and also removes its rooms. As long as rooms of the building still have active bookings, the building cannot be deleted. The pre-defined filters "All", "Relevant" (active buildings only) and "Deleted" control which buildings the list shows.


## Rooms [:octicons-tag-16:{ title="from Release 21.0 (OO-9524)" }](https://track.frentix.com/issue/OO-9524){:target="_blank"} {: #rooms}

In the segment "Rooms" you create the individual rooms and assign them to a building. The dialog "Create room" offers, among others, the following fields:

* **Reference** (mandatory field): the identification attribute of the room, for example the room number.
* **Description**: an optional name of the room, such as "Auditorium".
* **#Seats** (mandatory field): the number of seats. The value must be greater than 0 and is used to detect insufficient capacity when booking.
* **Building** (mandatory field): the building the room belongs to. The active buildings are available for selection.
* **Additional information**: general additional details about the room.
* **Administrative information**: details that are visible only to persons with an administrative role, for example notes on the equipment.

In the room list you see for each room, among other things, the "Next event" and the "Occupancy rate" (utilisation of the current month). An icon opens the "Calendar" of the room with its occupancy, and "Details" opens the preview of the room with location and map. In addition to the table view, a calendar view is available.

As with the building, a room has the status "Active", "Inactive" or "Deleted". An inactive room can no longer be booked; bookings that have already been made remain valid. A room cannot be deleted as long as it still has active bookings.


## Room Scheduling [:octicons-tag-16:{ title="from Release 21.0 (OO-9525)" }](https://track.frentix.com/issue/OO-9525){:target="_blank"} {: #room_scheduling}

The segment "Room Scheduling" bundles all room bookings in one overview. This lets you see at a glance which rooms are occupied at what time and where there are conflicts.

Use the pre-defined filters "All", "Today", "Upcoming" and "With warnings" as well as the filters by building and room to narrow down the display. In addition to the table view there is a calendar view. Via "Open in Course Planner" you jump from a booking to the corresponding event in the Course Planner.

The column "Warnings" draws attention to conflicts:

* **Double booking**: "The room "..." is double-booked during this period!"
* **Not enough seats**: "There aren't enough seats!" if the number of participants exceeds the number of seats.
* **Inactive room**: "The room "..." is inactive!"


---

## Further information {: #further_information}

[Course Planner: Overview >](../../manual_user/area_modules/Course_Planner.md)<br>
[Course Planner: Events >](../../manual_user/area_modules/Course_Planner_Events.md)<br>

[To the top of the page ^](#module_rooms)
