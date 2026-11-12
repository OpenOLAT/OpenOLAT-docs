# General Functions: Info Page {: #general_functions_info}

## What's the purpose of the info page? [:octicons-tag-16:{ title="from Release 10.0 (OO-984)" }](https://track.frentix.com/issue/OO-984){:target="_blank"} {: #purpose}

Anyone deciding whether a course is the right one finds everything that matters before booking or opening it on the info page: description, events, objectives, teachers and the price. Every learning resource has an info page, and so does every implementation in the Course Planner. OpenOlat generates part of the information itself, the owners of the learning resource enter the rest in the settings. Once the learning resource is published, interested users see the info page, even without a booking and before they enter the learning resource. This is particularly useful if you want to inform the target audience in advance, for example for a course with a fee.

In a course, you open the info page via the link "Info page" in the toolbar, in the course overview and in the catalog via "Learn more". The ways to open it are described under [How do you access the info page?](#access).

![Info page of a course with actions, facts, sections, Get started with booking, events, license, rating and comment](assets/general_functions_infopage_course_example_v1_en.png){ class="shadow lightbox" title="Info page of a course · 2026.09.29" }

[To the top of the page ^](#general_functions_info)

---


## Content of the info page [:octicons-tag-16:{ title="from Release 21.1 (OO-8728)" }](https://track.frentix.com/issue/OO-8728){:target="_blank"} {: #content}

The info page separates two questions into two columns. The left column shows what it is about: header, facts, sections, license and rating. The right column shows what concerns you and what you can do next: cover image, "Get started", "My course" and events.

The table shows what the info page consists of, from top to bottom. The column "In the image" tells you whether the element can be seen in the image above. The paths refer to the settings of the learning resource: `Course > Administration > Settings`. "Course only" means that other learning resources do not have this setting. An element only appears if it has content.

| Element | In the image | Set as author under | Only with administration |
|---|---|---|---|
| **Header** | | | |
| Reference | yes | Tab "Metadata" | no |
| Type | yes | automatic | no |
| Title | yes | Tab "Metadata" | no |
| Set bookmark | yes | automatic | no |
| [Share](../basic_concepts/Navigation.md#share): shares the link to the info page, from the catalog and for an implementation the link to the offer [:octicons-tag-16:{ title="from Release 21.1 (OO-9693)" }](https://track.frentix.com/issue/OO-9693){:target="_blank"} | yes | automatic | no |
| Download as PDF | yes | automatic | PDF Generator |
| Teaser | yes | Tab "Info" | no |
| Implementation format | yes | course only: Tab "Metadata" | no |
| Subjects | yes | Tab "Metadata" | Taxonomy |
| **Right column** | | | |
| Cover image or teaser movie | yes | Tab "Info" | no |
| [Get started](#get_started) with booking or opening [:octicons-tag-16:{ title="from Release 20.2 (OO-9042)" }](https://track.frentix.com/issue/OO-9042){:target="_blank"} | yes | automatic, offers under Tab "Share" | no |
| My educational product with [Cancel booking](#cancel_booking) | no | implementation only: automatic for participants if the offer allows cancellation | no |
| [My course](#my_course): progress, status, score, grade, groups and [Leave Course](#leave_course), for an implementation of type Single course "Cancel booking" | no | automatic for members; progress, status, score and grade course only | no |
| Events | yes | course only: Tab "Info", "Display on info page" | Events / Absences |
| **Facts** | | | |
| Execution period | yes | course only: Tab "Execution" | no |
| Events | yes | course only: Tab "Info", "Display on info page" | Events / Absences |
| Location | yes | course only: Tab "Execution", field "Location" | no |
| Authors / taught by | yes | Tab "Info" | no |
| Main language | yes | Tab "Info" | no |
| Expenditure of work | yes | Tab "Info" | no |
| Credit points | no | course only: Tab "Info", "Display on info page" | Credit points |
| Certificate | yes | course only: Tab "Info", "Display on info page" | no |
| Participants | no | implementation only | no |
| **Sections** | | | |
| Description | yes | Tab "Info" | no |
| Outline | no | implementation only | no |
| Meet your teachers | yes | course only: Tab "Info", "Display on info page" | no |
| Objectives | yes | course only: Tab "Info", section "Additional information" | no |
| Requirements | yes | course only: Tab "Info", section "Additional information" | no |
| Certification | yes | course only: Tab "Info", section "Additional information" | no |
| Categories | no | Tab "Catalog" | Catalog V1 |
| **Bottom** | | | |
| License | yes | Tab "Metadata" | Licenses |
| Rating | yes | automatic | Rating |
| Comments | yes | automatic | Comment |

Some elements only appear once system administrators have switched on the corresponding module in the system administration. The button "Download as PDF" requires the [PDF Generator](../../manual_admin/administration/External_Tools_-_Administration/index.md#pdf_generator). System administrators switch on rating and comments in the [Module Learning resource](../../manual_admin/administration/Modules_Learning_Resource.md), licenses under [Licenses](../../manual_admin/administration/Licenses.md), subjects in the [Module Taxonomy](../../manual_admin/administration/Modules_Taxonomy.md). Events require the [Module Events and Absences](../../manual_admin/administration/Modules_Events_and_Absences.md). System administrators set up credit points in the [e-Assessment Administration](../../manual_admin/administration/e-Assessment_Credit_Points.md).

The info page does not show technical details such as the ID, the external link and the responsible persons. They are in the window "About this course", see [About this course: Open the window](../learningresources/Technical_Information_on_Resources_and_Usage.md#open).

!!! note "Note"

    If you, as a participant, can hardly find any information on the info page, the owners of the learning resource have not set up the page further yet. Ask your coaches about it.

On a smartphone or in a browser window narrower than 992 pixels, all boxes are shown in one column, one below the other. The order is fixed: cover image, header, "Get started", "My course", facts, sections, events, license and rating. From a width of 768 pixels, the cover image is next to the title, as in the following image.

![Info page in a narrow window in one column: title with the cover image next to it, below it Get started, My course and Facts one after the other](assets/general_functions_infopage_narrow_v1_en.png){ class="shadow lightbox" title="Info page in a narrow window · 2026.10.20" }

[To the top of the page ^](#general_functions_info)

---


## Get started and My course {: #get_started_my_course}

The right column of the info page shows what you can do next and how far you have got in the course. The box "Get started" takes you into the course or to the booking, the box "My course" shows your own progress. OpenOlat fills both boxes itself, depending on your role and the settings of the course.

![Right column of the info page of a learning path course for participants: Get started with Open Course, below it My course with progress, status, score, groups and Leave Course](assets/general_functions_infopage_my_course_v1_en.png){ class="shadow lightbox" title="Info page of a learning path course as a participant · 2026.10.20" }

You also leave again on the info page. The right column shows one of two boxes, with the button for leaving at its bottom:

| Box | Button at the bottom of the box | If the button is missing |
|---|---|---|
| "My course" | "Leave course", for other learning resources for example "Leave wiki", see [Leave course](#leave_course). If you booked an implementation that is offered like a single course, "Cancel booking" or "Cancel booking for a fee" appears here, see [Cancel booking](#cancel_booking). | If you booked the course as part of an implementation, open its info page: in the catalog or under `Courses > Educational products` via "Learn more". You see what you booked in your [Booking orders](../personal_menu/Bookings.md). The other reasons are listed under [Leave course](#leave_course); if in doubt, ask your coaches. |
| "My educational product" | "Cancel booking" or "Cancel booking for a fee", see [Cancel booking](#cancel_booking). | The box only exists if you can cancel. If it is missing, ask your coaches. |

An implementation is the concrete run of an educational offer, with period, location, members and one or more courses. Under `Courses`, the scope with your implementations is called "Educational products". Whether a button appears is defined by the owners of the course, for an implementation by the course planners and product owners. The scope "Educational products" under `Courses` only exists if system administrators have switched it on, see [Products in "Courses"](../../manual_admin/administration/Modules_Course_Planner.md#product_in_my_courses).

### Get started {: #get_started}

The box "Get started" shows the action that suits your situation:

- **Without membership:** the offers of the course and the button "Book". How the booking works is described in [Catalog 2.0 - Offers](../area_modules/catalog2.0_angebote.md#offer_booking).
- **As a member:** the button "Open Course". If the course is not accessible yet, a message is shown above it, for example "The content is not yet available" or "Booking pending", and the button is greyed out.
- **With an administrative role:** If you are not a member but an administrator, learning resource manager, principal or course planner, you open the course with "Open with administrative role".
- **Without login:** Anyone who opens the info page via a link without being logged in to OpenOlat sees "Show in Catalog" if the course can be booked in the catalog, otherwise "To login".

If a course is finished and participants no longer have access in the status "Finished", the box reports "Course finished".

You cancel a booking in the box below: "My educational product" or "My course", see [Cancel booking](#cancel_booking).

### Cancel booking [:octicons-tag-16:{ title="from Release 20.0 (OO-8397)" }](https://track.frentix.com/issue/OO-8397){:target="_blank"} {: #cancel_booking}

If you cannot take part in a booked implementation after all, you cancel the booking yourself if the offer allows it. You cancel on the info page of the implementation, which you reach via the catalog:<br>
`Catalog > "Your implementation" > Learn more > Box "My educational product" > Cancel booking` [:octicons-tag-16:{ title="from Release 21.1.2 (OO-9977)" }](https://track.frentix.com/issue/OO-9977){:target="_blank"}

If the implementation is offered like a single course, the box is called "My course".

You can cancel a booking yourself if it was made via an offer of an implementation in the Course Planner. You leave a booked individual course with [Leave course](#leave_course) instead.

![As a participant you find the button "Cancel booking" in its own box "My educational product" below "Get started"](assets/general_functions_infopage_my_product_v1_en.png){ class="shadow lightbox" title="Info page of an implementation as a participant · 2026.11.09" }

Confirm in the dialog with "Cancel booking". If a cancellation fee applies, the button is called "Cancel booking for a fee", and the confirmation dialog states the fee. After the cancellation, you receive an e-mail whose subject ends with "Confirmation of your cancellation".

If system administrators have switched on the scope "In preparation" under "Courses" in the system administration at `Administration > Modules > Learning resource`, you also reach the same info page under `Courses > In preparation > Learn more`. An implementation is listed there only as long as it is not running yet. The administration manual describes the setting under [Module Learning resource](../../manual_admin/administration/Modules_Learning_Resource.md).

!!! info "Important"

    If you booked an implementation and the button is missing on the info page of one of its courses, open the info page of the implementation: in the catalog or under `Courses > Educational products` via "Learn more". The [Booking orders](../personal_menu/Bookings.md) do not show the button.

The button only appears if the offer allows cancellation and your booking fits. As a participant, you do not see the settings of the offer. If the button is missing, one of these reasons applies:

- **The offer does not allow cancellation:** The offer you booked does not let participants cancel themselves. With payment via "PayPal Checkout", this is always the case.
- **The start has been reached:** With many offers, you can only cancel until the day before the start of the implementation. From the begin date on, the button is missing. If the implementation has no begin date, it is missing completely with these offers.
- **You were enrolled without a booking order:** The button needs a booking order with the status "New", "In payment process" or "Paid". You have one if you booked in the catalog or were enrolled with an offer. You can see whether a booking order exists under [Booking orders](../personal_menu/Bookings.md).
- **You have another role:** Only participants of the implementation and persons whose booking is still pending see the button.

In these cases, contact your coaches or the person who enrolled you. Whoever manages the members of the implementation cancels your booking regardless of the setting of the offer. If there is no booking order, this person removes you from the implementation.

The settings of the offer and how long each offer type can be cancelled are described in [Offer concepts: Cancellation](../basic_concepts/Offer_Concepts.md#offer_cancellation).

### My course {: #my_course}

As a member, you see your own progress in the box "My course" without opening the course. The box only shows the details that exist for you:

- **Progress:** your progress in percent. Only in a learning path course and only once OpenOlat has recorded progress.
- **Status, score and grade:** your result in the course. For this, the switch "Show evidence of achievement to participants" must be switched on under `Course > Administration > Settings > Tab "Assessment"`, see [Course Settings - Tab Assessment](Course_Settings_Assessment/index.md#section_evidence_of_achievements). The status appears if the course assesses "Passed" or "Not passed", the score if it awards points. The grade additionally requires system administrators to have switched on grades in the system administration: `Administration > e-Assessment > Levels/Grading`.
- **Groups:** the groups of the course in which you are a member. A click on the name opens the group.

At the bottom of the box is the button "Leave Course", see [Leave course](#leave_course). On the info page of an implementation that is offered like a single course, "Cancel booking" appears there instead if the offer allows it, see [Cancel booking](#cancel_booking).

For learning resources other than courses, the box only shows the groups and the button to leave. If none of these details exist, the box "My course" is missing completely.

### Leave course [:octicons-tag-16:{ title="from Release 10.2 (OO-1405)" }](https://track.frentix.com/issue/OO-1405){:target="_blank"} {: #leave_course}

If you no longer need a course, you remove yourself from it. You leave the course on its info page:<br>
`Courses > Active > Learn more > Box "My course" > Leave Course`

In the opened course, the link "Info page" in the toolbar leads to the same page. The entry "Leave course" in the menu "My course" of the course toolbar offers the same way, see [Toolbar: My Course](Toolbar_My_Course.md#leave_course). For other learning resources, the button carries the type in its name, for example "Leave Wiki".

The button only appears for participants and only if the owners of the course allow leaving. They set it under:<br>
`Course > Administration > Settings > Tab "Share" > Participants can leave`

If the setting is "Never", the button is missing. If it is "After course end date or status "Finished"", the button is greyed out until the course end date has passed or the course has the status "Finished". The options are described in [Access configuration](Access_configuration.md#leave_learning_resource). Which option a new course has is preset by system administrators in the system administration: `Administration > Modules > Learning resource`, see [Module Learning resource](../../manual_admin/administration/Modules_Learning_Resource.md#allow_leaving_courses).

The button is also missing in these cases:

- You are a member of the course via an implementation, for example because you booked the implementation. Then you cancel your booking on the info page of the implementation, see [Cancel booking](#cancel_booking).
- A group enrolled you that does not allow leaving or is linked to several courses.
- An assessment mode is running.

[To the top of the page ^](#general_functions_info)

---


## Print the info page or download it as PDF [:octicons-tag-16:{ title="from Release 21.1 (OO-9299)" }](https://track.frentix.com/issue/OO-9299){:target="_blank"} {: #print}

Anyone who may only book a course after approval by a supervisor often needs the course details on paper. For this, the info page can be output as a flyer: in one column, without buttons and with a QR code that leads directly to the offer.

Click "Download as PDF" in the header of the info page. The button is next to "Set bookmark" and "Share". OpenOlat creates a PDF file with the title of the learning resource as the file name. You get the same printout with the "Print" command of your browser, then without a file.

![Printout in one column with logo, title, cover image, price, facts, sections, events as a table and QR code View offer](assets/general_functions_infopage_print_v1_en.png){ class="shadow lightbox" title="PDF of an info page · 2026.09.29" }

The printout contains:

- at the top the logo of the OpenOlat instance, if the layout provides one
- title, teaser and cover image
- under "Get started" only the details of the selected offer, for example the price
- facts, all sections expanded, license and star rating
- the events as a table with date, event and time
- at the end the QR code with the heading "View offer" and the address of the offer

The printout leaves out what only makes sense on screen: Set bookmark, Share and Download as PDF, the buttons "Book" and "Open Course", notes and free places, and the comments. If you are already a member, "Get started" is left out completely. The QR code points to the same address as the action "Share". Where the info page has no action "Share", the QR code is missing too.

!!! note "Note"

    The button "Download as PDF" only appears if system administrators have set up a PDF service in the system administration, see [External Tools: PDF Generator](../../manual_admin/administration/External_Tools_-_Administration/index.md#pdf_generator). Without a PDF service, print the info page via the browser.

[To the top of the page ^](#general_functions_info)

---


## Info page of an implementation [:octicons-tag-16:{ title="from Release 20.0 (OO-8286)" }](https://track.frentix.com/issue/OO-8286){:target="_blank"} {: #implementation}

Anyone booking an implementation in the catalog first sees the same info page as for a course, with facts, sections, events and "Get started". Printing and "Download as PDF" work the same way.

![Info page of an implementation with reference and element type, actions, facts, description, teachers, Get started with price and events](assets/general_functions_infopage_example_v2_en.png){ class="shadow lightbox" title="Info page of an implementation · 2026.09.29" }

Some elements differ:

- **Missing** are license, rating and comments.
- **Instead of "My course"**, participants see the box "My educational product" with [Cancel booking](#cancel_booking). An implementation of type Single course shows the box "My course".
- **Added** are the section "Outline" and the fact "Participants" with the number of places.
- **In the header**, the element type of the implementation appears next to the reference.

You do not enter the details in a course, but in the settings of the implementation, in the sub-tabs "Metadata", "Infos" and "Execution":<br>
`Course Planner > Implementations > "your implementation" > Tab "Settings"`

More on this under [Course Planner: Implementations](../area_modules/Course_Planner_Implementations.md#tab_settings).

[To the top of the page ^](#general_functions_info)

---


## How do you access the info page? {: #access}

### Access the info page via the course overview {: #access_course_overview}

In your course overview, you open the info page of a course with "Learn more" next to the button "Open":<br>
`Courses > Learn more`

If the course belongs to an implementation that is offered like a single course, "Learn more" opens the info page of the implementation.

![Courses in the main navigation and the link Learn more next to the Open button of a course highlighted](assets/general_functions_infopage_access_courses_v1_en.png){ class="shadow lightbox" title="Course overview Courses in the tab Active · 2026.10.20" }


[To the top of the page ^](#general_functions_info)

---


### Access the info page in the catalog {: #access_catalog}

In the tile view of the catalog, you open the info page with "Learn more" at the bottom right or with a click on the image.

![Catalog in the main navigation, the image of a course and the link Learn more at the bottom right next to the Book button highlighted](assets/general_functions_infopage_access_catalog_tile_v1_en.png){ class="shadow lightbox" title="Tile of a course in the catalog · 2026.10.20" }

In the list view, click the link "Learn more" or the title of the learning resource.

![Title of a course and link Learn more in the column of the same name highlighted](assets/general_functions_infopage_access_catalog_list_v1_en.png){ class="shadow lightbox" title="List view of the catalog · 2026.10.20" }

[To the top of the page ^](#general_functions_info)

---


### Access the info page within a course {: #access_within_a_course}

If you have opened a course, select the link "Info page" with the info icon in the toolbar. You reach the same page in any other opened learning resource via the toolbar. If the course belongs to an implementation that is offered like a single course, the link opens the info page of the implementation.

![Link Info page with info icon highlighted as the first tool, next to it Learning path, Events and Course search](assets/general_functions_infopage_access_toolbar_v2_en.png){ class="shadow lightbox" title="Toolbar of an opened course · 2026.09.29" }

[To the top of the page ^](#general_functions_info)

---


### Access the info page of other learning resources {: #access_other_learning_resources}

You open the info page of other learning resources in the same way as the info page of courses. In the authoring area, no link leads directly to the info page: open the learning resource and select "Info page" in the toolbar there.

The details on usage, for example in which courses the learning resource is embedded, are not on the info page, but in the window named after the type of the learning resource, for example "About this test", see [Information on usage](../learningresources/Technical_Information_on_Resources_and_Usage.md#usage).

[To the top of the page ^](#general_functions_info)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Navigation >](../basic_concepts/Navigation.md)<br>
[External Tools: Overview >](../../manual_admin/administration/External_Tools_-_Administration/index.md)<br>
[Module Learning resource >](../../manual_admin/administration/Modules_Learning_Resource.md)<br>
[Licenses >](../../manual_admin/administration/Licenses.md)<br>
[Module Taxonomy >](../../manual_admin/administration/Modules_Taxonomy.md)<br>
[Module Events and Absences >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[About this course: Technical information and usage >](../learningresources/Technical_Information_on_Resources_and_Usage.md)<br>
[Module Course Planner >](../../manual_admin/administration/Modules_Course_Planner.md)<br>
[User tools: Booking orders >](../personal_menu/Bookings.md)<br>
[Catalog 2.0 - Offers >](../area_modules/catalog2.0_angebote.md)<br>
[Course Planner: Implementations >](../area_modules/Course_Planner_Implementations.md)<br>
[Offer concepts >](../basic_concepts/Offer_Concepts.md)<br>
[Course Settings - Tab Assessment >](Course_Settings_Assessment/index.md)<br>
[Toolbar: My Course >](../learningresources/Toolbar_My_Course.md)<br>
[Access configuration >](../learningresources/Access_configuration.md)

**Further reading**<br>
[Course Settings >](Course_Settings/index.md)<br>
[Course settings - Tab Share >](Course_Settings_Share/index.md)

[To the top of the page ^](#general_functions_info)
