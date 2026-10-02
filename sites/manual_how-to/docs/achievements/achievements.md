# How do I make successes and achievements visible? {: #achievements}

??? abstract "Objectives and content of this instruction"

    If you have already created an OpenOlat course, you should also let participants know which successes and achievements they have attained. This instruction gives you an overview of the options OpenOlat offers you for this.


??? abstract "Target group"

    [x] Authors [x] Coaches  [ ] Participants

    [x] Beginners [x] Advanced users  [ ] Experts


??? abstract "Expected previous knowledge"

    * ["How do I create my first OpenOlat course?"](../my_first_course/my_first_course.md)<br>


---

## What options are available for communicating successes and achievements to participants? {: #possibilities}

### Overview {: #overview}

* In principle, performances and test results in OpenOlat are initially evaluated with [**points**](#points) and displayed, for example, on the completed course element.

* Points can be converted into [**grades**](#grades) or other systems upon request.

* The [**evidence of achievement**](#evidence_of_achievements) compiles the results of a person in a course, per assessable course element, e.g., for tests taken, assignments submitted and graded, etc.

* An achieved goal in an online learning program can be rewarded with a [**badge**](#badges).

* A [**certificate**](#certificates) can be generated as a PDF file for passing a course. The criteria for passing can be set by the course owners.

* If a joint certificate is to be created for the completion of several courses, this can be done with a [**certification program**](#certificate_programs).

* As a course owner, you can award [**credit points**](#credit_points) when a course is passed. These credit points can then serve as a prerequisite for a recertification in a certification program.

* The submission of a test can be confirmed with a [**test receipt**](#test_receipt).


### How do points, grades, evidence of achievement, badges, certificates, and credit points differ?

**Definition**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| Basic assessment system in OpenOlat | Assessment of performance within a course, conversion of points into grades | Participants see an overview of the assessable course elements with their respective current assessment status | Digital badge within a course | Digital badge, independent of individual courses | Official attestation in PDF format | OpenOlat internal currency |

**Purpose**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| Comparison of results | Transparent assessment of performance in a course | Overview of current assessment status | Motivation, progress tracking, proof of individual course performance | Recognition of achievements that apply across courses (e.g., institutional competencies) | Formal proof of course completion or compulsory training | As a reward for learning achievements and as a prerequisite for a recertification in a certification program |

**Assigning**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ----------------- | ------------------- | -------------- | ----------- | ------------ |
| Automatically in assessable course elements (e.g., tests) and by coaches | Automatically or manually by coaches, based on the points earned and the rating scale of the course element | Display is activated by course owners in the settings | Automatically according to the award criteria or manually by course owners and authorized coaches | Automatically according to the award criteria or manually by administrators in the system administration | Automatically after passing the course or manually by coaches | Automatically after passing a course, manually by administrators in the user management |


**Content**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| Result value as a number, also with decimal places | Grade (e.g., 5.0) and points achieved according to the rating scale | Progress indicator, points, passed, certificate, certificate validity | Image, title, description, date of award, link for verification | Image, title, description, date of award, link for verification | Course name, name of the participant, date of issue, signature/logo if applicable | Credit balances, possibly in different currencies (credit point systems) |


**Form**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| Numerical value, visible e.g. after completing a test on the course element | Grade or level as a number, term or symbol, visible in the performance summary of the course element | Table describing the status in graphics, numbers, words | Digital badge with metadata and link | Digital badge with metadata and link | PDF document for download, printable | virtual credit point balance |


**Usage**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| Basic method for recording results as a basis for the podium, etc. | For participants as feedback on performance, for coaches for assessment purposes | For participants as detailed feedback | Shareable online (e.g., LinkedIn, portfolio) | Shareable online (e.g., LinkedIn, portfolio); strengthens institutional reputation | Can be used as a formal document in applications or for archiving purposes | As a reward for passing courses or as a prerequisite for a recertification |


**Usage example**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| Results of questions, added to the total score of a test and the overall score of a course | Points from tests or assignments can be automatically converted into grades (e.g., 50 points = grade 3.0) | Display option under "My course" | Participation in modules, completed assignments, gamification | Award for institutional programs, global competencies, organizational badges | Completion of a compulsory course, proof of further training | Recertification is only possible once a certain number of credit points have been earned |


**Creation/Configuration**

| Points | Grades | Evidence of achievement | Badges, course related | Global badges | Certificates | Credit points |
| -------| ----- | ------------------ | ------------------- | -------------- | ----------- | ------------ |
| By authors when creating questions and course elements | In the course editor in the course element with the option "Levels/Grading", rating systems under `Administration > e-Assessment > Levels/Grading` | Option "Show evidence of achievement to participants" under `Course > Administration > Settings > Tab "Assessment"` | By course owners in the course editor (tab "Badges") or under `Course > Administration > Badges` | Under `Administration > e-Assessment > OpenBadges > Tab "Global badges"` | Section "Certificate" under `Course > Administration > Settings > Tab "Assessment"` | Credit point systems under `Administration > e-Assessment > Credit points`, award per course under `Course > Administration > Settings > Tab "Assessment"` |



[PDF to download](assets/OpenOlat_Erfolge_und_Leistungen_v1_de.pdf)

[To the top of the page ^](#achievements)

---


## Points {: #points}

By default, questions in tests in OpenOlat are graded with points.
The points are then added to the total points for the course element. If there are several course elements with points in a course, OpenOlat forms the total points for the course from them: in learning path courses, depending on the setting in the "Assessment" tab of the course settings, as a sum, as a sum with weighting or as an average. Based on the total points for the course, a "course passed" can then be awarded, for example.

[More about points >](../../manual_user/learningresources/Course_Settings_Assessment.md#section_assessment_settings)<br>
[To the top of the page ^](#achievements)

---


## Grades {: #grades}

The final total of points can be converted into

* Grades (details are configurable, e.g., 1-6 or 6-1)
* Terms used for assessment (e.g., "very good," "good," etc., or A1, B1, etc. for language levels)
* Graphic rating (e.g., various smileys)

The rating scale can then be used in the assessment tool.

[More about grades >](../../manual_user/learningresources/Assessment_translate_points_in_grades.md)<br>
[To the top of the page ^](#achievements)

---


## Evidence of achievement {: #evidence_of_achievements}

The evidence of achievement compiles the results of a person in a course, per assessable course element with points, status and date (in tests, task elements, etc.). Participants see it in the course in the "My course" menu if the course owners have switched on the display, and all their evidence of achievement in the personal menu.

[More about evidence of achievement >](../../manual_user/personal_menu/Evidence_of_Achievements.md)<br>
[To the top of the page ^](#achievements)

---


## Certificates {: #certificates}

A certificate (PDF) can be issued for each course: automatically as soon as the course has been passed, or manually by coaches. When a course is considered passed is determined by the course owners in the course settings. Criteria for passing may include, for example, whether certain course elements have been completed or a certain number of points have been achieved.

Participants then find an issued certificate in their personal menu. All certificates can be viewed there, including those that have already expired.
A certificate can be given an expiration date and, if necessary, a recertification process can be initiated.

[More about certificates >](../../manual_user/learningresources/Course_Settings_Assessment_Certificate.md)<br>
[To the top of the page ^](#achievements)

---


## Certification programs {: #certificate_programs}

A certification program can be used to issue a certificate for attending an implementation or for attending several courses. To do this, individuals can be added to a certification program within the Course Planner (in an implementation).

[More about certification programs >](../../manual_user/area_modules/Course_Planner_Certification_Programs.md)<br>
[To the top of the page ^](#achievements)

---


## Credit points {: #credit_points}

Credit points can be regarded as a kind of currency within OpenOlat.
Administrators define different credit point systems ("currencies") in the system administration, whereby the validity period of the credit points can also be limited.

Participants can automatically be awarded credit points after passing a course. The course owners determine how many credit points are awarded in the course settings in the "Assessment" tab.

When a certification program issues a certificate, a determinable number of credit points can be deducted from the credit balance.

A prerequisite for recertification may be that a certain number of credit points have been earned beforehand.

[More about credit points >](../../manual_user/learningresources/Course_Settings_Assessment.md#section_credit_points)<br>
[To the top of the page ^](#achievements)

---


## Badges {: #badges}

Badges are digital learning badges that can be used to recognize individual progress.
A badge is online proof that a goal has been achieved.

There are basically three categories of badges that can be awarded:

* **Badges for a course**<br> (for passing the course or fulfilling the conditions set therein)
* **Badges for a specific course element**<br> (like course badges, with a condition for a specific course element)
* and **global badges**<br> (cross-course, can only be created by administrators)

[More about badges >](../../manual_user/learningresources/OpenBadges.md)<br>
[To the top of the page ^](#achievements)

---


## Test receipt {: #test_receipt}

A test receipt is a digitally signed confirmation of a completed test attempt. It proves later what the participant submitted at what time. Authors activate it in the test settings with the option "Generate a test receipt". After finishing the test, participants can download the test receipt; with the option "Send the test receipt per mail" they also receive it by e-mail. Coaches check a test receipt in the assessment tool with "Validate test receipt".

The prerequisite is that administrators have set up the test receipt in the system administration under `Administration > e-Assessment > Test` in the "QTI" tab.

[More about the test receipt >](../../manual_user/learningresources/Test_settings.md#digital_signature)<br>
[More about validating the test receipt >](../../manual_user/learningresources/Assessing_tests.md)<br>
[To the top of the page ^](#achievements)

---


## Where can participants view their achievements and accomplishments? {: #participants}

All OpenOlat users can find the evidence of achievement, certificates, badges, and credit points awarded to them in their **personal menu**.

Points earned in a course element or course are also displayed on the course elements (depending on the default settings of the course owner), for example, when clicking on a test course element that has already been completed.

(Coaches can find the achievements in the assessment tool.)

[More about the personal menu >](../../manual_user/personal_menu/index.md)<br>
[To the top of the page ^](#achievements)

---


## Checklist {: #checklist}

- [x] Were the tools for communicating results configured within the course? (Podium, etc.)
- [x] Should grades or other assessments/graphical symbols be awarded in addition to points?
- [x] Have the necessary rating systems been set up?
- [x] Is the evidence of achievement activated in the course administration?
- [x] Are badges generally enabled by administrators across the entire instance?
- [x] Has badge awarding been activated in the course?
- [x] Should a certificate be issued?
- [x] Has a certificate template been provided?
- [x] Should the certificate be issued for a single course or for multiple courses?
- [x] Are certification programs enabled?
- [x] Should credit points be available?
- [x] Has at least one credit point system been set up?
- [x] Should different credit point systems ("currencies") be available?
- [x] Were participants informed about where they can view their acquired evidence of achievement, badges, etc.?

[To the top of the page ^](#achievements)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[How do I create my first OpenOlat course? >](../my_first_course/my_first_course.md)<br>
[Course Settings - Tab Assessment >](../../manual_user/learningresources/Course_Settings_Assessment.md)<br>
[Levels/Grading >](../../manual_user/learningresources/Assessment_translate_points_in_grades.md)<br>
[Personal achievements/successes: Evidence of Achievements >](../../manual_user/personal_menu/Evidence_of_Achievements.md)<br>
[Course Settings - Tab Assessment: Certificates and recertification >](../../manual_user/learningresources/Course_Settings_Assessment_Certificate.md)<br>
[Course Planner: Certification programs >](../../manual_user/area_modules/Course_Planner_Certification_Programs.md)<br>
[Badges >](../../manual_user/learningresources/OpenBadges.md)<br>
[Test settings - Administration >](../../manual_user/learningresources/Test_settings.md)<br>
[Assessing tests >](../../manual_user/learningresources/Assessing_tests.md)<br>
[Personal menu >](../../manual_user/personal_menu/index.md)

**Further reading**<br>
[e-Assessment Administration: Levels/Grading >](../../manual_admin/administration/Assessment_translate_points_in_grades_admin.md)<br>
[How can I create certification programs with the Course Planner? >](../certification_programs/certification_programs.md)<br>
[e-Assessment Administration: OpenBadges >](../../manual_admin/administration/e-Assessment_openBadges.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Assessment of learners >](../../manual_user/learningresources/Assessment_of_learners.md)<br>
[Assess tasks >](../../manual_user/learningresources/Assess_tasks.md)<br>
[Forms in Rubric Scoring >](../../manual_user/learningresources/Forms_in_Rubric_Scoring.md)<br>
[Types of Course Elements >](../../manual_user/learningresources/Course_Elements.md)<br>
[Personal achievements/successes: Certificates >](../../manual_user/personal_menu/Certificates.md)<br>
[Personal achievements/successes: Credit points >](../../manual_user/personal_menu/Credit_Points.md)

[To the top of the page ^](#achievements)
