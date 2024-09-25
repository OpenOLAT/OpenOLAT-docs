# Course Settings {: #course_settings}

Under **Administration > Settings** you can make configurations that affect the course as a whole.

![course_settings_menu_v1_de.png](assets/course_settings_menu_v1_de.png){ class="shadow lightbox" }

!!! info "Notes"

    Every [learning resource](../learningresources/index.md) has a "Settings" menu, not just courses.

    The settings of conventional and [learning path courses](../learningresources/Learning_path_course.md) vary slightly.

    You can use the "Info", "Metadata", "Implementation" and "Release" tabs to specify information that will be visible in the [Course info page](../learningresources/Set_up_info_page.md).


## Tab Info {: #info}

![course_settings_tab_info_v1_de.png](assets/course_settings_tab_info_v1_de.png){ class="shadow lightbox" }

Here you define information about the course or learning resource. This includes:

* Title
* Identifier (An external identifier that is displayed in the course overview. E.g. the name from the course catalog or a printed course catalog).
* Teaser (text line/term)
* Course description
* Description of the learning objectives
* Prerequisites
* Requirements for a certificate
* Cover picture
* Teaser movie

This information is also visible to interested parties without course access under (course) info. 
The learning resource appears under the title defined here in the alphabetical course list and is relevant for inquiries via the search mask.

[Details about the **info page** >](../learningresources/Info_page.md)<br>
[Details about the **Set up of the info page** >](../learningresources/Set_up_info_page.md)<br>
[To the top of the page ^](#course_settings)


## Tab Metadata {: #metadata}

![course_settings_tab_metadata_v1_de.png](assets/course_settings_tab_metadata_v1_de.png){ class="shadow lightbox" }

Metadata contains keywords that describe the course. The metadata can be used to make your course easier to find, for example. They are optional and do not have to be filled in.

Metadata of a course are

* Type of the learning resource (in this case: course)
* ID of the course
* Creator of the course
* Author/name of the teachers of the course
* Subject areas (from the taxonomy)
* Implementation format (blended learning, self-study, ...)
* Main language
* Estimated time required for processing
* License

[More about **Meta data** >](../basic_concepts/Full_Text_Search.md#metadata)<br>
[To the top of the page ^](#course_settings)


## Tab Execution {: #Execution}

![course_settings_tab_execution_v1_de.png](assets/course_settings_tab_execution_v1_de.png){ class="shadow lightbox" }


Here you can

* define the implementation period of the course,
* switch on the "[Lesson and absence management](../learningresources/Lectures_and_absences.md)" and configure it further (if activated by the administrator),
* convert existing conventional courses into learning path courses
* or for [Learning_path_courses](Learning_path_course.md) define how the learning progress is calculated, based on the number of course elements or on the duration of the course elements.

[To the top of the page ^](#course_settings)


## Tab Share {: #share}

![course_settings_tab_share_v1_de.png](assets/course_settings_tab_share_v1_de.png){ class="shadow lightbox" }

In the "Release" tab, you define how and for whom a course or learning resource is released.

* Whether access is only possible for selected members, the course itself can be selected and booked or access is completely open
* When participants can withdraw from the course
* Whether only administrative roles of a specific organizational unit are granted access
* Whether and how other authors can access the course
* Whether external OER catalogs and search engines receive information
* Whether an offer is made in the catalog for the course and if so, which one
* Ob der Kurs auch von einem anderen LMS aus via LTI genutzt werden kann

[Details about the **Share** >](Access_configuration.md)<br>
[To the top of the page ^](#course_settings)


## Tab Catalog (only applies to catalog version 1) {: #catalog}

![course_settings_tab_catalog_v1_de.png](assets/course_settings_tab_catalog_v1_de.png){ class="shadow lightbox" }

The "Add to catalog" button can be used to enter the learning resource in the catalog and assign it to one or more predefined categories. To enter the course or learning resource in several catalog areas, the step must be repeated. All catalog entries then appear here in the "Catalog" tab and can also be removed here.

The entire OpenOlat [catalog (version 1)](../area_modules/Courses.de.md) can be viewed by all users in the "Courses" menu.

Only enter your courses in the catalog once they have been completed and should be visible to users.

[To the top of the page ^](#course_settings)



## Tab Terms of use {: #disclaimer}

![course_settings_tab_disclaimer_v1_de.png](assets/course_settings_tab_disclaimer_v1_de.png){ class="shadow lightbox" }

Here

* freely definable course-related **terms of use**
* and a course-related **privacy policy** 

can be activated and stored. If a person starts the course, they must first accept the conditions, otherwise access to the course is not possible.

In the [Member management](../learningresources/Members_management.md) you can see in the "Consents" section which persons have already accepted the conditions.

![Disclaimer form](assets/disclaimer_course.png){ class="shadow" }

[To the top of the page ^](#course_settings)


## Tab Layout {: #layout}

![course_settings_tab_layout_v1_de.png](assets/course_settings_tab_layout_v1_de.png){ class="shadow lightbox" }

Under "Layout" you can

* select a **layout template** for a course,
* define the **course navigation** in more detail
* and define the **style of the course elements**.

Depending on the settings by the course administrator, certain **layout templates** are available, but at least one default template. In addition, you can store your own CSS course templates in the course [Storage folder](../learningresources/Storage_folder.md) and link them in the Layout menu. For example, fonts and colors for texts, headlines, links, the menu and the toolbox can be individually designed and provided with a suitable logo.

In the "**Navigation**" section you can set the visibility of the menu and crumb navigation. In learning path courses it is also possible to set whether the menu icons and the specific learning path are displayed to the user or not. Depending on the linear or flexible scenario, one or the other variant offers itself.

![Lernpfad mit Icons](assets/lp_icons.png){ class="shadow" }
![Lernpfad ohne Pfad und Icons](assets/no_lp_no_icons.png){ class="shadow" }

In the section **"Course element default style"** you can define the default presentation of the course elements and, for example, upload a background image and define the style of the image as well as assign a color category. In the preview you can see the effects.

[To the top of the page ^](#course_settings)


## Tab Toolbar {: #toolbar}

![course_settings_tab_toolbar_v1_de.png](assets/course_settings_tab_toolbar_v1_de.png){ class="shadow lightbox" }

Here you can switch the toolbar in the course header on or off and define which specific individual tools are displayed to course participants in the toolbar.

**Example:**

![course_settings_toolbar_v1_de.png](assets/course_settings_toolbar_v1_de.png){ class="shadow lightbox" }

In this way, tools that are to be continuously available can be accessed from a central location. In addition to course search, glossary and course chat these tools include various [tools](../learningresources/Using_Additional_Course_Features.md) that can also be called up as course element, e.g. calendar, list of participants, e-mail, blog, wiki, forum, and documents folder. In the case of [Wiki](../learningresources/Wiki.md) and [Blog](../learningresources/Blog.md), it is also possible to fall back on learning resources that have already been created. The other tools are similar to the corresponding course elements, but do not offer the further configuration options as they are available in the course elements in the course editor.

The use of the tools in the toolbar is particularly important for linear [Learning path courses](Learning_path_course.md) in order to make important tools available continuously and centrally, regardless of the sequential order of the learning steps.

[To the top of the page ^](#course_settings)


## Tab Assessment {: #assessment}

![course_settings_tab_assessment_v1_de.png](assets/course_settings_tab_assessment_v1_de.png){ class="shadow lightbox" }

In the Assessment tab, you can make settings for

* Assessment methods: total, average, weighted
* Requirements for passing the course 
* The role of coaches in the assessment process
* Activate and configure course certificates
* Activate and configure course certificates and also set up recertification
* Award of badges

![course_settings_assessment_v1_de.png](assets/course_settings_assessment_v1_de.png){ class="shadow lightbox" }


!!! info 

    For conventional courses, only the settings for evidence of achievement, certificates and badges are available in the evaluation table.  The configuration for passing the course is done in the course editor on the top course element in the "Score" tab. There is no progression for conventional courses.


[For more details >](../learningresources/Course_Settings_Assessment.md)<br>
[To the top of the page ^](#course_settings)

## Tab Options {: #options}

![course_settings_tab_options_v1_de.png](assets/course_settings_tab_options_v1_de.png){ class="shadow lightbox" }

Here you activate as required

* a course-specific [glossary](../learningresources/Using_Additional_Course_Features.md)
* a [resource folder](../learningresources/index.md) for your course
* a special folder for coaches
* To-dos for coaches<br>
If you are a user with an administrative role (learning resource manager, administrator), you will be shown additional special options:
* Invitation to activate external users for course owners with author rights
* activate the "LTI 1.3" release for course owners with authoring rights

[For more details > ](../learningresources/Course_Settings_Options.md)<br>
[To the top of the page ^](#course_settings)