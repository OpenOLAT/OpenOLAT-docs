# Course elements at a glance {: #course_elements}

:octicons-device-camera-video-24: **Video Introduction (German)**: [What are course elements?](<https://www.youtube.com/embed/JM6iSrfkHog>){:target="_blank"}

:octicons-device-camera-video-24: **Video Introduction (German)**: [Configuring course elements](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}

You build your course from course elements. With them, you provide and structure content, promote collaboration and exchange, check the participants' level of knowledge and handle organizational matters.

In the course editor, OpenOlat organizes the course elements into five groups. You see the groups in the dialog "Insert course elements":<br>
`Course > Administration > Course editor > Insert course elements`

![All course elements that can be inserted into a course, sorted into groups, plus the entries Multiple checklists and Multiple HTML pages](assets/course_elements_index_V1_en.png){ class="shadow lightbox" title="Dialog Insert course elements in the course editor" }

The manual organizes the course elements into the same groups. Each group has its own page with all course elements of the group:

Group | Purpose
---------|----------
[Knowledge transfer](Knowledge_Transfer/index.md) | Provide course content and structure the course, also with content created outside OpenOlat.
[Assessment](Assessment/index.md) | Check the participants' level of knowledge, assess their work and survey them.
[Communication and collaboration](Communication_and_Collaboration/index.md) | Exchange and collaboration in the course, also live in virtual classrooms.
[Administration and Organisation](Administration_and_Organisation/index.md) | Enrolment in groups, the assignment of topics and appointments as well as information and emails to the participants.
[Other](Other/index.md) | Own and external web pages, external learning applications via LTI (Learning Tools Interoperability), link lists, topic assignment and selection.

## General information on course elements

All course elements have the tabs "Title and description" and "Layout". Further tabs depend on the course type: course elements in learning path courses have the tab "Learning path", course elements in conventional courses the tabs "Visibility" and "Access".

In addition to the course elements, you design courses with further tools and learning resources. They are described in the respective chapters.

## Performance assessment {: #performance_assessment}

You can use many course elements for summative or formative assessment or for progress control. You view and edit the assessments of the assessable course elements in the [assessment tool](../Assessment_tool_overview/index.md). The page of the respective course element describes all settings:

* [Task](../Course_Element_Task/index.md) (manual assessment)
* [Group task](../Course_Element_Grouptask.md) (manual assessment)
* [Portfolio task](../Course_Element_Portfolio_Task.md) (manual assessment)
* [Check list](../Course_Element_Checklist.md) (manual & automatic assessment)
* [Assessment](../Course_Element_Assessment.md) (manual assessment)
* [LTI](../Course_Element_LTI_Page.md) (automatic assessment, transferred from LTI page)
* [SCORM](../Course_Element_SCORM_Learning_Content.md) (automatic assessment, transferred from SCORM module)
* [Test](../Course_Element_Test/index.md) (automatic & manual assessment)
* [Video task](../Course_Element_Video_Task.md#tab_assessment) (automatic & manual assessment, only in the mode "Test: Identify situations")

[Learning path courses](../Learning_path_course/index.md) control the progress with the completion criterion, which you set in the course editor for each course element in the tab "Learning path". With the criterion "Confirmation by participant", the participants confirm the completion themselves with the toggle button "Mark as done".

![Toggle button Mark as done next to the arrow navigation](../assets/learning_path_mark_as_done_v1_en.png){ class="shadow lightbox" title="Course toolbar in the participant view of a learning path course · 2026.11.03" }

An overview of all criteria can be found on the page [Learning path course - Course editor](../Learning_path_course_Course_editor.md#completion_criterion).

### Highscore [:octicons-tag-16:{ title="from Release 11.3 (OO-2133)" }](https://track.frentix.com/issue/OO-2133) {: #highscore}

If you award points in a course element, you can show the participants a highscore. The highscore makes a playful comparison possible and can motivate the participants.

You set up the highscore in the tab "HighScore". All assessable course elements have this tab except Practice and Video task, and in addition the course element "Structure". The prerequisite is that the course element awards points, for example a test, a task or an assessment.

First switch on "Show Highscore". Under "Starting Date (optional)" you define from when OpenOlat shows the highscore. Without a starting date, OpenOlat shows the highscore as soon as the assessment of the person is released: for a test directly after finishing it, for the course element "Assessment" only when coaches complete and release the assessment. Points that are only saved temporarily are not enough. With "Anonymize usernames" the highscore shows the persons anonymised instead of with first and last name.

Then you choose which elements the highscore shows: "Congratulations title", "Podium", "Histogram" and "Top results listing". For the listing you define whether it shows all participants or only a certain number of the top participants. At least one of these options must be selected.

![Congratulations title with your own position, podium with three ranks, histogram of the score distribution and top results listing](../assets/course_elements_highscore_v1_en.png){ class="shadow lightbox" title="Highscore of a course element from the participants' view · 2026.11.02" }

## Read-only assessment configuration [:octicons-tag-16:{ title="from Release 21.1 (OO-9647)" }](https://track.frentix.com/issue/OO-9647){:target="_blank"} {: #assessment_config_read_only}

As soon as assessments exist for an assessable course element, OpenOlat displays the settings that change the assessment result as read-only in the course editor. A lock symbol in front of the label shows which settings these are. The other settings in the same tab remain editable.

The reason: every change to the assessment rules triggers a recalculation of all existing assessments when you publish. The recalculation cannot be undone. The read-only mode makes sure that you trigger this intervention deliberately.

An assessment counts as existing as soon as at least one person has a score, a passed status or a grade for this course element. A status alone is not enough: if a person has only started the course element, the configuration remains editable. The check applies per course element. Assessments in another course element of the course do not trigger the read-only mode.

The read-only mode applies in learning path courses and in conventional courses. The course elements "Self-test" and "Questionnaire" do not have it.

### Editing read-only settings {: #enable_edit_mode}

In the read-only state, the message below the legend "Grading configuration" reads: "**Assessments already exist**, certain settings are displayed as **read-only**. To make changes, you must enable edit mode - when changes are made, all existing assessments will be recalculated."

![Message with the button "Enable edit mode" below "Grading configuration", a lock in front of every read-only setting, "Assessment form" without lock](../assets/assessment_read_only_info_v1_en.png){ class="shadow lightbox" title="Tab Configuration of a checklist with existing assessments · 2026.11.02" }

The message contains the button "Enable edit mode" with the symbol of an open lock. After the click, the read-only settings are editable, and in place of the message the warning appears: "You are currently editing the assessment configuration, even though assessments already exist. Saving and publishing your changes will cause all existing assessments to be **recalculated**. This action **cannot be undone**."

![Warning about the recalculation in place of the message, the settings under "Grading configuration" without lock and editable](../assets/assessment_read_only_warning_v1_en.png){ class="shadow lightbox" title="Tab Configuration of a checklist in edit mode · 2026.11.02" }

If no assessments exist yet, neither message nor warning appears. The tab is then directly editable.

The edit mode only applies while you are editing the course element in the course editor. If you open the course element in the course editor again later, the read-only mode is active again. There is no setting that lifts the read-only mode permanently.

### Affected course elements {: #read_only_course_elements}

The assessable course elements structure their assessment rules in the same way: at the top, below the legend "Grading configuration", are the message and the settings covered by the read-only mode. Below that, under "Assessment form", are the settings "Individual comment" and "Individual assessment documents", which remain editable. The table shows in which tab you encounter the read-only mode and what it covers.

Course element | Tab | Read-only | Remains editable
---------|----------|----------|----------
[Test](../Course_Element_Test/Test_Setup.md#tab_configuration) | "Test configuration" | "Levels/Grading" including the grading scale, "Include in course assessment" | all other settings, for example "Set assessment period", "Correction" and "Report"
[SCORM 1.2](../Course_Element_SCORM_Learning_Content.md#editor_tab_learning_content) | "Learning content" | the settings under "Grading configuration", for example "Transfer score from SCORM", "Maximum score", "Score needed to pass" and "Include in course assessment" | "Prevent the score from decreasing on subsequent attempts", "Count attempts only if score is transferred", "Maximum number of attempts", the areas "SCORM" and "Settings"
[Task](../Course_Element_Task/Task_Setup.md#grading) | "Grading" | "Rubric assessment", score, levels/grading, passed/failed, "Include in course assessment" | "Assessment form"
[Group task](../Course_Element_Grouptask.md#tab_assessment) | "Grading" | score, levels/grading, passed/failed, "Include in course assessment" | "Assessment form"
[Video task](../Course_Element_Video_Task.md#tab_assessment) | "Assessment" | all settings under "Grading configuration", among them score, levels/grading, passed/failed, "Include in course assessment" | "Assessment form"
[Portfolio task](../Course_Element_Portfolio_Task.md#tab_assessment) | "Assessment" | score, levels/grading, passed/failed, "Include in course assessment" | "Assessment form"
[Assessment](../Course_Element_Assessment.md#tab_assessment) | "Assessment" | "Rubric assessment", "Score granted", "Levels/Grading", "Display passed / not passed", "Include in course assessment" | "Set status "To review" if accessible", "Assessment form"
[Check list](../Course_Element_Checklist.md#tab_configuration) | "Configuration" | score, levels/grading, passed/failed including "Type of display" and thresholds, "Include in course assessment" | "Checklist configuration" with the deadline, "Assessment form"
[Structure](../Course_Element_Structure.md#score), only in the conventional course | "Score" | the whole legend "Combined assessment" | none

Settings that are not editable anyway remain so in the edit mode, for example "Minimum score" for the video task.

## Further information {: #further_information}

**Further reading**<br>
[Course elements in the Course editor >](../General_Configuration_of_Course_Elements.md)<br>
[Deleting, Moving and Copying Course Elements >](../Deleting_Moving_and_Copying_Course_Elements.md)<br>
[Course editor tools >](../Using_additional_Course_Editor_Tools.md)

**youtube**<br>
[What are course elements?](<https://www.youtube.com/embed/JM6iSrfkHog>)<br>
[Configuring course elements](<https://www.youtube.com/embed/SAkzzoOQEoQ>)

[To the top of the page ^](#course_elements)
