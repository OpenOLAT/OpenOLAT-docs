# Course Settings - Tab Share:<br> Configure LTI access to a course {: #LTI_share_course}

OpenOlat allows other LMS to access individual OpenOlat courses via LTI. This means that your OpenOlat courses can also be visited by people who work on another LMS.

**Example:**<br>
An OpenOlat course is launched from Moodle via LTI 1.3. When the course is opened, the users are created in OpenOlat as LTI users and get access to the OpenOlat course (in the role of participant or coach).<br>
You can find detailed instructions [here](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md).


## Requirements {: #conditions}

### Requirements in system administration {: #conditions_admin}

For the configuration, administrator access must be ensured in both systems. (In OpenOlat, this can also be the System administrator role).  Preferably, the configuration takes place on both systems at the same time, as certain dialogs have to be configured in both systems in direct succession.

### Requirements in the LTI share of a course [:octicons-tag-16:{ title="from Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #conditions_share}

The LTI share allows a specific external platform, for example Moodle, to launch this one course via LTI 1.3. Without a share, OpenOlat rejects every LTI call for the course, even if the platform is set up in the administration.

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
| Deployment ID and target URL | Show which shared course or which group is meant. OpenOlat checks the target URL against the share. | 
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

With every LTI course share, OpenOlat creates an LTI group. All persons accessing externally via LTI are added to this group.

Through the group, the persons are then (group) coach or (group) participant in the course. 
Which of the two roles they get is decided by the LTI role that Moodle sends with the call.

| LTI role in Moodle |   | Course role in OpenOlat                               |
| ----------------- | ----- |------------------------------------------- |
| Instructor (course role or role in the institution) | becomes | group coach in the LTI group |
| Mentor            | becomes | group coach of the LTI group |
| Learner or any other role | becomes | group participant |

Nobody becomes course owner via LTI.

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

How-to: [How do I integrate an OpenOlat course into Moodle? >](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md)<br>
User manual: [Configure LTI access to a group >](../../manual_user/groups/LTI_Share_groups.md)<br>
User manual: [Course element "LTI page" >](../../manual_user/learningresources/Course_Element_LTI_Page.md)<br>
Admin manual: [LTI 1.3 Integrations at a glance >](../../manual_admin/administration/LTI_Integrations.md)<br>
Admin manual: [LTI - External tools >](../../manual_admin/administration/LTI_External_tools.md)<br>
Admin manual: [LTI - External platforms >](../../manual_admin/administration/LTI_External_platforms.md)<br>
Admin manual: [LTI - Deep Linking](../../manual_admin/administration/LTI_Deeplinking.md)<br>
Admin manual: [LTI - Role mapping](../../manual_admin/administration/LTI_Role_Mapping.md)

User manual: [Members management >](../../manual_user/learningresources/Members_management.md)<br>
User manual: [Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
User manual: [Access configuration / Share >](../../manual_user/learningresources/Access_configuration.md)<br>

[To the top of the page ^](#LTI_share_course)
