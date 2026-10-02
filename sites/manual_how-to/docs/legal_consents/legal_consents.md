# How do I comply with legal consent requirements? {: #legal_consents}

??? abstract "Objectives and content of this instruction"

    As the author of a course that involves working with sensitive data, you need legal protection. This raises the following questions:<br>
    - How do I obtain legal consents?<br>- How do I comply with legal consent requirements?<br>
    This guide shows you where and how you can do this in OpenOlat.


??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants

    [x] Beginners [x] Advanced users  [x] Experts


??? abstract "Expected previous knowledge"

    * You have already created an OpenOlat course and are familiar with [adding course elements (German)](https://www.youtube.com/embed/AJ76e3urdKA).
    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)


---

## Case study of a teacher {: #case_study}

As the coach of a course on "Managing Patient Data," you are aware that all course participants will be handling sensitive data. It is therefore essential that all participants accept a written data protection statement.

Since part of this internship takes place online, you want to ensure that, as the coach, you cannot be held liable for data protection violations in your course.

How do you proceed?

Below is a description of the available OpenOlat tools and their intended uses.


[To the top of the page ^](#legal_consents)

---

## Clarification 1: Objective {: #clarify_objective}

Determine which terms of use and privacy policies course participants must agree to. For example:

WHAT?

- Do students have to submit an "affidavit"?
- Is it necessary to submit a statement confirming that the submitted work was completed independently?
- Is an NDA required?
- Do specific consents regarding use and data sharing need to be confirmed?
- ...

WHEN?

- Do consents need to be obtained before participants can access certain content?
- Do consents need to be obtained only when specific content is accessed? For example, before or after participants take exams, submit assignments, etc.
- ...

[To the top of the page ^](#legal_consents)

---


## Clarification 2: OpenOlat Platform {: #platform}

If the terms of use of the platform are switched on, all users are asked to accept the Terms of Use and Privacy Policy the first time they open OpenOlat. You can therefore review:

- What has already been confirmed by all users of the OpenOlat platform?
- Would corrections need to be made at this stage?
- What additional consents need to be obtained given the particularly sensitive nature of your course?

All users can review the Terms of Use and Privacy Policy, which they have previously agreed to, at any time in their personal menu:<br>
`Personal menu > System settings > Terms of use`<br>
More about this: [Personal Configuration: Settings >](../../manual_user/personal_menu/Settings.md#tab_terms_of_use)

Information about the OpenOlat platform's Terms of Use and Privacy Policy, as well as the confirmation required from OpenOlat users upon their first visit, can be found here: [OpenOlat Platform Terms of Use >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_platform).

[To the top of the page ^](#legal_consents)

---

## Clarification 3: Rights within OpenOlat {: #rights}

Within OpenOlat, you collaborate with many different people. These include administrative roles such as user administrators, learning resource administrators, and administrators, among others, who may have access to your course content and to information about the participants due to their roles.

For part of this information, restrictions can be set in the system administration:<br>
`Administration > Modules > Privacy`

There you specify which system roles are allowed to view the administrative user properties, for example during account searches or in lists. Which user properties are considered administrative is configured in the user properties.

If you have any questions, please contact your administrators.<br>
You can find more information here: [Data Protection Module (Administration) >](../../manual_admin/administration/Modules.md#data_privacy)

[To the top of the page ^](#legal_consents)

---

## Clarification 4: Course {: #course}

Does it turn out that additional consent must be obtained from all participants specifically for your course?

OpenOlat also allows you to create course-specific terms of use. As a course owner, you can obtain consent for your course under:<br>
`Course > Administration > Settings > Terms of use`

You can find more information here:<br>
[Terms of Use for a Course >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_course)

[To the top of the page ^](#legal_consents)

---


## Clarification 5: Course internal areas {: #areas}

In learning path courses, you can also use the learning path's features to restrict access to certain content or obtain participants' consent in advance.

Using the learning path settings, you can, for example, make a page containing information on data protection and data use mandatory. Participants must then confirm that they have "completed" this page before they can access the subsequent course elements in the course menu. You will find the settings under:<br>
`Course > Administration > Course editor > "Course element" > Learning path`

Also in the tab "Learning path", you can use exceptions to configure that a course element is visible only to specific groups of people.

[To the top of the page ^](#legal_consents)

---


## Clarification 6: Individual course elements {: #course_elements}

If privacy policies or notices apply specifically to individual course elements, OpenOlat also provides options within those elements for obtaining consent from course participants.

**Example: Course element Task**<br>
The course element Task has its own workflow. It consists of several steps, ranging from the task prompt to uploading answer documents, providing feedback, and viewing the sample solution.<br>
You can use the task assignment feature, for example, to create a message for participants with relevant instructions. ("By downloading this assignment, you agree to ...")<br>
In the "Submission" step, the task instructions can be set as a template. A consent form could also be included this way. ("By uploading your files, other people may be able to view ... Please therefore check ...")

**Example: Course element Checklist**<br>
In the course element "Checklist", you can add checkboxes for required confirmations.
Points can also be awarded that count as a criterion for "passed". A checklist that has been "passed" can then be used as one of the criteria for passing the entire course.

[To the top of the page ^](#legal_consents)

---


## Clarification 7: Forms {: #forms}

When filling out a form, the information entered may require participants to accept the terms of use. For this reason, the "Form" learning resource includes a dedicated content element "Terms of use" that authors can insert using the form editor.

[Terms of use of a form >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_form)

[To the top of the page ^](#legal_consents)

---


## Clarification 8: External tools {: #external_tools}

If external tools are used, that is, programs that are not part of OpenOlat itself but are integrated into it, OpenOlat has no way of verifying whether data transmitted to these tools is stored elsewhere or used for other purposes.

**Example: Office Programs**<br>
For example, if Microsoft products such as Word, Excel, and PowerPoint are to be used and have been set up by administrators after obtaining the necessary licenses, users can collaborate on the same document. While collaborating, the files are stored on Microsoft servers and not in OpenOlat. You should simply be aware that this may have implications under data protection laws.

**Example: Course element External Page**<br>
The course element "External Page" can transmit data about the current account to the external system via the HTTP header of the request in order to implement certain learning scenarios (username, email, first name, last name, and the user's current IP address).
Administrators specify whether this data should be transmitted or not in the system administration under:<br>
`Administration > Modules > External page`<br>
Alternatively, this setting can also be configured under `Administration > Modules > Privacy`, in the section Data transmission within course element "external page".<br>
However, OpenOlat has no control over what happens to this data on the external site.

In OpenOlat, all external tools are configured in the system administration under:<br>
`Administration > External tools`

[To the top of the page ^](#legal_consents)

---


## Clarification 9: Connected platforms {: #LTI}

With OpenOlat, it is possible to access courses that are technically hosted on a different platform (another OpenOlat instance or another LMS). The technology for this is provided by the [LTI connection](../../manual_admin/administration/LTI_Integrations.md). This is similar to an external page. However, it is not just a single page, but entire courses that appear as if they were part of your own LMS.

Data is also exchanged between the connected platforms, subject to strict security measures. It may also be necessary to determine whether additional information and consent from participants are required for particularly sensitive data.

[To the top of the page ^](#legal_consents)

---


## Checklist {: #checklist}

- [x] What general consents did participants already have to provide in order to use the OpenOlat learning platform?
- [x] I have the General Terms of Use and the General Privacy Policy at hand.
- [x] All course participants have already confirmed the General Terms of Use and the General Privacy Policy.
- [x] Are additional course-specific statements required?
- [x] Are the texts of the course-specific statements available?
- [x] Have the course-specific statements already been integrated into the OpenOlat course?
- [x] Are they integrated in such a way that working on the course without prior consent is ruled out?
- [x] Do the consents need to be filed and archived somewhere?
- [x] Are forms being used? Should a statement regarding the terms of use be included there?
- [x] Does the course use external tools that access other external servers?
- [x] Is separate consent required for these external tools?
- [x] Are courses shared with other learning platforms via LTI? Are there any legal issues regarding data transfer to or from those platforms?

[To the top of the page ^](#legal_consents)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I create my first OpenOlat course? >](../my_first_course/my_first_course.md)<br>
[Personal Configuration: Settings >](../../manual_user/personal_menu/Settings.md)<br>
[Terms of Use >](../../manual_user/basic_concepts/Terms_Of_Use.md)<br>
[Modules: Overview >](../../manual_admin/administration/Modules.md)<br>
[LTI 1.3 Integrations >](../../manual_admin/administration/LTI_Integrations.md)

**Further reading**<br>
[Data protection >](../../manual_admin/usermanagement/Data_protection.md)<br>
[Course Element "Task" >](../../manual_user/learningresources/Course_Element_Task.md)<br>
[Course Element "Checklist" >](../../manual_user/learningresources/Course_Element_Checklist.md)<br>
[Course Element "External Page" >](../../manual_user/learningresources/Course_Element_External_Page.md)

**youtube**<br>
[Adding course elements (German)](<https://www.youtube.com/embed/AJ76e3urdKA>)

[To the top of the page ^](#legal_consents)
