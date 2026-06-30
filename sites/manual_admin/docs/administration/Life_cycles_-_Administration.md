# Life cycles - Overview {: #lifecycles}

![admin_lifecycles_overview_v1_de.png](assets/admin_lifecycles_overview_v1_de.png){ class="shadow lightbox aside-left-lg" }

The following life cycles can be administered in this section:

---

## Groups {: #lifecycle_groups}

In OpenOlat Administration, settings for the [group lifecycle](Automatic_Group_Lifecycle.md) can be configured. It proceeds in the following steps:

* Inactivation
* Deletion
* Irrevocable deletion

Settings can be made both for groups in general and only for certain group types. 

!!! info "Group lifecycle — Details"
    Steps and settings for the automatic group lifecycle.<br>
    [Group lifecycle](Automatic_Group_Lifecycle.md)

[To the top of the page ^](#lifecycles)


## Courses {: #lifecycle_courses}

The life cycle of courses can be defined, 

* whether and when a course is automatically set to "Finished" status 
* when it is then moved to the trash,
* and when it will be permanently deleted

Course owners can be automatically informed of any status changes.

[To the top of the page ^](#lifecycles)



## Account {: #lifecycle_accounts}

Similar to the automatically controlled course lifecycle, the lifecycle of OpenOlat users' accounts can also be automated. 

!!! note "Note"
    The lifecycle runs in separate steps and is fed by partly different settings. The following table provides an overview.

| Variant | Settings source | Mail actions for automations | Version |
|---------|----------------|------------------------------|---------|
| Account expiry | **a)** User Management > Create user (field "Account expiry") or subsequently in the "Account" tab **b)** Automatically and thus system-wide, configured in Administration. **Important:** Both paths can be active simultaneously; the one whose time expires first takes precedence. | Configurable before and/or after account expiry | :octicons-tag-24:{ title="Available since Release 15.4" } |
| Deactivation | Automatically: Administration > Life cycles > Account (inactivity period) or Manually: User Management > Users > "Account" tab | Configurable before and/or after deactivation | :octicons-tag-24:{ title="Available since at least OO 20.1" } |
| Deletion | Automatically: Administration > Life cycles > Account (after deactivation period) or Manually: User Management > Delete user | Configurable before and/or after deletion | :octicons-tag-24:{ title="Available since at least OO 20.1" } |

!!! note "Note"
    General rule: If no new login occurs within the specified period, the user account is deleted.
    Additionally: It can be set up that the irrevocable deletion in the last step takes place automatically or exclusively manually.

Different notifications can be formulated for each step in the context of the steps and the time of the mail notification can be defined.

[To the top of the page ^](#lifecycles)
