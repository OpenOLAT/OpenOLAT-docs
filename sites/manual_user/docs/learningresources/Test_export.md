# Export tests {: #test_export}

When exporting tests, a distinction must be made between

- export test **course** (Exam course)
- export test **learning resource**
- export single **questions**
- export test **results**


## Export course {: #export_course}

An entire course, e.g., an exam course, can be exported as a zip file under <br>**Administration > Export content**.

![test_export_course_content_v1_de.png](assets/test_export_course_content_v1_de.png){ class="shadow lightbox"}

[To the top of the page ^](#test_export)

---

## Export test learning resource {: #export_learning_resource}

Test learning resources contain entire sets of questions and can be integrated into test course modules as question packs, including configuration (total number of points, etc.).
A test learning resource can also be exported under<br>**Administration > Export content**

![test_export_resource_content_v1_de.png](assets/test_export_resource_content_v1_de.png){ class="shadow lightbox"}

!!! tip "Hint"

    Please note whether you are in the administration of a (test) course or a (test) learning resource. You can easily tell by checking whether the option under Administration is <br>
            **Course editor**<br>
            or<br>
            **Edit content**


[To the top of the page ^](#test_export)

---


### Export as word file {: #word}

Test learning resources can be exported as Word documents. Such files are often created for review purposes before a test is conducted, so that additions and corrections can be easily noted in them.

![test_export_resource_word_v1_de.png](assets/test_export_resource_word_v1_de.png){ class="shadow lightbox"}

[To the top of the page ^](#test_export)

---


### Generate hand-written exam

The Word documents created with this option under the administration of a test learning resource differ from a simple Word export.

![test_export_resource_test_manually1_v1_de.png](assets/test_export_resource_test_manually1_v1_de.png){ class="shadow lightbox"}

Each document is given a cover sheet and a serial number so that it can be clearly assigned after the participants have completed the test by hand.

You must therefore specify a number for the Word files to be generated.

![test_export_resource_test_manually2_v1_de.png](assets/test_export_resource_test_manually2_v1_de.png){ class="shadow lightbox"}

Various attributes can be selected for the cover page.

![test_export_resource_test_manually3_v1_de.png](assets/test_export_resource_test_manually3_v1_de.png){ class="shadow lightbox"}

A descriptive text can also be provided.

![test_export_resource_test_manually4_v1_de.png](assets/test_export_resource_test_manually4_v1_de.png){ class="shadow lightbox"}

**Cover page example:**

![test_export_resource_test_manually6_v1_de.png](assets/test_export_resource_test_manually6_v1_de.png){ class="shadow lightbox"}


[To the top of the page ^](#test_export)

---


## Export single questions

Questions created in OpenOlat comply with the QTI standard. This means they can also be transferred to other LMS' that use questions in the QTI standard. Conversely, OpenOlat can also import questions in QTI format. 

### Export to pool

If you are in the editor of a test learning resource, select the desired question and click on the icon with the 3 dots in the upper right corner to export the question to the pool.

![test_export_question_to_pool_v1_de.png](assets/test_export_question_to_pool_v1_de.png){ class="shadow lightbox"}

!!! tip "Hint"

    This way, you can also export an entire section with multiple questions to the question pool. Simply select the section on the left and then click on the 3 dots.

[To the top of the page ^](#test_export)

---


### Export single questions from the pool

If you have opened a single question in the question editor, you will find an option to export this individual question to a zip file under the "Share" icon. Since the questions in OpenOlat comply with the QTI standard, the zip file can be reimported into another OpenOlat or another LMS that also uses the QTI standard.  

![test_export_single_question_from_pool_v1_de.png](assets/test_export_single_question_from_pool_v1_de.png){ class="shadow lightbox"}

[To the top of the page ^](#test_export)

---

### Export multiple selected single questions from the pool

If you have selected multiple questions from the question pool, these questions can be exported together in both a Word file and a zip file for transfer to another LMS.

![test_export_several_questions_from_pool1_v1_de.png](assets/test_export_several_questions_from_pool1_v1_de.png){ class="shadow lightbox"}


![test_export_several_questions_from_pool2_v1_de.png](assets/test_export_several_questions_from_pool2_v1_de.png){ class="shadow lightbox"}


[To the top of the page ^](#test_export)

---


## Export test results {: #export_results}

### Test statistics

One way to evaluate the test results is in statistical form. To do this, use the **"Test Statistics" button** in the "Participants" tab. The button is available to instructors and owners when they select a "Test" course element in run mode.

![test_export_statistics1_v1_de.png](assets/test_export_statistics1_v1_de.png){ class="shadow lightbox"}

* You can print out the various statistics on the test results (or "print" them to a PDF file) or download the raw data as an Excel file.
* When you expand the sections of a test, you can view detailed statistics for each individual question. 

![test_export_statistics2_v1_de.png](assets/test_export_statistics2_v1_de.png){ class="shadow lightbox"}

### Test results of participants

The **"Export results" button** creates a zip file containing all test results for all participants in the selected course module.

![test_export_results1_v1_de.png](assets/test_export_results1_v1_de.png){ class="shadow lightbox"}

If you have decided to create a zip file, you can specify a name for the zip file and choose one of the options offered for its contents.
Two variants of a zip file can be created:

* The **standard export** contains detailed test results for each participant in the form of an HTML document and an Excel file with the raw data.
* The **"Advanced - with PDF"** option creates the same zip file, but also adds PDF files with the results. 

![test_export_results2_v1_de.png](assets/test_export_results2_v1_de.png){ class="shadow lightbox"}

Click on the **"Start export" button** to generate the zip file containing the test results. 

Created zip files are listed in the lower section under **"Export history"**.

Then open or unzip the created zip file to access the required files.

!!! hint "Note"

    There is also an option in the course administration to export or archive test results. For more information, see [Archiving test results](../learningresources/Course_Element_Test.md#archive).


[To the top of the page ^](#test_export)

---


## Further information {: #further_information}

[How do I procede when creating a test? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.md)<br>
[General information on tests >](../learningresources/General_Information_on_Tests.md)<br>
[The Test editor >](Test_editor_QTI_2.1.de.md)<br>
[Question types >](../learningresources/Test_question_types.md)<br>
[Configure test questions >](Configure_test_questions.de.md)<br>
[Configure test learning resources](Configure_tests.de.md)<br>
[Test learning resource settings >](Test_settings.de.md)<br>
[Archive test results >](../learningresources/Course_Element_Test.md#archive)

[To the top of the page ^](#test_export)

