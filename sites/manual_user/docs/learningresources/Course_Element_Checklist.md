# Course Element "Checklist" {: #course_element_checklist}


## Profile

Name | Checklist
---------|----------
Icon | :o_icon_o_cl_icon:
Available since | Release 9.4
Functional group | Assessment
Purpose | Checklist with functions such as blocking the editing option by submission date, grayed out checkboxes that only coaches can check off, etc.
Assessable | yes
Specialty / Note |



Achieved goals, missing tasks, correct or incorrect solutions - checklists make this visible and thus also assessable for coaches.

As an informational work aid that supports participants in completing smaller tasks, for example, or in keeping information secure, the checklist allows participants to keep to-do or check lists, for example. For example, tasks outside of OpenOlat can also be documented. If this is the case, you may find information about the evaluation on the start page of the checklist.

If a checklist has been given a submission date, it cannot be edited afterwards. Below the submission date and rating information is the actual list with all the checkboxes, including any information and files to download. If a checkbox appears grayed out, either only coaches can check it, or the submission date has already passed.

Several checklists can also be added at once. This procedure is useful if you need several identical checklists. Several (maximum 12) modules with the same check elements are created and bundled with a structure module. A title is automatically created for each module, but changes are possible. Each module can then be given a specific delivery date.

Thus, several checklists with identical check criteria but for different groups, for different objects to be checked, for different event dates or for checking the same object at different points in time (development) can be created relatively quickly.

## Create and configure a checklist [:octicons-tag-16:{ title="from Release 9.4 (OO-936)" }](https://track.frentix.com/issue/OO-936){:target="_blank"}

By means of the course element "Checklist" you add a checklist to your course. For each course element, create a checklist with as many checkboxes as needed. Create individual checkboxes in the tab "Checkboxes" via the button "Add checkbox". You can also assign points to the checkboxes and add files for download.

## Tab Configuration [:octicons-tag-16:{ title="from Release 17.0 (OO-6458)" }](https://track.frentix.com/issue/OO-6458){:target="_blank"} {: #tab_configuration}

In this tab, you determine whether a deadline should be effective for the checklist and if and how participants are assessed. Depending on the selected settings, you have different assessment options at your disposal. Later, you assess either in the course with the course editor closed or in the [Assessment tool](../learningresources/Assessment_of_course_modules.md) of the course.

The tab is divided into the areas "Checklist configuration", "Grading configuration" and "Assessment form". If assessments already exist for the checklist, OpenOlat displays the settings under "Grading configuration" as read-only. The deadline under "Checklist configuration" and the area "Assessment form" remain editable. With "Enable edit mode" you make the settings editable again, see [Read-only assessment configuration](Course_Elements.md#assessment_config_read_only). [:octicons-tag-16:{ title="from Release 21.1 (OO-9647)" }](https://track.frentix.com/issue/OO-9647)

### Checklist configuration {: #checklist_configuration}

#### Lock checklist for users on deadline {: #lock_checklist}

If this toggle is switched on, participants can no longer edit the checklist once the deadline has been reached.

#### Deadline {: #deadline}

The field appears if "Lock checklist for users on deadline" is switched on. Set the date by which participants must have completed the checklist.

### Grading configuration {: #grading_configuration}

#### Score granted {: #score_granted}

If you assign points to the individual checkboxes in the "Checkboxes" tab, participants receive these points for each marked checkbox, awarded manually or automatically. If the toggle is switched off, OpenOlat does not award any points.

#### Minimum score {: #min_score}

Enter the minimum score participants can achieve. The field appears if "Score granted" is switched on.

#### Maximum score {: #max_score}

Enter the maximum score participants can achieve. The field appears if "Score granted" is switched on.

#### Levels/Grading {: #grading}

If "Score granted" is switched on, you can additionally select a rating scale. OpenOlat then converts the points into a grade. More about this on the page [Levels/Grading](Assessment_translate_points_in_grades.md).

#### Display passed / not passed {: #display_passed}

If you switch on the toggle, participants see "Passed" or "Failed". If it is switched off, OpenOlat does not display a passed status. If "Levels/Grading" is switched on, the toggle does not appear: the rating scale then determines the passed status.

#### Type of display {: #output_type}

The field appears if "Display passed / not passed" is switched on. With "Automatic (using cut value)" or "Automatic (using number of checks)", OpenOlat allocates the passed status automatically, based on a cut value or on a certain number of marked checkboxes. With "Manually by tutor", coaches allocate the status themselves.

#### Passed cut value {: #cut_value}

Enter the minimum number of points participants need to get "Passed". Below this cut value they get "Failed". The field appears if the option "Automatic (using cut value)" is selected under "Type of display".

#### Number of checks needed to pass {: #checks_to_pass}

Enter the minimum number of checkboxes participants must have marked to get "Passed". The field appears if the option "Automatic (using number of checks)" is selected under "Type of display".

#### Include in course assessment {: #include_in_course_assessment}

In learning path courses, the option appears as soon as "Score granted" or "Display passed / not passed" is switched on. If it is switched off, the checklist is not taken into account in the course assessment.

#### Scaling factor for course assessment {: #score_scaling}

The field appears if the course assessment adds up the points with weighting and "Score granted" as well as "Include in course assessment" are switched on. OpenOlat multiplies the points of the checklist by this factor for the course assessment. More about this under [Course assessment with points: Sum with weighting](Course_Settings_Assessment.md#evaluation_with_points_weighting).

### Assessment form {: #assessment_form}

#### Individual comment {: #individual_comment}

When checking this box, you have the possibility to give each participant an individual comment during the assessment.

#### Individual assessment documents {: #individual_assessment_documents}

When checking this box, you can provide documents to each participant during the assessment, for example as feedback.

## Tab Checkboxes [:octicons-tag-16:{ title="from Release 15.1 (OO-4758)" }](https://track.frentix.com/issue/OO-4758){:target="_blank"} {: #tab_checkboxes}

In this tab you create and edit the checkboxes that participants or coaches tick afterwards. Click the button "Add checkbox" to create a new checkbox. A form with the following fields opens.

### Title {: #checkbox_title}

Enter a meaningful short title for the checkbox.

### Access {: #checkbox_release}

With this setting you define who can mark the checkbox. "Participant and coach" allows both participants and coaches to mark the checkbox. If you select "Coach only", participants see the checkbox but cannot mark it.

### Label {: #checkbox_label}

You can select from 11 different types of checkboxes: Achieved, Done, Processed, Fulfilled, Passed, Presented, Verified, Attendant, Read, Viewed and Confirmed. Choose the one most appropriate for your purpose.

### Score {: #checkbox_points}

Specify whether points are awarded for marked checkboxes and how many.

### Description {: #checkbox_description}

The description appears in the checklist to the right of the checkbox along with the title, the score (if configured) and the uploaded file, if applicable.

### File {: #checkbox_file}

If necessary, add a file for the participants to download here.

The table of the tab then shows an overview of the checkboxes you have created. Here you also change their order.

## Tab Badges [:octicons-tag-16:{ title="from Release 18.0 (OO-7003)" }](https://track.frentix.com/issue/OO-7003){:target="_blank"}

If course owners have activated the awarding of badges under `Course > Administration > Settings > Tab "Assessment" > Section "Badges"`, the course editor shows the tab "Badges" for this course element. There you create a badge specifically for this course element.

[To the top of the page ^](#course_element_checklist)


## Use and evaluate checklists [:octicons-tag-16:{ title="from Release 16.1 (OO-5946)" }](https://track.frentix.com/issue/OO-5946){:target="_blank"}

In the course, course owners and coaches see the tabs "Overview", "Participants" and "Preview" in the course element, depending on the configuration also "Reminders" and "Badges". Participants without coach rights see their checklist directly. If points have been assigned to the individual checkboxes, they are visible to the learners in their checklist. This way, the learners see directly how an overall score is made up.

The "Participants" tab offers you as course owner or coach an overview of all checklists of the participants coached by you. If you coach several groups, you can filter the overview table by group. In the same tab, you assess the checklists of the individual learners, either per person or via the button "Edit per checkbox".

In addition, the button "PDF overview" prints the current state of the checklist across all participants as a PDF. In the PDF you find the column "Signature", with which participants confirm the correctness of the document.

The button "PDF marked checkboxes" creates a PDF containing a table per checkbox with the participants who have already marked this checkbox.

!!! warning "Attention"

    If possible, change the checkboxes only after the deadline has expired.

Altogether you have four ways to edit the checklists of participants.

  1. **Edit**: The link in the table opens the checklist of the individual person, in which you mark single checkboxes. From there you also have direct access to the assessment tool: open the tab "Assessment" to reach the assessment form. You also change the assessment in the assessment tool.
  2. **Edit per checkbox**: The button opens a list of all participants, sorted by checkbox. Select the desired checkbox in the dropdown list. This reduces the error rate, especially for large checklists with many checkboxes.

      Filter by group beforehand in the table of the checklist management. You can sort the table by first or last name to match the participants list with the checklist more easily.

  3. **Edit**: The button opens the overview table in edit mode, in which you edit all checkboxes of all participants.
  4. **Assessment tool**: And finally, you select or deselect checkboxes of individual participants in the [Assessment tool](../learningresources/Assessment_of_course_modules.md) as well.

##  Course element: Multiple checklists [:octicons-tag-16:{ title="from Release 9.4 (OO-937)" }](https://track.frentix.com/issue/OO-937){:target="_blank"} {: #multi}

![Icon of the course element Multiple checklists](assets/wizard_434343_64.png)

If activated by the OpenOlat Admin, the option "Multiple checklists" is also available. It opens the checklist wizard, which enables you to create multiple similar checklists simultaneously. They will be added as child nodes to a structure course element. The checklist group is inserted at the bottom of the course. You can arrange the group or individual checklists afterwards via drag & drop into their correct order.

In the **first** step, create a template for the checklist group to be created by defining the type and number of checkboxes, and configure it in the second step. All lists and settings can be edited separately in the course editor after creation.

The  **second**  step lets you determine how many checklists should be created based on the template defined in the first step. Specify a title, which will then make up the individual checklist titles together with a sequential number. You can adapt the titles in the next step. Here you also define whether and how points are to be awarded or the Pass attribute is to be assigned.

For more information on the other settings, please refer to [Tab Configuration](#tab_configuration). If you configured the checklists to have a deadline, you can define the date in the third step.

The  **third**  step of the wizard allows you to customize the individual checklist titles according to your requirements. Define the individual due dates here, if you enabled the deadline in the previous step. Just leave the date input field blank, if you do not wish to configure a deadline. 

Define the title and description of the parent structure course element in the **fourth**  and last step. Both short title and title are displayed as usual in the course.

In the lower part of the form, you determine whether the course element "Structure" displays assessment information from the checklists and how it combines it. For more information on the course element "Structure" and the assessment information of other course elements, please refer to the chapter Knowledge Transfer - [Structural element: Score](Course_Element_Structure.md#score).

## Further information {: #further_information}

**Mentioned on this page**<br>
[Assessment of course modules >](../learningresources/Assessment_of_course_modules.md)<br>
[Course elements at a glance >](../learningresources/Course_Elements.md)<br>
[Levels/Grading >](../learningresources/Assessment_translate_points_in_grades.md)<br>
[Course Settings - Tab Assessment >](../learningresources/Course_Settings_Assessment.md)<br>
[Course Element "Structure" >](Course_Element_Structure.md)

**Further reading**<br>
[Badges >](../learningresources/OpenBadges.md)

[To the top of the page ^](#course_element_checklist)

