# Payment modules: Invoice [:octicons-tag-16:{ title="from Release 20.0 (OO-8210)" }](https://track.frentix.com/issue/OO-8210){:target="_blank"} {: #invoice}

If there are booking requests in OpenOlat, Excel files can be exported there.
The strategy here is that the relevant data is transferred via these Excel files to other programs specialized in invoicing, where it can be further processed.

OpenOlat itself does not create invoices. Accordingly, reminders can neither be created nor managed in OpenOlat.

---

## Booking order with invoice [:octicons-tag-16:{ title="from Release 20.0 (OO-8211)" }](https://track.frentix.com/issue/OO-8211){:target="_blank"} {: #booking_order_with_invoice}

Booking orders with invoice are only created via offers of an implementation in the Course Planner.

To do this, offers are stored in the Course Planner. These (course) offers are displayed in an external catalog, for example, showing both the prices and the number of available places. 

Users can book these courses by registering from the catalog (if they are already OpenOlat users) or by signing up.

If an offer has been made in the catalog from the Course Planner that can be booked with an invoice, interested parties are guided through the registration process to enter their billing address, etc. A booking number is also created during this process.

The booking order then has the status "Open". After the payment has been received, the person who manages the implementation in the Course Planner sets it to "Paid" with «Set as "Paid"». This person writes off a claim that is no longer collected with "Write off booking order"; the participant's membership remains. What the statuses mean is described in [Offer types: Status of booking orders](../../manual_user/learningresources/Offer_Types.md#order_status).

You can also wait to create the corresponding OpenOlat course until it is certain that the implementation takes place.

In the Course Planner under:<br>
`Course Planner > Implementations > "your implementation" > Tab Catalog`<br>
in the "Booking orders" subsection, the booking orders are collected and can be exported as an Excel file.

If the [customer number](Modules_Organisations.md#customer_number) is switched on in the Organisations module, the Excel file also contains the customer number of the person, that of the billing address and that of the organisation to which the billing address belongs. This way, your accounting assigns each booking directly to the right account. All columns of the file are described on the page [Reports: Booking orders](../../manual_user/area_modules/Reports_BookingOrders.md). [:octicons-tag-16:{ title="from Release 21.1 (OO-9736)" }](https://track.frentix.com/issue/OO-9736){:target="_blank"}


[To the top of the page ^](#invoice)

---

## Further information {: #further_information}

[Offer types >](../../manual_user/learningresources/Offer_Types.md)<br>
[Module Organisations >](Modules_Organisations.md)<br>
[Reports: Booking orders >](../../manual_user/area_modules/Reports_BookingOrders.md)<br>
[Course Planner: Overview >](../../manual_user/area_modules/Course_Planner/index.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)

[To the top of the page ^](#invoice)