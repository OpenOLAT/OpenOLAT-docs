# Configure tests

Further structuring and configuration options are available for the OpenOlat tests. In principle, each test consists of at least one section and one question. Therefore, when creating a new test, you will already find a section ("Section") and a single-choice question ("Single choice"). If there is no single-choice question in your test, you can delete the default single-choice question as soon as you have added another question.

You make all settings described here in the test editor: `Test > Administration > Test editor`. The test editor can be opened by owners of the test, administrators and learning resource managers.

Settings for tests can be made on three levels:

* on test level: Settings for the entire test
* on part level: settings for areas with questions and sections
* at section level: Settings for individual sections

The test level is the top level. The test can then contain several parts, which in turn contain different sections. If a test contains only one part, this part can still contain several sections.

**Sections** are used to structure your test. Often, for example, introductory questions are asked first and a "General" section is created. Your test can consist of any number of sections. It is possible to nest several sections among each other.

If you want to add a new section or another part, select `Add elements > Section` or `Test part` at the top in the dropdown menu. You can then assign specific questions to the section.

In the following, the setting options on the three levels are explained:

## Test level

At test level, you define the title that appears in the navigation. The following configurations can also be selected:

![Set test title and cut value, Test configuration tab of the top level in the test editor](assets/test_configuration.png){ class="shadow lightbox" }

### Tab Test configuration

* **Max. score:** This score is calculated automatically out of the single questions of the test.
* **Display passed / not passed:** Check the box if you want a "passed" or "not passed" to be displayed for the test.
* **Type of display:** If "Display passed / not passed" is activated, you define here how the result is determined: "Using cut value" or "Manually by coach". This setting and the cut value also apply when you embed the test in a course. Exception: if you activate the option "Levels/Grading" there, the rating scale converts the points reached into a grade or level, for example 0 to 100 points into Swiss grades from 1 to 6. The grade then decides whether the test is passed: with "Passed with", the rating scale defines from which grade the test is passed, for example from grade 4. The cut value of the test is not converted and no longer counts, see [Course element "Test"](Course_Element_Test.md#section_test) and [Levels/Grading](Assessment_translate_points_in_grades.md).

    ![Passed in the course: without Levels/Grading the cut value of the test decides, with Levels/Grading the converted grade](assets/test_passed_decision_v1_en.svg){ class="shadow lightbox" }
* **Passed cut value:** Enter the minimum score required to pass the test.
* **Time limit:** The time limit can be defined for the whole test. Hours and minutes can be defined. Participants see above the test how much time is still available. The color highlighting also indicates that the end of the test is approaching. A time limit for sections or single questions is not possible.

    As soon as the time is over, the test is pulled. Questions which have not been submitted yet will be treated as empty, not answered questions and don't give a score. It is not asked, if the questions should be saved or not. The feedback over the whole test and the review are also part of the time limit.

!!! note "Note"

    A time limit of the test can either be done in the test editor as described here or after embedding the test into the course in the course editor in the tab `Options`. If necessary the test time can be extended for single users in the [assessment tool](../learningresources/Assessment_tool_overview.md).

### Tab Feedback

* **Feedback for all correct answers:** Enter a total feedback here if the score for passed is reached.
* **Feedback for wrong answer:** Enter a total feedback here if the score is not sufficient.

### Tab Expert {: #expert} [:octicons-tag-16:{ title="from Release 20.3.0 (OO-8321)" }](https://track.frentix.com/issue/OO-8321)

In the tab expert (or on the level of the part, as far as a part has been added), the following configurations can be done:

![Set navigation, number of attempts, skipping, personal notes, review and solution, Expert tab in the test editor](assets/expert.jpg){ class="shadow lightbox" }

* **Navigation mode:**

    * Linear: All questions need to be solved after each other. It cannot be jumped in between the menu.
    * Non linear: The questions can be answered in the desired order.

* **Limit number of attempts:** If only a certain number of attempts is allowed, it can be defined here. This limitation is only valid for the test part. If the number of attempts should be limited for the whole test, it needs to be limited in the options or in the course element test. If a test contains only one test part, the setting also applies to the entire test.

    If the number of attempts is limited on the level of the test or part, this configuration is inherited to all sections and questions below.

* **Allow skipping questions:** If this check box is selected, the test can be finished before all questions are answered.

* **Allow personal notes:** Participants can take personal notes, which are not available after the test anymore and are not assessed. This feature can only be selected, if "Personal notes" is selected in Options.

* **Allow review of questions:** After finishing the test, the test and its answers can be shown again, but no corrections are possible.

* **Show solution:** In the review the solutions are shown additionally. This feature is only possible, if "Allow review of questions" is selected.

## Part level

At the Part level, it is practically the same as at the Test level. Each created test consists of one part. However, this is not shown. The parts are only visible when another part is added and the test consists of at least two parts.

As soon as two or more parts exist, the configurations are defined mainly at the level of the parts and no longer at the level of the test. For example, an area in which questions can be skipped and one in which all questions must be answered, or an area with restricted solutions and an area without restrictions.

## Section level {: #section}

Several sections can be subordinated to a test part. Several nested sections with descriptions are displayed one below the other and can be shown and hidden separately and also displayed in random order. If only one test part exists for a test, all sections appear at the top level.

In the tab **"Section"** a description for the section can be entered and it can be defined whether all or only a selection of the questions of the section should appear. Furthermore, the type of order, random or linear, can be defined.

The "Expert" tab of the Test or Part level can be overwritten and changed again at section level. This allows to configure a different behavior for single sections compared to the rest of the test.

If the visibility of the section title in the "Expert" tab is activated, the respective section description is also displayed in the following places in OpenOlat:

* In the test, when a question belonging to the section is called. Participants can show or hide the section description.
* In the test results.
* In the correction workflow for the questions belonging to this section.

## Further information {: #further_information}

[Course Element "Test" >](Course_Element_Test.md)<br>
[Levels/Grading >](Assessment_translate_points_in_grades.md)<br>
[Assessment tool - overview >](Assessment_tool_overview.md)<br>
[Test editor >](Test_editor_QTI_2.1.md)<br>
[Test settings - Administration >](Test_settings.md)

[To the top of the page ^](#configure-tests)
