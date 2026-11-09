# General Information {: #general_information}

:octicons-device-camera-video-24: **Video introduction (German)**: [OpenOlat Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>){:target="_blank"}

With OpenOlat courses you map different event formats, for example lectures, seminars, online tutorials or group puzzles. You also implement different types of learning, for example problem-based, cooperative or self-organized learning. For this you use any number of [course elements](../Course_Elements/index.md) in any order and align the course with your didactic concept.

To create courses, you need author rights. You get them from your OpenOlat support center or from the administrators of your OpenOlat instance.

## The course cycle at a glance {: #course_lifecycle}

### 1. Create course {: #stage1}

Create the learning resource Course via `Authoring > Create > Course` and choose the desired course design: "With learning path" or "With learning progress" for a learning path course, "Classic" for a conventional course.

![Entry Course in the opened Create menu, top right](../assets/create_course_16_DE.png){ class="shadow lightbox" title="Authoring area" }

!!! note "Further Information"
    * [Creating Courses](../Creating_Course.md)
    * [My first course](../../../manual_how-to/my_first_course/my_first_course.md)
    * [Creating learning path courses](../Creating_learning_path_courses.md)

### 2. Set up, design, publish course {: #stage2}

You implement your course in the course editor: you select the suitable course elements, create learning resources if necessary and configure everything as desired. You open the course editor via `Course > Administration > Course editor`.

![Entry Course editor in the opened Administration menu](../assets/course_editor.png){ class="shadow lightbox" title="Course toolbar" }

!!! note "Further Information"
    * [Course elements](../Course_Elements/index.md)
    * [Using additional Course Editor Tools](../Using_additional_Course_Editor_Tools.md)
    * [Learning path course - Course editor](../Learning_path_course_Course_editor.md)
    * [Various types of learning resources](../index.md)
    * [General Configuration of Course Elements](../General_Configuration_of_Course_Elements.md)
    * [Course Settings](../Course_Settings/index.md)

### 3. Set up access {: #stage3}

You define the access in the course administration: `Course > Administration > Settings`. The "Share" tab is particularly important here.

![Entry Settings in the opened Administration menu, next to it the status Published](../assets/course_settings.png){ class="shadow lightbox" title="Course toolbar" }

!!! note "Further Information"
    * [Access configuration](../Access_configuration.md)
    * [Course Settings](../Course_Settings/index.md)

In learning path courses, it is partially possible to grant participants time-limited access to a course:

* At the course element level: yes, via `Course > Administration > Course editor > Tab "Learning path"` with a relative date
* At the structure element level: no
* At the top-level node (overall course): no

### 4. Publish course {: #stage4}

Set the status to "Published" in the course toolbar. This makes the course visible to the participants.

![Opened status menu with the values Preparation, Review, Access for coach and Finished, current status Published](../assets/course_state.png){ class="shadow lightbox" title="Course toolbar" }

!!! note "Further Information"
    * [Access configuration](../Access_configuration.md)

### 5. Run and assess the course {: #stage5}

In the assessment tool you assess the participants and give feedback. In addition, you coach the course, for example with posts in the forum or by organising the absences.

![Entry Assessment tool in the opened Administration menu](../assets/course_assessment_tool.png){ class="shadow lightbox" title="Course toolbar" }

!!! note "Further Information"
    * [Course Operation](../Administration/index.md)

### 6. End course {: #stage6}

Once the course is over, set the status to "Finished".

![Status Finished as a brown badge](../assets/course_finish.png){ class="shadow lightbox" title="Course toolbar" }

!!! note "Further Information"
    * [Access configuration](../Access_configuration.md)

### 7. Delete course {: #stage7}

The course is deleted via `Course > Administration > Delete`. Deleted courses are in the "Deleted" tab of the authoring area. In the other tabs, the "Status" filter with the option "Trash" shows or hides them.

![Option Trash in the opened Status filter, together with the Deleted tab](../assets/authoring_filter_status_trash_v1_en.png){ class="shadow lightbox" title="My courses tab in the authoring area" }

!!! note "Further Information"
    * [Access configuration](../Access_configuration.md)

## Tip {: #tip}

!!! tip "Before you create your OpenOlat course"

    First think about what you want to achieve with the course.

    The structure of your course depends on your didactic concept, the goals and the framework conditions. On this basis, you decide whether a conventional course or a learning path course is the right choice for you. If in doubt, choose the conventional course: via `Course > Administration > Duplicate as learning path` you later create a copy of it as a learning path course, provided that the learning path course supports all course elements it contains. The conventional course remains unchanged. This conversion only leads from the conventional course to the learning path course.

    After deciding on a course design, choose the course elements with which you reach your goal and implement your course concept. Bundle content that belongs together so that participants find their way around the course easily. When the structure is clear, prepare the learning content, additional files ([HTML pages, PDF files, CP learning content](../index.md), etc.) and everything else you need for use in the learning platform.

[To the top of the page ^](#general_information)

---

## Role change {: #role_change}

The toolbar shows you in which role you are currently viewing the course. As author of a course, this will be as a rule the "Owner" role. Via the role menu you can switch to the "Participant view" at any time.

![Role menu Owner, opened with the entry Switch to participant view](../assets/Besitzer_TN.jpg){ class="shadow lightbox" title="Course toolbar" }

If you have other roles in the course, these are also displayed and you can switch to the corresponding view.

There is no further distinction between coaches and group coaches or participants and group participants, but the options within the role coach or participant are summarized.

The role change is useful if you want to look at the course from the respective perspective, e.g. as the course owner you want to take on the role of the participant. It is also possible to view the flow of the course elements task, group task, checklist or the participant folder from the participant's point of view.

### Initial role when opening a course {: #initial_role}

Users with administrative rights (such as administrator or learning resource manager) can open courses even though they are not a member of the course. This right corresponds to the role, but interferes if the user is explicitly supposed to be a participant in a course.

Therefore: If a person with administrative rights is a participant in a course, the course is initially always opened in the "Participant" role. (However, the role can be changed as usual.)

This does not apply to course owners or coaches. For these roles, it makes sense to be in the "Owner" or "Coach" role as soon as you enter the course. (You can then switch to the participant view.)


<details>
    <summary>Special case: Behaviour when enrolling in a group (course element "Enrolment")</summary>

    <b>Situation:</b> <br>
    - You create a course with the course element "Enrolment".<br>
    - You switch to the participant view and make an enrolment.<br>
    <b>-></b> OpenOlat then unintentionally switches to the owner role.<br>
    - When switching back to the participant view, the useful warning dialogue ("You are in the participant role") with the option to delete data is no longer displayed.<br>
    - The participant view with warning dialogue is only displayed correctly again once the course has been called up again.
    <br><br>
    <b>Explanation:</b> <br>
    The participant view is implemented in the same way as the course share option "Without booking" - in this view you are not booked into the course member administration.
    The following therefore now happens:<br>
    - If you enrol in a group in the course element "Enrolment", you become a group participant at that moment and are entered in the course member administration.<br>
    - As soon as you have a registered "Participant" membership (course or group or curriculum) in the course, the "Participant view" is no longer available. This is only available if you are not listed as a participant in the course member administration.<br>
    <b>-></b> If I enrol in a group from the participant view, the participant view no longer exists for me, but I am listed as a group participant in the member administration of the course. The role therefore changes from the participant view to the owner role.<br>
    - If you now unfold the selection for the roles, you will now see the role "Participant" listed instead of the participant view.<br>
    - If you unsubscribe from the group (and reload the course), the "Participant" role is removed and the participant view is available again instead.<br><br>

</details>

## Further information {: #further_information}

**Further reading**<br>
[Learning path course - Overview >](../Learning_path_course/index.md)<br>
[Members management >](../Members_management.md)<br>
[Course Administration: Overview >](../Administration/index.md)

[To the top of the page ^](#general_information)
