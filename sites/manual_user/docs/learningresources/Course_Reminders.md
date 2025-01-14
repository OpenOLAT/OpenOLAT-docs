# Course Reminders {: #course_reminders}

The reminder function organizes the automatic sending of e-mails.

![course_reminder_access_v1_de.png](assets/course_reminder_access_v1_de.png){ class="shadow lightbox" }

In addition to course administration, reminders can also be set up directly for the respective course element for certain assessable course elements. In this case, the corresponding course element is already preselected. For example, a reminder can be quickly created for learners who have not yet completed a particular test (attempts = 0). Or an e-mail can be sent to all people who have passed a task.

[To the top of the page ^](#course_reminders)

---


## Create reminder {: #create}

As the course owner, you define a list of rules,

* under which **conditions** the reminder should be sent
* the **mail text**
* to **who** the reminder should be sent to

As soon as the conditions are met, the mails are automatically released for dispatch. The exact sending time and frequency is defined system-wide by your system administrator. 

To do this, click on the **"Create reminder"** button. A wizard will appear to guide you step by step through the creation process.

![course_reminder_new_v1_de.png](assets/course_reminder_new_v1_de.png){ class="shadow lightbox" }

First enter the description for the reminder. This description is only visible to the authors and is used for the clear and informative presentation of all reminders of a course. Then select the conditions for shipping.

In the second step of the wizard, the conditions are checked and displayed again.

In the last step, you then enter the e-mail text and can select whether coaches or owners should also receive a copy or whether a copy should be sent to an external address.


[To the top of the page ^](#course_reminders)

---



## Conditions for sending reminders {: #conditions}

The conditions can be selected from a drop-down menu. Depending on the condition, a further input field appears to the right for more detailed information.

![course_reminder_condition1_v1_de.png](assets/course_reminder_condition1_v1_de.png){ class="shadow lightbox" }

Several conditions can be combined as required. This allows reminders to be triggered that are tailored to individual requirements. However, at least one criterion must be selected for a dispatch to be triggered.

![course_reminder_condition2_v1_de.png](assets/course_reminder_condition2_v1_de.png){ class="shadow lightbox" }

!!! info "Note"

    The link is an "and" link. This means that only if all conditions are met, the reminder e-mail will be triggered.

The following criteria can be configured as a condition:

* **Date of registration**<br>
Dispatch x days, weeks, months or years later<br>
_Example_: Users will receive additional information about the course 2 days after enrolment. (Provided the other conditions are also met).

* **Course status**<br>
Select the status the course must be in for a reminder to be sent.

    * Preparation
    * Review
    * Release from coach
    * Published
    * Not preparation
    * Not review
    * Not release from coach
    * Not published

_Example_: Only if the course has the status "Approved coaches" will all coaches receive an info e-mail about their coaching task.


* **Start date Implementation period of the course**<br>
x Days, weeks, months or years before or after

* **End date Implementation period of the course**<br>
x Days, weeks, months or years before or after

* **First course visit**<br>
x Days, weeks, months or years after

* **Last course visit**<br>
x Days, weeks, months or years after

* **Participant is in the course implementation number**<br>
See note on operators

* **Progress**<br>
Only for [Learning path courses](../learningresources/Learning_path_course.md).
In this case, the course is sent based on the percentage progress of the participants as configured in the administration settings.<br>
_Example_: Users who have successfully completed at least 80% of a course.
<br>
See note on operators

* **Certificate date of issue**<br>
This option is only displayed if certificate allocation is activated
(Course administration > Settings > Tab "Assessment").

* **Certificate date of expiry**<br>
This option is only displayed if certificate allocation is activated
(Course administration > Settings > Tab "Assessment").

---

* **Group members**<br>
Selection of a specific group. Only the members of this group will receive the e-mail.

* **Course role**<br>
The reminder recipients must have one of the following roles:

    * Owner
    * Coach
    * Participant
    * Coach and participant
    * Owner and coach
    * Member
    
    _Example_: Only owners and coaches will receive a reminder.

* **User property**<br>
The reminder recipients must have a certain value for one of the following characteristics:

    * Postal code
    * Region
    * City
    * Country
    * Institution
    * Institution number (matriculation number)
    * Institution e-mail
    * Organizational unit / study group
    * Study subject
  
    _Example_: User from the city of Zurich.

---

* **Until date**<br>
Input fields for date and time, as input help button for displaying the calendar

* **After date**<br>
Input fields for date and time, as input help button for displaying the calendar

!!! info "When is the e-mail being sent, if I specify a date here?"

    Course reminders are not sent out immediately. All reminder e-mails are sent together, e.g. daily at 9.00 am. This is a default setting and can be changed by administrators and adjusted to "hourly" (Administration > Modules > Course reminders).
    At the time of sending, OpenOlat checks which conditions are met and sends the e-mails accordingly. All course reminders that fulfill the conditions ("are in the outbox") at 9.00 a.m., for example, are then sent.

    If **"To date"** is checked, the condition may already be fulfilled at the time the reminder is created and e-mails are sent. This setting is particularly useful in conjunction with another condition, e.g. if "to date" is "the test has been passed", an e-mail is sent "You have qualified on time and will receive ...".

    If **"By date"** is used with a date after the time of reminder creation, the e-mails in the "Outbox" will be sent on the first possible sending date when the "By date" has been reached.

---

* **Date of last attempt**<br>
This option only applies to assessable course elements.
    * Dropdown for selecting an assessable course element
    * x Days, weeks, months or years after

* **Attempts**<br>
This option only affects assessable course elements. The number of solution attempts for sending the mail is taken into account here.<br>
_Example_: A test has not yet been carried out (0).

* **Passed**<br>
This option only affects assessable course elements for which a pass status has been configured in the editor. This can be selected here as a condition.<br>
_Example_: One test course element was assessed as "Passed".

* **Score**<br>
This option only affects assessable course elements for which a number of points has been configured in the editor. These can be selected here as a condition.<br>
_Example_: Less than 3 points were achieved in one checklist.

---

* **Schedule: Task Assignment**<br>
This option only affects course elements of the type "Task".

* **Schedule: Task Submit documents**<br>
This option only affects course elements of the type "Task". If an edited task can be uploaded there, a condition for a reminder can refer to the submission time of the task documents.

* **Schedule: Task Peer review submission**<br>
This option only affects course elements of the "Assignment" type. If a peer review is configured there, a condition can refer to the submission time of the peer review.

---

* **Schedule: Fill out form**<br>
This option only affects course elements of the type "Form".


!!! info "Option before/after"

    For conditions that require a "before" or "after" specification for a date, this is provided as a selection list.
    ![Option davor/danach](assets/reminder_option_before_after_DE.png){ class="shadow" }

!!! info "Date"

    The reminder is sent at the next possible sending time on the date (incl. time) entered. If "to date" is used, the reminder is sent at the next possible sending time until the date (and time) is reached.<br>
    _Example_: 24.06.2021 16:30 

!!! info "Time span"

    These conditions are based on how long ago something happened or how far away a certain point in time is.

    _Example_: 5 weeks before the assignment for the group task closes.

    _Example_: 5 days after the user has accessed the course for the first time.


!!! info "Operators"

    Operators are required for the conditions "Participant is in course execution number", "Attempts" and "Points" to correctly represent the different states "more than, less than, less or equal, more or equal, equal" and "not equal". They are used to compare expressions with each other and to generate a logical return value depending on this.

    Operator | Description | Explanation
    ---------|----------|---------
    `<` | less than | correct if a is less than b
    `<=`| less or equal | correct if a is less than or equal to b
    `=`| equal | correct if a is equal to b
    `=>`| more or equal | correct if a is greater than or equal to b
    `>`| more | correct if a is greater than b
    `!=`| not equal | correct if a is not equal to b

    In our conditions in this case, for example, the result of a test (a) is compared with the entered value in the condition rule (b). If the logical return value is "True", i.e. the condition is true, then the reminder is triggered.

    _Example_: A reminder should be sent when a student has scored a maximum of 5 points in a test. In OpenOlat the condition looks like this:

    ![Reminder operators](assets/reminder_operator_EN.png)




## E-mail text {: #text}

Using the e-mail text, which can be customized as needed, you create very specific e-mail reminders tailored to the situation.

!!! tip "Tip"

    It is best to use the variables already entered to make the reminder as personal and helpful as possible.

* **$firstName**: The first name of the user
* **$lastName**: The last name of the user
* **$fullName**: The full name depending on the system configuration. The default value is "lastname, firstname"
* **$email**: The e-mail address of the user
* **$userName**: The username.
* **$courseUrl**: The internet address of the course
* **$courseName**: The name of the course as on the info page
* **$courseDescription**: The description of the course as on the info page

Here is an example:

![Reminder Mail](assets/reminder_notification_text.png){ class="shadow" }

At the top course node, all reminders that are not tied to a specific course element are also listed. Also here as well as with other assessment elements with the tab "Reminders" further configurations can be made, e.g. configured reminders can be edited, duplicated, sent, deleted. It is also possible to display the dispatch.


## Recipients {: #recipients}

Reminders are good for reminding **course participants** of what they should do next.
A **copy to the coaches and/or course owners** also informs them that participants have something to do.


In some cases, reminders should be sent **exclusively to coaches**.<br>
**Example:**<br>
Course participants do not show any progress. The coach should then contact these students and provide assistance. This reminder should only go to the coach.

Reminders can also be sent **exclusively to course owners**.<br>
**Example:**<br>
Sometimes authors forget to publish their course because things were still unclear when they last worked on the course creation. In this case, the course status can be used in combination with the role as a dispatch criterion.

![course_reminder_condition_status_v1_de.png](assets/course_reminder_condition_status_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#course_reminders)

---


## Check and edit reminders {: #check_and_edit}

If reminders have already been created, these are listed under **Administration > Reminders**.
On the overview page you can see all the reminders already created for this course and can also view reminders that have already been sent. The list of reminders that have already been sent contains information about the recipient and the sending time. Individual reminders from this list can be easily sent via the "Send again" link.

![Erinnerungen Aktionsmenü](assets/reminder_DE.png){ class="shadow" }

New reminders can be created at any time.

If, for example, an individual condition for dispatch is to be removed, you will find the buttons for deleting an individual condition to the right of the respective condition in edit mode.

Reminders can also be triggered repeatedly and in a targeted manner. However, reminders are only sent to those users for whom all conditions have been met.


[To the top of the page ^](#course_reminders)

---


## Further information {: #further_information}

[Personal Menu: E-Mails >](../personal_menu/E-Mail.md)<br>
[Course element Notifications](../learningresources/Course_Element_Notifications.md)<br>
[Participant infos](../learningresources/Using_Additional_Course_Features.de.md#teilnehmer-infos)<br>



