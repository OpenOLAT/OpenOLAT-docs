# Test settings - Administration {: #test_settings}

In the `Test > Administration` area you will find further menus, similar to other learning resources. Here you can configure the test in more detail. The "Settings" and "Edit content" menus are particularly important. Owners of the learning resource, learning resource managers and administrators see this area.

![Expanded Administration menu of a test learning resource with the entries Settings, Correction workflow, Generate handwritten exams and further administration functions.](assets/test_administration_menu_v1_en.png){ class="shadow lightbox" }

The basic configuration of the entire test is largely carried out in the **"Settings"**, particularly in the "Options" tab (see below).

The **"Member administration"** menu is particularly relevant if the test is to be used independently of the course, otherwise the member administration of the test participants is carried out via the linked course.

Under "Edit content" you access the test editor. This is where you create the actual test.

!!! note "Test editor QTI 2.1"
    Overview of the test editor.<br>
    [Edit content](Test_editor_QTI_2.1.md)

The **"Assessment tool"** of the test only appears if the test is to be used independently of the course: `Test > Administration > Settings > Tab "Share"`, purpose "Independent".

Correctors can be added for the test in the **"Correction workflow"** menu (see below). 

The **"Test statistics"** menu only appears for independent tests, otherwise the test statistics are displayed in the respective course menu.

The **"Offer types"** menu is only active if the test has been configured as bookable.

A wizard can be used to generate **"Handwritten exams"** based on the online test (see below). 

The tests can be copied or saved using the "Copy", "Export content" and "Export as Word document" menus.

**"Delete test"** deletes the test learning resource. It can then be found in the author area in the "Deleted" tab. 

On this page you will find more detailed explanations of the following administration menus of the learning resource Test:

* Settings
* Correction workflow
* Generate handwritten exams
* Export as Word document

[To the top of the page ^](#test_settings)

---

## "Settings" of a test {: #settings}

The "Options" tab is particularly important for tests. This is where you configure the entire test. 

![Administration menu of a test learning resource with the entry Settings selected: on the right the tabs Info, Metadata, Share, Catalog and Options appear, with Options active.](assets/Test_menu_settings_DE.png){ class="shadow lightbox" }

In addition, further settings for the learning resource can be made in the other tabs "Info", "Metadata", "Share" and "Catalog". Make sure that the license information under "Metadata" corresponds to your requirements.

### Tab Options [:octicons-tag-16:{ title="from Release 20.3.0 (OO-8321)" }](https://track.frentix.com/issue/OO-8321)

The following configurations can be made:

**Standard settings**

Here you can choose a preconfigured selection of typical settings for different test usage situations.

Decide, for example, whether it is a summative or formative test or use a different preset configuration. This makes it easier for inexperienced authors in particular to quickly find a suitable setting. However, later changes and individual adjustments are still possible.

![Standard settings field in the Options tab with the selection list "Choose a profile", "Summative (real test)" and "Formative (exercise test)" and the "Apply configuration" button.](assets/Test_Standardeinstellungen_DE.png){ class="shadow lightbox" }

**Limit number of test attempts**

Activate this option to limit the number of possible solution attempts for a test. Enter the desired number in the "Max. number of attempts" field. The value can be a maximum of 20.

**First passed solution attempt counts**

As soon as the result "passed" is achieved, participants cannot perform the test again.

**Allow anonymous users (guests) {: #guest}** 

People without an OpenOlat account can also take the test. However, guests cannot interrupt the test. Only completed tests are counted. The results are also available in the test statistics.

**Display module only, hide LMS**

This selection is made to prevent participants from accessing other OpenOlat functions during a test. OpenOlat is hidden and only displayed again once the test has been completed. 

**Show question title**

Select the checkbox to show participants the titles of the questions. If the titles are not to be displayed but the navigation is activated, an anonymized title will appear in the menu navigation.

**Display menu navigation**

If you _do not_ allow menu navigation:

* If "non-linear navigation" is set on the test, the navigation below the question can be called up via a button to select a different question.
* If "linear navigation" is set on the test, the next question appears automatically after submitting an answer and the respondent cannot navigate to other questions.

**Personal notes  {: #notes}**

You can allow participants to create personal notes during the test, which are no longer available after the test has been completed.

**Show number of questions and progress in the test**

Select the checkbox to show participants the number of questions.

**Display number of points and score in the test**

Select the checkbox to show participants their current score in the test history.

**Show max. points of the question** 

If the checkbox is marked, the maximum achievable points per question in the test are displayed. 

**Allow interruption**

Ticking the checkbox allows participants to interrupt the test. The previous answers are saved and participants can continue answering the questions at a later time.

**Allow to cancel**

By ticking the checkbox, you allow course participants to cancel the test without saving their answers.

**Create test receipt**

If this option is selected, a test receipt is created at the end of the test, which can be downloaded as an XML file. It is used to verify the test.

![Performance overview of a completed test: the highlighted "Test receipt" row contains the "Download" link with creation date, above it the number of attempts, score and status.](assets/Testquittung_DE.png){ class="shadow lightbox" }

If the "Create test receipt" option is selected, the option Send test receipt by email can also be activated. The XML file created is then also sent to the participant by email.

**Display feedback**

As long as this checkbox is selected, the feedback is displayed in the test history. If the checkbox is no longer selected, feedback is no longer displayed. This applies to the feedback for all question items and also the feedback that can be added at the test level. The individual feedbacks are configured in the test editor.

**Show results after test completion {: #results}**

If this checkbox is selected, the result is displayed after the test has been completed. What exactly is displayed can be selected.

* **Test summary**: The metadata of the entire test is displayed as a summary (incl. points and pass/fail).
* **Section summary**: The metadata of the section is displayed as a summary.
* **Question summary**: The metadata for each individual question is displayed.
* **Answer provided by the participant**: The question is displayed together with the participant's answer.
* **Solution**: The question is displayed together with the correct solution. If a correct solution is stored in the Feedback tab, it is also displayed in the results view with this option.

!!! note "Note"

    The settings made under Options are automatically adopted when the test is included in a [course](Tests_at_course_level.md) and, if desired, can be adapted in the respective course element Test in the course editor in the tabs "Test configuration" or "Options".

    Whether the results are displayed on the test start page in the course is also configured directly in the course.


## Correction workflow [:octicons-tag-16:{ title="from Release 15.0 (OO-4442)" }](https://track.frentix.com/issue/OO-4442) {: #correction-workflow}

To add additional correctors to a test, including correctors from other courses, you must enable correction under `Test > Administration > Correction workflow`. You can then add correctors, assign grading assignments and make further settings.


### Tab "Configuration"

Here the external correction is generally switched on. You can then define whether examinees are assessed anonymously or with a visible name. The correction period specifies the maximum time available to the corrector.

The respective correctors are automatically notified when new edits of the test are available. The notification can be sent either immediately after the test is completed or once a day. For this purpose, a suitable mail text can be stored or a template ("Choose language template") can be used. After the first mail notification, two reminder mails can be sent at user-defined intervals (days).

### Tab "Correctors"

![Tab "Correctors" in the Correction workflow menu with the tabs "Configuration" and "Grading assignments" and the "Add corrector" button.](assets/grading_workflow_tab_correctors_v1_de.png){ class="shadow lightbox" }

Here you add the persons who are to grade a test. It does not matter which role the person has in OpenOlat. Users can also be added as correctors. Via the row menu of a corrector, further actions are available, for example contacting, deactivating or removing the corrector as well as displaying their grading assignments.

### Tab "Grading assignments"

Here the processing status of the grading assignments of the different correctors can be displayed and filtered according to various criteria.

### Report / Excel export [:octicons-tag-16:{ title="from Release 21.0 (OO-9569)" }](https://track.frentix.com/issue/OO-9569)

Owners of the test learning resource and learning resource managers pull the report either here or across courses under `Coaching > Order management`. Correctors see their own assignments under `Coaching > Assessment orders` and do not download a report there.

In the "Correctors" tab, open the "Download report" entry in the row menu of a corrector. OpenOlat generates an Excel file with the state of that corrector's grading assignments. Before the download, you define the scope:

* With the "Only completed orders" switch, you limit the report to completed grading assignments.
* Using the predefined periods "Last month" and "Last year", or the "Close date" fields (from and to), you narrow down the period. At least one date must be specified.

![Download report dialog with the "Only completed orders" switch, the periods "Last month" and "Last year" and the mandatory "Close date" field.](assets/grading_report_export_dialog_v1_de.png){ class="shadow lightbox" }

In the "Grading assignments" tab, the "Report" button generates the same report for the grading assignments displayed there.

For each grading assignment, the report shows the status ("Unassigned", "Assigned", "Done"), the "Due date", the "Close date" and the "Missed deadline" flag.

The generated Excel file contains the worksheets "Graders", "Assignments" and "Archive". The "Archive" worksheet lists archived grading assignment entries whose assignment record has since been removed (for example because an examinee, a corrector or the test learning resource was deleted), including correction time and close date for remuneration. [:octicons-tag-16:{ title="from Release 21.0 (OO-6914)" }](https://track.frentix.com/issue/OO-6914)

![Excel report of the correction workflow in the "Archive" tab with the columns username, first name, last name, course, identifier, correction time and "Close date".](assets/grading_report_archive_v1_de.png){ class="shadow lightbox" }

!!! note "Coaching Tool"
    More information on cross-course correction.<br>
    [Coaching Tool](../area_modules/Coaching.md)

[To the top of the page ^](#test_settings)

---

## Generate handwritten exams {: #create_paper_pencil}

If you want to run a test offline, you can use this wizard to generate a cover sheet and different versions of your test resource with randomly selected answers.

1. In the options you select the language and the number of tests, as well as a prefix for the file names. You can also specify whether you want to generate a cover sheet or an additional sheet.

    ![Options step in the "Export exams" wizard: fields for number of tests, output language, serial number as prefix, and the choice of cover sheet and additional sheet.](assets/Test_offline_options_DE.png){ class="shadow lightbox" }

2. In the second step you choose the attributes that should be copied to the cover sheet. Some attributes, like the description of the test resource, are still customizable.

    ![Cover sheet attributes step in the "Export exams" wizard with the attribute groups General and Test parameters to choose from for the cover sheet.](assets/Test_offline_Deckblattattribute_DE.png){ class="shadow lightbox" }

3. Here you have the possibility to select and overwrite certain fields. The description field is copied over from the test resource and can be customized again here.

    ![Cover sheet fields step in the "Export exams" wizard: the "Title" and "Procedure" fields as well as the description field with HTML editor can be overwritten for the cover sheet.](assets/Test_offline_Deckblattfelder_DE.png){ class="shadow lightbox" }

4. If you activated the "Additional sheet" option in the "Options" step, the "Additional sheet" step appears here.

5. The summary contains an overview of all settings made and a preview of the tests to be generated. Please note that a large number of generations may take some time and the browser may not always respond.

    ![Summary step in the "Export exams" wizard with number of tests, file format, output language, serial number, and the "Preview" and "Preview with solutions" buttons.](assets/Test_offline_Zusammenfassung_DE.png){ class="shadow lightbox" }

[To the top of the page ^](#test_settings)

---

## Export as Word document {: #export_word}

The test is then downloaded in zip format with two Word files, one of which contains only the questions and the other also contains the solutions. The exported file contains all the important information about the test, including the score, so that you can use the document directly.

[To the top of the page ^](#test_settings)

---


## Further information {: #further_information}

**Further**<br>
[How do I proceed when creating a test? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.md)<br>
[How do I assess a test? >](../../manual_how-to/assessing_tests/assessing_tests.md)<br>
[How do you grade an anonymous test in OpenOlat? >](../../manual_how-to/assessing_tests_anonymously/assessing_tests_anonymously.md)<br>
[Assessment tool >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Coaching Tool >](../../manual_user/area_modules/Coaching.md)

[To the top of the page ^](#test_settings)
