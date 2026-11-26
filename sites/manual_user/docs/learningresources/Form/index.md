# Forms - Overview {: #overview}

With a form, you collect information, opinions and ratings in OpenOlat, for example:

* as classic forms (with selection fields or free text entries)
* for online surveys
* as rubric assessment, which rates performance against fixed criteria in levels
* for self-assessment
* or when booking offers in the Course Planner

## Profile

Name | Form
---------|----------
Icon | :o_icon_o_FileResource-FORM_icon:
Available since | Release 11.2 (OO-2329)
Purpose | Collect information, opinions and ratings
In the course | Course elements "Form" and "Survey", as rubric also in "Assessment" and "Task"

## Structure and use {: #structure}

In OpenOlat, a form is a learning resource of its own, that is a content object you manage in the authoring area and use in different places. As an author, you create it in the authoring area: `Authoring > Create > Form`. Whoever creates a form is owner of the form learning resource. Owners, learning resource managers and administrators can edit it.

You open the [form editor](../Form_Editor/index.md) in the authoring area or from a course in which a course element includes the form. In the course, open the course editor for this: `Course > Administration > Course editor`. In the tab "Form" of the course element "Form", click "Edit learning resource"; for the course element "Survey", in the tab "Survey". The button opens the form learning resource. There, select the entry "Form editor" in the menu "Administration": `Form > Administration > Form editor`.

In the editor, you build the form from layouts that define the columns and rows of the page. Into the layouts you insert [elements](../Form_Elements/index.md), for example texts and questions. With [question rules](../Form_Question_Rules.md) you specify that an area of the form only appears once the person filling it in has selected a specific answer.

!!! info "Important"

    There is a learning resource "Form" and a course element "Form". The learning resource contains the form itself, the course element includes it in a course. How the two work together is explained in the guide [How do I create a form learning resource?](../../../manual_how-to/create_a_form/create_a_form.md#step2) in the section "Course element and learning resource".

A form collects answers where you use it: in a course, in a Portfolio 2.0 template or when booking in the Course Planner (see [Places of use](#usage)). When booking in the Course Planner, the form collects the information directly when an offer is booked, without any course. If you open the form learning resource directly, for example by clicking its title in the authoring area, you see the form and can fill it in to try it out. OpenOlat does not save your answers there, and the form cannot be submitted. If you want to collect answers, use the form in one of the places of use, usually in a course, see [Forms in courses](../Forms_in_Courses.md).

## Pages on the form learning resource {: #pages}

These pages describe the form learning resource itself, in the order of the navigation:

Topic | Purpose
---------|----------
[Form editor](../Form_Editor/index.md) | How you open the editor, also from a course element, and how you build a form from layouts and elements.
[Elements](../Form_Elements/index.md) | All content elements and question types you insert into a layout, with their settings.
[Rubric](../Form_Element_Rubric.md) | Have several questions answered or rated on the same rating scale.
[Question rules](../Form_Question_Rules.md) | Show an area of the form only if it matches the selected answer.
[In courses](../Forms_in_Courses.md) | Which course elements let a form collect answers in a course.

## Places of use {: #usage}

You use a form in these places. The manual describes each of them under its own topic:

Place of use | Purpose
---------|----------
[Course element "Form"](../Course_Element_Form.md) | Participants fill in a form once by default, for example as a confirmation before a lab course; OpenOlat assigns the answers to their name.
[Course element "Survey"](../Course_Element_Survey.md) | The members of a course answer an online questionnaire, for example on their satisfaction; OpenOlat saves the results anonymised.
[Rubric scoring](../Forms_in_Rubric_Scoring.md) | Coaches and course owners assess performance in the course element "Assessment" against fixed criteria with a rubric.
[Peer review in the task](../Course_Element_Task/Task_Peer_Review.md#peer_review_rubric) | Participants of a task assess each other's submissions with a rubric form.
[Portfolio 2.0 template](../Forms_in_the_ePortfolio_template.md) | Participants reflect on their work or assess their own performance in an assignment of the template.
[Booking orders in the Course Planner](../../area_modules/Course_Planner_Implementations.md#booking_order_forms) [:octicons-tag-16:{ title="from Release 21.1 (OO-9724)" }](https://track.frentix.com/issue/OO-9724){:target="_blank"} | When an offer is booked, a form collects additional information, for example dietary requirements or prior knowledge.


## Further information {: #further_information}

[Course element "Assessment" >](../Course_Element_Assessment.md)<br>
[Course element "Task" >](../Course_Element_Task/index.md)<br>
[Course element "Group task" >](../Course_Element_Grouptask.md)

[To the top of the page ^](#overview)
