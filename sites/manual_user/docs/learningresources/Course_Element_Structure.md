# Course Element "Structure" {: #course_element_structure}

## Profile

Name | Structure
---------|----------
Icon | ![Structure Icon](assets/structure.png){ class=size24 }
Available since | Release 1
Functional group | Knowledge transfer
Purpose | Structuring of the menu into chapters, collection of assessments of all course elements subordinate to the structure element
Assessable | yes
Specialty / Note | Generation of automatic overviews

Use this course element to organize and structure your course elements and/or to clearly separate areas. For example, create an area for communication, one for course activities and one for content.

The course element Structure offers, among other things, an automatic overview of course elements subordinate to it with their short titles, titles and descriptions. The automatic overview is also linked to an automatically generated performance overview with points, status and link to the performance record, provided these have been activated for the course element or the course in general. 

![Leistungsübersicht Strukturbaustein für Teilnehmende in Lernpfadkursen](assets/Leistungsuebersicht_Struktur_Lernpfad1.png)

The concrete setting options depend on whether the course element is used in conventional or in learning path courses.

 **Tabs in learning path courses**

 **![structure tab learnign path courses](assets/structure_tabs_lpc_en.png)**

 **Tabs in conventional courses**

 **![structure tab conventional courses](assets/sturcture_tabs_cc_en.png)**

For more information on the general tabs "Title and Description", "Layout" and "Visibility" and "Access", see [here](../learningresources/General_Configuration_of_Course_Elements.md)

## Tab Overview {: #overview}

The central settings are made in the "Overview" tab.You can choose between four display modes for the course element "Structure" in the tab Overview and thus generate an automatically generated overview, integrate your own HTML page or simply display the first subordinate course element.

* **Automatic overview** generates a list of the subordinate course elements. You can additionally select whether all or only certain course elements are displayed and whether the display should be in one or two columns.
* **Automatically generated overview incl. preview**  also generates a directory of the subordinate course elements, but also displays a preview for some course elements. The exact preview varies depending on the course element. The configuration options for this setting are similar to those for the automatic overview. Furthermore, it can be set whether the preview refers to all course elements or only to structure elements. However, the user does not see a preview for course elements to which he does not (yet) have access.
* **Custom HTML page** allows you to create your own information page instead of the automatically generated overview. Therefore, you can select an HTML page from the storage folder, create a new HTML file or import a suitable file. Text, images etc. can then be added in the OpenOlat HTML editor in a similar way to the HTML page course element. In addition, the "Display content" tab appears and further specific settings for HTML pages can be made.  
* If you select the radio button **«No overview, activate first visible child node»**, the first visible subordinate course element will be displayed instead of an overview. 

!!! info "Info"

    If you have chosen your own HTML page and this contains links to graphics or other files stored in OpenOlat, you must select the option "Allow links in the entire storage folder" under "Security settings". You can also allow coaches to edit the HTML page without access to the course editor.

##  Tab Highscore

Here you can activate and configure the high score display. You can display a congratulation title, a winner's podium, a histogram as well as a highscore list. An anonymized representation is also possible here.

Auch hier ist eine anonymisierte Darstellung möglich. It also contains the tab "[Reminders](../learningresources/Course_Reminders.md)" and can neither be deleted nor moved.


## Tab Badges

If the course owner has activated the assignment of badges under **Administration > Settings > Assessment tab > Badges section**, the ‘Badges’ tab is displayed in the course editor for this course element and a specific badge can be created for this course element.

[To the top of the page ^](#course_element_structure)

---

## Special settings of the course element structure depending on the course type


### Settings for learning path courses

The settings in the tab "Learning path" basically differ from the settings in other course elements. For learning path courses, the course element structure defines whether the sequence of learning steps is sequential (one after the other) or not. There is no specific completion criterion for structure elements.

![Tab Lernpfad für Strukturbausteine](assets/Tab_Lernpfad.png)

Further information on the tab can be found [here](../learningresources/Learning_path_course_Course_editor.md) 

### Settings for conventional courses

#### Tab Score   {: #score}

Conventional courses have the "Points" tab. Here points that were collected in other assessable OpenOlat course elements (e.g. _assessment_, _group/assignment, SCORM learning content, checklist, LTI page, portfolio task_, _test_ ) be added up and a pass/fail result displayed. The summarized results appear when you click on the course element _Structure_ in the current course.

The following settings are possible:

 Calculate **score**: An overview of the assessable elements of your course will appear, which you can take into account when calculating the points. Select either all or specific course elements and OpenOlat adds the respective points. It is also possible to calculate an average value instead of a total. This makes sense, for example, if all course elements have the same maximum number of points. Course elements that do not (yet) contain a rating are not taken into account in the calculation. The calculated value is displayed to the user after the evaluation under "Score".

 Calculate **passing score:** Pass or fail can refer to a minimum score that you define or to passing selected or all assessable course elements.
 If you select  _«As of minimum score»_ , you can enter the minimum score in another field. This refers to the course elements selected above, i.e. on the course element  _Structure_  a _«Passed»_  is displayed, if the total score is greater or equal to the selected minimum score. 
 
 If you select _«Adopt from course element»_, assessable course elements of your course are displayed by means of  **Passed by**. You can now select those whose "Passed" value should result in the "Passed" value of the course element  _Structure_ with a boolean AND-link. I.e. if the course element _Structure_  should show a  _«Passed»_, all selected course elements have to have a  _«Passed»_.

 Calculate **failed score:**  It is also possible to calculate "Failed".

![structue score tab](assets/structure_score_tab.png)

  * As long as the conditions for passed are not reached, the structure is shown as "Failed". 
  * As long as the conditions for passed are not reached _and_ the end date of the course is reached, the structure is shown as "Failed". If the conditions for "passed" have already been fulfilled before the end of the course, passed is already displayed during the course duration.

If certificates of achievement are to be issued for a course, it is necessary to adjust the settings in the "Score" tab accordingly.

For the user, the performance overview is as follows:

![Teilnehmer Leistungsübersicht des Strukturbausteins](assets/Leistungsuebersicht_Struktur_herkoemmlich.png)


!!! note "Note"

    In case you wish to utilize an evidence of achievement or be able to check the Passed status in the Coaching tool, you must check the option  **Calculate passing score?**  in the course root node.


!!! Tip "Hint"

    Use distinct short titles for all of your assessable course elements to be able to clearly distinguish them in the tab "Score."


#### Tab Access
The course element "Structure" and thus its subordinate course elements can be protected with a password.

!!! warning "Attention"

    On the top course element, which is actually also a structure element, _no_ password can be stored in the "Access" tab.


  

