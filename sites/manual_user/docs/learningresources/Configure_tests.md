# Configure tests

In the test editor, you structure a test and define how participants work on it: whether it can be passed, how much time they have, whether they jump between questions and whether they can view their answers afterwards. Each test consists of at least one section and one question. Therefore, when creating a new test, you will already find a section ("Section") and a single-choice question ("Single choice"). If there is no single-choice question in your test, you can delete the default single-choice question as soon as you have added another question.

You define all settings described here in the test editor: `Test > Administration > Test editor`. The test editor can be opened by owners of the test, administrators and learning resource managers.

The settings apply on three levels:

* on test level: Settings for the entire test
* on test part level: settings for a block of sections that participants work on and finish as a whole
* at section level: Settings for individual sections

The settings of the single questions are described on the page [Configure test questions](Configure_test_questions.md).

The test level is the top level. The test can contain several test parts, which in turn contain different sections. If a test contains only one test part, this test part can still contain several sections. Divide a test into several test parts if parts of the test are to follow different rules, see [Test part level](#testpart).

![Hierarchy of test, test part, section and question with the settings that apply on each level](assets/test_structure_levels_v1_en.svg){ class="shadow lightbox" title="Levels of a test · 2026.10.07" }

With sections, you structure your test. Often, for example, introductory questions come first, collected in a "General" section. Your test can consist of any number of sections, and sections can be nested inside each other.

If you want to add a new section or another test part, select `Add elements > Section` or `Test part` at the top in the dropdown menu. You can then assign specific questions to the section.

## Test level

At test level, you define the title that appears in the navigation, and the settings in the "Test configuration", "Feedback" and "Expert" tabs.

### Tab Test configuration

In the "Test configuration" tab, you define how many points the test awards, whether it can be passed and how much time participants have.

![Display passed / not passed with cut value and time limit](assets/test_editor_tab_test_configuration_v1_en.png){ class="shadow lightbox" title="Test configuration tab in the test editor" }

* **Max. score:** OpenOlat calculates this score automatically from the points of the single questions in the test.
* **Display passed / not passed:** Check the box if you want a "passed" or "not passed" to be displayed for the test.
* **Type of display:** If "Display passed / not passed" is activated, you define here how the result is determined: "Using cut value" or "Manually by coach". This setting and the cut value also apply when you embed the test in a course. Exception: if you activate the option "Levels/Grading" in the course element "Test", the rating scale converts the points reached into a grade or level, for example 0 to 100 points into Swiss grades from 1 to 6. The grade then decides whether the test is passed: with "Passed with", the rating scale defines from which grade the test is passed, for example from grade 4. The cut value of the test is not converted and no longer counts, see [Set up a test](Course_Element_Test/Test_Setup.md#section_test) and [Levels/Grading](Assessment_translate_points_in_grades.md).

    ![Passed in the course: without Levels/Grading the cut value of the test decides, with Levels/Grading the converted grade](assets/test_passed_decision_v1_en.svg){ class="shadow lightbox" title="Passed in the course with and without Levels/Grading" }
* **Passed cut value:** Enter the minimum score required to pass the test.
* **Time limit:** The time limit applies to the whole test, in hours and minutes. Above the test, participants see how much time they have left. Towards the end, OpenOlat highlights the display in color. A time limit for sections or single questions is not possible.

    As soon as the time is over, OpenOlat finishes the test automatically. In the course, the course element "Test" announces this before the start with "is pulled in automatically". Answers that participants have not yet submitted with "Submit answer" count as unanswered and give no points. No confirmation asks whether the answers should be saved. The feedback on the whole test and the review also fall under the time limit.

!!! note "Note"

    You set up a time limit either directly in the test editor, as described here, or after embedding the test into a course in the course element "Test":<br>
    `Course > Administration > Course editor > "Title of the course element" > Tab "Options"`<br>
    With "Use configuration of the learning resource", the time limit from the test editor applies there. With "Adjust configuration", the time limit of the course element applies; if none is activated there, the one of the test applies. If necessary, you extend the test time for single persons in the [assessment tool](Assessment_tool_overview/index.md).

### Tab Feedback

* **Feedback if required score for "Passed" is reached:** Enter a total feedback here if the score for passed is reached.
* **Feedback if required score for "Passed" is _not_ reached:** Enter a total feedback here if the score is not sufficient.

### Tab Expert {: #expert} [:octicons-tag-16:{ title="from Release 20.3.0 (OO-8321)" }](https://track.frentix.com/issue/OO-8321)

In the "Expert" tab, you define how participants move through the questions, how often they may take the test and whether they can view their answers after the test. If the test has at least two test parts, the same settings are in the "Test part" form of the respective test part, and the test level has no "Expert" tab, see [Test part level](#testpart).

![All settings of the Expert tab at a glance, among them Limit number of attempts with a maximum of 2 attempts and Allow personal notes](assets/test_editor_tab_expert_v2_en.png){ class="shadow lightbox" title="Expert tab in the test editor · 2026.11.10" }

* **Navigation mode:**

    * Linear: Participants answer all questions in order and do not jump back and forth between the questions.
    * Non linear: Participants answer the questions in the order they choose themselves.

* **Limit number of attempts:** Define here how often participants may submit their answer to a question. With "Yes", enter the number under "Max. number of attempts". The limit applies to each question separately, not to the test run: each submission with "Submit answer" counts as one attempt, and below the question participants see, for example, "Still 1 attempt (1/2)". Once all attempts are used up, the answer to this question can no longer be changed. In a new test run, the count starts again. You limit the number of attempts for the whole test in the course element "Test" or in the settings of the test: `Test > Administration > Settings > Tab "Options"`.

    If the number of attempts is limited on the level of the test or test part, this configuration is inherited to all sections and questions below.

* **Allow skipping questions:** If this check box is selected, the test can be finished before all questions are answered.

* **Allow personal notes:** Participants can take personal notes, which are not available after the test anymore and are not assessed. This feature can only be selected if "Personal notes" is selected in the settings of the test: `Test > Administration > Settings > Tab "Options"`.

* **Allow review of questions:** After finishing the test, participants can view the test and their answers again, but can no longer correct them.

* **Show solution:** In the review the solutions are shown additionally. This feature is only possible, if "Allow review of questions" is selected.

## Test part level {: #testpart}

If parts of a test are to follow different rules, for example a mandatory part without going back before a part that can be worked on freely, divide the test into test parts. A test part is the top level of structure of a test. It bundles sections and sets for all of them together how participants move through the questions ("Navigation mode": "Linear" or "Non linear") and which settings of the "Expert" tab apply.

Participants work on the test parts one after the other. Finishing a test part submits it: OpenOlat saves the answers, and the test part can no longer be opened afterwards. This is the reason for dividing a test, and at the same time what you take into account when planning.

An example: test part 1 contains basic questions with "Navigation mode" "Linear" and a limited number of attempts, participants solve the questions in order. Test part 2 contains questions with "Navigation mode" "Non linear", whose order participants choose themselves. Anyone who enters test part 2 can no longer change the answers from test part 1.

In the test editor, the following rules apply to test parts:

* Every new test contains one test part. As long as there is only one, it does not appear in the menu of the test editor, and its settings are in the "Expert" tab of the test level.
* `Add elements > Test part` creates another test part at the end of the test, with an empty section "Section". A new test part starts with "Navigation mode" "Non linear", "Allow skipping questions" and "Allow personal notes" set to "Yes" and "Allow review of questions" set to "No".
* From two test parts onwards, each test part appears as a separate entry in the menu, for example "1. Test part" and "2. Test part". Clicking on it opens the "Test part" form with "Navigation mode" and the settings of the "Expert" tab: "Limit number of attempts" with "Max. number of attempts", "Allow skipping questions", "Allow personal notes", "Allow review of questions" and "Show solution". The test level then has no "Expert" tab.
* "Delete" only appears for a test part when the test has at least two test parts. After the confirmation "Do you really want to delete the test part along with all its questions?", OpenOlat removes the test part with all its questions.
* A test part always contains at least one section. The last section cannot be deleted, OpenOlat reports "The section cannot be deleted. A test or a test part must contain at least one section."
* As soon as the test has been carried out, the test editor shows "The resource is already used for assessment purposes. Editing is limited." All settings of the test parts are then locked, "Delete" and "Add elements" are missing.

![Two test parts in the menu of the test editor, on the right the Test part form of the second test part with navigation mode and the settings of the Expert tab](assets/test_editor_testpart_v1_en.png){ class="shadow lightbox" title="Test part form in the test editor · 2026.10.07" }

The settings of a test part also control what participants experience when finishing:

* With "Navigation mode" "Linear" without "Allow skipping questions", the "Finish test part" button only appears when all questions of the test part have been answered. With "Allow skipping questions", it is available from the first question.
* With "Allow review of questions", OpenOlat shows the page "Test part complete" after finishing, on which participants can view their answers but no longer change them. Without review, participants go directly to the next test part.

!!! warning "In a linear test part, «Next question» only moves forward"

    If a test part with "Navigation mode" "Linear" allows skipping questions, "Next question" and "Finish test part" are shown next to each other. "Next question" without an answer leaves the question unanswered, and participants can no longer reach it in this test part. On the last question, "Next question" finishes the test part without confirmation. Inform your participants about this before the test.

A time limit exists only for the whole test ("Test configuration" tab), not per test part.

!!! info "Important"

    A test from a tool other than OpenOlat can bring several test parts with it when imported. For such a test, the test editor reports "This test cannot be processed with the OpenOlat editor." In the "Test part" form, only "Navigation mode" can be changed, the other settings are locked. The questions open in the "Unknown" tab, with "Convert" you change a question into a question type of the test editor. A test that you exported from OpenOlat and imported again remains fully editable.

What participants see while taking the test is described on the page [Course element "Test"](Course_Element_Test/index.md#participate_as_learner).

## Section level {: #section}

You assign one or more sections to a test part. In the test, participants see nested sections with a description one below the other and show and hide them individually. Sections can also appear in random order. If a test contains only one test part, all sections are listed in the menu of the test editor directly below the test.

In the "Section" tab, you enter a description of the section and define with "Number of questions in this section" whether all questions of the section appear or only a selection. With "Random order of questions or sections?" you define whether the questions or the subordinate sections appear in random order.

In the "Expert" tab of a section, you override the settings of the "Expert" tab of the test or test part level. This way, a single section behaves differently from the rest of the test.

If "Section's title visible in test" is activated in the "Expert" tab of the section, OpenOlat also displays the section description in the following places:

* In the test, when a question belonging to the section is called. Participants can show or hide the section description.
* In the test results.
* In the [correction workflow](Test_correction_workflow.md), in which correctors assess the answers, for the questions belonging to this section.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Configure test questions >](Configure_test_questions.md)<br>
[Set up a test >](Course_Element_Test/Test_Setup.md)<br>
[Levels/Grading >](Assessment_translate_points_in_grades.md)<br>
[Assessment tool - overview >](Assessment_tool_overview/index.md)<br>
[Course Element "Test" >](Course_Element_Test/index.md)<br>
[Test: Correction workflow >](Test_correction_workflow.md)

**Further reading**<br>
[Test editor >](Test_editor_QTI_2.1/index.md)<br>
[Test: Settings >](Test_settings.md)

[To the top of the page ^](#configure-tests)
