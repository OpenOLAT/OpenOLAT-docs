# Course settings - Tab Share {: #tab_share}

In the Sharing tab, you will find the following sections

 ![1_green_24.png](assets/1_green_24.png) [Verwendung](#section_usage)<br>
![2_green_24.png](assets/2_green_24.png) [Freigabe](#section_share)<br>
![3_green_24.png](assets/3_green_24.png) [Angebot](#section_offer)<br>
![4_green_24.png](assets/4_green_24.png) [LTI 1.3 Zugriffskonfiguration](#section_LTI)<br>
![5_green_24.png](assets/5_green_24.png) [Freigabeübersicht](#section_share_overview)<br>

<br>

![course_settings_share1_v1_de.png](assets/course_settings_share1_v1_de.png){ class="shadow lightbox"}

---

## ![1_green_24.png](assets/1_green_24.png) Section usage {: #section_usage}

If no Course Planner is used, the courses are independent.

![course_settings_share_usage1_v1_de.png](assets/course_settings_share_usage1_v1_de.png){ class="shadow lightbox"}

!!! warning "Attention"

    By clicking on "Change," you can select a different use. Please note, however, that member management is not carried out in the course for other uses. Therefore, it is no longer possible to make changes once members have already been added to a course. 

![course_settings_share_usage2_v1_de.png](assets/course_settings_share_usage2_v1_de.png){ class="shadow lightbox"}

**Independent**<br>
Independent learning resources have their own member management system. To add new members, open "Administration > Member Management" in the course.<br>
Access can be granted using the "Private" booking method by registering as a member (e.g., by course owners), by assigning an access code, or by publishing it in the catalog.

**Integration into product**<br>
If the course is integrated into a product, memberships are assigned and managed by the Course Planner. The course then does not require a second, separate membership management system.

**Template**<br>
These courses are also managed by the Course Planner and do not require separate member management. The difference to the "Use in Course Planner" option is that a template is used for instantiation. The course in a run is only created (instantiated) from this template at a specific point in time.

!!! hint "Note"

    When creating new courses, pay attention to the default usage setting. Administrators can set the default usage for new courses under **Administration > Modules > Module Courser Planner > Course Planner tab**.

[To the top of the page ^](#tab_share)

---

## ![2_green_24.png](assets/2_green_24.png) Section Share {: #section_share}
![course_settings_share_share_v1_de.png](assets/course_settings_share_share_v1_de.png){ class="shadow lightbox"}

**Access for participants**<br>
If you select **"Private"**, participants will be added by the course owner or persons who have member management rights. This is done in the course under "Administration > Member Management." It is therefore like a personal invitation to the course by the course owner.
When selecting the option **"Bookable and open offers"**, learners can book a course themselves, but may have to enter a password (depending on the settings). If the booking is to be made after selecting an offer in the catalog, this option must also be selected. 

**Direct link**<br> 
If you share this link, this course can be accessed directly. If the person is not yet known (registered) in OpenOlat and logged in, the login screen will appear first.

**Participants may withdraw.**<br>
**At any time:** If participants wish to terminate their membership in the course themselves, they can do so at any time.<br>
**After end date:** Participants may only terminate their course membership on their own initiative after the end of the implementation period. If this option is selected without first selecting an implementation period in the description, participants will not be allowed to leave the course at any time.<br>
**Never**: Attendance at the course is compulsory, so participants cannot withdraw themselves.

**Administrative Share**<br>
People with certain higher-level roles (e.g., administrators, learning resource managers) can also access this course from the organizational units selected here. Because these roles exist per organizational unit (e.g., admin for department xy), you can determine here which organizational units will have administrative access to your course.
If the Organizational Units module is not activated, you will only find a single organization here (usually "OpenOlat").<br>
You can see how many people have administrative access in the [share overview >](#section-share--section_share).

**Authors can**<br>
Allow other authors to reference, copy, or export their course here.

**External OER catalogs and search engines**<br>
OAI-PMH allows metadata from learning resources to be shared with Internet portals or catalogs outside OpenOlat, enabling search engines to find content more easily. (OER = Open Educational Resources)

The function must first be activated by an administrator.<br>
In order for the information about a specific course to be passed on to search engines, the respective author (course owner) must then allow this for their own course.

Find out more about OER here:<br>
How-to: [Release courses for indexing >](../../manual_how-to/oai_pmh/oai_pmh.md#wie-sehe-ich-im-autorenbereich-welche-kurselernressourcen-zur-indexierung-freigegeben-sind)<br>
Admin Manual: [Modul OAI PMH >](../../manual_admin/administration/Modules_OAI.md)

[To the top of the page ^](#tab_share)

---

## ![3_green_24.png](assets/3_green_24.png) Section offers {: #section_offer}

![course_settings_share_offer_v1_de.png](assets/course_settings_share_offer_v1_de.png){ class="shadow lightbox"}

In order for a course to be listed in the catalog, an offer must be created. Multiple offers can also be created if the same course is to be offered under different conditions (e.g., free of charge for a specific target group, subject to a fee for others).

In order to create an offer for the catalog, the option "Bookable and open offers" must be selected in the "Approval" section under "Access for participants." 

You can find more information about offers and the catalog here:<br>
[Catalog >](../area_modules/catalog2.0.md)<br>
[Offer types >](../learningresources/Offer_Types.md)<br>
[Create offers >](../area_modules/catalog2.0_angebote.md)<br>
[Offering bushings in the catalog >](../area_modules/Course_Planner_Implementations.md#tab_catalog)<br>

[To the top of the page ^](#tab_share)

---

## ![4_green_24.png](assets/4_green_24.png) Section LTI 1.3  {: #section_LTI}

OpenOlat courses can also be accessed from another LMS via LTI 1.3. However, this external access requires security measures and precisely defined permissions.<br>
In this section, you can set up a deployment to make the course accessible for another LMS.
You can find more information about sharing a course via LTI here:<br>
[Configuring LTI access to a course >](../learningresources/LTI_Share_courses.md)<br>

[To the top of the page ^](#tab_share)

---

## ![5_green_24.png](assets/5_green_24.png) Section Share Overview {: #section_share_overview}

![course_settings_share_overview_v2_de.png](assets/course_settings_share_overview_v2_de.png){ class="shadow lightbox"}

In the **Members** block, you will find the number of course members, broken down by owners, coaches, and participants.

The **Administrative Release** block lists all persons who also have access to this course due to their role.

If the course has been assigned to groups, you will find the relevant groups displayed in the **Groups** block.

If the course has been assigned to a product in the Course Planner, you will find the uses displayed in the **Product** block.

[To the top of the page ^](#tab_share)

---


## Further information {: #further_information}

[Access configuration >](../learningresources/Access_configuration.md)<br>
[Catalog >](../area_modules/catalog2.0.md)<br>
[Offer types >](../learningresources/Offer_Types.md)<br>
[Create offers >](../area_modules/catalog2.0_angebote.md)<br>
[Offering implementations in the catalog >](../area_modules/Course_Planner_Implementations.md#tab_catalog)<br>
[Configure LTI access to course >](../learningresources/LTI_Share_courses.md)<br>

[To the top of the page ^](#tab_share)

