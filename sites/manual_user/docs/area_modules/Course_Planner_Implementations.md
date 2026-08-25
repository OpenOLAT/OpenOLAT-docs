# Course Planner: Implementations [:octicons-tag-16:{ title="from Release 20.0 (OO-7834)" }](https://track.frentix.com/issue/OO-7834){:target="_blank"} {: #implementations}

![The entry point to the implementations, highlighted in the Products area of the Course Planner start page, next to Products, Events, To-dos, Reports, Certification programs and Room management](assets/course_planner_implementations_v4_en.png){ class="shadow lightbox" }

## What is an implementation? {: #definition}

An educational program/product (consisting of one or more courses) can be offered and carried out several times. Each implementation can take place on a different date and different participants are then present at each implementation.

In an educational program/product, one or more courses are assigned to each implementation. The courses used multiple times only exist once.

If a course is to be used multiple times and always stay exactly the same, it can also be created as a template. The courses are then instantiated for each implementation (created from the template). This instantiation can also take place automatically on a specific date, for example a few days before an implementation starts. Until then, the template owners can still work on finalizing the template courses. The organizational aspects of the implementation (date, catalog offer and so on) can already be prepared with the Course Planner.

From this conceptual idea, the same courses are generally assigned and used in each implementation. However, it is also possible in OpenOlat to adapt the content in each implementation.

[To the top of the page ^](#implementations)

---


## The list of implementations {: #listing}

If you have selected the "Implementations" button in the Course Planner overview, you will first be taken to a list of all implementations for this product. You can use filters to narrow down the selection.
![All implementations of a product in a filterable list with Reference, Type and Status, here with the Occupancy status filter open, on the Implementations page in the Course Planner](assets/course_planner_implementations_list_v1_de.png){ class="shadow lightbox" }  

With **Save filter**, frequently used filter combinations can be saved and reused as your own preset. [:octicons-tag-16:{ title="from Release 20.3 (OO-9223)" }](https://track.frentix.com/issue/OO-9223){:target="_blank"}

![The Save filter action in the menu at the top right of the table, which keeps a filter combination as your own preset, on the Implementations page in the Course Planner](assets/course_planner_implementations_list_filter_v1_en.png){ class="shadow lightbox" }  

The individual column selector can also be used to show the **Subjects** and **Subject paths** columns, which are hidden by default (between the "Status" and "Calendar" columns). [:octicons-tag-16:{ title="from Release 20.3.1 (OO-9392)" }](https://track.frentix.com/issue/OO-9392){:target="_blank"}

!!! info "Important"
    The subjects are made available in the system administration, under `Administration > Modules > Taxonomy`.

### Bulk action "Change type" [:octicons-tag-16:{ title="from Release 21.0 (OO-9583)" }](https://track.frentix.com/issue/OO-9583){:target="_blank"} {: #change_type}

By activating the checkbox in the first column you select several implementations. The action **"Change type"** then appears above the table. In the dialog you choose the new element type and confirm with **"Change type"**. Only types that fit the selected elements are offered.

The same action is available in the search of the Course Planner and in the "Structure" tab of an implementation.

![Three selected implementations with the "Change type" action displayed and the dialog for choosing the new element type, in the implementation overview of the Course Planner](assets/course_planner_implementations_change_type_v1_en.png){ class="shadow lightbox" }


[To the top of the page ^](#implementations)

---

## Navigation the implementations [:octicons-tag-16:{ title="from Release 20.0 (OO-8128)" }](https://track.frentix.com/issue/OO-8128){:target="_blank"} {: #navigation}

Once you have selected and opened an implementation in the list, the tabs shown allow you to make all settings for this implementation:

- click on the "**Go to**" button at the top right to jump to an element within the current implementation.

- use the **arrow buttons** at the top right to switch to other implementations.

- configure this implementation by clicking on the various **tabs**.

- click on one of the **headings** to jump directly to the corresponding tab.

![The ways through an implementation: the Go to button, the arrow buttons for switching between implementations and the tabs from Overview to Reports, in the header of an opened implementation](assets/course_planner_implementations_navigation_v2_en.png){ class="shadow lightbox" }


[To the top of the page ^](#implementations)

---



### Tab Overview [:octicons-tag-16:{ title="from Release 20.2 (OO-8953)" }](https://track.frentix.com/issue/OO-8953){:target="_blank"} {: #tab_overview}

The "Overview" tab shows you the members, the next dates, the offers in the catalog and the course content for this product. This makes it easier for you to navigate the activities related to this implementation.

Use the **Show all** button in the **Events** widget to go directly to the Events tab.

The **Content** and **Catalog** widgets also show an icon in the title as well as the **Details** button [:octicons-tag-16:{ title="from Release 20.3 (OO-9244)" }](https://track.frentix.com/issue/OO-9244){:target="_blank"}, which takes you directly to the Content tab or the Catalog tab.

![The widgets for Events, Content, Members and Catalog with the Show all and Details buttons, in the Overview tab of an implementation](assets/course_planner_implementations_tab_overview_v2_en.png){ class="shadow lightbox" }

#### Member widget [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9243)" }](https://track.frentix.com/issue/OO-9243){:target="_blank"} {: #widget_members}

The **Members** widget shows the **"Participants"** key figure of this implementation, broken down into **"Active"** and **"Pending"**. If no course staff has been added yet, the widget shows the note "No course staff yet." Use the **"Details"** button to go directly to the Members tab of this implementation. [:octicons-tag-16:{ title="from Release 21.0 (OO-9405)" }](https://track.frentix.com/issue/OO-9405){:target="_blank"}

![The Participants key figure with Active and Pending as well as the note No course staff yet, in the Members widget in the Overview tab of an implementation](assets/course_planner_implementations_widget_members_v1_en.png){ class="shadow lightbox" }

If course staff has been added, they appear instead of the note, with their role (e.g. coaches, master coaches, course owners, element owners).

If a maximum or minimum number of participants is defined, an additional note text supplements the "Participants" key figure:

* If a maximum is set: **"\<number\> seats left"**
* If a minimum is set: **"\<number\> to minimum"**
* For fully booked or overbooked implementations, the corresponding message appears.

![Seats left and the distance to the minimum number below the participant count, plus the course staff with their roles, in the Members widget in the Overview tab](assets/course_planner_implementations_widget_members2_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#implementations)

---


### Tab Structure [:octicons-tag-16:{ title="from Release 20.0 (OO-8634)" }](https://track.frentix.com/issue/OO-8634){:target="_blank"} {: #tab_structure}

The "Structure" tab is shown for a structured implementation (the type is selected when a new implementation is created).
In the displayed tree structure, each individual element of the implementation can be edited or information about it can be queried.

![The tree structure of the elements with the Create menu open and the columns Ref., #Participants and Status, in the Structure tab of an implementation](assets/course_planner_implementations_tab_structure1_v1_de.png){ class="shadow lightbox" }

![1](assets/1_green_24.png) If you would like to add other elements for this implementation that deviate from the product structure ("copy template" of this structure), you will find the available element types under the **Create** button, as they were defined in the system administration under `Administration > Modules > Course Planner > Tab Element types`.

![2](assets/2_green_24.png) You can also download the displayed structure as an Excel file using the **Download button**.

![3](assets/3_green_24.png) In the **Ref.** column, you can display the content referenced in this element; the detail area is called "Referenced courses".

![4](assets/4_green_24.png) In this column you will find the **Schedules** of the respective elements.

![5](assets/5_green_24.png) In this column you will find the **Absences**. (Provided that absence management is activated.)

![6](assets/6_green_24.png) If the "Quality management" module has been activated, you can jump to the assigned **data collection preview** for each element.

![7](assets/7_green_24.png) The **Learning progress** column shows the average progress of all participants. All learning path courses for this element are taken into account. (Conventional courses do not provide any data on learning progress).

![8](assets/8_green_24.png) Under the **3 points** you will find options for editing the elements.

![The actions on an element: Open in new tab, Edit, Create new sub-element, Copy element, Member administration and Delete, in the menu of the 3 dots in the Structure tab](assets/course_planner_implementations_tab_structure2_v1_de.png){ class="shadow lightbox" }

#### Move an element [:octicons-tag-16:{ title="from Release 20.3 (OO-8841)" }](https://track.frentix.com/issue/OO-8841){:target="_blank"}

Use the **Move element** action under the **3 points** to open the move dialog. The element to be moved is highlighted in colour.

Every possible target position is displayed as a radio button. Positions that are not allowed (for example an incompatible element type) are greyed out and cannot be selected.

After selecting a target position, the following actions appear directly on the element:

* **Above**
* **Below**
* **Sub-element**

Click **Move element** to carry out the move.

![The possible target positions as radio buttons with the actions Above, Below and Sub-element, the element to be moved highlighted in colour, in the Move element dialog](assets/course_planner_implementations_move_element_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#implementations)

---


### Tab Content {: #tab_content}

The list shows all courses belonging to this implementation.

If you want to add further courses for this implementation (deviating from the original structure), use the "**Add course**" button at the top right.

The option to **remove** an **individual course** from this implementation can be found under the 3 dots at the end of a line.<br>
To **remove several courses**, select the courses with the checkboxes in the first column. A Remove button will then be displayed above the list.

![The courses of an implementation with share, creator and status, plus the Add course and Remove buttons for selected rows, in the Content tab of an implementation](assets/course_planner_implementations_tab_content_v1_de.png){ class="shadow lightbox" }

<br>

**Automatically controlled course content** [:octicons-tag-16:{ title="from Release 21.0 (OO-9578)" }](https://track.frentix.com/issue/OO-9578){:target="_blank"}<br>
If automation rules control the content of this implementation, the "Automation overview" section appears above the list. Only active rules that concern the content are listed. For each rule you see the type of rule, either "Instantiation" or the target status, plus the date of the planned execution and the condition that triggers the execution. Use the "Settings" link to switch directly to the [automation configuration](#tab_settings_automation).

![Content tab of an implementation with the "Automation overview" info box: for each rule it shows the type, here instantiation and three target statuses, the planned execution date and the triggering condition, plus the "Settings" link.](assets/course_planner_implementations_tab_content_automation_v1_en.png){ class="shadow lightbox" }

<br>

**Course template as course content**<br>
If it corresponds to the selected implementation type (individual course required), it is also possible to add a course template that can be instantiated at a later date. This means that at the time of planning in the Course Planner, a course is only announced but not yet added. Only when the course is actually held, for example, because there are enough bookings, is the course added to the implementation (instantiated).

Using a template for instancing is recommended if it is a recurring course that is always the same.

![The Course template section with the Add course template button below the still empty course list, in the Content tab of an implementation of type single course](assets/course_planner_implementations_tab_content_template1_v1_de.png){ class="shadow lightbox" }

The "Add course" and "Add course templates" buttons become inactive once the number of courses or templates corresponding to the selected delivery type has been added.

**Creation of course templates**<br>
Course templates are created by selecting the "Template" option in the course under `Course > Administration > Settings > Share > Usage`. 
The templates for course content in Course Planner do not have independent member management, as members are added in the Course Planner for each implementation.

!!! info "Important"

    Templates are copied. If the template is changed later, the previously created copy remains unchanged.


[To the top of the page ^](#implementations)

---

### Tab events [:octicons-tag-16:{ title="from Release 20.0 (OO-8064)" }](https://track.frentix.com/issue/OO-8064){:target="_blank"} {: #tab_events}

- If there are many appointments, the **filters** above the table are useful for keeping an overview.
- The **"Add appointment"** button can be used to add new appointments to the currently selected implementation.
- A click on the **+** at the beginning of a line shows the **details** of this appointment.
- It is also possible to **import** appointments. To do this, click on the small arrow next to the "Add appointment" button.

![The events of an implementation with date, time, units and lecturers, the All levels and This level switches and the Add appointment button, in the Events tab](assets/course_planner_implementations_tab_events_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#implementations)

---

### Tab members [:octicons-tag-16:{ title="from Release 20.3 (OO-8514)" }](https://track.frentix.com/issue/OO-8514){:target="_blank"} {: #tab_members}

![The members of an implementation filtered by role, with the views Active, Pending, Non-members and Members' history, in the Members tab](assets/course_planner_implementations_tab_members_v1_de.png){ class="shadow lightbox" }

As mentioned above, an educational product (consisting of one or more courses) can be carried out several times. Different participants take part in each implementation.

Participants are therefore made members of a specific implementation (not members of individual courses or an educational product). It can be determined whether they become members of the entire implementation or only of a sub-area.

If the participants were made members of the educational product (the "copy template"), they would be present as participants in all implementations of this product. This is not desirable. Therefore, only owners can be added to a product as members, not participants.

!!! info "Member administration in the Course Planner"
    Because member administration is carried out in the implementation when using the Course Planner, the course settings offer the usage "Use in Course Planner":<br>
    `Course > Administration > Settings > Tab Share > Section Usage`

**The course then no longer has *any* independent member administration**: member administration now takes place exclusively in the member administration of the implementation, **within the Course Planner**.

<br>

#### Tab members > Add members {: #add_members}


To add participants to an implementation as members, use:<br>
`Course Planner > Implementations > "your implementation" > Tab Members > Button "Add participants"`

![The Add participants button at the top right of the member list, which starts the wizard for adding members, in the Members tab of an implementation](assets/course_planner_implementations_add_member_v1_de.png){ class="shadow lightbox" }

<br>

#### Tab members > Invitation and membership requests [:octicons-tag-16:{ title="from Release 20.3 (OO-9156)" }](https://track.frentix.com/issue/OO-9156){:target="_blank"} {: #invitation_flow}

When participants are assigned to an implementation, they receive a system notification by email depending on the context:

- Assignment to a **course**: notification with a link to the course area
- Assignment to an **educational product**: notification with a link to the course area
- Assignment to a **group**: notification with a link to the group area

The notification box **"Accept membership requests"** appears in the course area, in the group area, and directly on the course or educational product info page. Participants can accept or decline the request there. Acceptance is possible equally at all three locations.

![The notification box Accept membership requests with the actions Details, Accept and Decline, as invited persons find it in the course area](assets/course_planner_implementations_accept_membership_v1_en.png){ class="shadow lightbox" }

!!! info "Important"

    Whether confirmation by the invited persons is required depends on the reservation requirement configuration. Details on this can be found in the section on confirming membership below.

For administrators: [System-wide configuration of the invitation >](../../manual_admin/administration/Modules_Groups.md#accept_membership)

<br>

#### Tab members > Confirmation of membership by line managers/education managers {: #confirm_membership}


The Course Planner can be set up so that a booking request must be confirmed by an administrative role (e.g. a line manager or education manager). With this setting, users can book a course, but the manager must confirm or decline the booking in an intermediate step.

This approval step can also be set up for all offers, except when paying with Paypal (since payment/booking there is immediate).

![The choice between Standard and With confirmation, plus confirmation by administrative roles and the deadline, in the Membership step of the Add participants wizard](assets/course_planner_implementations_confirm_member_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#implementations)

---


### Tab Catalog [:octicons-tag-16:{ title="from Release 20.0 (OO-8236)" }](https://track.frentix.com/issue/OO-8236){:target="_blank"} {: #tab_catalog}

The various implementations can be offered in the catalog. To do this, an [offer](../../manual_user/area_modules/catalog2.0_angebote.md) must be created, as for every catalog entry.

![The offers of an implementation with the Add offer button and the available offer types, in the Catalog tab of an implementation](assets/course_planner_implementations_tab_catalog1_v1_de.png){ class="shadow lightbox" }

To draw the attention of potential participants to an offer in the catalog, you can send a direct link to the offer, e.g. in an email. You will find the links in the overview of the offers (per implementation in the Catalog tab).

![The direct links to the offer for the external and the internal catalog, opened via Access and Links in the offer overview, in the Catalog tab of an implementation](assets/course_planner_implementations_tab_catalog3_v1_de.png){ class="shadow lightbox" }

If offers with booking options have been added to the catalog, the booking orders and their details can also be found under the "Catalog" tab in the "Booking orders" subsection.

![The booking orders with status, offer type, price and billing address, plus the download of the list and the actions per order, in the Booking orders subsection of the Catalog tab](assets/course_planner_implementations_tab_catalog2_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#implementations)

---


### Tab Settings {: #tab_settings}

The many possible settings for an implementation can be found under several subordinate tabs. A preview info page is permanently available.

![The sub-tabs of the settings from Metadata to Options and the Preview info page button, in the Settings tab of an implementation](assets/course_planner_implementations_tab_settings_v2_en.png){ class="shadow lightbox" }


#### Metadata of the settings

The metadata entered here is used to simplify search processes, for example.

![The mandatory fields Title, Reference and Type as well as Delivery format and Subjects, in the Metadata sub-tab of the settings of an implementation](assets/course_planner_implementations_tab_settings_metadata_v1_de.png){ class="shadow lightbox" }


#### Infos in the settings

The information entered in the "Infos" tab is used for the display in the catalog, for example.

![The details for the information page: teaser, title image, description, learning objectives, requirements and time expenditure, in the Infos sub-tab of the settings](assets/course_planner_implementations_tab_settings_infos_v1_de.png){ class="shadow lightbox" }


#### Implementation in the settings

The implementation settings include the implementation period, the location and the number of participants.

![Implementation period, location and the minimum and maximum number of participants, in the Implementation sub-tab of the settings](assets/course_planner_implementations_tab_settings_execution_v1_de.png){ class="shadow lightbox" }


#### Configure automation [:octicons-tag-16:{ title="from Release 21.0 (OO-9578)" }](https://track.frentix.com/issue/OO-9578){:target="_blank"} {: #tab_settings_automation}

In the **"Automation"** subsection of the settings tab, you define when courses are [instantiated](#tab_content) automatically and when status changes are triggered automatically.

The subsection appears for elements whose element type has the use "Implementation" or "Element". For the use "Implementation or element (legacy)" it is missing.

If a course is to be used multiple times in exactly the same way, it can be created as a template. The courses are then created from the template for each implementation. [Instantiation](#tab_content) can take place automatically at a specific time and role-specifically, e.g. accessible to coaches a few days before an implementation starts. Until then, the template owners can still work on the template while the organizational planning in the Course Planner is already under way.

**Scope of the automation rules:**

Automation rules are defined at two levels:

* **Element type level** in the system administration under `Administration > Modules > Course Planner > Tab Element types`: Administrators define default rules for each element type. These rules serve as a template for all elements of this type.
* **Element level** `Settings tab > Automation`: For each individual element, you decide whether the rules of the element type are adopted or overridden individually.

Two modes are available for the individual element:

* **"Adopt from type "Element type""**: The element uses the default rules of the element type. The label names the type and whether rules are active there. If administrators adjust the template, this automatically affects all elements that use this mode.
* **"Override"**: The element uses deviating, individually configured rules, independent of the element type.

**Types of automation rules:**

| Type | Trigger |
|---|---|
| On status change | An action is triggered as soon as the implementation or element status reaches a certain value. |
| Time-controlled | An action is triggered relative to the start or end of the implementation period. |

**Execution of the rules:**

Enabled automations run once a day at a fixed time. The information text above the configuration names the time.

As soon as at least one rule is active, the header of the implementation above the tabs shows the date of the next execution under "Automation". If no execution is pending, a dash appears there.

![Automation sub-tab of the settings of an implementation: the "Override" mode is selected, the table lists context, automation, target status, condition and planned execution for each rule, the header names the next execution.](assets/course_planner_implementations_tab_settings_automation_v3_en.png){ class="shadow lightbox" }

[To the element types and automation rules (Admin) >](../../manual_admin/administration/Modules_Course_Planner.md#tab_element_types)<br>
[To the to-dos on CPL elements >](Course_Planner_Todos.md)


#### Assessment in the settings [:octicons-tag-16:{ title="from Release 21.0 (OO-9499)" }](https://track.frentix.com/issue/OO-9499){:target="_blank"} {: #tab_settings_assessment}

The sub-tab "Assessment" is displayed for implementations of type single course and for every implementation that is already assigned to a certification program. Here you link the implementation directly to a certification program, without going through the program itself.

* Use the **"Certification program"** toggle to enable or disable the link.
* If no program is linked yet, use the **"Select"** action to choose a program. The "Select certification program" dialog shows title, Reference, validity period, recertification and required credit points. Only programs you have access to are displayed.
* If a program is linked, a panel shows the program title. Validity period, recertification and required credit points appear there provided they are configured on the program. From there you open the program in a new tab (provided you have access to the program) or remove the link with **"Remove"**; the confirmation dialog "Remove certification program" completes the step. Removing requires the role Course planner or Product owner and must be confirmed. Participants who have already received a certificate remain members of the program.

![The Certification program toggle and the Select button as long as no program is linked, in the Assessment sub-tab of the settings of an implementation](assets/course_planner_implementations_tab_settings_assessment_v1_en.png){ class="shadow lightbox" }

![The program list with Reference, validity period, recertification and required credit points, in the Select certification program dialog](assets/course_planner_implementations_tab_settings_assessment_select_v1_en.png){ class="shadow lightbox" }

![The linked program with the actions Remove and Open, shown when the Certification program toggle is on, in the Assessment sub-tab of the settings](assets/course_planner_implementations_tab_settings_assessment_linked_v1_en.png){ class="shadow lightbox" }

An implementation can also be added directly via the [certification program](Course_Planner_Certification_Programs.md#config_tab_implementations).

When [copying an implementation](#copy), the link to the certification program is applied, provided you have permission for the program. If the permission is missing, the wizard shows the warning "The certification program cannot be applied due to a lack of permissions." Copying creates an entry in the program's activity log.


#### Options in the settings

Separate settings can be made here for each implementation:

- Calender configuration
- Schedule
- Absence configuration
- Absence management
- Progress configuration

![Calendar, absence and progress configuration adopted from the type or overridden per element, plus the Schedule and Absence management switches, in the Options sub-tab](assets/course_planner_implementations_tab_settings_options_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#implementations)

---


### Tab Absences [:octicons-tag-16:{ title="from Release 20.0 (OO-8442)" }](https://track.frentix.com/issue/OO-8442){:target="_blank"} {: #tab_absences}

This tab only appears if absences have been activated on the element.

Activation takes place in the implementation settings: `Settings tab > Options > Absence configuration`.

![Attendance and absences of the participants with units, excused and unexcused absences and attendance rate, in the Absences tab of an implementation](assets/course_planner_implementations_tab_absences_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#implementations)

---


### Tab Reports [:octicons-tag-16:{ title="from Release 20.0 (OO-8387)" }](https://track.frentix.com/issue/OO-8387){:target="_blank"} {: #tab_reports}

The reports that can be created here relate to the currently selected implementation.

In contrast, the report creation, which can be called up in the [Overview](../../manual_user/area_modules/Course_Planner_Reports.md), refers to **all** implementations. 
The structure of the Excel files (columns) and the procedure for creating them is identical for both.

![The report templates with category, description and type, the Execute column and below it the generated Excel files with download, in the Reports tab of an implementation](assets/course_planner_implementations_tab_reports1_v1_de.png){ class="shadow lightbox" }

Click on the **arrows in the "Execute"** column to generate Excel files with the current data using the listed templates.

You will then find the Excel files created in this way listed at the bottom of the screen. They can be copied and downloaded.

[To the top of the page ^](#implementations)

---


## Copy an implememtation [:octicons-tag-16:{ title="from Release 20.0 (OO-8418)" }](https://track.frentix.com/issue/OO-8418){:target="_blank"} {: #copy}

You will find the **"Copy element"** action in the list of implementations at the end of a line under the 3 dots.

![The Copy element action in the menu of the 3 dots at the end of a row, which starts the copy wizard, in the list of implementations](assets/course_planner_implementations_copy1_v1_de.png){ class="shadow lightbox" } 

In the first step of the small wizard, you can select whether course content, dates, members, to-dos and room bookings should also be copied.

![Title and reference of the copy as well as the options for course content, standalone events, to-dos and memberships, in the General settings step of the Copy element wizard](assets/course_planner_implementations_copy2_v2_en.png){ class="shadow lightbox" }  

The second step of the wizard shows you an overview of the elements that will now be copied.<br>
You can still make adjustments here (especially to the dates).<br>
Click on the + in front of an element to display the courses and dates for the element.

![The elements to be copied with start, end and the counters #Courses, #Templates and #Events, one element expanded with its courses and events, in the Overview elements step](assets/course_planner_implementations_copy3_v1_de.png){ class="shadow lightbox" }  

An implementation contains many different dates that are arranged in a specific order. When copying, all of this data can be automatically adjusted and moved together. To do this, use the **"Shift all dates"** button in the overview of the elements. The dialog shows the "Reference date (earliest)". Under "Shift by" you choose between "Date" and "Days" and then enter the "New date" or the number of days.

![The Shift all dates button at the top right of the element overview, with which all dates can be moved together, in the Overview elements step](assets/course_planner_implementations_copy4_v2_en.png){ class="shadow lightbox" }

![Reference date, the choice of shifting by Date or Days and the new date, in the Shift all dates dialog of the Copy element wizard](assets/course_planner_implementations_copy5_v2_en.png){ class="shadow lightbox" } 

### Adopt to-dos when copying [:octicons-tag-16:{ title="from Release 21.0 (OO-9419)" }](https://track.frentix.com/issue/OO-9419){:target="_blank"} {: #copy_todos}

To-dos of an implementation are carried over when copying. In the first step of the wizard, the "To-dos" selection determines how this is done:

* **Standard:** Copy to-dos with assignments.
* **To-dos only:** Copy to-dos without assignments.
* **Don't copy:** To-dos are not copied.

In the overview of the elements, the **"#To-dos"** column shows how many to-dos an element contains. In the detail view of an element, the "To-dos" section lists all to-dos with title, priority, date input (absolute or relative), due date, status, assignment, delegation and tags. Use the checkbox at the start of a row to deselect individual to-dos from copying. If no to-dos exist, the note "No to-dos available." is shown.

![The counters #Courses, #Templates, #Events and #To-dos and below them the detail areas Courses, Events and To-dos of an expanded element, in the Overview elements step](assets/course_planner_implementations_copy_todos_details_v1_en.png){ class="shadow lightbox" }

### Adopt room bookings when copying [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9710)" }](https://track.frentix.com/issue/OO-9710){:target="_blank"} {: #copy_rooms}

If the module "Rooms" is activated, the first step of the wizard additionally shows the **"Room management"** section. The **"Room scheduling"** selection there determines whether the room bookings of the events are copied as well:

* **Copy:** The room bookings are copied along with the events. This option is preselected.
* **Don't copy:** The room bookings are not copied.

The selection is only active if events are copied at all, that is if the "Copy" option is selected for **Content** or for **Standalone events**. Otherwise it is greyed out and no bookings are created.

!!! note "You cannot see the Room management section?"

    The section only appears once a system administrator has activated the module "Rooms".<br>
    [Manage rooms (administration) >](../../manual_admin/administration/Modules_Rooms.md#activation)

The copy takes over the room of the original booking. The period of the booking follows the copied event: if you shift the events with **"Shift all dates"**, the bookings move along with them. When copying, OpenOlat does not check whether the room is still free in the new period. Conflicts such as a double booking only appear afterwards as a warning in [Room Scheduling](Course_Planner_Rooms.md#room_scheduling).

In the **"Overview elements"** step, the **"#Rooms"** column additionally appears if the module is active and the "Copy" option is selected. Expand an element and the "Events" table there lists the **"Rooms"** column with the booked rooms.

The **"Copy element"** action is available to administrators, course planners and product owners. You will find the complete overview in the [rights matrix](Course_Planner.md#rights_matrix) of the Course Planner.

You copy individual events in the event list of an implementation instead, with the **"Copy"** action. If you mark several events there and copy them together, OpenOlat takes over the room bookings automatically. If you copy a single event, the editing dialog of the copy opens with an empty **"Rooms"** field; you then select the rooms yourself.

[To the top of the page ^](#implementations)

---

## Delete an implementation [:octicons-tag-16:{ title="from Release 20.0 (OO-8354)" }](https://track.frentix.com/issue/OO-8354){:target="_blank"} {: #delete}

You will also find the option to delete in the list of implementations at the end of a line under the 3 dots.

![The Delete action in the menu of the 3 dots at the end of a row, in the list of implementations in the Course Planner](assets/course_planner_implementations_delete1_v1_de.png){ class="shadow lightbox" }

If you have already opened an implementation, you will also find the option to delete it at the top right under the 3 dots.

![The Delete action in the menu of the 3 dots at the top right, available in an opened implementation above the tabs](assets/course_planner_implementations_delete2_v1_de.png){ class="shadow lightbox" } 

[To the top of the page ^](#implementations)

---

## Further information {: #further_information}

[How do I create my first OpenOlat course >](../../manual_how-to/my_first_course/my_first_course.md)<br>
[Course Planner: Overview >](../../manual_user/area_modules/Course_Planner.md)<br>
[Course Planner: Products >](../../manual_user/area_modules/Course_Planner_Products.md)<br>
[Course Planner: Events >](../../manual_user/area_modules/Course_Planner_Events.md)<br>
[Course Planner: Certification programs >](../../manual_user/area_modules/Course_Planner_Certification_Programs.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.md)<br>
[How can I plan and run courses with the Course Planner? >](../../manual_how-to/course_planner_courses/course_planner_courses.md)<br>
[How can I plan and run a course with the Course Planner? >](../../manual_how-to/course_planner_curriculum/course_planner_curriculum.md)<br>
[Activate Course Planner (Admin) >](../../manual_admin/administration/Modules_Course_Planner.md)<br>
