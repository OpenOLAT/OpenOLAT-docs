# Module Learning resource {: #learning_resource} [:octicons-tag-16:{ title="from Release 20.3 (formerly: Repository)" }](https://track.frentix.com/issue/OO-9185){:target="_blank"}

The Learning resource module includes settings that affect courses and learning resources stored in the authoring area.

![modules_learning_resource_tab_settings_v1_de.png](assets/modules_learning_resource_tab_settings_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#learning_resource)

---


## Section Settings {: #tab_settings}

Activating the first checkbox makes the pre-selection "In Preparation" visible for participants in the "Courses" menu. This has the following effect.

#### Area "In Preparation" under "Courses":

**Participant view when activated**
![modules_learning_resource_tab_settings_section_v1_de.png](assets/modules_learning_resource_tab_settings_section_v1_de.png){ class="shadow lightbox" }

#### Course search {: #course_search}

Course owners can activate [course search](../../manual_user/basic_concepts/Search_in_Course.md) in the course under `(Course) Administration > Settings > Toolbar tab` to search for content within the course.

![modules_repository_course_search_v1_de.png](assets/modules_repository_course_search_v1_de.png){ class="shadow lightbox" }

The availability of this function can be switched on/off globally by administrators in this module. [:octicons-tag-16:{ title="Available from Release 20.3.0 (OO-9185)" }](https://track.frentix.com/issue/OO-9185){:target="_blank"}

[To the top of the page ^](#learning_resource)

---

#### Comment {: #comment}

The course info page can be called up in the header of a course. The comment is "hidden" within it.

![modules_repository_course_info_v1_de.png](assets/modules_repository_course_info_v1_de.png){ class="shadow lightbox" }

An input field for submitting a comment can then be displayed on the info page.

![modules_repository_course_comment_v1_de.png](assets/modules_repository_course_comment_v1_de.png){ class="shadow lightbox" }

The availability of this input field can be switched on/off globally by administrators in this module.

[To the top of the page ^](#learning_resource)

---


#### Assessment

Clickable stars for rating can also be displayed on the info page of a course.

![modules_repository_course_review_v1_de.png](assets/modules_repository_course_review_v1_de.png){ class="shadow lightbox" }

The availability of stars for rating a course can be switched on/off globally by administrators in this module.

[To the top of the page ^](#learning_resource)

---

#### Request membership

If someone opens a course to which they do not have access, a screen with a notice appears. 
There is a button here that can be used to request membership. When clicked, an email is sent to all course owners.

![modules_repository_request_membership_v1_de.png](assets/modules_repository_request_membership_v1_de.png){ class="shadow lightbox" }

This function can be switched on/off globally by administrators in this module.

[To the top of the page ^](#learning_resource)

---


#### Taxonomy
**Use of taxonomy in the catalog** [:octicons-tag-16:{ title="Available from Release 20.3.0 (OO-9214)" }](https://track.frentix.com/issue/OO-9214){:target="_blank"}

Activating taxonomy in the learning resource means that the selected "structure" is available in the catalog. For this to work, the corresponding taxonomy must first be created and integrated.

!!! tip "Prerequisite"
    Various taxonomies can be created under `Administration > Modules > Taxonomy`.


A taxonomy cannot be deselected in this area as long as **it is used in a launcher of the catalog**. Attempting to deselect it shows the message: "The taxonomy is still used in a launcher of the catalogue and therefore cannot be deselected."


!!! note "Module Taxonomy"
    How taxonomies are created and configured.<br>
    [To module Taxonomy >](Modules_Taxonomy.md)

[To the top of the page ^](#learning_resource)

---

### Section "Default settings"

#### Participants may leave {: #allow_leaving_courses}

This option specifies a default setting for all new courses. (Existing courses are not affected by this.) Course participants can then decide for themselves whether they want to leave a course.

The following options are available as the default:

* At any time
* After the course end date or status "Finished"
* Never


!!! tip "Course-specific"
    This preselected setting can be adjusted again on a course-specific basis by course owners: `(Course) Administration > Settings > Sharing tab`

[To the top of the page ^](#learning_resource)

---

### Section "Notification" {: #notification}

OpenOlat can send notifications about events at various points. If someone wants to receive the notifications, a subscription can be set up.

!!! note "Note"
    Notifications about events in the learning resource currently only affect the subscription "*Notify owners about status changes for learning resources*".

#### Subscribers

A) Default setting<br>
Activating/deactivating the subscription determines whether a subscription for the described target group is also set up by default when a new course or learning resource is created in the authoring area. This has no effect on already existing subscriptions.

B) Existing subscriptions can be updated using the "Activate existing subscriptions" and "Deactivate existing subscriptions" buttons.

[To the top of the page ^](#learning_resource)

---


### Section "Default role priority" [:octicons-tag-16:{ title="Available from Release 20.1.2 (OO-8795)" }](https://track.frentix.com/issue/OO-8795){:target="_blank"}

This setting defines the order in which roles are prioritized when a member has multiple roles when accessing the learning resource. The top role in the list has the highest priority. System roles always have a lower priority than member roles.

[To the top of the page ^](#learning_resource)

---


## Access tab {: #tab_accesss}


![modules_learning_resource_tab_access_v1_de.png](assets/modules_learning_resource_tab_access_v1_de.png){ class="shadow lightbox" }


### Section "Access"

#### Access for course owners/coaches

Anyone who is an owner or coach in a course (a learning resource) can always find that course in the Coaching tool.
Here you can choose whether such learning resources can also be accessed under "Courses".


#### Show notice in "Courses"

If this toggle button is activated, course owners/coaches receive notices about the effects of the access setting.

#### Overview of access settings for Sites

Under `Administration > Customizing > Sites`, administrators can configure which menu items (sites) are displayed in the main navigation (header).

Here (under the Learning resource module) it shows what is configured there regarding "Courses" and "Coaching tool". Whether this site should be displayed in the header at all, and for which roles it is visible.

To change the settings, you can switch directly via a link to `Administration > Customizing > Sites` ("Open site settings").

[To the top of the page ^](#learning_resource)
