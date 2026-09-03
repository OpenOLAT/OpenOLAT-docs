# Coaching - People {: #people}


![Marked button People in the Coaching group leads to the list of all people you coach, on the Coaching entry page.](assets/coaching_people1_v1_de.png){ class="shadow lightbox" }


![Focus buttons As coach, As course owner, Line manager and Education manager above the people list with Status, Username, Courses, Last visit, Progress, Success status and Certificates.](assets/coaching_people_who_v1_de.png){ class="shadow lightbox" }


## WHOM does the list show? [:octicons-tag-16:{ title="from Release 20.0.0 (OO-8374)" }](https://track.frentix.com/issue/OO-8374){:target="_blank"} {: #people_who}

The menu item "People" in the Coaching Tool shows the list of **all participants you coach**.

  * The participants from **all** coached courses are displayed. (In contrast to the [assessment tool](../learningresources/Assessment_tool_overview.md) of the course. There, only participants of the current course are displayed.)
  * Each coach only sees the participants they coach.
  * The participants you coach are **grouped and assigned to the roles** you have in relation to them.<br>
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

* **Status**
* **Username**
* **Last name, First name**<br>Clicking on the username, last name or first name of a person leads to the overview of all courses of this participant. This gives the teacher access to the assessment areas of a course of this person, including access to the respective evidence of achievement, the assessment tool of the course and the respective lectures.
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

!!! info "Important"

    Hovering the mouse over the graphic bar shows a tooltip with the exact numbers: "Passed: X / Not passed: Y / Not specified: Z" [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9229)" }](https://track.frentix.com/issue/OO-9229){:target="_blank"}.

* **Certificates**<br> Number of certificates received / Number of possible certificates
* **Further actions** _(icon with 3 dots)_<br>
    * Contact (by e-mail)

[To the top of the page ^](#people)

---


## Contacting coached people [:octicons-tag-16:{ title="from Release 20.0.3 (OO-8591)" }](https://track.frentix.com/issue/OO-8591){:target="_blank"} {: #contact}

To send an e-mail to **a specific person**, simply click on the 3 dots at the end of the relevant row.

To write an e-mail to **several people**, select the relevant people in the first column. A "Contact" button then appears above the list.

![Contact button above the list after selecting two people and the entry Contact in the row menu, in the people list of Coaching.](assets/coaching_people_contact_v1_de.png){ class="shadow lightbox" }

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

### Confirm pending memberships {: #linemanager_educationmanager_confirm_membership}

Line managers and education managers often decide whether learners can participate in a training measure. In OpenOlat, they can be given the option to accept or reject pending memberships.

To do this, select the relevant person in the Coaching Tool and open the **detail view** by clicking on the plus symbol at the beginning of the row.

At the top right of the detail view, you will find the two **buttons "Accept" and "Reject"** with which you decide on a membership.

Alternatively and more simply, you can also use the **link within the notification**.

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

If you, as a line manager or education manager, want certain rights, you can have them set up by administrators. The screenshot below shows which options administrators can configure. (The same options exist for education managers.)

![Rights of the role Line manager as a checkbox list from Show courses and products to Show administrative properties, in the tab Line manager of an organisation unit in the system administration.](assets/coaching_people_line_manager5_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#people)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Assessment tool >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Module Organisations >](../../manual_admin/administration/Modules_Organisations.md)<br>
[Define own roles and relations >](../../manual_user/basic_concepts/Assign_Roles.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)

**Further reading**<br>
[Coaching: User search >](../../manual_user/area_modules/Coaching_User_Search.md)<br>
[Coaching: Courses >](../../manual_user/area_modules/Coaching_Courses.md)<br>
[Coaching: Educational products >](../area_modules/Coaching_Educational_Products.md)<br>
[Coaching: Events / Absences >](../area_modules/Coaching_Events_Absences.md)<br>
[Coaching: Assessment orders >](../area_modules/Coaching_Assessment_Orders.md)<br>
[Coaching: Reports >](../../manual_user/area_modules/Coaching_Reports.md)<br>
[Coaching: Groups >](../../manual_user/area_modules/Coaching_Groups.md)<br>
[Coaching: Order management >](../../manual_user/area_modules/Coaching_Order_Management.md)<br>
[Roles >](../../manual_user/basic_concepts/Roles.md)

[To the top of the page ^](#people)
