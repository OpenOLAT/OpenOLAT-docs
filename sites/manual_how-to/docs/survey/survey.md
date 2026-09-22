# How can I run a survey at the end of a course? {: #survey}


??? abstract "Goal and content of this guide"

    Have you already created an OpenOlat course?<br>
    For quality control and improvement, you can gather feedback on the course from the participants after the course has ended by having them complete a survey.
    The following guide shows you how to set this up with a course element "Survey".

??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants [ ] Administrators

    [x] Beginners [x] Advanced  [ ] Experts


??? abstract "Expected prior knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)
    * [How do I create a form learning resource? >](../../manual_how-to/create_a_form/create_a_form.md)<br>
    * Set an implementation period for the course
    * Integrate a form into the course
  

---


## What is a survey in OpenOlat? {: #survey_description}

You should distinguish 4 terms:

- **Learning resource "Form"**<br>
A form with several questions is created in OpenOlat as a **learning resource** and stored in the authoring area. This form learning resource can be reused several times in different course elements.

- The **questions** (single choice, multiple choice, text input, rubric, etc.) are compiled by creating and editing a learning resource "Form".

- **Course element "Form"**<br>
A **learning resource** "Form" is inserted into the **course element** "Form". Please do not confuse learning resource and course element. The course element integrates the form at a specific point in the course – for a final survey, therefore, at the end of the course.

- **Course element "Survey"**<br>
A learning resource "Form" is also inserted into this course element. In contrast to the course element "Form", in the course element "Survey" the questions are answered **anonymously** by default. When coaches review the submitted forms, they will find no assignment by name there. (Exception: If you insert input fields for name, first name, etc. in the form learning resource, the survey is of course no longer anonymous. However, the evaluation mechanism in the course element "Survey" is designed for anonymity in principle.)

[To the top of the page ^](#survey)

---

## Step 1: Insert the course element "Survey" into the course {: #step1}

We assume that you have already created a course. There you can insert another course element at the end of the course. If it is to be an anonymous survey, use the course element "Survey". (In the following we assume this course element.) Alternatively, you can use the course element "Form", in which the answers can be assigned to the respective participants.

!!! info "Note"

    Even when using the course element "Survey" (anonymized survey), OpenOlat ensures that participants can only fill out the survey once.

In the course administration, open the **course editor** and insert the course element **"Survey"**. Place it at the end of the course structure so that it appears as a final survey.

After inserting it, the following tabs are available in the course editor for setting up/configuring:

* **Title and description** – general information about the course element
* **Layout** – visual presentation
* **Learning path** (for learning path courses) or **Visibility** and **Access** (for classic courses)
* **Survey** – the central configuration, in which you also integrate the learning resource (see Step 2)

Make the desired settings.

[To the top of the page ^](#survey)

---

## Step 2: Create the form learning resource {: #step2}

!!! hint "Recommendation"

    If you have never created a form for surveys, first read the guide ["How do I create a form learning resource?"](../create_a_form/create_a_form.md). It shows how to compile the questions.

First prepare the form (more precisely: the form learning resource) with the desired questions. You have two options for this:

#### Approach 1: Learning resource -> Course element
a) Create the form learning resource in the authoring area<br>
b) Insert the learning resource into the course element

#### Approach 2: Course element -> Learning resource
a) In the course editor, select the course element and there the tab "Survey".<br>
b) Click the button "Choose, create or import".<br> 
A list of already existing learning resources of which you are the owner is displayed.<br>
There you can select one or create a new form learning resource with the button above the list.<br>
This takes you to the editor of the form, where you can create the questions.<br>
As soon as the learning resource is saved, it is also displayed in the authoring area.

!!! tip "Hint"

    For a final survey on course quality, **single choice questions** (which force a clear position) or **rubric elements** (traffic-light/scale system) are often suitable. This keeps the effort for the participants low.

[To the top of the page ^](#survey)

---

## Step 3: Insert the form learning resource into the Survey course element {: #step3}

If you proceeded by first selecting the course element and then creating the learning resource (Step 2, Approach 2), then the form learning resource is already inserted into the course element and this step is omitted.

If you first created the form learning resource in the authoring area (Step 2, Approach 1), then the learning resource still has to be integrated into the Survey course element.

- Open the **course editor** and select the **course element** with your final survey.
- Select the **tab "Survey"**.
- With the **button "Choose, create or import"**, you integrate the form learning resource into the course element. In the overview, all forms of which you are the owner are displayed. Select the desired form.

!!! warning "Attention"

    Once a form has been viewed by at least one participant, it can **no longer be replaced** – the "Replace" button is omitted. If it nevertheless has to be exchanged, create a new course element "Survey" and integrate the desired form there.

[To the top of the page ^](#survey)

---


## Step 4: Set up access to the survey {: #step4}

Should the Survey course element only be visible from a certain point in time?<br>
Should the survey only be fillable from a certain point in time?<br>
Should only certain persons be able to fill out the survey?<br>
Should the survey only be possible once a certain processing status in the course has been reached?<br> 
(E.g. all course elements processed, a test passed, etc.)<br>
Should the course only count as completed once the survey has been filled out as well?<br>
Who should be able to view and evaluate the survey results?

All these questions have to do with access rights, which you control

a) via the **tab "Survey"**<br>
b) via the **tab "Learning path"** (in learning path courses)<br>
c) via the **tabs "Visibility"** and **"Access"** (in classic courses) 


### Step 4 a): Define permissions in the tab "Survey" {: #step4a}

In the **"User rights"** area of the "Survey" tab, you define **who may fill out the survey** and **who may view the results**. Available in each case are:

* the **owners** of the course
* the **coaches** of the course
* the **participants** of the course (all persons in the role "Participant")
* **Guests** (persons without an OpenOlat account)

If you activate the **advanced configuration**, you can make additional settings, e.g. define certain **periods** of participation for certain roles or restrict participation to certain groups. The release of the results can also be linked to a start and end date.

!!! tip "Hint"

    A prerequisite for participation is that the **entire course** is released for the respective group of people. If, for example, the final survey is also to be fillable by guests, the course must include an access offer for guests. Please note: A course release for guests is only possible for classic courses, not for learning path courses.


### Step 4 b): Define permissions in the tab "Learning path" (in learning path courses) {: #step4b}

So that the survey actually acts as a **conclusion**, you may want the survey to only appear or be fillable once the rest of the course has already been processed.

- With activated exception rules in the tab "Learning path", it can be determined very specifically that only certain persons find the survey in the course menu.

- If preceding course elements are configured in the tab "Learning path" so that a "done" must be reached there as "mandatory", the participants can only reach the survey at the end of the course. However, the course element is always visible in the menu.

- In the tab "Learning path" you can select the **completion criterion "Survey finished"**. If, at the same time, the criterion for passing the entire course requires the completion of all or certain course elements (Administration > Settings > Assessment tab), you can thereby make filling out the survey a condition for course completion as well.


### Step 4 c): Define permissions in the tabs "Visibility" and "Access" (in classic courses) {: #step4c}

In **classic/conventional courses**, you define via the tabs **"Visibility"** and **"Access"** who may see or edit the course element "Survey" and when. Via date-dependent rules, the survey can, for example, only be made visible or accessible towards the end of the course.

The procedure for setting the visibility in the conventional course is as follows:<br>
On the Survey element, a rule must be stored in the Visibility tab to define when the element should be visible. In the simple configuration mode this is only possible with absolute dates. To work with relative dates, you have to switch to expert mode. This makes it possible to control that the survey is, for example, only displayed for one week at the end of the course.

1. Open expert mode

- In the course editor, navigate to the "Survey" element<br>
- Open the "Visibility" tab<br>
- Click the "Display expert mode" button

2. Variant a): Create an expert rule: duration after course start

- Add the following expert rule: (today <= getCourseBeginDate(0) + 7d)<br>
This expert rule states that the survey should be visible for 7 days after the course start.
The number of days can be adjusted as desired.

2. Variant b): Create an expert rule: duration after course end

- Add the following expert rule: (getCourseEndDate(0) >= today) & (getCourseEndDate(0) + 7d >= today)<br>
This expert rule states that the survey should be visible for 7 days after the course end.
The number of days can be adjusted as desired.

3. Save

- Save your expert rules and publish your course again.

---

!!! info "Anonymous or personalized?"

    In the course element "Survey", the results are stored **anonymized** by default. A personalized evaluation is possible by adding the element **"Information"** in the form editor – this cancels the anonymity.

[To the top of the page ^](#survey)

---


## Step 5: Set up reminders {: #step5}

Via the reminder tool (Administration > Reminders) you can, for example, send a reminder 3 days after the course end so that the participants fill out the survey.

Add a reminder:

- In the "Administration" drop-down menu, open the item "Reminder"
- Click the "Create reminder" button. A new reminder opens.
- Enter a description
- Add conditions: E.g. "After course end"
- Insert the e-mail subject and text
- Save


[To the top of the page ^](#survey)

---


## Step 6: Filling out the survey by the participants {: #step6}

What the participants see depends on the permissions set in the tab "Survey":

* If a person has the right to fill out the form, they first see the **form**.
* The survey can be filled out **only once** and can **no longer be changed** after submission. If the form is not yet to be submitted, the **"Quick save"** option is available.
* If the person is authorized to fill out but **not** to see the results, the message appears after filling out: *"You have already finished this survey. Thank you for your participation."*
* If the person is also authorized to see the results, the **statistics overview** appears directly at the Survey element after filling out.
* If a person is authorized neither to fill out nor to view the results, the message **"No access"** appears.

!!! warning "Attention"

    If participants are currently running the survey but have not yet completed it, their results will be lost if the form is changed during this time.


[To the top of the page ^](#end_of_course_survey)

---

## Step 7: Evaluate the results {: #step7}

When they click on the course element "Survey", course owners and all coaches of the course are shown the following tabs:

* **Overview**: Number of persons who have filled out the questionnaire, submission period, and average processing time. Depending on the question type, further key figures are listed.
* **Tables**: The individual questions and answers, and for rubrics additional statistical evaluations. Free texts can be downloaded as an Excel table.
* **Diagrams**: Graphical representation of the individual questions as bar charts with statistical data such as median, variance, and standard deviation.
* **Individual forms**: Access to each individual (anonymously) filled-out form.

The contents of all tabs can be **printed** or downloaded as an **Excel table** or **PDF**.

!!! info "Further ways to access the evaluation"

    You will find the same evaluation in the menu `Administration > Questionnaire statistics`. In addition, the results can be saved as part of the **course archiving** – it is even possible to bundle the results of several course elements in one ZIP file.


[To the top of the page ^](#survey)

---

## Subsequent changes to the form learning resource {: #changes}

Once a form integrated in the course has been called up, it can only be changed to a **limited** extent. Texts (e.g. typos) can be corrected, but individual blocks can no longer be moved and no areas can be newly created or deleted. The message *"The resource is already used …"* then appears in the form.

Therefore, plan the content of the final survey as completely as possible before the participants gain access.

[To the top of the page ^](#survey)

---

## Reset the survey {: #reset}

Course owners can delete already filled-out forms via the **3-point menu** of the course element with **"Reset"**. In doing so, **all** already submitted forms of this survey are deleted.

Resetting **individual** forms is **not** possible in the course element "Survey", since submission is anonymous.

[To the top of the page ^](#survey)

---


## Checklist {: #survey_checklist}

- [x] Is the form fully prepared with all the desired questions?
- [x] Is the course element "Survey" placed at the end of the course structure?
- [x] Is the correct form selected in the tab "Survey"?
- [x] Is it defined who may fill out the survey?
- [x] Is it clarified whether the survey should be anonymous or personalized?
- [x] Is the course released for the intended groups of people (incl. guests if applicable)?
- [x] Does the survey only appear at the course end via learning path or visibility/access rules?
- [x] Is it defined who may view the results?

[To the top of the page ^](#survey)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I create a form learning resource? >](../../manual_how-to/create_a_form/create_a_form.md)<br>
[Course Element Survey >](../../manual_user/learningresources/Course_Element_Survey.md)<br>
[Course Element Form >](../../manual_user/learningresources/Course_Element_Form.md)<br>
[The Form Editor >](../../manual_user/learningresources/Form_Editor.md)<br>
[Form Elements >](../../manual_user/learningresources/Form_Elements.md)<br>
[Questionnaire Statistics >](../../manual_user/learningresources/Statistics_Survey.md)<br>
[Forms - Overview >](../../manual_user/learningresources/Form.md)<br>
[Access configuration / Release >](../../manual_user/learningresources/Access_configuration.md)<br>

**Further reading**<br>
[Reminders >](../../manual_user/learningresources/Course_Reminders.md)<br>
[Forms in Courses >](../../manual_user/learningresources/Forms_in_Courses.md)<br>
[Learning path course - Course editor >](../../manual_user/learningresources/Learning_path_course_Course_editor.md)<br>
[Authoring - Overview >](../../manual_user/area_modules/Authoring.md)<br>
[Access configuration / Release >](../../manual_user/learningresources/Access_configuration.md)<br>
[Course administration - Archiving & Reports >](../../manual_user/learningresources/Course_Archiving.md)<br>


[To the top of the page ^](#survey)

