# Form in surveys

The learning resource Form is used in the course element "Survey" in the form of a questionnaire. Course owners can thus include questionnaires in their course and learners can complete the surveys provided. The results are then displayed to course owners and tutors accordingly.

OpenOlat ensures that course participants can only fill out the survey or questionnaire once. By default, the results are stored anonymously. However, personalization is possible by selecting the appropriate form elements [Form Editor](../learningresources/Form_editor_Questionnaire_editor.md).

You can learn how to create forms and integrate them into courses [here](../forms/Three_Steps_to_your_Form.md).

## In the course editor

Go to the course editor and add the course element Survey. After you have added the course element Survey to the course the following tabs will be available in the course editor:

![Survey course editor](assets/Umfrage_Kurseditor.png){ class="shadow lightbox" }

In the tab "Title and description" as well as "Layout" general descriptions and information about the respective course element can be stored and the visual presentation can be defined. In the [tab learning_path](../learningresources/Learning_path_course_Course_editor.md) special settings are defined that apply to learning_path courses, e.g. the completion criterion "survey participated" can be selected.

Conventional courses, on the other hand, have the tabs Visibility and Access. Here you define who can see or edit this course element.

## Tab Survey in course editor

The central configuration is done in the tab "Survey". In the first step, you can either create a new form or select an existing one. In the overview that appears, all forms for which you are the owner are displayed and can be selected simply by clicking on the checkmark and thus added to the course.

![form selection dialog](assets/Formular_auswahlmenue1.jpg){ class="shadow lightbox" }

If you have not yet created a form, you can create a new learning resource form by clicking the "Create" button or import an existing external form. Afterwards, the newly created or imported form will also appear in the list and can be selected.

A newly created form does not yet contain any elements, questions or text fields. These have to be added in the course via "Edit" or alternatively directly in the learning resource in the [Form Editor](../learningresources/Form_editor_Questionnaire_editor.md).

If a form is created directly in the course editor, a new learning resource Form will be created automatically, which can also be found in the [Authoring Area](../area_modules/Authoring.md) under "My entries" and can be included in further courses.

After a form has been selected it can be designed via the link "Edit". If the form has already been set up appropriately, it is no longer necessary to edit it.

![embed survey](assets/Umfrage_Tab.png){ class="shadow lightbox" }

Then you can define who can fill in the survey and who can see the results of the survey. The following options can be selected in each case:

* the owners of the course
* the supervisors of the course
* the participants of the course: All people who are enrolled in the course in the role of "Participant".
* guests: persons without OpenOlat account

If one activates the advanced configuration, even more settings can be made, e.g. certain periods of participation can be defined for certain roles and participation can be defined by certain groups.

Also the results can be released for all these groups and can be linked with a start and end date in the advanced configuration.

!!! tip "Tip"

    However, a prerequisite for editing the survey is that the entire course is also released for the respective group of people. So, for example, if a survey should also be fillable by external persons (guests), the course must also be released for guests in the menu `"Settings" > [Release](../learningresources/Access_configuration.md) "open without booking"`.

If a form is included as a survey in a course, the form can be changed in a limited way in the course via the "edit" button. Texts can be changed but individual blocks cannot be moved or new areas can be created or deleted. In the form the message "The resource is already used..." appears.

!!! warning "Attention"

    Once a form has been viewed by at least one participant, it can no longer be replaced. The button "Replace" is then omitted.

## View with closed course editor

What owners, tutors and participants see when the editor is closed depends on which user permissions have been selected in the Survey tab. If the respective group of persons has the right to fill in the questionnaire (Participation by...), then they will see the respective questionnaire first.  But as soon as the person has filled out the questionnaire himself, the questionnaire statistics overview appears directly at the respective survey module, as long as the results are also visible for the user group.

![Survey Statistics](assets/Umfrage_Kurs.jpg){ class="shadow lightbox" }

If a group of people (e.g. learners) is authorized to fill out the survey but not authorized to see the results, the message will appear after the completion:

![message survey completed](assets/Umfrage_ausgefuellt.jpg){ class="shadow lightbox" }

The survey can be filled out only once and cannot be changed after it is submitted. The user will see a corresponding information. If the questionnaire is not to be sent directly, the option "Save temporarily" can be used.

If a group of people is neither authorized to fill in the questionnaire nor to view the results, the message "no access" will appear.

## Viewing the results of a survey

The following evaluation tabs are available to authorized persons:

**Overview** : Here you can see how many people have filled out the questionnaire, the submission period as well as the processing time. Depending on the question type, other key figures are also listed.

**Tables** : Here you can see the individual questions and answers as well as further statistical evaluations for rubrics. Free texts can also be downloaded as Excel tables.

**Diagrams** : In the tab Diagrams you can see a graphical representation of the individual questions.

**Individual Questionnaires** : Here you have access to the entire completed, anonymous questionnaires of individual persons.  
  
Furthermore, the contents of all 4 tabs can also be printed or downloaded as an Excel table or as a PDF version.

The same evaluation can be found in the menu `Administration > Survey Statistics`.

The results can also be saved via the menu "[Data archiving](../learningresources/Using_Course_Tools.md)" > "Surveys". This is the same file as under "Export" in the course run.

### Reset surveys

Course owners can also "Reset" already completed questionnaires via the link in the 3-point menu of the respective course element. In this case, all questionnaires already submitted for this survey will be deleted. It is not possible to reset individual questionnaires because they are submitted anonymously.

![Reset survey](assets/Umfrage_zuruecksetzen.jpg){ class="shadow lightbox" }

Furthermore, the contents of all 4 tabs can also be printed or downloaded as Excel table or PDF version.
