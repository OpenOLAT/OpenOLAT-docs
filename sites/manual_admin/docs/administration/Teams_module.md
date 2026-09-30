# Microsoft Teams module {: #teams_module}

Microsoft Teams is the web conferencing solution from Microsoft. In courses and groups, course owners, coaches and group coaches use it to create online meetings that participants join from within OpenOlat. Administrators define for the whole instance which types of online meetings are available, for example whether every meeting needs a date and therefore appears in the calendar.

You configure the module in the system administration under:<br>
`Administration > External tools > Microsoft Teams`

The page [External Tools: Overview](External_Tools_-_Administration.md#_microsoft_teams) describes the prerequisites for the connection to Microsoft 365. How course owners and coaches create individual online meetings is described in the user manual in the chapter [Course Element "Microsoft Teams"](../../manual_user/learningresources/Course_Element_Microsoft_Teams.md).

---

## Tab "Configuration" [:octicons-tag-16:{ title="from Release 15.4 (OO-5124)" }](https://track.frentix.com/issue/OO-5124) {: #tab_config}

In the tab "Configuration", you switch Microsoft Teams on for the instance and define where and with which variants online meetings may be created.

### Configuration of Microsoft Teams integration {: #teams_config}

The fields "Activate for" and "Online-Meetings without date/permanent" only appear when the module is switched on.

#### Module "Microsoft Teams" {: #module_enabled}

Switches Microsoft Teams on or off for the whole instance. If the module is switched off, the course element "Microsoft Teams" is not available for selection in the course editor.

#### Activate for {: #activate_for}

Enables Microsoft Teams individually for the places where online meetings are created: Course element "Microsoft Teams", Course events, Course element "Appointment scheduling", Groups and Supervisor chat.

#### Online-Meetings without date/permanent [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9666)" }](https://track.frentix.com/issue/OO-9666) {: #permanent_meetings}

Determines whether permanent reservations may be created in courses and groups. A permanent reservation is an online meeting without a start and an end. The room is permanently open, but it does not appear in any calendar.

With "On" (default), the selection "Add online-meeting" offers the variant "Add permanent meeting room". With "Off", this variant is missing in the course element "Microsoft Teams", in the group tool "Microsoft Teams" and in the course tool "Teams". Every new online meeting then needs a start and an end and appears in the calendar. This helps organisations that want to plan all online meetings and keep track of them in the calendar.

Existing permanent reservations are kept when you set the option to "Off". They can still be opened, edited and saved without a date. The option only prevents new permanent reservations from being created.

The BigBlueButton module has the same setting under the name "Online-Meetings without date", see [BigBlueButton module](BigBlueButton_module.md#tab_config).

#### Application (client) ID, Client secret, Tenant GUID {: #tenant_credentials}

If access data for the Microsoft 365 tenant is stored in the server configuration, the tab shows it in these three fields for viewing. It can only be changed in the server configuration. frentix customers contact the frentix support for a change: [support@frentix.com](mailto:support@frentix.com)

---

## Tab "Online-meetings" {: #tab_online-meetings}

In the tab "Online-meetings", you keep track of all Microsoft Teams online meetings in the instance and clean up meetings that are no longer needed.

The table shows "Name", "Without date", "Start", "End" and "Context" for each meeting. A click on the context opens the course or the group in which the meeting was created. Use the search to find individual meetings. With "Delete" you remove one meeting, or several selected meetings at once.

---

## Tab "Calendar" {: #tab_calendar}

In the tab "Calendar", you see when many online meetings take place at the same time and detect bottlenecks early. The view opens in the week view and shows all Microsoft Teams online meetings with start and end. Permanent reservations do not appear here because they have no date.

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[External Tools: Overview >](External_Tools_-_Administration.md)<br>
[Course Element "Microsoft Teams" >](../../manual_user/learningresources/Course_Element_Microsoft_Teams.md)<br>
[BigBlueButton module >](BigBlueButton_module.md)

**Further reading**<br>
[Using Group Tools >](../../manual_user/groups/Using_Group_Tools.md)<br>
[Virtual classrooms >](../../manual_user/basic_concepts/Virtual_classrooms.md)

[To the top of the page ^](#teams_module)
