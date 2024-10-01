# Course Element "Topic Broker" {: #topic_broker}

## Profile

Name | Topic Broker
---------|----------
Icon | ![Topic Broker Icon](assets/icon_topic_broker.png){ class=size24  }
Available since | Release 19
Functional group | Administration and organisation
Purpose | self registration of participants in groups
Assessable | no
Speciality / Note | In contrast to the course elements "Topic assignment" and "Enrolment", all participants can specify several topics with priorities in the course element "Topic Broker". OpenOlat then creates assignments based on these topic and prioritization requests.

With the "Topic exchange" course module, a registration process for a topic is completed in 2 steps:<br>
1. Step: All participants indicate their preferred topics and prioritization.<br>
2. Step: The topics are assigned to the participants.

This division brings more fairness to the allocation of topics, because the allocation does not depend on who was able to register their wishes first.


## Functionality {: #topic_broker_functionality}

* One or more course participants can take part in the topic broker (no coaches).
* One or more topics can be offered for selection.
* Participants can specify a priority order for their chosen topics.
* Both a selection of topics and a limit on the number of people per topic can be specified. A limitation to groups is also possible.
* A certain number of topics per participant can also be made mandatory.
* The choice of topic is limited to a specific time slot.
* After closing the time window, OpenOlat can calculate who is assigned which topics based on the specified priorities. The calculation can be triggered automatically or manually.

[To the top of the page ^](#topic_broker)


## The algorithm for automatic topic assignment {: #topic_broker_algorithm}

If a selection and allocation process works on a first-come, first-served basis, then this is unfair. This is familiar from the allocation of tickets for football matches and concerts. Users with a better internet connection will be given preference, as will users who have time to log in immediately at the time of publication.

The problem is known as the "stable matching" problem. Details on the implementation in OpenOlat can be found here: [OpenOlat_Project_Broker_Matching_Algorithm.pdf](assets/OpenOlat_Project_Broker_Matching_Algorithm.pdf)

The assignment of topics in the course module Topic Exchange therefore takes place in 2 steps:

- Choice of topic/project/group and indication of personal priorities (first choice, second choice, etc.).
- Once everyone has submitted their preferred wishes, the assignment is made. If a topic was requested with first priority more often than there are places available, the assignment is made using the fair algorithm according to the information on the second priority. 

![course_element_topic_broker_periods_v1_de.png](assets/course_element_topic_broker_periods_v1_de.png){ class="shadow lightbox" }

!!! note "Note"

    Due to the functionality described above, it is understandable that the topic broker cannot be used in open courses with an undefined number of participants.

[To the top of the page ^](#topic_broker)


## Who can record eligible topics?

* By default, topics are entered by the **course owners**.

* **Coaches** can also be allowed to add topics in the "Topics" tab.

* **Coaches** can also be allowed to edit participants. (Assign topic, adjust prioritization, add or remove participants)

* Topics can also be imported from an **Excel file**.


[To the top of the page ^](#topic_broker)

---

## Set up topic exchange (course owner perspective) {: #topic_broker_setup}

### "Configurtion" Tab

In the "Configuration" tab, the framework conditions for the choice of subject and enrollment are defined.

![course_element_topic_broker_configuration_v1_de.png](assets/course_element_topic_broker_configuration_v1_de.png){ class="shadow lightbox" }


[Up (Course owner perspective) ^](#topic_broker_setup)<br>
[To the top of the page ^](#topic_broker)


### "Custom fields" tab

Additional fields can be created in the "Custom fields" tab, which are then displayed in each topic. They can be edited and deleted at any time under the 3 dots at the end of a line.

![course_element_topic_broker_custom_fields_v1_de.png](assets/course_element_topic_broker_custom_fields_v1_de.png){ class="shadow lightbox" }

![course_element_topic_broker_custom_field_add_v1_de.png](assets/course_element_topic_broker_custom_field_add_v1_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Name**<br>
The name entered here appears as an additional field in the "Add custom field" pop-up.


![2_green_24.png](assets/2_green_24.png) **Input type**<br>
**Text**: When entering data, you can enter a text entry for each topic. <br>
**File**: When entering, a file can be uploaded for each topic, e.g. a pdf file with information on the topic.


![3_green_24.png](assets/3_green_24.png) **Display in table**<br>
If the toggle button is activated, this field appears in the overview table by default.

[Up (Course owner perspective) ^](#topic_broker_setup)<br>
[To the top of the page ^](#topic_broker)

### Tab "Topic" (Capturing topics)

The selectable topics can be added and described by course owners in the "Topics" tab of the course editor. Alternatively, this can also be done outside of the editor in run mode. Depending on the configuration, this can also be done by course coaches.

![course_element_topic_broker_topics_v1_de.png](assets/course_element_topic_broker_topics_v1_de.png){ class="shadow lightbox" }

In the example below, the lower section also contains a field that was added in the "Custom fields" tab.

![course_element_topic_broker_add_topic_v1_de.png](assets/course_element_topic_broker_add_topic_v1_de.png){ class="shadow lightbox" }

[Up (Course owner perspective) ^](#topic_broker_setup)<br>
[To the top of the page ^](#topic_broker)

---

### Coach topic exchange (course coach perspective) {: #topic_broker_coaching}

### Capture topics

The selectable topics may have already been added and described by course owners (in the "Topics" tab in the course editor). Alternatively, this can also be done by course tutors. As a coach, select the course element and the "Topics" tab. The topics can be newly created here or imported from an Excel spreadsheet. (You will also find an Excel template for download under the "Import topics" selection option).

![course_element_topic_broker_topics_coach_v1_de.png](assets/course_element_topic_broker_topics_coach_v1_de.png){ class="shadow lightbox" }

[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)


### View of topic requests

In the "Participants" tab, coaches can see who has already submitted their topic requests, who is on the waiting list or who is already enrolled. Click on the + in front of one of the names to open the detailed view.

![course_element_topic_broker_participant_list1_v1_de.png](assets/course_element_topic_broker_participant_list1_v1_de.png){ class="shadow lightbox" }


!!! tip "Note"

    If course coaches have been given the right, they can intervene at any time and override a selection made or make a selection for the person if there is no selection.
    It is also possible to add another topic.

    However, this should only be used in exceptional situations if possible.

[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)

### Topic assignment (final enrollment pending)

The process proceeds in the following steps

* "Selection in progress"
* "Definitive enrollment pending"
* "Enrolment completed"

Once all participants have entered their topic requests and the time window for submission has closed, the "Selection in progress" phase is complete. The status changes to "**Definitive enrollment pending**".

Participants and topics must now be assigned. OpenOlat can automatically make assignments based on the topic and prioritization requests. For this purpose, OpenOlat uses a [fair algorithm](assets/OpenOlat_Project_Broker_Matching_Algorithm.pdf).

The execution of the assignment process can be triggered **automatically or manually**. The way in which the process is triggered is determined by the course owner in the course editor in the **"Configuration"** tab. 

[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)


### Automatic topic assignment {: #topic_broker_assignment_automatically}

If the course owner has selected the "Automatic" option in the "Configuration" tab in the course editor, the assignment algorithm will start automatically shortly after the time window in which the participants were able to make their selection has closed. (How long the process runs depends, for example, on the number of topics and participants).

The assignment algorithm is **only executed once**. The mapping result found is used for enrolment.

However, coaches can manually correct and amend the enrolments see [Adjustment](../learningresources/Course_Element_Topic_Broker.md#topic_broker_adjustment)

After an automatic assignment, an e-mail is always sent to all course participants.

[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)


###  Manual topic assignment/enrolment by coaches {: #topic_broker_assignment_manually}

If the course owner has selected the "Manual" option in the "Configuration" tab in the course editor, the execution of the assignment algorithm must be started by a course administrator.

The time when they trigger enrolment is not fixed.

![course_element_topic_broker_enrollment_start_v1_de.png](assets/course_element_topic_broker_enrollment_start_v1_de.png){ class="shadow lightbox" }

If the assignment algorithm is triggered manually, **several runs** can be made. The results differ because the algorithm also contains a random factor. They are listed in a dropdown and coaches can select a run to be used for the final enrolment.

![course_element_topic_broker_choose_a_run_v1_de.png](assets/course_element_topic_broker_choose_a_run_v1_de.png){ class="shadow lightbox" }

Once the coach has decided on a run (an assignment result), the **enrolment** is carried out based on this assignment by clicking on the "Apply" button. Reconfirmation is required, as enrolment cannot be repeated with a different assignment result/pass.

![course_element_topic_broker_confirm_assignment_v1_de.png](assets/course_element_topic_broker_confirm_assignment_v1_de.png){ class="shadow lightbox" }

In the case of manual kick-off, you can also specify that the participants are subsequently informed of the enrolment by e-mail.

![course_element_topic_broker_confirm_assignment_v1_de.png](assets/course_element_topic_broker_confirm_assignment_v1_de.png){ class="shadow lightbox" }

In the case of manual kick-off, you can also specify that the participants are subsequently informed of the enrolment by email.

!!! tip "Note"

    If there are still people with the status "Waiting list" or "Open" after clicking on "Apply", you can assign them manually (see [Adjustment](Course_Element_Topic_Broker.md#topic_broker_adjustment)).<br>
    This may be necessary, for example, if a person has not yet entered a topic after the time window has expired and therefore could not be assigned by the algorithm.


[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)


### Correction of topic assignment/enrolment by coaches {: #topic_broker_adjustment}

For an overview, select the course element as the course coach and then click on the plus symbol in front of a name in the list in the "Participants" tab. The view of the selection and prioritization of this person opens.

As a coach, you have the option of making the enrolment manually or removing a pre-selected topic. 

![course_element_topic_broker_enrollment_manually_v1_de.png](assets/course_element_topic_broker_enrollment_manually_v1_de.png){ class="shadow lightbox" }

Enrolment (including automatic enrolment) can be canceled by coaches (deregistration).

![course_element_topic_broker_enrollment_manually2_v1_de.png](assets/course_element_topic_broker_enrollment_manually2_v1_de.png){ class="shadow lightbox" }


[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)


### Export of topic requests and prioritizations {: #topic_broker_export}

In the "Topics" tab, you can use the "Export data" button to download a zip file containing all topics, requests and prioritizations (overview as an Excel file).

The button is available both in the course editor (for course owners) and in run mode for coaches/owners.

![course_element_topic_broker_topic_export_coach_v1_de.png](assets/course_element_topic_broker_topic_export_coach_v1_de.png){ class="shadow lightbox" }


[Up (Course owner perspective) ^](#topic_broker_coaching)<br>
[To the top of the page ^](#topic_broker)

---

## Choice of topic (student perspective) {: #topic_broker_participant}

As a participant, simply select the course element Topic Exchange in your course. Depending on the phase of the enrolment process, you will be shown the current status of topic allocation.

### 1. Step: Select topics
Click on the "Add" button for a topic description that you would like to enrol in and it will be added to the list of your selected topics. 

Depending on the preset authorization, participants can also withdraw an enrolment or reduce the number of enrolments.

![course_element_topic_broker_topic_participant_choose_v1_de.png](assets/course_element_topic_broker_topic_participant_choose_v1_de.png){ class="shadow lightbox" }


[Up (Perspective course participant) ^](#topic_broker_participant)<br>
[To the top of the page ^](#topic_broker)


### 2. Step: Prioritize topics

If you have many topics to choose from, it is advisable to first include all possible topics in your selection. In a second step, you can then create a ranking list from this preselection.

As long as the selection is still in progress (the time window for this is not yet closed), you can change the position of the topics in your list by clicking on the double arrows. Excess topics will then not be considered for enrolment.

![course_element_topic_broker_topic_participant_choose_priority_v1_de.png](assets/course_element_topic_broker_topic_participant_choose_priority_v1_de.png){ class="shadow lightbox" }

[Up (Perspective course participant) ^](#topic_broker_participant)<br>
[To the top of the page ^](#topic_broker)

### 3. Step: Wait for assignment

You will be informed as soon as you have been assigned a topic. The final assignment and enrolment (by your coach) will only take place once the selection period has expired and all course participants have submitted their requests. (To enable fair allocation, OpenOlat creates an allocation proposal from an algorithm).

![course_element_topic_broker_participant_v1_de.png](assets/course_element_topic_broker_participant_v1_de.png){ class="shadow lightbox" }


[Up (Perspective course participant) ^](#topic_broker_participant)<br>
[To the top of the page ^](#topic_broker)


### 4. Step: Request enrolment(s)

As soon as the final enrolment has been made by the coach, you as a participant will be able to see in the course element which topic(s) you have been enroled for.  

![course_element_topic_broker_participant_enrolled_v1_de.png](assets/course_element_topic_broker_participant_enrolled_v1_de.png){ class="shadow lightbox" }

[Up (Perspective course participant) ^](#topic_broker_participant)<br>
[To the top of the page ^](#topic_broker)

---

## Further informations

[Course element Topic Assignment](../learningresources/Course_Element_Topic_Assignment.md)<br>
[Course element Enrolment](../learningresources/Course_Element_Enrolment.md)<br>
[OpenOlat_Project_Broker_Matching_Algorithm.pdf](assets/OpenOlat_Project_Broker_Matching_Algorithm.pdf)<br>





