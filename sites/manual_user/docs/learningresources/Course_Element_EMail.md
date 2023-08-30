# Course Element "E-Mail"  {: #mail}


## Profile

Name | E-Mail
---------|----------
Icon | ![E-Mail Icon](assets/contact.png){ class=size24 }
Available since | 
Functional group | Administration and organisation
Purpose | Contact form with e-mail sending
Assessable | no
Specialty / Note |



By means of the course element "E-Mail" you provide your course participants
with the possibility to send an e-mail to pre-defined recipients.

There are two possibilities to send messages. You can either select the pre-
defined groups of recipients you want to send a message to in the tab
"Recipients" or you directly indicate your e-mail addresses. You can select
whether you wish to address owners, coaches and /or participants of either
course, groups or both.

In order to enter several addresses in the field "E-mail addresses" you have
to separate them by line breaks, i.e. each e-mail address has to be put into
one separate row.

### Distribution to owners/coaches/participants

By checking this box you
those member groups you would like to send a message. When selecting coaches
or participants, chose in a second step whether you wish to address all
members, or either course or group members. (if no box is checked, no mail is
sent).

In the fields "Subject (form)" and "Message (form)" you can optionally pre-
define default values to be edited later on by your course participants when
sending e-mails.

In the fields "Subject (form)" and "Message (form)", you can
optionally specify default values. 

 * *Subject*: If the subject is predefined, it cannot be changed by the participants. 
If the subject is left empty in the template, the participants have to define their 
own subject (mandatory field).
 * *Message*: The predefined message can be edited by the participants when sending an e-mail. 

In addition, the message / subject can be designed with the use of variables
personal and course-related.

### Use of variables

The following variables can be used in the subject and text of the e-mail:

variable | description
---|--- 
$firstname |The users first name  
$lastname | The users last name  
$fullName | The users full name  
$username | The users username  
$email | The users email adress  
$courseurl | The internet address of the course  
$coursename | The name of the course as defined in the course info page  
$coursedescription | The description of the course as defined in the course info page  
  
!!! info ""

    The user variables refer to the person who triggers and sends the e-mail via the **"Send" button**.

By means of a suitable short title for the course element "E-mail" you can
provide your course participants with information to whom they can send
messages. For privacy reasons they will not be able to see the recipients'
addresses in your e-mail form.

!!! tip "Tip"

    An element "E-mail" with similar functions, but without specific configuration, can also be found in the [toolbar](../learningresources/Using_Additional_Course_Features.md).
