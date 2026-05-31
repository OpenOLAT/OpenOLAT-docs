# How do I comply with legal consent requirements? {: #legal_consents}

!!! abstract "Objectives and content of this instruction"

    As the author of a course that involves working with sensitive data, you need legal protection. This raises the following questions:<br> 



??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants

    [x] Beginners [x] Amateurs  [x] Experts


??? abstract "Expected previous knowledge"

    * You have already created an OpenOlat course and are familiar with [adding course modules](https://www.youtube.com/embed/AJ76e3urdKA). 
    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)



---

## Case study of a teacher {: #case_study}

As the instructor of a course on "Managing Patient Data," you are aware that all course participants will be handling sensitive data. It is therefore essential that all participants sign a written data protection agreement.

Since part of this internship takes place online, you want to ensure that, as the course instructor, you cannot be held liable for data protection violations in your course.

How do you proceed?

Below is a description of the available OpenOlat tools and their intended uses.

[To the top of the page ^](#legal_consents)

---

## Clarification 1: Objective

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

The first time you open OpenOlat, all users are asked to accept the Terms of Use and Privacy Policy. You can review them here:

- What has already been confirmed by all users of the OpenOlat platform? 
- Would corrections need to be made at this stage?
- What additional consents need to be obtained given the particularly sensitive nature of your course?

All users can review the Terms of Use and Privacy Policy, which they have previously agreed to, at any time in their personal menu: <br>
**Personal Menu > Settings > "Terms of Use" tab**

Information about the OpenOlat platform's Terms of Use and Privacy Policy, as well as the confirmation required from OpenOlat users upon their first visit, can be found here: [OpenOlat Platform Terms of Use >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_platform).

[To the top of the page ^](#legal_consents)

---


## Clarification 3: Rights within OpenOlat {: #rights}

Within OpenOlat, you collaborate with many different people. These include administrative roles such as user administrators, learning resource administrators, and system administrators, among others, who may have access to your sensitive course content due to their roles.

In OpenOlat, you can therefore set restrictions for these administrative roles under **Administration > Modules > Data Protection**.

You can specify which system roles are allowed to view administrative user properties—for example, during account searches or in lists—and which user properties are considered administrative.

If you have any questions, please contact your administrator.<br>
You can find more information here: [Data Protection Module (Administration)](../../manual_admin/administration/Modules.md#data_privacy)

[To the top of the page ^](#legal_consents)

---

## Clarification 4: Course {: #course}

Does it turn out that additional consent must be obtained from all participants specifically for your course?

OpenOlat also allows you to create course-specific terms of use. As a course owner, you can obtain consent for your course under **Administration > Settings > "Terms of Use" tab**.

You can find more information here: 
[Terms of Use for a Course >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_course)

[To the top of the page ^](#legal_consents)

---

## Clarification 5: Course internal areas {: #course}

In learning path courses, you can also use the learning path’s features to restrict access to certain content or obtain participants’ consent in advance.

Using the learning path settings (Course Editor > Select course blocks > Learning Path tab), you can, for example, make a page containing information on data protection and data use mandatory. Participants must then confirm that they have “completed” this page before they can access the subsequent course blocks in the course menu. 

The learning path feature also allows you to use exception rules to configure a course module so that it is visible only to specific groups of people.

[To the top of the page ^](#legal_consents)

---


## Clarification 6: Individual course elements {: #course_elements}

If privacy policies or notices apply specifically to individual course elements, OpenOlat also provides options within those elements for obtaining consent from course participants. 

**Example: Course element task**<br>
The Course Element Task has its own workflow. It consists of several steps, ranging from the task prompt to uploading answer documents, providing feedback, and viewing the sample solution.<br>
You can use the task assignment feature, for example, to create a message for participants with relevant instructions. ("By downloading this assignment, you agree to ...")<br>
In the "Submission" step, the task instructions can be set as a template. A consent form could also be included this way. ("By uploading your files, other people may be able to view ... Please therefore check ...")

**Example: Course element Checklist**<br>
In the "Checklist" course module, you can add checkboxes for required confirmations.
Points can also be awarded that count toward passing the course. A checklist that has been "passed" can then be used as one of the criteria for passing the entire course. 

[To the top of the page ^](#legal_consents)

---

## Clarification 7: Forms {: #forms}

When filling out a form, the information entered may require participants to accept the terms of use. For this reason, the "Form" learning resource includes a dedicated content element that authors can insert using the form editor.

[Terms of use of a form >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_form)


[To the top of the page ^](#legal_consents)

---

## Clarification 8: External tools {: #external_tools}

If external tools are used—that is, programs that are not part of OpenOlat itself but are integrated into it—OpenOlat has no way of verifying whether data transmitted to these tools is stored elsewhere or used for other purposes.

**Example: Office Programs**<br>
For example, if Microsoft products such as Word, Excel, and PowerPoint are to be used and have been set up by administrators after obtaining the necessary licenses, users can collaborate on the same document. While collaborating, the files are stored on Microsoft servers and not in OpenOlat. You should simply be aware that this may have implications under data protection laws.

**Example: Course Module – External Page**<br>
The "External Page" course module can transmit data about the current account to the external system via the HTTP header of the request in order to implement certain learning scenarios (username, email, first name, last name, and the user's current IP address). 
In **System Administration > Modules > External Page**, administrators can specify whether this data should be transmitted or not. Alternatively, this setting can also be configured under **Administration > Modules > Privacy > "Data Transmission for External Page Course Block" section**.<br>
However, OpenOlat has no control over what happens to this data on the external site.

In OpenOlat, all external tools are configured under **(System) Administration > External Tools > ...**.

[To the top of the page ^](#legal_consents)

---


## Clarification 9: Connected platforms {: #LTI}

With OpenOlat, it is possible to access courses that are technically hosted on a different platform (another OpenOlat instance or another LMS). The technology for this is provided by the [LTI connection](../../manual_admin/administration/LTI_Integrations.md). This is similar to an external page. However, it is not just a single page, but entire courses that appear as if they were part of your own LMS.

Data is also exchanged between the connected platforms—subject to strict security measures. It may also be necessary to determine whether additional information and consent from participants are required for particularly sensitive data. 

[To the top of the page ^](#legal_consents)

---



## Checklist {: #checklist}

- [x] What general consents did participants already have to provide in order to use the OpenOlat learning platform?
- [x] I have read and understood the General Terms of Use and the General Privacy Policy.
- [x] All course participants have already agreed to the General Terms of Use and the General Privacy Policy.
- [x] Are additional course-specific explanations required?
- [x] Are the texts for the course-specific explanations available?
- [x] Have the course-specific explanations already been integrated into the OpenOlat course?
- [x] Are they integrated in such a way that the course cannot be modified without prior consent?
- [x] Do the consent forms need to be filed and archived somewhere?
- [x] Are forms being used? Should a statement regarding the terms of use be included there?
- [x] Does the course use external tools that access other external servers?
- [x] Is separate consent required for these external tools?
- [x] Are courses shared with other learning platforms via LTI? Are there any legal issues regarding data transfer to or from those platforms?


[To the top of the page ^](#legal_consents)

---


## Further information {: #further_information}

[Terms of use >](../../manual_user/basic_concepts/Terms_Of_Use.md)<br>
[Terms of use: OpenOlat Platform >](../../manual_user/basic_concepts/Terms_Of_Use.md)<br>
[Terms of use: Course >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_course)<br>
[Terms of use: Form >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_form)<br>
[Terms of use: External tools >](../../manual_user/basic_concepts/Terms_Of_Use.md#terms_of_use_external_tools)<br>
[Terms of use: User management >](../../manual_admin/usermanagement/Data_protection.md)<br>
[Module Data privacy (Administration) >](../../manual_admin/administration/Modules.md#data_privacy)<br>

[To the top of the page ^](#legal_consents)
