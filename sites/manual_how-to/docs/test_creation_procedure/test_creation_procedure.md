# How do I proceed when I create a test? {: #test_creation_procedure}

??? abstract "Objectives and content of this instruction"

    Whether you build a new course, add a test to an existing course or first collect questions in the question bank: for each of these starting points, these instructions show a separate way to the finished test. Compare the three ways and choose the one that fits your situation.

    All three ways require the role Author. With this role, the main navigation shows Authoring and the question bank.

??? abstract "Target group"

    [x] Beginners [x] Advanced users  [ ] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)


---

## The interaction of the components

A test in OpenOlat consists of several components that work together. If you keep them apart, you find every setting in the right place.

![Course element of type Test containing the learning resource Test, whose questions are exchanged with the question bank](assets/kurs-kursbaustein-lernressource-frage_v1_de.png){ class="lightbox" title="Course, course element, learning resource and question bank" }

**Course:**<br> You assemble it from course elements in the course editor.

**Course element:** <br>Most course elements are containers into which you insert a learning resource. For example, you insert a learning resource "Test" into the course element "Test". Keep these two "Tests" apart: you configure the course element in the course editor and the learning resource in the test editor.

**Questions:** <br>A test learning resource consists of individual questions of different question types, for example single choice or multiple choice.

**Question bank:** <br>In the question bank you collect individual questions to use them in several tests. When you create a test learning resource, you adopt existing questions from the question bank, and OpenOlat copies them into the test. You create additional questions directly in the learning resource if required. <br>
A question created in the learning resource only exists in this test learning resource. For multiple use, you transfer it to the question bank in the test editor with "Export to pool".

<br>

Each of these components has its own settings (configurations). You therefore configure a test on four levels. You open the course and the test learning resource in Authoring; the click paths below start at the opened course or test.

![Four nested levels, each with its own configuration: course, course element Test, learning resource Test and question](assets/grafik_konfigurationsebenen_v1_de.png){ width=450px class="lightbox" title="Configuration levels of a test" }


**Configuration of the course:**<br>
`Course > Administration > Settings`

**Configuration of the course element:**<br>
`Course > Administration > Course editor > "Course element" > Tabs of the course element`

**Configuration of the learning resource:**<br>
`Test learning resource > Administration > Settings`

**Configuration of a question:**<br>
`Test learning resource > Administration > Test editor > "Question" in the tree structure > Tabs of the question`

<br>

:octicons-device-camera-video-24: **Video introduction (German)**: [Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>){:target="_blank"}

:octicons-device-camera-video-24: **Video introduction (German)**: [Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>){:target="_blank"}

:octicons-device-camera-video-24: **Video introduction (German)**: [Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>){:target="_blank"}

:octicons-device-camera-video-24: **Video introduction (German)**: [Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>){:target="_blank"}

<br>

---

## Procedure Option 1

If you start from scratch, without a course and without questions, this way leads you in four stages from the new course to the finished test.<br>

<br>

![Four steps from creating the course to creating the questions in the test learning resource](assets/flowchart_testerstellung1_v1_de.png){ class="lightbox" title="Procedure option 1" }

<br>

> <h3>Create a course</h3>

<br>

!!! note "Note"

    If you have not created a course yet, the instructions ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md) guide you step by step.

1\. Create a new course via `Authoring > Create > Course`.

![Open Create menu in Authoring, highlighted the entry Course, with which you set up a new course](assets/testerstellung_1_1_v2_en.png){ class="shadow lightbox" title="Create menu in Authoring · 2026.11.10" }

2\. In the "Create course" dialog, enter a title and define initial settings of the course. Under "Course design", select the appropriate design, for example "With learning path".

![Create course dialog, highlighted the Title field with a course title and the selected course design With learning path, below the buttons Create with course wizard and Create](assets/testerstellung_1_2_v2_en.png){ class="shadow lightbox" title="Dialog Create course · 2026.11.10" }

3\. If you want a wizard to guide you through the further setup, click "Create with course wizard" instead of "Create" and select "Simple course" or "Exam course".<br>
An exam course is a normal course, either a learning path course or a conventional course. Its wizard sets up the exam with the test in one pass, and on request also the re-exam, the certificate, coaches and participants. This saves you work later.

![Highlighted the opened button Create with course wizard with the entries Simple course and Exam course, through which a wizard takes over the further setup](assets/testerstellung_1_3_v2_en.png){ class="shadow lightbox" title="Dialog Create course with course wizard · 2026.11.10" }

4\. Click "Create". OpenOlat then opens the settings of the course (configuration of the course).

!!! tip "Tip"

    You can also adjust all details except the course design later under `Course > Administration > Settings`.

![Highlighted the entry Settings in the Administration menu and next to it the tabs of the course settings from Metadata to Options, in which you adjust the course details later](assets/testerstellung_1_4_v2_en.png){ class="shadow lightbox" title="Settings of the course · 2026.11.10" }

<br>

> <h3>Insert course element "Test"</h3>

<br>

5\. Open the course editor via `Course > Administration > Course editor`. Click "Insert course elements" and select the type "Test" or "Self-test". OpenOlat inserts a course element of this type into the course.

![Highlighted the entry Course editor in the Administration menu and, in the toolbar of the course editor, the button Insert course elements, with which you add the course element Test](assets/testerstellung_1_5_v2_en.png){ class="shadow lightbox" title="Course editor · 2026.11.10" }

<br>

> <h3>Create a test learning resource within the course element</h3>

<br>

6\. Click the new course element in the course menu on the left.

7\. On the right, open the "Test configuration" tab, for a self-test "Self-test configuration", and click "Create". This creates a new test learning resource that is directly linked to the course element.

![Highlighted the new course element Test in the course menu, the Test configuration tab and the Create button, with which you set up a new test learning resource](assets/testerstellung_1_7_v2_en.png){ class="shadow lightbox" title="Course element Test in the course editor · 2026.11.10" }

8\. In the "Create test" dialog, enter a title for the test learning resource and click "Create".

![Create test dialog with the title E-Learning Basics in the Title field, field and Create button highlighted](assets/testerstellung_2_2_v2_en.png){ class="shadow lightbox" title="Dialog Create test · 2026.11.10" }

<br>

> <h3>Edit learning resource and create questions</h3>

<br>

9\. The "Test configuration" tab now shows the new test learning resource. With "Edit learning resource" you open it to add questions.

![Embedded test learning resource in the Test configuration tab, highlighted the buttons Preview and Replace and the link Edit learning resource, which opens the test for editing](assets/testerstellung_1_9_v2_en.png){ class="shadow lightbox" title="Tab Test configuration in the course element Test · 2026.11.10" }

10\. A new test learning resource already contains a single choice question. Use it as a sample, adjust it or delete it.

![New test learning resource with one single choice question and the answer New answer, in the toolbar the links Administration and Info page](assets/testerstellung_1_10_v2_en.png){ class="lightbox" title="Test learning resource · 2026.09.28" }

11\. Open the test editor via `Test learning resource > Administration > Test editor`. The test editor belongs to the learning resource; you continue to edit the course in the course editor.

![Entry Test editor in the Administration menu highlighted](assets/testerstellung_1_11_v2_en.png){ class="lightbox" title="Administration menu of a test learning resource · 2026.09.28" }

12\. Click "Add elements" and select the appropriate question type, for example "Multiple choice".

![Highlighted the button Add elements in the toolbar of the test editor, with which you create a question such as the multiple choice question in the Choice tab shown below](assets/testerstellung_1_12_v2_en.png){ class="shadow lightbox" title="Test editor · 2026.11.10" }

13\. In the "Choice" tab, enter the title of the question, the question wording and the possible answers. You add further answers via the plus sign.

14\. In the "Score" tab you define the method of assessment and the score.

15\. In the "Feedback" tab you add feedback to the question if required. In the "Preview" tab you check the question.

You add more questions according to the same principle; the settings differ depending on the question type. With sections or [test parts](../../manual_user/learningresources/Configure_tests.md#testpart) you structure the test further.


!!! warning "Attention"

    Consider before creating which question type serves your purpose best. You cannot change the question type of a created question afterwards.

!!! tip "Tip"

    If you need several questions with the same answers, for example a scale from 1 to 5, copy a finished question: in the test editor, select "Duplicate" in the menu with the three dots. Then you only adjust the question wording.

<br>

---

## Procedure Option 2

If the course already exists and you have some experience as an author, start with the learning resource "Test" and then include it in the course.

<br>

![Five steps from creating the test learning resource to inserting it into the test course element](assets/flowchart_testerstellung2_v1_de.png){ class="lightbox" title="Procedure option 2" }

<br>

> <h3>Create a test learning resource</h3>

<br>

1\. Create a test learning resource via `Authoring > Create > Test`.

![Create menu opened in Authoring, entry Test highlighted](assets/testerstellung_2_1_v2_en.png){ class="shadow lightbox" title="Create menu in Authoring · 2026.11.10" }

2\. In the "Create test" dialog, enter the title of the test and click "Create".

![Dialog Create test with the title E-Learning Basics in the Title field, Create button highlighted](assets/testerstellung_2_2_v2_en.png){ class="shadow lightbox" title="Dialog Create test · 2026.11.10" }

3\. OpenOlat then opens the settings of the test learning resource. Define further settings in the tabs if required.

You can also adjust the same settings later under `Test learning resource > Administration > Settings`.

![Settings of the test learning resource with the tabs Metadata, Info, Share and Options](assets/testerstellung_2_3_v2_en.png){ class="shadow lightbox" title="Settings of the test learning resource · 2026.11.10" }

:octicons-device-camera-video-24: **Video introduction (German)**: [Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>){:target="_blank"}

<br>

> <h3>Edit learning resource and create questions</h3>

<br>

4\. Open the test editor via `Test learning resource > Administration > Test editor`.

![Entry Test editor in the Administration menu highlighted](assets/testerstellung_1_11_v2_en.png){ class="shadow lightbox" title="Administration menu of a test learning resource · 2026.09.28" }

5\. Click "Add elements" and select the appropriate question type, for example "Multiple choice".

6\. In the "Choice" tab, enter the title of the question, the question wording and the possible answers. You add further answers via the plus sign.

7\. In the "Score" tab you define the method of assessment and the score.

8\. In the "Feedback" tab you add feedback to the question if required. In the "Preview" tab you check the question.

You add more questions according to the same principle; the settings differ depending on the question type. With sections or [test parts](../../manual_user/learningresources/Configure_tests.md#testpart) you structure the test further.

:octicons-device-camera-video-24: **Video introduction (German)**: [Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>){:target="_blank"}

!!! info "Important"

    A new test learning resource already contains a single choice question. Edit or delete this question so that it does not remain in the test unintentionally.

!!! warning "Attention"

    Consider before creating which question type serves your purpose best. You cannot change the question type of a created question afterwards.

!!! tip "Tip"

    If you need several questions with the same answers, for example a scale from 1 to 5, copy a finished question: in the test editor, select "Duplicate" in the menu with the three dots. Then you only adjust the question wording.

<br>

> <h3>Configure learning resource "Test"</h3>

<br>

9\. In the test editor, click the top item on the left, the title of the test. On the right, the tabs with the settings for the whole test appear.

![Top element of the test editor selected, in the Test configuration tab a maximum of 3 points, passed automatically from a cut value of 2 and a time limit of 30 minutes](assets/testerstellung_2_9_v2_en.png){ class="shadow lightbox" title="Tab Test configuration in the test editor · 2026.11.10" }

10\. **Test configuration:** Define from how many points the test is passed and whether a time limit applies.

In the "Feedback" tab you add, if required, a general feedback for passed and for failed tests. It applies when OpenOlat outputs the passed status automatically via the score threshold.

11\. **Expert:** Define further details of the test procedure, for example the navigation or the display of solutions.

12\. Finally, leave the test editor by clicking the title of the test in the bread-crumb navigation.

![Title of the test highlighted in the bread-crumb navigation of the test editor](assets/testerstellung_2_12_v2_en.png){ class="shadow lightbox" title="Bread-crumb navigation in the test editor · 2026.11.10" }

:octicons-device-camera-video-24: **Video introduction (German)**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}

!!! tip "Tip"

    You add feedback for individual questions in the "Feedback" tab of the question and for the whole test in the "Feedback" tab of the top item.

<br>

> <h3>Insert course element "Test" into the existing course</h3>

<br>

13\. In Authoring, open the course the test belongs to. You find your courses in the tabs "My courses" and "My entries".

14\. Open the course editor via `Course > Administration > Course editor`. Click "Insert course elements" and select the type "Test" or "Self-test".

<br>

> <h3>Insert learning resource "Test" into the course element "Test"</h3>

<br>

15\. In the new course element, open the "Test configuration" tab and click "Select".<br>
In the "Select test learning resource" dialog, select the prepared test.

![New course element Test in the course editor, Test configuration tab still without a test learning resource, Select button highlighted](assets/testerstellung_2_15_v2_en.png){ class="shadow lightbox" title="Tab Test configuration in the course element Test · 2026.11.10" }

16\. The "Test configuration" tab now shows the included test. With "Preview" you view it, with "Edit learning resource" you open it for editing. As soon as participants have started the test, editing is limited.

![Embedded test learning resource in the Test configuration tab, highlighted the buttons Preview and Replace and the link Edit learning resource, with which you view, exchange or edit the test](assets/testerstellung_1_9_v2_en.png){ class="shadow lightbox" title="Tab Test configuration with embedded test · 2026.11.10" }

17\. Configure the other tabs of the course element if required. Here you override part of the settings of the test learning resource for this course. This is worthwhile if you use the same test learning resource in different courses.

18\. So that participants can work on the test, publish the course. To do this, close the course editor, for example by clicking the name of the course in the bread-crumb navigation, and select "Publish manually" or "Publish automatically" in the dialog that follows.

Alternatively, click "Publish" on the right of the toolbar in the course editor, or close the course editor via the small red cross in the upper right corner.

19\. Then set the status of the course to "Published" so that participants can work on the test.<br>
You decide who gets access under `Course > Administration > Members management`.

20\. Once test results are available, coaches assess the participants in the assessment tool. For a self-test, this step does not apply.<br>
How this works is described on the page [Assessing tests](../../manual_user/learningresources/Assessing_tests.md).

<br>

---

## Procedure Option 3

Do you share the work with colleagues and create, as a subject matter expert, questions that are used in several tests?<br>
Then start in the question bank: the questions there are available for every test you adopt them into.

<br>

![Four steps from creating the questions in the question bank to inserting the test into the Test course element](assets/flowchart_testerstellung3_v1_de.png){ class="lightbox" title="Procedure option 3" }

<br>

> <h3>Create questions in the question bank</h3>

<br>

1\. Open the question bank in the main navigation. With the role Author, it appears there next to Authoring.

![Highlighted the entry Question bank in the main navigation next to Authoring, below it the opened question bank with the menu My question bank](assets/testerstellung_3_1_v2_en.png){ class="shadow lightbox" title="Question bank in the main navigation · 2026.11.10" }

2\. Under "My question bank", select the entry "My questions" and click "Create question". Enter a title and select the appropriate type under "Type", for example "Multiple-Choice".

![Highlighted the entry My questions in the menu My question bank and the button Create question above the list, with which you create a new question](assets/testerstellung_3_2_v2_en.png){ class="shadow lightbox" title="My questions in the question bank · 2026.11.10" }

3\. In the "Choice" tab, enter the title of the question, the question wording and the possible answers. You add further answers via the plus sign.

![Choice tab of a new multiple choice question in the question bank with the fields Title, Question and four answers, three of them ticked as correct](assets/testerstellung_3_3_v2_en.png){ class="lightbox" title="Question in the question bank · 2026.09.28" }

4\. In the "Score" tab you define the method of assessment and the score.

5\. In the "Feedback" tab you add feedback to the question if required. In the "Preview" tab you check the question.

You create more questions according to the same principle; the settings differ depending on the question type.


!!! warning "Attention"

    Consider before creating which question type serves your purpose best. You cannot change the question type of a created question afterwards.

!!! tip "Tip"

    If you need several questions with the same answers, for example a scale from 1 to 5, copy a finished question and only adjust the question wording.

So that you find the questions again later via the search filters and the course element "Practice" selects them automatically, maintain the metadata of every question in the question bank, for example subject, level and keywords. The instructions [Benefits of metadata](../question_metadata/question_metadata.md) show how this works.

<br>

> <h3>Create and edit test learning resource</h3>

<br>

6\. Create a test learning resource via `Authoring > Create > Test`.

![Create menu opened in Authoring, entry Test highlighted](assets/testerstellung_2_1_v2_en.png){ class="shadow lightbox" title="Create menu in Authoring · 2026.11.10" }

!!! note "Note"

    You find the new test learning resource in Authoring in the "My entries" tab, because the "My courses" tab only lists courses. In the "Type" column you recognize it by the icon for test learning resources.
    ![Highlighted the tab My entries, the filter Type with the value Test and the Type column, in which you recognize test learning resources by their icon](assets/testerstellung_3_6b_v2_en.png){ class="shadow lightbox" title="Tab My entries in Authoring · 2026.11.10" }

7\. Open the test editor via `Test learning resource > Administration > Test editor`.

![Entry Test editor in the Administration menu highlighted](assets/testerstellung_3_7_v2_en.png){ class="lightbox" title="Administration menu of a test learning resource · 2026.09.28" }

8\. You recognize the test editor by the shaded header. Here you add new questions under "Add elements".

![Highlighted the button Add elements and, in the opened menu, the question types from Single choice to Drawing, from which you select the type of the new question](assets/testerstellung_3_8_v2_en.png){ class="shadow lightbox" title="Menu Add elements in the test editor · 2026.11.10" }

<br>

> <h3>Import questions from the question bank</h3>

<br>

9\. You adopt your questions from the question bank in the same menu with "Import questions from pool". OpenOlat copies them into the test; there they are initially read-only. How to edit such a question is described under [Using questions from the question bank](../../manual_user/learningresources/Test_editor_QTI_2.1/index.md#questions_from_pool).

![Highlighted the entry Import questions from pool in the Add elements menu, with which you adopt questions from the question bank into the test](assets/testerstellung_3_9_v2_en.png){ class="shadow lightbox" title="Menu Add elements in the test editor · 2026.11.10" }

10\. The "Choose questions" dialog shows your questions under "My favorites" and "My questions", depending on the configuration also under "My lists" and "My shares". A click on the title of a question inserts it directly. For several questions, tick the checkboxes and click "Select".

![Selected question and button Select highlighted](assets/testerstellung_3_10_v1_de.png){ class="lightbox" title="Dialog Choose questions" }

11\. With sections or [test parts](../../manual_user/learningresources/Configure_tests.md#testpart) you structure the questions in the test further if required. Once all questions are in the test learning resource, leave the test editor.

<br>

> <h3>Insert test learning resource into the test course element</h3>

<br>

12\. In Authoring, open the course the test learning resource belongs to. You find your courses in the tabs "My courses" and "My entries".

13\. Open the course editor via `Course > Administration > Course editor`. Click "Insert course elements" and select the type "Test" or "Self-test".

14\. In the new course element, open the "Test configuration" tab and click "Select".<br>
In the "Select test learning resource" dialog, select the prepared test.

15\. The "Test configuration" tab now shows the included test. With "Preview" you view it, with "Edit learning resource" you open it for editing. As soon as participants have started the test, editing is limited.

16\. Configure the other tabs of the course element if required. Here you override part of the settings of the test learning resource for this course. This is worthwhile if you use the same test learning resource in different courses.

17\. So that participants can work on the test, publish the course. To do this, close the course editor, for example by clicking the name of the course in the bread-crumb navigation, and select "Publish manually" or "Publish automatically" in the dialog that follows.

Alternatively, click "Publish" on the right of the toolbar in the course editor, or close the course editor via the small red cross in the upper right corner.

18\. Then set the status of the course to "Published" so that participants can work on the test.<br>
You decide who gets access under `Course > Administration > Members management`.

19\. Once test results are available, coaches assess the participants in the assessment tool. For a self-test, this step does not apply.<br>
How this works is described on the page [Assessing tests](../../manual_user/learningresources/Assessing_tests.md).


<br>

---

## Checklist {: #checklist}

Before participants work on the test, check these points:

- [x] Course available?

- [x] Course element "Test" or "Self-test" available?

- [x] Learning resource "Test" created?

- [x] Existing questions from the question bank adopted into the learning resource?

- [x] Additional questions created in the learning resource?

- [x] Test learning resource configured?

- [x] Test course element configured?

- [x] Course published and status "Published" set?

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I create my first OpenOlat course? >](../my_first_course/my_first_course.md)<br>
[Configure tests >](../../manual_user/learningresources/Configure_tests.md)<br>
[Assessing tests >](../../manual_user/learningresources/Assessing_tests.md)<br>
[Benefits of metadata >](../question_metadata/question_metadata.md)<br>
[Test editor >](../../manual_user/learningresources/Test_editor_QTI_2.1/index.md)

**Further reading**<br>
[Course Element "Test" >](../../manual_user/learningresources/Course_Element_Test/index.md)<br>
[Question Bank: Overview >](../../manual_user/area_modules/Question_Bank/index.md)<br>
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
