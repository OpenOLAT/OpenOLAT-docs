#  [Release notes 15.3](Release+notes+15.3.html)

**Keywords:**  Contact Tracing -- Course element Document \-- OnlyOffice
enhancements -- Microsoft Azure Directory Login -- Office for the web --
Disadvantage compensation -- User relations in Coaching tool -- Improved
Drag&Drop -- Numerous optimizations in the area of e-assessment, user
management and authoring

  

With OpenOlat 15.3 we release our next major release. Due to the current
pandemic situation, a module "Contact Tracing" was integrated into OpenOlat in
order to identify possible contagious contacts. The implementation of the
document course module allows the integration of different types of documents
from different sources into a course. Additional extensions of the OnlyOffice
integration support the document preview (thumbnails) in OpenOlat as well as
the viewing and editing of documents on mobile devices. In addition to the
implementation of the Microsoft Azure Directory Login, the integration of
Office for the web has been updated. In the area of e-testing, there were also
some innovations and optimizations in addition to the integration of
disadvantage compensation for participants with physical or mental
disabilities. User-to-user relationships can now be called up via the coaching
tool and access to content can be controlled precisely for each relationship.
In particular, the drag & drop function for file uploads has been optimized
throughout OpenOlat. Numerous improvements can also be found in the user
administration area, in the authoring area and in other OpenOlat modules.

Overall more than 75 new features and improvements have been added to OpenOlat
since release 15.2 and many processes have been improved. Here, you can find
the most important new features and changes. In addition to these
improvements, more than 95 bugs have been fixed. The complete list of changes
for 15.2 – 15.2.8 can be found
[here](https://confluence.openolat.org/display/OO152DE/Release+Notes+15.2#ReleaseNotes15.2-ReleaseNotes-
Versionen).

![](assets/153/Features_Improvements_Labels_EN.png)

  

* * *

  

## Contact Tracing Module

With the contact tracing in OpenOlat, anonymous proofs of location can be
generated in order to reconstruct possible contagious contacts if necessary to
stem the pandemic.

The module works with the following five steps:

  * Registration of the locations (manually or via import)
  * Generation of the QR codes for the placement at the locations
  * Registration of existing OpenOlat users or guests at the locations
  * Sending an e-mail confirmation after registration
  * Export of data in case of an official request

The data is stored in OpenOlat in accordance with data protection regulations
and automatically deleted after a defined period of time.

The practical application is clearly explained in the following video of the
OOacademy (german only). For advice and support on the introduction, please
contact us at [support@openolat.com](mailto:support@openolat.com).

(German only)

  

* * *

  

## Course element "Document"

With the document course element, Office documents, PDF and also images are
directly integrated into the course.

The following can be used

  * Documents from the author area (existing learning resource)
  * Documents from the course storage folder
  * New documents that can be uploaded e.g. via drag & drop

New documents can also be converted into learning resources, for example, to
re-integrate them into other courses. Existing document learning resources can
also be used as templates by making local copies of them.

![](assets/153/Dok_KBS2_EN.png)

Office documents and PDF are displayed via the integrated Document viewer.
Text documents can be edited if the corresponding licenses are activated. The
editor then opens in a separate window.

![](assets/153/DOK_KBS_EN.png)

  

* * *

  

## OnlyOffice Application

The integration of OnlyOffice now supports the generation of thumbnails of
documents.

The editing of documents can be explicitly activated and corresponding editing
licenses can be stored. When deactivated, OnlyOffice is available as viewer /
reader.

For an improved viewing and editing of OnlyOffice documents on mobile devices,
the mobile OnlyOffice Viewer / Editor has been integrated into OpenOlat.

Documents are opened in a separate window for viewing and editing.

![](assets/153/Thumbnail_EN.png)

  

* * *

  

## Office for the web Editor

## Authentication via Microsoft Azure Directory

The integration of Microsoft Office 365 editors for Office documents is
currently being rolled out in the frentix cloud (planned by the end of 2020).

Note

For licensing reasons, the Microsoft Office 365 editors are only available in
the frentix hosting cloud!

Microsoft 365 logins are now supported in OpenOlat via Azure Active Directory.
For consulting and introduction please contact
[support@openolat.com](mailto:support@openolat.com).

![](assets/153/Azure_EN%EF%B9%96version=1&modificationDate=1604938299000&api=v2.png)

  

* * *

  

## Disadvantage compensation for online exams

For examinee with physical or mental handicap, a compensation for
disadvantages can be defined before the exam. Participants are given more time
for the test.

The compensation of disadvantages can be set via the user administration or
directly in the course in the assessment tool on the respective participant.

![](assets/153/Nachteilsausgleich_EN.png)

In the assessment tool and also in the test results the extension is
transparently shown. The test time and the test mode (in case of manual
control) are automatically extended by the disadvantage compensation.

![](assets/153/Nachteilsausgleich_Assessment_EN.png)

  

* * *

  

## Optimization in the area of e-assessment and e-testing

  * Optimized calculation of the maximum score for X from Y questions in tests
  * Display of the participants' individual test start time in the assessment tool
  * Enhancements to the correction workflow in the assessment tool (see screenshot)
    * Formatting of comments
    * File upload per user per question
  * Question pool:
    * Display of the number of selected questions in the question pool dialog
    * Additional columns in the question overview table
  * Optional anonymization in the correction tool for external graders

![](assets/153/Korrektur_EN.png)

  

* * *

  

## User relations in coaching tool

With the user-to-user relationship in OpenOlat, cross-course support functions
for mentors, learning guides and supervisors can be represented.

The coaching tool now provides easy and clear access to the coached users.

![](assets/153/Coaching_EN.png)

For each user-to-user relationship, specific rights can be defined and thus
access to explicitly released content of the coaches can be granted, e.g.
course list, calendar, absence overview, evidences of achievement and
certificates.

![](assets/153/Userbeziehung_EN.png)

  

The role of "line manager" was also mapped in the coaching tool in the same
way. Here, defined contents can also be accessed by users of the own
organizational unit.

  

* * *

  

## Additions in authoring area

  * Automatic lifecycle of courses extended by "Definitely delete" (see screenshot)
  * Filter learning resources by taxonomy

![](assets/153/Kurs%20LifeCycle_EN.png)

  

* * *

  

## Enhancements in the user administration

  * 30-day grace period for reactivated users
  * Separate handling of non-deletable users in the user life cycle
  * Import of users without authentication

  

* * *

  

## Additional notes

  * BigBlueButton innovations:
    * Integration in course element "Appointment scheduling" (see screenshot)
    * Participants' consent, if recording function for the meeting is activated
  * Optimized Drag&Drop for file upload
  * Optimization of the document preview for Word, Excel, PowerPoint and other formats
  * Improvements in drop-down menus and HTML editor display
  * Additional roles in the course when changing roles
  * Course reminders: "Learning progress" as a further condition (only for learning path course) and alphabetical sorting of the created reminders
  * Group management: new filters "Last access" and "External management"
  * Curriculum: improved membership management
  * Deactivation of reasons for lecture completion in absence management
  * LinkedIn field in user profile

![](assets/153/BBB%20Terminvergabe_EN.png)

  

* * *

  

## Technical details

  * Technical support of Java 11 and Servlet 4.0 (Tomcat 9.0 required)
  * Code maintenance after security audit with Sonarqube
  * Refactoring the configuration overview olat.local.properties in the admin area
  * Library Updates

  

* * *

  

## Release notes - versions

  * [15.3.18](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17107)
  * [15.3.17](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17105)
  * [15.3.16](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17103)
  * [15.3.15](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17100)
  * [15.3.14](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17026)
  * [15.3.13](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17025)
  * [15.3.12](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17022)
  * [15.3.11](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17020)
  * [15.3.10](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17019)
  * [15.3.9](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17016)
  * [15.3.8](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17013)
  * [15.3.7](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17010)
  * [15.3.6](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17008)
  * [15.3.5](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17007)
  * [15.3.4](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17005)
  * [15.3.3](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17002)
  * [15.3.2](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17000)
  * [15.3.1](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=16945)
  * [15.3](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=16933)

  

  1. [OpenOlat 16.1 User Manual](../OO161EN.html)
  2. [Seiten](https://confluence.openolat.org/collector/pages.action?key=OO161EN)
  3. [OpenOlat 16.1 User Manual](OpenOLAT+16.1+User+Manual.html)
  4. [Release notes](Release+notes.html)
  5. [Release notes 15.3](Release+notes+15.3.html)

Sie sind nicht angemeldet. Ihre Änderungen werden mit anonym markiert. Sie
sollten sich
[anmelden](https://confluence.openolat.org/login.action?os_destination=%2Fdisplay%2FOO161EN%2FRelease%2Bnotes%2B15.3),
wenn Sie bereits über ein Konto verfügen.

search

attachments

weblink

advanced

image-effects

image-attributes

  * Absatz
    * Absatz
    * Überschrift 1
    * Überschrift 2
    * Überschrift 3
    * Überschrift 4
    * Überschrift 5
    * Überschrift 6
    * Vorformatiert
    * Zitat

  * Fett
  * Kursiv
  * Unterstreichen
  * Farbauswahl

Weitere Farben

    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  

  * Formate

    * Durchgestrichen 
    * Tiefgestellt 
    * Hochgestellt 
    * Festbreitenschriftart 

    * Formatierung zurücksetzen 

  * Aufzählung
  * Nummerierte Liste

  * Aufgabenliste

  * Einzug verkleinern
  * Einzug vergrößern

  * Linksbündig ausrichten
  * Zentriert ausrichten
  * Rechtsbündig ausrichten

  * Seitenlayout

  * Verknüpfung

  * Tabelle

  * Einfügen

Inhalt einfügen

    * Dateien und Bilder 
    * Verknüpfung 
    * Markup 
    * Horizontale Trennlinie einfügen 
    * Aufgabenliste 
    * Datum 
    * Emoticon 
    * Sonderzeichen 
Makro einfügen

    * Benutzererwähnung 
    * Jira-Vorgang/-Filter 
    * Info 
    * Status 
    * Galerie 
    * Inhalt 

    * Andere Makros 

  * Seitenlayout
    * Kein Layout
    * Zweispaltig (einfach)
    * Zweispaltig (einfach, linke Randleiste)
    * Zweispaltig (einfach, rechte Randleiste)
    * Dreispaltig (einfach)
    * Zweispaltig
    * Zweispaltig (linke Randleiste)
    * Zweispaltig (rechte Randleiste)
    * Dreispaltig
    * Dreispaltig (Randleisten links und rechts)

  * Rückgängig
  * Wiederholen

  * Suchen/Ersetzen

  * Hilfe für Tastenkombinationen

Sie sind nicht angemeldet. Ihre Änderungen werden mit anonym markiert. Sie
sollten sich
[anmelden](https://confluence.openolat.org/login.action?os_destination=%2Fdisplay%2FOO161EN%2FRelease%2Bnotes%2B15.3),
wenn Sie bereits über ein Konto verfügen.

Diese Seite wird auch von  bearbeitet. Ihre Änderungen werden mit seinen/ihren
zusammengeführt, wenn Sie speichern.



Bearbeiten

Vorschau

Speichern

Schließen

