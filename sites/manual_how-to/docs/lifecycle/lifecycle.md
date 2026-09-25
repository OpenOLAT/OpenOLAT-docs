#  How do I manage lifecycles of groups, courses or user accounts? {: #lifecycles}

??? abstract "Objectives and content of this instruction"

    With these instructions you should

    * know what is meant by lifecycles in OpenOlat,
    * be able to set up life cycle management.

??? abstract "Target group"

    [ ] Authors [ ] Coaches  [ ] Participants  [x] Administrators

    [ ] Beginners [x] Experienced users  [x] Experts


??? abstract "Expected previous knowledge"

    * Experience as administrator

OpenOlat knows four life cycles. Administrators set up three of them in the system administration under `Administration > Life cycles`:

* **Group life cycle**
* **Course life cycle**
* **Automatic user lifecycle**

The fourth, the **implementation life cycle**, belongs to the Course Planner and is set up there, see [Implementation life cycle](#implementation_lifecycle).

OpenOlat monitors whether a group has not been visited for a long time, whether nobody has logged in to an account for a long time and whether the course end of a course has passed. According to predefined criteria, it sends a message that first enables a reaction and then, for example, manual deletion. Or OpenOlat deletes if necessary also automatically according to set criteria.


## Stages/Phases {: #lifecycle_stages}

Each life cycle has its own trigger and its own steps:

| Life cycle | Trigger | Steps |
|---|---|---|
| Group life cycle | Days without a visit by group coaches or group participants | Inactivation, Deletion, Permanent deletion |
| Course life cycle | Course end, i.e. the end date of the execution period | Status "Finished", status "Trash", "Definitely deleted" |
| Automatic user lifecycle | Last login | Deactivation, Deletion |
| Implementation life cycle | Execution period or status change | Status change, for example to "Active" or "Finished". Nothing is deleted. |

Using the group life cycle as an example:

- **Inactivation**<br>
When a group is inactivated, the status of the group changes from "Active" to "Inactive", and group members can only access the group in read-only mode. Inactive groups and inactive accounts can be fully reactivated.
- **Deletion**<br>
When a group is deleted, all members are removed from the group and any links to courses are removed. All other data is retained and remains viewable. The group can be restored.
- **Permanent deletion**<br>
When a group is permanently deleted, it is completely removed.

[To the top of the page ^](#lifecycles)

---


## Where and how are the life cycles set up? {: #lifecycle_setup}

### General activation and setting {: #lifecycle_activation}

The general activation and the definition of the automatically executed reminders or deletions is done by the administration. You find the settings in the system administration under:<br>
`Administration > Life cycles`

Based on these **general** presets, life cycles can then be activated **for individual** courses, groups or accounts.

![Marked area Account expiration with explanatory text and daily run time, below it the Yes/No choice for the notification: page User in the system administration](assets/lifecycle_user_admin_v2_en.png){ class="shadow lightbox" }

[To the top of the page ^](#lifecycles)

---


### Group life cycle [:octicons-tag-16:{ title="from Release 16.1 (OO-5190)" }](https://track.frentix.com/issue/OO-5190) {: #group_lifestyle}

The group life cycle is managed by group managers, based on the default settings of the administration, under:<br>
`Groups > Tab "Group management"`

Under `Groups > Tab "Group management"`, click on the big arrows with the description of the steps. The descriptions on the arrows reflect the administrator's default settings.

* In the first step (1st arrow) you will find all active groups listed.
* In the "To inactivate" tab of the 1st arrow you will see the groups proposed for inactivation, according to the administrator's rules.
* If you select one or more groups, buttons appear above the list.
* With the buttons above the list or the link at the end of a list line you can now inactivate specific individual groups or use "Start inactivation" to inform about the upcoming inactivation. You can withdraw a started inactivation with "Cancel inactivation".

![Three arrows for active, inactive and deleted groups with the configured periods, below them the marked tab To inactivate with the buttons for inactivating: tab Group administration](assets/lifecycle_groups_active_v1_en.png){ class="shadow lightbox" }

<br>

* In the second step (2nd arrow) you will find all already **inactive** groups listed.
* If groups were automatically set to the status "inactive" by the system, it is also possible to reactivate groups here.

![Second arrow Inactive groups active, the list shows Inactivated on and Deletion date, the button Reactivate is on the right: tab Group administration](assets/lifecycle_groups_inactive_v1_en.png){ class="shadow lightbox" }

<br>

* In the third step (3rd arrow) you will find all **deleted** groups listed.
* This list corresponds to the "recycle bin". The groups can now be permanently deleted - automatically or manually.

![Third arrow Deleted groups active, the list names Deleted on and Date of irrevocable deletion: tab Group administration](assets/lifecycle_groups_deleted_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#lifecycles)

---


### Course life cycle {: #course_lifecycle}

The course life cycle can be used by anyone who has access to the authoring area.

The basis is the administrator's default settings:

![The three steps Finished, Delete (Trash) and Delete permanently with period and unit, below them the enforced notification of the owners: page Courses in the system administration](assets/lifecycle_course_admin_v1_en.png){ class="shadow lightbox" }

<br>

* Courses with the status "Trash" are collected in the "Deleted" tab of the authoring area.
* As soon as you have selected a course and marked the checkbox at the beginning of the line, further buttons appear above the list. Here you can restore a course. Administrators and learning resource managers can delete it permanently.
* Also by clicking on the 3 dots at the end of a line you will get to the options for restoring or permanently deleting.

![Tab Deleted with courses in the status Trash, the buttons Restore and Delete permanently and the same actions in the row menu: authoring area](assets/lifecycle_course_authoring_v1_en.png){ class="shadow lightbox" }

How administrators configure the periods, check the impacts in the confirmation dialog and follow the running process is described in the administration manual under [Automatic Course Life Cycle](../../manual_admin/administration/Automatic_Course_Lifecycle.md).

[To the top of the page ^](#lifecycles)

---


### Automatic user lifecycle [:octicons-tag-16:{ title="from Release 15.1 (OO-4460)" }](https://track.frentix.com/issue/OO-4460) {: #user_account_lifecycle}

The automatic user lifecycle can be used by anyone who has access to the user administration.

The basis is the default settings of the administration:

![Marked area Automatic user lifecycle with explanatory text and run time, below it the enabled toggle and the period: page User](assets/lifecycle_user2_admin_v2_en.png){ class="shadow lightbox" }

<br>

The configuration is held in two separate areas. The area **Account expiration** takes effect when an account reaches the expiry date stored for it. The area **Automatic user lifecycle** takes effect when nobody logs in to the account any more. Whichever occurs first takes effect. [:octicons-tag-16:{ title="from Release 21.1 (OO-8382)" }](https://track.frentix.com/issue/OO-8382)

Three phases follow from this:

* **Account expiration**: The expiry date is stored per account. Once it is reached, OpenOlat deactivates the account.
* **Deactivation**: Accounts without a login during the inactivity period are deactivated automatically or manually.
* **Deletion**: After the deactivation period, permanent deletion occurs automatically or manually. Depending on the configuration, it can also be triggered exclusively manually.

Notification emails can be configured for each phase, before or after the respective step.

How far a single account has progressed through these phases is shown in the "Account" tab of the person, see [Configure user](../../manual_admin/usermanagement/Configure_User.md#automatic_user_lifecycle).

!!! info "Configuration in the Administration"

    Periods, email notifications and the level of automation for all three phases are configured in the system administration under:<br>
    `Administration > Life cycles > User`<br>
    [Details about the automatic user lifecycle](../../manual_admin/administration/Life_cycles_-_Administration.md#lifecycle_accounts)

[To the top of the page ^](#lifecycles)

---


### Implementation life cycle [:octicons-tag-16:{ title="from Release 20.0 (OO-8092)" }](https://track.frentix.com/issue/OO-8092) {: #implementation_lifecycle}

Anyone who plans implementations in the Course Planner wants an implementation to start and finish at the right time without setting every status change by hand. For this, an implementation passes through the status values "Preparation", "Provisional", "Confirmed" and "Active" to "Finished" or "Cancelled". This sequence is the implementation life cycle. Unlike the other three life cycles, it does not delete anything, and it is not under `Administration > Life cycles`.

You can set the status values manually or via the automation. Time-controlled rules of the automation refer to the begin or the end of the execution period, other rules take effect on a status change. Administrators store the rules per element type in the system administration under:<br>
`Administration > Modules > Course Planner > Tab Element types`

Each implementation takes over the rules of its element type or overrides them, see [Configure automation](../../manual_user/area_modules/Course_Planner_Implementations.md#tab_settings_automation).

[To the top of the page ^](#lifecycles)

---

## Notifications {: #lifecycle_messages}

To minimize the risk of accidental deletion as much as possible, the affected individuals can be notified at each stage or phase of the preparation for deletion.

**Notification Settings for Courses:**<br>
It can be configured so that owners are notified of status changes.

**Notification Settings for Groups and Accounts:**<br>

- Email announcing the deactivation
- Response time following the announcement of the deactivation
- Customizable notification text announcing the deactivation
- An email confirming that the account has been deactivated
- Customizable notification text after deactivation

- Email announcing the deletion
- Response period following the notice of deletion
- Customizable notification text announcing the deletion
- An email confirming that the deletion has been completed
- Customizable notification text after deletion

- Optional email copy to any address in each case

[To the top of the page ^](#lifecycles)

---


## Checklist {: #checklist}

**Group life cycle**

- [x] By administrators: general activation and configuration in the system administration under `Administration > Life cycles > Groups`
- [x] By group managers: settings under `Groups > Tab "Group management"`
- [x] Configure the notification of the affected persons

**Course life cycle**

- [x] By administrators: general activation and configuration in the system administration under `Administration > Life cycles > Courses`
- [x] By anyone who has access to the authoring area: mark courses under `Authoring > Tab "Deleted"` and delete them
- [x] Configure the notification of the affected persons

**Automatic user lifecycle**

- [x] By administrators: general activation and configuration in the system administration under `Administration > Life cycles > User`
- [x] By anyone who has access to the user management: deactivate recognised inactive accounts manually under `User management > "Account of the person" > Tab "Account"`, delete them manually under `User management > Delete user`
- [x] Configure the notification of the affected persons

**Implementation life cycle**

- [x] By administrators: rules of the automation per element type in the system administration under `Administration > Modules > Course Planner > Tab Element types`
- [x] Per implementation: take over or override the rules of the element type under `Tab Settings > Automation`

[To the top of the page ^](#lifecycles)

## Further information {: #further_information}

**Mentioned on this page**<br>
[Automatic Course Life Cycle >](../../manual_admin/administration/Automatic_Course_Lifecycle.md)<br>
[Configure user >](../../manual_admin/usermanagement/Configure_User.md)<br>
[Life cycles: Overview >](../../manual_admin/administration/Life_cycles_-_Administration.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)

**Further reading**<br>
[Automatic Group Life Cycle >](../../manual_admin/administration/Automatic_Group_Lifecycle.md)<br>
[Delete user >](../../manual_admin/usermanagement/Delete_User.md)<br>
[Module Course Planner >](../../manual_admin/administration/Modules_Course_Planner.md)

[To the top of the page ^](#lifecycles)
