# Icon Map

OpenOlat maps [FontAwesome](https://fontawesome.com/) icons to its own CSS classes (`o_icon_*`).
One FA icon can correspond to multiple OO classes — each class represents its own semantic context.

!!! info "Source data"
    386 FA icons · 1045 OO classes · 8,071 references in source code (`src/main`)

## Usage

Icons are embedded as `<i>` elements with two CSS classes: `o_icon` (base) and the specific icon class:

```html
<i class="o_icon o_icon_user" aria-hidden="true"></i>
```

## Icon Mapping Table

| Icon | FA-Icon | Variant | OO CSS-Klasse | Name DE | Name EN | Vorkommen |
|------|---------|---------|---------------|---------|---------|----------:|
| :fontawesome-solid-a: | `a` | fa-solid | `o_icon_a` |  |  | 6 |
| :fontawesome-solid-address-card: | `address-card` | fa-solid | `o_icon_billing_address` |  |  | 9 |
|  |  |  | `o_icon_visiting_card` |  |  | 3 |
| :fontawesome-solid-adjust: | `adjust` | fa-solid | `o_icon_todo_status_in_progress` |  |  | 5 |
|  |  |  | `o_lectures_rollcall_warning` |  |  | 8 |
| :fontawesome-solid-align-center: | `align-center` | fa-solid | `o_icon_align_middle` |  |  | 2 |
| :fontawesome-solid-align-justify: | `align-justify` | fa-solid | `o_forum_all_flat_icon` |  |  | 3 |
|  |  |  | `o_icon_column` |  |  | 2 |
| :fontawesome-solid-align-left: | `align-left` | fa-solid | `o_icon_align_left` |  |  | 6 |
|  |  |  | `o_icon_textinput` |  |  | 2 |
|  |  |  | `o_mi_qtiessay` |  |  | 5 |
| :fontawesome-solid-align-right: | `align-right` | fa-solid | `o_forum_all_icon` |  |  | 3 |
|  |  |  | `o_icon_align_right` |  |  | 2 |
| :fontawesome-solid-ambulance: | `ambulance` | fa-solid | `o_icon_cleanup` |  |  | 3 |
| :fontawesome-solid-angle-double-down: | `angle-double-down` | fa-solid | `o_icon_modified` |  |  | 2 |
|  |  |  | `o_icon_move_down` |  |  | 39 |
|  |  |  | `o_icon_todo_priority_low` |  |  | 5 |
| :fontawesome-solid-angle-double-left: | `angle-double-left` | fa-solid | `o_icon_move_left` |  |  | 6 |
|  |  |  | `o_icon_previous_page` |  |  | 10 |
|  |  |  | `o_icon_previous_step` |  |  | 3 |
| :fontawesome-solid-angle-double-right: | `angle-double-right` | fa-solid | `o_icon_move_right` |  |  | 6 |
|  |  |  | `o_icon_next_page` |  |  | 10 |
|  |  |  | `o_icon_next_step` |  |  | 3 |
| :fontawesome-solid-angle-double-up: | `angle-double-up` | fa-solid | `o_icon_move_up` |  |  | 40 |
| :fontawesome-solid-angle-down: | `angle-down` | fa-solid | `o_icon_details_expand` |  |  | 33 |
| :fontawesome-solid-angle-up: | `angle-up` | fa-solid | `o_icon_details_collaps` |  |  | 33 |
| :fontawesome-solid-angles-right: | `angles-right` | fa-solid | `o_icon_forward` |  |  | 3 |
| :fontawesome-brands-apple: | `apple` | fa-brands | `o_icon_apple` |  |  | 5 |
| :fontawesome-solid-archive: | `archive` | fa-solid | `o_FileResource-IMSCP_icon` |  |  | 2 |
|  |  |  | `o_FileResource-SCORMCP_icon` |  |  | 3 |
|  |  |  | `o_cp_icon` |  |  | 8 |
|  |  |  | `o_scorm_icon` |  |  | 6 |
|  |  |  | `o_scorm_org` |  |  | 5 |
| :fontawesome-solid-arrow-circle-left: | `arrow-circle-left` | fa-solid | `o_icon_left` |  |  | 3 |
| :fontawesome-solid-arrow-circle-right: | `arrow-circle-right` | fa-solid | `o_icon_qual_ana_trend_arrow` |  |  | 3 |
|  |  |  | `o_icon_right` |  |  | 3 |
| :fontawesome-solid-arrow-down: | `arrow-down` | fa-solid | `o_icon_element_after` |  |  | 2 |
| :fontawesome-solid-arrow-right: | `arrow-right` | fa-solid | `o_icon_arrow_right` |  |  | 12 |
|  |  |  | `o_icon_qitem_status` |  |  | 2 |
|  |  |  | `o_membership_status_transfer` |  |  | 2 |
| :fontawesome-solid-arrow-rotate-right: | `arrow-rotate-right` | fa-solid | `o_icon_certification_certifying` |  |  | 5 |
|  |  |  | `o_icon_recertification` |  |  | 3 |
| :fontawesome-solid-arrow-up: | `arrow-up` | fa-solid | `o_icon_element_before` |  |  | 2 |
|  |  |  | `o_membership_status_parentbooking` |  |  | 2 |
| :fontawesome-solid-arrow-up-right-dots: | `arrow-up-right-dots` | fa-solid | `o_icon_progress` | Fortschritt | Progress | 5 |
| :fontawesome-solid-arrow-up-right-from-square: | `arrow-up-right-from-square` | fa-solid | `o_icon_arrow_up_right_from_square` |  |  | 13 |
| :fontawesome-solid-arrows: | `arrows` | fa-solid | `o_icon_move` | Verschieben | Move | 15 |
| :fontawesome-solid-arrows-down-to-line: | `arrows-down-to-line` | fa-solid | `o_icon_tb_select_last` |  |  | 5 |
| :fontawesome-solid-arrows-h: | `arrows-h` | fa-solid | `o_icon_eva_end_show` |  |  | 3 |
|  |  |  | `o_icon_spacer` |  |  | 5 |
| :fontawesome-solid-arrows-rotate: | `arrows-rotate` | fa-solid | `o_icon_mix` |  |  | 4 |
| :fontawesome-solid-arrows-turn-right: | `arrows-turn-right` | fa-solid | `o_icon_cns` |  |  | 5 |
|  |  |  | `o_icon_shift` |  |  | 3 |
| :fontawesome-solid-arrows-turn-to-dots: | `arrows-turn-to-dots` | fa-solid | `o_icon_assign_new_item` |  |  | 3 |
| :fontawesome-solid-arrows-up-to-line: | `arrows-up-to-line` | fa-solid | `o_icon_tb_select_first` |  |  | 5 |
| :fontawesome-solid-arrows-v: | `arrows-v` | fa-solid | `o_icon_node_up_down` |  |  | 3 |
|  |  |  | `o_icon_order` |  |  | 3 |
| :fontawesome-solid-asterisk: | `asterisk` | fa-solid | `o_ac_status_new_icon` |  |  | 6 |
|  |  |  | `o_forum_new_icon` |  |  | 5 |
|  |  |  | `o_icon_compulsory` |  |  | 4 |
|  |  |  | `o_icon_mandatory` |  |  | 12 |
|  |  |  | `o_icon_new` | Neu | New | 10 |
| :fontawesome-solid-award: | `award` | fa-solid | `o_icon_badge` | Abzeichen | Badge | 20 |
| :fontawesome-solid-backward-step: | `backward-step` | fa-solid | `o_icon_slide_backward` |  |  | 6 |
| :fontawesome-solid-ban: | `ban` | fa-solid | `o_CourseModule_icon_closed` |  |  | 7 |
|  |  |  | `o_ac_billing_address_inactive_icon` |  |  | 3 |
|  |  |  | `o_ac_offer_finished_icon` |  |  | 3 |
|  |  |  | `o_ac_offer_fully_booked_icon` |  |  | 4 |
|  |  |  | `o_forum_status_closed_icon` |  |  | 5 |
|  |  |  | `o_forum_status_opened_icon` |  |  | 5 |
|  |  |  | `o_forum_status_sticky_closed_icon` |  |  | 2 |
|  |  |  | `o_grader_inactive` |  |  | 5 |
|  |  |  | `o_icon_assessment_inspection_withdrawn` |  |  | 2 |
|  |  |  | `o_icon_ban` |  |  | 21 |
|  |  |  | `o_icon_building_status_inactive` |  |  | 2 |
|  |  |  | `o_icon_businessgroup_status_inactive` |  |  | 2 |
|  |  |  | `o_icon_cancelled` |  |  | 6 |
|  |  |  | `o_icon_certification_status_revoked` |  |  | 4 |
|  |  |  | `o_icon_check_disabled` |  |  | 6 |
|  |  |  | `o_icon_curriculum_status_finished` |  |  | 3 |
|  |  |  | `o_icon_deactivate` | Deaktivieren | Deactivate | 13 |
|  |  |  | `o_icon_identity_login_denied` |  |  | 3 |
|  |  |  | `o_icon_invitation_status_inactive` |  |  | 2 |
|  |  |  | `o_icon_proj_project_status_done` |  |  | 3 |
|  |  |  | `o_icon_qti_ended` |  |  | 4 |
|  |  |  | `o_icon_qual_ana_pres_delete` |  |  | 3 |
|  |  |  | `o_icon_qual_blacklist_add` |  |  | 3 |
|  |  |  | `o_icon_qual_gen_disabled` |  |  | 4 |
|  |  |  | `o_icon_qual_prev_blacklisted` |  |  | 3 |
|  |  |  | `o_icon_repo_status_closed` |  |  | 6 |
|  |  |  | `o_icon_status_not_ready` | Status: Nicht bereit | Status: Not Ready | 5 |
| :fontawesome-solid-bank: | `bank` | fa-solid | `o_icon_institution` |  |  | 4 |
|  |  |  | `o_icon_qpool` |  |  | 5 |
| :fontawesome-regular-bar-chart: | `bar-chart` | fa-regular | `o_icon_statistics_tool` |  |  | 12 |
| :fontawesome-solid-bars: | `bars` | fa-solid | `o_icon_menuhandel` |  |  | 5 |
|  |  |  | `o_mi_qtiorder` |  |  | 4 |
| :fontawesome-regular-bell: | `bell` | fa-regular | `o_icon_reminder` | Erinnerung | Reminder | 12 |
|  |  |  | `o_icon_todo_priority_urgent` |  |  | 5 |
| :fontawesome-solid-bold: | `bold` | fa-solid | `o_bigbluebuttonmeeting_icon` |  |  | 3 |
|  |  |  | `o_icon_bold` | Fett | Bold | 3 |
| :fontawesome-solid-bolt: | `bolt` | fa-solid | `o_icon_administrator` |  |  | 3 |
|  |  |  | `o_icon_assignment` |  |  | 12 |
|  |  |  | `o_icon_bolt` |  |  | 3 |
| :fontawesome-solid-bolt-lightning: | `bolt-lightning` | fa-solid | `o_icon_bolt_lightning` |  |  | 6 |
| :fontawesome-solid-bomb: | `bomb` | fa-solid | `o_icon_bomb` |  |  | 3 |
| :fontawesome-solid-book: | `book` | fa-solid | `o_icon_lecture` |  |  | 26 |
|  |  |  | `o_icon_manual` |  |  | 7 |
| :fontawesome-solid-book-open: | `book-open` | fa-solid | `o_icon_catalog_intern` |  |  | 10 |
| :fontawesome-solid-bookmark: | `bookmark` | fa-solid | `o_forum_marked_icon` |  |  | 3 |
|  |  |  | `o_icon_bookmark` | Lesezeichen | Bookmark | 21 |
|  |  |  | `o_icon_bookmark_add` |  |  | 21 |
|  |  |  | `o_icon_bookmark_header` |  |  | 18 |
|  |  |  | `o_icon_pool_favorits` |  |  | 3 |
|  |  |  | `o_portlet_bookmark_icon` |  |  | 2 |
| :fontawesome-solid-box-archive: | `box-archive` | fa-solid | `o_icon_certification_status_archived` |  |  | 3 |
| :fontawesome-solid-boxes-packing: | `boxes-packing` | fa-solid | `o_icon_coursearchive` |  |  | 10 |
| :fontawesome-solid-briefcase: | `briefcase` | fa-solid | `o_BinderTemplate_icon` |  |  | 2 |
|  |  |  | `o_ep_icon` |  |  | 10 |
|  |  |  | `o_icon_pf_binder` |  |  | 10 |
| :fontawesome-solid-bug: | `bug` | fa-solid | `o_icon_bug` |  |  | 3 |
|  |  |  | `o_icon_dev` |  |  | 4 |
| :fontawesome-solid-bullhorn: | `bullhorn` | fa-solid | `o_FileResource-BLOG_icon` |  |  | 4 |
|  |  |  | `o_blog_icon` |  |  | 14 |
| :fontawesome-solid-bullseye: | `bullseye` | fa-solid | `o_icon_landingpage` |  |  | 3 |
|  |  |  | `o_icon_objectives` |  |  | 4 |
|  |  |  | `o_icon_proj_milestone` |  |  | 4 |
| :fontawesome-solid-c: | `c` | fa-solid | `o_icon_c` |  |  | 3 |
| :fontawesome-solid-calculator: | `calculator` | fa-solid | `o_icon_grade_scale` |  |  | 3 |
|  |  |  | `o_mi_qtinumerical` |  |  | 4 |
| :fontawesome-regular-calendar: | `calendar` | fa-regular | `o_den_icon` |  |  | 7 |
|  |  |  | `o_icon_lifecycle_date` |  |  | 15 |
|  |  |  | `o_icon_proj_appointment` |  |  | 8 |
|  |  |  | `o_icon_qual_prev_regular` |  |  | 3 |
|  |  |  | `o_icon_timetable` | Stundenplan | Timetable | 2 |
| :fontawesome-regular-calendar-check: | `calendar-check` | fa-regular | `o_appointment_icon` |  |  | 5 |
|  |  |  | `o_icon_events` | Veranstaltungen | Events | 10 |
| :fontawesome-solid-calendar-day: | `calendar-day` | fa-solid | `o_icon_calendar_day` | Kalendertag | Calendar Day | 8 |
| :fontawesome-regular-calendar-days: | `calendar-days` | fa-regular | `o_cal_icon` |  |  | 13 |
|  |  |  | `o_calendar_icon` |  |  | 4 |
|  |  |  | `o_icon_calendar` | Kalender | Calendar | 76 |
|  |  |  | `o_portlet_cal_icon` |  |  | 2 |
| :fontawesome-solid-calendar-plus: | `calendar-plus` | fa-solid | `o_icon_qual_prev_changed` |  |  | 3 |
| :fontawesome-solid-caret-down: | `caret-down` | fa-solid | `o_icon_caret` |  |  | 49 |
|  |  |  | `o_icon_close_togglebox` |  |  | 175 |
|  |  |  | `o_icon_close_tree` |  |  | 6 |
|  |  |  | `o_icon_provider_performx` |  |  | 3 |
|  |  |  | `o_mi_qtiinlinechoice` |  |  | 5 |
| :fontawesome-solid-caret-left: | `caret-left` | fa-solid | `o_icon_previous_toolbar` |  |  | 8 |
| :fontawesome-solid-caret-right: | `caret-right` | fa-solid | `o_icon_caret_right` |  |  | 5 |
|  |  |  | `o_icon_next_toolbar` |  |  | 8 |
|  |  |  | `o_icon_open_togglebox` |  |  | 176 |
|  |  |  | `o_icon_open_tree` |  |  | 6 |
| :fontawesome-solid-cart-arrow-down: | `cart-arrow-down` | fa-solid | `o_ac_order_pre` |  |  | 3 |
| :fontawesome-solid-cart-shopping: | `cart-shopping` | fa-solid | `o_ac_offer_bookable_icon` |  |  | 6 |
| :fontawesome-brands-cc-paypal: | `cc-paypal` | fa-brands | `o_ac_paypal_icon` |  |  | 4 |
| :fontawesome-solid-certificate: | `certificate` | fa-solid | `o_icon_certificate` | Zertifikat | Certificate | 30 |
|  |  |  | `o_icon_certification_certified` |  |  | 5 |
|  |  |  | `o_portlet_eff_icon` |  |  | 2 |
| :fontawesome-solid-chalkboard-user: | `chalkboard-user` | fa-solid | `o_icon_coaching_tool` |  |  | 8 |
| :fontawesome-solid-chart-line: | `chart-line` | fa-solid | `o_icon_radar_chart` |  |  | 3 |
| :fontawesome-solid-chart-simple: | `chart-simple` | fa-solid | `o_icon_chart_simple` |  |  | 6 |
| :fontawesome-solid-check: | `check` | fa-solid | `o_ac_billing_address_active_icon` |  |  | 3 |
|  |  |  | `o_ac_status_success_icon` |  |  | 6 |
|  |  |  | `o_icon_accept` | Akzeptieren | Accept | 11 |
|  |  |  | `o_icon_addremove_add` |  |  | 3 |
|  |  |  | `o_icon_assessment_inspection_carriedout` |  |  | 2 |
|  |  |  | `o_icon_building_status_active` |  |  | 2 |
|  |  |  | `o_icon_businessgroup_status_active` |  |  | 2 |
|  |  |  | `o_icon_certification_status_active` |  |  | 2 |
|  |  |  | `o_icon_certification_status_valid` |  |  | 2 |
|  |  |  | `o_icon_check` | Häkchen | Check | 27 |
|  |  |  | `o_icon_correct_answer` |  |  | 9 |
|  |  |  | `o_icon_curriculum_status_active` |  |  | 2 |
|  |  |  | `o_icon_curriculum_status_confirmed` |  |  | 3 |
|  |  |  | `o_icon_immunity_proof_validated` |  |  | 3 |
|  |  |  | `o_icon_invitation_status_active` |  |  | 2 |
|  |  |  | `o_icon_line` |  |  | 3 |
|  |  |  | `o_icon_member_valid` |  |  | 6 |
|  |  |  | `o_icon_ms_done` |  |  | 2 |
|  |  |  | `o_icon_ok` | OK | OK | 22 |
|  |  |  | `o_icon_pf_entry_published` |  |  | 7 |
|  |  |  | `o_icon_presence` |  |  | 3 |
|  |  |  | `o_icon_progress_success` |  |  | 4 |
|  |  |  | `o_icon_proj_project_status_active` |  |  | 3 |
|  |  |  | `o_icon_qitem_finalVersion` |  |  | 4 |
|  |  |  | `o_icon_repo_status_published` |  |  | 4 |
|  |  |  | `o_icon_review_added` |  |  | 5 |
|  |  |  | `o_icon_select` |  |  | 6 |
|  |  |  | `o_icon_selected` |  |  | 4 |
|  |  |  | `o_icon_status_done` | Status: Erledigt | Status: Done | 21 |
|  |  |  | `o_icon_submit` |  |  | 9 |
|  |  |  | `o_icon_tb_edit_enrollments` |  |  | 4 |
|  |  |  | `o_membership_status_finished` | Mitglied abgeschlossen | Member Finished | 3 |
| :fontawesome-regular-check-circle: | `check-circle` | fa-regular | `o_grader_active` |  |  | 5 |
|  |  |  | `o_icon_activate` | Aktivieren | Activate | 12 |
|  |  |  | `o_icon_cns_status_done` |  |  | 3 |
|  |  |  | `o_icon_correct_response` |  |  | 4 |
|  |  |  | `o_icon_dispensation_authorized` |  |  | 5 |
|  |  |  | `o_icon_notice_authorized` |  |  | 5 |
|  |  |  | `o_icon_passed` | Bestanden | Passed | 22 |
|  |  |  | `o_icon_proj_milestone_status_achieved` |  |  | 6 |
|  |  |  | `o_icon_qti_summary_correct` |  |  | 12 |
|  |  |  | `o_icon_qual_dc_finished` |  |  | 3 |
|  |  |  | `o_icon_qual_exec_participated` |  |  | 2 |
|  |  |  | `o_icon_quiz_single_choice_correct` |  |  | 6 |
|  |  |  | `o_icon_quiz_single_choice_on` |  |  | 10 |
|  |  |  | `o_icon_radio_on` |  |  | 4 |
|  |  |  | `o_icon_rubric_sufficient` |  |  | 6 |
|  |  |  | `o_icon_tb_broker_enrollment_done` |  |  | 4 |
|  |  |  | `o_icon_tb_selection_enrolled` |  |  | 4 |
|  |  |  | `o_icon_tb_selection_selected` |  |  | 3 |
|  |  |  | `o_icon_tb_topic_held` |  |  | 3 |
|  |  |  | `o_icon_todo_status_done` |  |  | 5 |
|  |  |  | `o_icon_toggle_button_on` |  |  | 3 |
|  |  |  | `o_midpub` |  |  | 6 |
| :fontawesome-regular-check-square: | `check-square` | fa-regular | `o_cl_icon` |  |  | 7 |
|  |  |  | `o_grad_assignment_done` |  |  | 3 |
|  |  |  | `o_icon_calendar_enabled` |  |  | 2 |
|  |  |  | `o_icon_check_on` |  |  | 26 |
|  |  |  | `o_icon_checkbox_checked` |  |  | 4 |
|  |  |  | `o_icon_eva_mc` |  |  | 3 |
|  |  |  | `o_icon_pool_public` |  |  | 4 |
|  |  |  | `o_icon_quiz_multiple_choice_correct` |  |  | 6 |
|  |  |  | `o_icon_quiz_multiple_choice_on` |  |  | 6 |
|  |  |  | `o_icon_todo_task` |  |  | 27 |
|  |  |  | `o_mi_qtikprim` |  |  | 5 |
|  |  |  | `o_mi_qtimc` |  |  | 4 |
| :fontawesome-solid-chevron-circle-left: | `chevron-circle-left` | fa-solid | `o_icon_previous` | Vorherige | Previous | 13 |
| :fontawesome-solid-chevron-circle-right: | `chevron-circle-right` | fa-solid | `o_icon_next` | Nächste | Next | 13 |
| :fontawesome-solid-chevron-down: | `chevron-down` | fa-solid | `o_icon_node_after` |  |  | 3 |
|  |  |  | `o_icon_slide_down` |  |  | 6 |
| :fontawesome-solid-chevron-left: | `chevron-left` | fa-solid | `o_icon_back` | Zurück | Back | 23 |
|  |  |  | `o_icon_course_previous` |  |  | 5 |
| :fontawesome-solid-chevron-right: | `chevron-right` | fa-solid | `o_icon_course_next` |  |  | 5 |
|  |  |  | `o_icon_curriculum_status_transition` |  |  | 3 |
|  |  |  | `o_icon_start` | Starten | Start | 89 |
| :fontawesome-solid-chevron-up: | `chevron-up` | fa-solid | `o_icon_node_before` |  |  | 3 |
|  |  |  | `o_icon_slide_up` |  |  | 6 |
|  |  |  | `o_icon_top` |  |  | 4 |
| :fontawesome-solid-circle: | `circle` | fa-solid | `o_black_led` |  |  | 7 |
|  |  |  | `o_green_led` |  |  | 6 |
|  |  |  | `o_grey_led` |  |  | 5 |
|  |  |  | `o_icon_circle` |  |  | 6 |
|  |  |  | `o_icon_circle_color` |  |  | 21 |
|  |  |  | `o_icon_courseareas` |  |  | 14 |
|  |  |  | `o_icon_disabled` |  |  | 8 |
|  |  |  | `o_icon_draw_ellipse` |  |  | 3 |
|  |  |  | `o_icon_enabled` |  |  | 2 |
|  |  |  | `o_icon_inheritance_none` |  |  | 3 |
|  |  |  | `o_icon_proj_milestone_status_open` |  |  | 3 |
|  |  |  | `o_icon_provider_tocco` |  |  | 3 |
|  |  |  | `o_icon_qti_answered` |  |  | 2 |
|  |  |  | `o_icon_qti_notAnswered` |  |  | 2 |
|  |  |  | `o_icon_qti_notPresented` |  |  | 4 |
|  |  |  | `o_icon_qti_summary_notAnswered` |  |  | 6 |
|  |  |  | `o_icon_qti_summary_notPresented` |  |  | 6 |
|  |  |  | `o_icon_qual_blacklist_remove` |  |  | 9 |
|  |  |  | `o_icon_quiz_single_choice_off` |  |  | 10 |
|  |  |  | `o_icon_radio_off` |  |  | 4 |
|  |  |  | `o_icon_read` |  |  | 4 |
|  |  |  | `o_icon_status_available` | Status: Verfügbar | Status: Available | 18 |
|  |  |  | `o_icon_status_not_started` |  |  | 5 |
|  |  |  | `o_icon_tb_broker_not_started` |  |  | 3 |
|  |  |  | `o_icon_tb_strategy_max_topics` |  |  | 3 |
|  |  |  | `o_icon_tb_topics` |  |  | 7 |
|  |  |  | `o_icon_to_read` |  |  | 4 |
|  |  |  | `o_icon_todo_priority_medium` |  |  | 5 |
|  |  |  | `o_icon_todo_status_open` |  |  | 3 |
|  |  |  | `o_icon_toggle` |  |  | 4 |
|  |  |  | `o_icon_toggle_button_off` |  |  | 6 |
|  |  |  | `o_icon_videotask` |  |  | 10 |
|  |  |  | `o_lectures_absent` | Abwesend | Absent | 12 |
|  |  |  | `o_lectures_attended` | Anwesend | Attended | 8 |
|  |  |  | `o_lectures_authorized` | Entschuldigt | Authorized | 8 |
|  |  |  | `o_lectures_closed` |  |  | 3 |
|  |  |  | `o_lectures_current` |  |  | 5 |
|  |  |  | `o_lectures_dispensed` | Dispensiert | Dispensed | 8 |
|  |  |  | `o_lectures_pending` |  |  | 5 |
|  |  |  | `o_lectures_rollcall_danger` |  |  | 11 |
|  |  |  | `o_lectures_rollcall_free` |  |  | 7 |
|  |  |  | `o_lectures_rollcall_notice` |  |  | 5 |
|  |  |  | `o_lectures_rollcall_ok` |  |  | 9 |
|  |  |  | `o_projectbroker_icon` |  |  | 7 |
|  |  |  | `o_red_led` |  |  | 7 |
|  |  |  | `o_yellow_led` |  |  | 6 |
| :fontawesome-solid-circle-arrow-down: | `circle-arrow-down` | fa-solid | `o_icon_load_more` |  |  | 3 |
|  |  |  | `o_icon_proj_timeline_earlier` |  |  | 3 |
| :fontawesome-solid-circle-arrow-up: | `circle-arrow-up` | fa-solid | `o_icon_proj_timeline_later` |  |  | 3 |
| :fontawesome-solid-circle-check: | `circle-check` | fa-solid | `o_ac_order_status_payed_icon` |  |  | 4 |
|  |  |  | `o_icon_absence_authorized` |  |  | 5 |
|  |  |  | `o_icon_certification_status_certified` |  |  | 2 |
|  |  |  | `o_icon_circle_check` |  |  | 5 |
|  |  |  | `o_membership_status_active` | Mitglied aktiv | Member Active | 5 |
| :fontawesome-regular-circle-dot: | `circle-dot` | fa-regular | `o_icon_selected_dot` |  |  | 7 |
| :fontawesome-regular-circle-down: | `circle-down` | fa-regular | `o_icon_inheritance_inherited` |  |  | 4 |
|  |  |  | `o_icon_inheritance_root` |  |  | 4 |
| :fontawesome-solid-circle-exclamation: | `circle-exclamation` | fa-solid | `o_ac_offer_overbooked_icon` |  |  | 3 |
|  |  |  | `o_icon_circle_exclamation` |  |  | 5 |
|  |  |  | `o_icon_recertification_error` |  |  | 8 |
|  |  |  | `o_icon_validation_error` |  |  | 7 |
| :fontawesome-solid-circle-half-stroke: | `circle-half-stroke` | fa-solid | `o_ac_offer_almost_fully_booked_icon` |  |  | 3 |
| :fontawesome-solid-circle-info: | `circle-info` | fa-solid | `o_icon_circle_info` |  |  | 7 |
|  |  |  | `o_icon_metadata` | Metadaten | Metadata | 3 |
| :fontawesome-solid-circle-minus: | `circle-minus` | fa-solid | `o_as_mode_closed` |  |  | 3 |
|  |  |  | `o_icon_invalidate` |  |  | 9 |
|  |  |  | `o_icon_tb_selection_surplus` |  |  | 3 |
| :fontawesome-solid-circle-notch: | `circle-notch` | fa-solid | `o_icon_wait` | Warten | Wait | 3 |
| :fontawesome-solid-circle-play: | `circle-play` | fa-solid | `o_icon_cns_status_in_progress` |  |  | 3 |
|  |  |  | `o_icon_curriculum_implementation_avatar` |  |  | 3 |
|  |  |  | `o_icon_tb_broker_selection_in_progress` |  |  | 3 |
| :fontawesome-solid-circle-plus: | `circle-plus` | fa-solid | `o_ac_order_status_new_icon` |  |  | 2 |
|  |  |  | `o_icon_qitem_new` |  |  | 3 |
| :fontawesome-solid-circle-radiation: | `circle-radiation` | fa-solid | `o_icon_circle_radiation` |  |  | 3 |
| :fontawesome-solid-circle-stop: | `circle-stop` | fa-solid | `o_icon_assessment_inspection_cancelled` |  |  | 2 |
|  |  |  | `o_icon_cancel` | Abbrechen | Cancel | 9 |
| :fontawesome-solid-circle-xmark: | `circle-xmark` | fa-solid | `o_ac_order_status_canceled_icon` |  |  | 4 |
|  |  |  | `o_ac_order_status_error_icon` |  |  | 3 |
|  |  |  | `o_icon_certification_status_removed` |  |  | 2 |
|  |  |  | `o_icon_circle_xmark` |  |  | 7 |
|  |  |  | `o_icon_curriculum_status_cancelled` |  |  | 3 |
|  |  |  | `o_icon_error` | Fehler | Error | 77 |
|  |  |  | `o_icon_quiz` |  |  | 8 |
|  |  |  | `o_icon_tb_topic_not_held` |  |  | 3 |
|  |  |  | `o_membership_status_cancel` | Mitglied storniert | Member Cancelled | 3 |
|  |  |  | `o_membership_status_cancelwithfee` |  |  | 3 |
|  |  |  | `o_membership_status_declined` |  |  | 3 |
|  |  |  | `o_membership_status_removed` | Mitglied entfernt | Member Removed | 4 |
| :fontawesome-regular-clipboard: | `clipboard` | fa-regular | `o_icon_form` |  |  | 4 |
|  |  |  | `o_icon_memo` |  |  | 5 |
| :fontawesome-solid-clipboard-check: | `clipboard-check` | fa-solid | `o_icon_view_all_rubrics` |  |  | 3 |
| :fontawesome-solid-clipboard-list: | `clipboard-list` | fa-solid | `o_icon_info_list` |  |  | 4 |
|  |  |  | `o_icon_tb_enrollments` |  |  | 5 |
|  |  |  | `o_icon_tb_strategy_max_enrollments` |  |  | 3 |
|  |  |  | `o_icon_topicbroker` |  |  | 9 |
| :fontawesome-solid-clipboard-question: | `clipboard-question` | fa-solid | `o_icon_qual_prev_data_collection` |  |  | 3 |
|  |  |  | `o_icon_qual_preview` |  |  | 7 |
| :fontawesome-solid-clock: | `clock` | fa-solid | `o_ac_offer_pending_icon` |  |  | 4 |
|  |  |  | `o_ac_status_waiting_icon` |  |  | 5 |
|  |  |  | `o_as_mode_none` |  |  | 3 |
|  |  |  | `o_grader_absence` |  |  | 5 |
|  |  |  | `o_icon_absence_leave` |  |  | 4 |
|  |  |  | `o_icon_assessment_inspection_scheduled` |  |  | 4 |
|  |  |  | `o_icon_change_notifications_settings` |  |  | 3 |
|  |  |  | `o_icon_expenditure` |  |  | 5 |
|  |  |  | `o_icon_extra_time` |  |  | 30 |
|  |  |  | `o_icon_identity_pending` |  |  | 3 |
|  |  |  | `o_icon_pf_history` |  |  | 4 |
|  |  |  | `o_icon_time` | Zeit | Time | 29 |
|  |  |  | `o_icon_timelimit` |  |  | 20 |
|  |  |  | `o_icon_visitingcard.o_icon_waiting` |  |  | 2 |
|  |  |  | `o_lectures_next` |  |  | 3 |
|  |  |  | `o_lectures_rollcall_` |  |  | 4 |
|  |  |  | `o_membership_status_booking` |  |  | 4 |
| :fontawesome-solid-clock-rotate-left: | `clock-rotate-left` | fa-solid | `o_icon_certification_status_expired` |  |  | 2 |
|  |  |  | `o_icon_history` | Verlauf | History | 7 |
| :fontawesome-solid-clone: | `clone` | fa-solid | `o_icon_duplicate` | Duplizieren | Duplicate | 7 |
|  |  |  | `o_mi_qtimatch_draganddrop` |  |  | 4 |
| :fontawesome-solid-cloud: | `cloud` | fa-solid | `o_icon_onedrive` |  |  | 5 |
|  |  |  | `o_icon_provider_oauth` | OAuth | OAuth | 7 |
|  |  |  | `o_icon_provider_panther` |  |  | 3 |
| :fontawesome-solid-code: | `code` | fa-solid | `o_icon_add_html` |  |  | 2 |
|  |  |  | `o_icon_code` | Code | Code | 8 |
| :fontawesome-solid-code-branch: | `code-branch` | fa-solid | `o_icon_code_branch` |  |  | 3 |
| :fontawesome-solid-code-fork: | `code-fork` | fa-solid | `o_icon_branch` |  |  | 7 |
| :fontawesome-solid-cog: | `cog` | fa-solid | `o_icon_inspect` |  |  | 4 |
| :fontawesome-solid-coins: | `coins` | fa-solid | `o_icon_coins` |  |  | 10 |
| :fontawesome-solid-columns: | `columns` | fa-solid | `o_icon_columns` |  |  | 2 |
|  |  |  | `o_icon_container` |  |  | 4 |
| :fontawesome-regular-comment: | `comment` | fa-regular | `o_forum_message_icon` |  |  | 3 |
|  |  |  | `o_icon_chat` | Chat | Chat | 12 |
|  |  |  | `o_icon_comments_none` |  |  | 7 |
|  |  |  | `o_icon_post` | Beitrag | Post | 3 |
|  |  |  | `o_icon_status_chat` |  |  | 8 |
|  |  |  | `o_portlet_infomessages_icon` |  |  | 2 |
| :fontawesome-solid-comment-sms: | `comment-sms` | fa-solid | `o_icon_comment_sms` |  |  | 2 |
| :fontawesome-regular-comments: | `comments` | fa-regular | `o_fo_icon` |  |  | 12 |
|  |  |  | `o_forum_status_sticky_icon` |  |  | 3 |
|  |  |  | `o_forum_status_thread_icon` |  |  | 12 |
|  |  |  | `o_icon_chats` | Chats | Chats | 5 |
|  |  |  | `o_icon_comments` | Kommentare | Comments | 12 |
| :fontawesome-regular-compass: | `compass` | fa-regular | `o_icon_compass` |  |  | 3 |
| :fontawesome-solid-compass-drafting: | `compass-drafting` | fa-solid | `o_icon_courseplanner` |  |  | 4 |
| :fontawesome-solid-compress: | `compress` | fa-solid | `o_icon_compress` | Komprimieren | Compress | 3 |
|  |  |  | `o_icon_width_collapse` |  |  | 3 |
| :fontawesome-solid-copy: | `copy` | fa-solid | `o_icon_copy` | Kopieren | Copy | 54 |
|  |  |  | `o_icon_files` | Dateien | Files | 15 |
|  |  |  | `o_icon_qitem_copy` |  |  | 3 |
|  |  |  | `o_icon_replace` |  |  | 2 |
|  |  |  | `o_icon_taxonomy_templates` |  |  | 6 |
| :fontawesome-solid-copyright: | `copyright` | fa-solid | `o_icon_lic_all_rights_reserved` |  |  | 4 |
|  |  |  | `o_icon_lic_freetext` |  |  | 4 |
|  |  |  | `o_icon_lic_general` |  |  | 4 |
| :fontawesome-solid-crosshairs: | `crosshairs` | fa-solid | `o_icon_crosshairs` |  |  | 3 |
| :fontawesome-solid-cube: | `cube` | fa-solid | `o_icon_courserun` |  |  | 5 |
|  |  |  | `o_icon_curriculum_element` |  |  | 34 |
|  |  |  | `o_icon_taxonomy` | Taxonomie | Taxonomy | 10 |
| :fontawesome-solid-cubes: | `cubes` | fa-solid | `o_icon_curriculum` | Lehrplan | Curriculum | 24 |
|  |  |  | `o_icon_taxonomy_level` |  |  | 5 |
|  |  |  | `o_icon_mi_qtisection` |  |  | 10 |
|  |  |  | `o_portlet_repository_student_icon` |  |  | 2 |
|  |  |  | `o_st_icon` |  |  | 8 |
| :fontawesome-solid-cubes-stacked: | `cubes-stacked` | fa-solid | `o_icon_course_bundle` |  |  | 5 |
|  |  |  | `o_icon_resources` |  |  | 3 |
| :fontawesome-solid-database: | `database` | fa-solid | `o_icon_coursedb` |  |  | 4 |
|  |  |  | `o_icon_database` | Datenbank | Database | 4 |
|  |  |  | `o_icon_quota` | Quota | Quota | 3 |
|  |  |  | `o_icon_sharepoint_drive` |  |  | 5 |
|  |  |  | `o_mi_qpool_import` |  |  | 6 |
| :fontawesome-brands-delicious: | `delicious` | fa-brands | `o_icon_delicious` |  |  | 4 |
| :fontawesome-solid-diagram-project: | `diagram-project` | fa-solid | `o_icon_diagram_project` |  |  | 3 |
| :fontawesome-brands-digg: | `digg` | fa-brands | `o_icon_digg` |  |  | 4 |
| :fontawesome-solid-door-open: | `door-open` | fa-solid | `o_ac_openaccess_icon` |  |  | 9 |
| :fontawesome-regular-dot-circle: | `dot-circle` | fa-regular | `o_icon_eva_sc` |  |  | 5 |
|  |  |  | `o_icon_eva_sc` |  |  | 5 |
|  |  |  | `o_icon_passed_undefined` |  |  | 8 |
|  |  |  | `o_icon_status_dnd` | Status: Nicht stören | Status: Do Not Disturb | 15 |
|  |  |  | `o_mi_qtisc` |  |  | 4 |
| :fontawesome-solid-download: | `download` | fa-solid | `o_icon_archive_tool` |  |  | 7 |
|  |  |  | `o_icon_download` | Herunterladen | Download | 83 |
|  |  |  | `o_icon_eva_export` |  |  | 3 |
|  |  |  | `o_icon_qitem_export` |  |  | 3 |
|  |  |  | `o_icon_qual_ana_export` |  |  | 3 |
| :fontawesome-solid-edit: | `edit` | fa-solid | `o_icon_courseeditor` |  |  | 3 |
|  |  |  | `o_icon_edit` | Bearbeiten | Edit | 181 |
|  |  |  | `o_icon_edit_file` |  |  | 3 |
|  |  |  | `o_icon_inline_editable` |  |  | 3 |
|  |  |  | `o_icon_qual_dc_preparation` |  |  | 3 |
|  |  |  | `o_icon_readonly` |  |  | 5 |
|  |  |  | `o_icon_readwrite` |  |  | 3 |
| :fontawesome-solid-ellipsis: | `ellipsis` | fa-solid | `o_icon_breadcrumb_more` |  |  | 3 |
| :fontawesome-solid-ellipsis-h: | `ellipsis-h` | fa-solid | `o_icon_pageing` |  |  | 2 |
|  |  |  | `o_mi_qtifib` |  |  | 5 |
| :fontawesome-solid-ellipsis-v: | `ellipsis-v` | fa-solid | `o_icon_actions` |  |  | 52 |
|  |  |  | `o_icon_commands` |  |  | 13 |
| :fontawesome-regular-envelope: | `envelope` | fa-regular | `o_co_icon` |  |  | 10 |
|  |  |  | `o_icon_mail` | E-Mail | Mail | 79 |
|  |  |  | `o_icon_message` |  |  | 5 |
|  |  |  | `o_icon_send` | Senden | Send | 3 |
| :fontawesome-solid-envelope-open: | `envelope-open` | fa-solid | `o_icon_message_open` |  |  | 7 |
| :fontawesome-solid-envelope-open-text: | `envelope-open-text` | fa-solid | `o_icon_tb_notification` |  |  | 4 |
| :fontawesome-solid-envelope-square: | `envelope-square` | fa-solid | `o_icon_mailto` |  |  | 3 |
| :fontawesome-solid-eraser: | `eraser` | fa-solid | `o_icon_eraser` | Radiergummi | Eraser | 3 |
|  |  |  | `o_icon_tb_unselect` |  |  | 4 |
|  |  |  | `o_middel` |  |  | 4 |
| :fontawesome-solid-exchange: | `exchange` | fa-solid | `o_icon_qitem_convert` |  |  | 3 |
|  |  |  | `o_icon_role` |  |  | 2 |
| :fontawesome-solid-exclamation: | `exclamation` | fa-solid | `o_icon_exclamation` |  |  | 3 |
|  |  |  | `o_icon_not_available` |  |  | 6 |
|  |  |  | `o_icon_todo_priority_high` |  |  | 5 |
| :fontawesome-solid-exclamation-circle: | `exclamation-circle` | fa-solid | `o_absences_col_alert` |  |  | 3 |
|  |  |  | `o_grad_assignment_unassigned` |  |  | 5 |
|  |  |  | `o_icon_absence_unauthorized` |  |  | 5 |
|  |  |  | `o_icon_exclamation_circle` |  |  | 3 |
|  |  |  | `o_icon_info_msg` | Hinweis | Info Message | 17 |
|  |  |  | `o_icon_qti_invalid` |  |  | 4 |
|  |  |  | `o_icon_rubric_neutral` |  |  | 6 |
|  |  |  | `o_miderr` |  |  | 9 |
| :fontawesome-solid-exclamation-triangle: | `exclamation-triangle` | fa-solid | `o_ac_order_status_warning_icon` |  |  | 3 |
|  |  |  | `o_icon_dispensation_unauthorized` |  |  | 5 |
|  |  |  | `o_icon_important` |  |  | 32 |
|  |  |  | `o_icon_member_not_valid` |  |  | 6 |
|  |  |  | `o_icon_notice_unauthorized` |  |  | 5 |
|  |  |  | `o_icon_warn` | Warnung | Warning | 79 |
|  |  |  | `o_icon_warning` | Warnung | Warning | 12 |
|  |  |  | `o_midwarn` |  |  | 14 |
| :fontawesome-solid-expand: | `expand` | fa-solid | `o_icon_expand` | Erweitern | Expand | 3 |
|  |  |  | `o_icon_width_expand` |  |  | 3 |
| :fontawesome-solid-external-link: | `external-link` | fa-solid | `o_FileResource-SHAREDFOLDER` |  |  | 2 |
|  |  |  | `o_icon_content_popup` |  |  | 11 |
|  |  |  | `o_icon_external_link` | Externer Link | External Link | 29 |
|  |  |  | `o_icon_link_extern` | Externer Link | External Link | 13 |
|  |  |  | `o_tu_icon` |  |  | 6 |
| :fontawesome-solid-eye: | `eye` | fa-solid | `o_ac_offer_active_icon` |  |  | 5 |
|  |  |  | `o_forum_one_icon` |  |  | 3 |
|  |  |  | `o_forum_status_visible_icon` |  |  | 5 |
|  |  |  | `o_icon_curriculum_manager` |  |  | 3 |
|  |  |  | `o_icon_eye` |  |  | 11 |
|  |  |  | `o_icon_master_coach` |  |  | 3 |
|  |  |  | `o_icon_preview` | Vorschau | Preview | 54 |
|  |  |  | `o_icon_principal` |  |  | 3 |
|  |  |  | `o_icon_qti_review` |  |  | 4 |
|  |  |  | `o_icon_quickview` |  |  | 5 |
|  |  |  | `o_icon_results_visible` |  |  | 20 |
| :fontawesome-solid-eye-slash: | `eye-slash` | fa-solid | `o_ac_offer_inactive_icon` |  |  | 5 |
|  |  |  | `o_ac_offer_not_available_icon` |  |  | 3 |
|  |  |  | `o_forum_status_hidden_icon` |  |  | 5 |
|  |  |  | `o_icon_eye_slash` |  |  | 3 |
|  |  |  | `o_icon_pf_section_draft` |  |  | 6 |
|  |  |  | `o_icon_qti_reviewInvalid` |  |  | 4 |
|  |  |  | `o_icon_results_hidden` |  |  | 26 |
| :fontawesome-solid-face-frown-open: | `face-frown-open` | fa-solid | `o_icon_qti_incorrect` |  |  | 4 |
| :fontawesome-solid-face-smile-beam: | `face-smile-beam` | fa-solid | `o_icon_qti_correct` |  |  | 4 |
| :fontawesome-brands-facebook: | `facebook` | fa-brands | `o_icon_provider_facebook` | Facebook | Facebook | 6 |
| :fontawesome-brands-facebook-square: | `facebook-square` | fa-brands | `o_icon_facebook` | Facebook | Facebook | 5 |
| :fontawesome-solid-feather-pointed: | `feather-pointed` | fa-solid | `o_icon_authoring` |  |  | 4 |
| :fontawesome-regular-file: | `file` | fa-regular | `o_FileResource-FILE_icon` |  |  | 2 |
|  |  |  | `o_dialog_icon` |  |  | 14 |
|  |  |  | `o_filetype_dwb` |  |  | 2 |
|  |  |  | `o_filetype_ico` |  |  | 3 |
|  |  |  | `o_icon_file` | Datei | File | 5 |
|  |  |  | `o_icon_fileupload` |  |  | 3 |
|  |  |  | `o_icon_inspection` |  |  | 10 |
|  |  |  | `o_icon_pf_entry` |  |  | 5 |
|  |  |  | `o_icon_pf_page` |  |  | 10 |
|  |  |  | `o_icon_proj_file` |  |  | 7 |
|  |  |  | `o_scorm_item` |  |  | 5 |
| :fontawesome-regular-file-archive: | `file-archive` | fa-regular | `o_filetype_tgz` |  |  | 3 |
| :fontawesome-solid-file-arrow-up: | `file-arrow-up` | fa-solid | `o_icon_file_arrow_up` |  |  | 3 |
| :fontawesome-regular-file-audio: | `file-audio` | fa-regular | `o_FileResource-SOUND_icon` |  |  | 2 |
|  |  |  | `o_filetype_wav` | Audio-Datei | Audio File | 3 |
| :fontawesome-solid-file-circle-plus: | `file-circle-plus` | fa-solid | `o_icon_filehub_add` |  |  | 8 |
| :fontawesome-solid-file-circle-xmark: | `file-circle-xmark` | fa-solid | `o_ac_order_status_written_off_icon` |  |  | 5 |
| :fontawesome-regular-file-code: | `file-code` | fa-regular | `o_filetype_sh` | Shell-Skript | Shell Script | 2 |
|  |  |  | `o_filetype_xsl` |  |  | 3 |
|  |  |  | `o_icon_qti_signature` |  |  | 3 |
|  |  |  | `o_icon_translation_item` |  |  | 6 |
| :fontawesome-regular-file-excel: | `file-excel` | fa-regular | `o_FileResource-XLS_icon` |  |  | 4 |
|  |  |  | `o_filetype_xlsx` | Excel-Datei | Excel File | 6 |
| :fontawesome-solid-file-export: | `file-export` | fa-solid | `o_icon_file_export` |  |  | 3 |
| :fontawesome-regular-file-image: | `file-image` | fa-regular | `o_FileResource-IMAGE_icon` |  |  | 2 |
|  |  |  | `o_filetype_jpg` | JPG-Bild | JPG Image | 4 |
|  |  |  | `o_icon_layout` |  |  | 3 |
| :fontawesome-solid-file-lines: | `file-lines` | fa-solid | `o_icon_courselog` |  |  | 5 |
|  |  |  | `o_icon_file_lines` |  |  | 3 |
| :fontawesome-regular-file-pdf: | `file-pdf` | fa-regular | `o_FileResource-PDF_icon` |  |  | 2 |
|  |  |  | `o_filetype_pdf` | PDF-Datei | PDF File | 41 |
|  |  |  | `o_icon_eva_pdf` |  |  | 4 |
|  |  |  | `o_icon_qual_ana_pdf` |  |  | 3 |
|  |  |  | `o_icon_tool_pdf` |  |  | 5 |
| :fontawesome-regular-file-powerpoint: | `file-powerpoint` | fa-regular | `o_FileResource-PPT_icon` |  |  | 4 |
|  |  |  | `o_filetype_pptx` | PowerPoint-Datei | PowerPoint File | 3 |
| :fontawesome-regular-file-text: | `file-text` | fa-regular | `o_cp_item` |  |  | 5 |
|  |  |  | `o_filetype_html` | HTML-Datei | HTML File | 10 |
|  |  |  | `o_icon_log` |  |  | 14 |
|  |  |  | `o_icon_new_document` |  |  | 3 |
|  |  |  | `o_page_icon` |  |  | 10 |
|  |  |  | `o_sp_icon` |  |  | 8 |
| :fontawesome-regular-file-video: | `file-video` | fa-regular | `o_FileResource-ANIM_icon` |  |  | 2 |
|  |  |  | `o_FileResource-MOVIE_icon` |  |  | 4 |
|  |  |  | `o_filetype_flv` |  |  | 2 |
| :fontawesome-regular-file-word: | `file-word` | fa-regular | `o_FileResource-DOC_icon` |  |  | 4 |
|  |  |  | `o_filetype_docx` | Word-Datei | Word File | 3 |
| :fontawesome-solid-film: | `film` | fa-solid | `o_FileResource-VIDEO_icon` |  |  | 3 |
|  |  |  | `o_icon_video` | Video | Video | 22 |
|  |  |  | `o_video_icon` |  |  | 8 |
| :fontawesome-solid-filter: | `filter` | fa-solid | `o_icon_filter` | Filtern | Filter | 5 |
| :fontawesome-solid-fire: | `fire` | fa-solid | `o_icon_fire` |  |  | 3 |
|  |  |  | `o_mi_qtihottext` |  |  | 4 |
| :fontawesome-solid-flag-checkered: | `flag-checkered` | fa-solid | `o_icon_finished` |  |  | 3 |
| :fontawesome-solid-flask: | `flask` | fa-solid | `o_icon_banned` |  |  | 5 |
|  |  |  | `o_icon_flask` |  |  | 3 |
| :fontawesome-regular-floppy-disk: | `floppy-disk` | fa-regular | `o_icon_qti_end_testpart` |  |  | 3 |
| :fontawesome-solid-folder: | `folder` | fa-solid | `o_filetype_folder` | Ordner | Folder | 20 |
|  |  |  | `o_icon_catalog_sub` |  |  | 5 |
|  |  |  | `o_icon_coursefolder` | Kursordner | Course Folder | 6 |
| :fontawesome-regular-folder-open: | `folder-open` | fa-regular | `o_FileResource-SHAREDFOLDER_icon` |  |  | 5 |
|  |  |  | `o_bc_icon` |  |  | 10 |
|  |  |  | `o_icon_mediacenter` |  |  | 4 |
|  |  |  | `o_icon_taxonomy_level_leaf` |  |  | 3 |
|  |  |  | `o_icon_translation_package` |  |  | 5 |
| :fontawesome-solid-folder-plus: | `folder-plus` | fa-solid | `o_icon_new_folder` | Neuer Ordner | New Folder | 5 |
| :fontawesome-solid-font: | `font` | fa-solid | `o_icon_text` | Text | Text | 4 |
| :fontawesome-solid-forward-step: | `forward-step` | fa-solid | `o_icon_slide_forward` |  |  | 6 |
| :fontawesome-solid-gauge: | `gauge` | fa-solid | `o_icon_reviews` |  |  | 4 |
| :fontawesome-solid-gavel: | `gavel` | fa-solid | `o_icon_proj_decision` |  |  | 8 |
| :fontawesome-solid-gear: | `gear` | fa-solid | `o_icon_customize` |  |  | 6 |
|  |  |  | `o_icon_edit_metadata` |  |  | 7 |
|  |  |  | `o_icon_gear` |  |  | 4 |
|  |  |  | `o_icon_tb_configuration` |  |  | 3 |
|  |  |  | `o_icon_tool` |  |  | 3 |
| :fontawesome-solid-gears: | `gears` | fa-solid | `o_icon_qitem_commands` |  |  | 3 |
|  |  |  | `o_icon_settings` | Einstellungen | Settings | 8 |
|  |  |  | `o_icon_tb_method_auto` |  |  | 3 |
|  |  |  | `o_icon_tb_strategy` |  |  | 4 |
|  |  |  | `o_icon_tb_strategy_custom` |  |  | 3 |
| :fontawesome-solid-gift: | `gift` | fa-solid | `o_ac_free_icon` |  |  | 3 |
| :fontawesome-solid-globe: | `globe` | fa-solid | `o_FileResource-WIKI_icon` |  |  | 2 |
|  |  |  | `o_icon_catalog_extern` |  |  | 11 |
|  |  |  | `o_icon_globe` | Globus | Globe | 4 |
|  |  |  | `o_icon_language` | Sprache | Language | 10 |
|  |  |  | `o_icon_origin` |  |  | 5 |
|  |  |  | `o_wiki_icon` |  |  | 12 |
| :fontawesome-brands-google: | `google` | fa-brands | `o_icon_provider_google` | Google | Google | 6 |
| :fontawesome-brands-google-plus-square: | `google-plus-square` | fa-brands | `o_icon_google` |  |  | 4 |
| :fontawesome-solid-graduation-cap: | `graduation-cap` | fa-solid | `o_FileResource-GLOSSARY_icon` |  |  | 5 |
|  |  |  | `o_icon_coach` | Betreuer | Coach | 11 |
|  |  |  | `o_icon_graduate` |  |  | 3 |
|  |  |  | `o_icon_repo_status_coachpublished` |  |  | 2 |
|  |  |  | `o_icon_user_vip` |  |  | 7 |
|  |  |  | `o_portlet_repository_teacher_icon` |  |  | 2 |
| :fontawesome-regular-hand: | `hand` | fa-regular | `o_icon_abstain` |  |  | 5 |
| :fontawesome-solid-hand-back-fist: | `hand-back-fist` | fa-solid | `o_icon_pull` |  |  | 6 |
| :fontawesome-solid-hand-point-right: | `hand-point-right` | fa-solid | `o_icon_instruction` |  |  | 4 |
| :fontawesome-solid-hand-point-up: | `hand-point-up` | fa-solid | `o_icon_cns_status_selected` |  |  | 3 |
|  |  |  | `o_icon_hand_point_up` |  |  | 4 |
|  |  |  | `o_icon_tb_broker_enrollment_in_progress` |  |  | 3 |
| :fontawesome-solid-hands-clapping: | `hands-clapping` | fa-solid | `o_icon_qual_part_not_available` |  |  | 2 |
| :fontawesome-regular-handshake: | `handshake` | fa-regular | `o_icon_disclaimer` |  |  | 10 |
| :fontawesome-solid-hashtag: | `hashtag` | fa-solid | `o_icon_number_of` |  |  | 3 |
| :fontawesome-regular-hdd: | `hdd` | fa-regular | `o_icon_hdd` |  |  | 4 |
| :fontawesome-solid-header: | `header` | fa-solid | `o_icon_header` | Überschrift | Header | 6 |
| :fontawesome-solid-heart: | `heart` | fa-solid | `o_icon_heart` | Herz | Heart | 3 |
| :fontawesome-solid-highlighter: | `highlighter` | fa-solid | `o_icon_correction` |  |  | 12 |
|  |  |  | `o_icon_status_in_review` |  |  | 15 |
| :fontawesome-solid-history: | `history` | fa-solid | `o_icon_version` | Version | Version | 9 |
| :fontawesome-solid-home: | `home` | fa-solid | `o_icon_home` | Home | Home | 17 |
| :fontawesome-solid-hourglass: | `hourglass` | fa-solid | `o_icon_curriculum_status_provisional` |  |  | 3 |
|  |  |  | `o_icon_qual_part_participated` |  |  | 4 |
|  |  |  | `o_icon_tb_selection_waiting_list` |  |  | 3 |
| :fontawesome-solid-hourglass-end: | `hourglass-end` | fa-solid | `o_as_mode_followup` |  |  | 3 |
|  |  |  | `o_as_mode_leadtime` |  |  | 3 |
|  |  |  | `o_icon_timelimit_end` |  |  | 2 |
| :fontawesome-regular-hourglass-half: | `hourglass-half` | fa-regular | `o_ac_membership_confirmation_icon` |  |  | 4 |
|  |  |  | `o_ac_order_status_inprocess_icon` |  |  | 3 |
|  |  |  | `o_ac_order_status_open_icon` |  |  | 3 |
|  |  |  | `o_ac_order_status_pending_icon` |  |  | 4 |
|  |  |  | `o_ac_order_status_prepayment_icon` |  |  | 3 |
|  |  |  | `o_icon_candidate` |  |  | 3 |
|  |  |  | `o_icon_payment_open` |  |  | 5 |
|  |  |  | `o_icon_timelimit_half` |  |  | 5 |
|  |  |  | `o_membership_status_pending` | Mitglied ausstehend | Member Pending | 5 |
|  |  |  | `o_membership_status_reservation` |  |  | 2 |
| :fontawesome-solid-hourglass-start: | `hourglass-start` | fa-solid | `o_icon_timelimit_start` |  |  | 4 |
| :fontawesome-solid-house: | `house` | fa-solid | `o_icon_breadcrumb_root` |  |  | 3 |
| :fontawesome-brands-html5: | `html5` | fa-brands | `o_icon_html5` |  |  | 5 |
| :fontawesome-solid-image: | `image` | fa-solid | `o_icon_image` | Bild | Image | 9 |
|  |  |  | `o_icon_image_comparison` |  |  | 11 |
|  |  |  | `o_icon_media` | Medien | Media | 9 |
| :fontawesome-solid-images: | `images` | fa-solid | `o_icon_images` | Bilder | Images | 3 |
| :fontawesome-solid-inbox: | `inbox` | fa-solid | `o_pf_icon` |  |  | 5 |
| :fontawesome-solid-infinity: | `infinity` | fa-solid | `o_icon_openolat` | OpenOlat | OpenOlat | 4 |
|  |  |  | `o_icon_provider_olat` |  |  | 6 |
| :fontawesome-solid-info-circle: | `info-circle` | fa-solid | `o_icon_description` | Beschreibung | Description | 23 |
|  |  |  | `o_icon_impress` |  |  | 7 |
|  |  |  | `o_icon_info` | Info | Info | 44 |
|  |  |  | `o_icon_info_ap` |  |  | 7 |
|  |  |  | `o_icon_info_badge` |  |  | 5 |
|  |  |  | `o_icon_info_resource` |  |  | 5 |
|  |  |  | `o_icon_news` |  |  | 5 |
|  |  |  | `o_infomsg_icon` |  |  | 14 |
|  |  |  | `o_portlet_infomsg_icon` |  |  | 2 |
| :fontawesome-solid-institution: | `institution` | fa-solid | `o_portlet_institutions_icon` |  |  | 2 |
| :fontawesome-solid-italic: | `italic` | fa-solid | `o_icon_italic` | Kursiv | Italic | 3 |
| :fontawesome-solid-k: | `k` | fa-solid | `o_icon_k` |  |  | 3 |
| :fontawesome-solid-key: | `key` | fa-solid | `o_ac_token_icon` |  |  | 6 |
|  |  |  | `o_icon_owner` | Besitzer | Owner | 5 |
| :fontawesome-regular-keyboard: | `keyboard` | fa-regular | `o_icon_keyboard` |  |  | 3 |
| :fontawesome-solid-laptop: | `laptop` | fa-solid | `o_icon_assessment_mode` |  |  | 23 |
| :fontawesome-solid-leaf: | `leaf` | fa-solid | `o_icon_instructional_design` |  |  | 4 |
|  |  |  | `o_icon_proj_project` |  |  | 14 |
| :fontawesome-solid-level-up: | `level-up` | fa-solid | `o_icon_reactivate` |  |  | 3 |
| :fontawesome-regular-lightbulb: | `lightbulb` | fa-regular | `o_icon_details` | Details | Details | 22 |
|  |  |  | `o_icon_lightbulb` |  |  | 4 |
|  |  |  | `o_icon_qti_solution` |  |  | 2 |
|  |  |  | `o_portlet_dyk_icon` |  |  | 2 |
| :fontawesome-solid-line-chart: | `line-chart` | fa-solid | `o_icon_qual_ana_trend` |  |  | 4 |
| :fontawesome-solid-link: | `link` | fa-solid | `o_icon_link` | Link | Link | 23 |
|  |  |  | `o_icon_link` | Link | Link | 23 |
|  |  |  | `o_icon_proj_reference` |  |  | 3 |
|  |  |  | `o_ll_icon` |  |  | 6 |
|  |  |  | `o_portlet_links_icon` |  |  | 2 |
| :fontawesome-brands-linkedin: | `linkedin` | fa-brands | `o_icon_linkedin` | LinkedIn | LinkedIn | 11 |
|  |  |  | `o_icon_linkedin` | LinkedIn | LinkedIn | 11 |
| :fontawesome-brands-linkedin-in: | `linkedin-in` | fa-brands | `o_icon_provider_linkedin` | LinkedIn | LinkedIn | 6 |
| :fontawesome-solid-list: | `list` | fa-solid | `o_icon_list` | Liste | List | 7 |
|  |  |  | `o_icon_pool_collection` |  |  | 5 |
| :fontawesome-solid-list-check: | `list-check` | fa-solid | `o_icon_list_check` |  |  | 3 |
| :fontawesome-solid-list-ol: | `list-ol` | fa-solid | `o_icon_list_num` |  |  | 6 |
|  |  |  | `o_mi_qtimatch_truefalse` |  |  | 4 |
| :fontawesome-solid-location-crosshairs: | `location-crosshairs` | fa-solid | `o_icon_exact_location` |  |  | 7 |
| :fontawesome-solid-location-dot: | `location-dot` | fa-solid | `o_icon_location` | Ort | Location | 19 |
| :fontawesome-solid-lock: | `lock` | fa-solid | `o_ac_membersonly_icon` |  |  | 5 |
|  |  |  | `o_icon_identity_permanent` |  |  | 3 |
|  |  |  | `o_icon_locked` | Gesperrt | Locked | 14 |
|  |  |  | `o_icon_password` | Passwort | Password | 8 |
|  |  |  | `o_icon_pf_entry_closed` |  |  | 6 |
|  |  |  | `o_icon_pf_section_closed` |  |  | 6 |
|  |  |  | `o_icon_tb_group_restrictions` |  |  | 3 |
|  |  |  | `o_midlock` |  |  | 7 |
| :fontawesome-solid-long-arrow-right: | `long-arrow-right` | fa-solid | `o_icon_eva_end_hide` |  |  | 3 |
|  |  |  | `o_icon_todo_date_range` |  |  | 3 |
| :fontawesome-solid-magic: | `magic` | fa-solid | `o_icon_wizard` |  |  | 5 |
| :fontawesome-solid-magnifying-glass: | `magnifying-glass` | fa-solid | `o_icon_magnifying_glass` |  |  | 6 |
| :fontawesome-solid-magnifying-glass-plus: | `magnifying-glass-plus` | fa-solid | `o_icon_search_lookup` |  |  | 3 |
| :fontawesome-solid-mail-reply: | `mail-reply` | fa-solid | `o_icon_node_under` |  |  | 5 |
| :fontawesome-regular-map: | `map` | fa-regular | `o_mi_qtihotspot` |  |  | 4 |
| :fontawesome-solid-map-signs: | `map-signs` | fa-solid | `o_icon_learning_path` |  |  | 10 |
|  |  |  | `o_midlpexob` |  |  | 6 |
| :fontawesome-solid-medal: | `medal` | fa-solid | `o_icon_statement` |  |  | 5 |
|  |  |  | `o_icon_success_status` |  |  | 8 |
| :fontawesome-regular-meh: | `meh` | fa-regular | `o_FileResource-SURVEY_icon` |  |  | 2 |
|  |  |  | `o_iqsurv_icon` |  |  | 7 |
| :fontawesome-solid-microphone: | `microphone` | fa-solid | `o_icon_audio_record` |  |  | 10 |
| :fontawesome-solid-minus: | `minus` | fa-solid | `o_ac_status_canceled_icon` |  |  | 6 |
|  |  |  | `o_icon_minus` |  |  | 4 |
|  |  |  | `o_icon_not_identified` |  |  | 3 |
|  |  |  | `o_icon_table_details_collaps` |  |  | 4 |
| :fontawesome-solid-minus-circle: | `minus-circle` | fa-solid | `o_icon_delete` | Löschen | Delete | 36 |
|  |  |  | `o_icon_member_skipped` |  |  | 6 |
| :fontawesome-regular-minus-square: | `minus-square` | fa-regular | `o_icon_check_mixed` |  |  | 4 |
|  |  |  | `o_icon_review_remove` |  |  | 2 |
| :fontawesome-solid-mobile: | `mobile` | fa-solid | `o_icon_mobile` | Mobiltelefon | Mobile | 3 |
| :fontawesome-solid-money-bill-1: | `money-bill-1` | fa-solid | `o_icon_pay` |  |  | 5 |
| :fontawesome-solid-mouse-pointer: | `mouse-pointer` | fa-solid | `o_icon_pointer` |  |  | 3 |
| :fontawesome-solid-n: | `n` | fa-solid | `o_icon_tb_selection_not_enrolled` |  |  | 3 |
| :fontawesome-solid-navicon: | `navicon` | fa-solid | `o_icon_pf_section` |  |  | 9 |
| :fontawesome-brands-openid: | `openid` | fa-brands | `o_icon_provider_openid` |  |  | 5 |
| :fontawesome-solid-paint-brush: | `paint-brush` | fa-solid | `o_icon_brush` | Pinsel | Brush | 3 |
|  |  |  | `o_icon_proj_whiteboard` |  |  | 3 |
|  |  |  | `o_mi_qtidrawing` |  |  | 4 |
| :fontawesome-regular-paper-plane: | `paper-plane` | fa-regular | `o_icon_show_send` |  |  | 6 |
|  |  |  | `o_portlet_quickstart_icon` |  |  | 2 |
| :fontawesome-solid-paperclip: | `paperclip` | fa-solid | `o_icon_paperclip` |  |  | 3 |
| :fontawesome-solid-paragraph: | `paragraph` | fa-solid | `o_icon_paragraph` | Absatz | Paragraph | 2 |
| :fontawesome-solid-pause: | `pause` | fa-solid | `o_icon_certification_status_inactive` |  |  | 2 |
|  |  |  | `o_icon_qti_suspend` |  |  | 4 |
| :fontawesome-regular-pause-circle: | `pause-circle` | fa-regular | `o_icon_identity_inactive` |  |  | 4 |
| :fontawesome-solid-pen: | `pen` | fa-solid | `o_icon_curriculum_status_preparation` |  |  | 3 |
| :fontawesome-solid-pencil: | `pencil` | fa-solid | `o_icon_changes` |  |  | 7 |
|  |  |  | `o_icon_new_portfolio` |  |  | 16 |
|  |  |  | `o_icon_overridden` |  |  | 4 |
|  |  |  | `o_icon_pencil` |  |  | 5 |
|  |  |  | `o_icon_pf_entry_draft` |  |  | 6 |
|  |  |  | `o_icon_pf_new_entry` |  |  | 3 |
|  |  |  | `o_icon_qitem_draft` |  |  | 4 |
|  |  |  | `o_icon_rename` | Umbenennen | Rename | 3 |
|  |  |  | `o_icon_repo_status_preparation` |  |  | 2 |
| :fontawesome-solid-pencil-square: | `pencil-square` | fa-solid | `o_FileResource-IMSQTI21_icon` |  |  | 6 |
|  |  |  | `o_FileResource-TEST_icon` |  |  | 3 |
|  |  |  | `o_iqself_icon` |  |  | 5 |
|  |  |  | `o_iqtest_icon` |  |  | 7 |
|  |  |  | `o_qtiassessment_icon` |  |  | 14 |
| :fontawesome-solid-people-group: | `people-group` | fa-solid | `o_icon_people` |  |  | 6 |
| :fontawesome-solid-person-chalkboard: | `person-chalkboard` | fa-solid | `o_icon_room_management` |  |  | 3 |
| :fontawesome-solid-person-circle-minus: | `person-circle-minus` | fa-solid | `o_icon_non_members` |  |  | 3 |
| :fontawesome-solid-person-rays: | `person-rays` | fa-solid | `o_icon_provider_guest` | Gast | Guest | 5 |
| :fontawesome-solid-phone: | `phone` | fa-solid | `o_icon_phone` | Telefon | Phone | 4 |
| :fontawesome-solid-play: | `play` | fa-solid | `o_icon_assessment_inspection_active` |  |  | 4 |
|  |  |  | `o_icon_certification_resume` |  |  | 2 |
|  |  |  | `o_icon_ms_pending` |  |  | 2 |
|  |  |  | `o_icon_play` | Abspielen | Play | 4 |
|  |  |  | `o_icon_qual_part_execute` |  |  | 4 |
|  |  |  | `o_icon_status_in_progress` | Status: In Bearbeitung | Status: In Progress | 9 |
|  |  |  | `o_icon_tb_run_start` |  |  | 4 |
|  |  |  | `o_icon_video_play` |  |  | 7 |
|  |  |  | `o_icon_video_resume` |  |  | 3 |
| :fontawesome-regular-play-circle: | `play-circle` | fa-regular | `o_icon_qual_dc_ready` |  |  | 3 |
|  |  |  | `o_icon_qual_dc_running` |  |  | 3 |
|  |  |  | `o_icon_qual_exec_participating` |  |  | 2 |
|  |  |  | `o_icon_qual_exec_ready` |  |  | 2 |
| :fontawesome-solid-plus: | `plus` | fa-solid | `o_icon_not_correct_plus` |  |  | 5 |
|  |  |  | `o_icon_plus` |  |  | 7 |
|  |  |  | `o_icon_table_details_expand` |  |  | 5 |
| :fontawesome-solid-plus-circle: | `plus-circle` | fa-solid | `o_icon_add` | Hinzufügen | Add | 216 |
|  |  |  | `o_icon_lic_add` |  |  | 3 |
|  |  |  | `o_icon_qual_dc_create` |  |  | 3 |
|  |  |  | `o_icon_qual_gen_ce_add` |  |  | 3 |
|  |  |  | `o_icon_qual_gen_create` |  |  | 3 |
|  |  |  | `o_icon_qual_gen_re_add` |  |  | 3 |
| :fontawesome-solid-plus-square: | `plus-square` | fa-solid | `o_icon_review_add` |  |  | 2 |
| :fontawesome-solid-podcast: | `podcast` | fa-solid | `o_FileResource-PODCAST_icon` |  |  | 2 |
|  |  |  | `o_podcast_icon` |  |  | 12 |
| :fontawesome-solid-power-off: | `power-off` | fa-solid | `o_icon_close_resource` |  |  | 4 |
|  |  |  | `o_icon_lifecycle` |  |  | 2 |
| :fontawesome-solid-print: | `print` | fa-solid | `o_icon_eva_print` |  |  | 4 |
|  |  |  | `o_icon_print` | Drucken | Print | 23 |
|  |  |  | `o_icon_private` |  |  | 2 |
|  |  |  | `o_icon_qual_ana_print` |  |  | 4 |
| :fontawesome-solid-puzzle-piece: | `puzzle-piece` | fa-solid | `o_icon_eportfolio_add` |  |  | 7 |
|  |  |  | `o_icon_eportfolio_link` |  |  | 2 |
| :fontawesome-solid-q: | `q` | fa-solid | `o_icon_q` |  |  | 3 |
| :fontawesome-solid-qrcode: | `qrcode` | fa-solid | `o_icon_qrcode` | QR-Code | QR Code | 23 |
| :fontawesome-solid-question: | `question` | fa-solid | `o_icon_immunity_proof_claimed` |  |  | 3 |
|  |  |  | `o_icon_question` |  |  | 5 |
|  |  |  | `o_icon_unselected` |  |  | 2 |
|  |  |  | `o_icon_user_anonymous` |  |  | 5 |
| :fontawesome-solid-question-circle: | `question-circle` | fa-solid | `o_icon_help` | Hilfe | Help | 53 |
|  |  |  | `o_icon_qti_hint` |  |  | 3 |
| :fontawesome-solid-quote-left: | `quote-left` | fa-solid | `o_icon_citation` |  |  | 6 |
| :fontawesome-solid-quote-right: | `quote-right` | fa-solid | `o_icon_quote_right` |  |  | 3 |
| :fontawesome-solid-radiation: | `radiation` | fa-solid | `o_icon_radiation` |  |  | 2 |
| :fontawesome-solid-random: | `random` | fa-solid | `o_icon_shuffle` |  |  | 9 |
| :fontawesome-solid-receipt: | `receipt` | fa-solid | `o_ac_invoice_icon` |  |  | 3 |
| :fontawesome-solid-recycle: | `recycle` | fa-solid | `o_icon_recycle` |  |  | 7 |
| :fontawesome-solid-refresh: | `refresh` | fa-solid | `o_grad_assignment_inprocess` |  |  | 3 |
|  |  |  | `o_icon_calendar_sync` |  |  | 4 |
|  |  |  | `o_icon_extend` |  |  | 4 |
|  |  |  | `o_icon_pf_section_progress` |  |  | 6 |
|  |  |  | `o_icon_proj_recurrence` |  |  | 3 |
|  |  |  | `o_icon_refresh` | Aktualisieren | Refresh | 33 |
|  |  |  | `o_icon_response_feedback` |  |  | 2 |
|  |  |  | `o_icon_update` | Aktualisieren | Update | 3 |
| :fontawesome-solid-repeat: | `repeat` | fa-solid | `o_icon_qual_gen_enabled` |  |  | 4 |
|  |  |  | `o_icon_redo` |  |  | 4 |
|  |  |  | `o_icon_video_replay` |  |  | 3 |
| :fontawesome-solid-reply: | `reply` | fa-solid | `o_icon_reopen` | Erneut öffnen | Reopen | 8 |
|  |  |  | `o_icon_reply` | Antworten | Reply | 4 |
| :fontawesome-solid-reply-all: | `reply-all` | fa-solid | `o_icon_reply_with_quote` |  |  | 3 |
| :fontawesome-solid-retweet: | `retweet` | fa-solid | `o_icon_managed` |  |  | 11 |
| :fontawesome-solid-right-left: | `right-left` | fa-solid | `o_icon_right_left` |  |  | 3 |
| :fontawesome-solid-rotate-left: | `rotate-left` | fa-solid | `o_icon_attempts` |  |  | 4 |
|  |  |  | `o_icon_pf_entry_revision` |  |  | 6 |
|  |  |  | `o_icon_qitem_revised` |  |  | 4 |
|  |  |  | `o_icon_revoke` |  |  | 3 |
|  |  |  | `o_icon_tb_withdraw` |  |  | 7 |
| :fontawesome-solid-rotate-right: | `rotate-right` | fa-solid | `o_icon_certification_status_recertifying` |  |  | 3 |
|  |  |  | `o_icon_retry` |  |  | 8 |
|  |  |  | `o_icon_tb_enroll` |  |  | 4 |
|  |  |  | `o_icon_tb_run` |  |  | 3 |
| :fontawesome-solid-rss: | `rss` | fa-solid | `o_icon_notification` | Benachrichtigung | Notification | 8 |
|  |  |  | `o_icon_rss` | RSS | RSS | 12 |
|  |  |  | `o_icon_rss_unsubscribe` |  |  | 4 |
|  |  |  | `o_portlet_noti_icon` |  |  | 2 |
| :fontawesome-solid-s: | `s` | fa-solid | `o_icon_s` |  |  | 3 |
| :fontawesome-solid-save: | `save` | fa-solid | `o_icon_save` | Speichern | Save | 6 |
| :fontawesome-solid-scale-balanced: | `scale-balanced` | fa-solid | `o_icon_tb_priority` |  |  | 4 |
|  |  |  | `o_icon_tb_strategy_max_priorities` |  |  | 3 |
| :fontawesome-solid-scale-unbalanced-flip: | `scale-unbalanced-flip` | fa-solid | `o_icon_score_unbalanced` |  |  | 5 |
| :fontawesome-solid-scroll: | `scroll` | fa-solid | `o_icon_activity_log` |  |  | 3 |
| :fontawesome-solid-search: | `search` | fa-solid | `o_icon_empty_indicator` |  |  | 10 |
|  |  |  | `o_icon_search` | Suchen | Search | 51 |
| :fontawesome-solid-search-minus: | `search-minus` | fa-solid | `o_icon_shrink` |  |  | 3 |
| :fontawesome-solid-search-plus: | `search-plus` | fa-solid | `o_icon_add_search` |  |  | 3 |
|  |  |  | `o_icon_browse` |  |  | 7 |
|  |  |  | `o_icon_enlarge` |  |  | 7 |
| :fontawesome-solid-section: | `section` | fa-solid | `o_icon_legal_folder` |  |  | 4 |
| :fontawesome-solid-share: | `share` | fa-solid | `o_icon_pf_page_shared` |  |  | 4 |
|  |  |  | `o_icon_pf_quick_links` |  |  | 2 |
|  |  |  | `o_icon_publish` | Publizieren | Publish | 5 |
|  |  |  | `o_icon_qitem_share` |  |  | 3 |
|  |  |  | `o_icon_share` | Teilen | Share | 4 |
| :fontawesome-solid-share-alt: | `share-alt` | fa-solid | `o_icon_pf_my_shares` |  |  | 3 |
| :fontawesome-solid-share-alt-square: | `share-alt-square` | fa-solid | `o_icon_pf_shared_with_me` |  |  | 3 |
|  |  |  | `o_icon_pool_pool` |  |  | 7 |
|  |  |  | `o_icon_share_alt` |  |  | 3 |
| :fontawesome-regular-share-square: | `share-square` | fa-regular | `o_icon_export` | Exportieren | Export | 23 |
|  |  |  | `o_icon_share_social` |  |  | 3 |
| :fontawesome-solid-shield: | `shield` | fa-solid | `o_icon_competences` |  |  | 12 |
| :fontawesome-solid-shopping-cart: | `shopping-cart` | fa-solid | `o_icon_booking` |  |  | 11 |
| :fontawesome-solid-shuffle: | `shuffle` | fa-solid | `o_icon_tb_method` |  |  | 3 |
| :fontawesome-solid-sign-in: | `sign-in` | fa-solid | `o_en_icon` |  |  | 7 |
|  |  |  | `o_icon_login` | Anmelden | Login | 9 |
|  |  |  | `o_portlet_shibboleth_icon` |  |  | 2 |
| :fontawesome-solid-sign-out: | `sign-out` | fa-solid | `o_icon_logout` | Abmelden | Logout | 3 |
|  |  |  | `o_icon_sign_out` |  |  | 4 |
| :fontawesome-solid-sitemap: | `sitemap` | fa-solid | `o_icon_catalog` | Katalog | Catalog | 7 |
|  |  |  | `o_icon_levels` |  |  | 8 |
|  |  |  | `o_icon_sitemap` | Sitemap | Sitemap | 4 |
|  |  |  | `o_icon_structure` | Struktur | Structure | 17 |
|  |  |  | `o_icon_taxonomy_levels` |  |  | 4 |
| :fontawesome-solid-sliders: | `sliders` | fa-solid | `o_FileResource-FORM_icon` |  |  | 6 |
|  |  |  | `o_icon_rubric` |  |  | 3 |
|  |  |  | `o_survey_icon` |  |  | 4 |
| :fontawesome-regular-soccer-ball: | `soccer-ball` | fa-regular | `o_practice_icon` |  |  | 6 |
| :fontawesome-solid-sort: | `sort` | fa-solid | `o_icon_sort` | Sortieren | Sort | 3 |
| :fontawesome-solid-sort-amount-asc: | `sort-amount-asc` | fa-solid | `o_icon_sort_amount_asc` |  |  | 5 |
|  |  |  | `o_icon_sort_menu` |  |  | 4 |
| :fontawesome-solid-sort-amount-desc: | `sort-amount-desc` | fa-solid | `o_icon_sort_amount_desc` |  |  | 6 |
| :fontawesome-solid-sort-asc: | `sort-asc` | fa-solid | `o_icon_sort_asc` | Aufsteigend | Sort Ascending | 6 |
| :fontawesome-solid-sort-desc: | `sort-desc` | fa-solid | `o_icon_sort_desc` | Absteigend | Sort Descending | 6 |
| :fontawesome-solid-spinner: | `spinner` | fa-solid | `o_as_mode_assessment` |  |  | 3 |
|  |  |  | `o_icon_assessment_inspection_inprogress` |  |  | 4 |
|  |  |  | `o_icon_busy` | Beschäftigt | Busy | 8 |
|  |  |  | `o_icon_pending` | Ausstehend | Pending | 7 |
| :fontawesome-regular-square: | `square` | fa-regular | `o_grad_assignment_assigned` |  |  | 4 |
|  |  |  | `o_icon_calendar_disabled` |  |  | 2 |
|  |  |  | `o_icon_check_off` |  |  | 16 |
|  |  |  | `o_icon_checkbox` |  |  | 3 |
|  |  |  | `o_icon_pool_private` |  |  | 4 |
|  |  |  | `o_icon_quiz_multiple_choice_off` |  |  | 6 |
|  |  |  | `o_icon_rectangle` |  |  | 5 |
|  |  |  | `o_icon_single_element` |  |  | 4 |
| :fontawesome-regular-square-caret-down: | `square-caret-down` | fa-regular | `o_icon_show_more` |  |  | 2 |
| :fontawesome-regular-square-caret-up: | `square-caret-up` | fa-regular | `o_icon_show_less` |  |  | 2 |
| :fontawesome-solid-square-root-variable: | `square-root-variable` | fa-solid | `o_icon_math` | Mathematik | Math | 5 |
| :fontawesome-solid-square-rss: | `square-rss` | fa-solid | `o_icon_square_rss` |  |  | 3 |
| :fontawesome-solid-square-share-nodes: | `square-share-nodes` | fa-solid | `o_icon_curriculum_implementations` |  |  | 12 |
|  |  |  | `o_icon_taxonomy_level_type` |  |  | 3 |
| :fontawesome-brands-square-x-twitter: | `square-x-twitter` | fa-brands | `o_icon_twitter` | Twitter/X | Twitter/X | 5 |
| :fontawesome-solid-star: | `star` | fa-solid | `o_icon_default_config` |  |  | 3 |
|  |  |  | `o_icon_grade` | Note | Grade | 9 |
|  |  |  | `o_icon_others` |  |  | 2 |
|  |  |  | `o_icon_qitem_review` |  |  | 4 |
|  |  |  | `o_icon_rating_off` |  |  | 9 |
|  |  |  | `o_icon_rating_on` |  |  | 5 |
|  |  |  | `o_icon_repo_status_review` |  |  | 2 |
|  |  |  | `o_icon_review` |  |  | 6 |
|  |  |  | `o_icon_star` | Stern | Star | 6 |
|  |  |  | `o_portlet_iframe_icon` |  |  | 2 |
| :fontawesome-solid-step-backward: | `step-backward` | fa-solid | `o_icon_reset` | Zurücksetzen | Reset | 6 |
| :fontawesome-solid-sticky-note: | `sticky-note` | fa-solid | `o_icon_educational_type` |  |  | 2 |
|  |  |  | `o_icon_notes` | Notizen | Notes | 20 |
|  |  |  | `o_icon_notes_empty` |  |  | 3 |
|  |  |  | `o_icon_proj_note` |  |  | 9 |
|  |  |  | `o_portlet_notes_icon` |  |  | 2 |
| :fontawesome-solid-stop: | `stop` | fa-solid | `o_as_mode_stop` |  |  | 5 |
|  |  |  | `o_icon_qti_cancel` |  |  | 3 |
| :fontawesome-solid-street-view: | `street-view` | fa-solid | `o_icon_fake_participant` |  |  | 4 |
| :fontawesome-solid-table: | `table` | fa-solid | `o_icon_report` | Bericht | Report | 3 |
|  |  |  | `o_mi_qtimatch` |  |  | 4 |
| :fontawesome-solid-table-cells-large: | `table-cells-large` | fa-solid | `o_icon_name` |  |  | 3 |
| :fontawesome-solid-table-list: | `table-list` | fa-solid | `o_icon_table` | Tabelle | Table | 15 |
| :fontawesome-solid-tachometer: | `tachometer` | fa-solid | `o_portlet_sysinfo_icon` |  |  | 2 |
| :fontawesome-solid-tag: | `tag` | fa-solid | `o_icon_tag` | Tag | Tag | 5 |
| :fontawesome-solid-tags: | `tags` | fa-solid | `o_icon_tags` | Tags | Tags | 16 |
| :fontawesome-solid-tasks: | `tasks` | fa-solid | `o_gta_icon` |  |  | 9 |
|  |  |  | `o_ta_icon` |  |  | 5 |
| :fontawesome-solid-th-large: | `th-large` | fa-solid | `o_icon_table_large` |  |  | 2 |
| :fontawesome-solid-thumb-tack: | `thumb-tack` | fa-solid | `o_icon_qual_ana_pres_edit` |  |  | 3 |
| :fontawesome-regular-thumbs-down: | `thumbs-down` | fa-regular | `o_icon_decline` |  |  | 16 |
|  |  |  | `o_icon_rating_no_off` |  |  | 4 |
|  |  |  | `o_icon_rating_no_on` |  |  | 4 |
|  |  |  | `o_icon_rejected` |  |  | 8 |
|  |  |  | `o_icon_revision` |  |  | 3 |
| :fontawesome-regular-thumbs-up: | `thumbs-up` | fa-regular | `o_icon_accepted` |  |  | 21 |
|  |  |  | `o_icon_browsercheck` |  |  | 2 |
|  |  |  | `o_icon_pending_confirmations` |  |  | 4 |
|  |  |  | `o_icon_rating_yes_off` |  |  | 4 |
|  |  |  | `o_icon_rating_yes_on` |  |  | 4 |
|  |  |  | `o_icon_restore` | Wiederherstellen | Restore | 12 |
|  |  |  | `o_ms_icon` |  |  | 5 |
| :fontawesome-solid-thumbtack: | `thumbtack` | fa-solid | `o_icon_thumbtack` |  |  | 3 |
| :fontawesome-solid-timeline: | `timeline` | fa-solid | `o_icon_timeline` |  |  | 4 |
| :fontawesome-solid-times: | `times` | fa-solid | `o_ac_status_error_icon` |  |  | 6 |
|  |  |  | `o_icon_absence` |  |  | 3 |
|  |  |  | `o_icon_addremove_remove` |  |  | 3 |
|  |  |  | `o_icon_close` | Schliessen | Close | 19 |
|  |  |  | `o_icon_close_tab` |  |  | 3 |
|  |  |  | `o_icon_close_tool` |  |  | 3 |
|  |  |  | `o_icon_immunity_proof_none` |  |  | 3 |
|  |  |  | `o_icon_not_correct` |  |  | 8 |
|  |  |  | `o_icon_progress_danger` |  |  | 4 |
|  |  |  | `o_icon_reject` | Ablehnen | Reject | 8 |
|  |  |  | `o_icon_remove` | Entfernen | Remove | 17 |
|  |  |  | `o_icon_review_removed` |  |  | 5 |
| :fontawesome-solid-times-circle: | `times-circle` | fa-solid | `o_icon_failed` | Nicht bestanden | Failed | 23 |
|  |  |  | `o_icon_incorrect_response` |  |  | 4 |
|  |  |  | `o_icon_qti_summary_ended` |  |  | 6 |
|  |  |  | `o_icon_qual_exec_future` |  |  | 3 |
|  |  |  | `o_icon_qual_exec_over` |  |  | 2 |
|  |  |  | `o_icon_quiz_single_choice_incorrect` |  |  | 4 |
|  |  |  | `o_icon_remove_filters` |  |  | 10 |
|  |  |  | `o_icon_rubric_insufficient` |  |  | 6 |
|  |  |  | `o_icon_status_unavailable` | Status: Nicht verfügbar | Status: Unavailable | 22 |
| :fontawesome-solid-times-square: | `times-square` | fa-solid | `o_icon_quiz_multiple_choice_incorrect` |  |  | 4 |
| :fontawesome-solid-tint: | `tint` | fa-solid | `o_icon_color_picker` | Farbwähler | Color Picker | 2 |
|  |  |  | `o_icon_draw_color` |  |  | 9 |
| :fontawesome-solid-toggle-off: | `toggle-off` | fa-solid | `o_icon_qitem_show_metadata` |  |  | 3 |
|  |  |  | `o_icon_qual_ana_show_filter` |  |  | 3 |
|  |  |  | `o_icon_toggle_off` |  |  | 6 |
| :fontawesome-solid-toggle-on: | `toggle-on` | fa-solid | `o_icon_options` |  |  | 2 |
|  |  |  | `o_icon_qitem_hide_metadata` |  |  | 3 |
|  |  |  | `o_icon_qual_ana_hide_filter` |  |  | 3 |
|  |  |  | `o_icon_toggle_on` |  |  | 7 |
| :fontawesome-solid-trash: | `trash` | fa-solid | `o_icon_qitem_endOfLife` |  |  | 4 |
|  |  |  | `o_membership_status_resourcedeleted` |  |  | 3 |
| :fontawesome-regular-trash-can: | `trash-can` | fa-regular | `o_icon_building_status_deleted` |  |  | 2 |
|  |  |  | `o_icon_businessgroup_status_deleted` |  |  | 2 |
|  |  |  | `o_icon_businessgroup_status_trash` |  |  | 2 |
|  |  |  | `o_icon_clear_all` |  |  | 6 |
|  |  |  | `o_icon_curriculum_status_deleted` |  |  | 2 |
|  |  |  | `o_icon_delete_item` | Löschen | Delete | 158 |
|  |  |  | `o_icon_deleted` |  |  | 21 |
|  |  |  | `o_icon_identity_deleted` |  |  | 6 |
|  |  |  | `o_icon_pf_entry_deleted` |  |  | 7 |
|  |  |  | `o_icon_pf_trash` |  |  | 4 |
|  |  |  | `o_icon_proj_project_status_deleted` |  |  | 4 |
|  |  |  | `o_icon_qitem_delete` |  |  | 3 |
|  |  |  | `o_icon_qual_dc_delete` |  |  | 3 |
|  |  |  | `o_icon_qual_gen_delete` |  |  | 3 |
|  |  |  | `o_icon_repo_status_deleted` |  |  | 3 |
|  |  |  | `o_icon_repo_status_trash` |  |  | 3 |
|  |  |  | `o_icon_todo_status_deleted` |  |  | 3 |
|  |  |  | `o_icon_trash` |  |  | 13 |
| :fontawesome-solid-triangle-exclamation: | `triangle-exclamation` | fa-solid | `o_icon_certification_status_expired_renewable` |  |  | 2 |
|  |  |  | `o_icon_recertification_warning` |  |  | 9 |
|  |  |  | `o_icon_triangle_exclamation` |  |  | 4 |
|  |  |  | `o_icon_validation_warning` |  |  | 7 |
| :fontawesome-solid-trophy: | `trophy` | fa-solid | `o_icon_assessment_tool` |  |  | 18 |
|  |  |  | `o_icon_score` | Punkte | Score | 13 |
|  |  |  | `o_icon_trophy` | Trophäe | Trophy | 7 |
| :fontawesome-solid-tv: | `tv` | fa-solid | `o_gotomeeting_icon` |  |  | 6 |
|  |  |  | `o_openmeetings_icon` |  |  | 7 |
|  |  |  | `o_vc_icon` |  |  | 33 |
|  |  |  | `o_vitero_icon` |  |  | 5 |
| :fontawesome-solid-undo: | `undo` | fa-solid | `o_icon_reload` | Neu laden | Reload | 8 |
|  |  |  | `o_icon_reset_data` |  |  | 13 |
|  |  |  | `o_icon_undo` | Rückgängig | Undo | 2 |
| :fontawesome-solid-universal-access: | `universal-access` | fa-solid | `o_icon_disadvantage_compensation` |  |  | 15 |
| :fontawesome-solid-university: | `university` | fa-solid | `o_icon_lrm` |  |  | 3 |
|  |  |  | `o_icon_provider_datenlotsen` |  |  | 4 |
|  |  |  | `o_icon_provider_ldap` | LDAP | LDAP | 3 |
|  |  |  | `o_icon_provider_shibboleth` |  |  | 4 |
|  |  |  | `o_icon_provider_switch_eduid` |  |  | 4 |
|  |  |  | `o_library_icon` |  |  | 3 |
| :fontawesome-solid-unlink: | `unlink` | fa-solid | `o_icon_split` |  |  | 3 |
| :fontawesome-solid-unlock: | `unlock` | fa-solid | `o_icon_unlocked` | Entsperrt | Unlocked | 3 |
| :fontawesome-solid-up-right-from-square: | `up-right-from-square` | fa-solid | `o_lti_icon` |  |  | 6 |
| :fontawesome-solid-upload: | `upload` | fa-solid | `o_icon_import` | Importieren | Import | 31 |
|  |  |  | `o_icon_qitem_import` |  |  | 3 |
|  |  |  | `o_icon_upload` | Hochladen | Upload | 17 |
|  |  |  | `o_mi_qtiupload` |  |  | 4 |
| :fontawesome-solid-user: | `user` | fa-solid | `o_icon_pool_my_items` |  |  | 3 |
|  |  |  | `o_icon_tb_method_namually` |  |  | 3 |
|  |  |  | `o_icon_user` | Benutzer | User | 99 |
| :fontawesome-solid-user-check: | `user-check` | fa-solid | `o_ac_membership_standard_icon` |  |  | 4 |
| :fontawesome-solid-user-circle: | `user-circle` | fa-solid | `o_ac_guest_icon` |  |  | 5 |
|  |  |  | `o_ac_guests_icon` |  |  | 5 |
|  |  |  | `o_icon_profile` | Profil | Profile | 4 |
| :fontawesome-solid-user-group: | `user-group` | fa-solid | `o_icon_num_participants` | Anzahl Teilnehmer | Number of Participants | 8 |
| :fontawesome-solid-user-large-slash: | `user-large-slash` | fa-solid | `o_icon_assessment_inspection_noshow` |  |  | 2 |
| :fontawesome-solid-user-md: | `user-md` | fa-solid | `o_icon_reviewer` | Gutachter | Reviewer | 4 |
| :fontawesome-solid-user-plus: | `user-plus` | fa-solid | `o_icon_add_member` | Mitglied hinzufügen | Add Member | 24 |
| :fontawesome-solid-user-secret: | `user-secret` | fa-solid | `o_icon_provider_keycloak` | Keycloak | Keycloak | 3 |
|  |  |  | `o_mi_qtiunkown` |  |  | 7 |
|  |  |  | `o_unkown_icon` |  |  | 3 |
| :fontawesome-solid-user-shield: | `user-shield` | fa-solid | `o_icon_user_authentication` |  |  | 4 |
| :fontawesome-solid-user-tie: | `user-tie` | fa-solid | `o_icon_manager` | Manager | Manager | 4 |
| :fontawesome-solid-user-times: | `user-times` | fa-solid | `o_icon_remove_member` | Mitglied entfernen | Remove Member | 4 |
| :fontawesome-regular-users: | `users` | fa-regular | `o_ac_group_icon` |  |  | 5 |
|  |  |  | `o_cmembers_icon` |  |  | 6 |
|  |  |  | `o_icon_committee` |  |  | 6 |
|  |  |  | `o_icon_membersmanagement` |  |  | 10 |
|  |  |  | `o_icon_pool_share` |  |  | 7 |
|  |  |  | `o_portlet_groups_icon` |  |  | 2 |
| :fontawesome-solid-v: | `v` | fa-solid | `o_icon_v` |  |  | 3 |
| :fontawesome-solid-video-camera: | `video-camera` | fa-solid | `o_icon_video_record` |  |  | 12 |
|  |  |  | `o_livestream_icon` |  |  | 8 |
| :fontawesome-solid-volume-up: | `volume-up` | fa-solid | `o_icon_audio` | Audio | Audio | 4 |
| :fontawesome-solid-wand-magic-sparkles: | `wand-magic-sparkles` | fa-solid | `o_icon_ai` | KI | AI | 6 |
|  |  |  | `o_icon_eva_coach_apply` |  |  | 3 |
| :fontawesome-solid-warning: | `warning` | fa-solid | `o_absences_col_warning` |  |  | 3 |
|  |  |  | `o_scorm_failed` |  |  | 3 |
|  |  |  | `o_scorm_incomplete` |  |  | 3 |
| :fontawesome-solid-wheelchair: | `wheelchair` | fa-solid | `o_icon_accessibility` |  |  | 2 |
| :fontawesome-solid-window-close: | `window-close` | fa-solid | `o_icon_qti_close_results` |  |  | 3 |
|  |  |  | `o_icon_qti_close_test` |  |  | 3 |
| :fontawesome-brands-windows: | `windows` | fa-brands | `o_icon_provider_adfs` |  |  | 10 |
|  |  |  | `o_teamsmeeting_icon` |  |  | 5 |
| :fontawesome-solid-wrench: | `wrench` | fa-solid | `o_icon_tools` |  |  | 5 |
| :fontawesome-brands-x-twitter: | `x-twitter` | fa-brands | `o_icon_provider_twitter` | Twitter/X | Twitter/X | 6 |
| :fontawesome-brands-xing: | `xing` | fa-brands | `o_icon_xing` | Xing | Xing | 5 |
| :fontawesome-brands-yahoo: | `yahoo` | fa-brands | `o_icon_yahoo` |  |  | 4 |
| :fontawesome-brands-youtube-square: | `youtube-square` | fa-brands | `o_icon_lic_youtube` |  |  | 6 |
|  |  |  | `o_icon_youtube` | YouTube | YouTube | 8 |
