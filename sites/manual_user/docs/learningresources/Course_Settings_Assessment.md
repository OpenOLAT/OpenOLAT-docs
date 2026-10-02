# Course Settings - Tab Assessment {: #tab_assessment}

In learning path courses, the settings for the **assessment method** and the **pass** of the course are defined under `Course > Administration > Settings > Tab "Assessment"`.<br>
You can also enable the use of **evidence of achievement** and the awarding of **credit points**, **certificates**, and **badges**.<br>
The tab can be edited by everyone who may open the "Settings" menu of the course: owners of the course, learning resource managers and administrators, as well as persons with the "Course editor" right, see [Course Settings](Course_Settings.md).

You can find the options for this in the sections

[Assessment settings](#section_assessment_settings)<br>
[User rights](#section_assessment_rights)<br>
[Evidence of achievement](#section_evidence_of_achievements)<br>
[Credit points](#section_credit_points)<br>
[Certificate](#section_certificate)<br>
[Badges](#section_badges)

![Six numbered sections from the assessment method to the awarding of badges, with score, success status and evidence of achievement switched on](assets/course_settings_assessment_v4_en.png){ class="shadow lightbox" title="Assessment tab in the course settings" }

[To the top of the page ^](#tab_assessment)

---


## Section Assessment Settings {: #section_assessment_settings}

!!! info "Assessment in traditional courses"

    The following information refers to learning path courses. For conventional courses, the criteria for passing a course are set in the course editor on the top course element in the "Score" tab, and the result is displayed on the course start page.

There are the following settings for course assessments:

- **With score** (only with learning path courses) {: #evaluation_with_points}<br>
    Here you can set whether and what type of points are displayed.
    There are 3 options to choose from for course assessment with points:

    * [Sum](#evaluation_with_points_sum)
    * [Sum with weighting](#evaluation_with_points_weighting) 
    * [Average](#evaluation_with_points_average)

    ![Progress display next to the My course menu with 61 % learning progress and an additional 6 points](assets/course_settings_assessment_points_percentage_v1_de.png){ class="aside-right lightbox" }
    If [learning path courses](Learning_path_course.md) are graded with **points**, this affects whether and what type of points are displayed in addition to the percentage display in the course.

    It can be graded with points, even if they are not relevant for passing the course.

- **With levels/grading** (only with learning path courses)<br>
  If the levels/grading module is enabled, you assign a grade to the course at course level.<br> [Find out more >](#evaluation_with_grades)

- **With success status**<br>
  Here you can set when a course is considered passed. The success status is the result of the course assessment: "Passed", "Not passed" or "Undefined". In addition to a certain number of points achieved, other criteria can also lead to a "Passed".<br> [Find out more >](#evaluation_passed_failed)

[To the top of the page ^](#tab_assessment)

---

### Course assessment with points: Sum {: #evaluation_with_points_sum}

The sum of all points achieved in the course is calculated.

![Selected option Sum under Scoring with the With score toggle switched on](assets/course_settings_assessment_points_sum_v2_de.png){ class="shadow lightbox" title="Scoring in the Assessment settings section" }

[Find out more about Assessment Settings ^](#section_assessment_settings)<br>
[To the top of the page ^](#tab_assessment)

---

### Course assessment with points: Sum with weighting [:octicons-tag-16:{ title="from Release 18.2.0 (OO-7378)" }](https://track.frentix.com/issue/OO-7378) {: #evaluation_with_points_weighting}

The weighting is taken into account when calculating the sum.

![Selected option Sum with weighting under Scoring with the With score toggle switched on](assets/course_settings_assessment_points_sum_with_weighting_v2_de.png){ class="shadow lightbox" title="Scoring in the Assessment settings section" }

If there are several assessments to be completed in a course, these are sometimes included in the overall assessment of the course with different weightings. The "Sum with weighting" option for the course assessment allows you to enter a **scale factor** for the points **for assessable course elements**. The prerequisite is that these assessable course elements are taken into account in the course assessment.

In the **Overview course configuration** of the course editor, the scaling for all assessable course elements can be checked and set or edited directly if required. The "Assessable" pre-filter provides a compact view of the assessable course elements.

![Pre-filter Assessable, columns Include in course assessment and Scale factor for course assessment, below them the open input field for the factor](assets/course_setting_assessment_weighting_score_scale_factor_v2_de.png){ class="shadow lightbox" title="Overview course configuration in the course editor" }

The weighted score is displayed to coaches in the assessment form. For participants, the weighted score is visible in the performance overview of the respective assessable course element and in the evidence of achievement.

[Find out more about Assessment Settings ^](#section_assessment_settings)<br>
[To the top of the page ^](#tab_assessment)

---

### Course assessment with points: Average {: #evaluation_with_points_average}

The average of the points achieved in the assessable course elements that are included in the course assessment is calculated. Course elements without a score do not count.

![Selected option Average under Scoring with the With score toggle switched on](assets/course_settings_assessment_points_sum_average_v2_de.png){ class="shadow lightbox" title="Scoring in the Assessment settings section" }

!!! info "HighScore"

    If "With score" is switched on, the "HighScore" tab of the top course element can also be configured in the course editor, with each of the three scoring options.

[Find out more about Assessment Settings ^](#section_assessment_settings)<br>
[To the top of the page ^](#tab_assessment)

---



### Course assessment with levels/grading [:octicons-tag-16:{ title="from Release 21.0 (OO-9511)" }](https://track.frentix.com/issue/OO-9511) {: #evaluation_with_grades}

If the levels/grading module is enabled and the course is graded with a **score**, you can use the **"With levels/grading"** option to assign a grade to the course at course level. The course grade is calculated from the sum of the score of the assessable course elements (sum, weighted sum, or average, depending on the selected scoring setting) and translated into a grade via the selected **rating scale**.

The toggle can only be switched once "With score" is on and "With success status" is off. As long as one of the two conditions is missing, "With levels/grading" stays greyed out.

If "With levels/grading" is active, the rating scale also determines the **success status** of the course: the course is considered passed if the **success criterion** of the rating scale is met. The success criterion is the lowest grade or performance class of the rating scale with which a performance counts as passed. "With success status" then stays switched off and can no longer be changed. If the selected rating scale has no success criterion, the course has no success status at course level.

The grade is not assigned automatically: the "Assignment" is fixed to "Manually by coach". Course owners and authorised coaches apply the calculated grade in the [assessment tool](Assessment_tool_overview.md). So that coaches without ownership may apply it too, course owners set the "assign Levels/Grading" option in the [User rights section](#section_assessment_rights).

![Enabled setting "With levels/grading" with assignment, rating scale and success criterion, below it the switched-off toggle "With success status" with its note](assets/course_settings_assessment_grades_v1_en.png){ class="shadow lightbox" title="Levels/grading in the Assessment settings section" }

[Find out more about Assessment Settings ^](#section_assessment_settings)<br>
[To the top of the page ^](#tab_assessment)

---


### Course assessment with "Passed/Failed" {: #evaluation_passed_failed}

A learning path course can be considered passed as soon as one of the criteria is met:

* **Learning progress 100%**:<br> If all mandatory course elements have been completed and 100% is displayed, the course is automatically deemed to have been passed.
* **Rule "All relevant course elements passed"**:<br> The course is deemed to have been passed if all assessable course elements marked with a "pass/fail" have been passed, regardless of whether they are compulsory or optional course elements. To exclude individual course elements, switch off the toggle "Include in course assessment" in the configuration of the course element in the course editor.
* **Rule "A certain number of the relevant course elements passed"**:<br> Here you can define how many and which course elements must be passed for the entire course to be considered passed. However, whether a course element is included in the overall assessment must be specified directly in the course editor for the respective course element (Assessment tab).
* **Cut value reached**:<br> Here you can define how many points learners must achieve for the entire course to be considered passed. You can also check which course elements the points must come from. Whether a course element is included in the overall assessment must be specified directly in the course editor for the respective course element (Assessment tab).

![Activated pass criteria Learning progress 100%, course elements passed with the rule "A certain number of the relevant course elements passed" and cut value reached](assets/course_settings_assessment_passed_v3_de.png){ class="shadow lightbox" title="Success status in the Assessment settings section" }

!!! info "Passed criteria"

    The individual criteria are an "or" link. It is therefore sufficient if one of the criteria applies.

!!! info "Which course elements are taken into account?"

    When calculating **learning progress**, only the **mandatory** course elements count.

    When calculating "**passed**" and **points**, **mandatory and voluntary**, course elements count.


[Find out more about Assessment Settings ^](#section_assessment_settings)<br>
[To the top of the page ^](#tab_assessment)

---

## Section User rights {: #section_assessment_rights}

![Options for coaches to reset participant data, to assign levels/grading and to release the assessment](assets/course_settings_assessment_user_rights_v1_de.png){ class="lightbox" title="User rights section" }

Coaches may be permitted to...

* Set "Passed/Failed" of the course assessment manually,
* Reset participant data,
* Assign a grade and marks,
* And release the assessment to the participants. 

The option for the manual success status only appears if at least one criterion is checked under "With success status" in the [Assessment settings section](#section_assessment_settings). It can only be selected once "release assessment" is also checked.

[To the top of the page ^](#tab_assessment)

---

## Section Evidence of achievement {: #section_evidence_of_achievements}

![Enabled switch Show evidence of achievement to participants](assets/course_settings_assessment_evidence_of_achievements_v1_de.png){ class="lightbox" title="Evidence of achievement section" }

![Entry Evidence of achievement in first position in the My course menu, below it To-dos, My badges, Notes and Bookmark](assets/course_settings_assessment_evidence_of_achievements_my_cours_v1_de.png){ class="aside-right lightbox" }

If you activate the option "Show evidence of achievement to participants", the option "Evidence of achievement" appears in the course in the toolbar menu ["My course"](../learningresources/Additional_Course_Features.md) and the participants see an overview of the assessable course elements with their current assessment status.

The entry "Evidence of achievement" appears in the "My course" menu for participants as soon as this option is switched on. It also appears with the option switched off if "Issue certificate" is switched on in the [Certificate section](#section_certificate). Guests do not see the entry, and as long as an exam is running in the course in [assessment mode](Assessment_mode.md), it stays hidden.

If you deactivate this function, your participants will no longer see any evidence of achievement. The evidence of achievement is not lost, it is simply no longer displayed. If you reactivate the evidence of achievement, all current data will be available again. However, if you delete a course with existing evidence of achievement, participants will still be able to view their [evidence of achievement](../personal_menu/Evidence_of_Achievements.md). There, the action "Open course" is missing for the deleted course. [:octicons-tag-16:{ title="from Release 21.0.3 (OO-8667)" }](https://track.frentix.com/issue/OO-8667)

[To the top of the page ^](#tab_assessment)

---

## Section Credit points [:octicons-tag-16:{ title="from Release 20.1.1 (OO-8558)" }](https://track.frentix.com/issue/OO-8558) {: #section_credit_points}

![Enabled switch Issue credit points with credit point system, awarded credit points and overridden validity period](assets/course_settings_assessment_credit_points_v1_de.png){ class="lightbox" title="Credit points section" }

If "Issue credit points" is switched on, participants are automatically credited with credit points after passing the course. Various credit point systems (defined by administrators) can be selected for this purpose.

As the course owner, you determine how many credits are awarded when this course is passed.<br>
The validity period of credit points may also be limited. 

!!! note "Note"

    The awarding of credit points is also important within a certificate program.

Further information:<br>
[Activate credit points system-wide >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>

[To the top of the page ^](#tab_assessment)

---


## Section Certificate [:octicons-tag-16:{ title="from Release 10.1 (OO-1254)" }](https://track.frentix.com/issue/OO-1254) {: #section_certificate}

![Enabled switch Issue certificate with Generate PDF certificate, certificate template, optional variables, validity period and recertification](assets/course_settings_assessment_certificate_v1_de.png){ class="lightbox" title="Certificate section" }

A **PDF certificate** can be issued as confirmation of attendance at a course or completion of certain course-related activities.

[Details about certificates in a course >](../learningresources/Course_Settings_Assessment_Certificate.md)<br>

If a certificate with a limited period of validity has been issued, a **recertification process** can be activated.<br>
[Details on recertification >](../learningresources/Course_Settings_Assessment_Certificate.md#recertification)

[To the top of the page ^](#tab_assessment)

---

## Section Badges [:octicons-tag-16:{ title="from Release 18.0.0 (OO-7003)" }](https://track.frentix.com/issue/OO-7003) {: #section_badges}

![Enabled switch Award badges with the options for manual awarding by course owners and coaches](assets/course_settings_assessment_badges_v1_de.png){ class="lightbox" title="Badges section" }

To use badges in courses, they must be activated here in the "Assessment" tab of the settings. A new menu item will then appear in the course administration, and the "Badge" tab will also appear when editing course elements under "Assessment."

Course owners can always award badges manually, and coaches can also be authorized to do so if desired.


Further information about badges can be found here:<br> 
[Infos for course owners (Creation and editing of badges) >](../learningresources/OpenBadges.md)<br>
[Infos for users (Badges in "User tools") >](../personal_menu/OpenBadges.md)<br>
[Infos for OpenOlat administrators >](../../manual_admin/administration/e-Assessment_openBadges.md)

[To the top of the page ^](#tab_assessment)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[Course Settings >](Course_Settings.md)<br>
[Learning path course - Overview >](Learning_path_course.md)<br>
[Assessment tool - overview >](Assessment_tool_overview.md)<br>
[Additional Course Features >](Additional_Course_Features.md)<br>
[Assessment management: Assessment mode >](Assessment_mode.md)<br>
[Personal achievements/successes: Evidence of Achievements >](../personal_menu/Evidence_of_Achievements.md)<br>
[e-Assessment Administration: Credit points >](../../manual_admin/administration/e-Assessment_Credit_Points.md)<br>
[Course Settings - Tab Assessment: Certificates and recertification >](Course_Settings_Assessment_Certificate.md)<br>
[Badges >](OpenBadges.md)<br>
[Personal achievements/successes: Badges >](../personal_menu/OpenBadges.md)<br>
[e-Assessment Administration: OpenBadges >](../../manual_admin/administration/e-Assessment_openBadges.md)

**Further reading**<br>
[Translate points into rating or grades >](Assessment_translate_points_in_grades.md)<br>
[Learning path course - Course editor >](Learning_path_course_Course_editor.md)

[To the top of the page ^](#tab_assessment)
