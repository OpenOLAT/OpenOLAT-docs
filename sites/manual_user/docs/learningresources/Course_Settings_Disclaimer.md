# Course Settings - Tab Terms of use {: #tab_disclaimer}

If persons have to agree to rules before their first visit to the course, for example on the use of the content or on the visibility of their name, you store these rules in the "Terms of use" tab. Whoever starts the course reads the texts and confirms them before the course opens. In the members management you see who has consented. You find the tab under:<br>
`Course > Administration > Settings > Tab "Terms of use"`


## When the tab appears {: #requirements}

!!! info "Contact"

    To have it activated, contact your organisation.

The tab only exists for courses. You see it if the option "Course related terms of use and privacy policy" is switched on in the system administration, under `Administration > Modules > Course` ([Module Course](../../manual_admin/administration/Modules_Course.md#enable_course_option)).

Like all tabs of the [course settings](Course_Settings/index.md), it is visible to owners of the course, learning resource managers and administrators, and also to persons with the right "Course editor" from the [Members management](Members_management.md#section_rights).

[To the top of the page ^](#tab_disclaimer)


## Set up terms of use and privacy policy [:octicons-tag-16:{ title="from Release 15.0 (OO-4455)" }](https://track.frentix.com/issue/OO-4455){:target="_blank"} {: #setup}

In the tab you switch on two texts independently of each other: for "Terms of use" and for "Privacy policy" you tick the checkbox "Enabled". For each text you switch on, you fill in the following fields and then click "Save":

* **Title:** the heading under which participants read the text.
* **Terms:** the text itself.
* **Label checkbox 1:** the sentence that participants tick, for example "I accept".
* **Label checkbox 2:** optionally a second sentence that participants also tick.

![Terms of use and privacy policy can be switched on separately, each with a title, terms and up to two checkbox labels; here the privacy policy is switched on](assets/disclaimer_course_v2_en.png){ class="shadow lightbox" title="Form Course related terms of use · 2026.10.29" }

When a person starts the course, OpenOlat first shows the texts that are switched on. This applies to all persons in the course, including owners and coaches, and also to persons who visited the course before the texts were switched on. Once the person has ticked all checkboxes, "Accept" opens the course. With "Deny" the course stays closed. Guests accept again each time they open the course, because OpenOlat does not store their consent.

After consenting, participants can read the texts again at any time in the "My course" menu under ["Consent"](Toolbar_My_Course.md#terms_of_use). There they also withdraw their consent.

[To the top of the page ^](#tab_disclaimer)


## Change or switch off the texts {: #change}

If you change a text after persons have already consented, OpenOlat asks in the dialog "Updated configuration" whether all existing consents are revoked. This way, everyone agrees to the new version again before entering the course again.

If you switch off both texts, OpenOlat asks whether the existing consents are deleted.

[To the top of the page ^](#tab_disclaimer)


## View consents {: #consents}

You see which persons have accepted the conditions in the members management in the "Consents" area:<br>
`Course > Administration > Members management > Consents`

There you revoke or delete individual consents, see [Members management](Members_management.md#consent).

[To the top of the page ^](#tab_disclaimer)


## Further information {: #further_information}

**Mentioned on this page**<br>
[Module Course >](../../manual_admin/administration/Modules_Course.md)<br>
[Course Settings >](Course_Settings/index.md)<br>
[Members management >](Members_management.md)<br>
[Toolbar: My Course >](Toolbar_My_Course.md)

**Further reading**<br>
[Terms of Use >](../basic_concepts/Terms_Of_Use.md)

[To the top of the page ^](#tab_disclaimer)
