# Assess tasks {: #assess_tasks}

The assessment of handed in tasks can be done by coaches and course owners either in the assessment tool or directly in the course run.

You can find out in detail how tasks and group tasks are evaluated in the assessment tool in the chapter ["Assessment tool"](../learningresources/Assessment_tool_overview.md) → ["Assessing tasks and group tasks"](../learningresources/Assessing_tasks_and_group_tasks.md). The following is a brief description of how the assessment is performed in the run time view:

## Coach view {: #coach_view}

In the run time view you get to the assessment area by clicking on the corresponding task. The tabs "Overview" and "Participants" are available. For the course element Task, the tab "Workflow" is added. If the assignment is stored directly in the task, the tab "Edit tasks and sample solutions" also appears. If a coach may also create tasks, the tab "Edit tasks and sample solutions" is also visible for him. If reminders or to-dos are set up, the tab "Reminders & to-dos" appears for course owners.

In the tab "Participants", filter tabs narrow down the list, among them "All" and "Relevant". Which further tabs appear depends on the configuration of the course element.

The table displays the current workflow step in the column "Step". The symbol :o_icon_o_icon_info: in front of the step means that an action by the coach is required. The steps Review and Correction require coach input in order for the user to be able to finalize the task. Whether the step Solution (without icon) includes the assessment step, depends on the configuration of the task. The Grading step is only displayed if no sample solution is available, but remains, even with the assessment already carried out. Choose the column according to your needs.

![The column "Step" names the workflow step reached for each person and marks with an info symbol where an action is required; next to it stand Coach, Task, Submission date, Score, Passed, number of documents and State, above them the actions "Export results" and "Statistic": tab Participants of the coach view in the course](assets/task_correction.png){ class="shadow lightbox" }

Clicking on an individual person in the participant list takes you to the assessment workflow for that person and allows you to upload feedback and assign points, depending on the configuration of the task.

To process several people at once, select the rows you want. As soon as one row is selected, the actions "Finalize assessment", "Release", "Withdraw release", "Extend", "Export results" and "E-Mail" appear above the list.

![After a row is selected, a bar with six actions for the selected people appears above the list: "Finalize assessment", "Release", "Withdraw release", "Extend", "Export results" and "E-Mail": tab Participants of the coach view in the course](assets/task_coach_bulk_actions_en.png){ class="shadow lightbox" }

All files uploaded by the participant can be downloaded in the tab "Submissions" as well as in the assessment tool with one click on the button "Export results". The single uploads are saved sorted after learners (last name, name, username) with the corresponding sub folders as zip file.

The zip file additionally contains an Excel report. It carries a separate date column for every activated workflow step, that is exactly for the steps that the overview table shows in the column "Step". If the assignment of coaches and participants is activated, the report also states the assigned coach. The individual columns are described under [Excel report of the results](Assessing_tasks_and_group_tasks.md#results_export).

If the coach assignment is activated, the column "Coach" of the overview table shows who supervises a person. The assignment itself is made by course owners via the [assignment table](Course_Element_Task.md#coach_assignment_table); coaches do not see this button.

If no file is uploaded until the submission deadline it is marked in the overview as "No submission".

!!! tip "Hint"

    If you are simultaneously registered in the course as a course owner and a participant, you can switch between the respective roles to see how the task looks from the learner's point of view.

How participants will see the course element "Task" will be explained in the chapter "Learning Activities in Courses," section ["Task and Group Task"](../learningresources/Course_Elements.md).

### Changing return and feedback documents {: #return_feedback}

To change the feedback documents of individual participants under "Return and feedback" for a task that has already been completed, coaches can proceed as follows:

!!! warning "Attention"

    Feedback documents can only be changed as long as the submission deadline has not yet passed. If necessary, this deadline has to be extended!

    In order to prevent participants from accessing the task again in this case, the course element can be "blocked for learners" in the course editor --> Visibility tab, for example. Attention: this option is not available in the learning path course!

- Select the participant in the course element.
- In the "Submission" step, select "Reopen submission".
- The following message appears:

    ![The message lists the three consequences of reopening: documents already submitted are no longer accessible, the person has to submit again, the submission deadline needs checking: dialogue Reopen submission](assets/Task_reopen_submission.png){ class="shadow lightbox aside-right-sm" }
    The submission for "Last name, First name" is reopened:<br>
        * Documents already submitted are no longer accessible to you<br>
        * The participant can edit the documents and must submit them again<br>
        * Please check the submission deadline!

- After confirming the notification, coaches can use a button "Collect all submitted documents". The documents of the participant are now available again in the coach view.
- In the "Return and feedback" step, the documents can now also be edited, exchanged, supplemented or deleted again.

!!! warning

    Don't forget: Change the submission deadline back to the original value, and participants will no longer be able to submit anything. Also, the restriction of visibility for learners on the course element can now be removed again so that the task is available again for all participants in the course navigation.
