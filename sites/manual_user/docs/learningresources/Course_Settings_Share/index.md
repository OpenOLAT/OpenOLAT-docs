# Course settings - Tab Share {: #tab_share}

In the Share tab, you define who uses your course and who manages it: where the members come from, whether participants book the course themselves and which organisations have administrative access to it. You open the tab under `Course > Administration > Settings > Tab "Share"`.

![Via the Administration tool menu and the Settings entry you reach the settings tabs, among them the Share tab](../assets/course_settings_share_entry_v1_en.png){ class="shadow lightbox" title="Administration menu of a course" }

In the Share tab, you will find these sections. Which of them a course actually shows depends on its usage: see [Which sections appear?](#sections_by_usage)

[Usage](#section_usage)<br>
[Share](#section_share)<br>
[Offer](#section_offer)<br>
[LTI 1.3 access configuration](#section_LTI)<br>
[Share overview](#section_share_overview)

---

## Which sections appear? {: #sections_by_usage}

The Share tab does not look the same for every course. What matters is the usage set in the [Usage section](#section_usage). A standalone course controls access, booking and leaving on its own and therefore shows all sections. For a course in the Course Planner, the Course Planner takes over these tasks, and the corresponding settings are dropped from the course. A template has no participants, so everything that concerns participant access is dropped there.

| Section or setting | Standalone | Use in Course Planner | Template |
|---|---|---|---|
| Usage | yes | yes | yes |
| Share: Access for participants | yes | no | no |
| Share: Direct link | yes | no | yes |
| Share: Participants can leave | yes | no | no |
| Share: Administrative access | yes | yes | yes |
| Share: Authors can | yes | no | yes, without "embed in groups" |
| Share: External OER catalogues and search engines | yes | no | no |
| Offer | yes | no | no |
| LTI 1.3 access configuration | yes | no | no |
| Share overview | yes | yes | yes |

For a course in the Course Planner, only the administrative access therefore remains in the Share section. Membership, booking and leaving are handled in the implementation in the Course Planner. The share overview is shorter too: it counts only the owners, because the course itself manages no coaches and no participants.

![With Use in Course Planner only the administrative access remains in the Share section, and the share overview counts only the owners as members](../assets/course_settings_share_cpl_v3_en.png){ class="shadow lightbox" title="Share tab of a course in the Course Planner · 2026.10.09" }

!!! info "Important"

    The External OER catalogues and search engines section additionally appears only if the OAI-PMH module is activated, and the administrative access only if the Organisations module is activated. The usage "Use in Course Planner" exists only if the Course Planner module is activated.

The descriptions of the following sections assume the usage "Standalone".

[To the top of the page ^](#tab_share)

---

## Section Usage [:octicons-tag-16:{ title="from Release 18.2.0 (OO-7277)" }](https://track.frentix.com/issue/OO-7277) [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9805)" }](https://track.frentix.com/issue/OO-9805){:target="_blank"} {: #section_usage}

The usage defines where the members of a learning resource come from: from its own member management, from the Course Planner or from the place where it is embedded. New courses are standalone as long as the Course Planner module is not activated.

![Usage Standalone with the Change link](../assets/course_settings_share_usage1_v1_en.png){ class="shadow lightbox" title="Usage section in the Share tab · 2026.10.09" }

**Standalone**<br>
Standalone learning resources have their own member management. To add new members, open `Course > Administration > Member management`.<br>
Participants get access via "Private", for example when course owners enter them as members, or via "Bookable and open offers", for instance with an access code or via an offer in the catalog.

**Use in Course Planner**<br>
If the course is integrated into a product of the Course Planner, the Course Planner assigns and manages the memberships. The course then does not require a second, standalone member management.

**Template**<br>
The Course Planner also manages these courses, they have no standalone member management. Unlike with "Use in Course Planner", the course serves for instantiation: OpenOlat creates the course of an implementation from this template only at a specific point in time (instantiated).

**Embedding**<br>
This usage exists only for learning resources that are not courses, for example a test or a form. The learning resource is reusable and has no standalone member management: it is embedded elsewhere, for instance in a course element, and the members come from there. More on this under [Provide for the usage of a learning resource](../General_Functions_Concept.md#usage).

Clicking "Change" opens the "Change usage" dialog. It shows the current usage at the top under "Current usage" and below it, under "Change usage to", the usages you can switch to. The current usage is therefore not in the selection. The help icon next to "Change usage to" shows a help text when you hover over it and opens this section of the manual when you click it.

Except for "Standalone", a course does not manage its members itself. OpenOlat therefore blocks a switch as soon as the course does not meet a precondition. A blocked usage appears in the dialog but cannot be selected. The dialog names the reasons above the selection, under the sentence "Due to the following preconditions, certain options are not available:":

- **No members except owners:** The course has coaches or participants. Blocks the switch to "Use in Course Planner" and to "Template".
- **No groups that are also referenced by other courses:** A group of the course is also embedded in another course. Blocks the switch to "Use in Course Planner" and to "Template".
- **"Access for participants" must be set to "Private":** In the Share section, "Bookable and open offers" is selected. Blocks the switch to "Use in Course Planner" and to "Template".
- **Not used by the Course Planner:** The course or the template is assigned to an implementation. Blocks every switch except the one from "Standalone" to "Use in Course Planner".

![Above the selection the dialog states why a switch is blocked, here because the course has coaches and participants; both usages therefore cannot be selected](../assets/course_settings_share_usage2_v3_en.png){ class="shadow lightbox" title="Change usage dialog for a course with members · 2026.10.09" }

If a course already has members, a copy is the simplest way into the Course Planner: it is created without coaches and participants and can be switched. The steps are described here:<br>
[If the usage cannot be changed >](../../../manual_how-to/course_planner_courses/course_planner_courses.md#embedding_locked)

!!! tip "Tip"

    When creating new courses, pay attention to the default usage setting. System administrators set the usage for new courses in the system administration, in the field "Usage for new courses" under:<br>
    `Administration > Modules > Course Planner > Tab "Settings"`

[To the top of the page ^](#tab_share)

---

## Section Share {: #section_share}

![Standalone course: access Bookable and open offers, direct link with buttons for copying and for the QR code, leaving At any time, administrative access, rights for authors](../assets/course_settings_share_share_v5_en.png){ class="shadow lightbox" title="Share section in the Share tab · 2026.11.09" }

#### Access for participants {: #section_share_access}

With "Private", course owners or persons with the right to manage members add the participants, under `Course > Administration > Member management`. This is like a personal invitation to the course.<br>
With "Bookable and open offers", the participants book the course themselves, depending on the offer with an access code. A booking via an offer in the catalog also requires this option.

#### Direct link {: #section_share_direct_link}

With the direct link, persons open the course directly without searching for it. If the person is not registered in OpenOlat or not logged in, the login screen appears first.

With "Copy to clipboard", you take the direct link into an e-mail or onto a web page. With "Show QR code", you show it as a QR code, for example on a notice, and with "Download PNG" you save the QR code as an image. How this works is described under [Copy links and pass them on as a QR code](../../basic_concepts/Navigation.md#url_field). [:octicons-tag-16:{ title="from Release 21.1.2 (OO-9982)" }](https://track.frentix.com/issue/OO-9982){:target="_blank"}

#### Participants can leave [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9272)" }](https://track.frentix.com/issue/OO-9272) {: #section_share_leave}

**At any time**: If participants wish to terminate their membership in the course themselves, they can do so at any time.<br>
**After course end date or status "Finished"**: Participants can only leave once the execution period has ended or the course has the status "Finished". If no execution period is set in the ["Execution" tab](../Course_Settings_Execution.md#execution_period), they can only leave with the status "Finished".<br>
**Never**: Attendance at the course is compulsory, so participants cannot withdraw themselves.

!!! info "Important"

    This setting exists only for courses with the usage "Standalone". If the Course Planner manages the course instead (usage "Use in Course Planner"), it does not appear in the Share tab, and the "Leave course" function is not available to the participants. If participants have booked an implementation, they cancel the booking themselves: They open the info page of the implementation in the catalog and select the action "Cancel booking" there. If a cancellation fee applies, the action is called "Cancel booking for a fee", and the confirmation dialog states the amount. The action appears only if the offer allows cancellation; whether only until the day before the start or at any time depends on the offer type and its setting (see [Cancellation](../../basic_concepts/Offer_Concepts.md#offer_cancellation)). Otherwise, the administration of your organisation can help. [:octicons-tag-16:{ title="from Release 20.0 (OO-8397)" }](https://track.frentix.com/issue/OO-8397)

#### Administrative access {: #section_share_admin_access}

With the administrative access, you assign the course to one or more organisations. This determines who besides the members can access the course: persons who have an administrative role in these organisations. Because these roles exist per organisation, for example learning resource manager of a department, you determine here which organisations have administrative access to your course. Per role:

- **Administrators and learning resource managers** have full access and find the course in Authoring.
- **Principals** read content and assessment data and also find the course in Authoring.
- **Course planners** read the content and use the course in the Course Planner.
- **Authors** of these organisations see the course from the status "Review" if you grant them at least one right under "Authors can".

You can select the organisations in which you have the role author, learning resource manager or administrator. The field is mandatory and only appears if the Organisations module is activated. The roles are described on the page [Roles and Rights](../../basic_concepts/Roles/index.md#org).

You can see how many people have administrative access in the [share overview >](#section_share_overview)

#### Authors can {: #section_share_authors}

Allow here what other authors may do with your course: "embed in groups", "copy" and "export content". For learning resources other than courses, the first option is called "embed".

#### External OER catalogues and search engines {: #section_share_oer}

To let external OER catalogues and search engines find your course, select the checkbox "Allow indexing of metadata": `Course > Administration > Settings > Tab "Share"`. OpenOlat then passes the metadata of the course on to portals and catalogues outside OpenOlat via OAI-PMH. (OER = Open Educational Resources)

This requires the OAI-PMH module, which your administration switches on. OpenOlat only passes the course on once it has the status "Published". If your administration requires specific licences, the course must also carry one of them. If the course is not published or lacks the required licence, a warning below the checkbox names the reason.

Find out more about OER here:<br>
How-to: [Release courses for indexing >](../../../manual_how-to/oai_pmh/oai_pmh.md#how-do-i-see-in-the-authoring-area-which-courseslearning-resources-are-enabled-for-indexing)<br>
Admin Manual: [Modul OAI PMH >](../../../manual_admin/administration/Modules_OAI.md)

[To the top of the page ^](#tab_share)

---

## Section Offer [:octicons-tag-16:{ title="from Release 17.0.0 (OO-6141)" }](https://track.frentix.com/issue/OO-6141) {: #section_offer}

![As long as access for participants is set to Private, the Add offer button is inactive, and the section states the reason](../assets/course_settings_share_offer_v2_en.png){ class="shadow lightbox" title="Offer section in the Share tab · 2026.10.09" }

For a course to appear in the catalog, you create an offer. If the same course is to be bookable under different conditions, you create several offers, for example free of charge for a specific target group and subject to a fee for others.

You create offers as soon as the option "Bookable and open offers" is selected in the "Share" section under "Access for participants". As long as "Private" is selected, the section shows a single heading "Offer" with the inactive button "Add offer".

With "Bookable and open offers", the section carries two headings "Offer". The upper one opens the section and shows where the course is offered. The lower one stands above the offers themselves.

**Upper heading "Offer"**<br>
The "Overview" box shows for "Internal catalog" and, if the external catalog is switched on, for "External catalog" whether the course is "Bookable" or "Not available" there. "Offered in subjects" lists the subjects from the "Metadata" tab, and the link "Open metadata" leads there. Under "Access", the link "Links" opens the addresses of the course in the internal and external catalog. If catalog 1.0 is switched on, the box lists under "Catalog" the categories in which the course is entered, instead of the subjects. If sorting by priority is switched on in the system administration, the "Settings" section follows with the [catalog priority when sorting](../../area_modules/catalog2.0_sort_offers.md#sorting_microsites_define_priority).

**Lower heading "Offer"**<br>
Here you create a new offer with the button "Add offer". Below it, each offer stands in a box of its own, with the links "Edit offer" and "Delete offer". If the course has no offer yet, "No offer created yet" appears there, and the offer types are also available as separate buttons.

For a new offer, the path therefore leads to the button under the lower heading:<br>
`Course > Administration > Settings > Tab "Share" > Section "Offer" > Button "Add offer"`

You can find more information about offers and the catalog here:<br>
[Catalog >](../../area_modules/catalog2.0/index.md)<br>
[Offer types >](../Offer_Types.md)<br>
[Create offers >](../../area_modules/catalog2.0_angebote.md)<br>
[Offering implementations in the catalog >](../../area_modules/Course_Planner_Implementations.md#tab_catalog)

[To the top of the page ^](#tab_share)

---

## Section LTI 1.3 access configuration [:octicons-tag-16:{ title="from Release 18.2.3 (OO-7664)" }](https://track.frentix.com/issue/OO-7664) {: #section_LTI}

If another LMS is to call up your OpenOlat course, you release it via LTI 1.3. For this, you set up a so-called deployment in this section. It defines the security measures and permissions for the external access.

You can find more information about sharing a course via LTI here:<br>
[Configuring LTI access to a course >](../LTI_Share_courses.md)

[To the top of the page ^](#tab_share)

---

## Share overview {: #section_share_overview}

![Member counts by role, assigned groups and products, plus the administratively authorised persons with their rights](../assets/course_settings_share_overview_v1_en.png){ class="shadow lightbox" title="Share overview in the Share tab · 2026.10.09" }

In the "Members" block, you will find the number of course members, broken down by owners, coaches, and participants. With "Open members management", you switch directly to the member management of the course.

The "Administrative access" block shows per role how many persons can also access this course due to this role, and with which right, for example "full access" for learning resource managers and administrators.

If the course is assigned to groups, the "Groups" block shows these groups.

If the course is assigned to a product in the Course Planner, the "Product" block shows the uses.

[To the top of the page ^](#tab_share)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[Function concept courses and learning resources >](../General_Functions_Concept.md)<br>
[How do I plan and run a course in several implementations with the Course Planner? >](../../../manual_how-to/course_planner_courses/course_planner_courses.md)<br>
[Navigation >](../../basic_concepts/Navigation.md)<br>
[Course Settings - Tab Execution >](../Course_Settings_Execution.md)<br>
[Offer concepts: Cancellation >](../../basic_concepts/Offer_Concepts.md)<br>
[Roles and Rights: Which roles are available? >](../../basic_concepts/Roles/index.md)<br>
[How can I have my courses found by search engines? >](../../../manual_how-to/oai_pmh/oai_pmh.md)<br>
[Module OAI-PMH >](../../../manual_admin/administration/Modules_OAI.md)<br>
[Catalog 2.0 - Sorting/order >](../../area_modules/catalog2.0_sort_offers.md)<br>
[Catalog 2.0 - Overview >](../../area_modules/catalog2.0/index.md)<br>
[Offer types >](../Offer_Types.md)<br>
[Catalog 2.0 - Offers >](../../area_modules/catalog2.0_angebote.md)<br>
[Course Planner: Implementations >](../../area_modules/Course_Planner_Implementations.md)<br>
[Course Settings - Tab Share: Configure LTI access to a course >](../LTI_Share_courses.md)

**Further reading**<br>
[Access configuration >](../Access_configuration.md)<br>
[Course Settings >](../Course_Settings/index.md)<br>
[Copy (a course) >](../Course_Copy.md)

[To the top of the page ^](#tab_share)
