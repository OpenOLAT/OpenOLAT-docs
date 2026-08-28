# Email Settings {: #email_settings}

The email settings are located in the system administration under: `Administration > Core functions > E-mail`. The page has two segments: "Settings" with the specifications for the email address and the OpenOlat inbox, and "E-mail template" with the appearance of the emails sent.

## User email address [:octicons-tag-16:{ title="from Release 12.2 (OO-2981)" }](https://track.frentix.com/issue/OO-2981) {: #email_address}

In the section "User email address" you define which limitations apply to the email address of the users. Below each of the two options, a link states the number of accounts without an email address or without a unique one. The link opens the list of these accounts in the user management.

![Mandatory and Unique switched off, one link each counts the affected accounts: section User email address](assets/email_EN.png){ class="shadow lightbox" }

### Mandatory

If this option is *not* activated, it means that the email address is optional for an account. However, this will lead to limitations, as OpenOlat is set up for every person having an email address. The following limitations occur (list is not exhaustive):

  * No real emails are sent.
  * No notifications are sent.
  * Login with the email address is not possible.
  * The password cannot be reset.

### Unique

If this option is not activated, it means that several accounts can have the
same email address. The following limitations occur (list is not exhaustive):

  * Login with the email address is deactivated in general. This means that nobody on the whole platform can log in with the email address any more, only with the username. This also applies to accounts with a unique email address.
  * For accounts without a unique email address, resetting the password only works by entering the username, no longer by the email address.

!!! warning "Attention"

    In both cases either no emails or no unique emails can be sent.
    Therefore we strongly recommend activating the internal OpenOlat inbox! Otherwise unexpected errors may occur!

## E-mail inbox and outbox {: #e-mail-inbox-and-outbox}

OpenOlat has an internal email inbox system that lists all emails sent and received within the system in the personal inbox of each person: [Personal tools: E-Mail](../../manual_user/personal_menu/E-Mail.md). The email inbox in OpenOlat is an optional component.

### Enable the OpenOlat inbox

  * If the OpenOlat inbox is switched off, all emails created in OpenOlat are sent exclusively to the personal email address. The OpenOlat inbox is not visible in the personal tools.
  * If the OpenOlat inbox is switched on, all received and sent emails are listed in the personal inbox of each person.

In addition, every person can define in their personal [settings](../../manual_user/personal_menu/Settings.md) whether received emails are delivered internally only or also to the personal email address. As an administrator you define the default behaviour:

  * Send emails to the internal OpenOlat inbox
  * Send emails to the internal OpenOlat inbox and the personal email address

### Inbox and outbox [:octicons-tag-16:{ title="from Release 12.2 (OO-2982)" }](https://track.frentix.com/issue/OO-2982)

For the inbox and the outbox you define separately what a person sees about the other recipients of an email. The same two switches are available in both areas:

  * "Show the name of the recipient"
  * "Show e-mail address"

## E-mail template {: #template}

OpenOlat sends emails for various events. To make the emails look more
attractive, they are sent as HTML emails including formatting. Using the email template you modify the general appearance of the emails.

The email template applies to all emails and controls only their appearance, not their text. You define the text of an individual email where the email originates: [Texts of individual emails](#mail_texts).

The following variables have to be in the template:

  *  **$content**: Is replaced with the actual content of the email. The content is usually adapted to the language of the recipient.
  *  **$footer**: Is replaced with the generic footer. The footer is adapted to the language of the recipient and can be modified for each language with the language adaptation tool. (see footer.no.userdata and footer.with.userdata from the package org.olat.core.util.mail)

### Texts of individual emails {: #mail_texts}

Several functions of OpenOlat come with their own mail text. You adapt this text in the respective function, not in the email template:

  * [Course reminders](../../manual_user/learningresources/Course_Reminders.md#text): subject and mail text of every reminder, with their own variables.
  * [Course Element "E-Mail"](../../manual_user/learningresources/Course_Element_EMail.md): subject and message as a template for the emails that the course element sends.
  * [Course Element "Test"](../../manual_user/learningresources/Course_Element_Test.md#tab_email_confirmation): subject and mail text of the confirmation after the test submission, either from the template or as your own text.
  * [Course Element "Task"](../../manual_user/learningresources/Course_Element_Task.md#submission): pre-formulated text of the confirmation after the final submission, adaptable in the tab "Submission".
  * [Correction workflow of a test](../../manual_user/learningresources/Test_settings.md#correction-workflow): mail text for the notification of the correctors, either as your own text or from a template.
  * [Certification program](../../manual_user/area_modules/Course_Planner_Certification_Programs.md#config_tab_messages): templates of the prepared notifications and of the reminders for the recertification, adaptable in the tab "Messages".
  * [Members management](../../manual_user/learningresources/Members_management.md#add_members): in the last step of the wizard "Add members" you formulate the email to the new members, likewise with variables.
  * [e-Assessment Administration: Test](e-Assessment_Test.md#tab_correction-workflow): system-wide pre-formulated mail templates for the actors of the correction workflow, in several languages.
  * [Life cycles: Account](Life_cycles_-_Administration.md#lifecycle_accounts): notifications before and after account expiry, deactivation and deletion, each step separately formulated.
  * [Automatic Group Lifecycle](Automatic_Group_Lifecycle.md): notifications before and after the inactivation as well as before and after the deletion of a group.

### Texts of the system emails {: #system_mails}

Many emails are created without any action by a person: the validation code for the registration, the message before an account expires or the confirmation when joining a group. For these system emails there is no text field in the administration. Their text is stored as a variable in the language package of the respective function.

You adapt the text with the language adaptation tool in the system administration under:<br>
`Administration > Customizing > Language adaptation tool`

The guide [How do I use the language adaptation tool?](../../manual_how-to/language_adaption_tool/language_adaption_tool.md) shows step by step how to find the variable for a text and how to change its value.

The obstacle is not the tool, but finding the variable: the mail texts are spread over the language packages of all functions that send emails. If you do not find the matching variable, contact the support of your OpenOlat instance. There you learn in which package the variable is located and what it is called.

## E-Mail signature [:octicons-tag-16:{ title="from Release 18.0 (OO-6616)" }](https://track.frentix.com/issue/OO-6616) {: #signature}

With the E-Mail signature, OpenOlat appends the personal text of a person to the end of the emails that this person sends from OpenOlat via an email form, for example via the course element E-mail, the course element Participant list or the member management. The text sits at the end of the message in the mail window, where it can still be edited before sending. Every person enters their signature themselves: [Profile](../../manual_user/personal_menu/Profile.md).

For the signature field to appear in the profile, activate the attribute "emailSignature" in the system administration under:<br>
`Administration > Customizing > User Properties`

**Step 1: Tab "Properties", activate the row "emailSignature"**

<details>
    <summary>Screen</summary>
	<img src="../assets/e-mail_settings_activate1_v1_de.png" alt="Column Active releases emailSignature system-wide: tab Properties of the page User Properties" />
</details>

**Step 2: Tab "Contexts", edit the context "org.olat.user.ProfileFormController"**

<details>
    <summary>Screen</summary>
	<img src="../assets/e-mail_settings_activate2_v1_de.png" alt="Link Edit opens the attribute list of org.olat.user.ProfileFormController: tab Contexts of the page User Properties" />
</details>

In the context, switch on the column "include" for "emailSignature". Only then is the field available in the profile.

<details>
    <summary>Screen</summary>
	<img src="../assets/e-mail_settings_activate3_v1_de.png" alt="Column include releases emailSignature for the personal profile: dialogue edit Context" />
</details>

The recommended setting:

![Only include switched on, Mandatory, Admin only and User readonly off: row emailSignature in the dialogue edit Context](assets/e-mail_settings_activate4_v1_de.png){ class="shadow lightbox" }

## Further information {: #further_information}

**Mentioned on this page**
[Personal tools: E-Mail >](../../manual_user/personal_menu/E-Mail.md)<br>
[Personal Configuration: Settings >](../../manual_user/personal_menu/Settings.md)<br>
[Course Reminders >](../../manual_user/learningresources/Course_Reminders.md)<br>
[Course Element "E-Mail" >](../../manual_user/learningresources/Course_Element_EMail.md)<br>
[Course Element "Test" >](../../manual_user/learningresources/Course_Element_Test.md)<br>
[Course Element "Task" >](../../manual_user/learningresources/Course_Element_Task.md)<br>
[Test settings - Administration >](../../manual_user/learningresources/Test_settings.md)<br>
[Course Planner: Certification programs >](../../manual_user/area_modules/Course_Planner_Certification_Programs.md)<br>
[Members management >](../../manual_user/learningresources/Members_management.md)<br>
[e-Assessment Administration: Test >](e-Assessment_Test.md)<br>
[Life cycles - Overview >](Life_cycles_-_Administration.md)<br>
[Automatic Group Lifecycle >](Automatic_Group_Lifecycle.md)<br>
[How do I use the language adaptation tool? >](../../manual_how-to/language_adaption_tool/language_adaption_tool.md)<br>
[Personal Configuration: Profile >](../../manual_user/personal_menu/Profile.md)

[To the top of the page ^](#email_settings)
