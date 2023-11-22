# Automatic Group Lifecycle

The group life cycle makes it easy to **automatically** deactivate and then delete unused groups after a certain period of time.

![automatic_grouplifecycle_v1_de.png](assets/automatic_grouplifecycle_v1_de.png){ class="lightbox" }


!!! note "Note"

    The process is similar to the lifecycle management of user accounts and courses.



## Check group status

Authorized persons (group managers, administrators) receive the additional tab "**Group management**" when they click on "Groups" in the main navigation.

![automatic_group_lifecycle_groupmanagement_v1_de.png](assets/automatic_group_lifecycle_groupmanagement_v1_de.png){ class="shadow lightbox" }

By clicking on one of the 3 arrows (phases/status), all existing groups are listed sorted into 3 categories:

* I. Active groups
* II. Inactive groups
* III. Deleted groups

Below the arrows it is possible to further narrow down the lists (e.g. Active groups - Within response time).

The additional information in the 3 arrows describes the configuration set up by the administrator for this phase.


## Configuration

Administrators can configure the progress of the group life cycle under **Administration > Lifecycles > Groups**.

![automatic_group_lifecycle_admin_v1_de.png](assets/automatic_group_lifecycle_admin_v1_de.png){ class="shadow lightbox" }

The configuration is defined in 4 sections:

* **1 Configuration of automatic methods**<br>
  Here you can define groups that are included or explicitly excluded from the automatic methods.

* **2 Deactivation**<br>
  When deactivated, the status of the group is changed from "Active" to "Inactive" and members can only access the group in read-only mode. Inactive groups can be fully reactivated.<br>
  **Options:**
    * Number of days that a group remains in the "Active" status without activity until it is deactivated
    * Automatic or manual deactivation?
    * Notifications about imminent deactivation
    * Response period
    * If reactivation takes place, waiting time until reactivation
    * Notifications about deactivation

* **3 Deletion**<br>
  When deleting, all members of the group and the links to courses are removed. All remaining data is retained and can be viewed. The group can be restored.<br>
  **Options:**
    * Automatic or manual deletion?
    * Notifications of impending deletion
    * Response period
    * Number of days a group remains in "Inactive" status until it is deleted
    * Notifications of deletion

* **4 Irrevocable deletion**<br>
  Irrevocable deletion removes the group completely.<br>
  **Options:**
    * Number of days a group remains in "Deleted" status until it is finally deleted
    * Automatic or manual deletion?

The result of the settings made is summarized both in the 3 arrows in the upper part of the configuration screen (for administrators) and in the arrows in the "Group administration" tab, which is displayed to group administrators under the main navigation in "Groups".

**Example: View for group coaches**

![automatic_group_lifecycle_example1_v1_de.png](assets/automatic_group_lifecycle_example1_v1_de.png){ class="shadow lightbox" }

  *  **active:** The group is used and someone has visited it within the set period. (Standard 660 days without a visit).

  *  **inactive:** The group is inactive. An e-mail has been sent (if configured). If no further changes are made to this group, it will be deleted.

  *  **deleted:** In the "deleted" status, the group can be restored. However, not all data can be restored. This group is completely deleted after 2 days.

  

## Examples of the chronological sequence of a status change 

![](assets/Beispielkonfiguration.jpg){ class="lightbox" }



## Exclusion of a group from the group lifecycle

Group administrators have the option of explicitly excluding their group from the automatic methods. This means that all actions in the group life cycle must be triggered manually.

**Select group > Administration > Tab "Group lifecycle"**

![automatic_group_lifecycle_groupcoach_v1_de.png](assets/automatic_group_lifecycle_groupcoach_v1_de.png){ class="shadow lightbox" }

!!! note "Note"

    If the option is already activated and write-protected, the group belongs to a specific group type (externally managed or with integrated courses), which has already been globally excluded in the administration.



## Who receives the notifications?

As soon as an automatic notification has been triggered by the set conditions, OpenOlat checks to whom the notification is sent as an e-mail.


![automatic_group_lifecycle_mailcascade_v1_de.png](assets/automatic_group_lifecycle_mailcascade_v1_de.png){ class="lightbox" }




