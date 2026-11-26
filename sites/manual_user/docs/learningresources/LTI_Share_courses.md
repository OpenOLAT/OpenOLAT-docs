# Course Settings - Tab Share:<br> Configure LTI access to a course {: #LTI_share_course}

## What can you do with the LTI share? {: #lti_share_meaning}

With the LTI share (in OpenOlat "deployment"), you can offer an OpenOlat course in another learning management system, such as Moodle. Users there remain in their familiar system. They click on a link and are taken directly to your OpenOlat course without having to create an OpenOlat account or log in separately.

This is useful when a partner organization uses a different system and needs to access your course. You maintain the course once in OpenOlat and publish it to one or more platforms.

For step-by-step instructions on integrating a course into Moodle, see [How do I integrate an OpenOlat course into Moodle?](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md).

**What the LTI share does:**

* The course remains in OpenOlat. Users work on content and tests in OpenOlat, which opens in a new window for this purpose.
* The first time a user accesses the course, OpenOlat creates an LTI account for them. The account belongs to the organisation that is set for LTI in the system administration. The user becomes a member of the LTI group of the course, as participant or as coach.
* OpenOlat reports the course results back to the other system if a grading column is designated for this purpose there, that is a column into which the platform enters the results of the persons.
* The LTI share applies only to this specific course and only to the platform you select. All other courses remain blocked for that platform.
* If you delete the LTI share, the platform can no longer access the course.

You set up the LTI share in the course administration, under: `Course > Administration > Settings > Tab "Share"`, area "LTI 1.3 access configuration". The platform must first be set up as an external platform in the system administration, under `Administration > External tools > LTI > Tab "External platforms"`. Whether you add the LTI share yourself with the button "Add deployment" or request it with the button "Ask for a new deployment" by a message to the support of your OpenOlat instance depends on your role: [Who can add deployments?](../../manual_admin/administration/LTI_Integrations/index.md#deployments)

[To the top of the page ^](#LTI_share_course)

---


## Requirements {: #conditions}

### Requirements in system administration {: #conditions_admin}

The LTI share requires the module "LTI 1.3" to be switched on: [Activate LTI](../../manual_admin/administration/LTI_Integrations/index.md#activate_lti). System administrators register the external platform in the system administration of OpenOlat under `Administration > External tools > LTI > Tab "External platforms"`. On the other side, administrator access to the other LMS is required as well. Who may add the LTI share ("deployment") of a course is set in the system administration: [Who can add deployments?](../../manual_admin/administration/LTI_Integrations/index.md#deployments)<br>
Ideally, set up both systems at the same time, because you enter details from one system in the other. The order is shown in the instructions [How do I integrate an OpenOlat course into Moodle?](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md)

### Requirements in the LTI share of a course [:octicons-tag-16:{ title="from Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #conditions_share}

The LTI share ("deployment") allows a specific external platform, for example Moodle, to launch this one course via LTI 1.3. Without a share, OpenOlat rejects every LTI call for the course, even if the platform is set up in the system administration.

### One deployment ID for several courses [:octicons-tag-16:{ title="from Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092) {: #deployment_id_several_courses}

If you offer several OpenOlat courses on the same platform, the platform often sends the same deployment ID for all of them. This happens when the platform sets up the tool jointly for several courses. If the platform is itself an OpenOlat instance, it uses a shared deployment ID when the option "With shared deployment" is switched on for the external tool there, or when an "LTI page" course element or its course is copied: [Global or local deployment](../../manual_admin/administration/LTI_External_tools.md#deployment_scope). Each OpenOlat course can still be shared with this deployment ID, no second tool is needed on the platform.

Enter the deployment ID in the LTI share ("deployment") of every course the platform should reach, in the field "Deployment ID" of the dialog after clicking "Add deployment". Within the same course, a deployment ID can be used only once per platform. A second attempt ends with the message "Deployment ID must be unique for a specific platform and course."

OpenOlat recognizes which course to open from the address the platform sends with the call. In Moodle, this is the "Tool URL" of the external tool. This address must begin with the "Tool URL" that OpenOlat shows in the dialog after clicking "Add deployment". If the address matches no shared course, OpenOlat cancels the call instead of opening another course.

A copied OpenOlat course does not take over the LTI share of the original. It needs its own LTI share, even if the platform uses the same deployment ID.

[To the top of the page ^](#LTI_share_course)

---


## What information is exchanged between the two systems? {: #data_exchange}

With every call, Moodle sends information about the person and the course context to OpenOlat. OpenOlat sends only one thing back: the course result of the person.

Which LTI services OpenOlat supports as a tool and as a platform is shown in the overview [Supported LTI services](../../manual_admin/administration/LTI_Integrations/index.md#supported_services).


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

OpenOlat sends the result with every change of the score, not only at the end of the course. OpenOlat sends results only for participants of the course. Whoever comes from Moodle as Instructor or Mentor becomes coach of the LTI group and receives no result: [Which role do people get who open an OpenOlat course from Moodle?](#roles_for_externals)


### What is not exchanged {: #data_exchange_non}

* **Member lists:** OpenOlat stores the address of the names and roles service, but never queries it. Members are therefore only added when they open the course themselves.
* **List of grade columns:** This address is also only stored.
* **Course content:** It remains in OpenOlat and is displayed there.

[To the top of the page ^](#LTI_share_course)

---


## Which role do people get who open an OpenOlat course from Moodle? [:octicons-tag-16:{ title="from Release 15.5 (OO-5207)" }](https://track.frentix.com/issue/OO-5207) {: #roles_for_externals}

With every LTI share ("deployment") of a course, OpenOlat creates an LTI group. All persons accessing externally via LTI are added to this group.

Through the group, the persons are then (group) coach or (group) participant in the course. Which of the two roles they get is decided by the LTI role that Moodle sends with the call. The table names the roles with their English names from the LTI standard. The course element "LTI page" shows the same roles, for example "Learner".

| LTI role in Moodle |   | Course role in OpenOlat                               |
| ----------------- | ----- |------------------------------------------- |
| Instructor (course role or role in the institution) | becomes | group coach in the LTI group |
| Mentor            | becomes | group coach in the LTI group |
| Learner or any other role | becomes | group participant |

Nobody becomes course owner via LTI.

### Where do you see the people from the other platform? {: #roles_members_management}

Once you have added the LTI share ("deployment"), OpenOlat creates the group "LTI: Name of the platform" in the course. You find it in the members management under the groups. The group is initially empty. A person will only appear in it when they access the course for the first time from the other platform. In the member list, they will then be listed as group coach or group participant.

If you copy the course, the LTI group is not copied along with it. Set up a separate LTI share for the copy.

[To the top of the page ^](#LTI_share_course)

---


## Configuration procedure {: #config_process}

The configuration requires steps in Moodle and in OpenOlat. The instructions [How do I integrate an OpenOlat course into Moodle?](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md) guide you through the whole procedure, from the external tool in Moodle to the connection test.

[To the top of the page ^](#LTI_share_course)

---


## How and where are the results displayed? {: #results}

### Results in the assessment tool and in the platform {: #results_assessment_tool}

Persons from the other platform who are participants of your course through the LTI group appear like all participants in the [assessment tool](Assessment_tool_overview/index.md) of the course, under: `Course > Administration > Assessment tool`. Who becomes a participant is decided by the LTI role: [Which role do people get who open an OpenOlat course from Moodle?](#roles_for_externals) In the other platform, the course result appears in the grading column the platform specified with the call: [From OpenOlat to Moodle](#data_exchange_from_openolat)

You do not need the course element "LTI page" for this. It serves the opposite direction: with it, OpenOlat integrates an external tool into a course and takes over its scores, see [Course element "LTI page"](Course_Element_LTI_Page.md).

[To the top of the page ^](#LTI_share_course)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I integrate an OpenOlat course into Moodle? >](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.md)<br>
[LTI 1.3 Integrations >](../../manual_admin/administration/LTI_Integrations/index.md)<br>
[LTI - External tools >](../../manual_admin/administration/LTI_External_tools.md)<br>
[Assessment tool - overview >](Assessment_tool_overview/index.md)<br>
[Course Element "LTI Page" >](../../manual_user/learningresources/Course_Element_LTI_Page.md)

**Further reading**<br>
[Configure LTI access to a group >](../../manual_user/groups/LTI_Share_groups.md)<br>
[LTI - External Platforms >](../../manual_admin/administration/LTI_External_platforms.md)<br>
[LTI - Deep Linking >](../../manual_admin/administration/LTI_Deeplinking.md)<br>
[LTI - Role mapping >](../../manual_admin/administration/LTI_Role_Mapping.md)<br>
[Course settings - Tab Share >](Course_Settings_Share/index.md)<br>
[Members management >](../../manual_user/learningresources/Members_management.md)<br>
[Access configuration >](../../manual_user/learningresources/Access_configuration.md)

[To the top of the page ^](#LTI_share_course)
