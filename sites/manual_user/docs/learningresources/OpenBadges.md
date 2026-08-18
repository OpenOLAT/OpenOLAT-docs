# Badges {: #badges}

## What is a badge? {: #what_is_a_badge}

Open Badges is a system of digital certificates or **learning badges** that they can use to award individual progress.<br>
A badge is online proof that a goal has been achieved. It consists of

* an image (svg or png)
* (possibly with an editable key term on the image)
* meta information (description of the goal achieved, period of validity of the badge, issuer of the badge, date of issue, etc.)
* a link

The difference between a paper certificate and an online badge is that the badge can be shared online via links. For example, it can be included in a CV or portfolio.
For example, a badge recipient can also include the badges on their LinkedIn profile.

In contrast to a formal certificate, the idea of the badge is more playful (gamification, to loosen up and motivate, the learners gain something).

---

## Where can badges be purchased? {: #badge_categories}

Basically 3 categories of badges can be acquired:

* **Badges for a course**<br> (for passing the course or fulfilling the conditions set out there)
* **Badges for a specific course element**<br> (like course badges, with a condition for a specific course element)
* and **global badges**<br> (cross-course, can only be created by administrators) 

Global badges are independent of courses. Other badges relate to a specific course element or course. The same badge cannot be awarded in different places, e.g. for different course elements.

[To the top of the page ^](#badges)


---

## How are course badges awarded? [:octicons-tag-16:{ title="from Release 18.0 (OO-7003)" }](https://track.frentix.com/issue/OO-7003) {: #award_a_course-badge}

Course badges can be awarded manually or automatically based on defined rules.

### Assign course badges manually

In each course, under<br>
`Course > Administration > Settings > "Assessment" tab > "Badges" section`<br>
manual assignment by course owners and coaches is made possible.

### Award course badges in the assessment tool

Badges can also be awarded manually in the assessment tool via a mass action.

### Course badges assigned automatically [:octicons-tag-16:{ title="from Release 19.0 (OO-7073)" }](https://track.frentix.com/issue/OO-7073) {: #award_criteria}

When creating a badge with the wizard, rules for the automatic awarding of a badge can be defined in the "Award criteria" step. Multiple rules are combined with "And". The badge is awarded as soon as all conditions are met.

The following criteria are available for course badges:

* **Course is passed**: The course is passed.
* **Course score**: The course score reaches a defined comparison value.
* **Course element passed**: The selected assessable course element is passed.
* **Course element score**: The score of an assessable course element reaches a defined comparison value.
* **Another badge has already been earned**: Another badge of this course has already been earned.

In learning path courses, the following criteria are additionally available:

* **Course element completion criterion met** [:octicons-tag-16:{ title="from Release 19.1 (OO-8046)" }](https://track.frentix.com/issue/OO-8046): The completion criterion of the selected course element is met.
* **Learning path progress**: The course progress reaches a defined percentage.

The selection for "Course element passed" and "Course element score" contains the assessable course elements of the course, e.g. test, task or checklist. Structure course elements cannot be selected. For a badge after completing a course section, therefore select the assessable course elements within this section as conditions.


[To the top of the page ^](#badges)

---

## How are global badges awarded? [:octicons-tag-16:{ title="from Release 18.0 (OO-6999)" }](https://track.frentix.com/issue/OO-6999) {: #award_a_global-badge}

Global badges can also be assigned manually or automatically based on defined rules.
However, both manual assignment and the definition of rules for the automatic assignment of global badges can only be carried out by [administrators](../../manual_admin/administration/e-Assessment_openBadges.md).

### Assign global badges manually

Global badges can be assigned manually by administrators in the system administration under<br>
`Administration > e-Assessment > OpenBadges > "Global Badges" tab > Button "Award manually"`

### Global badges assigned automatically

Administrators can set up the rules for automatic assignment in the system administration under<br>
`Administration > e-Assessment > OpenBadges > "Global Badges" tab`<br>
If the badge tool for creating a global badge is called up there, the rules can be specified in the wizard.

The following criteria are available for global badges:

* **Courses passed**: The selected published courses are passed.
* **Badges earned**: The selected other global badges have already been earned.


[To the top of the page ^](#badges)

---


## Create and edit a badge {: #create}

Badges can only be created within a course by course owners.

### Where can badges for _course elements_ be created? {: #create_for_course_elements}

**In the course editor:**<br>
Course elements that can display a "Passed" have an additional tab "Badges". There you will find a button "Create new badge".
It is available in the course elements:

* Test
* SCORM learning content
* Task
* Group task
* Assessment
* Check list
* LTI page
* Participant folder
* Portfolio task
* Structure

[To the top of the page ^](#badges)


### Where can badges be created for the _course_?

**In the course editor:**<br>
If you click on the top "node", the course title in the course menu, a "Badges" tab will also appear on the right. As with the course elements, you can create a badge there by clicking on the "Create new badge" button. Here, however, the badge refers to the course as a whole.

**In the course administration:**<br>
Under `Course > Administration > Badges` a list of all badges that can be acquired in this course appears. The "Create new badge" button can be used to create additional badges for the course and/or individual course elements.

You can find a step-by-step instruction for **course badges** [here](../../manual_how-to/badges/badges.md)

[To the top of the page ^](#badges)


### Where can _global_ badges be created?

The option to create **global badges** is described [here](../../manual_admin/administration/e-Assessment_openBadges.md).

[To the top of the page ^](#badges)


---

## Badge tool {: #badge_tool}

Badges are created in the badge tool. A wizard guides you through the creation process.<br> The tool is used (with minor differences) for both **course badges** and **global badges**.

[To the top of the page ^](#badges)

---

### The wizard

As soon as you have decided to create a new badge (click on the "Create new badge" button), a wizard will guide you through the creation process step by step.


1. **Image**: The first step is to select a template or upload your own image. SVG and PNG are currently supported.
![Image step in the badge wizard: selection of a badge template from motifs such as thumbs up, star, cup or check mark on shield, circle or hexagon, alternatively upload of an own badge.](assets/badges-wizard-1.de.jpg){ class="shadow lightbox" }

2. **Customization**: If the template was created with variables, you can change e.g. the background color and the title of the template. This step only appears for customizable templates.
![Customization step in the badge wizard: for the selected template, the background color bronze and the title are set, the preview shows the finished badge.](assets/badges-wizard-2.de.jpg){ class="shadow lightbox" }

3. **Details**: Mandatory details are the name, version and description of the badge, as well as the issuer. You can additionally add an issuer URL and an issuer email. The expiration can be set to "Never" or defined with a validity period, e.g. 12 months.
![Details step in the badge wizard with the mandatory fields name, version, description and issuer as well as issuer URL, issuer email and the expiration with validity period.](assets/badges-wizard-3.de.jpg){ class="shadow lightbox" }
   
4. **Award criteria**: Fill in the criteria description and choose the award procedure: automatic awarding based on the selected criteria, or manual awarding only via the assessment tool. The available criteria are described under [Course badges assigned automatically](#award_criteria).
![Award criteria step in the badge wizard: criteria description, award procedure automatic or manual only via the assessment tool, and the selected rule course is passed.](assets/badges-wizard-4.de.jpg){ class="shadow lightbox" }
   
5. **Summary**: Summary screen of all the details.
![Summary step in the badge wizard: badge preview with name, version, description and the award rule, when the course is passed, then the badge is awarded.](assets/badges-wizard-5.de.jpg){ class="shadow lightbox" }
   
6. **Recipients**: Shows in a preview which participants receive the badge based on the criteria immediately after "Finish". For manual awarding, you select the recipients here.

!!! note "Note"

    If entire courses are copied, the option to get badges is also included in the copy.


[To the top of the page ^](#badges)

---

### Where can badges be edited?

As long as a badge has not yet been acquired by anyone, the "Edit" option is available.

If the badge has already been acquired, the "Create a new version" action replaces editing. The image and the description can be changed. The award criteria and the validity period remain unchanged, and badges already awarded keep their previous version. The badge table shows the version in a separate column. [:octicons-tag-16:{ title="from Release 20.1 (OO-8287)" }](https://track.frentix.com/issue/OO-8287)

**In the course administration:**<br>
`Course > Administration > Badges` > Click on the 3 dots at the end of a row > Option "Edit"

If coaches have also been granted the right to assign badges manually under `Course > Administration > Settings > "Assessment" tab > "Badges" section`, then an overview is also available for coaches in the "Administration" menu under "Badges". However, coaches cannot create new badges, only assign them manually.

**In the course menu (as course owner):**<br>
Select a course element to which a badge can be added. [(Find the list of course elements with badges here)](#create_for_course_elements). Then click on the "Badges" tab. If a badge assignment has been set up for this course element, you can also click on the 3 dots at the end of a row and you will find the "Edit" option there.<br>

[To the top of the page ^](#badges)

---


## View of awarded course badges {: #assigned_badges}

The awarding of **course badges** is enabled by course owners in each course under<br>
`Course > Administration > Settings > "Assessment" tab > "Badges" section`<br>
The right to manual assignment can also be given to coaches here.

If badges have been activated, the **Badges** option will be available in **Course administration** after the next login. The rules for awarding badges for the course can be set up here.

If badges have been acquired by participants, they can be seen in the **performance overview** of the participant concerned.



### View awarded badges in LinkedIn and other websites {: #assigned_badges_LinkedIn}

The display of OpenOlat badges on other websites can be done manually by exporting and importing.

LinkedIn allows you to display certificates and badges in your personal profile. For this, the "Add to LinkedIn" button is available on the detail page of an acquired badge. OpenOlat passes the name, issuer, date of issue, validity period and the URL of the public badge page to LinkedIn, prefilled. The badge is checked there with a host-based verification. [:octicons-tag-16:{ title="from Release 19.0 (OO-7741)" }](https://track.frentix.com/issue/OO-7741)


[To the top of the page ^](#badges)

---

## Verify the authenticity of a badge {: #verification}

Administrators can upload a badge file, and OpenOlat will then verify whether it is a validly issued badge.

See [Verify badges >](../../manual_admin/administration/e-Assessment_openBadges.md#verification)<br>

[To the top of the page ^](#badges)

---


## Further information  {: #further_information}

[How do I award badges in my course? >](../../manual_how-to/badges/badges.md)<br>
[Global Badges >](../../manual_admin/administration/e-Assessment_openBadges.md#global_badges)<br>
[OpenBadges administration >](../../manual_admin/administration/e-Assessment_openBadges.md)<br>
[The OpenBadges standard >](https://www.imsglobal.org/activity/openbadges)<br>
[Verify badges >](../../manual_admin/administration/e-Assessment_openBadges.md#verification)<br>

[To the top of the page ^](#badges)


