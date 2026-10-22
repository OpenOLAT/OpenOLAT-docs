# Assessment tool - overview {: #assessment_tool_overview}

The assessment tool is the central switch point for assessments of an OpenOlat course. Course owners and coaches get a general overview here of all assessable course elements contained in the course and can carry out the assessments.

You reach the assessment tool via `Course > Administration > Assessment tool`. When you open the assessment tool, you will first see the overview page with central information as well as an overview of the currently pending assessments and actions. This way you will quickly know what you have to do. From the overview page you can also access the concrete assessment areas of the individual course elements and persons.

![Start page of the assessment tool that shows at a glance how the course is doing, which exam is coming up and what still needs to be assessed](assets/assessment_tool_overview.jpg){ class="shadow lightbox" title="Overview of the assessment tool" }

Let's take a closer look at the individual areas of the overview:

## "Overview" of the assessment tool

### "Open reviews" (Overview)

At a glance you can see whether, and for whom, one or more reviews are open. It also shows how many course elements of the respective person need to be reviewed. If only one course element needs to be reviewed, it is listed directly. Clicking on the course element takes you to the corresponding review.

![2 open reviews, per course element with the name of the person](assets/open_reviews.jpg){ class="shadow lightbox" title="Area Open reviews" }

Only the unfinished reviews are displayed here. Reviews that have already been carried out are not listed here.

### "Reviews to release" (Overview)

If there are reviews in the course that are not yet visible to the participants, they appear here.

![One review in a test that the participant does not see yet](assets/review_to_release.jpg){ class="shadow lightbox" title="Area Reviews to release" }

### "Participants" (Overview)

This area shows how many participants, groups and curriculum elements are generally available in the specific course.

If "passed" has been configured for the entire course, the number of the respective course members who have passed or not passed the course is displayed. The average distribution of points is also visible, provided points are activated in the course. 

![Share passed and score distribution of the participants, below members, average score and passed per group and curriculum element](assets/Uebersicht_Bewertungswerkzeug.jpg){ class="shadow lightbox" title="Area Participants" }

### Assessment mode (Overview)

If an exam in [assessment mode](../learningresources/Assessment_mode.md) is planned for the course or an exam is currently running, the assessment tool shows it in this area.

![Running exam with the button "Prüfung beenden" in the banner and in the area, below two scheduled exams with start and end](assets/Pruefng1_Bewertungswerkzeug1.jpg){ class="shadow lightbox" title="Area Assessment mode" }

Here you also see how many people are already logged in and waiting for the exam to start.

If the exam has a manual start, the area shows the button "Start exam" from the day of the exam and, after the start, the button "Finish exam". Coaches only see these buttons with an additional right. Who sees the buttons is described in the section [Who can start and finish an exam manually](../learningresources/Assessment_mode.md#start_stop_rights).

![Scheduled exam with manual start, one of two persons is waiting, below the button "Start exam"](assets/start_exam.jpg){ class="shadow lightbox" title="Area Assessment mode before the start" }

### "Notification Service"

Here coaches can use the subscribe toggle to activate receiving an email for new submissions, test results and other submissions. Notifications about newly generated certificates (if generally activated) can also be subscribed to.

![The bell next to "Neue Testresultate" opens the subscription with the toggle "Abonnieren"](assets/Benachrichtigungen_Bewertungswerkzeug20.jpg){ class="shadow lightbox" title="Notifications in the assessment tool" }

## Orders

Below the overview is the link to the "Orders" area. Here you can see whether there are open reviews, whether ratings/grades need to be set by hand, and whether there are reviews to release.

![Tabs for open reviews, open gradings and reviews to release, with the list of reviews to release open](assets/Auftraege1.jpg){ class="shadow lightbox" title="Area Orders of the assessment tool" }

## Assessment inspection [:octicons-tag-16:{ title="from Release 18.2 (OO-7425)" }](https://track.frentix.com/issue/OO-7425)

This menu area is only visible if an exam has been configured for the course and the assessment inspection option has also been activated.

Coaches can then add participants, define which exam the inspection applies to, and at what specific time the inspection is possible. If required, an access code for the inspection can also be assigned and an info email sent.

![Participants with test status, inspection period, inspection duration and status Scheduled, plus the button to add a participant](assets/Pruefungseinsicht_Baustein1.jpg){ class="shadow lightbox" title="Tab Assessment inspection of a test" }

You can find more information on the page [Assessment management: assessment inspection](../learningresources/Assessment_inspection.md).

## Overview of the assessment elements of the course

In the left navigation of the assessment tool you see all assessable course elements. For all course elements, the tabs "Overview" and "Participants" are displayed.

The overview tab shows information similar to the overview area of the assessment tool, but related to the course element, e.g. the distribution of points, number of reviews, information on passing, etc.

### Tab Participants

In the "Participants" tab, the actual assessment is carried out: persons can be selected, points and feedback entered, and the release of visibility set. 
The table then shows the processing status of all participants of the specific course element.<br>
Furthermore, for tasks, all submitted documents can also be downloaded in the Participants tab.

The automatically generated top course node also counts as an assessable element. It corresponds to a ["Structure"](../learningresources/Course_Element_Structure.md) element.<br>
Clicking on a person at the top course element gives you a complete overview of the processing status of the assessment elements of the course for that person, allowing you to also view their proof of performance.

If a point calculation is set up on the top course element, the *total points* of a course, or the points defined for the top element, can also be displayed at the top level of the user view, and the overall results of the course participants can be downloaded.

!!! tip "Tip"

    Use the filter settings to display only certain participants in the table. Also use the column configuration via the gear icon to display the columns that are relevant to you.

To learn exactly how assessments are carried out, see the chapters ["Assessment of course elements"](../learningresources/Assessment_of_course_modules.md) or ["Assessing learners"](../learningresources/Assessment_of_learners.md).

!!! info "Important"

    If assessment inspection has been activated for participants, the "Assessment inspection" tab also appears for the corresponding course element.

Detailed information on processing and assessing in the Participants tab is available in the chapter ["Tab Participants"](../learningresources/Assessment_tool_tab_Users.md).

## Reset data [:octicons-tag-16:{ title="from Release 17.2.4 (OO-6792)" }](https://track.frentix.com/issue/OO-6792) {: #course_reset}

With the help of the wizard, the data of the participants of a course can be reset. The reset can be carried out for the entire course or only for selected course elements, for all or selected participants.

[Find out more >](../../manual_user/learningresources/Assessment_tool_reset_data.md)

## Bulk assessment [:octicons-tag-16:{ title="from Release 9.2 (OO-852)" }](https://track.frentix.com/issue/OO-852) {: #mass_assessment}

With the "Bulk assessment" tool, assessment data such as points, status information, comments as well as return files can be submitted for several participants in one step.

![First step "Kursbaustein auswählen" with the assessable course elements of the course and the link "Wählen"](assets/Massenbewertung_wizard.png){ class="shadow lightbox" title="Bulk assessment wizard" }

Find out how to create a bulk assessment in the [How to](../../manual_how-to/bulk_assessment/bulk_assessment.md) section.

## Further information {: #further_information}

**Further reading**<br>
[Assessment Management: Overview >](../learningresources/Assessment_Management.md)<br>
[Members management >](../learningresources/Members_management.md)<br>
[Roles and Rights: Which roles are available? >](../basic_concepts/Roles.md)

[To the top of the page ^](#assessment_tool_overview)
