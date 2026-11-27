# Wizard "Multiple checklists" {: #multiple_checklists}

If you need the same checklist several times, for example for different dates or to check the same object at different points in time, the wizard "Multiple checklists" creates them all in one go, bundled as one chapter in the course menu. You create the checkboxes once as a template, and the wizard uses it to create up to 12 course elements "Checklist" below one common course element "Structure".

## Profile

Name | Multiple checklists
---------|----------
Icon | :o_icon_o_icon_wizard:
Available since | Release 9.4 (OO-937)
Functional group | Assessment
Purpose | Wizard that creates up to 12 checklists from a common template in one step
Creates | per checklist: course element ["Checklist"](Course_Element_Checklist.md), up to 12<br>for all checklists together: one course element ["Structure"](Course_Element_Structure.md)

## All checklists in one chapter {: #structure}

The wizard does not place the checklists individually in the course menu, but bundles them like in a folder below one course element "Structure". This way they appear in the course menu as one chapter, and you move them together. In conventional courses, the course element "Structure" can also add up the points of all checklists and show whether the participants have passed. You define this in the [fourth step](#step_structure).

## Creating multiple checklists [:octicons-tag-16:{ title="from Release 9.4 (OO-937)" }](https://track.frentix.com/issue/OO-937){:target="_blank"} {: #create}

The wizard can be used by anyone who may open the course editor: course owners, administrators, learning resource managers and persons with the [course right "Course editor"](../learningresources/Members_management.md#additional_rights). It is available in conventional courses and in learning path courses.

In the course editor, click "Insert course elements" and, in the group "Assessment", "Multiple checklists". The entry is located directly after "Checklist". A window with the title "Checklist set" opens.<br>
`Course > Administration > Course editor > Insert course elements > Assessment > Multiple checklists`

The wizard guides you through four steps.

### Step 1: Template {: #step_template}

Use "Add checkbox" to create the checkboxes that each checklist should contain. The fields of a checkbox are the same as in the [tab "Checkboxes"](Course_Element_Checklist.md#tab_checkboxes) of a single checklist. The template needs at least one checkbox.

### Step 2: Configuration {: #step_configuration}

Under "Title", enter the common title. Each checklist receives this title with its sequential number, for example "Lab 1", "Lab 2". Under "Quantity", choose between 1 and 12.

The other fields apply to all checklists, for example whether a score is granted or when a checklist counts as passed. They correspond to the [tab "Configuration"](Course_Element_Checklist.md#tab_configuration) of a single checklist.

### Step 3: Title and deadline {: #step_titles}

The wizard shows the checklists with their titles from step 2. Adjust each title if required; a title can be up to 32 characters long. If you set a "Deadline" for a checklist, OpenOlat locks the checklist for participants from that point in time. If you leave the field empty, the checklist has no deadline.

### Step 4: Structure information {: #step_structure}

Enter "Title", "Title in course menu" and "Description" of the course element "Structure" below which the checklists are placed. The "Title in course menu" is the short form that the course menu displays. More about this under [tab "Title and description"](General_Configuration_of_Course_Elements.md#desc). In learning path courses, this step only shows these three fields.

In conventional courses, you also define here whether the course element "Structure" combines the results of the checklists: with "Sum of all checklists" it adds up the points. With "Display passed / not passed" it shows whether the participants have passed, either via a "Passed cut value" or with "Adopt from course element". More about this under [Course element "Structure"](Course_Element_Structure.md#score).

## What the wizard creates {: #result}

The wizard appends a course element "Structure" to the end of the course and creates the checklists below it. Then [move](Deleting_Moving_and_Copying_Course_Elements.md) the course element "Structure" to the desired place in the course menu; the checklists move with it. You can then edit each checklist individually, for example its title or deadline. What the settings do and how you assess checklists is described under [Course element "Checklist"](Course_Element_Checklist.md). Participants see the new course elements as soon as you [publish](Using_additional_Course_Editor_Tools.md#publish) the course.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Course Element "Checklist" >](Course_Element_Checklist.md)<br>
[Members management >](../learningresources/Members_management.md)<br>
[Course elements in the Course editor >](General_Configuration_of_Course_Elements.md)<br>
[Course Element "Structure" >](Course_Element_Structure.md)<br>
[Deleting, Moving and Copying Course Elements >](Deleting_Moving_and_Copying_Course_Elements.md)<br>
[Course editor tools >](Using_additional_Course_Editor_Tools.md)

**Further reading**<br>
[Assessment of course modules >](../learningresources/Assessment_of_course_modules.md)<br>
[Wizard "Multiple HTML pages" >](Course_Element_Multiple_HTML_Pages.md)

[To the top of the page ^](#multiple_checklists)
