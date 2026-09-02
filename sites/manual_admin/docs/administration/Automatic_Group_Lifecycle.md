# Automatic Group Lifecycle

The group life cycle makes it easy to **automatically** inactivate and then delete unused groups after a certain period of time. A group passes through five stages: creation, active, inactivation, deletion as a marking, and permanent deletion.

![Five stages of the group life cycle, from creation to permanent deletion](assets/automatic_grouplifecycle_v1_en.png){ class="lightbox" }


!!! note "Note"

    The process is similar to the lifecycle management of user accounts and courses.



## Check group status [:octicons-tag-16:{ title="from Release 16.1 (OO-5190)" }](https://track.frentix.com/issue/OO-5190)

Authorized persons (group managers, administrators) receive the additional tab "**Group management**" when they click on "Groups" in the main navigation.

![Three status arrows with their deadlines and the filter row below, Group management tab in the Groups area](assets/automatic_group_lifecycle_groupmanagement_v1_de.png){ class="shadow lightbox" }

By clicking on one of the 3 arrows (phases/status), all existing groups are listed sorted into 3 categories:

* I. Active groups
* II. Inactive groups
* III. Deleted groups

Below the arrows, filters narrow the list down further, for active groups for example "Longer without activity", "To inactivate" or "Within reaction time".

The additional information in the 3 arrows describes the configuration set up by the administrator for this phase.


## Configuration

Administrators can configure the progress of the group life cycle in the system administration under:<br>
`Administration > Life cycles > Groups`

![Menu item Groups under Life cycles highlighted, on the right the status arrows and the first configuration section, system administration](assets/automatic_group_lifecycle_admin_v1_de.png){ class="shadow lightbox" }

The configuration comprises 4 sections:

* **1 Configuration of automatic methods**<br>
  Here you can define groups that are included or explicitly excluded from the automatic methods.

* **2 Inactivation**<br>
  Upon inactivation, the status of the group is set from "Active" to "Inactive" and members can only access the group in read-only mode. Inactive groups can be fully reactivated.<br>
  **Options:**
    * Number of days that a group remains in the "Active" status without activity until it is inactivated
    * Automatic or manual inactivation?
    * Notifications about upcoming inactivation
    * Reaction time
    * If reactivation takes place, waiting time until the next inactivation
    * Notifications about completed inactivation

* **3 Deletion**<br>
  When deleting, all members of the group and the links to courses are removed. All remaining data is retained and can be viewed. The group can be restored.<br>
  **Options:**
    * Automatic or manual deletion?
    * Notifications about upcoming deletion
    * Reaction time
    * Number of days a group remains in "Inactive" status until it is deleted
    * Notifications about completed deletion

* **4 Permanent deletion**<br>
  Permanent deletion removes the group completely.<br>
  **Options:**
    * Number of days a group remains in "Deleted" status until it is permanently deleted
    * Automatic or manual deletion?

The result of the settings made is summarized both in the 3 arrows in the upper part of the configuration screen (for administrators) and in the arrows in the "Group management" tab, which group managers and administrators see under the main navigation in "Groups".

**Example: View for group managers**

![Highlighted example values of the three status arrows: 660, 6 and 2 days, automatic, Group management tab](assets/automatic_group_lifecycle_example1_v1_de.png){ class="shadow lightbox" }

  *  **active:** The group is used and someone has visited it within the set period. (Default value: 400 days without a visit).

  *  **inactive:** The group is inactive. An email is sent (if configured). If no further changes are made to this group, it will be deleted.

  *  **deleted:** In the "deleted" status, the group can be restored. However, not all data can be restored. This group is completely deleted after 2 days.



## Examples of the chronological sequence of a status change

The four examples show the status change automatically or manually, each without and with a reaction time. With a reaction time, a notification is sent at the start of the period; in all cases one is sent at the status change, if configured.

![Four timelines of a status change: automatic or manual, each without and with a reaction time, with focus phase and notifications](assets/Beispielkonfiguration.jpg){ class="lightbox" }



## Exclusion of a group from the group life cycle [:octicons-tag-16:{ title="from Release 17.1 (OO-5887)" }](https://track.frentix.com/issue/OO-5887)

Group coaches have the option of explicitly excluding their group from the automatic methods. This means that all actions in the group life cycle must be triggered manually. You will find the option under:<br>
`Group > Administration > Group Life Cycle`

![Highlighted checkbox Exclude from the automatic methods, below it status and inactivation date, Group Life Cycle tab](assets/automatic_group_lifecycle_groupcoach_v1_de.png){ class="shadow lightbox" }

!!! info "Important"

    If the option is already activated and read-only, the group belongs to a specific group type (externally managed or with included courses), which has already been globally excluded in the system administration under `Administration > Life cycles > Groups`.



## Who receives the notifications?

As soon as an automatic notification is triggered by the set conditions, OpenOlat checks in this order to whom the notification is sent as an email:

1. If the group has group coaches, all group coaches receive the email.
2. If the group has no group coaches but is included in courses, all owners of these courses receive the email.
3. If neither applies, nobody is notified.


![Decision tree of the notification: group coaches, otherwise owners of the courses, otherwise nobody](assets/automatic_group_lifecycle_mailcascade_v2_en.svg){ class="lightbox" }




