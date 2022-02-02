#  [Assessing tests](Assessing+tests.html)

Here you will learn how to make assessments for tests using the OpenOlat
"Assessment tool".

Go to the assessment tool, activate the tab "Users" and select a test from the
left overview of the assessment elements of the course.  The table will now
show you various action options as well as all assessable persons for the
test.

![](../../download/attachments/590041/Test_Bewertungswerkzeug.png)

Course coaches and course owners have the possibility via the corresponding
buttons ...

  * view the test statistics,
  * export the results of all displayed learners as zip file,
  * to pull tests that are currently in progress and
  * reset the results of all previous tests.
  * set the task's status to "completed" for all or several selected learners, thus finalizing the assessment.
  * to set the assessments of the task to visible or invisible for all or several selected participants at one go.
  * to extend the time for processing the test.
  * correct the tests question by question ("Correct" button)

In case of tests that contain elements that need to be assessed manually, the
"Grade" button will appear additionally.

![](../../download/attachments/590041/Test_korrigieren.png)

 **Test Statistics:**  Access detailed test statistics for each question of a
test. All learner responses are included.

 **Export results:** Here the complete test results can be exported as a zip
file and thus archived. The title of the zip file shows the name of the test,
the corresponding course and the date and time of the download. The results
download includes a user overview as html page, folders with the respective
user results as well as other files. If test receipt is enabled, it will be
exported as well.

 **Retract tests:** If there are tests that have been started but not yet
submitted, they can be pulled in and thus viewed. Tests can also be pulled in
once after the end of the test run.

 **Grade:** This button can be used to make manual evaluations per test
question. Points can be assigned and comments added here. The option appears
only in case of manual scoring.

 **Validate test receipt:**  If this option is selected, a test receipt is
created after the test is completed, which can be downloaded as an XML file.
It is used to verify the test. The created XML file can additionally be sent
to the participant by mail if the option "Send test receipt by mail" is
activated.

 **Reset all data:  **This resets all data of the current test. This means
that all data of all users including results will be irrevocably deleted. It
is also possible to reset only single tests of certain users. This is done
directly in the respective user settings.

 **Extend:** Here the preset test time can be extended.

### Manual correction of test questions per question

Clicking on "Grade" takes you to the question overview. All questions of the
test are displayed and the respective correction status is shown. This makes
it possible to see at a glance whether all corrections have been made or which
questions still need to be (manually) checked or corrected.

  * Auto: questions that have been corrected automatically by the system
  * Manual: Questions that need to be corrected manually
  * Not corrected: Questions that have not yet been corrected. Hier sollte man aber erst mal prüfen ob für diese Frage auch Antworten eingereicht wurden (Spalte "Beantwortet").
  * Review: Questions that have been marked for further review

![](../../download/attachments/108600728/Test_korrigieren_Fragen%EF%B9%96version=1&modificationDate=1624812122000&api=v2.jpg)

For example, if there was an error during test creation, a certain score can
also be automatically added for a question for all edits, or alternatively,
the score for that question can be set to a certain value.

Two procedures are possible for the **correction process** of the evaluation
per question:

  * Tab Questions: Per question, the answers of all participants (anonymized) are corrected one after the other.
  * Tab User: All questions of the test are corrected one after the other for each participant.

Depending on the selected procedure, you can quickly switch between the
questions or participants using the navigation.

The solution or the correct solution to the question can be folded out if
required.

In the lower area, the correction status of the question is also displayed and
points and a comment can be entered. In case of auto-corrected question types,
it is possible to overwrite the points. The question can also be marked for
further review.

Multiple reviewers can score a test at the same time. If a question is already
being edited by a corrector, it is automatically blocked for others.

In the administration it is possible to define for this correction process
whether the users should be listed anonymously (user 1 , user 2...).

### Manual assessment of test questions per user

Activate the tab "User". Now directly select the desired person to get an
overview of the edits for all course elements. Then navigate to the desired
test to get to the assessment form. Alternatively, you can first go to the
desired test element via the left navigation and then select the appropriate
person from to get to the assessment form and the previous attempts.

In the table with the attempts, the points of an attempt can be displayed
separately differentiated by automatically generated points, manually awarded
points and final points. Configure the displayed columns as needed.

![](../../download/attachments/590041/Test_korrigieren.png)

Adjustments can now be made via the "Grade" link. Click on "Grade". An
overview view of all questions in the test appears. Here you can view the
submission for individual questions and make the manual assessment. Call up
the assessment form by clicking on the name of the question.

![](../../download/attachments/590041/Test_Bewertungswerkzeug1.png)

### Invalidate or cancel tests

Test attempts performed by learners can also be undone. To do this, the
corresponding test of a person is called up and then the option "Cancel" or
"Reset test data" is selected.

![](../../download/attachments/590041/Test_annullieren_zuruecksetzen%EF%B9%96version=2&modificationDate=1627746463000&api=v2.jpg)

When invalidating, a single attempt is marked as invalid. This means that the
attempt continues to appear in the list and can be viewed and even reactivated
by the teacher, but is no longer taken into account as a result for the
learner. If the user has performed several attempts, the next attempt in time
will be considered as the result. However, this does not change the number of
attempts displayed. For example, if a test is limited to three attempts and
the user has made three attempts, no further attempts are available to the
user, even if one or more of the attempts have been cancelled.

If there is only one attempt and it is cancelled, the table display in the
evaluation tool does not change. The cancelled attempt with the associated
points is still displayed.

In contrast to cancelling, "Reset test data" results in all tests being
completely deleted, and the number of tests is therefore set to 0.

  

In addition to the assessment in the assessment tool, individual tests can
also be assessed in the course run with the editor closed. The assessment
options are mostly identical. Only the "Preview" and "Reminders" tabs
supplement the options. The preview shows the user perspective and in the tab
"Reminders" there is the possibility to send a reminder email for certain
conditions e.g. at a certain score, certain number of attempts or at pass/fail
(see also [Reminder](Course+Reminders.html)).

![](../../download/attachments/108600728/Test_kursrun%EF%B9%96version=1&modificationDate=1624810026000&api=v2.jpg)

  

  

