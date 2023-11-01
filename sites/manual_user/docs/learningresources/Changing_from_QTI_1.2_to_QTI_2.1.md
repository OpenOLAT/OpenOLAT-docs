# Changing from QTI 1.2 to QTI 2.1

!!! warning "Attention"

    Since OpenOlat version 15.0 the old QTI 1.2 format is no longer supported. As of OpenOlat 16.0, **conversion** of QTI 1.2 tests is **no longer possible**!

## Converting QTI 1.2 tests

1. Export the QTI 1.2 test from OpenOlat version 16
2. Import the exported QTI 1.2 test into an OpenOlat version 15.x
3. Convert the test

    To convert a QTI 1.2 test, open the test learning resource in the authoring area and select `Administration > Convert to QTI 2.1` from the menu. This will save a copy of the old test in the new format. Thus, both test versions are available under "My entries".

    ![Convert tests](assets/test12_export.png){ class="shadow" }

4. Export the newly created QTI 2.1 test from OpenOlat 15.x.
5. Import the QTI 2.1 test back into OpenOlat 16

## Convert single questions

Beside tests, single questions can also be converted. Questions are converted in the question bank.

1. Open the [question bank](../area_modules/Question_Bank.md)
2. Mark the questions (in the format IMS QTI 1.2) you want to convert
3. Confirm with the button "Convert"

![Convert question](assets/EN_convert_question.png){ class="shadow lightbox" }

Converted questions will be saved under "My questions".

If you have put some questions to lists or shares as well, the will be found there still in the format QTI 1.2. If you want to have the questions also there in the new format QTI 2.1 you need to add the questions again to the list or share manually. The old questions can be removed to avoid a doubled appearance.

## Check converted tests

!!! tip "Tip"

    After converting please check the test configuration to make sure, that the test is shown as you desired.

The following points need to be considered when converting questions or tests from QTI 1.2 to QTI 2.1:

* If a hint is added, it will be shown in QTI 2.1 anyway. It cannot be hidden. (Shown as button, which can be opened by test participants)
* If a feedback is filled in, it will be shown in QTI 2.1 anyway. It cannot be hidden.
* The description on test level will not be converted. In QTI 2.1 no description can be added to the test level.
* The section description is converted. In QTI 2.1 it will be shown above each question.
* The question description is not converted and will not be shown anywhere in the QTI 2.1 questions, as QTI 2.1 question items do not have a description.
* Time limits are available in QTI 2.1 only for the whole test. Time limit on the level of questions or sections are therefore not converted.
* For gap text questions alternatives can be added. The separation of these alternatives has been done by semicolon in QTI 1.2 and will be done be comma in QTI 2.1. During the conversion, the separation sign is changed.

## Replace QTI1.2 tests in the course

If the learning resource has been embedded in a course as test, it will not be exchanged automatically.

If you want to run the test in the new format QTI 2.1 you can:

* create a new course element test where you embed the converted learning resource or
* exchange the learning resource in the existing test.

!!! tip "Recommendation"

    If you exchange the existing test all results will be lost. It is thus recommended to create a new course element "test" and limit the visibility/access to the old test.
