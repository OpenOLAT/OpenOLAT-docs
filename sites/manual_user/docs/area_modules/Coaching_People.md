# Coaching - People {: #people}


![Marked button People in the Coaching group leads to the list of all people you coach, on the Coaching entry page.](assets/coaching_people1_v1_de.png){ class="shadow lightbox" }


![Focus buttons As coach, As course owner, Line manager and Education manager above the people list with Status, Username, Courses, Last visit, Progress, Success status and Certificates.](assets/coaching_people_who_v1_de.png){ class="shadow lightbox" }


## WHOM does the list show? [:octicons-tag-16:{ title="from Release 20.0.0 (OO-8374)" }](https://track.frentix.com/issue/OO-8374){:target="_blank"} {: #people_who}

The menu item "People" in the Coaching Tool shows the list of **all participants you coach**.

  * The participants from **all** coached courses are displayed. (In contrast to the [assessment tool](../learningresources/Assessment_tool_overview.md) of the course. There, only participants of the current course are displayed.)
  * Each coach only sees the participants they coach.
  * The participants you coach are **grouped and assigned to the roles** you have as coach in relation to them.<br>
  In the example shown above, the coach can access presorted lists that correspond to their roles:
    * as coach
    * as course owner
    * as line manager
    * as education manager


!!! info "Note on the roles line manager and education manager"

    These roles are only displayed in the Coaching Tool if administrators have activated the [Module Organisations](../../manual_admin/administration/Modules_Organisations.md) in the system administration.



!!! info "Note on other person relations"

    If you have additionally defined your [own roles and relations](../../manual_user/basic_concepts/Assign_Roles.md#role_assignment_relations), these also appear here as a separate, pre-grouped list.


[To the top of the page ^](#people)

---


## WHAT does the list show? [:octicons-tag-16:{ title="from Release 20.0.3 (OO-8591)" }](https://track.frentix.com/issue/OO-8591){:target="_blank"} {: #people_what}

You can define the displayed columns yourself by clicking on the gear icon at the top right above the list. The available columns may vary depending on the selected role.

With the search field above the list, you narrow down the people by name and further account details. Separate several search terms with a space or a comma; a person appears when all terms apply to them. The asterisk `*` stands for any number of characters, for example `Mei*` for all names beginning with "Mei". The wildcard behaves in the same way as in the [course search of the Coaching Tool](Coaching_Courses.md#courses_search) [:octicons-tag-16:{ title="from Release 20.3.7 (OO-9630)" }](https://track.frentix.com/issue/OO-9630){:target="_blank"}.

* **Status**
* **Username**
* **Last name, First name**<br>Clicking on the username, last name or first name of a person leads to the overview of all courses of this participant. This gives the teacher access to the assessment areas of a course of this person, including access to the respective evidence of achievement, the assessment tool of the course and the respective lectures. The search field above this course list also knows the asterisk `*` as a wildcard.
* **E-mail**
* **Gender**
* **Birth date**
* **Organisation**<br> Only if the module Organisations is activated: Which organisation unit does the person belong to? _(This information is particularly interesting for education managers.)_
* **Courses**<br> In how many of the courses you coach is a user a member?
* **Not visited**<br> In how many of the courses you coach is a user a member but has never visited the course?
* **Last visit**<br> How many days ago was the last visit to one of the courses you coach?
* **Average progress**<br> Average across all courses you coach
* **Success status**
    * "Passed"/"Not passed"/"Not specified" in graphic depiction
    * "Passed"/"Not passed"/"Not specified" in numbers
* **Certificates**<br> Number of certificates received / Number of possible certificates
* **Further actions** _(icon with 3 dots)_<br>
    * Contact (by e-mail)

!!! tip "Exact numbers for the success status"

    Hover the mouse over the graphic bar in the "Success status" column. A tooltip shows the exact numbers: "Passed: X / Not passed: Y / Not specified: Z" [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9229)" }](https://track.frentix.com/issue/OO-9229){:target="_blank"}.

[To the top of the page ^](#people)

---


## Contacting coached people [:octicons-tag-16:{ title="from Release 20.0.3 (OO-8591)" }](https://track.frentix.com/issue/OO-8591){:target="_blank"} {: #contact}

To send an e-mail to **a specific person**, simply click on the 3 dots at the end of the relevant row.

To write an e-mail to **several people**, select the relevant people in the first column. A "Contact" button then appears above the list.

![Contact button above the list after selecting two people and the entry Contact in the row menu, in the people list of Coaching.](assets/coaching_people_contact_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#people)

---

## The detail view of a person {: #person_detail_view}

If you want to know how far a coached person has got in their courses, when they attend a course or since when they have been booked into a course, you find the answer in their detail view. You open the detail view in the people list by clicking on the name or the username of the person. How the detail view is structured depends on the focus button under which you opened the person.

### Under "As coach" and "As course owner" {: #person_detail_view_coach}

If you coach a person in your courses, the detail view mainly shows you their courses, so that you can jump from there directly to the evidence of achievement and the assessment tool of a course. There are no tabs in this view. If the Course Planner module is switched on, the switches "All courses" and "Educational products" appear below the details of the person; "Educational products" shows the implementations of the person. In this role, you also see implementations in preparation there in a separate tab "Preparation", and the columns "Progress" and "Timetable" always appear.

In this role, you find the events and absences of the people you coach in the tool [Coaching - Events and Absences](Coaching_Events_Absences.md). It shows the events of all the courses you coach, not those of a single person.

### Under "Line manager", "Education manager" and own roles {: #person_detail_view_tabs}

If you are responsible for a person as line manager, as education manager or in an [own role](../../manual_user/basic_concepts/Assign_Roles.md#role_assignment_relations), the detail view arranges all information about the person by topic in tabs. This way you find the learning progress, events and bookings of the person without switching to the individual courses. Each tab only appears if administrators have granted your role the corresponding right; the rights are shown in the section [Observational tasks](#linemanager_educationmanager_observe). The tabs are located below the details of the person in the following order.

![The tabs from Courses to Account are arranged in a bar below the details of the person, in the detail view of a person in Coaching.](assets/coaching_people_detail_tabs_v1_en.png){ class="shadow lightbox" }

#### Courses {: #tab_courses}

Here you see how far the person has got in their courses. Depending on the rights of your role, the list shows progress, passed and score and, if the module Events and Absences is switched on, the number of units and absences per course. The tab shows the learning progress, not the schedule: when an event takes place is shown in the tab "Events & Absences", when the person was booked in is shown in the tab "Bookings". If the Course Planner module is switched on, you switch to the implementations of the person with the switch "Educational products", see [The educational products of a person](#linemanager_educationmanager_products). The prerequisite for the tab is the right "View course and CPL products".

#### Events & Absences {: #tab_lectures}

Here you see when the person attends a course. The first list shows the planned and the attended units per course (columns "Units" and "Attended") as well as the absences. If you click on a course, you see the individual events with "Date", "From", "To", "Event" and "Teachers". This is the only place in the detail view that shows the date and time of an event.

The prerequisites are the activated [Module Events and Absences](../../manual_admin/administration/Modules_Events_and_Absences.md) and the right "View events and absence". As a line manager or education manager, you moreover only see courses that are assigned to an organisation unit in which you hold this role. The right alone is therefore not sufficient. This is the most frequent cause of an empty list although the right is set.

![Individual events of a course with Date, From and To, after clicking on the course in the tab Events & Absences of the detail view of a person.](assets/coaching_people_lectures_detail_v1_en.png){ class="shadow lightbox" }

!!! tip "Why is a course missing under Events & Absences?"

    Check the causes in this order. The first one takes effect before all others.

    1. The [Event & absence management](../learningresources/Course_Settings_Execution.md#lecture_enabled) is switched off in the course. Then the course is missing, even if right, role and organisation unit are correct.
    2. No [events have been recorded](../learningresources/Events_and_absences.md) for the course.
    3. The course does not belong to any organisation unit in which you are line manager or education manager.
    4. The course has neither the status "Published" nor the status "Finished".
    5. The person is not a participant in the course.

#### Efficiency statements {: #tab_statements}

Here you see the evidence of achievement of the person, i.e. per course their results from the assessable course elements with points and status. The prerequisite is the right "View efficiency statements".

#### Certificates {: #tab_certificates}

Here you see which certificates the person has received. The tab appears with the same right as the tab "Efficiency statements".

#### Badges {: #tab_badges}

Here you see which badges the person has received. The prerequisite is the right "View badges".

#### Credit points [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9490)" }](https://track.frentix.com/issue/OO-9490){:target="_blank"} {: #tab_credit_points}

Here you see the credit point balance of the person per credit point system and the related transactions, read-only. The prerequisites are activated [credit points](../../manual_admin/administration/e-Assessment_Credit_Points.md) and the right "View credit points".

#### Bookings {: #tab_bookings}

Here you see when and via which offer the person got into a course or an implementation. The list shows per booking the "Order date", the "Offer", the "Content" and the "Status". The prerequisites are the activated [Module Catalog](../../manual_admin/administration/Modules_Catalog_2.0.md) and the right "View bookings". If you additionally hold the right "Pending course booking orders", the switch "Pending memberships" can appear, see [Confirm pending memberships](#linemanager_educationmanager_confirm_membership).

#### Groups {: #tab_groups}

Here you see in which groups the person is a member. The prerequisite is the right "View groups".

#### Calendar {: #tab_calendar}

Here you see at a glance when the person is scheduled. The calendar combines their personal calendar, the course calendars of the courses in which they are a participant, and the calendars of their groups with the tool Calendar. Which of these appear depends on which calendars administrators have switched on in the [Core functions](../../manual_admin/administration/Core_functions.md#calendar_administration). An event from the event and absence management only appears if it is linked to a course and the course synchronises its events with the course calendar. The prerequisite for the tab is the right "View course calenders".

!!! tip "Why is a course missing in the calendar?"

    Check the causes in this order.

    1. No events have been recorded for the course.
    2. The event has been recorded in the Course Planner on an implementation without a linked course. Such events do not appear in any calendar.
    3. The option [Synchronize course calendar](../learningresources/Course_Settings_Execution.md#course_calendar_sync) is switched off in the course.
    4. The person has a pending membership and is not yet a participant in the course.
    5. The course has neither the status "Access for coach" nor "Published" nor "Finished".

    It is not due to your authorisation. The calendar shows the courses of the person regardless of the organisation unit they belong to.

The tabs "Events & Absences" and "Calendar" can show different things for the same course, because they do not check the same conditions. "Events & Absences" requires the status "Published" or "Finished" and, for line managers and education managers, the matching organisation unit. The calendar is content with the status "Access for coach" and does not ask for the organisation unit. In addition, the calendar does not follow the setting "Event & absence management" in the course: if it is switched off, the course is missing under "Events & Absences", while its events can still appear in the calendar.

#### Profile {: #tab_profile}

Here you see the profile details of the person. With the right "View profile", the tab is read-only; with the right "Edit profile", you can also edit the details. If the person has additional roles, the tab remains read-only, see [Extended people view](#linemanager_educationmanager_extended_view).

#### Account {: #tab_account}

Here you see when the account of the person was created and when they last logged in, and you can change the status of the account, for example to deactivate it. The prerequisite is the right "Deactivate accounts".

[To the top of the page ^](#people)

---

## Coaching tasks as line manager / education manager [:octicons-tag-16:{ title="from Release 20.0.0 (OO-7839)" }](https://track.frentix.com/issue/OO-7839){:target="_blank"} {: #linemanager_educationmanager}

Line managers and education managers find an additional button under People in the Coaching Tool, under which they find all people they are responsible for in their role.

![Marked focus buttons Line manager and Education manager next to As coach and As course owner, above the people list in Coaching.](assets/coaching_people_line_manager1_v1_de.png){ class="shadow lightbox" }

### Extended people view [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9168)" }](https://track.frentix.com/issue/OO-9168){:target="_blank"} {: #linemanager_educationmanager_extended_view}

In the people list under the focus "Line manager" or "Education manager", all users of the organisation are displayed, regardless of their role.

If a person has additional roles (more than the author role), an info message with an icon appears in the detail view: **"Due to additional organisational roles, administration is restricted for this person."** In this case:

* The **Profile** and **Account** tabs are read-only.
* The **Reset password** action is not available.

[To the top of the page ^](#people)

---


### Requirements {: #linemanager_educationmanager_conditions}

The following requirements must be met for an additional button "Line manager" and/or "Education manager" to be displayed.

**Requirement 1:**
The module "Organisations" must be activated in the system administration.<br> `Administration > Modules > Organisations`

**Requirement 2:**
The person in question must have been assigned the role.<br> `User management > Select person > Tab Roles`

**Requirement 3:**
In the system administration, e.g. the option "Pending course booking orders" or further rights must **be activated**:<br>
`Administration > Modules > Organisations > Tab Organisations structures > "Organisation unit (top level)" > Tab Line manager or Education manager > Option "Pending course booking orders"`

---

### Create account for employees [:octicons-tag-16:{ title="from Release 20.0.1 (OO-8491)" }](https://track.frentix.com/issue/OO-8491){:target="_blank"} {: #linemanager_educationmanager_create_account}

As a line manager or education manager, you will find the **"Create account" button** at the top right of the Coaching Tool. It opens a form for entering the necessary details to add people not yet registered to OpenOlat.

Whether this button is available is defined in the system administration:<br>
`Administration > Modules > Organisations > Tab Organisations structures > "Organisation unit (top level)" > Tab Line manager or Education manager > Option "Create accounts"`

An account created by line managers or education managers automatically contains an assignment of the newly registered person to the organisation unit of the line manager or education manager.

![Marked button Create account at the top right, focus Line manager with the filter tabs All, Relevant, Without courses and To be confirmed, in the people list of Coaching.](assets/coaching_people_line_manager2_v1_de.png){ class="shadow lightbox" }

---

### Book participants on behalf of someone {: #linemanager_educationmanager_book_participants}

If you, as a line manager or education manager, want to book a person already registered in OpenOlat into a course or an implementation, select the person in the Coaching Tool and click the **"Book on behalf of" button**. There you can then select the course in which the person should participate.

![Marked button Book on behalf of at the right above the tabs, above it the notice of a pending membership, in the detail view of a person in Coaching.](assets/coaching_people_line_manager3_v1_de.png){ class="shadow lightbox" }


**Example 1:**<br>
A new employee is to complete several introductory courses next month.

**Example 2:**<br>
Your employees are required to take safety or compliance courses. As you are responsible as line manager or education manager, you book all persons yourself.


---

### Confirm pending memberships [:octicons-tag-16:{ title="from Release 20.1.5 (OO-8892)" }](https://track.frentix.com/issue/OO-8892){:target="_blank"} {: #linemanager_educationmanager_confirm_membership}

Line managers and education managers often decide whether learners can participate in a training measure. In OpenOlat, they can be given the option to accept or reject pending memberships.

To do this, select the relevant person in the Coaching Tool and open the **detail view** by clicking on the plus symbol at the beginning of the row.

At the top right of the detail view, you will find the two **buttons "Accept" and "Reject"** with which you decide on a membership.

Alternatively and more simply, you can also use the **link within the notification**. If the invoice module is active, the button "Pending confirmations" on the Coaching overview additionally leads to a list of all open memberships; its search field knows the asterisk `*` as a wildcard.

![Buttons Accept and Reject for a pending membership, reached via the link Go to confirmation and the tab Bookings, in the detail view of a person in Coaching.](assets/coaching_people_line_manager4_v1_de.png){ class="shadow lightbox" }

!!! note "How do pending memberships arise?"

    Memberships that still need to be approved by line managers or education managers are set up in the Course Planner for implementations.
    More about that [here >](../../manual_user/area_modules/Course_Planner_Implementations.md#confirm_membership)

---


### Observational tasks {: #linemanager_educationmanager_observe}

If you are a line manager or education manager, you can inform yourself about the learning progress within your organisation unit in the Coaching Tool at any time. Automatic notification about all certificates received is also possible.

As a line manager or education manager, you are generally granted read access, but editing is restricted and reserved for coaches and course owners.

**Examples:**<br>

* You can see who is attending which courses, but you cannot access checklists, tasks etc. within the courses to view the entries of the participants.
* You can view received badges and other performance data, but you cannot award badges yourself.
* You can view absences, but you cannot record them yourself. This must be done by the course owners/coaches. Creating absence reports, however, is possible.

In the detail view of a person, you find this information in separate tabs: the courses attended in the tab [Courses](#tab_courses), the badges received in the tab [Badges](#tab_badges) and the absences in the tab [Events & Absences](#tab_lectures). Which tab belongs to which right is described in the section [The detail view of a person](#person_detail_view_tabs).

If you, as a line manager or education manager, want certain rights, you can have them set up by administrators. The screenshot below shows which options administrators can configure. (The same options exist for education managers.)

![Rights of the role Line manager as a checkbox list from Show courses and products to Show administrative properties, in the tab Line manager of an organisation unit in the system administration.](assets/coaching_people_line_manager5_v1_de.png){ class="shadow lightbox" }

### The educational products of a person [:octicons-tag-16:{ title="from Release 21.0 (OO-9374)" }](https://track.frentix.com/issue/OO-9374){:target="_blank"} {: #linemanager_educationmanager_products}

Open a person and switch to "Educational products". The list shows the implementations of this person. It follows the same logic as the list under [Coaching - Educational products](../area_modules/Coaching_Educational_Products.md#filter), but offers fewer filters and columns:

* The filter tabs available are "All", "Relevant" and "Finished". "Relevant" is preselected.
* The tabs "Favourites" and "Preparation" do not exist here. Only coaches and course owners see implementations in preparation.
* There is no column "Status". Cancelled implementations appear in the tab "Finished", but cannot be filtered out separately there.
* The columns "Progress" and "Timetable" only appear if administrators granted your role the corresponding rights.

[To the top of the page ^](#people)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Assessment tool >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Module Organisations >](../../manual_admin/administration/Modules_Organisations.md)<br>
[Define own roles and relations >](../../manual_user/basic_concepts/Assign_Roles.md)<br>
[Coaching: Courses >](../../manual_user/area_modules/Coaching_Courses.md)<br>
[Coaching: Events / Absences >](../area_modules/Coaching_Events_Absences.md)<br>
[Module Events and Absences >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Course Settings - Tab Execution >](../learningresources/Course_Settings_Execution.md)<br>
[Events and absences in the course >](../learningresources/Events_and_absences.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Module Catalog >](../../manual_admin/administration/Modules_Catalog_2.0.md)<br>
[Core functions: Overview >](../../manual_admin/administration/Core_functions.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)<br>
[Coaching: Educational products >](../area_modules/Coaching_Educational_Products.md)

**Further reading**<br>
[Coaching: User search >](../../manual_user/area_modules/Coaching_User_Search.md)<br>
[Coaching: Assessment orders >](../area_modules/Coaching_Assessment_Orders.md)<br>
[Coaching: Reports >](../../manual_user/area_modules/Coaching_Reports.md)<br>
[Coaching: Groups >](../../manual_user/area_modules/Coaching_Groups.md)<br>
[Coaching: Order management >](../../manual_user/area_modules/Coaching_Order_Management.md)<br>
[Roles >](../../manual_user/basic_concepts/Roles.md)

[To the top of the page ^](#people)
