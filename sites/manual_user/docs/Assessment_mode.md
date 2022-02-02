#  [Assessment mode](Assessment+mode.html)

The assessment mode allows you to create exam settings where tests and
assessment are carried out in safe mode during a fixed time span, during which
only access to previously defined course elements in the respective course is
allowed. All other OpenOlat functions such as courses, groups, notes are
masked and thus not accessible. Students are only allowed to log out during
such an assessment.

You can create an assessment mode by selecting the link "Assessment mode" in
the course "Administration" and clicking on the button "Create test
configuration".

![](../../download/attachments/590936/assessment_mode_15.png)

The starting page offers an overview of all previous, current and future exam
settings. Future settings may be edited at any time, while previous settings
are read only. The overview contains information on date and time, preparation
and follow-up times as well as configured user groups.

Exam settings are created in advance, and have, aside from a time frame
including - if so desired - preparation and follow-up times, the user group
for which the exam is valid. An exam thus can be effective for course members
only, group members of selected groups or both. This facilitates the
simultaneous execution of multiple exams for the same course, but with
different configurations. Aside from the user group, you can also configure
access restrictions to the course elements, and whether one of the selected
elements should be displayed as starting element. You can also restrict access
to the exam to specified IP addresses, or make the use of the [Safe Exam
Browser](http://www.safeexambrowser.org/news_en.html) mandatory.

Users that have an assigned exam, are notified of the beginning of the exam
respectively preparation time. If access to other OpenOlat is restricted by
follow-up time at the end of the exam, users will be notified of that, too.

A running assessment mode can be terminated automatically or manually.

![](../../download/attachments/590041/Pruefung_beenden%EF%B9%96version=1&modificationDate=1606054356000&api=v2.jpg)

A running assessment mode is also terminated when the corresponding course is
closed or deleted.

This video offers a step-by-step tutorial in German (refers to an older
OpenOlat version):

### Configuration options

Aside from the title and the description, the following parameters can be
configured for an exam setting:

 **Start** : Define here the date and starting time for the planned exam. All
OpenOlat functions will be inaccessible during the indicated **preparation
time** , specified in minutes and in effect before the actual exam.

 **End** : Date and time the exam finishes. All OpenOlat functions will be
inaccessible during the indicated **follow-up** , specified in minutes and in
effect after the actual exam.

 **Start / End mode** : You can choose between manual and automatic handling
of the exam. The selected manual mode adds start and end links to the
corresponding exam setting in the overview.

 **Participants** : Define here which users will be affected by the exam.
Selecting one of the options "Participants from course or groups", "Course
participants only" or "Group participants only". If you choose an option with
a group, select the affected groups using either the "Select groups" or
"Select learning areas" buttons.

 **Restrict access to single course elements** : In order to restrict the exam
to individual elements of the respective course, select the checkbox here and
click on the "Select course element" button. A list of all available elements,
of which you can choose those you wish to be visible during the exam appears.
All non-checked course elements will be masked for the duration of the exam.

 **First element shown** : If a particular element should be displayed upon
starting the exam, please make use of the button "Select course element" and
select one of the available course elements. Only those selected in the
previous step will be available for selection.

 **Limit to IP address:** In order to limit access to an exam to particular
computers or locations, you can check this box and enter the admissible IP
addresses. They should be available from your IT department. Use this option
if you wish to e.g. prevent a student to take an exam at his home computer.

 **Use Safe Exam Browser** : Using the Safe Exam Browser allows you to carry
out online exams safely, by putting the affected computer in a so-called kiosk
mode, changing any computer into a secure workstation. It prevents
unauthorised resources being used during an exam. Enter the browser exam keys
of all permitted Safe exam installations, in order to enable the exam in
those. Users will be notified about the required use of the SEB. Once a
permitted SEB installation is started, the exam can be carried out.

 **Apply exam setting for coach** : Select this checkbox if coaches of the
selected user groups should also be subjected to the exam and its effects.

A current assessment mode can be followed by the teacher in the assessment
tool. Evaluations, e.g. for submission tasks or essay elements of tests, can
also be evaluated directly and activated or made visible for the users. This
enables a direct inspection and review of exams. Furthermore, the teacher can
end the assessment in manual mode in the assessment tool.

  

