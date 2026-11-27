# Terms of Use {: #terms_of_use}

## Which terms of use must be accepted?

When you use OpenOlat or certain elements of it for the first time, you may be required to agree to the terms of use. If this is required by the operating organisation or by the owners of a course or other element, various terms of use may be displayed for confirmation.

[Terms of use of the OpenOlat platform >](#terms_of_use_platform)

[Terms of use of a course >](#terms_of_use_course)

[Terms of use of a form >](#terms_of_use_form)

[Terms of use of external tools >](#terms_of_use_external_tools)

!!! note "Note"

    In addition to the terms of use, data protection provisions may also be displayed and require consent.


## Terms of use of the OpenOlat platform {: #terms_of_use_platform}

### Confirmation by OpenOlat users at the first login

At the first login, OpenOlat asks all users for their consent in the dialog "Terms of use". Only with "Accept" do you get into OpenOlat. If you deny, you stay on the login page.

![Text of the terms of use with the checkbox for consent, the Print link and the buttons Deny and Accept](assets/terms_of_use_platform_accept_v1_de.png){ class="shadow lightbox" title="Login page on the first login" }


### Define terms of use of the platform {: #terms_of_use_platform_define}

!!! info "Contact"

    For a change, contact your organisation.

Whether OpenOlat asks for consent at the first login is part of the server configuration and only applies after the next restart once changed. By default, the dialog is switched on.

System administrators adapt the text of the dialog in the system administration with the [language adaptation tool](../../manual_how-to/language_adaption_tool/language_adaption_tool.md):<br>`Administration > Customizing > Language adaptation tool`<br>
The text is one of the texts of the user interface. This is why it can be adapted separately for each activated language.

Separately from this, system administrators store a text "Terms of use" in the imprint:<br>`Administration > Customizing > Imprint`<br>
This text appears in the imprint under "Terms of use", not in the dialog at the first login. It can only be stored if the imprint is enabled, with a separate text for each activated language.

![In the row Terms of use, you store the text per language via its button, a checkmark shows an existing text](assets/terms_of_use_platform_define_v1_en.png){ class="shadow lightbox" title="Imprint page in the Customizing menu · 2026.11.27" }


### Read accepted terms of use {: #terms_of_use_platform_verify}

You can read the terms of use that you agreed to at the first login at any time in your personal menu:<br>`Personal menu > Settings > Tab "Terms of use"`

![In the personal menu, System settings opens the settings, where the Terms of use tab shows the accepted text with the date of your consent](assets/terms_of_use_pers_menu_v1_en.png){ class="shadow lightbox" title="Terms of use tab of the settings · 2026.11.27" }

[To the top of the page ^](#terms_of_use)


## Terms of use in the course settings [:octicons-tag-16:{ title="from Release 15.0 (OO-4455)" }](https://track.frentix.com/issue/OO-4455) {: #terms_of_use_course}

### Confirmation by participants in the course

Course owners can set their own terms of use for their course. The participants accept them when they call up the course for the first time. Anyone who declines cannot open the course.


### Define terms of use of a course {: #terms_of_use_course_define}

Course owners create course-specific terms of use for their course under:<br>`Course > Administration > Settings > Tab "Terms of use"`

The tab exists if the system administration has switched on the option "Course related terms of use and privacy policy" in the [module Course](../../manual_admin/administration/Modules_Course.md#enable_course_option). All fields of the tab are described on the page [Course Settings - Tab Terms of use](../learningresources/Course_Settings_Disclaimer.md).

The fields for the text appear as soon as you tick the checkbox "Enabled" next to "Terms of use". On the same tab, you can also switch on a course-related privacy policy; it has the same structure.

![With Terms of use enabled, you write the title, the terms in the text editor and the labels of checkbox 1 and 2](assets/terms_of_use_course_define_v1_en.png){ class="shadow lightbox" title="Terms of use tab of the course settings · 2026.11.27" }

In the field "Label checkbox 1" at the bottom of the page, you define which text is displayed to participants next to their checkbox for accepting the terms of use.

In addition, a second checkbox with any descriptive text can be defined for confirmation in the field "Label checkbox 2". If a text is entered, both checkboxes must be confirmed by the participants for the terms of use to be considered accepted. If no descriptive text is entered, the second checkbox is not displayed to the participants.

![In the field Label checkbox 2 you write the text of a second checkbox, here "I agree that ..."](assets/terms_of_use_course_checkbox2_v1_en.png){ class="shadow lightbox" title="Terms of use tab of the course settings · 2026.11.27" }


### Activate confirmation request for a course

The participants see the terms of use as soon as you tick the checkbox "Enabled" next to "Terms of use" and save. OpenOlat only saves the text while the checkbox is ticked. If you switch the terms of use off later, the last saved text is kept and appears again when you switch them on again.

![Once the checkbox Enabled next to Terms of use is ticked and saved, participants see the terms of use](assets/terms_of_use_course_activate_v1_en.png){ class="shadow lightbox" title="Terms of use tab of the course settings · 2026.11.27" }


### Management of the terms of use in the members management

Which participants have given their consent to the course-specific terms of use is visible to course owners in the [members management](../learningresources/Members_management.md) under:<br>`Course > Administration > Members management > Consents`

![In the Administration menu of the course, Members management leads to the consents](assets/terms_of_use_course_members_management1_v1_en.png){ class="shadow lightbox" title="Administration menu of the course · 2026.11.27" }

![Under Consents, the table shows who agreed to the terms of use and when, a revoked consent is struck through, and the buttons below revoke consents or delete entries](assets/terms_of_use_course_members_management2_v1_en.png){ class="shadow lightbox" title="Consents area of the members management · 2026.11.27" }

* If someone declines, the column "Consent" shows the note "Rejected or withdrawn". You can then contact the person directly.
* Course owners can revoke selected consents or delete the entries.


### Acceptance of terms of use when copying courses

[Learning path courses](../learningresources/Creating_learning_path_courses.md) can be copied with the help of a wizard: `Course > Administration > Copy with wizard`. In the wizard, you specify before copying which [course settings](../learningresources/Course_Settings/index.md) the copy takes over, including the terms of use.

![In the step Copy options, the row Terms of use decides with Customize, Copy or Don't copy whether the copy takes over the terms of use](assets/terms_of_use_course_copy_v1_en.png){ class="shadow lightbox" title="Copy course wizard, Copy options step · 2026.11.27" }

[To the top of the page ^](#terms_of_use)


## Terms of use in forms [:octicons-tag-16:{ title="from Release 13.0 (OO-3674)" }](https://track.frentix.com/issue/OO-3674) {: #terms_of_use_form}

### Confirmation when filling in

A form can also contain terms of use: the element "Terms of use" shows a letter of agreement with a checkbox. The person filling in the form ticks it. Without the tick, the form cannot be finished, OpenOlat then reports "Please give your consent first."

![Below the letter of agreement, the person filling in the form ticks the checkbox to give consent](assets/terms_of_use_form3_v1_en.png){ class="shadow lightbox" title="Participant view of a form · 2026.11.27" }

### Define terms of use of a form

Authors add the letter of agreement to the learning resource Form in the [form editor](../learningresources/Form_Editor/index.md) as the element "Terms of use": via "Add content", in the group "Organisational". In the element, you set the text and the label of the checkbox in the fields "Letter of agreement" and "Agreement label". In the tab "Style" of the inspector, you place the element in a highlighted box with the switch "Alert box".

![In the dialog Add content, you find the element Terms of use in the group Organisational](assets/terms_of_use_form1_v1_en.png){ class="shadow lightbox" title="Add content dialog in the form editor · 2026.11.27" }

![In the fields Letter of agreement and Agreement label you write the text and the label of the checkbox, in the Style tab of the inspector you switch on the Alert box](assets/terms_of_use_form2_v1_en.png){ class="shadow lightbox" title="Element Terms of use in the form editor · 2026.11.27" }

[To the top of the page ^](#terms_of_use)


## Terms of use of external tools {: #terms_of_use_external_tools}

In OpenOlat, external tools are integrated in some places, mostly also open source, but not developed by frentix. When such a tool opens a document, data goes to an external server. Depending on the setting, OpenOlat asks for your consent first.

Example **draw.io**<br>
draw.io is an online tool for creating diagrams that can be used in many places in OpenOlat, for example in projects, in the portfolio, in the "Document" course element, in the Media Center and wherever new documents can be created. In draw.io, several people can also work together on a diagram.

If the option "Confirmation of data transfer" is switched on for draw.io, OpenOlat shows the dialog "Confirmation of data transfer" when you open a diagram for the first time. It explains that the document is temporarily saved on an external server and that your name is passed to the editor. With "I accept the data transfer" you open the diagram, after that OpenOlat does not ask you again. System administrators switch the option on in the system administration:<br>`Administration > External tools > draw.io`

[To the top of the page ^](#terms_of_use)


## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I use the language adaptation tool? >](../../manual_how-to/language_adaption_tool/language_adaption_tool.md)<br>
[Module Course >](../../manual_admin/administration/Modules_Course.md)<br>
[Course Settings - Tab Terms of use >](../learningresources/Course_Settings_Disclaimer.md)<br>
[Members management >](../learningresources/Members_management.md)<br>
[Creating learning path courses >](../learningresources/Creating_learning_path_courses.md)<br>
[Course Settings >](../learningresources/Course_Settings/index.md)<br>
[The form editor >](../learningresources/Form_Editor/index.md)

**Further reading**<br>
[External Tools: Overview >](../../manual_admin/administration/External_Tools_-_Administration/index.md)<br>
[Data protection >](../../manual_admin/usermanagement/Data_protection.md)<br>
[Personal Configuration: Settings >](../personal_menu/Settings.md)

[To the top of the page ^](#terms_of_use)
