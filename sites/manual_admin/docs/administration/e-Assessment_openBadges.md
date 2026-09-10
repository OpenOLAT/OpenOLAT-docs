# e-Assessment Administration: OpenBadges {: #badges}

OpenBadges are implemented after the OpenBadges standard and fully compatible with it.
More information [here](https://www.imsglobal.org/activity/openbadges).

## Tab "Configuration" {: #tab_config}

* Here you can switch badges on/off for the entire instance of your OpenOlat.
* In addition, LinkedIn organizations that use badges can be added here.

![Activation of OpenBadges and management of LinkedIn organizations, tab "Configuration" in the OpenBadges administration](assets/badges_global_config_v2_de.png){ class="shadow lightbox" }


[To the top of the page ^](#badges)

---


## Tab "Templates" {: #tab_templates}

A standard set of templates is already instantiated on the OpenOlat instance.

![List of the prepared badge templates with image, name and scope, tab "Templates" in the OpenBadges administration](assets/badges_global_templates_v2_de.png){ class="shadow lightbox" }

Additional templates can be created by specifying the image, name and a description of the template.

![Form "Upload template" with the fields Image, Name, Description, Categories and Scope](assets/badges-admin-global-templates.de.jpg){ class="shadow lightbox" }

#### Name {: #name }

The name of the template is displayed in the wizard.

#### Description {: #description }

The description of the template is automatically taken from the template translation and cannot be edited here.

#### Categories {: #categories }

Here you can divide the templates into categories. Badge templates with the same category are displayed in the same tab in the wizard.

#### Scope {: #scope }

The scope defines whether a badge should be available globally (for issuing at instance level) or for courses.


[To the top of the page ^](#badges)

---


## Tab "Global badges" {: #tab_global_badges}

Global badges can be viewed in a separate tab, along with their status (active / in preparation) and whether they have already been awarded. They can also be edited and deleted. Global badges are not linked to a course.

![List of the global badges with image, name, status and number of awards, tab "Global badges" in the OpenBadges administration](assets/badges_global_tab_globalBadges_v2_de.png){ class="shadow lightbox" }

### Creating and editing a global badge

The tab "Global badges" also contains the button "Add global badge". It starts the badge tool (wizard) with the following steps:

1. **Template**: The first step is to select a template or upload your own image. SVG is currently supported.
![Selection of a template or upload of your own image, step "Image" in the badge tool for global badges](assets/badges-wizard_step1_v2_de.png){ class="shadow lightbox" }
2. **Customization**: If the template was created accordingly, you can change colors and text while creating the badge.
![Customization of the badge's background color and title with preview, step "Customization" in the badge tool for global badges](assets/badges-wizard_step2_v2_de.png){ class="shadow lightbox" }
3. **Award Criteria**: Enter the criteria and explanation for the rules you have chosen. Unlike badges awarded by authors in a course, global badges can, for example, also be awarded across courses for passing multiple courses.
![Criteria description and award method automatic or manual, step "Award Criteria" in the badge tool for global badges](assets/badges-wizard_step3_v2_de.png){ class="shadow lightbox" }
4. **Details & Validation Period**: Mandatory details are the name and description of the badge and the issuer. You can also add a URL and a contact to the exhibitor properties. The validity period can also be set so that it never expires or is 12 months, for example.
![Details such as name, description, issuer and expiration of the badge, step "Details" in the badge tool for global badges](assets/badges-wizard_step4_v2_de.png){ class="shadow lightbox" }
5. **Summary**: Screen with a summary of the key details.
![Summary of the details and award criteria before creating, step "Summary" in the badge tool for global badges](assets/badges-wizard_step5_v2_de.png){ class="shadow lightbox" }
6. **Recipients**: Displays the recipients in a table to see which participants already qualify according to the criteria you have selected.
![Table of participants who already qualify for the badge according to the selected criteria, step "Recipients" in the badge tool for global badges](assets/badges-wizard_step6_v2_de.png){ class="shadow lightbox" }

### Assign global badges manually

Manual assignment is possible under<br>
**Administration > e-Assessment > OpenBadges > Tab "Global badges" > Select badge > Tab Overview > Button "Assign manually"**.

![Navigation path to the button "Assign manually" via tab "Global badges", selecting a badge and tab "Overview", detail view of a global badge](assets/badges_global_manually_v3_de.png){ class="shadow lightbox" }

### Assign global badges automatically

Automatic assignment is set up in the wizard during creation.

!!! note "Note"

    When a global badge is assigned, the recipient is also automatically sent the badge by email, regardless of whether it is assigned manually or automatically.

[To the top of the page ^](#badges)

---

## Tab "Awarded global badges" {: #tab_awarded}

This tab lists **global badges** that have been awarded. (The course badges are not included here).

!!! note "Note"

    **Course badges** can be viewed by coaches and owners in the assessment tool. The automatically assigned course badges can be viewed there and course badges can be assigned manually.


!!! note "Note"

    For course participants, acquired badges are listed in the personal menu. [Here](../../manual_user/personal_menu/OpenBadges.md) for more information.

[To the top of the page ^](#badges)


---

## Tab "Verification" {: #verification}

In the "Verification" tab, you can upload a badge file. (You can simply drag and drop it into a field.) After clicking the "Verify badge" button, OpenOlat checks whether the badge was issued legitimately.

[To the top of the page ^](#badges)

---


## Further information {: #further_information}

[Badges in Assessment tool >](../../manual_user/learningresources/OpenBadges.md)<br>
[Personal achievements/successes: Badges >](../../manual_user/personal_menu/OpenBadges.md)<br>
[How do I award badges in my course? >](../../manual_how-to/badges/badges.md)<br>
[The OpenBadges standard >](https://www.imsglobal.org/activity/openbadges)<br>

[To the top of the page ^](#badges)


