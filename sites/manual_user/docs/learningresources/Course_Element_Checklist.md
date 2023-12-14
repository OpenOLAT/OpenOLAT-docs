# Course Element "Checklist"


## Profile

Name | Checklist
---------|----------
Icon | ![Checklist Icon](assets/checklist.png){ class=size24 }
Available since | 
Functional group | Assessment
Purpose | Checklist with functions such as blocking the editing option by submission date, grayed out checkboxes that only coaches can check off, etc.
Assessable | yes
Specialty / Note |



Achieved goals, missing tasks, correct or incorrect solutions - checklists make this visible and thus also assessable for the coach.

As an informational work aid that supports users in completing smaller tasks, for example, or in keeping information secure, the checklist allows users to keep to-do or check lists, for example. For example, tasks outside of OpenOlat can also be documented. If this is the case, you may find information about the evaluation on the start page of the checklist.

If a checklist has been given a submission date, it cannot be edited afterwards. Below the submission date and rating information is the actual list with all the checkboxes, including any information and files to download. If a checkbox appears grayed out, it can either only be checked by the coach, or the submission date has already passed.

Several checklists can also be added at once. This procedure is useful if you need several identical checklists. Several (maximum 12) modules with the same check elements are created and bundled with a structure module. A title is automatically created for each module, but changes are possible. Each module can then be given a specific delivery date.

Thus, several checklists with identical check criteria but for different groups, for different objects to be checked, for different event dates or for checking the same object at different points in time (development) can be created relatively quickly.

## Create and configure a checklist

By means of the course element "Checklist" you can add different kinds of checklists to your course. For each course element, create a checklist with as many checkboxes as needed. Create individual check boxes in the tab "Check boxes" via the button "Add checkbox". You can add files for download to a
checkbox.

###   Tab Configuration

In this tab, you can determine whether a deadline should be effective for the checklist and if and how course participants are assessed. Depending on the selected settings, you have different valuation options at your disposal. The later assessment takes place either in the course run with closed editor or in the [Assessment tool](../learningresources/Assessment_of_course_modules.md) of the course. Once an assessment has taken place, you should not change the configuration anymore.

 ### Configuration settings

 **Lock checklist for users on deadline**: If this checkbox is selected, the checklist can no longer be edited by the learner once the submission date has been reached.

 **Deadline**: Select here whether the checklist must be completed by a certain date. You can lock the list for participants after the expiry of the deadline.

 **Score granted**: If you assign points to the individual checkboxes in the "Checkboxes" tab, you can manually or automatically award points to users for marked check boxes. If you do not check this box no score will be allocated.

 **Minimum score**: Please enter the minimum score a course participant can achieve. You cannot do this if you have not checked the box Score granted.

 **Maximum score**: Please enter the maximum score a course participant can achieve. You cannot do this if you have not checked the box "Score granted".

 **Display passed / failed**: If you check this box a Passed or Failed will be displayed. If you do not check it nothing will be displayed.

 **Type of display**: By means of «Automatic (using cut value)», «Automatic (using number of checks)» or «Manually by tutor», you have the possibility to decide if Passed or Failed is allocated either automatically based on a cut value or if the tutor should allocate it manually. You cannot do this if you have not checked the box Display passed/failed.

 **Passed cut value**: Please enter the minimum number of points necessary to get a Passed. Below this cut value participants get a Failed. You cannot do this if you have selected «Manually by tutor» or «Automatic (using number of checks)» in the field Type of display.

 **Number of checks needed to pass**: Please enter the minimum number of checked boxes necessary to get a Passed. You cannot do this if you have selected «Manually by tutor» or «Automatic (using cut value)» in the field Type of display.

 **Individual comment**: When checking this box you have the possibility to make an individual comment regarding your assessment.

 **Notice for all users** : Please enter a text to be displayed to all participants whenever they click on this course element.

 **Notice for tutors** : Please enter a text to be displayed to the tutors of the course when assessing participants.

###  Tab Checkboxes

In this tab you create and edit the checkboxes that the users can tick later. Click the button "Add checkbox" in order to create a new checkbox. A form opens in a pop-up.

 **Title**: Enter a meaningful short title for the new checkbox.

 **Access**: Define who can actually mark the box as selected. Participant and coach allows for both to check the box. Once "Coach only" is selected, participants will see the box but won‘t be able to select it.

 **Label**: You can select from 11 different types of checkboxes: Achieved, Verified, Done, Fullfilled, Processed, Passed, Attendant, Presented, Read, Viewed, Confirmed. Choose the one most appropriate for your purpose.

 **Score**: Specify whether points are awarded for selected checkboxes and how many.

The **description** is shown in the checklist to the right of the checkbox along with the title, the score (if configured) and the uploaded file, if applicable.

If necessary, you can add a **file** for the participants to download.

The table then displays an overview of the checkboxes that have been created.
The order can also be changed here.

###  Use and evaluate checklists

After you have created the checklist, you will see the two tabs "My Checklist" and "Manage checklists" on the element page. Course participants without coach rights can not see the administration tab. If the checkboxes have a score it is visible to the learners, thus the calculation of the overall score is reasonable.

The checklist management offers an overview of all checklists of participants coached by you, and provides printable overviews. Filter the table by group if you are coaching multiple groups. Edit the checkboxes and assess your participants directly, without leaving the course. The evaluation can be carried out either per person or per box.

You can also download PDFs for offline use. The " **PDF overview**" button opens a PDF file with the checklists current state across all your supervised participants. In the PDF you will still find the Signature column, with which you can have the participant confirm the correctness of the document.

Clicking the "**PDF marked checkboxes**" creates a PDF containing a table per checkbox with all those participants that already checked the box.

!!! warning "Attention"

    Changes to the checkboxes should only be made after the submission date has expired.

Altogether there are four options to edit user checklists and process their assessment at your disposal.

  1. Use the "**Edit**" link in the table, from where you have direct access to the assessment tool. A user-specific checklist opens, allowing you to de/select single checkboxes. Select the " **Assessment**" tab in order to directly access the assessment form. You can also access the assessment form via the assessment tool.
  2. By clicking the "**Edit per checkbox**" button, a new table with a list of all participants filtered by checkbox opens. Select the appropriate checkbox by using the checkbox filter dropdown list. This can reduce the error rate significantly, especially for large checklists with many checkboxes. 

Filter the table beforehand by group. You can then sort by either first or last name, to facilitate matching your participants list with the checklist.

  3. The "**Edit**" button opens the table overview in edit mode, which allows you to edit all checkboxes across all participants.
  4. And finally, checkboxes of participants can also be edited in the [Assessment tool](../learningresources/Assessment_of_course_modules.md).

  

##  Course element: Multiple checklists {: #multi}

![multiple checklists icon.png](assets/wizard_434343_64.png)

If activated by the OpenOlat Admin, the option "Multiple checklists" is also available. It opens the checklist wizard, which enables you to create multiple similar checklists simultaneously. They will be added as child nodes to a structure course element. The checklist group is inserted at the bottom of the course. You can arrange the group or individual checklists afterwards via drag & drop into their correct order.

Create a template for the new checklists on which all to-be-created checklists are based on in the  **first**, and configure them in the second step. All lists, checkboxes and configuration settings can be edited separately in the course editor after creation.

The  **second**  step lets you determine how many checklists should be created based on the template defined in the first step. Specify a title, which will then make up the individual checklist titles together with a sequential number. You can adapt the titles in the next step. Here you also define whether and how points are to be awarded or the Pass attribute is to be assigned.

For more information on the the checklist configuration, please refer to the Checklist: configuration . If you configured the checklists to have a deadline, you can define the date in the third step.

The  **third**  step of the wizard allows you to customize the individual checklist titles according to your requirements. Define the individual due dates here, if you enabled the deadline in the previous step. Just leave the date input field blank, if you do not wish to configure a deadline. 

Define the title and description of the parent structure course element in the **fourth**  and last step. Both short title and title are displayed as usual in the course.

Determine whether assessment information from the checklist sub-elements should be displayed in the course element "Structure", and how the assessment should be conducted. For more information on the course element "Structure" and the assessment information of other course elements, please refer to the chapter Knowledge Transfer - [Structural element: Score](Course_Element_Structure.md#tab-punkte--score).

  

