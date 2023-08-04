# Access configuration {: #access-configuration}

In order for a course to be visible to learners, it must first be published. If the course is released for all users, the access can additionally be provided with a booking method, e.g. a password. In general, a distinction is made between the following publication variants, which are visible under "Status" in the toolbar of a course:

## Publication Status

A newly created learning resource is by default only accessible to its owners and has the publication status "Preparation". Under "Status" the status can be changed and the learning resource can be made accessible to other members:

![course status](assets/course-status.jpg){ class="thumbnail"}

Publication status| Access|
---|---|
Preparation | Only owners of this learning resource have access.|
Review | Only owners of this learning resource have access. All preparations for this learning resource have been completed and the contents have been released for further review.  
Access For Coach | Owners and coaches of this learning resource have access.  
Published | All members of the learning resource have access.  
Finished | All members still have access to the course, but can only read.  

!!! info "Note"

    If a course has the status "Review", “Access for coach" or "Preparation", the course appears in the courses menu in the tab "In preparation". However, it is not possible to access the course with all integrated course elements. Access to the toolbar is also not (yet) possible.
  
The concrete variant of course access (or access to a learning resource in general) is set up in the "Share" menu of the "Administration" course. In the following, you will learn which options are available to you.

## Tab Share

### Configure booking methods and create offers

:octicons-tag-24: Release 17.0

Access to a course is configured in "Administration" → "Settings" in the "Sharing" tab.
There are two basic options available:

![Booking options](assets/booking.png)

If the option **"Private "** is chosen, the participants are entered by the owners or persons who have the right of member management.

If the option **"Bookable and open offers "** is selected, learners can book a course/learning resource themselves, but may have to (depending on the setting) enter a password
enter.

### Leaving a learning resource

The system administrator determines in the administration tab whether course participants are per default allowed to leave the course at any time, never, or after the course end date. You can override the default setting anytime. The following options are available:

* At any time (Default): Participants may leave the course at any given time.
* After course end date: If an [execution period](https://confluence.openolat.org/display/OO130EN/Access+configuration#Accessconfiguration-d14e1774) has been configured for the course, this options allows participants to leave the course at the end of this time period. If this option was selected without a configured execution period, participants are not allowed to leave the course at any time.
* Never: Participants may never leave the course. Teilnehmende müssen wenn notwendig vom Kursbesitzer explizit ausgetragen werden.

If members are allowed to leave the course, they can do so by selecting "Leave course" in the "My course" menu.

![Action to leave course in course menu](assets/Leave_course_EN.png)

By default, users can leave a course or learning resource at any time.

### Administrative release

Here you can define for which organization/sub-organization (if set up) the course is released for the administrative roles. These include: other authors(depending on rights), learning resource administrators, principals, administrators.

Furthermore, the tab "Share" can be used to define which additional rights other authors have to the learning resource.

Authors can | Description  
---|---  
reference | Learning resources such as glossary, form or test can be integrated in courses of other authors.  
copy | The learning resource can be copied by other authors.  
download | The learning resource is available for download by other authors.  

!!! warning "Attention"

    The options "reference" and "copy" make sense if you want to use a template or a good example for other OpenOlat authors. However, referencing makes little sense *for courses* and should rather be avoided here.
    
    Consider carefully whether you really want to make the respective releases for *all* other authors of the OpenOlat instance.

## Configure offer / offers {: #offer}

If you have previously selected the option "Add booking methods" / "Bookable and open offers" (:octicons-tag-24: Release 17.0) you can then create offers.

![offer Screen](assets/offer.jpg){ class="lightbox" }

!!! note "Differences to booking methods before 17.0"

    * Offers can be published independent of the publication status of the course. To do this, select a in the offer creation "time-limited" and define a future period. The offer is then available in the catalog for this defined period.
    * Offers can be limited to different parts of organizations(sub-organizations).

You can define when and under which conditions the users of the users of the system can book a learning resource. Booking can be used as a synonym for book, enroll, purchase.The details are described below.

Select the button "Create offer" / "Add booking method" to add offers / booking methods.

!!! info  "Attention"

    The configuration of an access for OpenOlat guests (persons without OpenOlat account) is only possible in **conventional courses**.

### Offer options

![key](assets/key.png){ class="size24" } **Access code**

Select access code to restrict the booking to a specific group of people. Only people who have this access code can book the resource. Before opening the course for the first time, the user must enter this code, which may have been sent in advance by e-mail or written on the whiteboard in the case of blended learning events. The code needs to be entered only once.

![gift](assets/gift.png){ class="size24" } **Free available**

Select this option if no further restrictions apply. All OLAT users can open and use the learning resource. A user will thus be added as a participant. If the function _"Automatic booking"_ is activated, users will automatically be directed to the course view without having to book the learning resource explicitly using the booking dialog. The advantage compared to the option "open without booking" is that the owner can see who has booked his course.

![paypal](assets/cc-paypal.png){ class="size24" } **PayPal and credit card**
  
Is only available if enabled by the [administrator](../../manual_admin/administration/PayPal_Configuration.md): Select the PayPal/credit cards to enable booking against a financial payment. You can define an amount that has to be paid with a PayPal account or with a credit card (Visa/Mastercard). (This function is only available for users with author rights)

![notBooking](assets/notBooking.jpg){ class="size24" } **Without booking**

:octicons-tag-24: Release 17.0

With this offer you can publish a course which can be accessed by all OpenOlat users without showing up in the member administration.

!!! info "Note"

    Without posting corresponds to the "Open for all" option in the old release.

![guest](assets/guest.jpg){ class="size24" } **Guest access**

In the traditional course, an offer can also be created for guests only. This is then only available for guests and cannot be restricted for different sub-organizations.

### Details for offer configuration

Optionally, a start and end date can be added to a booking configuration/offer configuration. This configuration is then only valid between the configured date valid. You can also specify only a start date or only an end date. If you do not want to specify a time restriction, leave this field empty. Booking methods can be adjusted later.

You can also configure multiple booking methods/offers. These are considered as different options from which the user can choose, in this case make sure that the descriptions are meaningful. For example, course codes can be combined for people from different contexts, or a course can be made free until a certain date and then only accessible with password
be set up.

!!! warning "Attention"

    A specified start or end date refers exclusively to the **booking process** not to the implementation period of the learning resource. If a user has booked a resource, the person is entered in the participant list of this resource. From that point on, the system decides whether a person has access to a resource solely on the basis of the participant list. Therefore, expired booking configurations have no influence on a participant list. As the owner of the resource, you can also add or remove a person from the list of participants at any time. In the second case, the user can re-enter the resource as a participant by booking again.

You can easily delete the configured booking methods/offers at any time. The bookings already made remain in place and are not affected by this affected.

## Share Overview

![share-overview](assets/share-overview.jpg){ class="lightbox" }

If the sharing is set according to the wishes, you can see compactly at the end of the page, who has access to this course and which groups or curricula are linked to this course. Behind the roles is written in brackets, the respective rights of the role.

## Lifecycle: Finish/Delete

If a course has been completed and has expired, it can be finished and/or
deleted.

If a course is  **completed** , it is then in read mode. All user data is
retained and all course members still have access to the course. The course is
no longer in the tab "My Courses", but in the tab "Finished" next to it.

![Finished courses](assets/lifecycle_finished.png)

In the authoring area, the finished course is displayed with a new icon and
crossed out.

If you want to reopen the course, go back to the course life cycle and click Reopen.

### Delete course

A learning resource can be deleted in the menu "Administration" → "Delete" or
via the action menu ![Action menu](assets/Action%20menu.png) in the author area. In this case, the learning resource is moved to the "Deleted" tab and is in the trash, so to speak.
