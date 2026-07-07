# Creating Tests {: #create_tests}

This chapter explains how OpenOlat authors can create tests, which question types are available, and which configuration options are available. In addition, there is information on the integration and use of tests and self-tests in courses, as well as the assessment and provision of test results. 

OpenOlat tests are available in the standardized document format QTI 2.1. QTI stands for "Question & Test Interoperability" and is a defined, standardized data format used for designing online tests. The advantage is that these standardized tests can be used in various LMS and other systems that support the standard. [IMS](http://www.imsglobal.org/ "IMS") is working to develop such open standards for the e-learning sector.

In OpenOlat, tests are part of the "learning resources." Learning resources are created separately and can be integrated into online courses. For example, the same learning resource "Test (QTI 2.1)" can be used in multiple courses.

[To the top of the page ^](#create_tests)

---


## What is a test? {: #definition_test}

Tests are used to monitor performance, check current knowledge, or as online exams. They can be used at the beginning, during, or at the end of a course, or independently of courses.

Formative tests are about assessing interim learning progress and achieving learning-related improvement based on automated or manual feedback.  

Summative tests are only used at the end of a learning process or course. They are used to check whether the planned learning objectives have been achieved. Examples of this are rigorous exams or online tests.

Tests are created with the [OpenOlat test editor](Test_editor_QTI_2.1.md) as QTI 2.1 tests. The length of the test, the [question types](Test_question_types.md), and a range of other configurations can be specified.

Test subjects cannot see which answers are correct and which are incorrect in the source code of the test or self-test, as the answers are sent to the OpenOlat server and assessed there.

When you integrate a test into your course, you can decide whether you want to use it as a self-test, i.e. for practice purposes, or as an exam test ("live" test). In the first case, use the "Self-test" course element when integrating the test into the course; in the second case, use the "Test" course element. Self-test results are anonymized, while exam test results are stored in a personalized manner. In the case of self-tests, the teacher cannot see the results achieved by a specific learner.

Depending on the teaching scenario, however, it also makes sense to use normal "tests" rather than "self-tests" for practice purposes, namely whenever the teacher wants to know how individual learners are progressing or when it comes to identifying weaker course members and providing them with targeted support. In this respect, it should always be checked on an individual basis which module is the most suitable in each case.

[To the top of the page ^](#create_tests)

---


## How do the questions get into a test? {: #create_questions_in_tests}

Questions can either be created directly in the learning resource Test or created in the [question pool](../area_modules/Question_Bank.md) and then integrated into the test. In the chapter [How do I proceed when creating a test?](../../manual_how-to/test_creation_procedure/test_creation_procedure.md), you will learn how to create a test.

When importing a question from the question pool into a test, a copy of the question is made at that point in time. The question in the test is therefore independent of the original question in the question pool. If the original question in the question pool is modified, this does not affect the imported question in the test. It remains unchanged.

Questions imported from the question pool into tests cannot be edited in the editor!

If a question needs to be edited, you can create a copy of the question and enable editing by selecting "Create copy and edit." The question will then be assigned a new ID. However, you can still access the original question in the question pool using the master ID.

You may have already exported a test file in IMS QTI format from another LMS and want to import it into OpenOlat. The chapter "Actions in the authoring area" explains how to do this under [Import](../area_modules/authoring_new_course.md#import-learning-resources).

!!! info "Important"

    During import, the test file is checked for a valid QTI 2.1 package. Incorrectly generated packages, for example from external tools, are rejected with an error message. [:octicons-tag-16:{ title="from Release 20.3.2 (OO-9454)" }](https://track.frentix.com/issue/OO-9454)

[To the top of the page ^](#create_tests)

---


## Further information {: #further_information}

* [Changing from QTI 1.2 to QTI 2.1](Changing_from_QTI_1.2_to_QTI_2.1.md)
* [How do I proceed when I create a test?](../../manual_how-to/test_creation_procedure/test_creation_procedure.md)
* [Test editor QTI 2.1](Test_editor_QTI_2.1.md)
  * [Test question types](Test_question_types.md)
  * [Configure test questions](Configure_test_questions.md)
  * [Configure tests](Configure_tests.md)
* [Test settings](Test_settings.md)
* [Tests at course level](Tests_at_course_level.md)
* [Export tests](Test_export.md)

[To the top of the page ^](#create_tests)