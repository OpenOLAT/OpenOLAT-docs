# Offer concepts {: #offer_concepts}

## What is an offer? {: #offers}

Once courses and other learning content have been created in OpenOlat, it must be determined **which** users should have access to them **and when**. Access can be granted (approved) in two ways:

* **Private:** By entering them in the member management section of the course administration, registered OpenOlat users become members of the course or learning resource and can then access it.

* **Bookable and open offers:** An offer is added to a course by the owner (author). Users can then find this offer in the catalog and initiate membership themselves by booking the offer.<br>
Several different offers for different target groups can also be created for the same course.<br>
For example, a course can be offered free of charge to internal users, while a second offer provides the same course to external users for a fee.
Offers can also be displayed in the catalog for specific organizational units only. However, they can also be displayed for everyone; membership is not even required.

**Example of courses offered in the catalog:**
![Four course cards in the launcher "Selected learning resources" with type, title and subject, above them the search field on the start page of the catalog](assets/offer_concepts_example_v1_de.png){ class="shadow lightbox" }

[More about offers >](../area_modules/catalog2.0.md)

[To the top of the page ^](#offer_concepts)

---


## What can be shown in offers? {: #offers_card}

The visible part of the offer is displayed as a card in the catalog (or in the list view).
(The invisible part of an offer includes the rules: When and where is the offer displayed?)

What is displayed on a card in the catalog can be specified (uniformly for all cards) by administrators in the system administration under<br>
`Administration > Modules > Catalog > Tab Layout > Section Launchers`

* Implementation format
* Certificate
* Credit points
* Reference
* Type
* Title
* Teaser
* Authors
* Time required
* Main language
* Execution period
* Place of implementation
* Subjects / Catalog

[To the top of the page ^](#offer_concepts)

---


## Where can offers be displayed? {: #show_offers}

OpenOlat has an **internal** and an **external** catalog. You can specify whether an offer is displayed in only one or in both catalogs.

Within the catalog, there are sections called **launchers**. As the owner of a course or implementation, you can determine in which launcher your offer should appear. The offers are then dynamically compiled by the catalog (V2) and assigned to the various launchers. Taxonomy launchers can also display folders that correspond to specific taxonomy levels. This allows courses and learning resources to be displayed sorted by taxonomy terms.

An offer can also appear in **several different launchers of the catalog** (V2). For example, in a launcher called "Popular courses" and a launcher that compiles courses thematically based on a specific taxonomy.

Offers can also be displayed in catalog areas (launchers) that are visible **only to members of certain organizational units**. (This requires that the "Organisations" module is activated.)

You configure the release settings directly in the offer:<br>
Course: `Course > Administration > Settings > Share > Section "Offer" > Link "Edit offer"`<br>
Implementation: `Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers > Link "Edit offer"`

![Marked fields "Published in" with internal and external catalog and "Released for" with the selection of an organisational unit, dialog Freely available](assets/offer_concepts_share_org_v1_de.png){ class="shadow lightbox" }

!!! info "Important"

    Offers can be booked in the catalog as soon as their status has been set to "Published". (Or "provisional" or "confirmed" for implementations.)

!!! tip "Tip"

    Sorting can also be performed within a launcher.
    [Find out more >](../area_modules/catalog2.0_sort_offers.md)

[To the top of the page ^](#offer_concepts)

---


## Where can offers be created? {: #create_offers}

Offers are created

* in a course <br>or
* in an implementation (within the Course Planner)

### Create offers in courses [:octicons-tag-16:{ title="from Release 17.0.0 (OO-6141)" }](https://track.frentix.com/issue/OO-6141){:target="_blank"} {: #create_offers_course}

To offer a **course** in the catalog, select the relevant course and then<br>
`Course > Administration > Settings > Share > Section "Offer"`

![Marked button "Add offer" and the four offer types Access code, Freely available, PayPal Checkout and Without booking in the section Offer, tab Share of the course settings](assets/offer_concepts_create_offer_course_v1_de.png){ class="shadow lightbox" }

!!! tip "Tip"

    Once offers have been created, they can also be viewed under:<br>
    `Course > Administration > Offer types`<br>
    The entry appears as soon as a bookable offer has been configured for the course. Offers are configured under `Course > Administration > Settings > Share > Section "Offer"` (see above).<br>
    [Details on the offer configuration >](../learningresources/Access_configuration.md#offer)


### Create offers in the Course Planner [:octicons-tag-16:{ title="from Release 20.0 (OO-8301)" }](https://track.frentix.com/issue/OO-8301){:target="_blank"} {: #create_offers_implementation}

To offer an **implementation** in the catalog, select the relevant implementation in the Course Planner:<br>
`Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers`

![Marked tab Catalog and button Offers of an implementation, below them the button "Add offer", Course Planner](assets/offer_concepts_create_offer_implementation_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#offer_concepts)

---


## Offer types {: #offer_types}

The following offer types can be created:

|                       | Member status  |                                 | available in |
| --------------------- | --------------- |-------------------------------- | --- |
| <b>Without booking</b>    | without  |With this offer, the resource is accessible to users without a membership. | Single course |
| <b>Freely available</b>  | Membership | This offer allows the resource to be booked. Users receive a corresponding membership that gives them access to the resource. | Single course and implementation |
| <b>Access code</b> | Membership | With this offer, the resource can be booked with an access code. Users receive a corresponding membership that allows them to access the resource. | Single course and implementation |
| <b>PayPal Checkout</b> | Membership | With this offer, the resource can be booked for a fee using PayPal. Users receive a corresponding membership that gives them access to the resource. | Single course and implementation |
| <b>Invoice</b> | Membership | With this offer, the resource can be booked for a fee via invoice. Users receive a corresponding membership that gives them access to the resource. | Implementation |

When creating an offer, you select the offer type via the **"Add offer"** button.

![Expanded menu "Add offer" with the offer types Freely available, Access code, Invoice and PayPal Checkout, tab Catalog of an implementation](assets/offer_concepts_add_offer_types_v1_en.png){ class="shadow lightbox" }

[More about offer types >](../learningresources/Access_configuration.md#offer-options)

[To the top of the page ^](#offer_concepts)

---


## What can be offered? {: #what_is_offered}

The catalog can include offers for

- Courses
- Implementations
- other learning resources


### Offer courses [:octicons-tag-16:{ title="from Release 17.0.0 (OO-6141)" }](https://track.frentix.com/issue/OO-6141){:target="_blank"} {: #what_is_offered_courses}

Offers for a course are created under<br>
`Course > Administration > Settings > Share > Section "Offer"`<br>
Please note that the option "Bookable and open offers" must be selected beforehand under "Access for participants".

![Marked path via Administration and Settings to the tab Share with the button "Add offer" and the four offer types of a course](assets/offer_concepts_types_course1_v1_de.png){ class="shadow lightbox" }

![Selection of the offer type Without booking, Freely available, Access code or PayPal Checkout, grouped by membership and fee, dialog Add offer of a course](assets/offer_concepts_types_course2_v1_de.png){ class="shadow lightbox" }

Detailed information about [offering courses in the catalog can be found here >](../area_modules/catalog2.0_angebote.md)

[To the top of the page ^](#offer_concepts)

---


### Offer implementations [:octicons-tag-16:{ title="from Release 20.0 (OO-8301)" }](https://track.frentix.com/issue/OO-8301){:target="_blank"} {: #what_is_offered_implementations}

If the same course is to be offered several times on different dates, this can be done in the **Course Planner** using **implementations**.

Implementations can also be advertised in the catalog if it is still unclear whether they will actually take place (e.g., because they depend on the number of registrations/bookings). An offer for an implementation must therefore always be created in the Course Planner in the respective implementation and not in a course that is intended for this implementation. Courses can be specifically designated for use in implementations and then do not have their own member management.

Users can book these implementations by logging in from the catalog (if they are already OpenOlat users) or by registering as new users (if they have found a suitable course implementation in the external catalog, which they can view without registering).

If an offer has been made in the catalog from within the Course Planner that can be booked **with an invoice**, interested parties are guided through the registration process to enter their billing address, etc. A booking number is also generated. (This is only possible with the Course Planner.)

The booking order can then be confirmed.

Offers for implementations are created in the Course Planner under:<br>
`Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers`

![Marked path via Implementations and tab Catalog to the menu "Add offer" with Access code, Freely available, PayPal Checkout and Invoice, Course Planner](assets/offer_concepts_types_course_planner1_v1_de.png){ class="shadow lightbox" }

![Selection of the offer type Freely available, Access code, Invoice or PayPal Checkout without the offer type Without booking, dialog Add offer of an implementation](assets/offer_concepts_types_course_planner2_v1_de.png){ class="shadow lightbox" }

[More about offering implementations in the catalog >](../area_modules/Course_Planner_Implementations.md#tab_catalog)

[To the top of the page ^](#offer_concepts)

---


### Offer other learning resources {: #what_is_offered_other}

If individual videos or documents are to be offered in the catalog, courses with only one course element can be set up for each (e.g., course element Video or course element Document). Please note that when the course is called up, it automatically switches to the first course element.

The procedure for creating an offer is then identical to the offers for other independent courses.

The metadata and descriptions of such a "course" can only be adapted to the learning resource it contains, so that, for example, "Video xy" appears as an offer in the catalog.


[To the top of the page ^](#offer_concepts)

---

## Offers with payment {: #offer_payed}

### PayPal {: #offer_payed_paypal}

The PayPal payment module allows authors to unlock learning content in exchange for money. It must be set up and activated in advance in the system administration.

After the PayPal module has been configured successfully, the offer type "PayPal Checkout" is available when creating an offer: for courses under `Course > Administration > Settings > Share > Section "Offer"`, for implementations in the Course Planner and for groups in the [group administration](../groups/Group_Administration.md#booking).

[Setting up the PayPal payment module (Administration) >](../../manual_admin/administration/Payment_PayPal.md)


### Invoice [:octicons-tag-16:{ title="from Release 20.0 (OO-8210)" }](https://track.frentix.com/issue/OO-8210){:target="_blank"} {: #offer_payed_invoice}

Payment by invoice is only possible for implementations in the Course Planner.

For an offer with invoice,

* the membership is active immediately or
* the membership is initially pending until an administrative role confirms the reservation.


![Selection of the membership "Standard" (active immediately) or "With confirmation" (pending until confirmed), plus currency, price and cost center, dialog Invoice of an implementation](assets/offer_concepts_invoice_membership_v1_de.png){ class="shadow lightbox" }


!!! tip "Tip"

    The booking orders are collected per implementation:<br>
    `Course Planner > Implementations > "your implementation" > Tab Catalog > Button Booking orders`<br>
    The tabs of an implementation only appear once you have opened it in the table. There, the booking orders can be exported as an Excel file and used in another program (e.g., for invoicing).


[Setting up the invoice payment module (Administration) >](../../manual_admin/administration/Payment_Invoice.md)


### Cancellation policy for invoice offers [:octicons-tag-16:{ title="from Release 21.0 (OO-9382)" }](https://track.frentix.com/issue/OO-9382){:target="_blank"} {: #offer_invoice_cancellation}

When creating or editing an invoice offer, you define whether and under which conditions a booking can be cancelled. This way, users know the cancellation rules before they book.

![Enabled toggle "Cancelable" with the cancellation policy "With fee", the field Cancellation fee and the deadline "Cancellable free of charge until days before start", dialog Invoice](assets/offer_concepts_invoice_cancellation_v1_en.png){ class="shadow lightbox" }

* **Cost center:** Above the cancellation options, you can assign a cost center to the offer if required.
* **Cancelable:** This toggle determines whether bookings of this offer can be cancelled. The option is enabled by default.
* **Cancellation Policy:** If the offer is cancelable, choose between "Free of charge" (default) and "With fee".
* **Cancellation fee:** If "With fee" is selected, you enter the amount of the fee. With "Cancellable free of charge until \<number\> days before start" you additionally define a period during which cancellation is free of charge. In order for the deadline to be taken into account, a start date must be specified in the execution period.

The cancellation information is displayed to users with the offer.


### Credit points [:octicons-tag-16:{ title="from Release 20.1.1 (OO-8558)" }](https://track.frentix.com/issue/OO-8558){:target="_blank"} {: #offer_payed_credit_points}

Credit point systems can be set up in OpenOlat. A credit point system allows credit points to be collected across different learning opportunities. Using the "Credit points" module, you can define your own credit point systems globally. These enable participants to collect educational points/credits, such as ECTS or LearnCoins, for passing courses.

These points can also be used in certification programs for recertification, for example. Participants can earn credit points for each course they successfully complete. They can then use these credit points to purchase another course.

Organisations can define and name their own credit point systems and restrict them as needed, for example, by role or organisational area. After successfully completing a learning program, credit points can be assigned in a targeted manner to support long-term use for recertification.


[Activate credit points system-wide (Administration) >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Awarding credit points in courses >](../learningresources/Course_Settings_Assessment.md#section_credit_points)<br>
[Credit points in the personal menu >](../personal_menu/Credit_Points.md)

[To the top of the page ^](#offer_concepts)

---

## Further conditions for offers {: #further_boundary_conditions}

Additional conditions can be set for offers. Most configuration options are entered directly when creating a new offer.

![Options "Available in", membership "Standard" or "With confirmation", Booking receipt and "Automatic booking", dialog Freely available of an implementation](assets/offer_concepts_example1_v1_de.png){ class="shadow lightbox" }

* **Available if: Implementation status "Provisional" and "Confirmed":**<br>
An implementation does not have to be fully planned in order to publish an offer. For courses, the default condition is Course status "Published".

* **Available if: Custom condition:**<br>
The offer is only available in the selected statuses and additionally limited to a period, with fixed dates or relative to the execution period. [Details on availability >](../learningresources/Access_configuration.md) [:octicons-tag-16:{ title="from Release 21.0 (OO-9304)" }](https://track.frentix.com/issue/OO-9304){:target="_blank"}

* **Membership Standard:**<br>
The membership is active immediately after booking the offer.

* **Membership with confirmation:**<br>
The membership is initially pending. The reservation must be confirmed by an administrative role.

* **Booking receipt:**<br>
With the option "Send e-mail to participant", the booking person receives the booking receipt by e-mail after booking.

* **Automatic booking:**<br>
The membership is automatically created when the course is opened.
With automatic booking, the offer description is not displayed and users are only offered the "Open" action. This option should not be used in conjunction with other offers.

* Even with immediately active membership (implementations, offer with invoice), **acceptance of the privacy policy and other terms of use** is usually required first. Additional terms and conditions may be specified in the terms of use.

* A tender/offer for an implementation can be made even if it is still unclear whether the implementation will take place. A course does not even have to exist at the time the offer is created. If, on the other hand, an independent course is offered, the offer must be created in the course and only appears in the catalog once the course has been published.

* With an **offer of the type "Access code"**, the resource can be booked with an access code. Users receive a corresponding membership that allows them to access the resource.

[To the top of the page ^](#offer_concepts)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Catalog 2.0: Overview >](../area_modules/catalog2.0.md)<br>
[Catalog 2.0 - Sorting/order >](../area_modules/catalog2.0_sort_offers.md)<br>
[Access configuration >](../learningresources/Access_configuration.md)<br>
[Catalog 2.0 - Offers >](../area_modules/catalog2.0_angebote.md)<br>
[Course Planner: Implementations >](../area_modules/Course_Planner_Implementations.md)<br>
[Group Administration >](../groups/Group_Administration.md)<br>
[PayPal Configuration (Administration) >](../../manual_admin/administration/Payment_PayPal.md)<br>
[Payment modules: Invoice (Administration) >](../../manual_admin/administration/Payment_Invoice.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Course Settings - Tab Assessment >](../learningresources/Course_Settings_Assessment.md)<br>
[Personal achievements/successes: Credit points >](../personal_menu/Credit_Points.md)

**Further reading**<br>
[How do I present my courses in the OpenOlat catalog? >](../../manual_how-to/catalog/catalog.md)

[To the top of the page ^](#offer_concepts)
