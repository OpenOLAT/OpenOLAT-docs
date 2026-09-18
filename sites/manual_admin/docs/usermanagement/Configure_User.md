# Configure User {: #user_configuration} 

If you have the right to manage users, you can search for a specific person using the user search and make further configurations for them.

A maximum of the tabs listed below are available for configuration for each user (administrator). Depending on the roles and activated modules, there may be fewer tabs.


![Header area with status, identity, organisation, account type and username, below them 25 tabs from User profile to Grading assignments: page Manage account settings in User management](assets/user_management_configure_user_v5_en.png){ class="shadow lightbox" }

The account information lists the person's organisations under "User in" and their additional roles under "Additional Roles" as clickable entries; a click opens the "Roles" tab. If the account has no additional roles, the entry is not displayed. [:octicons-tag-16:{ title="from Release 20.0.2 (OO-8515)" }](https://track.frentix.com/issue/OO-8515)

Besides that, the account information states the status of the account, the identity, the account type, the username and the email address. Above the view, the action "Export data" compiles the personal data of the account, see [Data protection](Data_protection.md). At the same place the account can be deleted, see [Delete user](Delete_User.md).

Each user account is maintained independently; accounts are not merged. What a person has achieved in OpenOlat, that is course memberships, test results, evidence of achievements, certificates and badges, remains permanently linked to the account on which it was created. This keeps every record unambiguously assigned to one login and verifiable later on, and personal data stays limited to a single account.

If the option "Unique" is activated in the system administration, no two accounts with the same email address are created. You find the option in the section "User email address" under:<br>
`Administration > Core functions > E-mail`, segment "Settings", see [Email Settings](../administration/E-Mail_Settings.md#email_address).

!!! tip "Two accounts of the same person"
    If two accounts of the same person exist nevertheless, decide which account is continued. Download the certificates of the second account in the "Certificates" tab with "Download certificate" and record them in the continued account with "Upload certificate". Then set the second account to inactive in the "Account" tab.


### User profile

Personal data, personal details, contact details and details of the institution are recorded in the user profile. See: `Personal Menu > Configuration >` [Profile](../../manual_user/personal_menu/Profile.md). Furthermore, the personal information entered by the user, as well as the respective business card and the selected personal picture/photo are visible. The mandatory entries in the user profile include: Login name, first name, surname and email address. If the sending of emails to this address is to be prevented, this email address can be blocked.

[To the top of the page ^](#user_configuration)


### System settings

The system settings made by the user are displayed here. See: `Personal Menu > Configuration >` [Settings](../../manual_user/personal_menu/Settings.md).<br>
This includes, for example, the default language and whether emails are only sent within OpenOlat or also to the address in the profile. 

If the account carries an expiry date, the tab shows it under "Account expiration". A number of remaining days is not given here; the periods are listed in the "Account" tab. For inactive accounts OpenOlat hides the entry. [:octicons-tag-16:{ title="from Release 21.1 (OO-8382)" }](https://track.frentix.com/issue/OO-8382)

[To the top of the page ^](#user_configuration)


### Account

The "Account" tab shows the state of an account and the point it has reached in the lifecycle. Here you judge whether and when OpenOlat deactivates or deletes an account automatically, and here you set it to inactive manually.

Administrators, user administrators and role administrators reach the tab. Which fields it shows depends on the role of the edited account and on the toggles of the user lifecycle, see [Life cycles: Account](../administration/Life_cycles_-_Administration.md#lifecycle_accounts).

#### User type {: #account_type }

The user type distinguishes registered accounts, guest accounts and invited accounts. You convert an invited account with "Convert to registered user".

#### Created at {: #creation_date }

Date and time at which the account was created.

#### Last login {: #last_login }

Date and time of the last login. This value is the reference for the automatic user lifecycle. For guest accounts the entry is omitted.

#### Inactivation date {: #inactivation_date }

Date on which the account was deactivated. The field only appears for an account that has already been deactivated once.

#### Reactivation date {: #reactivation_date }

Date on which a deactivated account was released again. The field only appears after a reactivation.

#### Status {: #account_status }

The status controls whether the person can log in. Available are "Active", "Active and not deletable", "Pending", "Inactive" and "Login denied". For accounts with the role administrator, system administrator or role administrator the status cannot be changed.

#### Account expiration {: #account_expiration }

Here you store the date on which OpenOlat should deactivate the account. This suits fixed-term access, for example for guest lecturers or project work. For administrators, system administrators and guest accounts the field is not available.

#### Days until expiry {: #days_until_expiry }

If an expiry date is set, this field shows the remaining time in the format "In 14 days". If the date lies in the past, the number of overdue days appears in red, with the note that OpenOlat will deactivate the account in the next run. Without an expiry date the field is omitted.

#### Automatic user lifecycle {: #automatic_user_lifecycle }

This section shows how the system-wide lifecycle affects this account. It is omitted for guest accounts. Which entries appear depends on the state of the account:

| State | Entry | Meaning |
|-------|-------|---------|
| Active | "Last login", "Days until inactivation" | OpenOlat deactivates the account automatically after this period without a login. |
| Reactivated | additionally "Reactivation date", the period carries the addition "(grace period)" | The account was released again after a deactivation and runs in a grace period. |
| Inactive | "Inactivation date", "Days until deletion" | The account is deactivated and will be deleted automatically after this period. |

Besides the number of days, both periods also name the date on which the step falls due.

"Days until inactivation" only appears when the toggle "Deactivate user after inactivity" is active, "Days until deletion" only when the toggle "Delete inactive user" is active. You find both toggles in the system administration under:<br>
`Administration > Life cycles > User`

If the toggles are off, no automatic process takes effect and the periods are omitted.

An active account with a stored expiry date carries both periods next to each other: "Days until expiry" for the date, "Days until inactivation" for the last login.

![Account expiration 12/31/2028 with "In 837 days", below it the section Automatic user lifecycle with last login and "In 710 days": Account tab of an active account](assets/user_management_account_tab_active_v1_en.png){ class="shadow lightbox" }

After a reactivation the reactivation date is added, and the period carries the addition "(grace period)".

![Reactivation date 9/16/2026 and the period "In 710 days, on 8/26/2028 (grace period)": Account tab of a reactivated account](assets/user_management_account_tab_reactivated_v1_en.png){ class="shadow lightbox" }

For an inactive account the inactivation date and "Days until deletion" take the place of the inactivation period.

![Inactivation date 9/16/2026 and the period "In 1101 days, on 9/21/2029": Account tab of an inactive account](assets/user_management_account_tab_inactive_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#user_configuration)


### Roles

The roles of the user are defined in this tab. If the "Organisations" module is activated, different roles can be assigned per organizational unit. See ["Assign roles"](Assign_roles.md).

[To the top of the page ^](#user_configuration)


### Password [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9139)" }](https://track.frentix.com/issue/OO-9139)

If the user does not yet have local authentication, the "Local OpenOlat Authentication" section shows two buttons. The button "Send invitation link to set login credentials" sends a link by mail; the person then sets their own login credentials. "Create login credentials" sets them directly.

If an invitation link has already been sent, a message shows its validity period. The "Deactivate invitation link" action can be used to invalidate the link at any time. After expiry or deactivation the link leads nowhere; you can then send a new invitation link.

The "Password" tab and its actions are available to administrators, user managers and roles managers. User managers do not see the tab for accounts that are themselves administrator or roles manager.

You define how long an invitation link remains valid in the system administration in the section "Validity period of the login data":<br>
`Administration > Login > Self-registration`, tab "Configuration", see [Self-registration](../administration/Login_Self-Registration.md#tab_configuration).

![Six steps from sending the invitation link to the saved login credentials, split across the administrating role, OpenOlat and the person](assets/user_management_invitation_link_flow_v1_en.svg){ class="shadow lightbox" }

The "Passkeys" section is hidden if security level 1 (Password) applies as the minimum and no local authentication is available.

[To the top of the page ^](#user_configuration)


### Authentications

Here you can change the username and edit and delete authentications.  

[To the top of the page ^](#user_configuration)


### Properties

User Properties can be displayed and exported as a table.  

[To the top of the page ^](#user_configuration)


### GUI preferences

The GUI settings saved for the user(s) can be reset here.

[To the top of the page ^](#user_configuration)


### Groups

An overview of all groups in which the user is a participant or coach is displayed. 
Under this tab, the user can also be assigned to other groups or removed from a group.

[To the top of the page ^](#user_configuration)


### Learning resources

This tab generates an overview with all learning resources of the user. User administrators and administrators can remove users from the respective learning resources and call up the respective learning resources. Furthermore, the user can be registered as owner, coach or participant in further OpenOlat courses.  

The list carries single learning resources with the course and group roles of the person. Implementations of the Course Planner are listed in the "Educational products" tab instead.

[To the top of the page ^](#user_configuration)


### Projects

All projects in which this user is a member are listed under this tab. 

[To the top of the page ^](#user_configuration)


### Portfolio

All portfolio folders to which the user is invited are displayed here. (This user's own portfolios are not listed here).

[To the top of the page ^](#user_configuration)


### Bookings

The booking orders and pre-orders of the user are displayed here.  

[To the top of the page ^](#user_configuration)


### Credit points [:octicons-tag-16:{ title="from Release 20.1.1 (OO-8558)" }](https://track.frentix.com/issue/OO-8558)

The user's acquired credit points are displayed here. 

[To the top of the page ^](#user_configuration)



### Evidence of achievements

The evidence of achievements, points and progress of a user from courses are displayed here. In addition to the columns for points, success status and progress, further columns can be shown, including "Rating" with the achieved grade (if the grading module is active) and the "Reference" column, which is hidden by default. [:octicons-tag-16:{ title="from Release 21.0 (OO-9581)" }](https://track.frentix.com/issue/OO-9581)

<h4>Delete evidence of achievement</h4>

Via the actions menu (three dots) of a row, a single evidence of achievement can be deleted [:octicons-tag-16:{ title="from Release 21.0 (OO-9551)" }](https://track.frentix.com/issue/OO-9551). A confirmation dialog explains the effect: if the person is still a participant of the course, the evidence of achievement is automatically regenerated; if they are no longer enrolled, it is permanently deleted.

[To the top of the page ^](#user_configuration)


### Certificates [:octicons-tag-16:{ title="from Release 20.2.0 (OO-8984)" }](https://track.frentix.com/issue/OO-8984)

This tab brings together all of the person's certificates, both those acquired in courses and those uploaded manually. For each certificate the table lists "Awarded by", "Origin", "Issued on", "Valid until", "Recertification", "Revoked on", "#Issued" and "State"; the predefined filters "All", "Valid" and "Expired" narrow down the list. Above the table on the right you can switch between tile and table view. "Upload certificate" is used to record externally acquired certificates so that the profile reflects the entire transcript of records.

![Certificate list with origin, date of issue and state, above it the button Upload certificate: Certificates tab of an account](assets/user_management_certificates_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#user_configuration)


### Badges

This tab displays all the badges you have purchased.

[To the top of the page ^](#user_configuration)


### Compensation for disadvantages

Disadvantage compensation entitles test takers to use more time for a test due to a restriction. Disadvantage compensation can be added and configured under this tab. The dialog "Add disadvantage compensation" requires "Approved by", "Approval date", "Extra time (minutes)" and the course. The field "Course element" narrows the compensation down to a single test of the course.

![Four mandatory fields marked with an asterisk, below them the optional field Course element: dialog Add disadvantage compensation](assets/disadvantage_compensation.jpg){ class="shadow lightbox" }

[To the top of the page ^](#user_configuration)


### Subscriptions [:octicons-tag-16:{ title="from Release 8.1.2 (OO-265)" }](https://track.frentix.com/issue/OO-265)

All of a user's subscriptions are displayed here. They can also be deactivated or deleted here.  

[To the top of the page ^](#user_configuration)



### Relations [:octicons-tag-16:{ title="from Release 13.2 (OO-3305)" }](https://track.frentix.com/issue/OO-3305)

In this tab, relations between the selected user and other OpenOlat users can be defined. For example, whether someone is a teacher's superior, parent, training coach or student. The prerequisite is that a system is generally used. (Cf. [User roles](index.md))

[To the top of the page ^](#user_configuration)


### Quota

An individual quota can be set up here, e.g. to give a person with special tasks more upload options. For example, the quota in the Media Centre can be increased for authors who need to include a particularly large number of videos in their courses.

[To the top of the page ^](#user_configuration)


### Events

Here you will find an overview of events and absences of the user.

[To the top of the page ^](#user_configuration)


### Competences

Areas of competence can be added to the user here. They are categorized according to "Manage", "Teach", "Have" and "Target".

[To the top of the page ^](#user_configuration)


### Educational products [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9288)" }](https://track.frentix.com/issue/OO-9288)

Here you will find the implementations of the user. The list shows all implementations of the person, regardless of the role they hold in them [:octicons-tag-16:{ title="from Release 21.0 (OO-9374)" }](https://track.frentix.com/issue/OO-9374){:target="_blank"}.

OpenOlat only shows the tab when the Course Planner is active. Without this module it does not appear.

The list carries implementations, not single courses. A course appears here as part of the implementation through which the person was booked, and in the "Learning resources" tab additionally as a single learning resource. The two tabs answer different questions: "Educational products" shows which educational offerings the person passes through, "Learning resources" shows which courses they are registered in. Unlike there, you neither add nor remove the person here.

![Marked tab Educational products, preselected filter tab Relevant and the column Roles, User management](assets/user_management_educational_products_v1_en.png){ class="shadow lightbox" }

The filter tabs available are "All", "Relevant" and "Finished", "Relevant" is preselected. Compared to the Coaching Tool, the list shows the additional column "Roles", which states for each implementation in which role the person takes part. In return, the columns "Favourite" and "Status" and the tabs "Favourites" and "Preparation" are missing. A click on the title of an implementation opens its structure with the contained courses.

What the individual tabs show is described in the section [Filtering the list](../../manual_user/area_modules/Coaching_Educational_Products.md#filter) in the user manual.

[To the top of the page ^](#user_configuration)


### Grading assignments

Here you can check which grading assignments have been assigned to this user.

[To the top of the page ^](#user_configuration)


## Further information {: #further_information}

**Mentioned on this page**<br>
[Data protection >](Data_protection.md)<br>
[Delete user >](Delete_User.md)<br>
[E-mail settings >](../administration/E-Mail_Settings.md)<br>
[User profile >](../../manual_user/personal_menu/Profile.md)<br>
[Settings >](../../manual_user/personal_menu/Settings.md)<br>
[Life cycles: Administration >](../administration/Life_cycles_-_Administration.md)<br>
[Assign roles >](Assign_roles.md)<br>
[Self-registration >](../administration/Login_Self-Registration.md)<br>
[User roles >](index.md)<br>
[Coaching: Educational products >](../../manual_user/area_modules/Coaching_Educational_Products.md)

**Further reading**<br>
[User/account search >](Search_Users.md)<br>
[Create user >](Create_User.md)

[To the top of the page ^](#user_configuration)
