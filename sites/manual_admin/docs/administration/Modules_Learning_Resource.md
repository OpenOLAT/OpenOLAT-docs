# Module Learning resource [:octicons-tag-16:{ title="from Release 20.3 (OO-9185)" }](https://track.frentix.com/issue/OO-9185){:target="_blank"} {: #learning_resource}

The Learning resource module includes settings that affect courses and learning resources stored in the authoring area.

![Checkboxes for Comment, Rating and Request membership, plus the default setting for leaving and the role priority, Learning resource page in the Modules menu of the system administration](assets/modules_learning_resource_tab_settings_v2_en.png){ class="shadow lightbox" }

[To the top of the page ^](#learning_resource)

---


## Settings tab {: #tab_settings}

The "Settings" tab contains the sections Settings, Default setting, Notification and Default role priority.

### Settings section

Activating the first checkbox makes the pre-selection "In Preparation" visible for participants in the "Courses" menu. This has the following effect.

#### Scope "In preparation" under "Courses"

**Participant view when activated**
![Scope "In preparation" activated, one course in preparation in the list, Courses area](assets/modules_learning_resource_tab_settings_section_v1_en.png){ class="shadow lightbox" }

#### Course search {: #course_search}

The [course search](../../manual_user/basic_concepts/Search_in_Course.md) is configured per course, not in this module. Course owners activate it under `Course > Administration > Settings > Tab "Toolbar"`. The "Course search" button then appears in the toolbar of the course.

![Course search checkbox activated and highlighted, Toolbar tab of the course settings](assets/modules_learning_resource_course_search_setting_v1_en.png){ class="shadow lightbox" }

How course owners activate the course search and the other toolbar tools is described on the page [Using Additional Course Features](../../manual_user/learningresources/Using_Additional_Course_Features.md).

[To the top of the page ^](#learning_resource)

---

#### Comment {: #comment}

The course info page can be called up in the header of a course. The comment is "hidden" within it.

![Course toolbar with the Info page button highlighted](assets/modules_repository_course_info_v1_en.png){ class="shadow lightbox" }

An input field for submitting a comment can then be displayed on the info page.

![Info page of a course with the input field for a comment highlighted](assets/modules_repository_course_comment_v1_en.png){ class="shadow lightbox" }

The availability of this input field can be switched on/off globally by administrators in this module.

[To the top of the page ^](#learning_resource)

---


#### Rating

Clickable stars for rating can also be displayed on the info page of a course.

![Info page of a course with the rating widget of five clickable stars highlighted](assets/modules_repository_course_review_v1_en.png){ class="shadow lightbox" }

The availability of stars for rating a course can be switched on/off globally by administrators in this module.

[To the top of the page ^](#learning_resource)

---

#### Request membership

If someone opens a course to which they do not have access, a notice appears. There is a button there that can be used to request membership. When clicked, an email is sent to all course owners.

![Notice page "You are not a member." with the Request membership button](assets/modules_repository_request_membership_v1_en.png){ class="shadow lightbox" }

This function can be switched on/off globally by administrators in this module.

[To the top of the page ^](#learning_resource)

---


#### Taxonomy
**Use of taxonomy in the catalog** [:octicons-tag-16:{ title="Available from Release 20.3.0 (OO-9214)" }](https://track.frentix.com/issue/OO-9214){:target="_blank"}

Activating taxonomy in the learning resource means that the selected "structure" is available in the catalog. For this to work, the corresponding taxonomy must first be created and integrated.

!!! tip "Prerequisite"
    Various taxonomies can be created in the system administration under `Administration > Modules > Taxonomy`.


A taxonomy cannot be deselected in this area as long as **it is used in a launcher of the catalog**. Attempting to deselect it shows the message: "The taxonomy is still used in a launcher of the catalogue and therefore cannot be deselected."


How taxonomies are created and configured is described on the page [Module Taxonomy](Modules_Taxonomy.md).

[To the top of the page ^](#learning_resource)

---

### Default setting section [:octicons-tag-16:{ title="from Release 10.4 (OO-1811)" }](https://track.frentix.com/issue/OO-1811){:target="_blank"}

#### Participants can leave {: #allow_leaving_courses}

This option specifies a default setting for all new courses. (Existing courses are not affected by this.) Course participants can then decide for themselves whether they want to leave a course.

The following options are available as the default:

* At any time
* After the course end date or status "Finished"
* Never


!!! tip "Course-specific"
    This preselected setting can be adjusted again on a course-specific basis by course owners: `Course > Administration > Settings > Tab "Share"`

[To the top of the page ^](#learning_resource)

---

### Notification section [:octicons-tag-16:{ title="from Release 17.2.4 (OO-6739)" }](https://track.frentix.com/issue/OO-6739){:target="_blank"} {: #notification}

OpenOlat can send notifications about events at various points. If someone wants to receive the notifications, a subscription can be set up. For events in the learning resource there is the subscription "*Notify owner of status change for learning resources*".

#### Subscription

A) Default setting<br>
Activating/deactivating the subscription determines whether a subscription for the described target group is also set up by default when a new course or learning resource is created in the authoring area. This has no effect on already existing subscriptions.

B) Existing subscriptions can be updated using the "Activate existing subscriptions" and "Deactivate existing subscriptions" buttons.

[To the top of the page ^](#learning_resource)

---


### Default role priority section [:octicons-tag-16:{ title="from Release 20.1.2 (OO-8795)" }](https://track.frentix.com/issue/OO-8795){:target="_blank"}

This setting defines the order in which roles are prioritized when a member has multiple roles when accessing the learning resource. The top role in the list has the highest priority. System roles always have a lower priority than member roles.

[To the top of the page ^](#learning_resource)

---


## Access tab {: #tab_accesss}

The "Access" tab contains the sections Access and Status "Finished".

### Access section

#### Access for course owners/coaches [:octicons-tag-16:{ title="from Release 21.0 (OO-9576)" }](https://track.frentix.com/issue/OO-9576)

Anyone who is an owner or coach in a course (a learning resource) finds that learning resource in the Coaching tool. Under "My Courses", learning resources are displayed in which users with the coach role are participants themselves.

#### Show hint in "Courses"

If this toggle button is activated, course owners/coaches receive notices about the effects of the access setting.

![Toggle button Show hint in "Courses" switched on, Access tab in the Learning resource module](assets/modules_learning_resource_tab_access_hint_v1.png){ class="shadow lightbox" }
![Notice box for coaches/owners with the link To the coaching area, Courses area](assets/Modules_Learning_Resource_user_hint_v1.png){ class="shadow lightbox" }

#### Site settings

Whether the sites "My courses" and "Coaching Tool" appear in the main navigation and who sees them can be read in the "Overview of access settings for sites". It shows for each site whether it is enabled and which accounts can reach it, for example "Enabled | Registered users without guests/external users". The page [Area and modules >](../../manual_user/area_modules/index.md) describes what a site is.

Via the button "Open site settings" you go directly to the "Sites" page of the system administration:<br>
`Administration > Customizing > Sites`

There you define the order of the sites in the main navigation and for which roles they are visible. You can also deactivate the site "My courses" there. The Coaching tool cannot be deactivated in the standard configuration, because owners and coaches find their learning resources only there. More on this: [Customizing: Sites >](Customizing.md#sites)

!!! note "Access to the setting"
    Only **administrators** can open this page and make changes.

[To the top of the page ^](#learning_resource)

---

### Status "Finished" section [:octicons-tag-16:{ title="from Release 21.0 (OO-9298)" }](https://track.frentix.com/issue/OO-9298)

Here you define system-wide what access participants have to a course or a learning resource in the status "Finished". This setting is the default for all courses and can be overridden per course.

* **Read-only:** The content is still available to participants in read-only mode.
* **No access:** Participants no longer have access to the content. When they open it, a notice appears referring them to the responsible contact person.

Course owners overwrite the setting for their course under:<br>
`Course > Administration > Settings > Tab "Options"`

[To the top of the page ^](#learning_resource)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[Search in a course >](../../manual_user/basic_concepts/Search_in_Course.md)<br>
[Using Additional Course Features >](../../manual_user/learningresources/Using_Additional_Course_Features.md)<br>
[Module Taxonomy >](Modules_Taxonomy.md)<br>
[Area and modules >](../../manual_user/area_modules/index.md)<br>
[Customizing: Overview >](Customizing.md)

**Further reading**<br>
[Coaching - Overview >](../../manual_user/area_modules/Coaching.md)<br>
[Course Settings - Tab Options >](../../manual_user/learningresources/Course_Settings_Options.md)

[To the top of the page ^](#learning_resource)
