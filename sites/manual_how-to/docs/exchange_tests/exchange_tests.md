# How do I exchange a test? {: #exchange_tests}

??? abstract "Objectives and content of this instruction"

    This guide shows you how to replace a test learning resource in a test course module with another one—and what preparations are necessary if participants have already taken the test. 


??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants

    [x] Beginners [x] Amateurs  [ ] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)
    * ["How do I proceed when creating a test?"](../test_creation_procedure/test_creation_procedure.md)
    * [Assessment tool >](../../manual_user/learningresources/Assessment_tool_overview.md)

---


## What do I need to know before the exchange? {: #situation}

A test **course module** always references a test **learning resource**. When they are swapped, this reference is changed to a different learning resource. The previous test learning resource remains in the system—it is simply unlinked from the course module, and a new test learning resource is linked in its place.

**The main issue:** If participants have already started or completed the test, there is assessment data that is based on the content of the old test (questions, scores). After the update, this data may no longer match the new test. This can lead to inconsistencies in the assessment.

**Example:**<br>
You want to add an extra question to a test. Participants who completed the test before this edit were never able to see the question or earn points for it. Changing questions in a test that has already been submitted by participants constitutes forgery and must not happen under any circumstances. For this reason, authors can no longer modify a test learning resource that has been used, and OpenOlat blocks such changes.

As a rule of thumb, therefore:

* **No participants have taken the test yet:** The transition will be smooth; no preparations are necessary.
* **Participants have already taken the test:** Consider this carefully before making the change. If necessary, data can be reset. If a test learning resource is to be replaced, OpenOlat has a specific process for this that also includes archiving data before the change. 

[To the top of the page ^](#exchange_tests)

---


## Where do I make the exchange? {: #exchange}

This can be done in the **Course Editor**. To do this, you must have the **Course Owner** role or the appropriate permission to edit the course.

To open the course editor, go to:<br>
**Go to Course > Administration > Course Editor > Select Course Element Test > Test Configuration tab**

!!! info "Requirement"

    The new test learning resource must already exist in the system—either created by you, imported, or shared by someone else. You cannot create the test learning resource directly during the exchange.


[To the top of the page ^](#exchange_tests)

---


## Step 1: Check existing test data {: #check_existing_data}

Before replacing the test, you should use the **assessment tool** to get an overview of the existing test data.

1. Open the assessment tool via **Administration > Assessment Tool**.
2. In the left sidebar, select the **Course Element Test** whose test you want to replace.
3. Select the **Participants** button.
4. Check the table to see if any participants have already started or completed the test, and how many (columns **"Attempts"** and **"Status"**).

![exchange_tests_check_data_v1_de.png](assets/exchange_tests_check_data_v1_de.png){ class="shadow lightbox" }

!!! info "Note"

    If no attempts are listed in the "Attempts" column for **all** participants and the status is **"Not started"**, no preparations are necessary. You can proceed directly to step 3.


[To the top of the page ^](#exchange_tests)

---


## Step 2: Should all participants have to take the new test again? {: #reset_data}

Even if only one person has "clicked through" the test "just to try it out", the course element test is already considered "used" and can no longer be modified in terms of structure or content. OpenOlat cannot tell whether the test attempt was serious or not. 

In such cases, the data can simply be reset so that the test learning resource is once again considered "unused" and can be replaced without any loss of data.
To do this, use the **Reset Data** button. You can select the test course module directly or in the grading tool:
**(Assessment Tool >) Select course element Test > Participants tab > Select participants > "Reset All Data" button**

Course owners can also reset only specific tests for certain individuals. 

* To do this, select one (or more, or all) of the names in the list.
* Once at least one name is selected, a "Reset data" button will appear above the list, along with other options. 
* This will then reset only the data for the selected participants. 

![exchange_tests_reset_data_v1_de.png](assets/exchange_tests_reset_data_v1_de.png){ class="shadow lightbox" }

Depending on the course module, the following data will be reset or canceled:

* Progress
* Number of attempts
* Test runs
* Points and success status
* Share rating
* Reminders

!!! warning "Attention"

    Resetting test data is **irreversible**. When you reset the data, an archive file containing the relevant data is created and then downloaded. The archive is also available for download in the participants' performance records.

For more information, see the user manual under
[Reset data >](../../manual_user/learningresources/Assessment_tool_reset_data.md)


[To the top of the page ^](#exchange_tests)

---

## Step 3: Exchange learning resources {: #exchange}

* Open the course editor and select the relevant test course block.
* Select the "Test Configuration" tab.
* You will be notified that the test learning resource is already being used for grading.
* Click the "Replace" button.
* Select, create, or import a new test learning resource.

![exchange_tests_exchange1_v1_de.png](assets/exchange_tests_exchange1_v1_de.png){ class="shadow lightbox" }

Now the old and new test learning resources are displayed side by side, and you can choose between two replacement options:

* **Controlled replacement**
* **Replace only**

![exchange_tests_exchange2_v1_de.png](assets/exchange_tests_exchange2_v1_de.png){ class="shadow lightbox" }


|                   | Controlled exchange |  Replace only  |
| ----------------- | ------------------------ | ------------------------ |
| **Running and paused test runs:** | are withdrawn and marked as invalid | are withdrawn and marked as invalid |
| **Finished test runs:** | are marked as invalid | remain valid |
| **Existing reviews:** | are deleted | remain unchanged |
| **Publication:** | To avoid inconsistent test data, the course module is published immediately | To avoid inconsistent test data, the course module is published immediately   |

[To the top of the page ^](#exchange_tests)

---

## Publish course {: #publish}

Normally, after making changes in the course editor, you must explicitly publish the course and then exit the editor. You still have the option to discard the changes you’ve made.

When replacing a test learning resource, the course no longer needs to be published with the new test course module. Publication occurs automatically and immediately to prevent data inconsistencies.

In this case, the "Publish" step is therefore omitted.

[To the top of the page ^](#exchange_tests)

---


## Further information {: #further_information}

[Create tests >](../../manual_user/learningresources/Test.md)<br>
[Reset data >](../../manual_user/learningresources/Assessment_tool_reset_data.md)<br>

[To the top of the page ^](#exchange_tests)

---

## Checklist {: #checklist}

- [x] Is it absolutely necessary to replace the test learning resource?
- [x] Could the course or the test module also be copied? (So that we have another unused learning resource.)
- [x] Has the new test learning resource already been created in the authoring area?
- [x] Have participants already taken the previous test? Is data available?
- [x] Is it possible to reset the test data?
- [x] Should existing test data be completely deleted?
- [x] Has an archive of the data collected so far been created?
- [x] Was the archive file saved in the correct location?
- [x] Should the course participants be informed about the new version of the test?

[To the top of the page ^](#exchange_tests)
















