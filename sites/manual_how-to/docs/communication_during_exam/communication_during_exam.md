# Communication during an exam {: #communication_during_exam}

??? abstract "Objectives and content of this instruction"

    You have already prepared a course for an online exam and want to take the exam online within a certain time frame.<br>
    The following instructions show you which communication options are available to you during the exam in OpenOlat.

??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants

    [ ] Beginners [x] Advanced users  [x] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)
    * ["How do I proceed when I create a test?"](../test_creation_procedure/test_creation_procedure.md)
    * You have already prepared a course for the online exam.

---

## Communication needs {: #needs}

During an online exam, **various communication needs** may arise:

* individual participants have individual problems
* the exam supervision (coach) would like to point out that there are only 10 minutes left to complete the work
* the coach answers the question of a single person
* the coach recognizes through a query that a note to all exam participants is required
* ...

OpenOlat has communication options for these situations, even if the [Assessment mode](../../manual_user/learningresources/Assessment_mode.md) is active and the [Safe Exam Browser](../../manual_user/learningresources/Assessment_mode.md#tab-safe-exam-browser) deactivates all other tools on the computer.

In particular, these are **the two communication tools**

* **Messages** (from coaches to everyone) and
* the **Supervisor chat** (exam chat), 1:1 with coaches or from coaches to everyone

<br>

[Up (Section Communication needs) ^](#needs)<br>
[To the top of the page ^](#communication_during_exam)


---


## 1. Set up communication channels as course owner/author {: #author}

Would you like to allow exam participants to ask questions during the exam?<br>
The tool for this is the **Supervisor chat**. As the course owner, you configure it in the course editor:<br>
`Course > Administration > Course editor > Course element "Test" > Tab "Communication"`

![Form Supervisor chat with Allow requests from participants set to Yes and global notification for the coaches](assets/communication_during_exam_author1_v1_de.png){ class="shadow lightbox" title="Tab Communication of the course element Test in the course editor" }

* **Allow requests from participants**: With "Yes", exam participants and coaches can start requests via chat. With "No", only coaches start a chat.
* **Enable global notification for**: For new chat activities, OpenOlat informs the selected course roles, owners or coaches, in the global menu bar. The coaches are preselected.

The Supervisor chat during exams works regardless of whether the general chat function is activated in the OpenOlat instance or not.

[Up (Section Course owner/author) ^](#author)<br>
[To the top of the page ^](#communication_during_exam)

---

## 2. Communicate as coach {: #coach}

### Where can I find the communication tools?

* In the menu, select the test **course element** that contains the exam.
* As a coach, you will not see the test after clicking on it (like the participants), but several tabs.
* Select the **"Communication"** tab. There you will find the tools for communication between exam supervision (coaches) and exam participants.

In the **upper area** "Message to all participants" you create, edit and manage the **messages** to all exam participants, before and during the exam.

In the **lower area** "Supervisor chat" you can see an overview of the **chat** histories (1:1) with the exam participants.

![Tab Communication with the areas Message to all participants and Supervisor chat, both still without entries](assets/communication_during_exam_coach1_v1_de.png){ class="shadow lightbox" title="Tab Communication in the course element Test" }

!!! info "Multiple coaches"

    If there are several coaches, each of them can answer a question asked by exam participants in the chat.

### Message to all

Messages can be sent by coaches to all exam participants. You create a new message with the button "Create new message".

![Button Create new message marked, below it the filters All, Planned, Published and Expired](assets/communication_during_exam_coach2_v1_de.png){ class="shadow lightbox" title="Area Message to all participants" }

A message can be published immediately and displayed to the exam participants or within a specific time window. Under "Publication" you choose "Immediately until the end of the day" or "Individual schedule" with publication date and expiration date. The time window for publication can also be in the future so that messages can be prepared.

![Message to the exam participants with individual schedule, publication date and expiration date](assets/communication_during_exam_coach3_v1_de.png){ class="shadow lightbox" title="Dialog Message to all participants" }

### Answering questions from individual participants

If questions are received from exam participants, they are listed in the lower area "Supervisor chat".<br>
If a request has been waiting for a response for more than five minutes, the row has a red background. A yellow background indicates new requests. If a coach has already responded, the background turns white.

To answer, click on **"Join"** in the relevant row in the "Action" column.

![Two requests in the status Requested, the older one with red and the new one with yellow background, each with the link Join in the column Action](assets/communication_during_exam_coach_answer_chat1_v1_de.png){ class="shadow lightbox" title="Area Supervisor chat in the tab Communication" }


If there are several coaches, each coach decides for themselves whether to join a chat.<br>
All coaches (exam supervision) can see in the column "Supervisor" which coaches are currently chatting with an exam participant.

![Column Supervisor marked, it names the coaches who joined each chat, two persons for one of the chats](assets/communication_during_exam_coach_several_v1_de.png){ class="shadow lightbox" title="List of chats in the area Supervisor chat" }



### Get in touch with individuals as a coach

If you as a coach want to contact an **individual** during the exam on your own initiative, use the **chat**. Click on the button "Add participant".

![Button Add participant marked above the still empty list of chats](assets/communication_during_exam_coach_add_chat1_v1_de.png){ class="shadow lightbox" title="Button Add participant in the tab Communication" }



### Message to several chats at once

As a coach, you normally create a **message** for a note to all exam participants. However, there are also exceptional cases in which an answer in all **chats** makes sense.

**Example:**<br>
Several participants write: "There is error xy in the exam situations". As a coach, you therefore immediately expect further chat messages from another 100 exam participants. That's why you want to send a reply to all exam participants right away with a note saying, "Attention, for those who haven't noticed yet … We are now doing …".

Normally, you would have to reply in all 1:1 chats and close each chat individually. For this situation, mark the chats concerned in the list. With the button "Send message" you send a message to all marked chats, with "Complete request" you close them together. For plannable, non-spontaneous information, however, it is advisable to send a message.

![Two marked chats, above them the buttons Send message and Complete request](assets/communication_during_exam_coach_bulk_action_v1_de.png){ class="shadow lightbox" title="List of chats with two marked chats" }


### Video chat

Sometimes it is helpful if the exam supervision and the exam participant can see each other briefly in a 1:1 video chat. BigBlueButton or Microsoft Teams is available for the video chat as soon as administrators have enabled one of them for the Supervisor chat, see [Activate video chat as administrator](#admin).

Only **coaches can start** a video chat, with "Start video conference" in the chat window below the input field.<br>
Exam participants will then receive an invitation and can accept it.

![Link Start video conference below the input field and the sent invitation to a video conference in the history](assets/communication_during_exam_coach_answer_video_v1_de.png){ class="shadow lightbox" title="Chat window Supervisor chat" }


!!! info "Important"

    If a video conference is running and the chat (1:1) is changed, the old video conference is canceled. Only 1:1 is ever possible. This ensures that other people are not unintentionally present in a video conference.


### Supervising multiple exams

It is possible for coaches to supervise several exams taking place at the same time. For example, a subject expert can be available for subject-related problems, while other coaches take on the organizational tasks of the exam supervision.

So that this person does not have to switch to the different courses to check the chats there, OpenOlat informs them about new chat activities in the global menu bar. The prerequisite is that their course role is selected under "Enable global notification for", see [Set up communication channels as course owner/author](#author).

However, when the exams are over, these notes are also gone. They are only available during the exam.



### Documentation of messages and chat history

Since **messages** may be relevant for appeals, they can only be deleted as long as they have the status "Scheduled". After publication, they can only be withdrawn. A withdrawn message gets the status "Expired" and remains in the list.

![Message in the status Scheduled, its menu with the three dots offers Edit and Delete](assets/communication_during_exam_coach_documentation1_v1_de.png){ class="shadow lightbox" title="List of messages before publication" }

![Message in the status Published, its menu with the three dots offers Edit and Withdraw](assets/communication_during_exam_coach_documentation2_v1_de.png){ class="shadow lightbox" title="List of messages after publication" }

You archive the history of a **chat** via the menu with the three dots at the end of its row: "Archive" downloads the history of this one chat. For a completed chat, the same menu also offers "Reactivate request".

![Chat in the status Completed, its menu with the three dots offers Reactivate request and Archive](assets/communication_during_exam_coach_chat_archive_v1_de.png){ class="shadow lightbox" title="Menu of a completed chat" }

<br>

[Up (Coach section) ^](#coach)<br>
[To the top of the page ^](#communication_during_exam)

---

## 3. Communicate as a participant {: #participant}

### Messages from the exam supervision

Messages can only be sent by coaches (exam supervision) to the exam participants. The other way around is not possible. The Supervisor chat serves for requests from exam participants.

Messages appear in the header for exam participants. They remain there until a read confirmation has been submitted by clicking on the button "Read".

A message is also displayed outside the test course element, e.g. if the test has not yet been started.

![Message above the test with time and button Read](assets/communication_during_exam_participant1_v1_de.png){ class="shadow lightbox" title="Test from the view of the exam participants" }

Messages disappear after a read confirmation has been submitted. However, they can be displayed again at any time via the info icon in the header.

![Info icon marked, the opened window Messages shows the read message with a check mark](assets/communication_during_exam_participant2_v1_de.png){ class="shadow lightbox" title="Window Messages in the running test" }


### Asking the exam supervision questions

If the course owner has allowed requests from participants, a speech bubble icon appears in the header for the exam participants. A **1:1 chat** can be started there in a separate chat window. With "Mark request as done and close", exam participants end their request.

![Speech bubble icon marked, the opened window Supervisor chat shows the welcome message and the input field for the question](assets/communication_during_exam_participant_chat1_v1_de.png){ class="shadow lightbox" title="Supervisor chat in the running test" }

[Up (Participant section) ^](#participant)<br>
[To the top of the page ^](#communication_during_exam)

---

## 4. Activate video chat as administrator {: #admin}

So that coaches can start a video conference from the Supervisor chat, administrators enable BigBlueButton or Microsoft Teams for the Supervisor chat. One of the two modules is sufficient, and it must be switched on itself. To do this, activate the option "Supervisor chat" under "Activate for" in the system administration:<br>
`Administration > External tools > BigBlueButton > Tab "Configuration"`<br>
`Administration > External tools > Microsoft Teams > Tab "Configuration"`

![Option Chat-Prüfung under Aktivieren für marked, on the left in the menu External tools the entry BigBlueButton](assets/communication_during_exam_admin1_v1_de.png){ class="shadow lightbox" title="Tab Configuration in the module BigBlueButton" }

The other settings of the two modules are described on the pages [BigBlueButton module](../../manual_admin/administration/BigBlueButton_module.md#tab_config) and [Microsoft Teams module](../../manual_admin/administration/Teams_module.md#activate_for).

[Up (Admin section) ^](#admin)<br>
[To the top of the page ^](#communication_during_exam)


---

## Checklist {: #checklist}

- [x] Are there several coaches at the exam?
- [x] Should exam participants be able to ask coaches questions during the exam?
- [x] Are there opportunities for communication between the coaches outside of the exam course?
- [x] Should coaches be able to send messages to all exam participants during the exam?
- [x] Have texts for messages of greeting, for the note on the imminent end of the exam, etc. been prepared and agreed?
- [x] Are all members of the exam supervision aware of the communication options during the exam? (Messages and Supervisor chat)


[To the top of the page ^](#communication_during_exam)

## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I create my first OpenOlat course? >](../my_first_course/my_first_course.md)<br>
[How do I proceed when I create a test? >](../test_creation_procedure/test_creation_procedure.md)<br>
[Assessment management: Assessment mode >](../../manual_user/learningresources/Assessment_mode.md)<br>
[BigBlueButton module >](../../manual_admin/administration/BigBlueButton_module.md)<br>
[Microsoft Teams module >](../../manual_admin/administration/Teams_module.md)

**Further reading**<br>
[Course Element "Test" >](../../manual_user/learningresources/Course_Element_Test.md)<br>
[How do I prepare an online exam? >](../exam_preparation/exam_preparation.md)<br>
[How do I prepare an exam with the Safe Exam Browser (SEB)? >](../SEB/SEB.md)

**youtube**<br>
[Testing overview (German)](<https://www.youtube.com/embed/fkqH41-8CaI>)<br>
[How do tests work in OpenOlat? (German)](<https://www.youtube.com/embed/M0p3UKaEOlg>)

[To the top of the page ^](#communication_during_exam)
