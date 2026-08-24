# Assessing tasks and group tasks

Here you will learn how to make assessments for tasks and group tasks using the OpenOlat "Assessment tool".

Go to the assessment tool and select the assessment element you want to assess from the overview on the left. Here you will find two tabs: Overview and Participants.

In the tab Overview you get an overview of the assessment of this course element, e.g. how many persons have already passed this course element. 
In the tab Participants the participants are displayed and the actual evaluation of participants can be started.


## Tab Participants

**General action options**

![Above the participant list stand the actions "Start new bulk assessment", "Export results", "Export data" and "Statistic"; for each person the list carries Coach, Attempts, Passed, Task, State and last update: tab Participants of the assessment tool](assets/assessment_tool_task_participants_en.png){ class="shadow lightbox" }

Course coaches and course owners have various action options via the corresponding buttons:

* use "Export results" to download the submitted documents of all or selected participants together with an Excel report
* use "Export data" to output the assessment data of the participants.
* use "Statistic" to open the analysis of the course element.
* start a new bulk assessment and thus assess all participants at once.
* set the task to the status "completed" for all or several selected participants and thus finally finish the assessment. To do this, the desired participants or all participants must first be selected.
* set the assessments of the task to visible or invisible for all or several selected participants at once.
* To send an email to all or specific participants.
* To extend the submission time for certain or all people.

Directly selectable are the options "Export results" as well as to perform a mass evaluation. How to create a mass evaluation for tasks exactly you will learn here in the section [How to](../../manual_how-to/bulk_assessment/bulk_assessment.md).
For further actions that only apply to certain participants, the desired participants must first be selected before the options are displayed.

![After a row is selected, a bar with six actions for the selected people appears above the list: "Finalize assessment", "Release", "Withdraw release", "Extend", "Export results" and "E-Mail": tab Participants of the assessment tool](assets/assessment_tool_task_bulk_actions_en.png){ class="shadow lightbox" }

## View submitted documents

Before an assignment can be graded, the coaches or course owners must look at the submissions or submitted documents. This can be done either individually for each participant or in the form of mass evaluation or downloading the submitted documents from several people.

### Submissions of individual users

Once a file has been submitted by a learner via the "final submission" button, it can be opened and viewed by the teacher.

To view the submission of _an individual person_ select that person and click on the submitted file.

![The step Submission is marked "Completed" and lists the submitted file with its submission date, the actions "Open" and "Download" as well as the button "Submitted documents": assessment workflow of an individual person in the assessment tool](assets/Aufgabe_abgegeben.png){ class="shadow lightbox" }

You can find out how to assess the assessment modules of individual persons in general in a [step-by-step guide](Assessment_of_learners.md).

### Submissions from all or multiple users

If many solution attempts have been uploaded or you need to assess many learners, it is recommended to use the "Export results" button to download all solution attempts at once. In the downloaded folder you will also find all the task assignments. 

Alternatively, you can select the desired people and then choose the option "Export results".

Afterwards you can fill in the [Assessment form](The_assessment_form.md). It will appear under "Assessment" when you assess a course element.


### Excel report of the results [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9601)" }](https://track.frentix.com/issue/OO-9601) {: #results_export}

Besides the submitted documents, the zip file from "Export results" contains an Excel report. It carries one row per person and records who completed which step and when. Course owners read from it, for example, which coach completed an assessment, and base the remuneration of the assessment work on it.

Besides the sequential number, course path, first access and the person data, the report contains these columns:

Column | Content | Appears
---------|----------|----------
Group | Name of the group that submitted the solution | only for the course element Group task
Task | Title of the assigned task | if the step Task is activated
Step | Workflow step the person currently stands in | always
Assignment completed | Date on which the task was assigned | if the step Task is activated
Submission completed | Date of the final submission | always
Feedback completed | Date on which return and feedback were completed | if the step Feedback is activated
Revision completed | Date on which the revision was completed | if the step Revision is activated
Grading completed | Date on which the assessment was completed | if the step Assessment is activated
Remarks | Remarks on the submission | always
Coach | The coach assigned to the person | if the assignment of coaches and participants is activated

The column "Coach" stands behind the assessment columns (Score, Passed, Attempts, last change).

A step that is not activated in the course element produces no column. So if the column "Feedback completed" is missing, the step Feedback is not active in this course element. Which steps are active is defined by course owners in the course editor: `Course > Course editor > "Task element" > Tab "Workflow"`.

The course archiving produces the same Excel report, provided the step Assessment is activated in the course element.


## Assessment workflow course element "Task"

Exactly which steps are available in the evaluation flow depends on the specific configuration of the task module. The details are defined in the configuration of the course element ["Task"](../learningresources/Course_Element_Task.md) or ["Group task"](../learningresources/Course_Element_Grouptask.md). In the assessment tool, the assessment options can no longer be changed.

If desired and configured accordingly, a return document can be uploaded. This could be, for example, a detailed evaluation table or a revised version of the submission. It is also possible to return a submission to the learner via the "Revision" button and trigger a revision loop.

Once participants have definitely submitted a task, it is no longer possible for them to submit it again or to exchange it. However, if an assignment is submitted by mistake or the wrong document is uploaded, the coach can "reopen submission" and allow the learner to submit another submission.

Both learners and teachers can see how far the assessment workflow has progressed by the green ticks next to the individual assessment steps.

Once a submission has been accepted and the user is not to make any more submissions or revisions, the "Accept Submission" button should be confirmed. 

The further assessment actions for the task take place in the lower part in the "Assessment" area, in the actual assessment form. Here points, feedbacks etc. can be deposited. A description of the possibilities can also be found [here](The_assessment_form.md).

## Assessment workflow course element "Group task"

The evaluation of submissions via the course element "Group task" is similar to the course element "Task".

 * Go to the desired group task.
 * Select the desired group in the "Overview" tab or filter the desired group in the "Participants" tab.
 * Provided that a group member has made a submission for the group, this submission applies to the entire group and can now also be evaluated for the entire group.
 * Click on a group member or select the "View / Assess details" option in the 3-dot area and you will be taken to the assessment flow for the group.
 * Carry out the assessment in the same way as the assessment of the course element Task.

In the "Assessment" area, i.e. the actual assessment form, click on the "Assess" button.

![Assignment, submission and return of the group are completed, the step Assessment stands on "Open" and shows the performance overview of both group members with the button "Assess": assessment workflow of a group in the assessment tool](assets/Gruppe_bewerten.png){ class="shadow lightbox" }

The advantage of a group task is that an assessment can be made for all group members at once using the "Grade" button, but at the same time adjustments can be made for individual group members.

If not the whole group has passed or not all should receive the same score, "For the whole group" must _not_ be selected. This makes individual scoring per participant possible.

![The activated checkbox "For the whole group" transfers score and comment to all group members, below it the choice between "Not released" and "Released": dialogue Assessment of a group task](assets/Gruppenbewertung.png){ class="shadow lightbox" }


!!! info "Important"

    If other assessable course elements are to be assessed instead of a "group task" for a group, the assessments must be made separately for each group member.

!!! note "Hint"

    In the course run, the assessment of the individual groups is also possible, similar to the course element Task in general.