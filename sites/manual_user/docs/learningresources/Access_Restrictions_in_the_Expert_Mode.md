# Access Restrictions in the Expert Mode

## Introduction to Expert Rules

!!! info "Important"

    The tabs "Visibility" and "Access" only exist in conventional courses. You therefore use the expert mode only there, not in [learning path courses](Learning_path_course.md).

You want to decide who sees and opens a course element, for example only from a certain date or only a certain group. In conventional courses, you set this in the tabs "Visibility" and "Access" of the course element. There you block the course element for learners, for example, release it only for certain groups or unlock it from a certain date.

If the options of the simple mode are not enough, switch to the expert mode. There you write the rule yourself and set visibility and access exactly the way your course requires. For example, you release a course element only for certain user names, combine several conditions or work with relative dates. An example:

??? tip "Survey example"

    You want to unlock a survey only in the last week of the course and set this up today so that you do not forget it later.

    To do so, you unlock the course element "Survey" depending on the date and no longer have to take care of it during the course. In the simple mode, you enter the start and end date in the tabs "Visibility" and "Access" of the course element. If only a certain group is to see the survey, also select "Depending on group" there. This way you can, for example, use two different surveys in an online course with participants from two institutions. The prerequisite is that you have divided the participants into two groups, which you assign to the surveys.

With expert rules you also cover cases the simple mode does not handle, and you save recurring steps during the course. Like a language, expert rules follow a fixed syntax. If a rule contains a syntax error, OpenOlat reports the error. This helps above all at the beginning and without programming skills. An expert rule checks whether a certain attribute is TRUE or FALSE.

The easiest way to learn the syntax is to set up a rule in the simple mode first. To do so, create a course element, for example an "HTML page", and tick the option "Blocked for learners" in the "Access" tab.

Then click "Display expert mode". You see your first expert rule in its syntax:

    (  ( isCourseCoach(0) | isCourseAdministrator(0) ) )

The whole expression is enclosed in two pairs of brackets. You may omit the outer pair in this case. `isCourseCoach(0)` checks whether the person is a coach of the course, `isCourseAdministrator(0)` whether they have owner rights for the course. The vertical line "|" in the middle stands for the Boolean operator OR. The rule is therefore TRUE for coaches OR people with owner rights. Only they open the "HTML page".

Now replace the operator "|" with "&":

    isCourseCoach(0) & isCourseAdministrator(0)

Now only coaches who also have owner rights for the course open the course element. You can only set this rule in the expert mode.

In the same way, you try out further attributes and operators. The following sections describe the available attributes and show with examples what a rule does.

## Configuration of Expert Rules

An expert rule checks whether an attribute has a certain value. Three simple examples:

Attribute| Description| Example Expert rule
---|---|---
isGuest| accessible only for guests| isGuest(0)
isCourseCoach| visible only for coaches| isCourseCoach(0)
isUser| available only for one specific user| isUser("pmuster")

### Working with the constants "TRUE" and "FALSE"

With the constants "true" and "false" you check whether an attribute applies ("true" or "1") or does not apply ("false" or "0"). Such a value is called a Boolean value, after George Boole, the founder of Boolean algebra. It has only two states: "true" = "1" = true or "false" = "0" = false.

Example: Enabling areas for guests

A practical example is a rule for the access to a course element.

**Case 1**: Only guests are to open a course element, for example to separate areas for guests and for registered users.<br>
A person therefore gets access if the attribute "isGuest" is true for them. You can write the rule in three ways:

 `isGuest(0)` or `isGuest(0)=1` or `isGuest(0)=true`

**Case 2**: Everyone except guests is to open the course element. A person therefore gets access if the attribute "isGuest" is not true for them. You can write the rule in two ways:

 `isGuest(0)=0` or `isGuest(0)=false`

The following table lists all components from which you build expert rules.

 Functions, operators and other expert rule components

Type| Syntax| Meaning
---|---|---
 **Constants**|  _TRUE_ or _1_|  True
 | _FALSE_ or _0_|  False
 | _ANY_COURSE_|  Query should be applied to every course (only for isCourseAdministrator(), isCourseCoach(), isCourseParticipant())
 **Variable**|  _now_|  Actual time of server system
 **Functions**|  _ _date("_ [date] _")__|  Retrieve date
 | _inLearningGroup("_ [string] _")_|  Returns TRUE if the person is a member of the learning group [string].
 | _inRightGroup("_ [string] _")_|  Returns TRUE if the person is a member of the right group [string].
 | _isLearningGroupFull("_ [string] _")_|  Returns the boolean TRUE (= full) or FALSE (= not full) for the learning group indicated.
 | _isUser("_ [string] _")_|  Returns TRUE if the person has the username [string].
 | _inLearningArea("_ [string] _")_|  Returns TRUE if the person is a member of a group in the learning area [string].
 | _isGlobalAuthor(0)_|  Returns TRUE if the person has the role Author.
 | _isCourseAdministrator(0)_|  Returns TRUE if the person has owner rights for your course, for example as owner, learning resource manager or administrator.
 | _isCourseAdministrator( _ANY_COURSE_ )_| Returns TRUE if the person is owner of any course on the system (learning resource) or has the role Learning resource manager or Administrator.
 | _isCourseCoach(0)_|  Returns TRUE if the person coaches the course or a group of the course.
 | _isCourseCoach( _ANY_COURSE_ )_| Returns TRUE if the person coaches any course or a group of any course.
 | _isCourseParticipant(0)_|  Returns TRUE if the person is a participant of the course.
 | _isCourseParticipant( _ANY_COURSE_ )_| Returns TRUE if the person is entered as participant in any course.
 | _isGuest(0)_|  Returns TRUE if the person visits OpenOlat as a guest.
 | _hasAttribute("_ [AttrName] _","_ [string] _")_|  Returns TRUE if [string] corresponds to the value of the AAI attribute [AttrName] of the person. See also [General information on AAI](http://www.switch.ch/aai/); AAI attributes; [Specification of AAI attributes (pdf file)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)
 | _isInAttribute("_ [AttrName] _","_ [substring] _")_|  Returns TRUE if [substring] corresponds to part of the value of the AAI attribute [AttrName] of the person.
 | _getUserProperty("_[userPropertyname]_")_|  Returns the value of the specified user attribute. With "=" you compare this value with a fixed value.
 | _getPassed("_ [integer] _")_|  Returns the Boolean TRUE (= Passed) or FALSE (= Failed) of the course element with the specified ID
 | _getScore("_ [integer] _")_|  Returns the score of the course element with the specified ID
 |  _getMaxScore("_ [integer] _")_|  Returns the maximum achievable number of points from the course element with specified ID. For course elements without configured number of points, the function returns 0. For course elements with configured number of points, but without specification of a maximum number of points, the function returns [positive infinity](https://docs.oracle.com/javase/7/docs/api/java/lang/Double.html#POSITIVE_INFINITY).
 | _getAttempts("_ [integer] _")_|  Returns the number of completed attempts of the course element with the specified ID. Can be applied to course elements of the type _Test_ , _Self-test_ , _Questionnaire_ .
 | _getLastAttemptDate("_ [integer] _")_|  Returns the date of the last attempt of the course element with the specified ID. Applies to the same course elements as getAttempts.
 | _getInitialEnrollmentDate("_ [integer] _")_|  Returns the date on which the person enrolled for the first time via the course element _Enrolment_ with the specified ID.
 | _getRecentEnrollmentDate("_ [integer] _")_|  Returns the date on which the person last enrolled via the course element _Enrolment_ with the specified ID.
 | _getInitialCourseLaunchDate(0)_|  Returns the date on which the person opened the course for the first time.
 | _getRecentCourseLaunchDate(0)_|  Returns the date on which the person last opened the course.
 | _getPassedWithCourseId("_ [integer-1] _","_ [integer-2] _")_|  Returns the Boolean TRUE (=Passed) or FALSE (=Failed) of the course element ID=[integer-2] of the course ID=[integer-1]
 | _getScoreWithCourseId("_ [integer-1] _","_ [integer-2] _")_|  Returns the score of the course element ID=[integer-2] of the course ID=[integer-1]
 | hasUserProperty("[ _userPropertyname]", "[string]")_ | Returns TRUE if [string] corresponds to the value of the user attribute [userPropertyname] of the person.
 | hasUserProperty("[ _userPropertyname]", "[string]" , " , ")_ | Returns TRUE if [string] corresponds to a value in the multi-value field of the user attribute [userPropertyname] of the person.
 | userPropertyStartswith("[ _userPropertyname]", "[substring]")_|  Returns TRUE if the user attribute [userPropertyname] of the person starts with [substring].
 | userPropertyEndswith("[ _userPropertyname]", "[substring]")_|  Returns TRUE if the user attribute [userPropertyname] of the person ends with [substring].
 | isInUserProperty("[ _userPropertyname]", "[substring]")_|  Returns TRUE if the user attribute [userPropertyname] of the person contains [substring].
 | isNotInUserProperty("[ _userPropertyname]", "[substring]")_|  Returns TRUE if the user attribute [userPropertyname] of the person does not contain [substring].
 | hasNotUserProperty("[ _userPropertyname]", "[string]")_|  Returns TRUE if the value of the user attribute [userPropertyname] of the person does not correspond to [string].
 | hasLanguage("de")| Returns TRUE if the person has set German as the system language. For English, replace "de" with "en".
 **Units**|  _min_|  Minutes
 | _h_|  Hours
 |  _d_|  Days
 |  _w_|  Weeks
 |  _m_|  Months
 **Operators**|  =| equal
 | >| greater than
 | <| less than
 | >=| greater/equal
 | <=| less/equal
 | *| Multiplication
 | /| Division
 | +| Addition
 | -| Subtraction
 **Booleans**|  &| Logical AND
 | \|| Logical OR

### User attributes (UserProperty) {: #user_properties}

With user attributes you restrict access according to details about the person, for example name, gender, address or field of studies. The attributes usually come from the user profile. OpenOlat uses a fixed name for each attribute (see the table below). These expert rules work with user attributes:

  * getUserProperty _(" _[userPropertyname ]_")_
  * hasUserProperty("[ _userPropertyname]", " [string]")_
  * userPropertyStartswith(" [ _userPropertyname ]", "[substring]")_
  * userPropertyEndswith(" [ _userPropertyname ]", "[substring]")_
  * isInUserProperty(" [ _userPropertyname ]", "[substring]")_
  * isNotInUserProperty("[ _userPropertyname ]", "[substring]")_
  * hasNotUserProperty("[ _userPropertyname ]", "[string]")_

If an attribute contains several values (multi-value field), you enter the delimiter in the third parameter of these expert rules:

  * hasUserProperty("[ _userPropertyname]", "[string]", " , ")_
  * hasNotUserProperty("[ _userPropertyname]", "[string]", " , ")_

### Available user attributes {: #available_user_properties}

The following table shows the user attributes of OpenOlat. A rule with user attributes only works if your instance uses the attributes and they are filled in in the profiles. Which attributes your profile shows, you see in the personal menu under "Profile". If you have questions, contact the system administrators of your instance.

User data|| Contact data|| Address data| |
---|---|---|---|---|---
nickName| Username| telPrivate| Phone number private| street| Street
firstName| First name| telMobile| Phone number mobile| extendedAddress| Extra address line
lastName| Last name| telOffice| Phone number office| poBox| P.O.Box
email| E-mail address| skype| Skype ID| zipCode| Zip code
creationDateDisplayProperty| Account creation date| xing| Xing| region| Region / Canton
lastloginDateDisplayProperty| Last login| homepage| Homepage| city| City
birthDay| Date of birth ||| country| Country
gender| Gender||| countryCode| Country code
|
Organization|| Professional contact details|| Miscellaneous  ||
institutionalName| Institution| department| Department / Company | typeOfUser| Type of user
institutionalUserIdentifier| Institution identifier (registration number) | officeStreet| Address / P.O. box | rank| Service grade / employment title
| institutionalEmail| Institutional email | extendedOfficeAddress| Extended office address | socialSecurityNumber| Social security number
| orgUnit| Organizational unit / study group | officeZipCode| Office ZIP | degree| Academic degree
| studySubject| Field of studies | officeCity| Office city | position| Role / position
| graduation| Graduation year| officeCountry| Office country | userInterests| Expertise
|| | officeMobilePhone| Office mobile phone|

### Examples and combination of expert rules {: #rule_examples}

Examples on how to apply "getUserProperty":

  * Only participants of a certain field of studies are to get access:

        getUserProperty("studySubject") = "Mechanical Engineering"

Now whoever has entered the value "Mechanical Engineering" in the field "Field of studies" in their profile gets access.

  * If only participants who have entered nothing in the field "Field of studies" are to get access, the rule is:

        getUserProperty("studySubject") = ""

  * If only participants who have entered any value in the field "Field of studies" are to get access, the rule is:

        getUserProperty("studySubject") = "" = false

or

        getUserProperty("studySubject") = "" = 0

You combine several rules with operators. The two most important are:

  * AND conjunction: &
  * OR conjunction: |

If a rule mixes AND and OR conjunctions, use brackets. This way you decide yourself which conjunction applies first.

Example: The expert rule `(inLearningGroup("Participants IntensiveCourse") | isCourseCoach(0))` releases the course element for the members of the learning group "Participants IntensiveCourse" and for all coaches of the course.

The following examples show how to use the syntax.

## Examples expert mode

**Examples of expert rules in the tabs «Visibility», «Access» and «Score» (structural elements)**

 **inLearningGroup("Amateur") = 0**<br>
All participants except the members of the learning group "Amateur" see the course element.

 **((now >= date("22.07.2018 12:00")) & (now <= date("23.12.2018 18:00"))) |
inLearningGroup("Coach")**<br>
All participants see the course element between 22.07.2018 and 23.12.2018, the members of the learning group "Coach" at any time.

 **((now >= date("03.09.2018 00:00")) & (now <= date("13.10.2018 00:00")) &
inRightGroup("Assessors")) | isUser("Author")**<br>
The members of the right group "Assessors" see the course element between 03.09.2018 and 13.10.2018, the person with the user name "Author" at any time.

 **hasAttribute("swissEduPersonStudyBranch3","6200")**<br>
Only students of human medicine have access to this course element.<br>
See also:<br>
AAI attributes<br>
[Specification of AAI attributes (pdf file)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

 **hasAttribute("swissEduPersonHomeOrganization","[uzh.ch](http://uzh.ch/)")**<br>
Only students of the University of Zurich have access to this course element.<br>
See also:<br>
AAI attributes<br>
[Specification of AAI attributes (pdf file)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

 **isInAttribute("surname","Mue")**<br>
Returns TRUE if the attribute _surname_ of the person contains the letter sequence "Mue", for example for the value "Mueller" or "Muehlebacher".<br>
See also:<br>
AAI attributes<br>
[Specification of AAI attributes (pdf file)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

**isInAttribute("eduPersonEntitlement","[http://vam.uzh.ch](http://vam.uzh.ch/)")**<br>
Returns TRUE if the attribute _eduPersonEntitlement_ of the person contains the value "[http://vam.uzh.ch](http://vam.uzh.ch/)", for example also for the value "<http://vam.uzh.ch/surgery>".<br>
See also:<br>
AAI attributes<br>
[Specification of AAI attributes (pdf file)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

 **(getUserProperty("orgUnit") = "Sales")**<br>
Checks whether the value "Sales" is entered in the field "Organizational unit/study group" of the person. This is useful, for example, if OpenOlat takes over the profile data automatically from LDAP.

**(getPassed("69742969114730") | getPassed("69742969115733") |
getPassed("69742969118009")) * 10**<br>
You enter this rule in the tab "Score" of the course element "Structure" under "Processing score". The course element "Structure" shows 10 points if the person has passed one of the tests (course element IDs "69742969114730", "69742969115733" or "69742969118009"), otherwise 0 points.

**(getScore("69742969114730") + getScore("69742969115733") +
getScore("69742969118009")) >= 140 | getPassed("69978845384688")**<br>
You enter this rule in the tab "Score" of the course element "Structure" under "Passed if". The course element "Structure" shows "Passed" if the person achieves at least 140 points in the three tests together or if they have received the assessment "Passed" manually in the course element "Assessment" (ID "69978845384688").

**getAttempts("70323786958847") > 0 **<br>
Returns TRUE as soon as the person has completed the test with the specified ID once, regardless of the score.

**getLastAttemptDate("70323524635734") + 24h < now **<br>
Returns TRUE if the last test attempt was more than 24 hours ago.

**getInitialEnrollmentDate("70323786958847") <= date("26.5.2018 18:00")**<br>
Returns TRUE if the person enrolled in a group for the first time by 26 May 2018, 6 p.m., via the course element "Enrolment" with the specified ID.

**getInitialEnrollmentDate("70323786958847") + 2h > now**<br>
Returns TRUE during the first two hours after the person has enrolled in a group via the course element "Enrolment" with the specified ID. This way each person works on a script, for example, only during a fixed period of time.

**(getInitialCourseLaunchDate(0) >= never) | (getInitialCourseLaunchDate(0) +
2h > now)**<br>
Returns TRUE as long as the person has not yet opened the course, and afterwards during two hours from the first course visit. This way each person sees the content only during a fixed period of time.

**(getRecentCourseLaunchDate(0) + 10min < now) **<br>
Returns TRUE if the person last opened the course more than 10 minutes ago.

**(getCourseBeginDate(0) <= today) & (getCourseEndDate(0) >= today)**<br>
Returns TRUE if today's date lies between the start and the end of the execution period of the course.

**isAssessmentMode(0)**<br>
Returns TRUE as long as an exam is running for the person in the course.

 **hasUserProperty("email","john.doe@[openolat.org](http://openolat.org/)")**<br>
Returns TRUE if the person is registered in OpenOlat with this email address.

 **hasUserProperty("typeOfUser","staff", " , ")**<br>
Returns TRUE if the field "Type of user" of the person contains, among others, the value "staff", for example "staff, student".

 **userPropertyEndswith("email","@openolat.org")**<br>
Returns TRUE if the email address of the person ends with _@openolat.org_.

 **isInUserProperty("email","doe@openo")**<br>
Returns TRUE if the email address of the person contains the text _doe@openo_.

 **isNotInUserProperty("email","doe@openo")**<br>
Returns FALSE if the email address of the person contains the text _doe@openo_.

!!! warning "Attention"

    The course element IDs above are examples. In your course, use the ID that the tab "Title and description" of the respective course element shows.

## Use of AAI Attributes

If you work at a Swiss university or at another institution with access to an AAI infrastructure, you set access rules in the course with AAI attributes. This way only participants with certain attributes open the course material, for example only members of a certain institution. AAI stands for "Authentication and Authorization Infrastructure": with it, members of a university log in to the systems of all participating universities with a single username and password. For further information on AAI, see for example [Switch](http://www.switch.ch/aai/ "Switch") or the [Deutsches Forschungsnetz](https://www.aai.dfn.de/en/ "Deutsches Forschungsnetz").

The available attributes and values are described in the AAI Attribute Specification at [Switch](https://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf "Switch") and at [DFN-AAI](https://www.aai.dfn.de/der-dienst/attribute/ "DFN-AAI") (in German). The following table shows two attributes that Swiss universities often use, with matching expert rules:

Attribute| Description| Example Expert rule and Explication
---|---|---
swissEduPersonHomeOrganization| University or home organization| hasAttribute ("swissEduPersonHomeOrganization", "[uzh.ch](http://uzh.ch)"): only members of the Zurich University will get access.
swissEduPersonStudyBranch3| Field of study, 3rd classification| hasAttribute ("swissEduPersonStudyBranch3","6400"): only veterinary medicine students will have access.

### Utilization

You can retrieve AAI attributes by using the syntax<br>
**_hasAttribute("_ [AttrName] _","_ [string] _")_** or<br>
**_isInAttribute("_ [AttrName] _","_ [substring] _")_**.

The following applies:

* **[AttrName]** is the name of the attribute. You find it in the table below and in the Specification of AAI attributes (PDF file) on page 5, column _LDAP names_.
* **[string]** is the value of the AAI attribute with the name [AttrName].
* **[substring]** is any part of [string].

#### AAI example

_Values for John Doe_

Attribute [AttrName]| Example value [string]| Description
---|---|---
swissEduPersonUniqueID| [845938727494@uzh.ch](mailto:845938727494@uzh.ch)|Unambiguous personal identification number
surname| Doe| Last name
givenName| John| First name
mail| [john.doe@uzh.ch](mailto:john.doe@uzh.ch)| Preferred email address
swissEduPersonHomeOrganization| [uzh.ch](http://uzh.ch)| Home organisation/university
swissEduPersonHomeOrganizationType| university| Type of home organisation
eduPersonAffiliation| student| Position within this organisation
[swissEduPersonStudyBranch1](http://www.switch.ch/aai/support/documents/attributes/studybranch.html)| 4| Field of study 1st classification
[swissEduPersonStudyBranch2](http://www.switch.ch/aai/support/documents/attributes/studybranch.html)| 42 (=Natural sciences)| Field of study 2nd classification
[swissEduPersonStudyBranch3](http://www.switch.ch/aai/support/documents/attributes/studybranch.html)| 4600 (=Chemistry)| Field of study 3rd classification
swissEduPersonStudyLevel| 15| Description of study level
eduPersonEntitlement| <http://vam.uzh.ch/surgery>| Access right to resource
employeeNumber| 01-234-567| Registration number (only for students at Zurich university)
organizationalUnit| 1| Unity of home organisation e.g. faculty (only for employees)

For John Doe, the following queries return these results:

Request | Output
---|---
isInAttribute("surname","ust")|  **true**
hasAttribute("swissEduPersonStudyBranch3","4600")|  **true**
hasAttribute("swissEduPersonStudyBranch3","1200")|  **false**
isInAttribute("eduPersonEntitlement","<http://vam.uzh.ch>")|  **true**
isInAttribute("eduPersonEntitlement","<http://vam.uzh.ch/ophthalmology>")|**false**
hasAttribute("employeeNumber","01-234-567")|  **true**

The list of possible values is in the appendix of the [Specification of AAI attributes (PDF file)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf) from page 20.

For further information on attribute values or on the use of AAI attributes, contact [Switch](http://www.switch.ch/aai/ "Switch") in Switzerland and the [Deutsches Forschungsnetz](https://www.aai.dfn.de/en/ "Deutsches Forschungsnetz") in Germany.

!!! tip "Tip"

    Only use AAI attributes if all participants of your course log in via AAI. For people without an AAI login the attributes are missing, and the rule does not work as planned.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Learning path course - Overview >](Learning_path_course.md)<br>
[Specification of AAI attributes (PDF) >](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)<br>
[Switch AAI >](http://www.switch.ch/aai/)<br>
[Deutsches Forschungsnetz (DFN-AAI) >](https://www.aai.dfn.de/der-dienst/attribute/)

**Further information**<br>
[Course elements in the Course editor >](General_Configuration_of_Course_Elements.md)<br>
[Course elements at a glance >](Course_Elements.md)

[To the top of the page ^](#access-restrictions-in-the-expert-mode)
