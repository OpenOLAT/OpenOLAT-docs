# Course administration - Archiving & Reporting {: #Course_Archiving}

:octicons-tag-24: Release 19.0

## What is the course archive?

**Why is a course archive needed?**
If, for example, the results of participants have to be kept for 10 years for legal reasons, the course itself can be deleted while the participant data is kept separately in a course archive.

**What does an archive file include?**
Course archive files (**zip files**) can be created in the course administration as well as in the Authoring area, which mainly contain **Excel files** or rtf files for text formats. This lists all the results achieved by course participants in a course in tabular form. If the archiving includes other files, these are provided in subfolders within the zip file.

**Complete archive - partial archive**
Partial archives can also be created on request, e.g. if only the results of a particular course element are to be archived. course element are to be archived. (E.g. the final test and practice tests should not be included in the archive).

Such a course archive must be distinguished from the [“Export content”](../learningresources/Export_Content.md) option in the course administration.

| Course administration ><br> Export content | Course administration ><br> Course archive | Course administration ><br> Reports |
| ------------------------------------- | ------------------------------------- | -------------------------------------|
| Archive course structure and archive | Archive participant results   | Report with statistical analysis for a specific course element |
| Empty course without participant data      | pure participant data for documentation (proof)| Report Excel contains more than the participant data in the Excel of the course archive |
| for transfer to another LMS        | not re-importable     | Report for certain modules, e.g. forum |
| especially html and xml-files                | especially Excel-files                         |Course element-specific Excel files |



## Where can I find course archive files? 

In the top button line of the author area, you will find an icon with 3 dots on the far right. Below this you will find the course archive, in which all existing course archive files are listed and can be downloaded.

![course_archiving_open_v1_de.png](assets/course_archiving_open_v1_de.png){ class="shadow lightbox" }


!!! info "Note"

    Im Kursarchiv werden alle von Ihnen erstellten Archive aufgelistet. <br>Administrator:innen und Lernressourcenmanager:innen sehen unter Kursarchive auch nur die von Ihnen selbst erstellten Archive oder Kurse, in denen sie Besitzer sind. In the Course archive **management** tab, on the other hand, the archives of all authors are listed for administrators.

![course_archiving_all_v1_de.png](assets/course_archiving_all_v1_de.png){ class="shadow lightbox" }


## Create course archive

### Archive a single course

* Open the authoring area
* Select the desired course
* Click on the "**archiving and reporting**" option in the "**Administration**" area
* Then, select the button "**Create archive**" in the "Course archiving" area.

![course_archiving_create_single_v1_de.png](assets/course_archiving_create_single_v1_de.png){ class="shadow lightbox" }

![course_archiving_create_single2_v1_de.png](assets/course_archiving_create_single2_v1_de.png){ class="shadow lightbox" }


### Create a partial archive

As soon as you want to create an archive **via course administration**, you will first be asked whether it should be a complete or partial archive.

![course_archiving_create_partial_v1_de.png](assets/course_archiving_create_partial_v1_de.png){ class="shadow lightbox" }

!!! hint "Note"

    If administrators create an archive or partial archive, they can decide in the wizard whether the archive data should contain **personalized or non-personalized log files**. (Depending on data protection requirements). Archives with personalized log files are then only accessible to administrators and learning resource managers.

### Archive multiple courses in the authoring area

(Only complete archives can be created in this way).

* Open the authoring area
* Select all the courses you want to archive in the 1st column
* As soon as at least one course is selected, a button line appears above the list
* Select the “Archive course” button

![course_archiving_create_multiple_v1_de.png](assets/course_archiving_create_multiple_v1_de.png){ class="shadow lightbox" }

!!! hint "Note"

    If several archives are created with this bulk action, only complete archives can be created, not partial archives.

## Course archive management

!!! hint "Note"

    This tab is only available for administrators and learning resource managers.

All course archives are listed in the **Course archive management** tab.

* They can be preselected by further tabs
* The download option is also located under the icon with the 3 dots at the end of a line. The course archives can be downloaded here for a certain period of time (default setting 10 days).

![course_archiving_management_v1_de.png](assets/course_archiving_management_v1_de.png){ class="shadow lightbox" }

## What is archived from the individual elements?

### Questionnaire

Storage of old questionnaires. Generally no longer relevant.

### Surveys

All surveys of the course are displayed according to their integration in the course structure. The desired surveys to be archived can be selected and saved as a zip file.

### Tests

All tests and self-tests of the course are displayed. The desired elements to be archived can be selected and saved as a zip file. The individual selected tests are then stored in a separate folder in the zip file.

Archived self-tests contain anonymized user data, tests are saved on a personalized basis and contain all test results.

!!! hint "Note"

    If test results are to be saved as a PDF, this is done in the assessment tool or in the course run of the desired test course element.

    ![Test Resultate exportieren](assets/Test_Resultate_exportieren1.png)


### Course results

The *final results* of all assessment modules integrated in the course, such as tests, assessments, portfolio tasks, checklists, assignments, etc., are archived here as a zip file for all course participants. The zip file can be downloaded and saved directly, but can also be found in the course owner's private folder in OpenOlat.

The zip file contains an xlsx file with information on the course participants and any documents submitted by the participants. These documents are bundled per course element and contain subfolders with the names of the participants who have submitted documents.

Course results contain the summarized overall evaluation of a course, _not_ individual elements.


### Task and group tasks

All tasks and group tasks of the course are displayed. The desired tasks or group tasks to be archived can be selected and saved as a zip file.

The zip file then contains the individual selected tasks/group tasks, each in a separate folder. This folder then contains the results of the individual learners as well as the overall overview as an Excel file.


### Assignment of topics

All topics assigned to the course are displayed. The desired elements to be archived can be selected and saved as a zip file. The individual selected elements are then stored in a separate folder in the zip file.


### Log files

The personalized log files of course owners and the anonymized log files of course participants can be saved here for a selected period of time. Depending on the scope, the creation may take some time. You will then find the log files in your personal, private OpenOlat folder as a zip file with an Excel table.

### Forums

All forums of the course are displayed. The desired forums to be archived can be selected and saved as a zip file. In the zip file, the individual selected forums are then each in a separate folder with a DOCX file containing all the forum posts.

As of :octicons-tag-24: Release 18.0 : In addition to archiving, a report in xlsx format can also be generated for the desired forums. Each posting is noted in the report as a line entry and contains information on the creation date, last change, number of words, number of characters, etc.

### File discussion

All file discussions of the course are displayed. The desired elements to be archived can be selected and saved as a zip file.

### Participant folder

All "Participants folder" course elements are displayed. The desired elements to be archived can be selected and saved as a zip file. The zip file then contains the individual elements, each with a folder for each participant with a submission and return folder.

### Wikis

All wikis in the course are listed. The desired wikis to be archived can be selected and saved as a zip file. The zip file then contains one folder for each wiki and a folder with metadata for each saved wiki.

In the wiki, all pages and all uploaded files are packed into a ZIP file. The participant folder is saved according to the folder structure of this module.

### SCORM results

All SCORM course elements of the course are listed. The desired wikis to be archived can be selected and the results saved as a zip file.

### Checklists

All checklists for the course are listed. The desired checklists to be archived can be selected and saved as a zip file. The zip file contains a folder for each checklist. Inside is an xlsx file containing the results of the people who completed the checklists.

### Forms

All forms of the course are listed. The desired forms can be selected and saved as a zip file. The zip file contains a folder for each form. This contains an xlsx file with the form responses of the people who have completed the form.

### Video task

All of the course elements integrated in the course Video task are listed, regardless of the mode selected. The desired modules can be selected and the results saved as a zip file. The zip file contains an xlsx file with the results of the individual participants. 

### Chat history

Here the chat history can be exported as an xlsx file and also deleted.

### Bookings

The people who have booked the course are displayed here if the course has a booking method.

## More information

When you delete a course, all course data (not the course elements!) is automatically saved in your personal folder.

Further details on the recorded log files can be found in the chapter “[Recording of course activities](Record_of_Course_Activities.md)”.

By assigning rights in [Members management](Members_management.md), other persons can also be given the right to archive all data.