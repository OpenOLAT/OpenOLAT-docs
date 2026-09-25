# Module Quality Management {: #Modules_Quality_Management}

The "Quality management" module is an additional module.
It must first be activated by an administrator.

The configuration of the module is carried out by administrators in the system administration under<br>
`Administration > Module > Quality Management`.

![Quality management in the system administration: switches for module, suggestion for improvement, data collection preview, and action to-dos, plus email fields for sender and recipient](assets/modules_quality_management_v1_de.png){ class="shadow lightbox" }

## Configuration quality management {: #settings_qm}

The entire module is activated with the first checkbox.

The optional email address can be used for individual customization:<br>
Each time data is collected, it is defined to whom emails are automatically sent.
The mails are always sent by OpenOlat with the standard address (no-reply).
This address can be overridden by entering a different email in this section.
The field "Sender email name" sets the name displayed for the sender.

## Configuration suggestion for improvement [:octicons-tag-16:{ title="from Release 13.0 (OO-3740)" }](https://track.frentix.com/issue/OO-3740) {: #settings_improvement}

If the option is activated, the option to create suggestions for improvement is displayed under the Quality management menu item. The emails created there are sent to the email address specified here.

## Data collection preview [:octicons-tag-16:{ title="from Release 18.2 (OO-7399)" }](https://track.frentix.com/issue/OO-7399) {: #data_collection_preview}

This preview is displayed after activation

* in courses
* in products
* in the "Quality management" module

If this option is activated, the "Data collection preview" option is displayed for course owners in the course administration menu. The planned surveys relating to this course can be viewed there. This preview is purely informative for course owners. Editing is only possible for quality managers.

See [User manual](../../manual_user/learningresources/Data_Collection_Previews.md)

In addition, the data collection preview can be called up in products and shows all surveys that relate to one of the elements.

The data collection preview in the "Quality management" module refers to all planned surveys (not just individual courses).

## Action to-dos [:octicons-tag-16:{ title="from Release 18.0 (OO-6781)" }](https://track.frentix.com/issue/OO-6781) {: #to_do}

To-dos can be created in various places in OpenOlat (projects, tasks, etc.). In quality management, we tend to talk about "measures" as a reaction to findings from a survey. A "measure" in quality management is a to-do.

If this option is activated, quality managers can create to-dos (measures).

## Activation of Site {: #site_activation}

For quality managers to find quality management in the main navigation, the activated module is not enough: the [site](../../manual_user/area_modules/index.md) "Quality management" must be activated as well. You activate it in the system administration under:<br>
`Administration > Customizing > Sites`

In the tab "Order", in the row "Quality management", set the checkbox in the column "Enabled" and define in the column "Access" who sees the site in the main navigation.

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[Data collection preview >](../../manual_user/learningresources/Data_Collection_Previews.md)<br>
[Area and modules >](../../manual_user/area_modules/index.md)

**Further reading**<br>
[Customizing: Overview >](Customizing.md)

[To the top of the page ^](#Modules_Quality_Management)