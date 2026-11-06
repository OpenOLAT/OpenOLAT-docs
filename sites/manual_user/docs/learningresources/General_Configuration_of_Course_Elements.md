# Course elements in the Course editor {: #course_elements_course_editor}

:octicons-device-camera-video-24: **Video Introduction (German)**: [Inserting course elements](<https://www.youtube.com/embed/AJ76e3urdKA>){:target="_blank"}

:octicons-device-camera-video-24: **Video Introduction (German)**: [Configuring course elements](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}


## Overview of the Configuration [:octicons-tag-16:{ title="from Release 18.2 (OO-7496)" }](https://track.frentix.com/issue/OO-7496){:target="_blank"}

The configuration overview shows at a glance how the course and its course elements are set up. It is located in the course editor at the very top of the left navigation.

To adjust a course element, click it and you go directly to its configuration. If you select several course elements, the button "Change configuration" appears. With it, you apply certain changes to all selected course elements. Which changes are possible depends on the course element and the course design.

![Checkboxes for jointly changing display, exclusion from course assessment and learning path fields of several selected course elements](assets/Kurseditor_Konfiguration_aendern.png){ class="shadow lightbox" title="Dialog Change configuration" }

!!! tip "Tip"

    Do not select all columns, but only the ones that give you the overview information you need. This keeps the display clear. In particular, the column "Description" should only be shown if the course elements do not contain long texts. The column "Points" is only relevant for assessment elements. It shows whether awarding points is enabled for the respective course elements.

## Adding Course Elements

Once a course has been created, you can insert any number of course elements. You
can also use several course elements of the same type and nest them as you like. However,
the structure of an online course should always be sensible and didactically
well thought out and keep the usability for the learners in mind.

To add a course element to the course, select "Insert course element" in the course editor and click the desired [course element](../learningresources/Course_Elements.md). The selected course element is added to the left navigation. It is always inserted beneath the course element that was selected or clicked beforehand. If the top element of the course is selected, the new course element is automatically inserted at the end of the course. You can move course elements to the desired position at any time with "Drag&Drop".

If you place the cursor at the desired position before adding the element, you
do not need to move the new element again. In general, all course elements can be moved, duplicated and deleted. How this works is described on the page [Deleting, Moving and Copying Course Elements](../learningresources/Deleting_Moving_and_Copying_Course_Elements.md).

Once the course element has been added, it can be further configured.

## Configuration tabs of course elements

Each course element contains the tabs "Title and description" and "Layout". All course elements of a conventional course additionally have
the tabs "Visibility" and "Access". In contrast, [learning path courses](../learningresources/Learning_path_course.md) additionally have the tab "Learning path".

In addition, there are one or more tabs for the individual configuration of the respective course element.

### Tab "Title and description" {: #desc}

In the tab "Title and description" you describe the course element
in more detail. The field "Title" is mandatory. The "Title in course menu" corresponds to the display name in the left
course navigation and is restricted to 25 characters. Do not use slashes or periods in
either title field. Such special characters can cause problems when archiving courses.

The entry in the field "Title" describes the course element in more detail. A maximum of 75 characters is recommended. The title is also
displayed when moving the mouse over the short title in the course navigation and if you have chosen to display the title in the tab "Layout".

In the field "Description" you can provide further information on the
course element, for example what it is intended for.

You enter further details in predefined fields when you expand the area
"Insert additional information".

In the field "Objectives" you can communicate concrete
learning objectives for an individual course element. This is especially
useful for course elements that are linked to more complex actions or for
structure elements that bundle several other course elements and activities.

In the field "Instructions" you can provide information to the
participants how they should use the respective course element.

In the field "Instructions for the coach" you provide information for all
coaches that is not seen by the participants.

Use as short a text as possible (1-2 words) for the "Title in course menu", otherwise the
left navigation becomes too wide and confusing.

The "Description" is not intended for extensive contents, tasks or other
information. Only the function of the course element is to be explained in more
detail in the description. 3-4 sentences are suitable here as a rule.

In the tab "Title and description" you will also find the ID of the respective
course element and the information you need if you want to set a link to this course element.

![External and internal link for referencing this course element](assets/KB_Link_setzen.png){ class="shadow lightbox" title="Section Set link to this course element" }

**External link:** To link to this course element from another OpenOlat
course or outside OpenOlat, simply use the external link. You can also send
the link by e-mail or integrate it into HTML pages.

**Internal link (does not open in new window):** In order to link from a
course element within the OpenOlat course to this course element, you can set
the internal link as href attribute in the desired HTML page.

You need the ID number in the upper left corner of the field to refer to
another course element in its preconditions (e.g. visibility). Each course
element has its own ID number.

![Id number of the course element highlighted](assets/Baustein_ID.png){ class="shadow lightbox" title="Tab Title and description of a course element" }

### Tab "Layout" [:octicons-tag-16:{ title="from Release 16.0 (OO-5520)" }](https://track.frentix.com/issue/OO-5520){:target="_blank"} {: #layout}

In the tab "Layout" you define which details from the tab "Title and
description" appear in the course view: whether a title is displayed and,
if so, which of the two titles. Furthermore, you define a background image for the
header of the course element here. You can choose between "Course default" (the image
defined in the course settings in the tab "Layout"), "Inherited" and
"Course element specific". The same applies to the style of the background image and the
color category. The background image can be
displayed on the right or on the left as well as full-surface or with a
gradient. Under "Color category", a color can be selected or the color coding
can generally be switched off.

The preview immediately shows how the headings of the configured course element
appear in the course and what the overview of the course element looks like.

![Display, background image and color settings with a live preview of the course element header](assets/Tab_Layoutd.png){ class="shadow lightbox" title="Tab Layout of a course element" }

### Tab "Visibility" and "Access" of conventional courses {: #access}

The Visibility and Access tabs can be used to restrict access to a course
element and all subordinate course elements so that only certain persons have
access to this element. If the restriction is set to access, the course element
is visible to all course members, but only certain persons have access to the
course element. If the visibility is restricted, the course element is neither visible nor
accessible for certain persons.

If a course element is visible but not accessible for participants, it is
recommended to add a corresponding explanation in the tab "Visibility" which
explains the background of the blocked access to all excluded persons of the
course.

In most cases, it is sufficient to restrict either the visibility or the access.

The following settings and restrictions are possible in both tabs:

* Blocked for participants
* Depending on date
* Depending on group
* Depending on assessment
* Depending on attribute
* Only in assessment mode

**Blocked for participants**: All persons who are exclusively registered as
course or group participants do not have access to this course element. This can be
used, for example, if certain areas should (initially) only be visible to
teachers.

**Depending on date**: Here you can define a start and/or end date incl.
time for the visibility or the access to the course element. For example, you can
activate a questionnaire only at the end of the course or make teaching
materials available on a weekly basis.

**Depending on group**: In this way a course element can only be made
available for a certain group. It often makes sense to apply the group
dependency to a structure element and to subordinate all course elements relevant for
this group to it.

**Depending on assessment**: In this way, certain course elements or areas
can be provided depending on other assessable course elements such as tests,
tasks, portfolio tasks, checklists or assessments. You can check for a certain
minimum score or for a "passed" of another course element. For example,
certain areas of the course can only be activated once a certain test has been
passed.

**Depending on attribute**: In this way you make a course element available
only to persons with certain characteristics of their university or
institution, for example only to members of a certain university or field of
study. Each rule consists of an "Attribute", an "Operator" such as "has exactly
the value" or "contains the value", and a "Value". Click "+" to add further
rules. Under "Rules connected with" you define whether all rules must apply
("AND") or whether one is enough ("OR"). The university or institution
transmits the attributes when the person logs in via Shibboleth (AAI). The rule
therefore only applies to persons who log in via Shibboleth. The option only
appears if your OpenOlat instance offers login via Shibboleth and attributes
are set up for it. For the setup, contact your organization. For more
information on the attributes, see the section [Use of AAI Attributes](Access_Restrictions_in_the_Expert_Mode.md#use-of-aai-attributes).

**Only in assessment mode**: If you want certain course elements to be
displayed or accessible only during an OpenOlat assessment situation, select
this setting. For more information, refer to the section [Assessment Mode](../learningresources/Assessment_mode.md).

**Apply rules also for owners and coaches**: In order for a restriction to apply to owners and coaches as well, this option must be checked. If this checkbox is not checked, owners, coaches and administrators always see the course element, regardless of which visibility rules are set.

???+ info "Configuration example for restricting visibility"

    The visibility of a course element is configured "Depending on group" for group "A". (De)activating the option "Apply rules also for owners and coaches" affects the visibility for the different roles as follows:

    Role | :fontawesome-regular-square: Apply rules also for owners / coaches | :fontawesome-regular-square-check: Apply rules also for owners / coaches
    ---------|----------|---------
    Participants Group "A" | :fontawesome-regular-eye: | :fontawesome-regular-eye:
    Coaches Group "A" | :fontawesome-regular-eye: | :fontawesome-regular-eye:
    Participants Group "B" | :fontawesome-regular-eye-slash: | :fontawesome-regular-eye-slash:
    Coaches Group "B" | :fontawesome-regular-eye: | :fontawesome-regular-eye-slash:
    Participants of the course | :fontawesome-regular-eye-slash: | :fontawesome-regular-eye-slash:
    Coaches of the course | :fontawesome-regular-eye: | :fontawesome-regular-eye-slash:
    Owners of the course | :fontawesome-regular-eye: | :fontawesome-regular-eye-slash:

!!! note "Note"

    For people with multiple roles, the access/visibility restrictions take effect according to the currently selected role.

The button "Display expert mode" takes you to an input field where you define a more complex
configuration according to your needs. The syntax is described on the page [Access Restrictions in the Expert Mode](Access_Restrictions_in_the_Expert_Mode.md). It is also possible to first make a
basic setting using the general settings and then extend the syntax in expert
mode. Expert mode offers a wide range of options for linking different
restrictions to each other. For example, it can be configured that a certain
course element is only activated from a certain date and only if two tests
have been passed or if at least 10 points have been reached in a checklist or
if the person is a member of a certain group.

All restrictions on course elements are inherited by subordinate course
elements.

Furthermore the [course element "Structure"](Course_Element_Structure.md) offers the possibility to
store a password. All subordinate course elements will then only be visible to
persons having the appropriate password. That way you can e.g. integrate
additional content within a course that is only available to persons who have
paid for that additional content or activate course elements for certain
levels in the context of gamebased learning.

Learning path courses do not allow these restrictions. If you need these
specific selective releases, you must use a conventional course.

You can find information about the tab "Learning path" of learning path courses on the page
[Learning path course - Course editor](../learningresources/Learning_path_course_Course_editor.md).

## Further information {: #further_information}

**Mentioned on this page**<br>
[Course elements at a glance >](Course_Elements.md)<br>
[Deleting, Moving and Copying Course Elements >](Deleting_Moving_and_Copying_Course_Elements.md)<br>
[Learning path course - Overview >](Learning_path_course.md)<br>
[Access Restrictions in the Expert Mode >](Access_Restrictions_in_the_Expert_Mode.md)<br>
[Assessment management: Assessment mode >](Assessment_mode.md)<br>
[Course Element "Structure" >](Course_Element_Structure.md)<br>
[Learning path course - Course editor >](Learning_path_course_Course_editor.md)

**Further reading**<br>
[Course editor tools >](Using_additional_Course_Editor_Tools.md)<br>
[Course Settings >](Course_Settings.md)

**youtube**<br>
[Inserting course elements](<https://www.youtube.com/embed/AJ76e3urdKA>)<br>
[Configuring course elements](<https://www.youtube.com/embed/SAkzzoOQEoQ>)

[To the top of the page ^](#course_elements_course_editor)
