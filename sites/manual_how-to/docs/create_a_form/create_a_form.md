# How do I create a form learning resource?

## 1. What is a form in OpenOlat?

An OpenOlat form is a page that can be filled out interactively by users. Typically, questions are to be answered by ticking something or entering an answer as text.

The information can be stored anonymously or on a personal basis.

Authorized persons have access to the information provided and can call up (collective) evaluations.

---

## 2. Course element and learning resource

An OpenOlat course is composed of course elements. Most course elements are containers into which a learning resource is inserted.

![graphic_course_learning_resource_form_v1_en.png](assets/graphic_course_learning_resource_form_v1_en.png){ width=300px class="lightbox" }

**Attention!**<br>
There is a form **learning resource** and a form **course element**. These two are to be kept apart. A form learning resource can be used in different places in OpenOlat (see next section).

This tutorial describes how to create the form **learning resource**.
There are further instructions for using the learning resource in different course elements.

!!! tip "Note"

    In previous OpenOlat versions, form learning resources were called **questionnaires**. They were based on the QTI 1.2 standard, which is now no longer supported.
	
---

## 3. Where are form learning resources used?

![graphic_5_forms_v1_en.png](assets/graphic_5_forms_v1_en.png){ width=400px class="lightbox" }

a) Form learning resource in **course element Form**.

See more at 

b) Form learning resource in **course element Survey**.

See more at 

c) Form learning resource in **course element Assessment**.

See more at 

d) Form learning resource **in a portfolio**

See more at 

e) Form learning resource **Stand alone**

See more at 

 	
---

## 4. What is a form capable of?

<h3> a) How does a form look like?</h3>

Various question types are available in forms:

* Rubric 
* Single selection
* Multiple selection
* Text input
* File upload 

Depending on the objective, forms can be designed quite differently with it. Here is an example in participant view:

![form_lecturer_evaluation_v1_en.png](assets/form_lecturer_evaluation_v1_en.png){ class="shadow lightbox" }

<br>

<h3> b) What does a form consist of?</h3>

Each form consists of a page with one or more questions or other elements (e.g. title). The individual elements can be selected in the editor and then be edited. (Partially popups with setting options for this are displayed).

![form_lecturer_evaluation_editor_v1_en.png](assets/form_lecturer_evaluation_editor_v1_en.png){ class="shadow lightbox" }

<h3> c) How does a form work? </h3>

If participants have entered a response in the form, the entries are saved per participant.<br>
Exception: An anonymous survey was created.

The answers can be viewed by authorized persons.<br>.
Who is authorized can be configured, see "8. Configure form".

If a coach clicks on exactly the same course element with form in the course, he will not see the form at first (like the participant), but an automatically generated report. For the details, the individual forms can be accessed.<br>

![form_lecturer_evaluation_par_c_v1_en.png](assets/form_lecturer_evaluation_par_c_v1_en.png){ class="shadow lightbox" }

!!! info "Question rules"

    A **branch** is also possible via **question rules**: "If question xy is answered this way, then ..."

    You can find the icon for creating the rules in the header of the form editor.

    ![form_question_rules1_v1_en.png](assets/form_question_rules1_v1_en.png){ class="shadow lightbox" }


---

## 5. Create/edit forms

A **special editor** is available for creating form learning resources. It can be called from different places:

<h3>a) Authoring > create new form </h3>

You can create a form learning resource directly in the authoring area. Subsequently, you can access this prepared form learning resource when editing a course and include it in a course element.

![form_learning_resource_new_v1_en.png](assets/form_learning_resource_new_v1_en.png){ class="shadow lightbox" } 

<br>

<h3>b) Authoring > tab "My entries" > select avaliable form > edit</h3>

Does the form learning resource already exist but is still empty? Since we then edit a form**learning resource**, it can be found in the authoring area under the tab "My entries". (Only courses are listed under "My courses".) Use the filters to search in large databases.

To edit, click on the title or on the edit icon or on the 3 dots at the end of the line.

![form_learning_resource_edit_v1_en.png](assets/form_learning_resource_edit_v1_en.png){ class="shadow lightbox" } 

<br>

<h3>c) Course editor > course element > tab for learning content (e.g. tab "Survey") > button "create form" </h3>

If you have inserted a course element in the course editor (e.g. the course element "Survey"), then a learning resource must be inserted there under the tab "Survey". If no form learning resource is prepared, a new form learning resource can also be created directly here.

![course_editor_survey_without_form_v1_en.png](assets/course_editor_survey_without_form_v1_en.png){ class="shadow lightbox" } 

<br>

<h3>d) Course editor > course element > learning content > edit</h3>

If a form learning resource is already included in the course element, the editor for form editing can also be opened from the course editor.

![course_editor_survey_form_edit_v1_en.png](assets/course_editor_survey_form_edit_v1_en.png){ class="shadow lightbox" } 


!!! tip "Hint"

    Since the learning resource form can be used in many different ways, it makes sense to consider the later use already when assigning the title, e.g. to prefix it with a suitable abbreviation. This makes it easier to find and assign the learning resource later.

!!! tip "Hint"

    When you create a brand new form learning resource, you will be taken to the settings screen after the title entry prompt.
    Here you can optionally make settings right away, e.g. store a license. However, you can also access it again at any time later. For more information, see "7. Configuring the form"


!!! info "Note"

    If a form has already been used (filled in by participants), there are restrictions on editing. (See below: 9. Modify forms).


---

## 6. Designing forms in the editor.

Once you have opened the form editor by clicking on "Edit content", you can first insert a new **layout**. <br>
A layout here means a **grid**. You can insert several such layouts one after the other.

![form_editor_1_v1_en.png](assets/form_editor_1_v1_en.png){ class="shadow lightbox" } 
![form_editor_3_v1_en.png](assets/form_editor_3_v1_en.png){ class="shadow lightbox" } 

<br>

The content can now be inserted into the fields of the layout (title, single choice questions, etc.).

If you want to change the layout afterwards, you can open the selection tool again at any time by clicking on the small gear.

![form_editor_4_v1_en.png](assets/form_editor_4_v1_en.png){ class="shadow lightbox" } 

<br>

In the example below, the layout has been changed from two columns to one column.

Now add titles, paragraphs (sections) and the different questions. It is best to start with a title and add a short introductory text with the "Paragraph" element to inform the user accordingly.

![form_editor_6_v1_en.png](assets/form_editor_6_v1_en.png){ class="shadow lightbox" } 

<br>

In each case, click "Add Content" and then use the options provided.<br>.
For example, for a "Title" element.

![form_editor_8_v1_en.png](assets/form_editor_8_v1_en.png){ class="shadow lightbox" } 

For a "rubric" element, the options are much more diverse. However, the same principle of procedure always applies:

* Select an element.
* The displayed options apply to the currently selected element.

Explore the many options available!

![form_editor_11_v1_en.png](assets/form_editor_11_v1_en.png){ class="shadow lightbox" } 

<br>

<h3>Finish editing </h3>

* Repeat the process until the form is completed.
* As an alternative to the "Add content" button, you can also click on the icon with the 3 dots for content that has already been added and then select "Add before" or "Add after". You will see the selection of all elements again.
* If you want to use recurring elements, you can also duplicate them.
* If you want to change the order of the elements, you can simply drag and drop them.

When you are done **close the editor by clicking on the title of the form in the bread crumb navigation**. The form is now saved and you will see the form from a user's perspective.

---

## 7. Testing forms

To test a form as an author, switch to the participant view:

![form_role_change_v1_en.png](assets/form_role_change_v1_en.png){ class="shadow lightbox" } 

<br>

!!! warning "Limited editing possibility after data entry"

    When others (non-owners) test, their entered data is saved and a form can only be changed to a limited extent afterwards. This prevents subsequent manipulation.
    
    If others have already entered data into the form, it is best to create a copy of the learning resource or course element and continue working with it.

<br>

!!! tip "Hint when a 'Not accessible' appears"

    If you as an author have published a course (left the course editor), it often happens that the course element with the form learning resource is not accessible.
    
    Often it is because authors are not allowed to fill in the form themselves according to the preset configuration. (Because they are owner but not participant).
    
    You can get around this by switching roles to the participant view in the editor.

---

## 8. Configure forms

<h3>Where are configurations done?</h3>

Already when creating a new form learning resource you get to the settings after specifying a title. There you can configure the learning resource.
Often you skip these input fields at first. The settings can be called up again at any time and edited.

You have also made settings when creating the questions. You have configured individual questions. The configurations can therefore be made at different levels:

![graphic_configuration_level_v1_en.png](assets/graphic_configuration_level_v1_en.png){ width=450px class="lightbox" }


**Configuration of the course:**<br>
Authoring > select the learning resource > Administration > Settings

**Configuration of the course element:**<br>
Admninistration > Course editor > select the course element > settings in the tabs

**Configuration of the learning resource:**<br>
Authoring > select the form learning resource > Administration > Settings

**Configuration of a question:**<br>
Open form in the form editor > switch to the edit mode by clicking an element > related options appear 

<br>

<h3>What can be configured?</h3>

A complete enumeration of all configuration options across all levels would be too extensive at this point. The main options concern

* the appearance of the form and the questions
* who may fill out the form
* in which period the form can be filled in
* whether the information is collected anonymously or personalized 
* who may see the entries and evaluations
* ...

!!! Info "Anonymous or personalized?"

    You can have forms filled out anonymously or with the name.
    By default, no personalized information is recorded. By adding an element "Information" the anonymity is removed and a personalized evaluation is possible.
    ![formular_editor_12_v1_de.png](assets/formular_editor_12_v1_de.png){ class="shadow lightbox" } 


!!! tip "Note on Share"

    If you want to use the form in course elements, you do **not** need to set up the tab "Share" of the learning resource Form any further. Setting up the tab "Share" is primarily relevant if you want to use the learning resource stand-alone.

!!! tip "To note when the learning path is used"

    Are you using the learning path? If yes, make sure that the configuration of preceding course elements or the top course node does not undesirably restrict processing. E.g. by sequential learning steps or if the preceding course element must be worked off compellingly, before one arrives at the form.

---

## 9. Modify forms

As soon as a form learning resource has been included in a course element and a course participant has filled in the form, data exists.
However, this also means that the form must not be changed after the first use. This would otherwise allow any subsequent manipulations.

**Once a form has been included and called up in the course, the form can therefore only be changed to a limited extent.**

**No longer possible** is, for example, the addition of further questions or question rules.

**Possible** is e.g. still the change of the column titles:

* In the form editor, click the relevant question to edit it.
* Select the "Advanced" tab in the inspector popup.
* Change the column title of the selected question.

![form_restricted_edit_v1_en.png](assets/form_restricted_edit_v1_en.png){ class="shadow lightbox" }

---

## Examples

<h3>Example 1: Teaching quality survey</h3>

Characteristics:

* often Single Choice
* anonymous


<h3>Example 2: Employee survey</h3>

Characteristics:

* personalized
* often text input, e.g. personal goals of the employees
* less questions with answer type correct / wrong

<h3>Example 3: Customer satisfaction survey</h3>

Characteristics:

* often traffic light system, as it simplifies the response and means little effort for customers

