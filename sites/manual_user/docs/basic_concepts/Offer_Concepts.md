# Offer concepts {: #offer_concepts}

## What is an offer? {: #offers}

Once courses and other learning content have been created in OpenOlat, you determine which users access them and when. You grant access (release) in two ways:

* **Private:** If you enter registered OpenOlat users under `Course > Administration > Members management`, they become members of the course or learning resource and access it.

* **Bookable and open offers:** Owners add an offer to the course. Users find the offer in the catalog and become members by booking it.<br>
For the same course, you also create several offers for different target groups.<br>
For example, you offer a course free of charge to internal users and, with a second offer, for a fee to external users.<br>
Whether an offer appears in the catalog for everyone or only for specific organisational units is set in the offer, see [Where can offers be displayed?](#show_offers). With the offer type "Without booking", not even a membership is required, see [Offer types](#offer_types).

Groups have offers too. Users do not find a bookable group in the catalog but under `Groups > Published groups`, see [Offer groups](#what_is_offered_groups).

**Example of courses offered in the catalog:**
![Below the search field, the catalog shows its sections and a launcher with course cards, each card with format, reference, type and title](assets/offer_concepts_example_v1_en.png){ class="shadow lightbox" title="Start page of the catalog · 2026.11.09" }

[More about offers >](../area_modules/catalog2.0/index.md)

[To the top of the page ^](#offer_concepts)

---


## What can be shown in offers? {: #offers_card}

In the catalog, an offer appears as a card or as a row of the list view. In addition, there are rules that are not visible in the catalog: when and where the offer appears.

Which details a card shows is defined uniformly for all cards by system administrators in the system administration:<br>
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

OpenOlat has an internal and an external catalog. You determine whether an offer appears in one or in both catalogs.

The catalog shows offers of courses and of implementations. An implementation is the concrete run of an educational offer with a period, a place and members, for example a course that takes place in spring and once more in autumn. You plan implementations in the [Course Planner](../area_modules/Course_Planner/index.md), the module with which an organisation plans its educational offering.

The catalog is divided into sections, the launchers. Which launchers exist and by which rules they show offers is defined by system administrators, see [Tab Launch page (Administration manual)](../../manual_admin/administration/Modules_Catalog_2.0.md#tab_start_page). The catalog then compiles the offers dynamically and assigns them to the launchers. You do not choose a launcher in the offer itself. As the owner of a course, you influence the assignment through the subjects in the metadata of the course: taxonomy launchers show folders that correspond to specific taxonomy levels, and in them the courses and learning resources assigned to that level.

An offer also appears in several launchers of the catalog, for example in a launcher "Popular courses" and in a launcher that compiles courses thematically based on a specific taxonomy.

Offers also appear in launchers that only members of certain organisational units see. This requires that system administrators have switched on the module "Organisations" in the system administration under `Administration > Modules > Organisations`.

You set the release directly in the offer:<br>
Course: `Course > Administration > Settings > Tab "Share" > Section "Offer" > Link "Edit offer"`<br>
Implementation: `Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers > Link "Edit offer"`

![With "Published in" you choose the internal or external catalog, with "Released for" the organisational units whose members see the offer, here two units](assets/offer_concepts_share_org_v2_en.png){ class="shadow lightbox" title="Catalog section in the dialog Freely available of an implementation · 2026.11.09" }

!!! info "Important"

    An offer can be booked in the catalog as soon as the course has the status "Published". For an implementation, the status "Provisional" or "Confirmed" is sufficient by default. You set other conditions in the offer, see [Further conditions for offers](#further_boundary_conditions).

!!! tip "Tip"

    Within a launcher, you also define the order of the offers.
    [Find out more >](../area_modules/catalog2.0_sort_offers.md)

[To the top of the page ^](#offer_concepts)

---


## Where can offers be created? {: #create_offers}

You create offers in three places:

* in a course
* in an implementation in the Course Planner
* in a group under `Group > Administration > Tab "Share"`, see [Group administration: Tab Share](../groups/Group_Administration/index.md#booking)

The two subsections show the ways for courses and implementations. For groups, the group administration describes the tab "Share" in full.

### Create offers in courses [:octicons-tag-16:{ title="from Release 17.0.0 (OO-6141)" }](https://track.frentix.com/issue/OO-6141){:target="_blank"} {: #create_offers_course}

To offer a course in the catalog, open the course and select:<br>
`Course > Administration > Settings > Tab "Share" > Section "Offer" > Button "Add offer"`

The "Offer" section carries two headings "Offer": the upper one shows in the overview where the course is offered, under the lower one you find the button "Add offer" and the offers. More on this under [Section Offer](../learningresources/Course_Settings_Share/index.md#section_offer).

![In the section Offer you create the first offer with the button "Add offer" or directly with the offer types Without booking, Freely available, Access code and PayPal Checkout](assets/offer_concepts_create_offer_course_v1_en.png){ class="shadow lightbox" title="Share tab of the course settings · 2026.11.09" }

!!! tip "Tip"

    You see who booked your course through which offer under:<br>
    `Course > Administration > Offer types`<br>
    Despite its name, the menu item shows the booking orders of the course. It only appears once the course has an offer with booking, see [Offer types: When does the menu item appear?](../learningresources/Offer_Types.md#menu_visibility).<br>
    [Details on the offer configuration >](../learningresources/Access_configuration.md#offer)


### Create offers in the Course Planner [:octicons-tag-16:{ title="from Release 20.0 (OO-8301)" }](https://track.frentix.com/issue/OO-8301){:target="_blank"} {: #create_offers_implementation}

To offer an implementation in the catalog, open the implementation in the Course Planner and select:<br>
`Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers`

![In the Catalog tab of an implementation, the button Offers opens the offers, below it you create a new offer with "Add offer"](assets/offer_concepts_create_offer_implementation_v1_en.png){ class="shadow lightbox" title="Catalog tab of an implementation in the Course Planner · 2026.11.09" }

[To the top of the page ^](#offer_concepts)

---


## Offer types {: #offer_types}

The offer type determines how persons get access to a course, an implementation or a group: without booking, as a guest, with a free booking, with an access code or for a fee. Which offer types are available depends on whether you offer a course, an implementation or a group:

|                       | Member status  |                                 | available in |
| --------------------- | --------------- |-------------------------------- | --- |
| <b>Without booking</b>    | without  |With this offer, the resource is accessible to users without a membership. | Standalone course |
| <b>Guest</b>    | without  | With this offer, the resource is accessible to guests without registration. | Standalone conventional course, not a learning path course |
| <b>Freely available</b>  | Membership | This offer allows the resource to be booked. Users receive a corresponding membership that gives them access to the resource. | Standalone course, implementation and group |
| <b>Access code</b> | Membership | With this offer, the resource can be booked with an access code. Users receive a corresponding membership that allows them to access the resource. | Standalone course, implementation and group |
| <b>PayPal Checkout</b> | Membership | With this offer, the resource can be booked for a fee using PayPal. Users receive a corresponding membership that gives them access to the resource. Who creates this offer is described under [PayPal](#offer_payed_paypal). | Standalone course, implementation and group without waiting list |
| <b>Invoice</b> | Membership | With this offer, the resource can be booked for a fee via invoice. Users receive a corresponding membership that gives them access to the resource. | Implementation |

When creating an offer, you choose the offer type in the menu next to "Add offer" or in the dialog that a click on "Add offer" opens. The dialog groups the offer types by membership. If the course or the implementation does not have an offer yet, the same offer types are also available as buttons under "No offer created yet". In the tab "Share" of a group, you create offers in the same way.

[Offer types of a course in detail >](../learningresources/Access_configuration.md#offer-options)

### Offer types for courses {: #offer_types_courses}

A course with the usage "Standalone", in the table above "Standalone course", offers "Without booking", "Freely available", "Access code" and "PayPal Checkout". You choose the usage when creating the course in the field "Usage". Later you see and change it under:<br>
`Course > Administration > Settings > Tab "Share" > Section "Usage" > Link "Change"`<br>
If "Access for participants" is set to "Bookable and open offers", the dialog "Change usage" blocks the switch to "Use in Course Planner" and to "Template", see [Section Usage](../learningresources/Course_Settings_Share/index.md#section_usage).

The prerequisite for offers in the course is that "Access for participants" in the tab "Share" is set to "Bookable and open offers". The way to the button "Add offer" is shown in [Create offers in courses](#create_offers_course). Whether "PayPal Checkout" is available depends on the configured payment module and on your role, see [PayPal](#offer_payed_paypal).

![Menu next to Add offer with Without booking, Freely available, Access code and PayPal Checkout, the same offer types as buttons under No offer created yet](../learningresources/assets/offer_types_course1_v2_en.png){ class="shadow lightbox" title="Offer section in the Share tab of a course · 2026.11.18" }

![Without booking under Without membership, Freely available and Access code under With membership, PayPal Checkout under With membership - Chargeable](../learningresources/assets/offer_types_course2_v2_en.png){ class="shadow lightbox" title="Add offer dialog of a course · 2026.11.18" }

In a conventional course, that is not a [learning path course](../learningresources/Learning_path_course/index.md), the offer type "Guest" is also available. With it, you open the course to guests without registration, see [Roles and Rights: Guest access](guest_access.md).

### Offer types for implementations [:octicons-tag-16:{ title="from Release 20.0 (OO-8236)" }](https://track.frentix.com/issue/OO-8236){:target="_blank"} {: #offer_types_implementations}

An implementation in the Course Planner offers "Freely available", "Access code", "Invoice" and "PayPal Checkout". The way to the offers of the implementation is shown in [Create offers in the Course Planner](#create_offers_implementation). Whether "Invoice" and "PayPal Checkout" are available there depends on the configured payment modules, for "PayPal Checkout" also on your role, see [PayPal](#offer_payed_paypal) and [Invoice](#offer_payed_invoice).

![Menu next to Add offer with Freely available, Access code, Invoice and PayPal Checkout, the same offer types as buttons under No offer created yet](../learningresources/assets/offer_types_course_planner1_v2_en.png){ class="shadow lightbox" title="Offer section in the Catalog tab of an implementation · 2026.11.18" }

![Freely available and Access code under With membership, Invoice and PayPal Checkout under With membership - Chargeable](../learningresources/assets/offer_types_course_planner2_v2_en.png){ class="shadow lightbox" title="Add offer dialog of an implementation · 2026.11.18" }

### Offer types for groups {: #offer_types_groups}

A group offers "Freely available", "Access code" and "PayPal Checkout". Coaches of the group create the offers under `Group > Administration > Tab "Share"`. "PayPal Checkout" is only available as long as the waiting list is switched off in the tab "Description" of the group. In addition, the same prerequisites apply as for courses: the switched-on payment module and your role, see [PayPal](#offer_payed_paypal).

A group shows the tab "Share" if access control is switched on. System administrators set this in the system administration with the option "Enable resource access control":<br>
`Administration > Core functions > Access control`<br>
Persons who only have access to OpenOlat through an invitation do not see the tab. It is also missing for a group that is embedded in a course with the usage "Use in Course Planner", because there the Course Planner assigns the memberships.

[Offer types of a group in detail >](../groups/Group_Administration/index.md#booking)

[To the top of the page ^](#offer_concepts)

---


## What can be offered? {: #what_is_offered}

Offers exist for

- Courses
- Implementations
- Groups
- other learning resources

Courses and implementations appear with their offer in the catalog. You offer another learning resource as a course, see [Offer other learning resources](#what_is_offered_other). Groups appear under `Groups > Published groups`.


### Offer courses {: #what_is_offered_courses}

You create offers for a course under:<br>
`Course > Administration > Settings > Tab "Share" > Section "Offer" > Button "Add offer"`<br>
First select the option "Bookable and open offers" under "Access for participants" and click "Save". The section "Offer" then appears, and OpenOlat immediately opens the dialog "Add offer" for the first offer. Which offer types a course offers is shown in [Offer types for courses](#offer_types_courses).

Detailed information about [offering courses in the catalog can be found here >](../area_modules/catalog2.0_angebote.md)

[To the top of the page ^](#offer_concepts)

---


### Offer implementations {: #what_is_offered_implementations}

If you offer the same course several times on different dates, use implementations in the Course Planner.

You also advertise an implementation in the catalog if it is still unclear whether it will take place, for example because this depends on the number of bookings. You therefore always create the offer for an implementation in the implementation in the Course Planner, not in a course that is intended for this implementation. Courses can be designated specifically for implementations with the usage "Use in Course Planner" and then do not have their own member management, see [Offer types for courses](#offer_types_courses).

Users book an implementation by logging in from the catalog (if they are already OpenOlat users) or by registering as new users (if they have found a suitable implementation in the external catalog, which they can view without registering).

With an offer "Invoice", interested parties enter their billing address and further details when booking. OpenOlat creates a booking number in the process. The offer type "Invoice" exists only for implementations in the Course Planner.

OpenOlat records every booking through an offer as a booking order. The booking order is only created when the person completes the booking. If you select the option "With confirmation" under "Membership" in the offer, the membership of the booking person is then pending until someone accepts or declines it. This happens in two places:

* **In the Course Planner:** Whoever manages the members of the implementation selects "Pending" above the member list and decides with "Accept" or "Decline", for all persons at once with "Accept all":<br>
`Course Planner > Implementations > "your implementation" > Tab Members`<br>
See [Tab Members](../area_modules/Course_Planner_Implementations.md#tab_members).
* **In Coaching:** Line managers and education managers with the rights "View bookings" and "Pending course booking orders" decide in the tab "Bookings" of the person, see [Confirm pending memberships](../area_modules/Coaching_People.md#linemanager_educationmanager_confirm_membership).

With the option "Standard", the membership is active right after the booking.

Whether participants may cancel a booked implementation themselves is defined in the offer, see [Cancellation](#offer_cancellation).

If an implementation needs further details at booking, for example dietary requirements or prior knowledge, an offer of the implementation can require forms. The booking person fills them in as steps when booking, and the answers are then available with the booking order. This is only possible for offers of implementations in the Course Planner, not for course offers and not for the offer type PayPal Checkout. [Booking order forms >](../area_modules/Course_Planner_Implementations.md#booking_order_forms) [:octicons-tag-16:{ title="from Release 21.1 (OO-9724)" }](https://track.frentix.com/issue/OO-9724){:target="_blank"}

With forms, the booking becomes a wizard, and the booking order is only created in the last step. [Booking with forms as a wizard >](../area_modules/catalog2.0_angebote.md#offer_booking_wizard) [:octicons-tag-16:{ title="from Release 21.1 (OO-9742)" }](https://track.frentix.com/issue/OO-9742){:target="_blank"}

You create offers for implementations in the Course Planner under:<br>
`Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers`<br>
Which offer types an implementation offers is shown in [Offer types for implementations](#offer_types_implementations).

[More about offering implementations in the catalog >](../area_modules/Course_Planner_Implementations.md#tab_catalog)

[To the top of the page ^](#offer_concepts)

---


### Offer groups {: #what_is_offered_groups}

If people are to sign up for a group themselves, for example for a study group or a course-independent training, you offer the group. You create the offer under `Group > Administration > Tab "Share"`, which offer types are available is shown in [Offer types for groups](#offer_types_groups).

As soon as an offer exists, the group appears under `Groups > Published groups`. There users book it with "Join", see [Become a group member](../groups/Group_Membership.md). Groups do not appear in the catalog.

[More about offers of a group >](../groups/Group_Administration/index.md#booking)

[To the top of the page ^](#offer_concepts)

---


### Offer other learning resources {: #what_is_offered_other}

If you want to offer individual videos or documents in the catalog, set up one course with only one course element for each (e.g., course element Video or course element Document). Make sure that the course automatically switches to the first course element when it is opened.

You then create the offer as for any other independent course.

Adapt the metadata and description of this course to the learning resource it contains, so that, for example, "Video xy" appears as an offer in the catalog.


[To the top of the page ^](#offer_concepts)

---

## Offers with payment {: #offer_payed}

### PayPal [:octicons-tag-16:{ title="from Release 14.1 (OO-4203)" }](https://track.frentix.com/issue/OO-4203){:target="_blank"} {: #offer_payed_paypal}

With the PayPal payment module, authors offer learning content for payment. System administrators set up the module beforehand in the system administration under `Administration > Payment modules > PayPal` and switch it on.

Once the PayPal payment module is set up and switched on, the offer type "PayPal Checkout" is available when creating an offer: for courses under `Course > Administration > Settings > Tab "Share" > Section "Offer" > Button "Add offer"`, for implementations in the Course Planner and for groups in the [group administration](../groups/Group_Administration/index.md#booking).

An offer "PayPal Checkout" can only be created by persons with the role author, learning resource manager or administrator. Course owners and course planners without one of these three roles see the other offer types under "Add offer". The role administrator is not the same as the role system administrator, who sets up the payment module, see [Roles and Rights](Roles/index.md).

[Setting up the PayPal payment module (Administration manual) >](../../manual_admin/administration/Payment_PayPal.md)


### Invoice [:octicons-tag-16:{ title="from Release 20.0 (OO-8210)" }](https://track.frentix.com/issue/OO-8210){:target="_blank"} {: #offer_payed_invoice}

Payment by invoice exists only for implementations in the Course Planner.

For an offer with invoice,

* the membership is active immediately or
* the membership is initially pending until someone accepts it. Who does this is described under [Offer implementations](#what_is_offered_implementations).


![For the membership you choose "Standard", then the membership is active immediately, or "With confirmation", then it stays pending until someone accepts it](assets/offer_concepts_invoice_membership_v2_en.png){ class="shadow lightbox" title="Membership section in the dialog Invoice of an implementation · 2026.11.09" }


!!! tip "Tip"

    The booking orders are collected per implementation:<br>
    `Course Planner > Implementations > "your implementation" > Tab Catalog > Button Booking orders`<br>
    The tabs of an implementation only appear once you have opened it in the table. There, you export the booking orders as an Excel file, for example for invoicing in another program.


[Setting up the invoice payment module (Administration manual) >](../../manual_admin/administration/Payment_Invoice.md)

[To the top of the page ^](#offer_concepts)

---

## Cancellation [:octicons-tag-16:{ title="from Release 20.0 (OO-8397)" }](https://track.frentix.com/issue/OO-8397){:target="_blank"} {: #offer_cancellation}

If a person cannot attend a booked implementation after all, they cancel their booking themselves if the offer allows it. They do not need help from the administration. Cancelling a booking is only possible for an offer of an implementation. In courses and groups, participants leave instead, if the course or the group allows it:

| Offer in | What participants do | Who allows it | Where participants find it |
|---|---|---|---|
| Implementation in the Course Planner | Cancel booking | Course planners, product owners and element owners in the offer of the implementation, see the sections below | Info page of the implementation, depending on the implementation box "My educational product" or, for an implementation of type Single course, box "My course", see [Cancel booking](../learningresources/General_Functions_Infopage.md#cancel_booking) |
| Course | Leave course | Course owners with "Participants can leave" under `Course > Administration > Settings > Tab "Share"` | Info page of the course, box "My course", see [Leave course](../learningresources/General_Functions_Infopage.md#leave_course) |
| Group | Leave group | Group coaches with "Participants can leave the group" under `Group > Administration > Tab "Members"` | Column "Leave" in the list under `Groups`, see [Leave a group](../groups/Leave_a_Group.md) |

The following sections address course planners, product owners and element owners, the roles of the Course Planner, see [Roles and rights in the Course Planner](../area_modules/Course_Planner/index.md#roles_rights). Whether and until when participants can cancel depends on the offer type and its setting. The graphic shows the cases on a timeline:

![Timeline: how long participants can cancel their booking, by offer type and setting](assets/offer_concepts_cancellation_timeline_v1_en.svg){ class="shadow lightbox" title="Cancellation by offer type and setting · 2026.11.11" }

### Freely available and Access code [:octicons-tag-16:{ title="from Release 21.1.2 (OO-9977)" }](https://track.frentix.com/issue/OO-9977){:target="_blank"} {: #offer_cancellation_free_token}

With the toggle "Cancelable", you decide for the offers "Freely available" and "Access code" of an implementation whether participants may withdraw their booking themselves. If the toggle is off (default), only the administration of the implementation cancels a booking. The toggle is located in the offer directly below "Offer description":<br>
`Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers > Link "Edit offer"`

If it is switched on, you choose under "Participants can cancel":

* **At any time:** Participants also cancel after the start and for an implementation without a begin date, for example for an ongoing self-study offer. This option is preselected.
* **Until begin date:** Participants cancel until the day before the begin date, no longer on the day of the start. This way, the number of participants is fixed from the start. If the execution period has no begin date, the offer shows the warning "Participants can only cancel if a begin date is specified in the execution period!", and participants do not cancel themselves.

![If "Cancelable" is switched on, you define whether participants can cancel at any time or only until the begin date; without a begin date in the execution period, OpenOlat warns at "Until begin date"](assets/offer_concepts_cancellation_v1_en.png){ class="shadow lightbox" title="Dialog Freely available of an implementation · 2026.11.09" }

The execution period has a similar option, "Anytime", which means something else: the implementation is not bound to a period and therefore has no begin date, see [Execution in the settings](../area_modules/Course_Planner_Implementations.md#tab_settings_execution). For such an implementation, participants only cancel with the option "At any time" in the offer.

The current setting of the offer always applies, also to earlier bookings. If you switch "Cancelable" off, participants who have already booked no longer see the button "Cancel booking" either. With the update to Release 21.1.2, OpenOlat switches "Cancelable" off for all existing offers except "Invoice". If participants are to cancel an existing offer "Freely available" or "Access code" themselves, switch "Cancelable" on there.

You see which offers are cancelable in the list of offers under `Course Planner > Implementations > "your implementation" > Tab Catalog > Button Offers`. A cancelable offer shows the row "Cancelable" with the selected option, "At any time" or "Until begin date". If the row is missing, "Cancelable" is switched off.

!!! tip "Tip"

    The catalog does not show bookers whether an offer "Freely available" or "Access code" is cancelable. Therefore, write the rule in the "Offer description", for example "You can cancel your booking yourself until the day before the start."

### Cancellation policy for Invoice [:octicons-tag-16:{ title="from Release 21.0 (OO-9382)" }](https://track.frentix.com/issue/OO-9382){:target="_blank"} {: #offer_invoice_cancellation}

For the offer "Invoice", you define whether participants may cancel their booking and whether a fee applies.

![Enabled toggle "Cancelable" with the cancellation policy "With fee", the field Cancellation fee and the deadline "Cancellable free of charge until days before start"](assets/offer_concepts_invoice_cancellation_v1_en.png){ class="shadow lightbox" title="Dialog Invoice" }

* **Cost center:** Above the cancellation options, you can assign a cost center to the offer if required.
* **Cancelable:** This toggle determines whether participants may cancel their booking. It is switched on by default.
* **Cancellation Policy:** If the offer is cancelable, choose between "Free of charge" and "With fee".
* **Cancellation fee:** If "With fee" is selected, you enter the amount of the fee. With "Cancellable free of charge until \<number\> days before start" you additionally define a period during which cancellation is free of charge. After that, participants cancel with a fee until the day before the begin date. For the deadline to count, the execution period needs a "Start date"; if it is missing, the offer warns: "In order for the deadline to be taken into account, a start date must be specified in the execution period!"

For a new offer, OpenOlat takes the defaults of the payment module Invoice. If system administrators have entered a "Cancellation fee", that is a default cancellation fee, for the currency that the field "Currency" proposes in the new offer in the system administration under `Administration > Payment modules > Invoice > Configuration`, "With fee" is preselected with this amount, otherwise "Free of charge". OpenOlat also prefills the number of days for "Cancellable free of charge until" from the defaults.

Participants cancel until the day before the begin date of the implementation. Without a begin date in the execution period, they do not cancel themselves. For a booking, the toggle "Cancelable" and the cancellation policy apply as they were set at the time of booking; a later change to the offer only affects new bookings.

With "With fee", the catalog shows with the offer "Cancellation free of charge up to \<number\> days before start." or, without a deadline, "Not cancelable free of charge.", and the booking dialog states the cancellation fee. In the list of offers, the row "Cancelable" shows "Free of charge" or "With fee" for a cancelable offer.

### PayPal Checkout {: #offer_cancellation_paypal}

A booking with "PayPal Checkout" is cancelled by the administration of the implementation. The offer has no toggle "Cancelable", so a cancellation by participants cannot be set. How the administration cancels is described under [Cancellation by the administration](#offer_cancellation_management).

### Cancellation by the administration {: #offer_cancellation_management}

Whoever manages the members of the implementation, that is course planners, administrators and product owners, cancels a booking in the tab "Members" with "Cancel booking" in the menu of the member row:<br>
`Course Planner > Implementations > "your implementation" > Tab Members`<br>
This works for every offer type, also for "PayPal Checkout", and regardless of the toggle "Cancelable". It requires a booking order of the person, see [Tab Members](../area_modules/Course_Planner_Implementations.md#tab_members). If the person has none, for example because they were entered directly, "Cancel booking" is missing from the menu; you then take the person out of the implementation with "Remove".

[To the top of the page ^](#offer_concepts)

---

## Further conditions for offers {: #further_boundary_conditions}

You set further conditions for offers. You enter most configuration options directly when creating a new offer.

![Further conditions of an offer: "Available if" with implementation status or custom condition, the membership "Standard" or "With confirmation", the booking receipt by e-mail and auto-booking](assets/offer_concepts_example1_v2_en.png){ class="shadow lightbox" title="Catalog and Membership sections in the dialog Freely available of an implementation · 2026.11.09" }

* **Available if: Implementation status "Provisional" and "Confirmed":**<br>
An implementation does not have to be fully planned for you to publish an offer. For courses, the default condition is Course status "Published".

* **Available if: Custom condition:**<br>
The offer is only available in the selected statuses and additionally limited to a period, with fixed dates or relative to the execution period. [Details on availability >](../learningresources/Access_configuration.md) [:octicons-tag-16:{ title="from Release 21.0 (OO-9304)" }](https://track.frentix.com/issue/OO-9304){:target="_blank"}

* **Membership Standard:**<br>
The membership is active immediately after booking the offer.

* **Membership with confirmation:**<br>
The membership is initially pending until someone accepts it. Who does this is described under [Offer implementations](#what_is_offered_implementations). The option "With confirmation" exists only for offers of implementations, not for offers of courses and groups.

* **Booking receipt:**<br>
With the option "Send e-mail to participant", the booking person receives the booking receipt by e-mail after booking.

* **Auto-booking:**<br>
OpenOlat creates the membership automatically when the person opens the course. With auto-booking, OpenOlat does not show the offer description, and users only see the action "Open". Therefore, do not use this option together with other offers.

* Even with immediately active membership (implementations, offer with invoice), bookers usually first accept the privacy policy and further terms of use. In the terms of use, you define additional conditions if required.

* You also offer an implementation if it is still unclear whether it will take place. A course does not even have to exist when you create the offer. An independent course, on the other hand, is offered in the course, and the offer only appears in the catalog once the course has been published.

* With an offer "Access code", users book the resource with an access code. They receive a corresponding membership that allows them to access the resource.

[To the top of the page ^](#offer_concepts)

---

## Credit points in the catalog [:octicons-tag-16:{ title="from Release 20.1.1 (OO-8558)" }](https://track.frentix.com/issue/OO-8558){:target="_blank"} {: #offer_payed_credit_points}

Credit points are neither an offer type nor a payment method. A course awards them when participants complete it successfully. How many points a course awards is shown on its card in the catalog with the detail "Credit points", see [What can be shown in offers?](#offers_card).

With a credit point system, participants collect credit points across different learning opportunities, for example ECTS or LearnCoins. Organisations define and name their own credit point systems in the system administration under `Administration > e-Assessment > Credit points` and restrict them as needed, for example by role or organisational area. Certification programs use credit points, for example, for recertification.

[Activate credit points system-wide (Administration manual) >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Awarding credit points in courses >](../learningresources/Course_Settings_Assessment/index.md#section_credit_points)<br>
[Credit points in the personal menu >](../personal_menu/Credit_Points.md)

[To the top of the page ^](#offer_concepts)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Catalog 2.0: Overview >](../area_modules/catalog2.0/index.md)<br>
[Course Planner: Overview >](../area_modules/Course_Planner/index.md)<br>
[Module Catalog (Administration manual) >](../../manual_admin/administration/Modules_Catalog_2.0.md)<br>
[Catalog 2.0 - Sorting/order >](../area_modules/catalog2.0_sort_offers.md)<br>
[Course settings - Tab Share >](../learningresources/Course_Settings_Share/index.md)<br>
[Offer types >](../learningresources/Offer_Types.md)<br>
[Access configuration >](../learningresources/Access_configuration.md)<br>
[Roles and Rights: Guest access >](guest_access.md)<br>
[Learning path course - Overview >](../learningresources/Learning_path_course/index.md)<br>
[Catalog 2.0 - Offers >](../area_modules/catalog2.0_angebote.md)<br>
[Course Planner: Implementations >](../area_modules/Course_Planner_Implementations.md)<br>
[Coaching - People >](../area_modules/Coaching_People.md)<br>
[Become a group member >](../groups/Group_Membership.md)<br>
[Group Administration >](../groups/Group_Administration/index.md)<br>
[Roles and Rights: Which roles are available? >](Roles/index.md)<br>
[PayPal Configuration (Administration manual) >](../../manual_admin/administration/Payment_PayPal.md)<br>
[Payment modules: Invoice (Administration manual) >](../../manual_admin/administration/Payment_Invoice.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Course Settings - Tab Assessment >](../learningresources/Course_Settings_Assessment/index.md)<br>
[Personal achievements/successes: Credit points >](../personal_menu/Credit_Points.md)<br>
[General Functions: Info Page >](../learningresources/General_Functions_Infopage.md)<br>
[Leave a group >](../groups/Leave_a_Group.md)

**Further reading**<br>
[How do I present my courses in the OpenOlat catalog? >](../../manual_how-to/catalog/catalog.md)<br>
[User tools: Booking orders >](../personal_menu/Bookings.md)<br>
[Reports: Booking orders >](../area_modules/Reports_BookingOrders.md)

[To the top of the page ^](#offer_concepts)
