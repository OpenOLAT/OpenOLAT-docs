# As an administrator, how do I set up the Safe Exam Browser (SEB) system-wide? {: #SEB_admin}


??? abstract "Aim and content of these instructions"

    The following instructions show you how to set up the SEB as an administrator.

??? abstract "Target group"

    [x] Authors [ ] Coaches  [ ] Participants [x] Administrators

    [ ] Beginners [x] Amateurs  [x] Experts


??? abstract "Expected previous knowledge"

    * [How do I prepare an exam with the SEB? (for authors) >](../../manual_how-to/SEB/SEB.md)
  


---


## The SEB - what is it? {: #SEB_description}

Instead of running an online exam with browsers such as Edge, Firefox, Safari or Chrome, the [Safe Exam Browser](http://www.safeexambrowser.org) can be made mandatory for accessing the OpenOlat online exam. This special browser makes it possible to disable the option to open other websites or functions such as copy & paste during the exam period (kiosk mode). This prevents the use of unauthorised sources during an exam. 

In a course under `Course administration > Assessment management`, an [assessment mode](../../manual_user/learningresources/Assessment_mode.md) can be configured that defines the conditions (time window, etc.) of an exam. Within an [assessment mode](../../manual_user/learningresources/Assessment_mode.md) you can also determine whether the SEB should be used. If this option is activated, the SEB can be configured directly there in OpenOlat and a configuration file can be generated for sending to the participants. 

!!! info "The SEB is an external tool"

    The Safe Exam Browser is not developed by frentix GmbH, so we can neither provide guarantees nor directly influence its functionality. Our support is also limited to the configuration options on the OpenOlat side for accessing this external tool.


[To the top of the page ^](#SEB_admin)

---


## Where and how do I set up the SEB as an OpenOlat administrator? {: #SEB_setup}

Before authors and coaches can use the Safe Exam Browser in an assessment mode, the administration must activate the SEB system-wide in OpenOlat.

This pre-configuration can only be carried out with administration rights (role System administrator). 

All computers on which exams are to be carried out with the SEB must also have the SEB installed. As an administrator, you may have an advisory and supporting role here.

[To the top of the page ^](#SEB_admin)

---

### Step 1: Install the SEB if necessary {: #SEB_installation} 

!!! note "Note"

    It is not strictly necessary for you as an administrator to have the Safe Exam Browser installed on your own computer. Only everyone involved in an exam needs this browser. For testing and advisory purposes, however, it may be helpful if you as an administrator also have the SEB installed. 

There is a separate Safe Exam Browser for each operating system (Windows, macOS, iOS).

Download the browser from the [manufacturer's website (ETH Zurich)](http://www.safeexambrowser.org/) and install it.

!!! tip "Tip"

    Pay attention to which version of the SEB you install.
    Later, a specific SEB version can be required in the configuration file. The participants must then have the corresponding Safe Exam Browser version installed.

[To the top of the page ^](#SEB_admin)

---

### Step 2: Switch on the assessment mode {: #activate_assessment_mode}

The Safe Exam Browser is always used within an assessment mode. Activating the assessment mode is therefore a prerequisite. You do this under:<br>
**Administration > e-Assessment > Assessment management > Tab "Assessment management configuration"**

![SEB_Admin_step2_v1_de.png](assets/SEB_Admin_step2_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#SEB_admin)

---


### Step 3: Define the minimum version of the SEB {: #SEB_min_version} 

As an administrator, you can enforce the use of a specific minimum version of the Safe Exam Browser system-wide. Exam participants with an older SEB version are then not admitted.

A separate minimum version can be defined for each operating system.

You make this setting under<br>
**Administration > e-Assessment > Assessment management > Tab "Safe Exam Browser versions"**

![SEB_Admin_step3_v1_de.png](assets/SEB_Admin_step3_v1_de.png){ class="shadow lightbox" }


!!! note "Note"

    New versions of the SEB are released at irregular intervals. Occasionally, this also results in a need for adjustments in OpenOlat when minimum versions are prescribed. You maintain the SEB versions permitted on the OpenOlat instance in the same place.

[To the top of the page ^](#SEB_admin)

---


### Step 4: Clarify which conditions the SEB should set system-wide {: #SEB_clarify_requirements} 

Find out about the available functions on the [manufacturer's website (ETH Zurich)](http://www.safeexambrowser.org/) and clarify the desired requirements with the people responsible for conducting the exams.

[To the top of the page ^](#SEB_admin)

---

### Step 5: Configuration completely manual or with a template? {: #SEB_config_process} 

The SEB can be configured

- completely manually in the course (by authors)
- with a template (provided by administrators)

As an administrator, clarify with those responsible for the exams whether and which templates are needed.

[To the top of the page ^](#SEB_admin)

---


### Step 6: Provide an SEB configuration template {: #SEB_config_file} 

If configuration templates are to be used (clarification in step 5), the clarifications made in step 4 can now be described and stored in various configuration templates. Under
**Administration > e-Assessment > Assessment management > Tab "Safe Exam Browser configuration"** you can provide a configuration template in 2 ways:

- by creating a template directly in OpenOlat
- by importing a .seb file

![SEB_Admin_step6_create_import_v1_de.png](assets/SEB_Admin_step6_create_import_v1_de.png){ class="shadow lightbox" }

#### Option 1:

You can create a new SEB configuration template yourself directly in OpenOlat. To do this, select the "Create template" button.
The configurable options are described here: [SEB configuration template](../../manual_admin/administration/e-Assessment_AssessmentMgmt.md#tab_seb)

#### Option 2: 

Alternatively, you can also import an unencrypted .seb file as a template.<br> 
Open the SEB and create/save/export the SEB configuration file there.

#### List of templates

All created or imported configuration templates are listed under the "Safe Exam Browser configuration" tab and can be edited, activated/deactivated or set as default by administrators.

![SEB_Admin_step6_list_v1_de.png](assets/SEB_Admin_step6_list_v1_de.png){ class="shadow lightbox" }

**Type column**<br>
This column shows you how the template was created:<br>
Form -> This template was created directly in OpenOlat (see Option 1)<br>
SEB file -> This template was imported (Option 2). 

**Status column**<br>
A configuration template can have either the status "Active" or "Inactive".

**Default column**<br>
This column shows you which templates you have set as default via the three-dot icon.

**Uses column**<br>
This shows you how often a template is already being used by authors in exam courses. 

**Edit column (icon)**<br>
Clicking on one of the edit icons opens the popup window in which the configuration options on the OpenOlat side are displayed.

**Three dots**<br>
Clicking on a three-dot icon shows the options

- Edit
- Set as default
- Deactivate


[To the top of the page ^](#SEB_admin)

---


### Step 7: Activate the Events / Absences module if necessary {: #SEB_module_events}

For everyone who works with the "Events / Absences" module:<br>
The assessment mode and the SEB configuration can also be configured directly on an event.
The procedure (for authors) is analogous to creation in "Course administration > Assessment management"; it is the same process in "Course administration > Events".

As an administrator, you carry out the basic activation of the Events and Absences module under: **Administration > Modules > Events / Absences > Configuration tab > Configuration at course level section**.

In this tab you can then also define whether the Safe Exam Browser should be used with manual keys or keys in the SEB config. (Keys in the SEB config are recommended.)

!!! note "Note"

    The toggle in the Events / Absences module controls only the path via an event. A directly created assessment mode ignores it completely.


!!! note "Note"

    There are different types of events in OpenOlat:<br> 
    An event can (e.g. in Projects) have several assigned properties.<br>
    In addition, there are also events that are merely calendar entries.


[To the top of the page ^](#SEB_admin)

---



## Support knowledge for administrators {: #SEB_support} 

As an administrator, you may need to answer questions from authors. The following therefore describes some process steps that you as an administrator do not have to carry out yourself, but rather the authors. As a contact person and expert for OpenOlat, however, you should also have this background knowledge. Also consult the guide for authors: 
[How do I prepare an exam with the SEB?](../../manual_how-to/SEB/SEB.md)

### (by the course owner) Create an assessment mode {: #create_assessment_mode}

As the author of the OpenOlat exam course, you create an assessment mode under<br> 
**Course administration > Assessment management > Tab "Assessment mode configuration" > "Add assessment mode" button**

[To the top of the page ^](#SEB_admin)

---

### (by the course owner) Creating the configuration file {: #create_config_file}

Authors create a configuration file in the course (if necessary with the help of the configuration template) 
under **Course administration > Assessment management > Tab "Assessment mode configuration" > Select/edit mode > Tab "Safe Exam Browser"**

See [Step 4: Configuration (for course owners) >](../../manual_how-to/SEB/SEB.md#SEB_configuration)

[To the top of the page ^](#SEB_admin)

---


### (by the course owner) Distributing the configuration file to the participants {: #config_distribution}

**Option 1: Download by participants**<br> 
If the course owners configure it this way, the configuration file can be downloaded from OpenOlat by the exam participants when the assessment mode has started. 

**Option 2: Download and send by course owners**<br>
If downloading by participants is prohibited, the download option is no longer available for participants, but it remains available for authors. The course owners can download the configuration file at any time and send it to the exam participants. 
See [Step 6: Download configuration (for course owners) >](../../manual_how-to/SEB/SEB.md#download_SEB_configfile)


!!! note "Attention"

    Whenever changes are made to the configuration, a new configuration key is generated. If this is distributed to the exam participants with the configuration file, the configuration file must be redistributed each time. It is therefore not advisable to change the configuration a few minutes before the exam. 

[To the top of the page ^](#SEB_admin)

---

### Key {: #SEB_key} 

To ensure that only the correct locked-down browser is allowed to access the exam, proof is required. This proof can be provided in two ways:

**Option A – "SEB with manual keys":**<br>
Course owners manually store a key. This is a kind of password/checksum. Only those who know this key can enter the exam. 

**Option B – "SEB config (recommended)":**<br>
A configuration template can also bring the key with it. Instead of a manually stored key, a key that is contained in a ready-made configuration template is used. This is the more convenient method recommended by OpenOlat.

[See Step 7 ^](#SEB_module_events)

[To the top of the page ^](#SEB_admin)

---


### (by the course coach) Intervention while an exam with the SEB is running {: #SEB_intervention}

As a rule, no further intervention should be made while the assessment mode is running. If it is necessary for compelling reasons, however, the intervention is made via the [assessment mode](../../manual_user/learningresources/Assessment_mode.md).

[To the top of the page ^](#SEB_admin)

---


## Check list {: #SEB_checklist}

- [x] SEB downloaded from the manufacturer's website?
- [x] Assessment mode activated in e-Assessment?
- [x] Clarified whether a minimum version of the SEB should be used?
- [x] Have the desired requirements (SEB capabilities) been clarified with those responsible for the exams?
- [x] Should the configuration be done completely manually or with a template?
- [x] Can/should an unencrypted .seb file be imported as a template?
- [x] SEB configuration template created?
- [x] Link to the download (installation) of the SEB communicated to those responsible for the exams? (For forwarding to the participants)
- [x] Configuration file for distribution to participants created by the course owner?
- [x] Have all exam participants been asked to install the SEB on their computer?
- [x] If separate computers are provided for the exam: are all computers equipped with an SEB?
- [x] Is the "Events / Absences" module being used?
- [x] Has it been defined whether the Safe Exam Browser should be used with manual keys or keys in the SEB config?

[To the top of the page ^](#SEB_admin)

---


## Further information {: #further_information}

[Website of the manufacturer >](http://www.safeexambrowser.org)<br>
[How do I prepare an exam with the SEB? (for authors) >](../../manual_how-to/SEB/SEB.md)<br>
[Assessment mode >](../../manual_user/learningresources/Assessment_mode.md)<br>
[Assessment inspection > ](../../manual_user/learningresources/Assessment_inspection.md)<br>
[Assessment management (Admin) > ](../../manual_admin/administration/e-Assessment_AssessmentMgmt.md)<br>
[Assessment management by course owners and coaches > ](../../manual_user/learningresources/Assessment_Management.md)<br>
[Events and Absences module >](../../manual_admin/administration/Modules_Events_and_Absences.md)<br>
[Configuration of events and absences management in the course >](../../manual_user/learningresources/Course_Settings_Execution.md#config_event_and_absence_management)<br>

[To the top of the page ^](#SEB_admin)
