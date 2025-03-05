# Course Element "Task" {: #course_element_task}

## Profile

Name | Task
---------|----------
Icon | ![Task Icon](assets/task.png){ class=size24 }
Available since | New edition with release 19
Functional group | Assessment
Purpose | Modeling of complex task workflows with configurable substeps such as submission of solution documents, feedback and revision loop, provision of sample solution and assessment
Assessable | yes
Specialty / Note | also available as [group task](../learningresources/Course_Element_Grouptask.md)


Teachers can use the course element Assignment to organize **file submissions** and **submission assignments**. Learners upload their submissions to the OpenOlat course and receive feedback or an assessment from the teacher. Peer reviews are also possible. Revisions can also be requested or sample solutions provided.


## Create task (Author perspective) {: #create_task}

A task is created and configured in the course editor, as with all course elements.

![course_element_task_tabs_v1_de.png](assets/course_element_task_tabs_v1_de.png){ class="shadow lightbox"}

!!! note "Quick Links: Create tasks (Author perspective)"

    * [Tab Title](#title)<br> General information about the course element
    * [Tab Layout](#layout)<br> General settings in the layout
    * [Tab Learning path](#learningpath)<br> Should the task be voluntary, mandatory or only for certain groups of people?
    * [Tab Workflow](#workflow)<br> Here you determine which steps the task should contain.
    * [Tab Assignment](#assignment)<br> Creation or upload of the task, assignment of different tasks or drawing, etc.
    * [Tab Submission](#submission)<br> Definition of expected submissions (with template?, as audio/video recording?, etc.)
    * [Tab Revisions](#revisions)<br> E.g. definition of the process for a peer review.
    * [Tab Grading](#grading)<br> Configuration of the grading, criterion for passing, consideration in the course evaluation, etc.
    * [Tab Sample](#sample)<br> E.g. provision of a pdf file.
    * [Tab Highscore](#highscore)<br> Visualization of the results if points are awarded.
    * [Tab Reminders](#reminders)<br> Preparation of automatic reminder emails and to-dos


### Tab "Title"  {: #title}

The layout options are the same as those contained in all course elements.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)

### Tab "Layout"  {: #layout}

The layout options are the same as those contained in all course elements.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)

### Tab "Learning path"  {: #learningpath}

!!! info "Traditional courses"

    Traditional courses do not have the “Learning path” tab and instead have the “Visibility” and “Access” tabs, including expert mode.


Here you define whether the execution of the task is obligatory or voluntary or if the course element should hidden. Obligatory tasks are taken into account in the progress display, voluntary ones are not.

The **release date** can be used if the course element is to be opened and started only on a certain date. However, the course element itself is already displayed in the course structure.

The time entered under "**To be edited by**" refers to the deadline for picking up or starting the course element Task, not to the deadline for file upload (see tab Workflow).

In the case of the **processing time**, the estimated time a user needs to process the course element can be entered. An entry is especially relevant if the progress in the course refers to the processing time of the course elements (see Administration -> [Settings](../learningresources/Course_Settings.md) -> Tab "Execution").

The "Learning Path" tab also defines which criterion must be met for the task to be considered "completed". The following options are available:

![Completion criterion](assets/task_completion_criterion.png){ class="shadow" }

* **Visit course element**: User has clicked on the course element.
* **Confirmation by participant:** User has clicked on the "I've read the content" button.
* **Score**: The user has achieved at least the specified score while completing the task.
* **Passed**: The user has fulfilled the "passed" requirements configured in the "Grading" tab or the task has been manually set to passed by the coach.
* **Execution done**: All steps of the task flow were run through.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


!!! info "Traditional courses"

    Traditional courses do not have the "Learning Path" tab and instead have the "Visibility" and "Access" tabs, including expert mode.

### Tab "Workflow"  {: #workflow}

In the “Workflow” tab, you define which individual elements the task should contain.

!!! tip "Hint"

    Start the configuration in this tab and select the functions you require. The required tabs are then active/inactive and can be configured further.

![course_element_task_workflow_elements_v2_de.png](assets/course_element_task_workflow_elements_v2_de.png){ class="shadow lightbox"}

![1_green_24.png](assets/1_green_24.png) **Relative date**<br>
Instead of entering calendar data, you can also work with _relative data_. Specify how many days after the first course visit or booking the assignment remains open. All set times can also be adjusted individually, e.g. if a learner needs an extension due to certain circumstances. This applies to all process steps. If you extend the submission date, the task is reopened. A late submission date is also possible.

=== “With fixed date”

    ![course_element_task_workflow_fix_dates_v1_de](assets/course_element_task_workflow_fix_dates_v1_de.png){ class="shadow lightbox" }

=== “With relative date”

    ![course_element_task_workflow_relative_dates_v1_de](assets/course_element_task_workflow_relative_dates_v1_de.png){ class="shadow lightbox" }

The changeover to relative data affects the input fields for **Task**, **Submission** and **Sample solution**.

![2_green_24.png](assets/2_green_24.png) **Task**<br>
Should a specific task be stored in the course element or can the user perhaps find the task elsewhere? Should the user submit a document? Should there be feedback from the teacher? Should users be given the opportunity to revise a submission if necessary? Should a sample solution be provided? Should an assessment with points or a pass be possible? Should certain learners be assessed by certain coaches?

Simply activate the things you need and configure the relevant tabs in the next step.

![3_green_24.png](assets/3_green_24.png) **Submission**<br>
The sections Task, Submission, Late submission and Sample solution can be given a date. The task and submission are available until the date entered. If late submission is activated and a deadline is set, participants can still submit their solution up to the late deadline. Both the normal submission deadline and the late deadline are displayed for the user, or the deadlines that are still in the future. The late submission is also indicated to the coach or course owner in the evaluation flow.

![4_green_24.png](assets/4_green_24.png) **Feedback**<br>
By default, feedback is given by coaches, but it can also be given by the other participants (peer review).

![5_green_24.png](assets/5_green_24.png) **Correction**<br>
The submission of revisions by participants after correction is optional.

![6_green_24.png](assets/6_green_24.png) **Sample solution**<br>
A sample solution can be provided for all participants or only those who have completed the task from the date entered.
If sample solutions are activated, you can also define here whether coaches are allowed to add and edit documents.

![7_green_24.png](assets/7_green_24.png) **Assessment**<br>
Activating this toggle button activates the "Assessment" tab, in which the details of the assessment can be configured.

![8_green_24.png](assets/8_green_24.png) **Document configuration**<br>
This option is only displayed if one of the options "Task" or "Sample solution" has been selected and thus the upload of documents is required. In addition to course owners, coaches can also be allowed to add and edit documents here.

![9_green_24.png](assets/9_green_24.png) **Coaching**<br>
Participant-dependent coaching can be activated and configured in the "Coaching" section of the "Workflow" tab.

![Betreuerabhängige Bewertung](assets/course_element_task_workflow_assign_coaches_v1_de.png)

* **Assignment of coaches/participants**<br>
Selecting this checkbox displays the other options for coaches.
The differentiated assignment of persons then takes place when the course editor is closed.

* **Coaches available for selection**<br>
It can be decided whether, in addition to coaches, course owners should also be assigned to coach participants.

* **Type of assignment**<br>
The assignment (allocation) of coaches to a participant can be done manually or automatically.

* **Notification of coach**<br>
Select here in which cases coaches receive a notification by email.

* **Notification of participants**<br>
Select here whether participants should be informed by email about the assignment to a coach.

!!! warning "Warning"

    Changing the workflow will delete the corresponding elements from the workflow for all members or groups.
    
    When changes are made to the workflow, such as removing the assignment, all participants or groups in the course will have that component of the workflow removed. The information about already selected tasks is then no longer visible. However, if the workflow component is inserted again, this information will be accessible again.

    However, if you add the assignment step later and a member or group is already further into the task, then they don't have to choose an assignment anymore.

!!! warning "Warning"

    If no person has the role of coach among the course members and at the same time course owners do not perform any coach tasks (Workflow tab > "Coach" section > "Coaches available for selection"), then no coach assignment can take place.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)

### Tab "Assignment"   {: #assignment}

!!! info "Requirement"
    
    The "Task" must have been activated in the "Workflow" tab so that you can now make it available. 

**a) Upload files**

Upload tasks created outside of OpenOlat (upload assignment).
You can also upload a zip file with several (different) tasks and provide each file with a suitable title and description.

**b) Create files in different formats**

Create files directly in OpenOlat. Exactly which formats are available depends on which have been activated by the OpenOlat administration. In most cases, at least one HTML editor is available. But it is also possible to create Word, Excel, PowerPoint and, since :octicons-tag-24: release 18.1, diagrams or whiteboards. In addition, a specific video task or, from :octicons-tag-24: Release 18.1, an audio task can also be created.

If a task is created with the internal OpenOlat HTML editor, multiple files such as images or PDF files can be provided by first uploading them in the HTML editor and then linking them in the corresponding html page. Such a task will then be downloaded in .zip file format as well. If the HTML editor is used, the stored title is automatically used as the file name. However, this can be changed at any time.

!!! info "Multiple files"

    Please note: If multiple files are stored in the Task tab, they will be considered as multiple different tasks. It is _not_ a task with several complementary files.

Select in the field "Type of drawing" if several course participants can solve the same task or if each task or if each student should solve a different task.

In the "Type of draw" field, select whether several course participants can solve the same task or whether each course participant should solve a different task. If the task is selected manually, you can also specify in the "Preview" field whether the course participants can view the task before selecting it. If each course participant is to solve a different task for "Type of draw", at least as many tasks must be entered as there are course participants who are to solve this task.

!!! info "Hint"

    If the course element contains only one task, manual selection is not very useful. In this case, it is best to use the automatic assignment.

In the field "Message for user" you can provide general information for all course participants regarding your tasks.

In the setting manual choice, if a course participant choses by incident a wrong or not-wanted assignment, it can be reset in the [assessment tool](../learningresources/Assessment_tool_overview.md) by the course owner.

![Reset data of task](assets/task_reset_assessmenttool.png){ class="shadow" }

The assignment is not reset automatically. The participant gets the opportunity to undo all pervious steps.

![Reset task](assets/task_reset_user.png){ class="shadow" }

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


### Tab "Submission"  {: #submission}

Here you define the type and scope of the submission options for the participants.

!!! info "Requirements"

    In the tab "Workflow"

    * "Submission" must be activated in order to configurated them. 

    ![course_element_task_workflow_activate_submission_v1_de.png](assets/course_element_task_workflow_activate_submission_v1_de.png){ class="shadow lightbox" }


After activation, you can choose from:

**"Upload documents"**: In this case, course participants can upload and submit documents created outside of OpenOlat.

**"Submission with OpenOlat Editor**: With this selection, participants can create documents directly in the course element. An HTML editor can be used for this by default. If other document editors are integrated in OpenOlat, documents can also be created in other formats such as Word, Excel, etc.

**Allow video recordings**: In this case, learners can create and submit video recordings via webcam. A maximum recording duration and a quality level can also be selected for the videos.

**Allow audio recordings**: Here the user has the possibility to create and submit a sound recording directly in OpenOlat. (Since :octicons-tag-24: Release 18.1.)

!!! info "Hint"

    Audio and video recordings must always be combined with one of the options "Upload documents" or "Submit with OpenOlat Editor". 

Activate **"Task is template for submission"** if learners are to use the stored task file as the basis for their work, for example if the task contains a pre-structured table to be filled in. The prerequisite is that this option has been enabled by the OpenOlat administrators.

![mit Vorlage bearbeiten](assets/Aufgabe_Vorlage.png)

You can also define the minimum and maximum number of documents for submission. Leave the "Max. number of documents" field blank if you do not want to limit the number of documents. If it is mandatory to submit several documents, you can also increase the minimum number of documents.

Activate the e-mail confirmation so that people who have submitted a task receive a corresponding e-mail. The pre-formulated e-mail text can be further customized if required.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


### Tab "Revisions"  {: #revisions}

!!! info "Requirements"

    In the tab "Workflow"

    * "Return and feedback" must have been activated so that you can now set this up,
    * whether the feedback should be provided by coaches or peer review.

    ![course_element_task_workflow_activate_fb_v1_de.png](assets/course_element_task_workflow_activate_fb_v1_de.png){ class="shadow lightbox" }


**Revisions by coaches**

If the "By coach" option was selected in the Workflow tab, the minimum and maximum number of return documents that participants are allowed to submit during the "Return and feedback" and "Revision" steps can now be defined in the "Return and feedback" tab.

**Return and feedback**

If the "With peer review" option was selected in the Workflow tab, the rules for the submission of feedback by other participants can now be defined in the "Return and feedback" tab. The feedback from the reviewers is given in a [form](../learningresources/Rubric.md). As the course owner, enter this [form](../learningresources/Rubric.md). For a peer review, it must be a form that contains at least 1 rubric element, because only the rubric element passes on the points achieved in it to the course element.

![course_element_task_fb_v1_de.png](assets/course_element_task_fb_v1_de.png){ class="shadow lightbox" }

You can also provide feedback to the reviewers (Helpful? Yes/No and star rating).

In order for coaches as well as course owners to be able to trigger the automatic reviewer assignment, the corresponding option must be selected in the "Return and feedback" tab, "Authorizations" section.


### Tab "Grading"  {: #grading}

Here you define _how_ each course participant shall be assessed. Should there be points? Should there be a pass/fail for the course element? Should the point evaluation be linked to a rating scale? If so, with which? Should it be possible to provide further individual comments or documents? Decide in each case what is suitable for your scenario.

A form with a rubric can also be used for the assessment. The points can then be taken from the rubric form for the assessment of the course element. <br> The rubric form included here in the "Assessment" tab is to be distinguished from the rubric form used in the "Return and feedback" tab for peer reviews.

![course_element_task_tab_grading_rubrik_v1_de.png](assets/course_element_task_tab_grading_rubrik_v1_de.png){ class="shadow lightbox" }

#### Awarding points

If scoring has been activated, the minimum and maximum number of points must be specified. You can then also select the "Assessment with grading/marks" option and configure it further. The respective points can be assigned specific evaluation scales such as levels, grades, (competence) levels or labels. The available rating scales are defined by the OpenOlat administrator and can be selected via the "Edit rating scale" button and the points can be adjusted in detail. It must also be defined whether the assignment to the calculated classification is made manually by the coach or whether it should be displayed automatically when points are changed.

#### Total points from...

The total points can be calculated from one or more sources:

* **Rubric-assessment**: If a rubric form is used in the "Assessment" tab, points can be transferred from there.
* **Rubric-peer-review**: A peer review uses the rubric form, which is included in the "Return and feedback" tab.
* **Submitted reviews**: Additional points can be awarded to the person for reviewing other participants (points per completed review, configured below this selection as soon as the option has been selected).


#### Passed/Failed
If activated, passing can either be done manually by the coach or automatically. For automatic assessment, the points allocation must be activated and a points threshold for passing must be specified.

#### Consider in course assessment
In the "Assessment" tab, you can also define whether the result of the specific task module is included in the assessment of the entire course or whether it should be excluded.

#### Individual feedbacks
Optionally, you can also activate the option for individual comments or individual assessment documents so that coaches have even more flexible feedback options.

#### Hints
If you open the extended configuration, further configurations are available. Here you can store information texts for all learners and/or for all coaches.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


### Tab "Sample Solutions"  {: #sample}

In order to provide all course participants with a sample solution regarding your tasks just either upload appropriate documents or directly create them via the embedded text editor. The sample solution is visible after the coach accepted solution documents for submission.

!!! info "Requirements"

    In the tab "Workflow"

    * "Sample solutions" must be activated in order to be configurated.
  
    ![course_element_task_workflow_activate_sample_v1_de.png](assets/course_element_task_workflow_activate_sample_v1_de.png){ class="shadow lightbox" }

By default, the sample solution is only visible once the documents submitted by the participant have been accepted by the coach.

!!! Tip "Hint"

    If the participants are to receive help with the task in advance, upload it together with the task as a ZIP document or use the message field (see "Task" tab).

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)

### Tab "HighScore" {: #highscore}

If points are awarded for the task, you can visualize them with the HighScore options. 

The prerequisite is that the awarding of points has been activated for the task in the "Evaluation" tab. Only then does the Highscore tab become active and can be configured. It can be determined,

* Which elements are displayed,
* if the depiction should be anonymous,
* the time from which the high score list should be visible.

For more information on this tab, which is available in several course elements, see [here](../learningresources/Course_Elements.md).

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


### Tab "Reminders & To-dos"    {: #reminders}

With the reminder function, you can send [Reminders](../learningresources/Course_Reminders.md) to course members in the form of an e-mail and generate automatic [To-dos](../learningresources/Course_todos.md) for the task. To-dos are stored for course participants in the personal menu under "[To-dos](../../personal_menu/To-Dos.md)".

If the automatic creation of to-dos is activated (from :octicons-tag-24: Release 18.2.), learners can see the current status (step) of the corresponding worklow under "My course" -> To-dos and thus quickly recognize whether or which actions currently need to be taken by them. In addition, these to-dos also appear in the user's personal to-dos in the personal tools. 

The to-dos therefore help learners to keep track of their tasks.
Further information on To-dos can be found [here](../basic_concepts/To_Dos_Basics.md).

!!! note "Hint"

    Whether coaches are also allowed to edit to-dos is defined in the course administration settings. To do this, go to the "Options" tab and activate the corresponding checkmark.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


### Tab Badges

If the course owner has activated the assignment of badges under **Administration > Settings > Assessment tab > Badges section**, the ‘Badges’ tab is displayed in the course editor for this course element and a specific badge can be created for this course element.

[Up (Author perspective) ^](#create_task)<br>
[To the top of the page ^](#course_element_task)


!!! info "Hint"

    The functionality and structure of the course elements "Task" and "[Group task](../learningresources/Course_Element_Grouptask.md)" are similar.


---

## Complete tasks (Course participant perspective)  {: #process_task}

All steps of a task (workflow) are displayed to course participants directly in the course element, depending on the configuration of the course element. Once a step has been completed, the next step is displayed and accessible.

![course_element_task_participant_view1_v1_de.png](assets/course_element_task_participant_view1_v1_de.png){ class="shadow lightbox" }

!!! note "Quick Links: Complete tasks (Course participant perspective)

    * [Download assigned tasks](#process_task_download)
    * [Who coaches me?](#process_task_my_coach)
    * [Submit solution](#process_task_solution)
    * [Feedback](#process_task_solution)
    * [Results of a peer review](#process_task_view_reviews)
    * [Rework task](#process_task_rework)
    * [View sample solution](#process_task_view_example)
    * [Read "Assessment" of coach](#process_task_view_coach_assessment)

!!! info "Hint"

    Subscribe to the respective task module to be informed quickly by e-mail about changes.


### Download assigned tasks {: #process_task_download}

Depending on the configuration, one or more tasks are available for selection in the **"Assign task"** step or a task is automatically assigned to you. If the title of the task file is linked for several tasks, you can view the task before selecting it. If you only have the "Select" button, you cannot view the task in advance. A task is automatically assigned as soon as you click on the task before a possible submission deadline.

If you have selected a task or a task has been automatically assigned to you, click on "Download task" to download or display the task. If you click on the file name of the task, the task is displayed. You can then download the task again at any time.

It is also possible that your teacher has not stored the task in the course element "Task", but has chosen a different location, e.g. another course element, an HTML page, an external website or has set the task orally in presence or in an online meeting. In this case, the "Assign task" section does not appear.

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)


### Who coaches me? {: #process_task_my_coach}

In course settings with a large number of participants, they are often coached by several teachers. As a participant, you will be assigned a coach.

As a participant, you will see the coach assigned to you above the task. If no coach is displayed, no one has been assigned to you yet.

![course_element_task_participant_view_mycoach_v1_de.png](assets/course_element_task_participant_view_mycoach_v1_de.png){ class="shadow lightbox" }

With the implementation of peer review, participants have also been able to give each other feedback on the tasks they have completed since Release 19.

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)


### Submit solution {: #process_task_solution}

In the **"Submission"** area, you have the option of submitting your solution. Depending on the teacher's configuration, you can either upload documents, create files with the OpenOlat Editor or create short audio and video recordings directly in OpenOlat.  

![Abgabemöglichkeiten beim KB Aufgabe](assets/Aufgabe_Abgabe18.png)

As a rule, only some of the four options will be available to you.
Upload your solution or create it directly in OpenOlat and the document will be saved temporarily. The documents remain editable for you until you submit your task via the "Final submission" button. You will receive confirmation that you have submitted documents.

In the submission step, which is now marked as completed with a green tick, you will receive an overview of the submitted files. You can still view the files but can no longer make any changes.

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)


### Feedback {: #process_task_feedback}

If you have _not_ made a submission yet and the coach has not provided any feedback, this area will be empty.

If you have submitted an edit and the coach has not yet created a feedback, the corresponding information will appear.

![Info: Noch keine Rückmeldung vom Betreuer](assets/Aufgabe_Rueckgabe_Feedback_offen.png)

As soon as your coach has created feedback, you will find the feedback information in the "Return and feedback" step.

![Info: Bearbeitung wurde akzeptiert und es gibt ein Feedback](assets/Aufgabe_Rueckgabe_Feedback_FB.png)

If your editing was not sufficient and the coach requests a revision, a corresponding message also appears and you have the option of submitting a new edit in the "Revision" step. A deadline may be set for this.

![Info: Die Abgabe wurde zur Überarbeitung zurückgewiesen](assets/Aufgabe_Rueckgabe_Feedback_zurueckgewiesen.png)

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)


### Carry out a peer review {: #process_task_make_reviews}

If a peer review was planned for the task, you will now be assigned review tasks. You are to assess the documents submitted by other course members. The documents you are to review can be assigned to you automatically or manually by coaches. 

![course_element_task_participant_peer1_v1_de.png](assets/course_element_task_participant_peer1_v1_de.png){ class="shadow lightbox" }

Once you have completed all the reviews, finalise this step by clicking on the ‘Complete reviews’ button.

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)


### View results of a peer review {: #process_task_view_reviews}

If a peer review has been scheduled, you will see an overview of the assessments you have given and received.

![course_element_task_participant_peer2_v1_de.png](assets/course_element_task_participant_peer2_v1_de.png){ class="shadow lightbox" }

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)

### Rework task {: #process_task_rework}

If you need to make a revision, proceed as explained under "Submitting a solution" (submission). In the section **"Revision"**, your coach may also return your work to you several times for correction.

As soon as the coach considers the task to be completed, he or she will close the revision period. At any time, you can see which documents have been submitted by you and your coach and can view them.

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)

### View sample solution {: #process_task_view_example}

Your lecturer can attach a **sample solution** to the assignment, which will be visible at a time specified by him/her, but only _after_ your solution has been accepted by the coach. Click on the file name or the “Download sample solutions" button to view or download the sample solution.

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)

### Read "assessment" of coach {: #process_task_view_coach_assessment}

The **Assessment** area includes automatically generated information on the performance overview with status, score, classification of the selected assessment scale, depending on the configuration of the course element. On the other hand, coaches can store feedback in the comments field as well as (assessment) documents in the assessment area. 

![Bewertung User Sicht](assets/Aufgabe_Bewertung_TN.png)

[Up (Participant perspective) ^](#process_task)<br>
[To the top of the page ^](#course_element_task)


---

## Coaching tasks (Coach perspective) {: #coach_task}

!!! note "Quick links: Coaching tasks (Coach perspective)

    * [Rules of a peer review](#coach_task_peer_review_rules)
    * [Coach Peer-Review](#coach_task_peer_review)
    * [Manual assigning of peer reviewers](#coach_task_peer_review_assign_manually)
    * [Automatic assigning of peer reviewers](#coach_task_peer_review_assign_automatically)


### Rules of a peer review {: #coach_task_peer_review_rules}

In a peer review, the participants in a course give each other feedback or an assessment. The feedback can be of a general nature (e.g. in a text field) or also include an assessment with points.

It is not necessary for each participant to review all other participants. It can be determined for how many other people a review must be made.

You can also configure whether the reviewers see the names of the assigned persons, whether only their own name is visible as a reviewer or whether it is fully disclosed who is reviewing whom.

As a coach, you monitor the mutual reviews and can also intervene if necessary.

[Up (Coach perspective) ^](#coach_task)<br>
[To the top of the page ^](#course_element_task)

### Coach peer review {: #coach_task_peer_review}

The procedure for a peer review was determined by the course owner. As a coach, you will find the options for your supervision task accordingly.

* You can see the status of the peer reviews in an overview. In two tabs you will find the assessments received and awarded by the participants.
* As a coach, you can manually assign reviewers.

![course_element_task_coach_peer1_v1_de.png](assets/course_element_task_coach_peer1_v1_de.png){ class="shadow lightbox" }

!!! note "hint"

    Course coaches only see groups in which they themselves are members. If a peer review is to be carried out by members of other groups, the evaluations of these participants are not fully visible to course coaches.

[Up (Coach perspective) ^](#coach_task)<br>
[To the top of the page ^](#course_element_task)

### Manual assigning of peer reviewers {: #coach_task_peer_review_assign_manually}

If you as a coach want to determine who receives a review from whom, you can make the assignment yourself.

![course_element_task_peer-review_assign_reviewer_manually_v1_de.png](assets/course_element_task_peer-review_assign_reviewer_manually_v1_de.png){ class="shadow lightbox" }

[Up (Coach perspective) ^](#coach_task)<br>
[To the top of the page ^](#course_element_task)

### Automatic assigning of peer reviewers {: #coach_task_peer_review_assign_automatically}

The assignment of peer reviewers to participants can also be carried out automatically by OpenOlat. It is carried out according to the set rules. (E.g. defined number of people to be reviewed per participant). Even if manual assignments have already been made by coaches, these are taken into account in the remaining automatic assignments.

The automatic assignment process must be triggered by course owners or course coaches.

![course_element_task_peer-review_assign_reviewer_automatically_v1_de.png](assets/course_element_task_peer-review_assign_reviewer_automatically_v1_de.png){ class="shadow lightbox" }

!!! info "Hint"

    In order for coaches to be able to trigger the automatic reviewer assignment, the corresponding option must have been set up by the course owner.


!!! info "Hint"

    The "Automatically assign reviewer" button is not deactivated after an assignment has been made and is still available. The reason for this is that participants can still be added later or someone has received an extension.



[Up (Coach perspective) ^](#coach_task)<br>
[To the top of the page ^](#course_element_task)

