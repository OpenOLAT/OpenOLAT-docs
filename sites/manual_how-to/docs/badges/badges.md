# How do I award badges in my course? {: #badges}


??? abstract "Objectives and content of this instruction"

    If you have already created an OpenOlat course, you can award participants a badge as a reward for passing the course. These instructions show you how to do this.

??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants

    [ ] Beginners [x] Advanced users  [ ] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)
    * Familiarity with basic concepts of OpenOlat: actions for several selected entries, filters, [tables](../../manual_user/basic_concepts/Table_Concept.md) (show/hide columns), wizards


---

## Which badges can I award? {: #description}

Basically 3 categories of badges can be awarded:

* **Badges for a course**<br> (for passing the course or fulfilling the conditions set there)
* **Badges for a specific course element**<br> (like course badges, with a condition for a specific course element)
* and **global badges**<br> (cross-course, can only be created by administrators)


[To the top of the page ^](#badges)

---


## Conditions for awarding badges {: #conditions}

### General activation of badges {: #activation_general}

As a general prerequisite for the availability of badges

* the assignment option for the entire instance must have been activated by administrators, in the system administration under `Administration > e-Assessment > OpenBadges` (see [e-Assessment Administration: OpenBadges](../../manual_admin/administration/e-Assessment_openBadges.md))
* and a [matching badge created](#create).


### Activation of badges in a course {: #activation_course}

Course owners can determine when and which badge their course participants receive.

If badges are generally activated, the possibility of awarding badges can be activated for each course under:<br>
`Course > Administration > Settings > Assessment`<br>
with the toggle "Award badges" in the section "Badges". The settings are described on the page [Course Settings - Tab Assessment](../../manual_user/learningresources/Course_Settings_Assessment.md#section_badges).

Under "Allow manual awarding of badges" you specify who may award badges by hand: "for course owners" or additionally "for coaches".

![Section Badges with the toggle Award badges switched on and the options for course owners and for coaches](assets/badges_activation_course_v1_de.png){ class="shadow lightbox" title="Tab Assessment in the course settings" }


---

## How do I create a badge? {: #create}

(Course owners create the badges of a course. Administrators create global badges in the system administration.)

The following options are available for the image of a new badge:

* upload your own image (SVG or PNG, created with an external graphics program)
* use a template that administrators provide in the system administration
* take an existing badge as the starting point and copy its details. In addition, the action "Copy" in the badge list copies an existing badge.

As soon as awarding badges has been activated in a course, the course administration shows the entry "Badges":<br>
`Course > Administration > Badges`<br>
There you add new badges to your course with the button "Create a new badge".

A wizard will start and guide you step by step through the creation process.

![Menu Administration of a course with the highlighted entry Badges](assets/badges_create_menu_v1_de.png){ class="shadow lightbox" title="Menu Administration in the course" }

![Empty badge list with the button for creating a new badge](assets/badges_create_new_v1_de.png){ class="shadow lightbox" title="Page Badges in the course administration" }

The wizard has four to seven steps. Which steps appear depends on the starting point, on the selected image and on whether the course already has participants. The following sections are in the order of the wizard.


### Choose a starting point {: #create_starting_point}

If badges already exist in courses you own, the wizard starts with the choice of the starting point. With "Create a new badge" you start from scratch with image and criteria. With "Create from existing badge" you select an existing badge and copy its details, the wizard then goes directly to the award criteria. Without existing badges, the wizard starts directly with the image.


### Upload image or select template {: #create_1}

In this step you select a template or upload your own image with the tile "Own badge". The SVG and PNG formats are supported.

![Tile Own badge and twelve templates with thumbs up, star, cup and check mark on shield, circle or hexagon](assets/badges_create_wizard_step1_v1_de.png){ class="shadow lightbox" title="Step Image in the wizard" }

### Customize template {: #create_customization}

This step only appears for an SVG template that was created taking variables into account. You can then change colors and text in the template, for example the background color.

![Selection list Background color with gold, silver, bronze and further colors, next to it the preview of the badge](assets/badges_create_wizard_step2_v1_de.png){ class="shadow lightbox" title="Step Customization in the wizard" }


### Define award criteria {: #create_criteria}

Under "Criteria description", enter what the person has achieved. Under "Award procedure", select "Award automatically" or "Award manually only". Badges based on criteria can also be awarded manually.

![Mandatory field Criteria description, award procedure Award automatically or Award manually only, below the condition Course passed](assets/badges_create_wizard_step3_v1_de.png){ class="shadow lightbox" title="Step Award criteria in the wizard" }

When badges are created with the wizard, the rules for awarding them are also defined. Criteria/conditions can be

* a course has been passed
* a certain course score has been reached (prerequisite: score is switched on)
* the completion criterion was fulfilled for a specific course element
* a certain progress in the learning path has been achieved
* another badge has already been earned
* a course element has been passed
* a certain score was achieved in a certain course element

Several conditions can be combined with each other.


### Details & validity period {: #create_details}

Mandatory details are the name and description of the badge as well as the issuer. Under "Language", you specify in which language the badge is issued. For the issuer you can additionally enter an issuer URL and an issuer email. Under "Expiration", select "Never" or "Valid for" with a validity period, for example 12 months. OpenOlat assigns the version of the badge itself.

![Mandatory fields Name, Description and Issuer, as well as Language, Issuer URL, Issuer email and Expiration with validity period](assets/badges_create_wizard_step4_v1_de.png){ class="shadow lightbox" title="Step Details in the wizard" }


### Summary {: #create_summary}

You will receive a screen with a summary of all details and the rules for awarding for checking purposes.

![Preview of the badge with name, language, description, expiration and the rule: if the course is passed, then the badge is awarded](assets/badges_create_wizard_step5_v1_de.png){ class="shadow lightbox" title="Step Summary in the wizard" }


### Recipients {: #create_recipients}

This last step only appears if the course already has participants. With automatic awarding, the table shows which participants have already qualified for the badge according to the selected criteria. They receive the badge immediately after clicking "Finish". With manual awarding, you select here the participants who receive the badge after clicking "Finish".

![Recipient preview with the person who receives the badge immediately after finishing](assets/badges_create_wizard_step6_v1_de.png){ class="shadow lightbox" title="Step Recipients in the wizard" }

[To the top of the page ^](#badges)

---


## How do my course participants get a badge? {: #participants}

Badges can be awarded<br>
a) manually<br>
b) automatically on the basis of a condition and calculation<br>


### Manual assignment of badges {: #manual_award}

Manual assignment is possible for course owners and authorized coaches:<br>
a) **in the last step of the wizard**<br> (by course owners)<br>
b) **in the [assessment tool](../../manual_user/learningresources/Assessment_tool_overview.md)**<br>
    (in the participant list, select participants and then click on the button "Award badge")<br>
c) **in the badge list**<br>
    (under `Course > Administration > Badges`, select the badge and use the button "Award manually")


### Automatic awarding of badges {: #automatic_award}

Course owners set up automatic awarding in the wizard during creation: with the award procedure "Award automatically" and one or more conditions.

As soon as a change occurs in one of the assessable course elements, the fulfillment of the conditions for awarding a badge is checked again for all participants.


### Examples {: #examples}

**Example 1:**<br>
The "Bronze" badge is awarded automatically when 40 to 60 points have been achieved. The "Silver" badge is awarded automatically when 60 to 80 points have been achieved and the "Gold" badge when 80 to 100 points have been achieved.

**Procedure:**<br>
3 badges are created. Each badge has a rule with the condition "Course score". The various point limits are entered there.

**Example 2:**<br>
The "Gold" course badge is awarded automatically when 5 "Silver" badges have been earned in 5 course elements within a course.

**Procedure:**<br>
5 "Silver" badges are created, each containing the condition "Course element passed" or "Course element score".<br>
Then a 6th badge is created, which contains 5 conditions (all "Silver" conditions that were also created individually).
To do this, 5 conditions are specified in the wizard at the award criteria, each with the criterion "Another badge has already been earned".


### Subsequent allocation of a new badge to authorized persons {: #subsequent_award}

It is possible that course participants have already fulfilled the criteria for obtaining a badge before it is created. In this case, subsequent awarding can be triggered for this group of people in the last step of the wizard.

[To the top of the page ^](#badges)

---

## Where do course participants see their badges? {: #view_participant}

Participants find their badges

* in the course at the top right under `My course > My badges`
* in the [personal menu under "Badges"](../../manual_user/personal_menu/OpenBadges.md)
* If you qualify for a badge, it will also be sent by email and can be saved or forwarded as required (e.g. upload to LinkedIn).

[To the top of the page ^](#badges)

---

## Where can coaches/authors see who has received which badges? {: #view_coach}

Course owners as well as coaches with the right to award manually see awarded badges

* in the course at the top right under `My course > Awarded badges`
* in the course administration under `Course > Administration > Badges`
* in the assessment tool: select the top node of the course structure there and then a person. Their view shows the badges of this person and the button "Award badge".

[To the top of the page ^](#badges)

---

## Revoke badges {: #revoke}

(only available for course owners)

Badges that have already been awarded (e.g. also those awarded retroactively during the badge creation process in the "Recipients" step) can later be revoked under:<br>
`Course > Administration > Badges`<br>
via the menu with the three dots in the row of the badge concerned and the action "Revoke".

[To the top of the page ^](#badges)

---

## Delete Badges {: #delete}

(only available for course owners)

To delete a badge, click on the 3 dots at the end of the row of the desired badge under `Course > Administration > Badges` and then on "Delete".

![Menu with the three dots in the row of a badge with the actions Delete and Copy](assets/badges_delete1_v1_de.png){ class="shadow lightbox" title="Badge list in the course administration" }

In the dialog, you confirm with a checkbox that you want to delete the badge permanently. If the badge has already been awarded, you additionally choose what happens to the awarded badges:

1. "Revoke awarded badges": The badge is marked as deleted and removed from the badge list. All badges already issued are revoked.
2. "Remove awarded badges": All related information and criteria are permanently deleted, and the recipients no longer see the badges.

![Dialog for deleting a badge with the two options: delete the badge or delete the badge together with all issued badges](assets/badges_delete2_v1_de.png){ class="shadow lightbox" title="Dialog Delete badge" }


[To the top of the page ^](#badges)

---

## Checklist {: #checklist}

- [x] Are badges generally activated instance-wide by administrators?
- [x] Has awarding badges been activated in the course?
- [x] Should a self-designed image be used for a badge? Is it available as SVG or PNG?
- [x] Was a badge created with the wizard?
- [x] Has it been checked (and revoked if necessary) whether retroactively awarded badges were awarded correctly?
- [x] As the course owner/coach, have you checked the badges awarded in your course in the assessment tool?
- [x] Were the course participants informed about where they can view the badges they have earned?

[To the top of the page ^](#badges)


---


## Further information {: #further_information}

[How do I create my first OpenOlat course? >](../my_first_course/my_first_course.md)<br>
[Working with tables >](../../manual_user/basic_concepts/Table_Concept.md)<br>
[e-Assessment Administration: OpenBadges >](../../manual_admin/administration/e-Assessment_openBadges.md)<br>
[Course Settings - Tab Assessment >](../../manual_user/learningresources/Course_Settings_Assessment.md)<br>
[Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Personal achievements/successes: Badges >](../../manual_user/personal_menu/OpenBadges.md)<br>
[Badges >](../../manual_user/learningresources/OpenBadges.md)

[To the top of the page ^](#badges)
