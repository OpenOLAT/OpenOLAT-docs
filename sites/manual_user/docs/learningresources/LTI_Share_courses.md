# Course Settings - Tab Share:<br> Configure LTI access to a course {: #LTI_share_course}

## What can you do with LTI sharing? {: #lti_share_meaning}

With LTI sharing, you can offer an OpenOlat course in another learning management system, such as Moodle. Users there remain in their familiar system. They click on a link and are taken directly to your OpenOlat course without having to create an OpenOlat account or log in separately.

This is useful when a partner organization uses a different system and needs to access your course. You maintain the course once in OpenOlat and publish it to one or more platforms.

You can find detailed instructions [here](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md).

**What LTI integration does:**

* The course remains in OpenOlat. Users work on content and tests in OpenOlat, which opens in a new window for this purpose.
* The first time a user accesses the course, OpenOlat creates an LTI account for them. The user becomes a member of the course’s LTI group, either as a participant or as an instructor.
* OpenOlat reports the course results back to the other system if a grading column is designated for this purpose there.
* The LTI authorization applies only to this specific course and only to the platform you select. In the interface, it is called “Deployment.” All other courses remain blocked for that platform.
* If you delete the LTI authorization, the platform will no longer be able to access the course.

The platform must first be set up as an external platform in the administration section. Whether you add the LTI authorization yourself or request it from Support using the “Request New Deployment” button depends on your role. For more information, see [Prerequisites](#conditions).

[To the top of the page ^](#LTI_share_course)

---


## Requirements {: #conditions}

### Requirements in system administration {: #conditions_admin}

The external platform is registered in the system administration of OpenOlat, which requires administrator access (in OpenOlat, this can also be the System administrator role). On the other side, administrator access to the other LMS is required as well. Who may create the LTI share of a course is set in the system administration: [Who can add deployments?](../../manual_admin/administration/LTI_Integrations.md#deployments) Preferably, the configuration takes place on both systems at the same time, as certain dialogs have to be configured in both systems in direct succession.

### Requirements in the LTI share of a course [:octicons-tag-16:{ title="from Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #conditions_share}

The LTI share allows a specific external platform, for example Moodle, to launch this one course via LTI 1.3. Without a share, OpenOlat rejects every LTI call for the course, even if the platform is set up in the administration.

### One deployment ID for several courses [:octicons-tag-16:{ title="from Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092) {: #deployment_id_several_courses}

If you offer several OpenOlat courses on the same platform, the platform often sends the same deployment ID for all of them. This happens when the platform runs the tool as a shared deployment. A platform running OpenOlat does this automatically as soon as an "LTI page" course element or its course is copied there. Each OpenOlat course can still be shared with this deployment ID, no second tool is needed on the platform.

Enter the deployment ID in the LTI share of every course the platform should reach. Within the same course, a deployment ID can be used only once per platform. A second attempt ends with the message "Deployment ID must be unique for a specific platform and course."

OpenOlat recognizes which course to open from the address the platform sends with the call. In Moodle, this is the "Tool URL" of the external tool. This address must begin with the "Tool URL" that OpenOlat shows in the dialog after clicking "Add deployment". If the address matches no shared course, OpenOlat cancels the call instead of opening another course.

A copied OpenOlat course does not take over the LTI share of the original. It needs its own LTI share, even if the platform uses the same deployment ID.

[To the top of the page ^](#LTI_share_course)

---


## What information is exchanged between the two systems? {: #data_exchange}

With every call, Moodle sends information about the person and the course context to OpenOlat. OpenOlat sends only one thing back: the course result of the person.


### From Moodle to OpenOlat {: #data_exchange_from_moodle}

Moodle sends a signed token (LTI 1.3 launch). OpenOlat reads the following information from it:

| Information |  What OpenOlat needs it for | 
| -------| --------------------------- | 
| Issuer and user ID | This is how OpenOlat recognizes the person again. The combination is stored as LTI authentication. | 
| First name, last name, e-mail address | The user account is created from these. For LTI-only accounts, the values are updated with every call. | 
| Language | Is only adopted as the language setting of the account when the account is created. | 
| LTI roles | Determine whether the person becomes coach or participant. |
| Deployment ID and Tool URL | Show which shared course or which group is meant. If the same deployment ID applies to several courses, the Tool URL decides. | 
| Context ID and resource link ID | Identifier of the Moodle course and of the activity in it. | 
| Addresses of the Moodle services for grades and member lists | OpenOlat stores them per Moodle course. | 


### From OpenOlat to Moodle {: #data_exchange_from_openolat}

If the assessment of a person in the course changes, OpenOlat sends the result of the course as a whole to Moodle's grading service (Assignment and Grade Services). Individual course elements are not transferred. The following are transferred:

* the user ID from Moodle
* the score achieved
* the maximum score (100 if none is defined)
* the activity progress and the grading progress
* the comment on the assessment
* the timestamp

The result is only sent if Moodle has sent the address of a single grade column with the call. It goes to the Moodle platform through which the person is logged in.


### What is not exchanged {: #data_exchange_non}

* **Member lists:** OpenOlat stores the address of the names and roles service, but never queries it. Members are therefore only added when they open the course themselves.
* **List of grade columns:** This address is also only stored.
* **Course content:** It remains in OpenOlat and is displayed there.

[To the top of the page ^](#LTI_share_course)

---


## Which role do people get who open an OpenOlat course from Moodle? [:octicons-tag-16:{ title="from Release 15.5 (OO-5207)" }](https://track.frentix.com/issue/OO-5207) {: #roles_for_externals}

With every LTI share of a course, OpenOlat creates an LTI group. All persons accessing externally via LTI are added to this group.

Through the group, the persons are then (group) coach or (group) participant in the course. 
Which of the two roles they get is decided by the LTI role that Moodle sends with the call.

| LTI role in Moodle |   | Course role in OpenOlat                               |
| ----------------- | ----- |------------------------------------------- |
| Instructor (course role or role in the institution) | becomes | group coach in the LTI group |
| Mentor            | becomes | group coach of the LTI group |
| Learner or any other role | becomes | group participant |

Nobody becomes course owner via LTI.

### Where do you see the people from the other platform? {: #roles_members_management}

Once you have added the LTI integration, OpenOlat creates the group “LTI: Name of the Platform” in the course. You can find it in the Member Management section under “Groups.” The group is initially empty. A person will only appear in it when they access the course for the first time from the other platform. In the member list, they will then be listed as a group moderator or group participant.

If you copy the course, the LTI group is not copied along with it. You’ll need to set up a separate LTI integration for the copy.

[To the top of the page ^](#LTI_share_course)

---


## Configuration procedure {: #config_process}

1. Setup "External Tool" in Moodle
2. Setup "external platform" in OpenOlat
3. LTI share of the course in OpenOlat
4. Embedding the external tool (=OpenOlat) in the Moodle course
5. Connection test

You can find detailed instructions with these 5 steps [here](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md).

[To the top of the page ^](#LTI_share_course)

---


## How and where are the results displayed? {: #results}

### External courses in the assessment tool {: #results_assessment_tool}

The assessment form can also be filled in and adjusted for the LTI course element. Select the course element in the course editor. In the tab "Page content", "Transfer score" must be selected. Depending on the case, a scaling factor must also be entered and the score for passing must be defined. You can find more information on configuring LTI pages [here](../../manual_user/learningresources/Course_Element_LTI_Page.md).

[To the top of the page ^](#LTI_share_course)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I integrate an OpenOlat course into Moodle? >](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md)<br>
[LTI 1.3 Integrations >](../../manual_admin/administration/LTI_Integrations.md)<br>
[Course Element "LTI Page" >](../../manual_user/learningresources/Course_Element_LTI_Page.md)

**Further reading**<br>
[Configure LTI access to a group >](../../manual_user/groups/LTI_Share_groups.md)<br>
[LTI - External Platforms >](../../manual_admin/administration/LTI_External_platforms.md)<br>
[LTI - External tools >](../../manual_admin/administration/LTI_External_tools.md)<br>
[LTI - Deep Linking >](../../manual_admin/administration/LTI_Deeplinking.md)<br>
[LTI - Role mapping >](../../manual_admin/administration/LTI_Role_Mapping.md)<br>
[Course settings - Tab Share >](../../manual_user/learningresources/Course_Settings_Share.md)<br>
[Members management >](../../manual_user/learningresources/Members_management.md)<br>
[Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Access configuration >](../../manual_user/learningresources/Access_configuration.md)

[To the top of the page ^](#LTI_share_course)
