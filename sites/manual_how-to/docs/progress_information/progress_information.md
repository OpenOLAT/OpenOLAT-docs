# How can coaches be informed about the learning progress of course participants? {: #progress_information}

??? abstract "Objectives and content of this instruction"

    The guide shows you as a coach where you can access information on learning progress in order to provide the best possible advice and support to the people you are looking after. 

??? abstract "Target group"

    [ ] Authors [x] Coaches  [ ] Participants

    [x] Beginners [ ] Advanced users  [ ] Experts


??? abstract "Expected previous knowledge"

    * Basic knowledge about OpenOlat
    * (Access to a course in which you are a coach)


## A) Selection of a course element as a coach {: #by_course_element}

If you call up a course in the role of coach, you will see a different view than the participants after selecting an assessable course element in the course menu.

![Coach role active: Participants tab lists points, passed and status per person](assets/progress_information_course_element_v1_de.png){ class="shadow lightbox" title="Test course element in the Coach role" }

By clicking on the name of a participant (via the "Overview" or "Participants" tab), you can go directly to the results of the participant in this course element.

[To the top of the page ^](#progress_information)

---

## B) Assessment tool {: #by_assessment_tool}

If you are not only interested in a single course element, but would like to get an overview of the performance of the entire course, the most important tool for coaches is the [Assessment tool](../../manual_user/learningresources/Assessment_tool_overview.md). You can find it under:<br>
`Course > Administration > Assessment tool`

![Entry Assessment tool opens the overview with the passed share and open assessments](assets/progress_information_assessment_tool_v1_de.png){ class="shadow lightbox" title="Administration menu of the course" }

[To the top of the page ^](#progress_information)

---

## C) Learning path tool {: #by_learning_path_tool}

!!! info "Important"

    The "Learning path" icon is only displayed in the toolbar if you are in a [Learning path course](../../manual_user/learningresources/Learning_path_course.md).


When a participant accesses the learning path tool, only their own results are visible. As a coach, you have access to the learning path information of all the participants you coach. 

![Learning path icon and Coach role marked](assets/progress_information_lp_tool1_v1_de.png){ class="shadow lightbox" title="Toolbar of the course" }

![List Learning paths with progress, passed and points per participant](assets/progress_information_lp_tool2_v1_de.png){ class="shadow lightbox" title="Learning paths page after clicking the Learning path icon" }

Click on a name to display the learning path of this person.

![Progress, status and Date done per course element for one participant](assets/progress_information_lp_tool3_v1_de.png){ class="shadow lightbox" title="Learning path of a person after clicking their name" }


:octicons-device-camera-video-24: **Video Introduction (German)**: [Wie sehe ich den Lernfortschritt von mir betreuter Teilnehmer:innen?](<https://www.youtube.com/embed/VO7TyxN9EOA>){:target="_blank"}


[To the top of the page ^](#progress_information)

---


## D) Automatic reminders {: #by_reminders}

The [reminder function](../../manual_user/learningresources/Course_Reminders.md) is mostly used to send emails to participants. However, it can also be used to inform coaches.

![Entry Reminders in the Administration menu and button to add a reminder highlighted](assets/course_reminder_access_v1_de.png){ class="shadow lightbox" title="Reminders page of the course" }

**Example 1: Automatic mails to course participants, cc to coaches**<br>

In the last step of creating/editing a reminder, it is possible to add coaches to the group of recipients (defined by rules).

![Option According to the rules with Copy to Assigned coaches](assets/course_reminder_cc_coach_v1_de.png){ class="shadow lightbox" title="E-mail message step of the reminder" }

**Example 2: Automatic mail only to coach**<br>

A reminder that would be sent to certain recipients according to defined rules can also only be sent to coaches for information. 

For example, a reminder could be sent to those participants who have never accessed the course 2 weeks after the start of the course. The rules for this reminder are chosen so that the recipients are the somewhat negligent participants. In the last step of the reminder creation, however, "Only to specific recipients" is selected and "Assigned coaches" is selected. The information about the course not yet attended is then only sent to the coaches.

![Option Only to specific recipients with Assigned coaches](assets/course_reminder_excl_coach_v1_de.png){ class="shadow lightbox" title="E-mail message step of the reminder" }

!!! tip "Tip"

    Variables can also be used in the text of the reminder emails. (See [Variables in the email text of reminders](../../manual_user/learningresources/Course_Reminders.md#text).) If the reminder goes only to coaches as in example 2, two pairs of variables name different people:

    * `$firstName` and `$lastName`: the name of the coach who receives the email
    * `$firstNameAffectedUser` and `$lastNameAffectedUser`: the name of the participant for whom the conditions of the reminder are met


[To the top of the page ^](#progress_information)

---


## Further information {: #further_information}

[Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Learning path course - Overview >](../../manual_user/learningresources/Learning_path_course.md)<br>
[Course Reminders >](../../manual_user/learningresources/Course_Reminders.md)<br>
[Assessment of learners >](../../manual_user/learningresources/Assessment_of_learners.md)<br>
[Coaching - Overview >](../../manual_user/area_modules/Coaching.md)

**youtube**<br>
[Wie sehe ich den Lernfortschritt von mir betreuter Teilnehmer:innen?](<https://www.youtube.com/embed/VO7TyxN9EOA>)

[To the top of the page ^](#progress_information)
