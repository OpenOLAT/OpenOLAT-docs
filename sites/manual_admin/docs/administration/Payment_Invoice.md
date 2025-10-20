# Payment modules: Invoice {: #invoice}

Available on :octicons-tag-24: release 20

If there are booking requests in OpenOlat, Excel files can be exported there.
The strategy here is that the relevant data is transferred via these Excel reports to other programs specialized in invoicing, where it can be further processed.

OpenOlat itself cannot currently generate invoices. Accordingly, reminders, etc. cannot be created and managed directly in OpenOlat.

---

## Booking order with invoice {: #booking_order_with_invoice}

Booking orders with invoices can currently (as of release 20.1) only be created using the Course Planner.

To do this, offers are stored in the Course Planner. These (course) offers are displayed in an external catalog, for example, showing both the prices and the number of available places. 

Users can book these courses by registering from the catalog (if they are already OpenOlat users) or by signing up. 

If an offer has been made in the catalog from the Course Planner that can be booked with an invoice, interested parties are guided through the registration process to enter their billing address, etc. A booking number is also created during this process.

The booking request can then be confirmed. 

If the planned course actually takes place, a corresponding OpenOlat course may only be created then.

In the Course Planner under
**Implementations > Catalog tab > Booking orders tab**<br> the booking orders are collected and can be exported as an Excel file. 


[To the top of the page ^](#invoice)

---

## Further information {: #further_information}

[Course Planner >](../../manual_user/area_modules/Course_Planner.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)<br>
[Course Planner: Offers in the catalog >](../../manual_user/area_modules/Course_Planner_Implementations.md#tab_catalog)



[To the top of the page ^](#invoice)