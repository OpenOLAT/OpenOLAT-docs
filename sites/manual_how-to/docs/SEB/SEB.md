# How do I prepare an exam with the Safe Exam Browser (SEB)? {: #SEB}



??? abstract "Aim and content of these instructions"

    You have already created a course with a test course element and now want to take the exam with the Safe Exam Browser.<br>
    The following instructions show you how to use the SEB.



??? abstract "Target group"

    [x] Authors [x] Coaches [ ] Participants

    [ ] Beginners [x] Amateurs  [x] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)
    * ["How do I proceed when creating a test?"](../test_creation_procedure/test_creation_procedure.md)


---

## The SEB - What is it? {: #SEB_description}

Instead of performing an online exam with browsers such as Edge, Firefox, Safari or Chrome, the [Safe Exam Browser](http://www.safeexambrowser.org) can be made mandatory to call up the OpenOlat online exam. This special browser makes it possible to disable the ability to access other websites or functions such as copy & paste during the exam period (kiosk mode). This prevents the use of unauthorized sources during an exam. 

An [Assessment mode](../../manual_user/learningresources/Assessment_mode.md) can be configured in a course under **Administration > Assessment management**, which defines the conditions (time window etc.) of an assessment. As part of an [Assessment mode](../../manual_user/learningresources/Assessment_mode.md), you can also determine whether the SEB should be used. If this option is activated, the SEB can be configured directly there in OpenOlat and a configuration file can be generated for sending to the participants. 

!!! info "The SEB is an external tool"

    The Safe Exam Browser is not developed by frentix GmbH, therefore we can neither guarantee nor directly influence its functionality. Our support is also limited to the OpenOlat-side configuration options for calling up this external tool.


[To the top of the page ^](#SEB)

---

## As an OpenOlat author, how do I set up a test with the SEB? {: #SEB_setup}

### Step 1: SEB installation {: #SEB_installation} 

The installation file can be found on the [Web site of the manufacturer](https://www.safeexambrowser.org/download_en.html).

Also ask all exam participants to install the SEB on their computer. Or, if separate computers are provided for the exam, prepare these computers accordingly.

[To the top of the page ^](#SEB)

---

### Step 2: Create assessment mode {: #create_assessment_mode}

As author of the OpenOlat exam course, you create an exam mode under<br> 
**Administration > Assessment management > Tab "Configuration assessment mode" > Button "Add assessment mode"**

![SEB_new_assessment_mode_v1_de.png](assets/SEB_new_assessment_mode_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#SEB)

---

### Step 3: Activate SEB {: #activate_SEB}

The use of the SEB is optional in test mode. If desired, activate this option under<br>

**Administration > Assessment management > Tab "Configuration assessment mode" > Select/edit mode > Tab "Safe Exam Browser"**

![SEB_activate_v1_de.png](assets/SEB_activate_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#SEB)

---

### Step 4: Configuration
As soon as the SEB has been activated, the configuration options are displayed. The options and their effects on the subscriber view are briefly described below.

For configuration in OpenOlat applies:<br>
The suggested settings can be set in the OpenOlat system administration. They can therefore be regarded as a recommendation from your administrator to adopt them.

![SEB_config_v1_de.png](assets/SEB_config_v1_de.png){ class="shadow lightbox" }


![1_green_24.png](assets/1_green_24.png) **Type of application**<br>
We recommend the configuration here on this page in OpenOlat. In principle, however, it is also possible to use the SEB configuration file. This can be adapted with a text editor if required. When using the supplied configuration, the Safe Exam Browser Keys must be entered in OpenOlat. (More about this on the [manufacturer's website](http://www.safeexambrowser.org).). Apart from the information text, the configuration options listed below are unnecessary in this case. 


![2_green_24.png](assets/2_green_24.png) **Downloadable configuration file**<br>
If "Yes" is selected here, the configuration file can be downloaded from OpenOlat by the exam participants when exam mode is started. Authors can also download the file at any time and send it to the exam participants. See [Step 6](#download_SEB_configfile).

If "No" is selected here, the download option is no longer available for participants, but is still available for authors, as described in [Step 6](#download_SEB_configfile).


![3_green_24.png](assets/3_green_24.png) **Allow termination of SEB**<br>
Some exam participants finish earlier and are then unable to access OpenOlat or other websites until the end of the exam mode. 
If there is no risk of abuse (mutual assistance), exam participants can be allowed to exit the SEB as soon as they have submitted their exam. In this case, a Quit button is displayed at the bottom right of the screen.


![4_green_24.png](assets/4_green_24.png) **Exit/unlock password**<br>
This input field is only displayed as a configuration option if exiting the SEB has been permitted.
If exam participants click the Quit button to end the SEB restrictions, they will be prompted to enter this password. 

In the case of an examination in a common examination room, for example, the examination invigilator can give this password to each person leaving the examination room.


![5_green_24.png](assets/5_green_24.png) **Link to leave SEB after the exam**<br>
If no Quit button is to be displayed, this link can be provided in a suitable place within the exam. Exam participants can then use it to exit the Safe Exam Browser.


![6_green_24.png](assets/6_green_24.png) **User must confirm the termination**<br>
If this option is activated, all exam participants must confirm the end of the exam again. This is intended as a safety measure to ensure that an exam is not ended accidentally.


![7_green_24.png](assets/7_green_24.png) **Allow reload in check**<br>
If the website (exam page) is allowed to be reloaded while the exam is running, a reload button will appear at the bottom right of the screen for the exam participants. 


![8_green_24.png](assets/8_green_24.png) **Browser view mode**<br>
Select one of the specified modes. If no other websites have been shared, full screen mode is recommended. If the exam participants are to access certain shared pages, it may be useful to use browser windows. 


![9_green_24.png](assets/9_green_24.png) **SEB taskbar display**<br>
This option affects some other options. If the taskbar is not displayed, the displays for the exit button, audio control, time, keyboard layout and WiFi selection are also missing.


![10_green_24.png](assets/10_green_24.png) **Show reload button**<br>
If reloading is permitted, a button for reloading is displayed at the top left. If "No" is selected, it is grayed out and cannot be used.


![11_green_24.png](assets/11_green_24.png) **Display time**<br>
A helpful feature for exam participants to keep an eye on the remaining time. 


![12_green_24.png](assets/12_green_24.png) **Show keyboard layout selection**<br>
A selection of keyboard layouts for changing languages is displayed.


![13_green_24.png](assets/13_green_24.png) **Show WiFi selection**<br>
The selection of accessible WiFi networks is displayed at the bottom right of the taskbar if the option is set to "Yes".


![14_green_24.png](assets/14_green_24.png) **Display audio control**<br>
The audio control can be displayed at the bottom right of the taskbar. This option is required for tests with video or audio.


![15_green_24.png](assets/15_green_24.png) **Mute at start**<br>
If audio control is deactivated, this option prevents the use of audio devices.


![16_green_24.png](assets/16_green_24.png) **Allow audio recording (microphone, win)**<br>
It is recommended that you only activate this option if audio recordings are explicitly desired during the exam.


![17_green_24.png](assets/17_green_24.png) **Allow video recordings (Webcam, Win)**<br>
It is recommended that you only activate this option if video recordings are expressly desired during the exam.


![18_green_24.png](assets/18_green_24.png) **Allow spell check**<br>
Depending on the subject of the check, the spell check (currently only English) can be deactivated or made available. If the option is set to "Yes", misspelled words are underlined in red.


![19_green_24.png](assets/19_green_24.png) **Allow zoom in/out**<br>
Reasons for suppressing the zoom could be, for example, that the exam participants could read unwanted writing on image material through zoom. As a rule, however, Zoom should be allowed in order to ensure good readability (especially with BYOD - Bring your own device). You can zoom with Ctrl + and Ctrl -, as well as in the menu at the top right.


![20_green_24.png](assets/20_green_24.png) **Activate URL-filter**<br>
If the filter is activated, all websites are blocked except for the check. When activated, further configuration options are displayed. There you can control more precisely which URLs may also be accessed during the check.

![SEB_config_url_filter_v1_de.png](assets/SEB_config_url_filter_v1_de.png){ class="shadow lightbox" }


**Filter embedded content as well**<br>
If this option is selected, the content of a page is also checked to see whether it contains permitted/not permitted expressions and access is enabled or blocked accordingly.

**Permitted expressions**<br>
The expressions specified in this positive list may be searched for by the examination participants during active examination mode.

**Allowed regex**<br>
Regex are "regular expressions" (= placeholders). This whitelist can be used to specify which expressions with placeholders may be searched for by exam participants while the exam mode is active.

**Blocked expressions**<br>
Expressions specified here block access to URLs and file names on your own computer that contain these expressions.
If the option "Also filter embedded content" is selected, even if they are found in their content. 

**Blocked regex**<br>
URLs with the regex expressions (expressions with placeholders) specified here are blocked. If the embedded content is also filtered, such pages are also blocked.


![21_green_24.png](assets/21_green_24.png) **Configuration key of the saved configuration**<br>
If the configuration file is created in OpenOlat, this key does not need to be entered separately. It is only required if you edit a configuration file yourself.


**Note:** The generated key changes with every change to the configuration file.
You should therefore only copy and use the key after you have made all the settings.


![22_green_24.png](assets/22_green_24.png) **Safe Exam Browser Note**<br>
The information text entered here appears as soon as the exam participants start the SEB. For example, you can point out the examination conditions and the restrictions imposed by the SEB again here.


[To the top of the page ^](#SEB)

---


### Step 5: Create configuration file {: #create_SEB_configfile}
In the "Safe Exam Browser" tab, select the option<br> **"Downloadable configuration file: Yes"**.<br>
Don't forget to save the configuration!

![SEB_configfile_create_v1_de.png](assets/SEB_configfile_create_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#SEB)

---


### Step 6: Download configuration file {: #download_SEB_configfile}

Once the configuration is complete (step 5), return to the previous level **"Exam administration"** to export the configuration file, where all exam modes are listed.

For the relevant test mode, click on <br>

![SEB_configfile_download_v1_de.png](assets/SEB_configfile_download_v1_de.png){ class="shadow lightbox" }

Beispiel: SEBClientSettings.seb


[To the top of the page ^](#SEB)

---

### Step 7: Send configuration file {: #distribute_SEB_configfile}
In order for the test participants to be able to start a test in the SEB, they must run a configuration file on their computer. (Beispiel: SEBClientSettings.seb) The file can be sent to the exam participants by e-mail, for example, or offered for download via a page.

!!! tip "Note for download"

    Save the SEB configuration file on a page that is not restricted by the Safe Exam Browser in order to allow access at any time, even when exam mode is activated. (Specify a permitted download page in the configuration).

!!! tip "Note on other examination fraud"

    Please note: The Safe Exam Browser only restricts the use of the current device. However, exam fraud can also occur through the use of a smartphone, unauthorized documents or exchanges with other people.

[To the top of the page ^](#SEB)

---


## Starting the exam by coaches

The start and duration of the exam is determined by the specification in the configuration of the [Assessment mode](../../manual_user/learningresources/Assessment_mode.md). If a manual start by coaches is desired, the examination mode can be activated under
**Administration > Assessment management > Tab "Configuration exam mode"**
by clicking on the **Start button**.

![SEB_start_assessment_mode_v1_de.png](assets/SEB_start_assessment_mode_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#SEB)

---

## How do participants start an OpenOlat exam with the SEB?  {: #SEB_participants}

**Step 1: Installation of the SEB**<br>
The Safe Exam Browser must be installed on the device in advance. 
The installation file can be found on the [manufacturer's website](http://www.safeexambrowser.org/download_en.html).

In order to identify difficulties, a trial test organized by the coaches in advance is recommended. This ensures that the SEB is installed on all computers in advance.

**Step 2: Receiving the configuration file**<br>
All exam participants must receive the configuration file from their supervisors (e.g. by email or as a download).


**Step 3: Start test by calling up the configuration file**<br>
Exam participants start the exam by opening this configuration file. As soon as the configuration file is double-clicked, the SEB opens and the other functions of the computer are restricted. 


!!! tip "Note"

    If you have candidates who do not want to install the SEB, you as the examiner may be able to lend them special exam computers. To be on the safe side, point out that examination candidates should proactively contact the teachers.


!!! tip "Bring your own device (BYOD)"

    The SEB also enables secure examinations on the examinees' private computers. The prerequisite is that the Safe Exam Browser has been installed on the device in advance. The SEB can then be accessed on various BYOD devices using the sent configuration file.


[To the top of the page ^](#SEB)

---


## As a coach, how can I intervene while an exam with the SEB is in progress? {: #SEB_intervention}

As a general rule, you should not intervene while the check mode is running. However, if it is necessary for compelling reasons, the intervention is carried out via [Check mode](../../manual_user/learningresources/Assessment_mode.md).


!!! tip "Note"

    A special exam chat is available in OpenOlat for communication between supervisors and exam participants.
    You can find out more about communication during an exam [here](../communication_during_exam/communication_during_exam.md).

[To the top of the page ^](#SEB)

---


## How is a test ended with the SEB? {: #SEB_exit}

An online assessment in OpenOlat can be completed <br>
a\) automatically or <br>
b) manually <br>

If an assessement is ended **manually**, <br>
\- a coach can stop the SEB for all participants at the same time.<br>
or
\- each assessment participant can stop the SEB themselves with an individual exit link.


### End assessment automatically

The SEB is used as part of an **assessment mode** in OpenOlat. If the check mode is ended, the SEB is also ended.
The automatic termination of a check mode is configured under<br>
**Administration > Assessment management > Tab "Configure assessment mode"**


### End assessment manually (Examination at the same time for all students, by coaches)

This also applies here: If the **assessment mode** is ended by the coach, the SEB is also ended. The manual termination of a running assessment mode is carried out by coaches under
**Administration > Assessment management > Tab "Configure assessment mode"**<br>
As soon as an assessment mode has been activated, a "Finish" or "End assessment" button is displayed. Click one of the two buttons. The status of the exam mode then changes to "Finished".

![SEB_quit_exam_mode_v1_de.png](assets/SEB_quit_exam_mode_v1_de.png){ class="shadow lightbox" }


### Individual exit via exit link

If it has been configured accordingly (see [Step 4](#SEB_configuration)), a Quit button is displayed in the bottom right-hand corner of the SEB. If assessment participants click on this link, they will be asked to enter the password to exit. Participants can only exit the browser if they have this password. As a coach, you can announce the password at the appropriate time. (E.g. when candidates want to leave the assessment room).

[To the top of the page ^](#SEB)

---

## SEB during the inspection of the assessment results {: #SEB_exam_inspection}

By using the SEB, all other activities on the computer can also be blocked while the assessment results are being viewed.

[See the details > ](../../manual_user/learningresources/Assessment_inspection.md)<br>
[To the top of the page ^](#SEB)

---

## Check list {: #SEB_checklist}

- [x] Examinees informed that use of the SEB is mandatory?
- [x] Download and installation of the Safe Exam Browser on all participants' devices?
- [x] Communication during the exam clarified beforehand? (e.g. use of the exam chat)
- [x] Is communication of the password for exit regulated? (e.g. individual announcement shortly before leaving the examination room)
- [x] Procedure for ending the audit clarified in advance?
- [x] Mock exam conducted? With all exam participants?
- [x] Exam mode configured?
- [x] SEB activated in test mode?
- [x] SEB configuration file created?
- [x] SEB configuration file sent?
- [x] Instructions given to end the test? 


[To the top of the page ^](#SEB)


---


## Further information

[Website of the manufacturer >](http://www.safeexambrowser.org)<br>
[Assessment mode >](../../manual_user/learningresources/Assessment_mode.md)<br>
[Assessment inspection > ](../../manual_user/learningresources/Assessment_inspection.md)<br>


