# Course Settings - Tab Execution {: #tab_execution}

Unlike other learning resources, courses still have a "Delivery" tab in the "Settings" menu.

![course_settings_execution1_v1_en.png](assets/course_settings_execution1_v1_en.png){ class="shadow lightbox"}

## Settings for implementation  {: #config_execution}

![1_green_24.png](assets/1_green_24.png) **Implementation period**

For learning resources of the "Course" type, a duration can be specified. The following options are available:

* _Without_: Wählen Sie diese Option, wenn der Kurs nicht zu einem bestimmten Daten beginnt und aufhört oder Sie den Termin nicht explizit in den Informationen einbauen möchten.

* _With start and end dates_: The course owner can enter the start and end dates of the course here. The end date includes the final day (11:59 p.m.).

* _Time period_: If you select this option, you will be presented with predefined time periods, such as semesters, to choose from. See point 2.

The selected course period is displayed in the course information. 

!!! info "Important"

    This setting should not be confused with the course status and does not affect the visibility or access of course members. 

However, keep the following in mind: 

If "with start and end dates" is selected, the dates entered here will also apply to various time-dependent functions in the course, such as reminders or the automatic submission of assignments in the assignment module. 

The end date of the course period is also used for the course lifecycle. The exact implications of this are determined by the OpenOlat administrators. For example, the course could be set to "completed" two days after the end date and/or deleted four weeks after the end date. It is best to check which settings apply to the course lifecycle in your OpenOlat instance. 

In traditional courses, the "Pass" status is determined based on whether the result was achieved within the course period. If a "Pass" is not achieved by the end date, "Fail" is automatically displayed.

!!! note "Note"

    When using the automatic lifecycle, the course status is determined by the end date.


![2_green_24.png](assets/2_green_24.png) **Time Period**<br>
If the OpenOlat administrator has configured time periods (e.g., semesters) at the system level, you can select one of the predefined options here when "Time Period" is selected as the implementation period. The time period then appears as information in the course overview. However, the time period is independent of the course status and course access rights (see the chapter ["Access Configuration"](../learningresources/Access_configuration.md)). It therefore has no effect on visibility or access for course members.


![3_green_24.png](assets/3_green_24.png) **Implementation place**<br>
The location where a course or learning resource takes place. This field is particularly useful for blended learning offerings. For courses that are entirely online, this field can be left blank. Alternatively, you can enter "online" or "Internet" here.
The text entered in this field will be displayed in the course information.


[To the top of the page ^](#tab_execution)

---


## Configuring event and absence management in the course {: #config_event_and_absence_management}

![4_green_24.png](assets/4_green_24.png) **Enable event & absence management**<br>
This option is available if the module "Events and Absences" is [activated system-wide](../../manual_admin/administration/Modules_Events_and_Absences.md). Without the activated module, the entire section (points 4 to 15) does not appear in the "Execution" tab.

If you enable event and absence management for the current course, points 5 to 11 are displayed for further configuration, and with assessment mode allowed additionally points 12 to 15.

In addition, the "Events and Absences" menu will then appear under (Course) Administration. As the **course owner**, you can enter appointments and absences there once the configuration is complete (at runtime).

!!! note "Note"

    Unlike owners, **coaches** can find the capture tool in the toolbar.<br>
    **Members** find their absences in the [Personal Menu](../personal_menu/Absences.md)


![5_green_24.png](assets/5_green_24.png) **Override default configuration**<br>
If overwriting is permitted, the following checkboxes and input fields can be edited and a specific configuration of the event and absence management can be made for this course.

If overwriting is not permitted, the administrator's default setting will be applied. The checkboxes and input fields below remain inactive and display the default value. The functions preset there are nevertheless effective in the course.

Whether overwriting can be enabled in the course is controlled by the administration with the setting "Allow override of configuration".

![6_green_24.png](assets/6_green_24.png) **Roll call enabled**<br>
If attendance monitoring is enabled, the additional configuration options **"Calculate attendance rate"** and **"Attendance quota global in %"** are available.

![7_green_24.png](assets/7_green_24.png) **Calculate attendance rate**<br>
The attendance rate is calculated based on events with multiple units and absences.

**Example:**<br>
An event consists of 10 sessions. The participant was absent from one of the sessions.<br>
=> This results in an attendance rate of 90%.

![8_green_24.png](assets/8_green_24.png) **Attendance quota global in %**<br>
A global attendance rate is calculated for all participants across all dates of the current course and displayed in the personal menu under "Absences".
The global absence rate specified here is used to assess the attendance rate.

![9_green_24.png](assets/9_green_24.png) **Synchronize teacher calendar**<br>
If this option is selected, course dates are entered into the lecturers' personal calendars. (These dates are dates for which absences can be recorded.)

![10_green_24.png](assets/10_green_24.png) **Synchronize course calendar**<br>
If this option is selected, events are entered in the course calendar. If this option is not selected, only the simple events are listed in the course calendar; events with the option to record an absence are no longer listed.

![11_green_24.png](assets/11_green_24.png) **Allow assessment mode for events**<br>
If assessment mode is allowed for events, you can select the "Mark as exam" option from the 3-dot menu for events. This creates an assessment mode. In addition, the following points 12 to 15 are displayed with the course-wide default values for these assessment modes. The default values are applied when marking; assessment modes already created remain unchanged by later modifications.

To change this setting in the course, the option "Override default configuration" is required. If overwriting is not permitted and assessment mode is allowed in the administration, this field appears checked and inactive, and "Mark as exam" works with the default values from the administration.

![12_green_24.png](assets/12_green_24.png) **Prep time**<br>
The prep time refers to "Allow assessment mode for events".<br>
When coaches or owners "mark an event as an exam", an assessment mode is created with this setting. (All assessment modes created in this way for the course have the same prep time.)

![13_green_24.png](assets/13_green_24.png) **Follow-up**<br>
The follow-up refers to "Allow assessment mode for events".<br>
When coaches or owners "mark an event as an exam", an assessment mode is created with this setting. (All assessment modes created in this way for the course have the same follow-up.)

![14_green_24.png](assets/14_green_24.png) **Admissible IP addresses**<br>
This setting also refers to "Allow assessment mode for events".<br>
The IP addresses entered here are applied to the assessment mode when an event is "marked as exam".

![15_green_24.png](assets/15_green_24.png) **Safe Exam Browser Keys**<br>
This field is the course-wide default value for the "SEB with manual keys" variant. The stored key is applied when an event is "marked as exam" and the exam is secured with the Safe Exam Browser. In the assessment mode of the event, the key is displayed for information and cannot be edited there.

The field only appears if the administration has selected the "SEB with manual keys" variant for "Safe Exam Browser - Type of use". You find the setting under:<br>
`Administration > Modules > Events / Absences`, tab "Configuration".

If the field is left empty while overwriting is permitted, the assessment modes of this course receive no key; the key from the administration is not used in that case.

If "SEB-Config (recommended)" is active, the Safe Exam Browser is configured per exam via [configuration templates](../learningresources/Assessment_mode.md) and this field is not shown. When marking an event as an exam, the field "Configuration" with the active templates is available in the assessment mode of the event, with the default template preselected. Whether the configuration file can be downloaded is determined by the administration in this case.

Assessment modes created directly via the [assessment management](../learningresources/Assessment_mode.md) do not use this course-wide key. There, the SEB variant is chosen per assessment mode via "Type of use".

[To the top of the page ^](#tab_execution)

---


## Access course elements {: #access_course_elements}

![16_green_24.png](assets/16_green_24.png) **Type**<br>
For your information, this section indicates whether the current course is a learning path course or a traditional (classic) course. 

Existing courses can be converted into a learning path course at this point. 

![17_green_24.png](assets/17_green_24.png) **Calculate learning progress**
For learning path courses, you can specify whether the displayed course progress is calculated based on the number of required course modules or based on the time spent on the required course modules. If you select "time spent," all required course modules must be assigned corresponding durations in the course editor. 
Optional course modules are not taken into account.

Traditional courses do not include a "Learning Progress" option.


[To the top of the page ^](#tab_execution)

---

## Further Informationen {: #further_information}

[Basic concept events and absences >](../basic_concepts/Events_and_Absences.md)<br>
[Activation and configuration of absence management by administrators >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Tracking and managing absences in a course by course owners >](../learningresources/Events_and_absences.md)<br>
[Tracking and managing absences in a course by coaches >](../learningresources/Toolbar_Events.md)<br>
[Personal absences >](../personal_menu/Absences.md)<br>
[Cross-course absence recording in the coaching tool >](../area_modules/Coaching.md)<br>
[Cross-course absence management by absence administrators >](../area_modules/Absence_Management.md)<br>

[To the top of the page ^](#tab_execution)

