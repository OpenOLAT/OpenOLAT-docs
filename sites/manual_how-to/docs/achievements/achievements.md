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

* [**Highscore**](#highscore): Participants see how their points compare with those of the others.

* Points can be converted into [**grades**](#grades) or other systems upon request.

* The [**evidence of achievement**](#evidence_of_achievements) compiles the results of a person in a course, per assessable course element, e.g., for tests taken, assignments submitted and graded, etc.

* An achieved goal in an online learning program can be rewarded with a [**badge**](#badges).

* A [**certificate**](#certificates) can be generated as a PDF file for passing a course. The criteria for passing can be set by the course owners.

* If a joint certificate is to be created for the completion of several courses, this can be done with a [**certification program**](#certificate_programs).

* As a course owner, you can award [**credit points**](#credit_points) when a course is passed. These credit points can then serve as a prerequisite for a recertification in a certification program.

* The submission of a test can be confirmed with a [**test receipt**](#test_receipt).

How points, success status, highscore, badges and certificate build on each other is shown in the section [How does the assessment flow from the course element to the course?](#assessment_flow)


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
| Automatically in assessable course elements (e.g., tests) and by coaches | Automatically or manually by coaches, based on the points earned and the rating scale of the course element | Display is activated by course owners in the settings | Automatically according to the award criteria or manually by course owners and authorized coaches | Automatically according to the award criteria or manually by system administrators in the system administration | Automatically after passing the course or manually by coaches | Automatically after passing a course, manually by administrators in the user management |


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
| By authors when creating questions and course elements | In the course editor in the course element with the option "Levels/Grading", rating systems in the system administration under `Administration > e-Assessment > Levels/Grading` | Option "Show evidence of achievement to participants" under `Course > Administration > Settings > Tab "Assessment"` | By course owners in the course editor (tab "Badges") or under `Course > Administration > Badges` | In the system administration under `Administration > e-Assessment > OpenBadges > Tab "Global badges"` | Section "Certificate" under `Course > Administration > Settings > Tab "Assessment"` | Credit point systems in the system administration under `Administration > e-Assessment > Credit points`, award per course under `Course > Administration > Settings > Tab "Assessment"` |



[PDF to download](assets/OpenOlat_Erfolge_und_Leistungen_v1_de.pdf)

[To the top of the page ^](#achievements)

---


## Points {: #points}

By default, questions in tests in OpenOlat are graded with points.
The points are then added to the total points for the course element. If there are several course elements with points in a course, OpenOlat forms the total points for the course from them: in learning path courses, depending on the setting in the "Assessment" tab of the course settings, as a sum, as a sum with weighting or as an average. In conventional courses, you define the total points in the tab "Score" of the top course element. Based on the total points for the course, a "course passed" can then be awarded, for example.

[More about points >](../../manual_user/learningresources/Course_Settings_Assessment/index.md#section_assessment_settings)<br>
[To the top of the page ^](#achievements)

---


## Highscore {: #highscore}

With a highscore, participants see how their points compare with those of the others. The playful comparison can motivate. A highscore is available for most course elements that award points, for the course element "Structure" and for the whole course.

You set up the highscore in the course editor in the tab "HighScore" of the course element: `Course > Administration > Course editor`. The tab stays grey until the course element awards points. For the highscore of the whole course, select the top course element. Its tab "HighScore" is active as soon as the course has a score: in a learning path course with "With score" under `Course > Administration > Settings > Assessment`, in a conventional course with "Score" in the tab "Score" of the top course element.

In the tab "HighScore", switch on "Show Highscore" and choose what the highscore shows: "Congratulations title", "Podium", "Histogram" and "Top results listing". With "Anonymize usernames", the highscore shows the persons anonymized instead of with their names.

OpenOlat shows the highscore of a structure and that of the whole course on the automatic overview. For this, select "Automatic overview" or "Automatic overview incl. preview" in the tab "Overview".

[More about the highscore >](../../manual_user/learningresources/Course_Elements/index.md#highscore)<br>
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
System administrators define different credit point systems ("currencies") in the system administration under `Administration > e-Assessment > Credit points`, whereby the validity period of the credit points can also be limited.

Participants can automatically be awarded credit points after passing a course. The course owners determine how many credit points are awarded in the course settings in the "Assessment" tab.

When a certification program issues a certificate, a determinable number of credit points can be deducted from the credit balance.

A prerequisite for recertification may be that a certain number of credit points have been earned beforehand.

[More about credit points >](../../manual_user/learningresources/Course_Settings_Assessment/index.md#section_credit_points)<br>
[To the top of the page ^](#achievements)

---


## Badges {: #badges}

Badges are digital learning badges that can be used to recognize individual progress.
A badge is online proof that a goal has been achieved.

There are basically three categories of badges that can be awarded:

* **Badges for a course**<br> (for passing the course or fulfilling the conditions set therein)
* **Badges for a specific course element**<br> (like course badges, with a condition for a specific course element)
* and **global badges**<br> (cross-course, can only be created by system administrators)

[More about badges >](../../manual_user/learningresources/OpenBadges.md)<br>
[To the top of the page ^](#achievements)

---


## How does the assessment flow from the course element to the course? {: #assessment_flow}

A highscore for the whole course, a badge for the passed course or a certificate require that the assessment is set up consistently from the course element up to the course. Points and success status arise in the assessable course elements and flow upwards from there: via the structure to the top course element and on to the course settings. Each level builds on the level below.

The graphic shows the four levels. If you move the mouse pointer over a level, the graphic shows the path, the settings and the functions that this level unlocks. The same information is listed below the graphic as a procedure.

<div class="oo-assessment-layers" style="max-width:820px">
<svg viewBox="0 0 820 640" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Four levels of assessment, from the assessable course elements up to the course settings">
<title>Levels of assessment in a course</title>
<style>
.oo-al-layer { cursor: help; }
.oo-al-layer:hover .oo-al-band { stroke-width: 4; }
.oo-al-layer:hover .oo-al-light { fill: #D5E8E8; }
.oo-al-link { cursor: pointer; }
.oo-al-link:hover text { text-decoration: underline; }
</style>
<defs><marker id="oo-al-arrow-en" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#126365"/></marker></defs>
<rect x="0" y="0" width="820" height="640" fill="#F3F4EF"/>
<g font-family="'Roboto', sans-serif">
<path d="M 55 592 L 55 32" fill="none" stroke="#126365" stroke-width="3" marker-end="url(#oo-al-arrow-en)"/>
<text x="34" y="312" transform="rotate(-90 34 312)" text-anchor="middle" font-size="15" font-weight="700" fill="#126365">Assessment flows upwards</text>
<path d="M 450 468 L 450 449" fill="none" stroke="#126365" stroke-width="2.5" marker-end="url(#oo-al-arrow-en)"/>
<path d="M 450 318 L 450 299" fill="none" stroke="#126365" stroke-width="2.5" marker-end="url(#oo-al-arrow-en)"/>
<path d="M 450 168 L 450 149" fill="none" stroke="#126365" stroke-width="2.5" marker-end="url(#oo-al-arrow-en)"/>
<g class="oo-al-layer">
<title>Level 4: Course settings, tab "Assessment"
Path: Course > Administration > Settings > Assessment
Set up: In a learning path course, in the section "Assessment settings", the toggle "With score" with "Sum", "Sum with weighting" or "Average", plus "With success status" with criteria such as "Learning progress 100%" or "Cut value reached". In the section "Certificate", switch on "Issue certificate", e.g. with "Automatically after passing the course". In the section "Badges", switch on the toggle "Award badges".
Unlocks: score and success status of the course, the certificate after passing, the badge criteria "Course is passed" and "Course score" and the tab "Badges" on the assessable course elements.</title>
<rect class="oo-al-band" x="100" y="20" width="700" height="125" rx="10" fill="#126365" stroke="#0B4547" stroke-width="2"/>
<circle cx="132" cy="48" r="17" fill="#FFFFFF"/>
<text x="132" y="54" text-anchor="middle" font-size="17" font-weight="700" fill="#126365">4</text>
<text x="162" y="54" font-size="17" font-weight="700" fill="#FFFFFF">Course settings, tab "Assessment"</text>
<text x="162" y="76" font-size="13" fill="#E3EFEF">Course &gt; Administration &gt; Settings &gt; Assessment</text>
<text x="162" y="102" font-size="14" fill="#FFFFFF">"With score" and "With success status" (learning path course), certificate, badges</text>
<text x="162" y="125" font-size="14" fill="#FFFFFF">Unlocks: certificate after passing, badges for the course and course elements</text>
</g>
<g class="oo-al-layer">
<title>Level 3: Top course element
Path: Course > Administration > Course editor, top entry
Set up: In the tab "HighScore", switch on "Show Highscore". The tab is active as soon as the course has a score: in a learning path course with "With score" in the course settings, in a conventional course with "Score" in the tab "Score" of this course element. In the tab "Overview", select "Automatic overview" or "Automatic overview incl. preview".
Unlocks: Participants see their score, their success status and the highscore of the course on the overview of the course.</title>
<rect class="oo-al-band oo-al-light" x="100" y="170" width="700" height="125" rx="10" fill="#E3EFEF" stroke="#126365" stroke-width="2"/>
<circle cx="132" cy="198" r="17" fill="#126365"/>
<text x="132" y="204" text-anchor="middle" font-size="17" font-weight="700" fill="#FFFFFF">3</text>
<text x="162" y="204" font-size="17" font-weight="700" fill="#2D2926">Top course element</text>
<text x="162" y="226" font-size="13" fill="#126365">Course &gt; Administration &gt; Course editor, top entry</text>
<text x="162" y="252" font-size="14" fill="#2D2926">Tab "HighScore": highscore of the course as soon as the course has a score</text>
<text x="162" y="275" font-size="14" fill="#2D2926">Tab "Overview": the automatic overview shows the score and the highscore</text>
</g>
<g class="oo-al-layer">
<title>Level 2: Course element "Structure" (optional)
Path: Course > Administration > Course editor, course element "Structure"
Set up: Nothing in a learning path course. If "With score" is switched on in the course settings, the structure adds up the points of the course elements below it with the same scoring. In a conventional course, select the course elements under "Total score of" in the tab "Score" and define the Calculation "Passed".
Unlocks: tab "HighScore" of the structure and with it a highscore for the chapter on its automatic overview.</title>
<rect class="oo-al-band" x="100" y="320" width="700" height="125" rx="10" fill="#FFFFFF" stroke="#126365" stroke-width="2" stroke-dasharray="8 5"/>
<circle cx="132" cy="348" r="17" fill="#126365"/>
<text x="132" y="354" text-anchor="middle" font-size="17" font-weight="700" fill="#FFFFFF">2</text>
<text x="162" y="354" font-size="17" font-weight="700" fill="#2D2926">Structure (optional, sums up a chapter)</text>
<text x="162" y="376" font-size="13" fill="#126365">Course &gt; Administration &gt; Course editor, course element "Structure"</text>
<text x="162" y="397" font-size="14" fill="#2D2926">Learning path course: adds up the points of the course elements below automatically</text>
<text x="162" y="417" font-size="14" fill="#2D2926">Conventional course: tab "Score" with "Total score of" and Calculation "Passed"</text>
</g>
<a class="oo-al-link" href="../../../manual_user/learningresources/Course_Element_Structure/#score"><title>Page course element "Structure", tab "Score"</title><text x="162" y="437" font-size="13" font-weight="700" fill="#126365">More about the course element "Structure" and the tab "Score" &gt;</text></a>
<g class="oo-al-layer">
<title>Level 1: Assessable course elements
Path: Course > Administration > Course editor, assessable course element
Set up: Award points or "Passed", for the course element "Assessment" for example in the tab "Assessment" with the toggle "Score granted". A test awards the points of its questions. In a learning path course, the course element counts for the course if "Include in course assessment" is switched on.
Unlocks: tab "HighScore" (grey as long as the course element awards no points), the highscore of the course element and the badge criteria "Course element passed" and "Course element score".</title>
<rect class="oo-al-band" x="100" y="470" width="700" height="125" rx="10" fill="#FFFFFF" stroke="#126365" stroke-width="2"/>
<circle cx="132" cy="498" r="17" fill="#126365"/>
<text x="132" y="504" text-anchor="middle" font-size="17" font-weight="700" fill="#FFFFFF">1</text>
<text x="162" y="504" font-size="17" font-weight="700" fill="#2D2926">Assessable course elements, e.g. Test, Task, Assessment, Checklist</text>
<text x="162" y="526" font-size="13" fill="#126365">Course &gt; Administration &gt; Course editor, assessable course element</text>
<text x="162" y="552" font-size="14" fill="#2D2926">Award points or "Passed", e.g. with the toggle "Score granted"</text>
<text x="162" y="575" font-size="14" fill="#2D2926">Unlocks: tab "HighScore", highscore and badges for the course element</text>
</g>
<text x="100" y="625" font-size="13" fill="#4A5557">Hover over a level: path, settings and unlocked functions</text>
</g>
</svg>
</div>

### Procedure {: #assessment_flow_steps}

The procedure follows the assessment from bottom to top. If a result is unexpected, check the levels in the same order.

1. **Assessable course elements**<br>
    Award points or "Passed" in the assessable course elements. You find them in the course editor: `Course > Administration > Course editor`. For the course element "Assessment", switch on "Score granted" in the tab "Assessment"; a test awards the points of its questions. In a learning path course, a course element counts for the course if "Include in course assessment" is switched on. As soon as a course element awards points, its tab "HighScore" is active. The page [Course elements at a glance](../../manual_user/learningresources/Course_Elements/index.md#assessment) shows which course elements are assessable.

2. **Structure (optional)**<br>
    A course element "Structure" sums up the assessment of a chapter. In a learning path course, it adds up the points of the course elements below it automatically as soon as the course is assessed with points (step 4). In a conventional course, select the course elements under "Total score of" in the tab "Score" of the structure and define the Calculation "Passed". If the structure has points, its tab "HighScore" is active as well. More about this: [Course Element "Structure", tab Score](../../manual_user/learningresources/Course_Element_Structure.md#score)

3. **Top course element**<br>
    The top entry in the course editor stands for the whole course. In a conventional course, you define in its tab "Score" how the course is assessed. In the tab "HighScore", you set up the [highscore](#highscore) of the course. So that participants see the score, the success status and the highscore of the course, select "Automatic overview" or "Automatic overview incl. preview" in the tab "Overview".

4. **Course settings, tab "Assessment"**<br>
    Under `Course > Administration > Settings > Assessment`, you define in a learning path course in the section "Assessment settings" how the course is assessed: "With score" as "Sum", "Sum with weighting" or "Average", and "With success status" with the criteria for passing. In the same tab, switch on "Issue certificate" in the section "Certificate", for example with "Automatically after passing the course". If system administrators have activated badges, switch on "Award badges" in the section "Badges". The course editor then shows the tab "Badges" on the assessable course elements, and you can create badges with criteria such as "Course is passed" or "Course element score". More about this: [Course Settings - Tab Assessment](../../manual_user/learningresources/Course_Settings_Assessment/index.md)

[To the top of the page ^](#achievements)

---


## Test receipt {: #test_receipt}

A test receipt is a digitally signed confirmation of a completed test attempt. It proves later what the participant submitted at what time. Authors activate it in the test settings with the option "Generate a test receipt". After finishing the test, participants can download the test receipt; with the option "Send the test receipt per mail" they also receive it by e-mail. Coaches check a test receipt in the assessment tool with "Validate test receipt".

The prerequisite is that system administrators have set up the test receipt in the system administration under `Administration > e-Assessment > Test` in the "QTI" tab.

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
- [x] Does the top course element show an automatic overview so that participants see the highscore of the course?
- [x] Should grades or other assessments/graphical symbols be awarded in addition to points?
- [x] Have the necessary rating systems been set up?
- [x] Is the evidence of achievement activated in the course administration?
- [x] Are badges generally enabled by system administrators across the entire instance?
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
[Course Settings - Tab Assessment >](../../manual_user/learningresources/Course_Settings_Assessment/index.md)<br>
[Course elements at a glance >](../../manual_user/learningresources/Course_Elements/index.md)<br>
[Levels/Grading >](../../manual_user/learningresources/Assessment_translate_points_in_grades.md)<br>
[Personal achievements/successes: Evidence of Achievements >](../../manual_user/personal_menu/Evidence_of_Achievements.md)<br>
[Course Settings - Tab Assessment: Certificates and recertification >](../../manual_user/learningresources/Course_Settings_Assessment_Certificate.md)<br>
[Course Planner: Certification programs >](../../manual_user/area_modules/Course_Planner_Certification_Programs.md)<br>
[Badges >](../../manual_user/learningresources/OpenBadges.md)<br>
[Course Element "Structure" >](../../manual_user/learningresources/Course_Element_Structure.md)<br>
[Test: Settings >](../../manual_user/learningresources/Test_settings.md)<br>
[Assessing tests >](../../manual_user/learningresources/Assessing_tests.md)<br>
[Personal menu >](../../manual_user/personal_menu/index.md)

**Further reading**<br>
[e-Assessment Administration: Levels/Grading >](../../manual_admin/administration/Assessment_translate_points_in_grades_admin.md)<br>
[How can I create certification programs with the Course Planner? >](../certification_programs/certification_programs.md)<br>
[e-Assessment Administration: OpenBadges >](../../manual_admin/administration/e-Assessment_openBadges.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview/index.md)<br>
[Assessment of learners >](../../manual_user/learningresources/Assessment_of_learners.md)<br>
[Assess tasks >](../../manual_user/learningresources/Assess_tasks.md)<br>
[Forms in Rubric Scoring >](../../manual_user/learningresources/Forms_in_Rubric_Scoring.md)<br>
[Personal achievements/successes: Certificates >](../../manual_user/personal_menu/Certificates.md)<br>
[Personal achievements/successes: Credit points >](../../manual_user/personal_menu/Credit_Points.md)

[To the top of the page ^](#achievements)
