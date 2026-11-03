# Course Element "Group Task" {: #course_element_group_tasks}


## Profile

Name | Group task
---------|----------
Icon | :o_icon_o_gta_icon:
Available since | Release 10.3 (OO-991)
Functional group | Assessment
Purpose | Modeling of complex task workflows with configurable substeps such as submission of solution documents, feedback and revision loop, provision of sample solution and assessment
Assessable | yes
Specialty / Note | similar to course element Task



With the course element Group task, a group works on a task together and submits together. The course element works largely the same way as the course element ["Task"](Course_Element_Task.md), where you find the details. The following sections describe what is different for the group task.

## Tab Workflow {: #workflow}
In the tab "Workflow" you define who works on the group task: with "Select groups" you select one or more groups, with "Select areas" one or more learning areas. Only these groups see and work on the task. As long as no group is selected, the course editor reports "You have not selected a group yet", and the course element is not visible when the editor is closed.

!!! info "Important"

    For the group task, the option "Assignment coaches/participants" is missing in the area "Coaching" of the tab "Workflow". Coaches of a group automatically coach its group task, course owners see all groups of the group task.

When changes are made to the workflow, e.g., removing the task, this component of the workflow is removed for all groups in the course. The information about tasks that have already been selected will then no longer be visible. However, if the component is reinserted into the workflow, this information will be accessible again. However, if, for example, the task is added later and a group has already progressed further in its workflow, no task needs to be selected retrospectively.

Subsequent changes to the workflow affect all groups, even if they have already started the workflow.

## Tab Assignment {: #tab_task}
For the group task, each group selects _one_ task. As soon as a group member has selected a task in the step "Task assignment", it applies to the whole group, regardless of who in the group made the selection.

## Tab Submission {: #tab_submission}

If the option "Confirmation e-mail" is enabled, all participants of the group receive a confirmation by e-mail, regardless of who created, uploaded or submitted the files.

## Tab Grading {: #tab_assessment}
If assessments already exist for the group task, OpenOlat displays the settings under "Grading configuration" in the tab "Grading" as read-only. The area "Assessment form" remains editable. With "Enable edit mode" you make the settings editable again, see [Read-only assessment configuration](Assessment.md#assessment_config_read_only). [:octicons-tag-16:{ title="from Release 21.1 (OO-9647)" }](https://track.frentix.com/issue/OO-9647)

Points and feedback apply to the whole group and can be adjusted for individual group members.

When the editor is closed, the course element shows the assigned _groups_ under "Participants", which you select and assess. When assessing, you use the option "For the whole group" to define whether the assessment applies to all group members or only to a single member.

### Column "Group" in the result export [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9601)" }](https://track.frentix.com/issue/OO-9601) {: #results_export}

For the group task, the Excel report from "Export results" carries an additional column "Group" with the name of the group that submitted the solution. This keeps it traceable in the report which submission belongs to which group. The remaining columns are described under [Excel report of the results](Assessing_tasks_and_group_tasks.md#results_export).

## Tab Reminders & to-dos {: #tab_reminders_todo}
For the group task, OpenOlat does not create to-dos, even if the option can be activated in this tab.

## Group task from the participants' perspective {: #group_task_user_perspective}

All decisions and submissions in the workflow apply to the whole group. Therefore, coordinate within the group _before_ anyone submits finally, and keep an eye on the deadlines together.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Course Element "Task" >](Course_Element_Task.md)<br>
[Assessment >](Assessment.md)<br>
[Assessing tasks and group tasks >](Assessing_tasks_and_group_tasks.md)

**Further reading**<br>
[Create Groups >](../groups/Create_Groups.md)<br>
[Group Administration >](../groups/Group_Administration/index.md)

[To the top of the page ^](#course_element_group_tasks)
