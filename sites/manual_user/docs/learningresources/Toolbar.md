# Toolbar: Overview {: #toolbar}

The toolbar sits at the top of the page directly below the main navigation and shows the icons of the tools.

**Example participant**:

![Toolbar from a participant's point of view with the tools from Info page (info icon) to Course search, including Info messages (megaphone) and Blog (blog icon), on the right My course](assets/toolbar_example_course_participant_v2_en.png){ class="shadow lightbox" title="Toolbar of a course, participant view · 2026.10.27" }

**Example course owner/coach**:

![Toolbar from a course owner's point of view with additionally Administration, status Published and the role switcher, in between the same tools from Info page to Course search](assets/toolbar_example_course_owner_v2_en.png){ class="shadow lightbox" title="Toolbar of a course, course owner view · 2026.10.27" }

The course owner decides whether the toolbar is visible to course participants. It is always visible to coaches and owners.<br>
[More >](#show_icons)

If the toolbar is displayed for participants, course owners can decide which icons are displayed there and switch them on and off for each course as needed.<br>
[More >](#show_icons)

The tools then appear either in the toolbar or under "My course".

## Profile

Name | Toolbar
---------|----------
Available since | Release 10.0 (2014)

---

## Available icons {: #available_icons}

### Administration {: #admin}

![Tool Administration highlighted at the far left of the toolbar: the menu owners and authorised coaches use to manage the course. Next to it the status Published and the tools starting with Info page](assets/toolbar_admin_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

The course administration is only displayed to those authorized to edit, not to the participants. Many menu options for administration and editing can be accessed there.<br>
[More >](../learningresources/Administration.md)

---

### Status [:octicons-tag-16:{ title="from Release 13.0 (OO-3584)" }](https://track.frentix.com/issue/OO-3584) {: #status}

![Status Published highlighted as a green button with a selection arrow: this is where authorised persons change the status of the course. To its right the tools from Info page with its info icon](assets/toolbar_status_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

The status is only displayed to those authorized to edit, not to participants. The status of the course can be changed here.<br>
[More >](../learningresources/Access_configuration.md)

---

### Info page [:octicons-tag-16:{ title="from Release 21.1 (OO-9758)" }](https://track.frentix.com/issue/OO-9758){:target="_blank"} {: #info_page}

![Tool Info page with the info icon highlighted as the first tool of the toolbar](assets/toolbar_course_info_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

Anyone who wants to know what a course is about opens the description of the course with the tool "Info page" and its info icon, for example with the execution period and location. Interested people see the same details before they enter the course.<br>
[More >](../learningresources/Info_page.md)

---

### Learning path [:octicons-tag-16:{ title="from Release 15.0 (OO-4300)" }](https://track.frentix.com/issue/OO-4300) {: #learning_path}

![Tool Learning path highlighted in the toolbar, to its left the Info page with the info icon, to its right Calendar, Info messages and the other tools](assets/toolbar_learning_path_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

**Access by participants**<br>
The learning path icon in the toolbar gives learners an overview of their progress in all course elements. Depending on the columns selected, additional information such as the type of execution and dates can also be displayed. This makes it easy for learners to keep track of their activities in the course.

![Learning path table with all course elements, per element progress in percent, status, obligation, processing time and date completed](assets/Mein_Lernpfad.png){ class="shadow lightbox" title="Learning path from the participant's view" }

**Access by course owners and coaches**<br>
Course owners and coaches can use the "Learning path" link to first get an overview of all participants and then, in the next step, select a person to display their learning progress.

---

### Calendar {: #calendar}

![Tool Calendar highlighted in the toolbar, to its left Info page and Learning path](assets/toolbar_calendar_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

*One* calendar can be activated per course. There are two options for integration. The calendar can either be displayed as a [calendar course element](../learningresources/Course_Element_Calendar.md) or in a central position at the top of the course toolbar.

In addition to the course calendar, OpenOlat offers other calendars:

- [Personal calendar >](../personal_menu/Calendar.md)
- [Group calendar >](../groups/Using_Group_Tools.md)

New events are easily created by clicking on the desired date. You can then set the title, description, start and end, possibly a location, possible repetitions and the visibility. The event then appears in the calendar or in all instances of the course calendar and can be edited by clicking on the date and selecting the "Edit" option.

The "Edit" option also gives you access to additional calendar tabs and allows you to set links to course elements used in the course or to external websites. If you want to delete all events of a course calendar, simply click on the gear icon in the calendar area and select "Reset calendar".

Course calendars are also automatically transferred to the personal calendars of the course members. This means that all events can also be accessed directly via the personal OpenOlat calendar. The same applies to group calendars. For group calendars, the write and read permissions that members receive can be set in the group administration.

By default, only owners of a course have write access to the calendar. Course participants only have read access, meaning they cannot create new events or edit existing ones. However, if you add the calendar as a course element, you can configure the permissions in the course editor in the "Access" tab.

---

### Participant list [:octicons-tag-16:{ title="from Release 15.0 (OO-4168)" }](https://track.frentix.com/issue/OO-4168) {: #participant_list}

![Tool Participant list with the people icon highlighted in the toolbar, to its left Info page, Learning path and Calendar, to its right Info messages and the other tools](assets/toolbar_participant_list_v2_en.png){ class="shadow lightbox" title="Toolbar of a course, participant view · 2026.10.27" }

The participant list can also include contact options in the list of all course members.<br>
[More >](../learningresources/Course_Element_Participant_List.md)

---

### Info messages {: #notifications}

![Tool Info messages with the megaphone icon highlighted in the toolbar](assets/toolbar_notifications_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

In the info messages, teachers can store information about the entire course centrally.<br>
[More >](../learningresources/Course_Element_Notifications.md)

---

### E-Mail {: #email}

![Tool E-Mail with the envelope icon highlighted in the toolbar](assets/toolbar_email_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

E-mails can be sent from various places. In addition to the [personal menu](../personal_menu/E-Mail.md), the icon in the toolbar is a good way to offer course members a contact option with quick access.<br>
[More >](../learningresources/Course_Element_EMail.md)

---

### BigBlueButton (or other virtual classrooms) [:octicons-tag-16:{ title="from Release 15.4 (OO-5151)" }](https://track.frentix.com/issue/OO-5151) {: #BBB}

![Icon BigBlueButton highlighted in the toolbar](assets/toolbar_BBB_v1_de.png){ class="shadow lightbox" title="Toolbar of a course" }

As an alternative to a course element, access to a video conferencing tool can also be enabled via an icon in the toolbar. In addition to BigBlueButton, other installed video conferencing tools can also be displayed in the toolbar (e.g. Microsoft Teams or Zoom).<br>
[More >](../learningresources/bigbluebutton/index.md)

---

### Blog {: #blog}

![Tool Blog with the blog icon highlighted in the toolbar, to the left of Wiki](assets/toolbar_blog_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

Multiple blogs can be integrated into OpenOlat. Access via the icon in the toolbar is a good option if the blog content relates to the entire course.<br>
[More >](../learningresources/Course_Element_Blog.md)

---

### Wiki {: #wiki}

![Tool Wiki with the globe icon highlighted in the toolbar, to its left Blog, to its right Forum](assets/toolbar_wiki_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

Access to a central wiki for the entire course can be set up in the toolbar.<br>
[More about creating a wiki >](../learningresources/Wiki.md)<br>
[More about the course element Wiki >](../learningresources/Course_Element_Wiki.md)

---

### Forum {: #forum}

![Tool Forum with the speech bubble icon highlighted in the toolbar, to its left Wiki, to its right Documents](assets/toolbar_forum_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

In addition to the "Forum" course element, there is also the option of displaying a central forum for the entire course in the course toolbar. This is useful if the course only includes *one* forum that is to be permanently available. However, settings such as pseudonymization or moderation rights cannot be set here.<br>
[More >](../learningresources/Course_Element_Forum.md)

---

### Documents {: #documents}

![Tool Documents with the folder icon highlighted in the toolbar, to its right Course search](assets/toolbar_documents_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

Via this link, the teacher can make important course documents available for download in one central location. Learners can download the documents, receive notifications when new documents are available (subscribe), and send the files by e-mail if necessary. However, the configuration options are not as extensive as those of the "Folder" course element.<br>
[More >](../learningresources/Storage_folder.md)

---

### Events {: #events}

![Icon Events highlighted in the toolbar](assets/toolbar_events_v1_de.png){ class="shadow lightbox" title="Toolbar of a course" }

If the appointment and absence management is enabled, it can be accessed here to view or record events and absences.<br>
[More >](../learningresources/Toolbar_Events.md)

---

### Glossary {: #glossary}

![Tool Glossary with the mortarboard icon and a selection arrow highlighted in the toolbar, to its left Documents, to its right Course search](assets/toolbar_glossary_v2_en.png){ class="shadow lightbox" title="Toolbar of a course, participant view · 2026.10.27" }

If a glossary has been linked to the course, it can also be accessed from the toolbar. A glossary can be used to explain the terms of a course, a subject or an event. The terms are automatically sorted alphabetically and can be accessed by clicking on the corresponding initial letter.<br>
[More >](../learningresources/Glossary.md)

---

### Course chat {: #chat}

![Icon Course chat highlighted in the toolbar](assets/toolbar_course_chat_v1_de.png){ class="shadow lightbox" title="Toolbar of a course" }

The chat enables synchronous exchange between the course members.<br>
[More >](../basic_concepts/Chat.md)

---

### Course search [:octicons-tag-16:{ title="from Release 11.3 (OO-2581)" }](https://track.frentix.com/issue/OO-2581) {: #course_search}

![Tool Course search with the magnifier icon highlighted in the toolbar](assets/toolbar_search_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

Depending on where the search is started, different areas are searched. The course search is performed with the icon in the toolbar.<br>
[More >](../basic_concepts/Search_in_Course.md)

---

### External course tools [:octicons-tag-16:{ title="from Release 21.0 (OO-9488)" }](https://track.frentix.com/issue/OO-9488) {: #external_tools}

![External course tool Timetable with a calendar icon highlighted to the right of Course search](assets/course_toolbar_with_external_tools_v2_en.png){ class="shadow lightbox" title="External course tool in the course toolbar · 2026.10.02" }

External course tools lead from the toolbar directly to web applications outside OpenOlat, for example to an absence management system, a school information page, a partner portal, a room booking tool or an external mail or calendar system. Course owners set up to **four external course tools** per course, under `Course > Administration > Settings > Tab "Toolbar"`. The rows "External course tool 1" to "External course tool 4" appear there as soon as the checkbox "On" is activated for "Toolbar visible for participants".

Configurable per tool:

- **Name**: label of the tool in the toolbar
- **URL**: must start with `http://` or `https://`
- **Icon**: selectable from the icon catalog (e.g. Link, E-mail, Calendar, Timetable, Absence management, School portal, Booking, Videos, Files)
- **Visible to**: configurable separately for *Participants*, *Coaches* and *Owners and users with administrative roles*. Each option applies to its own role only. Administrators, learning resource managers, principals and course planners see the tool when the option for owners is selected.

Clicking the tool opens the configured URL in a **new browser window**. No user data is transferred to the target system. If OpenOlat and the target system share the same identity provider, single sign-on works automatically.

The configuration of the four external course tools is included when a course is **copied**. On course **import**, all four tools are switched off, and name, URL and icon must be entered again.

[Configuration >](../learningresources/Course_Settings_Toolbar.md#external_tools)

---

### Role {: #role}

![Role switcher with the active role Owner and the label Role highlighted in the toolbar, to its right My course](assets/toolbar_role_v2_en.png){ class="shadow lightbox" title="Toolbar of a course · 2026.10.27" }

If a person has multiple roles in this course, the role can be changed here.<br>
[More >](../basic_concepts/Roles.md#course)

---

### My course {: #my_course}

![Open menu My course with Evidence of achievement, To-dos, My badges, Notes, Bookmark and Leave course](assets/toolbar_my_course_v1_en.png){ class="shadow lightbox" title="Menu My course in the toolbar" }

The "My course" drop-down menu in the toolbar provides access to personalized components of the course.<br>
[More >](../learningresources/Toolbar_My_Course.md)

---

### Progress {: #progress}

![Progress indicator as a pie chart at 63 percent highlighted at the right edge of the toolbar](assets/toolbar_progress_v1_de.png){ class="shadow lightbox" title="Toolbar of a course" }

In learning path courses, course participants see their processing status here in the form of a pie chart. For other roles, the progress indicator is not relevant and is therefore not displayed. There is no learning path in conventional courses, so no learning progress can be calculated there.<br>
[More >](../learningresources/Creating_learning_path_courses.md#configuration-for-calculating-the-learning-progress)

[To the top of the page ^](#toolbar)

---

## Show icons (tools) {: #show_icons}

### Display by course owners [:octicons-tag-16:{ title="from Release 10.5 (OO-1967)" }](https://track.frentix.com/issue/OO-1967) {: #show_icons_by_owners}

As course owner you define under `Course > Administration > Settings > Tab "Toolbar"` whether participants see a toolbar and, if so, which icons (tools) are displayed in the toolbar.

![Open menu Administration with the highlighted entry Settings and the highlighted tab Toolbar](assets/toolbar_show_icons1_v1_de.png){ class="shadow lightbox" title="Administration menu of a course" }

![Checkbox Toolbar visible for participants, below it one checkbox per tool, all switched on](assets/toolbar_show_icons2_v1_de.png){ class="shadow lightbox" title="Toolbar tab of the course settings" }

### Permanently displayed tool icons {: #show_icons_permanently}

Some icons are displayed in every course as soon as the toolbar is displayed. These include:

- Administration
- Status
- Info page
- Learning path
- Role
- My course
- Progress (if learning path course)

### Automatically displayed tool icons {: #show_icons_automatically}

The display of the "Events" icon cannot be triggered manually. It appears automatically in the toolbar when the appointment and absence management has been activated.<br>
[More >](../learningresources/Toolbar_Events.md)

[To the top of the page ^](#toolbar)
