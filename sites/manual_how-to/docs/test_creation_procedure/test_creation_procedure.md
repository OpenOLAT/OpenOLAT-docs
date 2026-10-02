# How do I proceed when I create a test? {: #test_creation_procedure}

??? abstract "Objectives and content of this instruction"

    There are various ways to create tests in OpenOlat. Here you will find an overview of the most common ways. Get to know the possibilities and then choose the procedure that suits you best.

    All three ways require the role Author. With this role, the main navigation shows Authoring and the question bank.

??? abstract "Target group"

    [x] Beginners [x] Advanced users  [ ] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)


---

## The interaction of the components

![Course element of type Test containing the learning resource Test, whose questions are exchanged with the question bank](assets/kurs-kursbaustein-lernressource-frage_v1_de.png){ class="lightbox" title="Course, course element, learning resource and question bank" }

**Course:**<br> It is assembled from course elements in the course editor.

**Course element:** <br>Most course elements are containers into which a learning resource is inserted. E.g. a learning resource "Test" is inserted into the course element "Test". Please distinguish between these two "Tests"!

**Questions:** <br>A test learning resource consists of several individual questions, e.g., single choice, multiple choice, etc.

**Question bank:** <br>The individual questions can be collected in a question bank. When creating different test learning resources, the question bank can then be accessed. Existing questions from the question bank can be adopted (copied from there) and additional new questions can be created. <br>
Questions can be created in the question bank or the learning resource. Questions created in the learning resource are only available in this test learning resource as long as they are not transferred to the question bank for multiple use.

<br>

Settings (configurations) can be made for each of the elements. The configurations can therefore be made at different levels.

![Four nested levels, each with its own configuration: course, course element Test, learning resource Test and question](assets/grafik_konfigurationsebenen_v1_de.png){ width=450px class="lightbox" title="Configuration levels of a test" }


**Configuration of the course:**<br>
`Authoring > Select the course > Administration > Settings`

**Configuration of the course element:**<br>
`Authoring > Select the course > Administration > Course editor > Select the course element > Settings in the tabs`

**Configuration of the learning resource:**<br>
`Authoring > Select the test learning resource > Administration > Settings`

**Configuration of a question:**<br>
`Authoring > Select test learning resource > Administration > Test editor > Select question in the tree structure > Settings in the tabs`

<br>

:octicons-device-camera-video-24: **Video introduction (German)**: [Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>){:target="_blank"}

:octicons-device-camera-video-24: **Video introduction (German)**: [Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>){:target="_blank"}

:octicons-device-camera-video-24: **Video introduction (German)**: [Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>){:target="_blank"}

:octicons-device-camera-video-24: **Video introduction (German)**: [Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>){:target="_blank"}

<br>

---

## Procedure Option 1

If you are starting from scratch with the creation of a course, the following procedure is obvious.<br>

<br>

![Four steps from creating the course to creating the questions in the test learning resource](assets/flowchart_testerstellung1_v1_de.png){ class="lightbox" title="Procedure option 1" }

<br>

> <h3>Create a course</h3>

<br>

!!! note "Note"

    If you do not have any experience in course creation, you will find instructions in the chapter ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md).

1\. Go to Authoring and create a new course there.

![Create menu opened, entry Course highlighted](assets/testerstellung_1_1_v1_de.png){ class="lightbox" title="Authoring" }

2\. Assign a title and make initial settings for the course. Decide on a design.

![Title of the course entered and course design With learning path selected, below it the Create button](assets/testerstellung_1_2_v1_de.png){ class="lightbox" title="Dialog Create course" }

3\. If you want to use a wizard (course wizard) for the further process of course creation, you will be asked if you want to create an exam course.<br>
An exam course is a normal course (no matter if learning path course or conventional course) that already contains a certain configuration. So this option provides a later work relief.

![Button Create with course wizard opened, with the entries Simple course and Exam course](assets/testerstellung_1_3_v1_de.png){ class="lightbox" title="Dialog Create course with course wizard" }

4\. The first screen after clicking the "Create" button is the settings overview (configuration of the course).

!!! tip "Tip"

    Apart from the course design, you can also access and adjust the other details later under `Course > Administration > Settings`.

![Entry Settings in the Administration menu highlighted, next to it the tabs of the course settings from Info to Options](assets/testerstellung_1_4_v1_de.png){ class="lightbox" title="Settings of the course" }

<br>

> <h3>Insert course element "Test"</h3>

<br>

5\. Open the **Course editor** via the "Administration". Select "Insert course elements" and click on the desired course element type "Test" or "Self-test" there. This will insert a course element of this type.

![Entry Course editor in the Administration menu and button Insert course elements highlighted](assets/testerstellung_1_5_v1_de.png){ class="lightbox" title="Course editor" }

<br>

> <h3>Create a test learning resource within the course element</h3>

<br>

6\. Select the test course element in the course menu on the left.

7\. In the related tabs on the right side, under "Test configuration" you will find the "Create" button. Use it to create a new test learning resource.

![Course element Test in the course menu, tab Test configuration and button Create highlighted](assets/testerstellung_1_7_v1_de.png){ class="lightbox" title="Course element Test in the course editor" }

8\. Enter a name for the test learning resource as well.

![Title of the new test learning resource entered in the Title field](assets/testerstellung_1_8_v1_de.png){ class="lightbox" title="Dialog Create test" }

<br>

> <h3>Edit learning resource and create questions</h3>

<br>

9\. After creating the new test learning resource, you have the possibility to edit it, i.e. add questions.

![Embedded test learning resource with question types and points, link Edit learning resource highlighted](assets/testerstellung_1_9_v1_de.png){ class="lightbox" title="Tab Test configuration in the course element Test" }

10\. By default, a single choice question is already available. You can use this as a sample, delete it or modify it according to your needs.

![New test learning resource with one single choice question and the answer New answer, in the toolbar the links Administration and Info page](assets/testerstellung_1_10_v2_en.png){ class="lightbox" title="Test learning resource · 2026.09.28" }

11\. In the "Administration" of the test learning resource, now select the entry "Test editor". You will get to the test editor of the learning resource, not to the course editor.

![Entry Test editor in the Administration menu highlighted](assets/testerstellung_1_11_v2_en.png){ class="lightbox" title="Administration menu of a test learning resource · 2026.09.28" }

12\. Select "Add elements" and the appropriate question type, e.g. Multiple Choice.

![Button Add elements highlighted, below it a new multiple choice question in the Choice tab](assets/testerstellung_1_12_v1_de.png){ class="lightbox" title="Test editor" }

13\. In the "Choice" tab, enter the title of the question, the question wording and the possible answers. Additional answer options are added via the plus sign.

14\. In the "Points" tab you define the type and the sum of the points.

15\. If necessary, you define a feedback to the question. You can view the question via "Preview".

You add more questions according to the same principle. The details of the settings can vary depending on the question type. You can also further structure your test with sections or test parts.


!!! warning "Attention"

    Be sure to consider in advance which question type is most appropriate for your particular purposes, as the question type cannot be changed after the fact.

!!! tip "Tip"

    Copying questions is recommended when you have several questions with the same answer options, e.g. several questions with a value from a scale of 1-5.

<br>

---

## Procedure Option 2

If you already have some experience as an author and a course already exists, you can start with the learning resource "Test".

<br>

![Five steps from creating the test learning resource to inserting it into the test course element](assets/flowchart_testerstellung2_v1_de.png){ class="lightbox" title="Procedure option 2" }

<br>

> <h3>Create a test learning resource</h3>

<br>

1\. In Authoring, select the link "Create" and select the learning resource "Test".

![Entry Test (QTI 2.1) selected in the Create menu](assets/testerstellung_2_1_v1_de.png){ class="shadow lightbox" title="Authoring" }

2\. Enter a title for the test

![Title of the learning resource E-Learning Grundlagen entered, below it the Create button](assets/testerstellung_2_2_v1_de.png){ class="shadow lightbox" title="Dialog for creating a test" }

3\. A menu appears. Here you can make further settings in the different tabs if required.

The menu corresponds to the settings in the Administration section and can also be edited later.

![Tabs Info, Metadata, Share, Catalog and Options](assets/testerstellung_2_3_v1_de.png){ class="shadow lightbox" title="Settings of the test learning resource" }

:octicons-device-camera-video-24: **Video introduction (German)**: [Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>){:target="_blank"}

<br>

> <h3>Edit learning resource and create questions</h3>

<br>

4\. In the "Administration" of the learning resource "Test", select the entry "Test editor". You will get to the test editor.

![Entry Test editor in the Administration menu highlighted](assets/testerstellung_1_11_v2_en.png){ class="shadow lightbox" title="Administration menu of a test learning resource · 2026.09.28" }

5\. Select "Add elements" and select the appropriate question type, e.g. multiple choice.

6\. In the "Choice" tab, enter the title of the question, the question wording and the possible answers. Additional answer options are added via the plus sign.

7\. In the "Points" tab, define the type and the sum of the points.

8\. If needed, define a feedback to the question and preview it.

Add more questions according to the same principle. The details of the settings can vary depending on the question type. You can also further structure your test with sections or test parts.

:octicons-device-camera-video-24: **Video introduction (German)**: [Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>){:target="_blank"}

!!! info "Important"

    By default, a single choice question is already created, which you should use and edit or delete.

!!! warning "Attention"

    Be sure to consider in advance which question type is most appropriate for your particular purposes, as the question type cannot be changed after the fact.

!!! tip "Tip"

    Copying questions is recommended when you have several questions with the same answer options, e.g. several questions with a value from a scale of 1-5.

<br>

> <h3>Configure learning resource "Test"</h3>

<br>

9\. Select the top item of the test learning resource and edit the associated tabs as needed.

![Maximum of 50 points, output of Passed automatically by score threshold and a time limit of 30 minutes](assets/testerstellung_2_9_v1_de.png){ class="shadow lightbox" title="Tab Test configuration in the test editor" }

10\. **Test configuration:** Define from how many points the test is passed and whether or what time limit there is.

Define, if desired, a **general feedback:** in case of pass/fail (applies to automatic pass).

11\. **Expert:** Configure further details of the test procedure, e.g. type of navigation or display of solutions.

12\. Finally, close the test editor by clicking on the title of the test in the breadcrumb navigation.

![Title of the test clicked in the breadcrumb navigation](assets/testerstellung_2_12_v1_de.png){ class="shadow lightbox" title="Breadcrumb navigation in the test editor" }

:octicons-device-camera-video-24: **Video introduction (German)**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}

!!! tip "Tip"

    You can create feedback for individual questions as well as for the entire test.

<br>

> <h3>Insert course element "Test" into the existing course</h3>

<br>

13\. Go to Authoring. In the "My entries" area you will find your courses. Open the course in which you want to include the test.

14\. Open the "Course editor" via "Administration". Select "Insert course elements" and click on the desired course element type "Test" or "Self-test".

<br>

> <h3>Insert learning resource "Test" into the course element "Test"</h3>

<br>

15\. Go to the "Test configuration" tab and click the "Select, create or import file" button.<br>
A list with your test learning resources appears. Select the prepared test by clicking on the selection hook.

![Selected file still empty, below it the button Select, create or import file](assets/testerstellung_2_15_v1_de.png){ class="shadow lightbox" title="Tab Test configuration in the course element Test" }

16\. If required, you can preview the included test in the "Test configuration" tab under "Selected file" and also edit it as long as it has not been used by participants.

![Embedded test under Selected file with the buttons Change file, Edit and Show preview](assets/testerstellung_2_16_v1_de.png){ class="shadow lightbox" title="Tab Test configuration with selected test" }

17\. If required, the other tabs of the course element can still be configured. You can partially override the settings of the test learning resource with the settings of the course element. This makes sense if the same test learning resource is used in different courses.

18\. In order for learners to be able to work on the test, the course must still be published. To do this, simply close the course editor, e.g. by clicking on the name of the course in the breadcrumb navigation, and select "Publish manually" or "Publish automatically" in the dialog that appears.

Alternatively, you can also use the "Publish" button in the editor on the right side of the toolbar or the small red cross in the upper right corner.

19\. In order for learners to work on the test, the status of the course still needs to be changed to "Published".<br>
In the members management of the course you decide which learners get access.

20\. Once test results are available, coaches can make assessments in the assessment tool. (Does not apply to self-tests.)<br>
Further information can be found in the chapter "[Assessing tests](../../manual_user/learningresources/Assessing_tests.md)".

<br>

---

## Procedure Option 3

Is there a division of work and you, as the subject matter expert, are to create the questions that various colleagues can use in their tests?<br>
Then you can also start creating the individual questions in the question bank.

<br>

![Four steps from creating the questions in the question bank to inserting the test into the Test course element](assets/flowchart_testerstellung3_v1_de.png){ class="lightbox" title="Procedure option 3" }

<br>

> <h3>Create questions in the question bank</h3>

<br>

1\. If you have author rights, the question bank is displayed in the main navigation in addition to Authoring. Go to the question bank.

![Question bank highlighted and opened, on the left the menu My question bank](assets/testerstellung_3_1_v1_de.png){ class="lightbox" title="Question bank in the main navigation" }

2\. Select "Create question" and the appropriate question type, e.g. Multiple Choice.

![Button Create question highlighted, above the list My questions](assets/testerstellung_3_2_v1_de.png){ class="lightbox" title="Question bank" }

3\. In the "Choice" tab, enter the title of the question, the question wording and the possible answers. Additional answer options are added via the plus sign.

![Choice tab of a new multiple choice question in the question bank with the fields Title, Question and four answers, three of them ticked as correct](assets/testerstellung_3_3_v2_en.png){ class="lightbox" title="Question in the question bank · 2026.09.28" }

4\. In the "Points" tab you define the type and the sum of the points.

5\. If necessary, you define a feedback to the question. You can view the question via "Preview".

Add more questions according to the same principle. The details of the settings can vary depending on the question type. You can also further structure your test with sections or test parts.


!!! warning "Attention"

    Be sure to consider in advance which question type is most appropriate for your particular purposes, as the question type cannot be changed after the fact.

!!! tip "Tip"

    Copying questions is recommended when you have several questions with the same answer options, e.g. several questions with a value from a scale of 1-5.


<br>

> <h3>Create and edit test learning resource</h3>

<br>

6\. Switch to Authoring and create a test (test learning resource).

![Entry Test in the Create menu highlighted](assets/testerstellung_3_6_v1_de.png){ class="lightbox" title="Authoring" }

!!! note "Note"

    The new test learning resource is not listed under the "My courses" tab in Authoring, but under "My entries". It is recognizable by the icon for test learning resources.
    ![Tab My entries with the filter Type Test, test icon in the Type column highlighted](assets/testerstellung_3_6b_v1_de.png){ class="lightbox" title="Tab My entries in Authoring" }

7\. Open the editor by clicking **Administration** and then **"Test editor"**.

![Entry Test editor in the Administration menu highlighted](assets/testerstellung_3_7_v2_en.png){ class="lightbox" title="Administration menu of a test learning resource · 2026.09.28" }

8\. In the test editor (recognizable by the shaded header) you can now add new questions under **"Add elements"**.

![Opened menu Add elements with the question types](assets/testerstellung_3_8_v1_de.png){ class="lightbox" title="Test editor" }

<br>

> <h3>Import questions from the question bank</h3>

<br>

9\. As an alternative to creating new questions, you can add existing questions under the same menu item with **"Import questions from pool"**.

![Entry Import questions from pool in the Add elements menu highlighted](assets/testerstellung_3_9_v1_de.png){ class="lightbox" title="Menu Add elements in the test editor" }

10\. If you click on the title of a single question, it will be inserted directly. To import several questions, select the questions and confirm by clicking the "Select" button.

![Selected question and button Select highlighted](assets/testerstellung_3_10_v1_de.png){ class="lightbox" title="Dialog Choose questions" }

11\. Once all the questions are recorded in the test learning resource, exit the learning resource editor.

<br>

> <h3>Insert test learning resource into the test course element</h3>

<br>

12\. Go to Authoring. In "My entries" you will find your courses. Open the course in which you want to include the test learning resource.

13\. Open the "Course editor" via "Administration". Select "Insert course elements" and click on the desired course element type "Test" or "Self-test".

14\. Go to the "Test configuration" tab and click the "Select, create or import file" button.<br>
A list with your test learning resources will appear. Select the prepared test by clicking the selection hook.

15\. If required, you can preview the included test in the "Test configuration" tab under "Selected file" and also edit it as long as it has not been used by participants.

16\. The other tabs of the course element can be configured as required. You can partly override the settings of the test learning resource with the settings of the course element. This makes sense if the same test learning resource is used in different courses.

17\. In order for learners to be able to work on the test, the course must still be published. To do this, simply close the course editor, e.g. by clicking on the name of the course in the breadcrumb navigation, and select "Publish manually" or "Publish automatically" in the dialog that appears.

Alternatively, you can also use the "Publish" button in the editor on the right side of the toolbar or the small red cross in the upper right corner.

18\. In order for learners to work on the test, the status of the course still has to be changed to "Published".<br>
In the members management of the course you decide which learners get access.

19\. Once test results are available, coaches can make assessments in the assessment tool. (Does not apply to self-tests.)<br>
Further information can be found in the chapter "[Assessing tests](../../manual_user/learningresources/Assessing_tests.md)".


<br>

---

## Checklist {: #checklist}

- [x] Course available?

- [x] Course element "Test" or "Self-test" available?

- [x] Learning resource "Test" created?

- [x] Already existing questions from the question bank transferred into the learning resource?

- [x] Additional questions created within the learning resource?

- [x] Learning resource "Test" configured?

- [x] Course element "Test" configured?

---

## Further information {: #further_information}

[How do I create my first OpenOlat course? >](../my_first_course/my_first_course.md)<br>
[Assessing tests >](../../manual_user/learningresources/Assessing_tests.md)<br>
[Test editor >](../../manual_user/learningresources/Test_editor_QTI_2.1.md)<br>
[Course Element "Test" >](../../manual_user/learningresources/Course_Element_Test.md)<br>
[Question Bank: Overview >](../../manual_user/area_modules/Question_Bank.md)<br>
[How do I exchange a test? >](../exchange_tests/exchange_tests.md)

**youtube**<br>
[Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>)<br>
[Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>)<br>
[Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>)<br>
[Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>)<br>
[Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>)<br>
[Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>)<br>
[Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>)<br>
[Tests erstellen/bearbeiten](<https://www.youtube.com/embed/eNNdDdQDlfs>)

[To the top of the page ^](#test_creation_procedure)
