# Coaching - Assessment Orders {: #assessment_orders}

![Marked entry Assessment orders under Tasks leads to the open reviews, levels/gradings and grading assignments, on the Coaching start page.](assets/coaching_assessment_orders1_v1_de.png){ class="shadow lightbox" }


Here you can see where specific coaching actions such as assessments or gradings still need to be carried out, or whether they still need to be released.

Depending on your role, in addition to your own assessment orders, the others are also displayed and you can get an overview.

![List with username, name, coach, course name, course element, last update and the Assess link, in the tab Open reviews.](assets/coaching_assessment_orders_open_assessments_v1_de.png){ class="shadow lightbox" }

---

### Assessment, correction and levels/grading {: #assessment_terms}

Three terms appear on this page. They refer to different things:

* **Assessment**: the result of a person at an assessable course element, that is status, points, "Passed" and, if applicable, the grade. A test also has an assessment. You edit it in the [assessment form](../learningresources/The_assessment_form.md) or in the [assessment tool](../learningresources/Assessment_tool_overview.md) of the course.
* **Correction**: reviewing a submission by hand where OpenOlat does not evaluate it itself, for example with essay questions in a test. The correction is a step on the way to the assessment: in a test, the correcting person awards the points, and the assessment results from them. Coaches correct a test in the [correction tool](../learningresources/Assessing_tests.md), correctors via "Grade" in their grading assignment.
* **Levels/Grading**: the conversion of the points into a grade according to a grading scale. Without levels/grading, the assessment consists of points and, if applicable, "Passed". With [Levels/Grading](../learningresources/Assessment_translate_points_in_grades.md), the grade is added, and the grading system determines whether the score counts as passed.

[To the top of the page ^](#assessment_orders)

---

### Creating assessment orders {: #create_assessment_orders}

Course owners create assessment orders at the course element: they set it to manual assessment. As soon as a participant then completes their work, OpenOlat creates the assessment order and shows it in the matching tab. Coaches and correctors work on the open orders from all their courses under `Coaching > Assessment orders`.

Whoever works on an order usually does not set it up. Coaches without ownership only reach the course editor if they have been granted the "Course editor" right in the [Rights area of the members management](../learningresources/Members_management.md#section_rights). The owners of the test set up the correction workflow, correctors only work on the orders that are assigned to them.

The four tabs are not four kinds of orders. The first three show the assessment of a person at different points of its process: to be assessed, grade to be assigned, to be released. The fourth tab shows the grading assignments: test submissions that a corrector entered in the correction workflow corrects. The correction workflow only exists for tests. Other course elements, for example a task, therefore do not create grading assignments.

The tabs "Open reviews", "Open levels/gradings" and "Reviews to release" are seen by course owners for all participants of the course, and by coaches for the people they coach. The tab "Grading assignments" is seen by the people who are entered as correctors in the correction workflow.

![Four settings lead to the four tabs, plus two further ways to an order.](assets/coaching_assessment_orders_create_v1_en.svg){ class="shadow lightbox" }

The pages on which owners make the respective setting:

* **Open reviews**: [Tests at course level](../learningresources/Tests_at_course_level.md#correction), [Course Element "Task"](../learningresources/Course_Element_Task.md), [Course Element "Assessment"](../learningresources/Course_Element_Assessment.md)
* **Open levels/gradings**: [Levels/Grading](../learningresources/Assessment_translate_points_in_grades.md)
* **Reviews to release**: [Tests at course level](../learningresources/Tests_at_course_level.md#correction), [Course settings, section Assessment rights](../learningresources/Course_Settings_Assessment.md#section_assessment_rights)
* **Grading assignments**: [Test settings](../learningresources/Test_settings.md#correction-workflow)

The course element must be assessable and set to manual assessment, which means points or "Passed" are set at the course element. If the correction of a test is set to "Automatic", OpenOlat evaluates the test itself and releases the result immediately; the same applies to the assignment "Automatically on score change" for levels and grading.

Two further ways lead to an assessment order:

* **Reopen assessment**: With the button "Reopen assessment" in the [assessment form](../learningresources/The_assessment_form.md) the status returns to "To review". The row then appears again in the tab "Open reviews".
* **Assignment coaches/participants**: In the [Course Element "Task"](../learningresources/Course_Element_Task.md#coach_assignment_table) course owners assign a coach to each participant. That person is notified and finds their orders via the filter "Assigned to me".

[To the top of the page ^](#assessment_orders)

---

### Tab Open reviews [:octicons-tag-16:{ title="from Release 16.1 (OO-5851)" }](https://track.frentix.com/issue/OO-5851) {: #tab_open_assessments}

Here you have access to all course elements that still need to be assessed. These can be sorted according to the columns and then selected and assessed individually. Clicking on the "Assess" link takes you to the corresponding assessment form.

A row appears as soon as the assessment entry of the participant is in the status "To review". This status is created by the manual correction of a [test](../learningresources/Tests_at_course_level.md#correction), by the steps "Review", "Correction", "Peer review" and "Grading" in the course element [Task](../learningresources/Course_Element_Task.md), and by the switch "Set status To review if accessible" in the course element [Assessment](../learningresources/Course_Element_Assessment.md). Coaches see these steps in the column "Step" when they open the task in the course.

With the filter "Assigned to me" you limit the list to the orders that are assigned to you personally.

[To the top of the page ^](#assessment_orders)

---

### Tab Open levels/gradings [:octicons-tag-16:{ title="from Release 16.2 (OO-6009)" }](https://track.frentix.com/issue/OO-6009) {: #tab_open_classifications_scores}

Here you find all course elements that have already been assessed but for which the manual assignment to a grading scale or grading system has not yet been completed.

A row appears if "Levels/Grading" is switched on at the course element and the "Assignment" is set to "Manually by coach", the points are set and the grade is still pending. Course owners set both in the course editor at the course element, for a test in the tab "Test configuration", otherwise in the tab "Assessment". In addition, the module [Levels/Grading](../learningresources/Assessment_translate_points_in_grades.md) and a stored grading scale are required.

Coaches without ownership see the row and assign the grade as long as the option "assign Levels/Grading" is switched on. The option is switched on by default. In learning path courses, course owners switch it off or on under `Course > Administration > Settings > Tab "Assessment"` in the [section Assessment rights](../learningresources/Course_Settings_Assessment.md#section_assessment_rights). Conventional courses do not have this section; there, coaches can always assign the grade.

[To the top of the page ^](#assessment_orders)

---

### Tab Reviews to release {: #tab_assessments_to_be_released}

Here you find all assessments that are not yet visible to the participants and still need to be released.

In this tab, it is also possible to select all course elements and release them all at once.

For a test, the field "Release assessment" in the [section Correction](../learningresources/Tests_at_course_level.md#correction) controls whether OpenOlat releases the assessment itself once the correction is completed. For all other manually assessed course elements, the course option "release assessment" decides. The same option gives coaches without ownership access to this tab. It is switched on by default. In learning path courses, course owners switch it off or on in the [section Assessment rights](../learningresources/Course_Settings_Assessment.md#section_assessment_rights); conventional courses do not have this section.

[To the top of the page ^](#assessment_orders)

---


### Tab Grading assignments [:octicons-tag-16:{ title="from Release 15.0 (OO-4442)" }](https://track.frentix.com/issue/OO-4442) {: #tab_grading_assignments}

This tab only appears if you have been entered as a corrector for a test. You see an overview of the tests in the different courses that you still have to check and correct manually. Depending on the setting in the learning resource "Test", the assessment is anonymous or not.

If you are neither coach nor owner of a learning resource, the other tabs are missing; the heading "My grading assignments" with your list then appears directly under the title "Assessment orders". If, on the other hand, you manage the correction workflow yourself, as owner of a test learning resource with correction workflow, as learning resource manager or as administrator, this tab is missing; you then find your assignments under `Coaching > Order management` in the tab [Grading assignments](Coaching_Order_Management.md#tab_grading_assignments).

![Filters for Taxonomy, Course, Test, Corrector, State, Grading period, Score and Passed, below them the list with Deadline, Course, Course element and the Grade link, in the tab Grading assignments.](assets/coaching_assessment_orders_grading_assignments_v1_en.png){ class="shadow lightbox" }

In the example, the correction is set to anonymous. That is why the "First name" and "Last name" columns only show a dash. The owners of the test make this setting in the learning resource under `Test > Administration > Correction workflow > Tab "Configuration"`.

The "Grade" link takes you directly to the test to be corrected, where you make the manual assessments. You can overwrite automatic assessments. Leave a comment when you do so.

#### Who sets up a grading assignment {: #create_grading_assignment}

A grading assignment is created in five steps. Three roles set it up, the submission of a participant triggers it. It reaches the corrector as soon as all five steps have taken place.

![Five steps from the module to the grading assignment, plus the assignment in the order management.](assets/coaching_assessment_orders_grading_chain_v1_en.svg){ class="shadow lightbox" }

1. Administrators switch on the correction workflow in the system administration: `Administration > e-Assessment > Test`.
2. Owners of the test switch on the correction workflow in the learning resource Test: `Test > Administration > Correction workflow > Tab "Configuration"`.
3. Owners of the test enter the correcting people in the tab "Correctors". Their role in OpenOlat does not matter.
4. Course owners set the correction at the course element Test to "Manual by graders". This option becomes available as soon as step 2 is set. More about this on the page [Tests at course level](../learningresources/Tests_at_course_level.md#correction).
5. A participant completes the test.

If no corrector is available at that moment, the assignment carries the status "Unassigned" and waits in the [Order management](Coaching_Order_Management.md). There, owners of the test, learning resource managers or administrators assign it to a person. The assignment then appears in that person's list.

For essay questions, you download a person's answer as a PDF with the "Download as PDF" button at the top right. The PDF contains information about the course, course element and test in the header. With anonymous correction, the "Participant identifier" appears instead of the personal details. You download all answers to a question at once in the [correction tool of the course](../learningresources/Assessing_tests.md).

!!! tip "Prerequisite"

    The download requires a [PDF service](../../manual_admin/administration/External_Tools_-_Administration.md#pdf_generator) configured in the system administration.

The management of all correctors and their assignments, on the other hand, is done in the [Order management](Coaching_Order_Management.md).

[To the top of the page ^](#assessment_orders)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[The assessment form >](../../manual_user/learningresources/The_assessment_form.md)<br>
[Assessment tool - Overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Assessing tests >](../../manual_user/learningresources/Assessing_tests.md)<br>
[Levels/Grading >](../../manual_user/learningresources/Assessment_translate_points_in_grades.md)<br>
[Tests at course level >](../../manual_user/learningresources/Tests_at_course_level.md)<br>
[Course Element "Task" >](../../manual_user/learningresources/Course_Element_Task.md)<br>
[Course Element "Assessment" >](../../manual_user/learningresources/Course_Element_Assessment.md)<br>
[Course Settings - Tab Assessment >](../../manual_user/learningresources/Course_Settings_Assessment.md)<br>
[Test settings - Administration >](../../manual_user/learningresources/Test_settings.md)<br>
[Coaching: Order management >](../../manual_user/area_modules/Coaching_Order_Management.md)<br>
[External Tools: Overview >](../../manual_admin/administration/External_Tools_-_Administration.md)

**Further reading**<br>
[Coaching: User search >](../../manual_user/area_modules/Coaching_User_Search.md)<br>
[Coaching: People >](../../manual_user/area_modules/Coaching_People.md)<br>
[Coaching: Courses >](../../manual_user/area_modules/Coaching_Courses.md)<br>
[Coaching: Educational products >](../../manual_user/area_modules/Coaching_Educational_Products.md)<br>
[Coaching: Events / Absences >](../../manual_user/area_modules/Coaching_Events_Absences.md)<br>
[Coaching: Reports >](../../manual_user/area_modules/Coaching_Reports.md)<br>
[Coaching: Groups >](../../manual_user/area_modules/Coaching_Groups.md)<br>
[Roles >](../../manual_user/basic_concepts/Roles.md)

[To the top of the page ^](#assessment_orders)
