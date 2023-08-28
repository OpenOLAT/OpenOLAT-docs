# Course Element "Test" {: #course_element_test}


## Profile

Name | Test
---------|----------
Icon | ![Test Icon](assets/test.png){ class=size24 }
Available since | 
Functional group | Assessment
Purpose | Course element for integration of a learning resource test into a course
Assessable | yes
Specialty / Note |



The course element "Test" integrates tests into a course. A test in a course
is used to assess achievements and includes various question types. Depending
on the choice of question types, it is evaluated automatically or manually.
OpenOlat uses the IMS-QTI 2.1 format for tests, which allows exchange with
other test systems and learning management systems that also support this
standard.

If you have not selected any test yet, there will be a message saying _No file
chosen_ under the tab Test configuration. Click on "Choose, create or import
file" to add a test to the course element, or to create a new test,
respectively. In case you have already selected a test the name of this
learning resource will be displayed after _Selected file_. Click on the name
to open a preview of the test. Click on "Replace file" if you would like to
exchange the learning resource with another one. Further information can be
found in the chapter "[Creating Tests](../learningresources/Configure_tests.md)".

The two main tabs for test configuration are "[Test configuration](../learningresources/Tests_at_course_level.md)" and " **Options** ".

The settings under "Options" are initially being copied from the options of
the learning resource. However, the options can be adjusted if needed. To do
so, open the tab "Options" and click on "Adjust configuration". You may now
set a time limit, limit the number of attempts, allow guests to do the test,
choose from various display options, etc. If the option "Show question title"
is not selected while menu navigation is allowed, the navigation will only
show "anonymised" titles, not the real titles.

Furthermore, you can set up an information text (HTML page) which will be
visible at the test start page as "Information", above the "Start" button. To
add a file go to the tab "Options" and click on "Select page" or "Create page
and open in editor". You can replace the file later if needed.

Once you have selected a file, the security setting field is added to the
display and you can allow links to files in the storage folder. This is
useful, for example, if you want to link to other HTML files or graphics.
However, this setting also means that experienced course participants can view
the entire folder of the course.

Any test linked to a course can only be edited in your test-editor as long as
there are no users launching and taking it. After that only typing errors can
be corrected.

!!! attention

    In case participants are taking a test at that moment all their
    results will be lost since that test is not complete. All results achieved between replacing and publishing a test will be lost as well.

The test results of the participants will be personalised.