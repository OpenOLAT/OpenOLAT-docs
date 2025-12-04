# Coaching - People {: #people}

![coaching_teilnehmer_v1_de.png](assets/coaching_people1_v1_de.png){ class="shadow lightbox" }

![coaching_people_who_v1_de.png](assets/coaching_people_who_v1_de.png){ class="shadow lightbox" }

### WHOM does the list show?  {: #people_who}

The menu item "Participants" shows the list of **all the participants you are responsible for**.

  * The participants from **all** coached courses are displayed (in contrast to the course [assessment tool](../learningresources/Assessment_tool_overview.md). There, only participants from the current course are displayed.)
  * Each coach only sees the participants they are coaching.
  * The participants you are supervising are **grouped and assigned roles** that you, as their coach, have in relation to them.<br>
  In the example shown above, the caregiver can access presorted lists that correspond to their roles:
    * As Coach
    * As Course Owner
    * As Line Manager
    * As Education manager


!!! hint "Note on the roles of line manager and education manager"

    These roles are only displayed in the coaching tool if the [Organization module](../../manual_admin/administration/Modules_Organisations.md) has been activated in the administration. 


!!! hint "Note on other personal relationships"

    Even if you have defined your [own roles and relationships](../../manual_user/basic_concepts/Assign_Roles.md#role_assignment_relations), these roles will be displayed here so that you can view a pre-grouped list.


[To the top of the page ^](#people)

---


### WHAT does the list show?  {: #people_what}

You can define the displayed columns yourself by clicking on the cogwheel icon at the top right. The available columns may vary depending on the selected role. 

* **Status**
* **Login name**
* **Surname, First Name** <br>Clicking on the name of a person leads to an overview of all courses of this participant. This gives the teacher access to the assessment areas of a persons course including access to the relevant transcript, the course's assessment tool and the respective lessons.
* **E-Mail**
* **Gender**
* **Birth date**
* **Organization**<br>
    Only if the Organizational Units module is activated: Which organizational unit does the person belong to?<br>
  (This information is particularly interesting for those responsible for training.)
* **Courses**<br>
    In how many of the courses you coach is a user a member?
* **Not visited**<br>
    In how many of the courses you teach is a user a member but has never attended the course?
* **Last visit**<br>
    How many days ago was your last visit to one of the courses you teach?
* **Average progress**<br>
    Average across all courses you coach
* **Success status**<br>
    * "Passed"/"Not passed"/"Not specified" in graphic depiction
    * "Passed"/"Not passed"/"Not specified" in numbers
* **Certificates**<br>
    Number of certificates received / Number of possible certificates
* **Further actions** (Icon with three dots)<br>
  * Contact (per E-mail)

[To the top of the page ^](#people)

---


## Contact of coach persons {: #contact}

To send an e-mail to **a specific person**, simply click on the three dots at the end of the relevant line.

To write an e-mail to **multiple people**, select the relevant people in the first column. A "Contact" button will then appear above the list.

![coaching_people_contact_v1_de.png](assets/coaching_people_contact_v1_de.png){ class="shadow lightbox" }

### Requirements {: #linemanager_educationmanager_conditions}

The following requirements must be met in order for an additional button labeled "Line Manager" and/or "Education manager" to be displayed.

**Requirement 1:**
The module "Organizational units" must be activated.<br>
(Administration > Modules > Organizations)

**Requirement 2:**
The person in question must be assigned the role.<br>
(User Management > Select person > Tab Roles)

**Requirement 3:**
In the administration section, the "Pending course bookings" option or other rights must be activated. 
(Administration > Modules > Organizations > Tab Organizational structure > select organizational unit (top level) > Button line manager > Education manager > Activate option "Pending course bookings")

---

### Create account for employees {: #linemanager_educationmanager_create_account}

As a line manager or training supervisor, you will find the **"Create account" button** in the top right-hand corner of the coaching tool. Clicking on this button opens a form for entering the necessary information to add previously unregistered persons to OpenOlat.

(Whether this button is available is determined in: Administration > Modules > Organizations > Tab Organizational structure > Select an organizational unit (top level) > Button line manager or educational manager > Option "Create account")

An account created by line managers/education managers automatically assigns the newly registered person to the organizational unit of the line manager/education managers.

![coaching_people_line_manager2_v1_de.png](assets/coaching_people_line_manager2_v1_de.png){ class="shadow lightbox" }

---

### Register participants on behalf of someone else {: #linemanager_educationmanager_book_participants}

If you are a line manager or education manager and would like to register a person already registered in OpenOlat for a course or session, select the person in the coaching tool and click on the **"Register on behalf of" button**. There you can then select the course in which the person should participate. 

![coaching_people_line_manager3_v1_de.png](assets/coaching_people_line_manager3_v1_de.png){ class="shadow lightbox" }

**Example 1:**<br>
A new employee is scheduled to complete several introductory courses next month.

**Example 2:**<br>
Your employees are required to take safety or compliance courses. As their line manager or education manager, you are responsible for booking all participants yourself.

---

### Confirm pending memberships {: #linemanager_educationmanager_confirm_membership}

Line managers and education managers often decide whether learners can participate in a training program. In OpenOlat, they can be given the option to accept or reject pending memberships. 

To do this, select the relevant person in the coaching tool and open the **detail view** by clicking on the plus symbol at the beginning of the line.

At the top right of the detailed view, you will find two buttons, "Accept" and "Reject," which you can use to decide whether to accept or reject the membership.

Alternatively, you can simply use the **link within the notification**.

![coaching_people_line_manager4_v1_de.png](assets/coaching_people_line_manager4_v1_de.png){ class="shadow lightbox" }

!!! info "How do outstanding memberships arise?"

    Memberships that still need to be approved by line managers or education managers are set up in the Course Planner for implementation.
    More about that [here >](../../manual_user/area_modules/Course_Planner_Implementations.md#confirm_membership)

---

### Observational tasks {: #linemanager_educationmanager_observe}

If you are a line manager or educational manager, you can use the coaching tool to check on learning progress within your organizational unit at any time. Automatic notifications about all certificates received are also possible.

As a line manager or educational manager, you are generally granted read access, but editing is restricted and reserved for managers and course owners.

**Examples:**<br>

* You can see who is attending which courses, but you cannot access checklists, assignments, etc. within the courses to view participants' entries.
* You can view badges you have earned and other performance data, but you cannot award badges yourself.
* You can view absences, but you cannot record them yourself. This must be done by the course owners/managers. However, it is possible to create absence reports.

If you, as a line manager or educational manager, would like to have certain rights, you can have these set up by administrators. The screen below shows which options can be configured by administrators. (The same options are available for educational manager.)

![coaching_people_line_manager5_v1_de.png](assets/coaching_people_line_manager5_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#people)

---




## Further information {: #further_information}

[Coaching: User search >](../area_modules/Coaching_User_Search.md)<br>
[Coaching: Courses >](../area_modules/Coaching_Courses.md)<br>
[Coaching: Educational Products >](../area_modules/Coaching_Educational_Products.md)<br>
[Coaching: Groups >](../area_modules/Coaching_Groups.md)<br>
[Coaching: Events / Absences >](../area_modules/Coaching_Events_Absences.md)<br>
[Coaching: Assessment orders >](../area_modules/Coaching_Assessment_Orders.md)<br>
[Coaching: Reports >](../area_modules/Coaching_Reports.md)<br>
[Coaching: Order management >](../area_modules/Coaching_Order_Management.md)<br>
[Roles >](../basic_concepts/Roles.md)<br>
[Define own roles and relations >](../../manual_user/basic_concepts/Assign_Roles.md#role_assignment_relations)<br>
[Assessment tool >](../learningresources/Assessment_tool_overview.md)<br>

[To the top of the page ^](#people)




