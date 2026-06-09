# Icon-Map

OpenOlat mappt [FontAwesome](https://fontawesome.com/)-Icons auf eigene CSS-Klassen (`o_icon_*`).
Ein FA-Icon kann mehreren OO-Klassen entsprechen — jede Klasse steht für einen eigenen semantischen Kontext.

!!! info "Datenbasis"
    386 FA-Icons · 1045 OO-Klassen · 8,071 Referenzen im Quellcode (`src/main`)

## Verwendung

Icons werden als `<i>`-Element mit zwei CSS-Klassen eingebunden: `o_icon` (Basis) und der spezifischen Icon-Klasse:

```html
<i class="o_icon o_icon_user" aria-hidden="true"></i>
```

## Icon-Mapping Tabelle

| FA-Icon | Variant | OO CSS-Klasse | Vorkommen |
|---------|---------|---------------|---------:|
| `a` | fa-solid | `o_icon_a` | 6 |
| `address-card` | fa-solid | `o_icon_billing_address` | 9 |
|  |  | `o_icon_visiting_card` | 3 |
| `adjust` | fa-solid | `o_icon_todo_status_in_progress` | 5 |
|  |  | `o_lectures_rollcall_warning` | 8 |
| `align-center` | fa-solid | `o_icon_align_middle` | 2 |
| `align-justify` | fa-solid | `o_forum_all_flat_icon` | 3 |
|  |  | `o_icon_column` | 2 |
| `align-left` | fa-solid | `o_icon_align_left` | 6 |
|  |  | `o_icon_textinput` | 2 |
|  |  | `o_mi_qtiessay` | 5 |
| `align-right` | fa-solid | `o_forum_all_icon` | 3 |
|  |  | `o_icon_align_right` | 2 |
| `ambulance` | fa-solid | `o_icon_cleanup` | 3 |
| `angle-double-down` | fa-solid | `o_icon_modified` | 2 |
|  |  | `o_icon_move_down` | 39 |
|  |  | `o_icon_todo_priority_low` | 5 |
| `angle-double-left` | fa-solid | `o_icon_move_left` | 6 |
|  |  | `o_icon_previous_page` | 10 |
|  |  | `o_icon_previous_step` | 3 |
| `angle-double-right` | fa-solid | `o_icon_move_right` | 6 |
|  |  | `o_icon_next_page` | 10 |
|  |  | `o_icon_next_step` | 3 |
| `angle-double-up` | fa-solid | `o_icon_move_up` | 40 |
| `angle-down` | fa-solid | `o_icon_details_expand` | 33 |
| `angle-up` | fa-solid | `o_icon_details_collaps` | 33 |
| `angles-right` | fa-solid | `o_icon_forward` | 3 |
| `apple` | fa-brands | `o_icon_apple` | 5 |
| `archive` | fa-solid | `o_FileResource-IMSCP_icon` | 2 |
|  |  | `o_FileResource-SCORMCP_icon` | 3 |
|  |  | `o_cp_icon` | 8 |
|  |  | `o_scorm_icon` | 6 |
|  |  | `o_scorm_org` | 5 |
| `arrow-circle-left` | fa-solid | `o_icon_left` | 3 |
| `arrow-circle-right` | fa-solid | `o_icon_qual_ana_trend_arrow` | 3 |
|  |  | `o_icon_right` | 3 |
| `arrow-down` | fa-solid | `o_icon_element_after` | 2 |
| `arrow-right` | fa-solid | `o_icon_arrow_right` | 12 |
|  |  | `o_icon_qitem_status` | 2 |
|  |  | `o_membership_status_transfer` | 2 |
| `arrow-rotate-right` | fa-solid | `o_icon_certification_certifying` | 5 |
|  |  | `o_icon_recertification` | 3 |
| `arrow-up` | fa-solid | `o_icon_element_before` | 2 |
|  |  | `o_membership_status_parentbooking` | 2 |
| `arrow-up-right-dots` | fa-solid | `o_icon_progress` | 5 |
| `arrow-up-right-from-square` | fa-solid | `o_icon_arrow_up_right_from_square` | 13 |
| `arrows` | fa-solid | `o_icon_move` | 15 |
| `arrows-down-to-line` | fa-solid | `o_icon_tb_select_last` | 5 |
| `arrows-h` | fa-solid | `o_icon_eva_end_show` | 3 |
|  |  | `o_icon_spacer` | 5 |
| `arrows-rotate` | fa-solid | `o_icon_mix` | 4 |
| `arrows-turn-right` | fa-solid | `o_icon_cns` | 5 |
|  |  | `o_icon_shift` | 3 |
| `arrows-turn-to-dots` | fa-solid | `o_icon_assign_new_item` | 3 |
| `arrows-up-to-line` | fa-solid | `o_icon_tb_select_first` | 5 |
| `arrows-v` | fa-solid | `o_icon_node_up_down` | 3 |
|  |  | `o_icon_order` | 3 |
| `asterisk` | fa-solid | `o_ac_status_new_icon` | 6 |
|  |  | `o_forum_new_icon` | 5 |
|  |  | `o_icon_compulsory` | 4 |
|  |  | `o_icon_mandatory` | 12 |
|  |  | `o_icon_new` | 10 |
| `award` | fa-solid | `o_icon_badge` | 20 |
| `backward-step` | fa-solid | `o_icon_slide_backward` | 6 |
| `ban` | fa-solid | `o_CourseModule_icon_closed` | 7 |
|  |  | `o_ac_billing_address_inactive_icon` | 3 |
|  |  | `o_ac_offer_finished_icon` | 3 |
|  |  | `o_ac_offer_fully_booked_icon` | 4 |
|  |  | `o_forum_status_closed_icon` | 5 |
|  |  | `o_forum_status_opened_icon` | 5 |
|  |  | `o_forum_status_sticky_closed_icon` | 2 |
|  |  | `o_grader_inactive` | 5 |
|  |  | `o_icon_assessment_inspection_withdrawn` | 2 |
|  |  | `o_icon_ban` | 21 |
|  |  | `o_icon_building_status_inactive` | 2 |
|  |  | `o_icon_businessgroup_status_inactive` | 2 |
|  |  | `o_icon_cancelled` | 6 |
|  |  | `o_icon_certification_status_revoked` | 4 |
|  |  | `o_icon_check_disabled` | 6 |
|  |  | `o_icon_curriculum_status_finished` | 3 |
|  |  | `o_icon_deactivate` | 13 |
|  |  | `o_icon_identity_login_denied` | 3 |
|  |  | `o_icon_invitation_status_inactive` | 2 |
|  |  | `o_icon_proj_project_status_done` | 3 |
|  |  | `o_icon_qti_ended` | 4 |
|  |  | `o_icon_qual_ana_pres_delete` | 3 |
|  |  | `o_icon_qual_blacklist_add` | 3 |
|  |  | `o_icon_qual_gen_disabled` | 4 |
|  |  | `o_icon_qual_prev_blacklisted` | 3 |
|  |  | `o_icon_repo_status_closed` | 6 |
|  |  | `o_icon_status_not_ready` | 5 |
| `bank` | fa-solid | `o_icon_institution` | 4 |
|  |  | `o_icon_qpool` | 5 |
| `bar-chart` | fa-regular | `o_icon_statistics_tool` | 12 |
| `bars` | fa-solid | `o_icon_menuhandel` | 5 |
|  |  | `o_mi_qtiorder` | 4 |
| `bell` | fa-regular | `o_icon_reminder` | 12 |
|  |  | `o_icon_todo_priority_urgent` | 5 |
| `bold` | fa-solid | `o_bigbluebuttonmeeting_icon` | 3 |
|  |  | `o_icon_bold` | 3 |
| `bolt` | fa-solid | `o_icon_administrator` | 3 |
|  |  | `o_icon_assignment` | 12 |
|  |  | `o_icon_bolt` | 3 |
| `bolt-lightning` | fa-solid | `o_icon_bolt_lightning` | 6 |
| `bomb` | fa-solid | `o_icon_bomb` | 3 |
| `book` | fa-solid | `o_icon_lecture` | 26 |
|  |  | `o_icon_manual` | 7 |
| `book-open` | fa-solid | `o_icon_catalog_intern` | 10 |
| `bookmark` | fa-solid | `o_forum_marked_icon` | 3 |
|  |  | `o_icon_bookmark` | 21 |
|  |  | `o_icon_bookmark_add` | 21 |
|  |  | `o_icon_bookmark_header` | 18 |
|  |  | `o_icon_pool_favorits` | 3 |
|  |  | `o_portlet_bookmark_icon` | 2 |
| `box-archive` | fa-solid | `o_icon_certification_status_archived` | 3 |
| `boxes-packing` | fa-solid | `o_icon_coursearchive` | 10 |
| `briefcase` | fa-solid | `o_BinderTemplate_icon` | 2 |
|  |  | `o_ep_icon` | 10 |
|  |  | `o_icon_pf_binder` | 10 |
| `bug` | fa-solid | `o_icon_bug` | 3 |
|  |  | `o_icon_dev` | 4 |
| `bullhorn` | fa-solid | `o_FileResource-BLOG_icon` | 4 |
|  |  | `o_blog_icon` | 14 |
| `bullseye` | fa-solid | `o_icon_landingpage` | 3 |
|  |  | `o_icon_objectives` | 4 |
|  |  | `o_icon_proj_milestone` | 4 |
| `c` | fa-solid | `o_icon_c` | 3 |
| `calculator` | fa-solid | `o_icon_grade_scale` | 3 |
|  |  | `o_mi_qtinumerical` | 4 |
| `calendar` | fa-regular | `o_den_icon` | 7 |
|  |  | `o_icon_lifecycle_date` | 15 |
|  |  | `o_icon_proj_appointment` | 8 |
|  |  | `o_icon_qual_prev_regular` | 3 |
|  |  | `o_icon_timetable` | 2 |
| `calendar-check` | fa-regular | `o_appointment_icon` | 5 |
|  |  | `o_icon_events` | 10 |
| `calendar-day` | fa-solid | `o_icon_calendar_day` | 8 |
| `calendar-days` | fa-regular | `o_cal_icon` | 13 |
|  |  | `o_calendar_icon` | 4 |
|  |  | `o_icon_calendar` | 76 |
|  |  | `o_portlet_cal_icon` | 2 |
| `calendar-plus` | fa-solid | `o_icon_qual_prev_changed` | 3 |
| `caret-down` | fa-solid | `o_icon_caret` | 49 |
|  |  | `o_icon_close_togglebox` | 175 |
|  |  | `o_icon_close_tree` | 6 |
|  |  | `o_icon_provider_performx` | 3 |
|  |  | `o_mi_qtiinlinechoice` | 5 |
| `caret-left` | fa-solid | `o_icon_previous_toolbar` | 8 |
| `caret-right` | fa-solid | `o_icon_caret_right` | 5 |
|  |  | `o_icon_next_toolbar` | 8 |
|  |  | `o_icon_open_togglebox` | 176 |
|  |  | `o_icon_open_tree` | 6 |
| `cart-arrow-down` | fa-solid | `o_ac_order_pre` | 3 |
| `cart-shopping` | fa-solid | `o_ac_offer_bookable_icon` | 6 |
| `cc-paypal` | fa-brands | `o_ac_paypal_icon` | 4 |
| `certificate` | fa-solid | `o_icon_certificate` | 30 |
|  |  | `o_icon_certification_certified` | 5 |
|  |  | `o_portlet_eff_icon` | 2 |
| `chalkboard-user` | fa-solid | `o_icon_coaching_tool` | 8 |
| `chart-line` | fa-solid | `o_icon_radar_chart` | 3 |
| `chart-simple` | fa-solid | `o_icon_chart_simple` | 6 |
| `check` | fa-solid | `o_ac_billing_address_active_icon` | 3 |
|  |  | `o_ac_status_success_icon` | 6 |
|  |  | `o_icon_accept` | 11 |
|  |  | `o_icon_addremove_add` | 3 |
|  |  | `o_icon_assessment_inspection_carriedout` | 2 |
|  |  | `o_icon_building_status_active` | 2 |
|  |  | `o_icon_businessgroup_status_active` | 2 |
|  |  | `o_icon_certification_status_active` | 2 |
|  |  | `o_icon_certification_status_valid` | 2 |
|  |  | `o_icon_check` | 27 |
|  |  | `o_icon_correct_answer` | 9 |
|  |  | `o_icon_curriculum_status_active` | 2 |
|  |  | `o_icon_curriculum_status_confirmed` | 3 |
|  |  | `o_icon_immunity_proof_validated` | 3 |
|  |  | `o_icon_invitation_status_active` | 2 |
|  |  | `o_icon_line` | 3 |
|  |  | `o_icon_member_valid` | 6 |
|  |  | `o_icon_ms_done` | 2 |
|  |  | `o_icon_ok` | 22 |
|  |  | `o_icon_pf_entry_published` | 7 |
|  |  | `o_icon_presence` | 3 |
|  |  | `o_icon_progress_success` | 4 |
|  |  | `o_icon_proj_project_status_active` | 3 |
|  |  | `o_icon_qitem_finalVersion` | 4 |
|  |  | `o_icon_repo_status_published` | 4 |
|  |  | `o_icon_review_added` | 5 |
|  |  | `o_icon_select` | 6 |
|  |  | `o_icon_selected` | 4 |
|  |  | `o_icon_status_done` | 21 |
|  |  | `o_icon_submit` | 9 |
|  |  | `o_icon_tb_edit_enrollments` | 4 |
|  |  | `o_membership_status_finished` | 3 |
| `check-circle` | fa-regular | `o_grader_active` | 5 |
|  |  | `o_icon_activate` | 12 |
|  |  | `o_icon_cns_status_done` | 3 |
|  |  | `o_icon_correct_response` | 4 |
|  |  | `o_icon_dispensation_authorized` | 5 |
|  |  | `o_icon_notice_authorized` | 5 |
|  |  | `o_icon_passed` | 22 |
|  |  | `o_icon_proj_milestone_status_achieved` | 6 |
|  |  | `o_icon_qti_summary_correct` | 12 |
|  |  | `o_icon_qual_dc_finished` | 3 |
|  |  | `o_icon_qual_exec_participated` | 2 |
|  |  | `o_icon_quiz_single_choice_correct` | 6 |
|  |  | `o_icon_quiz_single_choice_on` | 10 |
|  |  | `o_icon_radio_on` | 4 |
|  |  | `o_icon_rubric_sufficient` | 6 |
|  |  | `o_icon_tb_broker_enrollment_done` | 4 |
|  |  | `o_icon_tb_selection_enrolled` | 4 |
|  |  | `o_icon_tb_selection_selected` | 3 |
|  |  | `o_icon_tb_topic_held` | 3 |
|  |  | `o_icon_todo_status_done` | 5 |
|  |  | `o_icon_toggle_button_on` | 3 |
|  |  | `o_midpub` | 6 |
| `check-square` | fa-regular | `o_cl_icon` | 7 |
|  |  | `o_grad_assignment_done` | 3 |
|  |  | `o_icon_calendar_enabled` | 2 |
|  |  | `o_icon_check_on` | 26 |
|  |  | `o_icon_checkbox_checked` | 4 |
|  |  | `o_icon_eva_mc` | 3 |
|  |  | `o_icon_pool_public` | 4 |
|  |  | `o_icon_quiz_multiple_choice_correct` | 6 |
|  |  | `o_icon_quiz_multiple_choice_on` | 6 |
|  |  | `o_icon_todo_task` | 27 |
|  |  | `o_mi_qtikprim` | 5 |
|  |  | `o_mi_qtimc` | 4 |
| `chevron-circle-left` | fa-solid | `o_icon_previous` | 13 |
| `chevron-circle-right` | fa-solid | `o_icon_next` | 13 |
| `chevron-down` | fa-solid | `o_icon_node_after` | 3 |
|  |  | `o_icon_slide_down` | 6 |
| `chevron-left` | fa-solid | `o_icon_back` | 23 |
|  |  | `o_icon_course_previous` | 5 |
| `chevron-right` | fa-solid | `o_icon_course_next` | 5 |
|  |  | `o_icon_curriculum_status_transition` | 3 |
|  |  | `o_icon_start` | 89 |
| `chevron-up` | fa-solid | `o_icon_node_before` | 3 |
|  |  | `o_icon_slide_up` | 6 |
|  |  | `o_icon_top` | 4 |
| `circle` | fa-solid | `o_black_led` | 7 |
|  |  | `o_green_led` | 6 |
|  |  | `o_grey_led` | 5 |
|  |  | `o_icon_circle` | 6 |
|  |  | `o_icon_circle_color` | 21 |
|  |  | `o_icon_courseareas` | 14 |
|  |  | `o_icon_disabled` | 8 |
|  |  | `o_icon_draw_ellipse` | 3 |
|  |  | `o_icon_enabled` | 2 |
|  |  | `o_icon_inheritance_none` | 3 |
|  |  | `o_icon_proj_milestone_status_open` | 3 |
|  |  | `o_icon_provider_tocco` | 3 |
|  |  | `o_icon_qti_answered` | 2 |
|  |  | `o_icon_qti_notAnswered` | 2 |
|  |  | `o_icon_qti_notPresented` | 4 |
|  |  | `o_icon_qti_summary_notAnswered` | 6 |
|  |  | `o_icon_qti_summary_notPresented` | 6 |
|  |  | `o_icon_qual_blacklist_remove` | 9 |
|  |  | `o_icon_quiz_single_choice_off` | 10 |
|  |  | `o_icon_radio_off` | 4 |
|  |  | `o_icon_read` | 4 |
|  |  | `o_icon_status_available` | 18 |
|  |  | `o_icon_status_not_started` | 5 |
|  |  | `o_icon_tb_broker_not_started` | 3 |
|  |  | `o_icon_tb_strategy_max_topics` | 3 |
|  |  | `o_icon_tb_topics` | 7 |
|  |  | `o_icon_to_read` | 4 |
|  |  | `o_icon_todo_priority_medium` | 5 |
|  |  | `o_icon_todo_status_open` | 3 |
|  |  | `o_icon_toggle` | 4 |
|  |  | `o_icon_toggle_button_off` | 6 |
|  |  | `o_icon_videotask` | 10 |
|  |  | `o_lectures_absent` | 12 |
|  |  | `o_lectures_attended` | 8 |
|  |  | `o_lectures_authorized` | 8 |
|  |  | `o_lectures_closed` | 3 |
|  |  | `o_lectures_current` | 5 |
|  |  | `o_lectures_dispensed` | 8 |
|  |  | `o_lectures_pending` | 5 |
|  |  | `o_lectures_rollcall_danger` | 11 |
|  |  | `o_lectures_rollcall_free` | 7 |
|  |  | `o_lectures_rollcall_notice` | 5 |
|  |  | `o_lectures_rollcall_ok` | 9 |
|  |  | `o_projectbroker_icon` | 7 |
|  |  | `o_red_led` | 7 |
|  |  | `o_yellow_led` | 6 |
| `circle-arrow-down` | fa-solid | `o_icon_load_more` | 3 |
|  |  | `o_icon_proj_timeline_earlier` | 3 |
| `circle-arrow-up` | fa-solid | `o_icon_proj_timeline_later` | 3 |
| `circle-check` | fa-solid | `o_ac_order_status_payed_icon` | 4 |
|  |  | `o_icon_absence_authorized` | 5 |
|  |  | `o_icon_certification_status_certified` | 2 |
|  |  | `o_icon_circle_check` | 5 |
|  |  | `o_membership_status_active` | 5 |
| `circle-dot` | fa-regular | `o_icon_selected_dot` | 7 |
| `circle-down` | fa-regular | `o_icon_inheritance_inherited` | 4 |
|  |  | `o_icon_inheritance_root` | 4 |
| `circle-exclamation` | fa-solid | `o_ac_offer_overbooked_icon` | 3 |
|  |  | `o_icon_circle_exclamation` | 5 |
|  |  | `o_icon_recertification_error` | 8 |
|  |  | `o_icon_validation_error` | 7 |
| `circle-half-stroke` | fa-solid | `o_ac_offer_almost_fully_booked_icon` | 3 |
| `circle-info` | fa-solid | `o_icon_circle_info` | 7 |
|  |  | `o_icon_metadata` | 3 |
| `circle-minus` | fa-solid | `o_as_mode_closed` | 3 |
|  |  | `o_icon_invalidate` | 9 |
|  |  | `o_icon_tb_selection_surplus` | 3 |
| `circle-notch` | fa-solid | `o_icon_wait` | 3 |
| `circle-play` | fa-solid | `o_icon_cns_status_in_progress` | 3 |
|  |  | `o_icon_curriculum_implementation_avatar` | 3 |
|  |  | `o_icon_tb_broker_selection_in_progress` | 3 |
| `circle-plus` | fa-solid | `o_ac_order_status_new_icon` | 2 |
|  |  | `o_icon_qitem_new` | 3 |
| `circle-radiation` | fa-solid | `o_icon_circle_radiation` | 3 |
| `circle-stop` | fa-solid | `o_icon_assessment_inspection_cancelled` | 2 |
|  |  | `o_icon_cancel` | 9 |
| `circle-xmark` | fa-solid | `o_ac_order_status_canceled_icon` | 4 |
|  |  | `o_ac_order_status_error_icon` | 3 |
|  |  | `o_icon_certification_status_removed` | 2 |
|  |  | `o_icon_circle_xmark` | 7 |
|  |  | `o_icon_curriculum_status_cancelled` | 3 |
|  |  | `o_icon_error` | 77 |
|  |  | `o_icon_quiz` | 8 |
|  |  | `o_icon_tb_topic_not_held` | 3 |
|  |  | `o_membership_status_cancel` | 3 |
|  |  | `o_membership_status_cancelwithfee` | 3 |
|  |  | `o_membership_status_declined` | 3 |
|  |  | `o_membership_status_removed` | 4 |
| `clipboard` | fa-regular | `o_icon_form` | 4 |
|  |  | `o_icon_memo` | 5 |
| `clipboard-check` | fa-solid | `o_icon_view_all_rubrics` | 3 |
| `clipboard-list` | fa-solid | `o_icon_info_list` | 4 |
|  |  | `o_icon_tb_enrollments` | 5 |
|  |  | `o_icon_tb_strategy_max_enrollments` | 3 |
|  |  | `o_icon_topicbroker` | 9 |
| `clipboard-question` | fa-solid | `o_icon_qual_prev_data_collection` | 3 |
|  |  | `o_icon_qual_preview` | 7 |
| `clock` | fa-solid | `o_ac_offer_pending_icon` | 4 |
|  |  | `o_ac_status_waiting_icon` | 5 |
|  |  | `o_as_mode_none` | 3 |
|  |  | `o_grader_absence` | 5 |
|  |  | `o_icon_absence_leave` | 4 |
|  |  | `o_icon_assessment_inspection_scheduled` | 4 |
|  |  | `o_icon_change_notifications_settings` | 3 |
|  |  | `o_icon_expenditure` | 5 |
|  |  | `o_icon_extra_time` | 30 |
|  |  | `o_icon_identity_pending` | 3 |
|  |  | `o_icon_pf_history` | 4 |
|  |  | `o_icon_time` | 29 |
|  |  | `o_icon_timelimit` | 20 |
|  |  | `o_icon_visitingcard.o_icon_waiting` | 2 |
|  |  | `o_lectures_next` | 3 |
|  |  | `o_lectures_rollcall_` | 4 |
|  |  | `o_membership_status_booking` | 4 |
| `clock-rotate-left` | fa-solid | `o_icon_certification_status_expired` | 2 |
|  |  | `o_icon_history` | 7 |
| `clone` | fa-solid | `o_icon_duplicate` | 7 |
|  |  | `o_mi_qtimatch_draganddrop` | 4 |
| `cloud` | fa-solid | `o_icon_onedrive` | 5 |
|  |  | `o_icon_provider_oauth` | 7 |
|  |  | `o_icon_provider_panther` | 3 |
| `code` | fa-solid | `o_icon_add_html` | 2 |
|  |  | `o_icon_code` | 8 |
| `code-branch` | fa-solid | `o_icon_code_branch` | 3 |
| `code-fork` | fa-solid | `o_icon_branch` | 7 |
| `cog` | fa-solid | `o_icon_inspect` | 4 |
| `coins` | fa-solid | `o_icon_coins` | 10 |
| `columns` | fa-solid | `o_icon_columns` | 2 |
|  |  | `o_icon_container` | 4 |
| `comment` | fa-regular | `o_forum_message_icon` | 3 |
|  |  | `o_icon_chat` | 12 |
|  |  | `o_icon_comments_none` | 7 |
|  |  | `o_icon_post` | 3 |
|  |  | `o_icon_status_chat` | 8 |
|  |  | `o_portlet_infomessages_icon` | 2 |
| `comment-sms` | fa-solid | `o_icon_comment_sms` | 2 |
| `comments` | fa-regular | `o_fo_icon` | 12 |
|  |  | `o_forum_status_sticky_icon` | 3 |
|  |  | `o_forum_status_thread_icon` | 12 |
|  |  | `o_icon_chats` | 5 |
|  |  | `o_icon_comments` | 12 |
| `compass` | fa-regular | `o_icon_compass` | 3 |
| `compass-drafting` | fa-solid | `o_icon_courseplanner` | 4 |
| `compress` | fa-solid | `o_icon_compress` | 3 |
|  |  | `o_icon_width_collapse` | 3 |
| `copy` | fa-solid | `o_icon_copy` | 54 |
|  |  | `o_icon_files` | 15 |
|  |  | `o_icon_qitem_copy` | 3 |
|  |  | `o_icon_replace` | 2 |
|  |  | `o_icon_taxonomy_templates` | 6 |
| `copyright` | fa-solid | `o_icon_lic_all_rights_reserved` | 4 |
|  |  | `o_icon_lic_freetext` | 4 |
|  |  | `o_icon_lic_general` | 4 |
| `crosshairs` | fa-solid | `o_icon_crosshairs` | 3 |
| `cube` | fa-solid | `o_icon_courserun` | 5 |
|  |  | `o_icon_curriculum_element` | 34 |
|  |  | `o_icon_taxonomy` | 10 |
| `cubes` | fa-solid | `o_icon_curriculum` | 24 |
|  |  | `o_icon_taxonomy_level` | 5 |
|  |  | `o_icon_mi_qtisection` | 10 |
|  |  | `o_portlet_repository_student_icon` | 2 |
|  |  | `o_st_icon` | 8 |
| `cubes-stacked` | fa-solid | `o_icon_course_bundle` | 5 |
|  |  | `o_icon_resources` | 3 |
| `database` | fa-solid | `o_icon_coursedb` | 4 |
|  |  | `o_icon_database` | 4 |
|  |  | `o_icon_quota` | 3 |
|  |  | `o_icon_sharepoint_drive` | 5 |
|  |  | `o_mi_qpool_import` | 6 |
| `delicious` | fa-brands | `o_icon_delicious` | 4 |
| `diagram-project` | fa-solid | `o_icon_diagram_project` | 3 |
| `digg` | fa-brands | `o_icon_digg` | 4 |
| `door-open` | fa-solid | `o_ac_openaccess_icon` | 9 |
| `dot-circle` | fa-regular | `o_icon_eva_sc` | 5 |
|  |  | `o_icon_eva_sc` | 5 |
|  |  | `o_icon_passed_undefined` | 8 |
|  |  | `o_icon_status_dnd` | 15 |
|  |  | `o_mi_qtisc` | 4 |
| `download` | fa-solid | `o_icon_archive_tool` | 7 |
|  |  | `o_icon_download` | 83 |
|  |  | `o_icon_eva_export` | 3 |
|  |  | `o_icon_qitem_export` | 3 |
|  |  | `o_icon_qual_ana_export` | 3 |
| `edit` | fa-solid | `o_icon_courseeditor` | 3 |
|  |  | `o_icon_edit` | 181 |
|  |  | `o_icon_edit_file` | 3 |
|  |  | `o_icon_inline_editable` | 3 |
|  |  | `o_icon_qual_dc_preparation` | 3 |
|  |  | `o_icon_readonly` | 5 |
|  |  | `o_icon_readwrite` | 3 |
| `ellipsis` | fa-solid | `o_icon_breadcrumb_more` | 3 |
| `ellipsis-h` | fa-solid | `o_icon_pageing` | 2 |
|  |  | `o_mi_qtifib` | 5 |
| `ellipsis-v` | fa-solid | `o_icon_actions` | 52 |
|  |  | `o_icon_commands` | 13 |
| `envelope` | fa-regular | `o_co_icon` | 10 |
|  |  | `o_icon_mail` | 79 |
|  |  | `o_icon_message` | 5 |
|  |  | `o_icon_send` | 3 |
| `envelope-open` | fa-solid | `o_icon_message_open` | 7 |
| `envelope-open-text` | fa-solid | `o_icon_tb_notification` | 4 |
| `envelope-square` | fa-solid | `o_icon_mailto` | 3 |
| `eraser` | fa-solid | `o_icon_eraser` | 3 |
|  |  | `o_icon_tb_unselect` | 4 |
|  |  | `o_middel` | 4 |
| `exchange` | fa-solid | `o_icon_qitem_convert` | 3 |
|  |  | `o_icon_role` | 2 |
| `exclamation` | fa-solid | `o_icon_exclamation` | 3 |
|  |  | `o_icon_not_available` | 6 |
|  |  | `o_icon_todo_priority_high` | 5 |
| `exclamation-circle` | fa-solid | `o_absences_col_alert` | 3 |
|  |  | `o_grad_assignment_unassigned` | 5 |
|  |  | `o_icon_absence_unauthorized` | 5 |
|  |  | `o_icon_exclamation_circle` | 3 |
|  |  | `o_icon_info_msg` | 17 |
|  |  | `o_icon_qti_invalid` | 4 |
|  |  | `o_icon_rubric_neutral` | 6 |
|  |  | `o_miderr` | 9 |
| `exclamation-triangle` | fa-solid | `o_ac_order_status_warning_icon` | 3 |
|  |  | `o_icon_dispensation_unauthorized` | 5 |
|  |  | `o_icon_important` | 32 |
|  |  | `o_icon_member_not_valid` | 6 |
|  |  | `o_icon_notice_unauthorized` | 5 |
|  |  | `o_icon_warn` | 79 |
|  |  | `o_icon_warning` | 12 |
|  |  | `o_midwarn` | 14 |
| `expand` | fa-solid | `o_icon_expand` | 3 |
|  |  | `o_icon_width_expand` | 3 |
| `external-link` | fa-solid | `o_FileResource-SHAREDFOLDER` | 2 |
|  |  | `o_icon_content_popup` | 11 |
|  |  | `o_icon_external_link` | 29 |
|  |  | `o_icon_link_extern` | 13 |
|  |  | `o_tu_icon` | 6 |
| `eye` | fa-solid | `o_ac_offer_active_icon` | 5 |
|  |  | `o_forum_one_icon` | 3 |
|  |  | `o_forum_status_visible_icon` | 5 |
|  |  | `o_icon_curriculum_manager` | 3 |
|  |  | `o_icon_eye` | 11 |
|  |  | `o_icon_master_coach` | 3 |
|  |  | `o_icon_preview` | 54 |
|  |  | `o_icon_principal` | 3 |
|  |  | `o_icon_qti_review` | 4 |
|  |  | `o_icon_quickview` | 5 |
|  |  | `o_icon_results_visible` | 20 |
| `eye-slash` | fa-solid | `o_ac_offer_inactive_icon` | 5 |
|  |  | `o_ac_offer_not_available_icon` | 3 |
|  |  | `o_forum_status_hidden_icon` | 5 |
|  |  | `o_icon_eye_slash` | 3 |
|  |  | `o_icon_pf_section_draft` | 6 |
|  |  | `o_icon_qti_reviewInvalid` | 4 |
|  |  | `o_icon_results_hidden` | 26 |
| `face-frown-open` | fa-solid | `o_icon_qti_incorrect` | 4 |
| `face-smile-beam` | fa-solid | `o_icon_qti_correct` | 4 |
| `facebook` | fa-brands | `o_icon_provider_facebook` | 6 |
| `facebook-square` | fa-brands | `o_icon_facebook` | 5 |
| `feather-pointed` | fa-solid | `o_icon_authoring` | 4 |
| `file` | fa-regular | `o_FileResource-FILE_icon` | 2 |
|  |  | `o_dialog_icon` | 14 |
|  |  | `o_filetype_dwb` | 2 |
|  |  | `o_filetype_ico` | 3 |
|  |  | `o_icon_file` | 5 |
|  |  | `o_icon_fileupload` | 3 |
|  |  | `o_icon_inspection` | 10 |
|  |  | `o_icon_pf_entry` | 5 |
|  |  | `o_icon_pf_page` | 10 |
|  |  | `o_icon_proj_file` | 7 |
|  |  | `o_scorm_item` | 5 |
| `file-archive` | fa-regular | `o_filetype_tgz` | 3 |
| `file-arrow-up` | fa-solid | `o_icon_file_arrow_up` | 3 |
| `file-audio` | fa-regular | `o_FileResource-SOUND_icon` | 2 |
|  |  | `o_filetype_wav` | 3 |
| `file-circle-plus` | fa-solid | `o_icon_filehub_add` | 8 |
| `file-circle-xmark` | fa-solid | `o_ac_order_status_written_off_icon` | 5 |
| `file-code` | fa-regular | `o_filetype_sh` | 2 |
|  |  | `o_filetype_xsl` | 3 |
|  |  | `o_icon_qti_signature` | 3 |
|  |  | `o_icon_translation_item` | 6 |
| `file-excel` | fa-regular | `o_FileResource-XLS_icon` | 4 |
|  |  | `o_filetype_xlsx` | 6 |
| `file-export` | fa-solid | `o_icon_file_export` | 3 |
| `file-image` | fa-regular | `o_FileResource-IMAGE_icon` | 2 |
|  |  | `o_filetype_jpg` | 4 |
|  |  | `o_icon_layout` | 3 |
| `file-lines` | fa-solid | `o_icon_courselog` | 5 |
|  |  | `o_icon_file_lines` | 3 |
| `file-pdf` | fa-regular | `o_FileResource-PDF_icon` | 2 |
|  |  | `o_filetype_pdf` | 41 |
|  |  | `o_icon_eva_pdf` | 4 |
|  |  | `o_icon_qual_ana_pdf` | 3 |
|  |  | `o_icon_tool_pdf` | 5 |
| `file-powerpoint` | fa-regular | `o_FileResource-PPT_icon` | 4 |
|  |  | `o_filetype_pptx` | 3 |
| `file-text` | fa-regular | `o_cp_item` | 5 |
|  |  | `o_filetype_html` | 10 |
|  |  | `o_icon_log` | 14 |
|  |  | `o_icon_new_document` | 3 |
|  |  | `o_page_icon` | 10 |
|  |  | `o_sp_icon` | 8 |
| `file-video` | fa-regular | `o_FileResource-ANIM_icon` | 2 |
|  |  | `o_FileResource-MOVIE_icon` | 4 |
|  |  | `o_filetype_flv` | 2 |
| `file-word` | fa-regular | `o_FileResource-DOC_icon` | 4 |
|  |  | `o_filetype_docx` | 3 |
| `film` | fa-solid | `o_FileResource-VIDEO_icon` | 3 |
|  |  | `o_icon_video` | 22 |
|  |  | `o_video_icon` | 8 |
| `filter` | fa-solid | `o_icon_filter` | 5 |
| `fire` | fa-solid | `o_icon_fire` | 3 |
|  |  | `o_mi_qtihottext` | 4 |
| `flag-checkered` | fa-solid | `o_icon_finished` | 3 |
| `flask` | fa-solid | `o_icon_banned` | 5 |
|  |  | `o_icon_flask` | 3 |
| `floppy-disk` | fa-regular | `o_icon_qti_end_testpart` | 3 |
| `folder` | fa-solid | `o_filetype_folder` | 20 |
|  |  | `o_icon_catalog_sub` | 5 |
|  |  | `o_icon_coursefolder` | 6 |
| `folder-open` | fa-regular | `o_FileResource-SHAREDFOLDER_icon` | 5 |
|  |  | `o_bc_icon` | 10 |
|  |  | `o_icon_mediacenter` | 4 |
|  |  | `o_icon_taxonomy_level_leaf` | 3 |
|  |  | `o_icon_translation_package` | 5 |
| `folder-plus` | fa-solid | `o_icon_new_folder` | 5 |
| `font` | fa-solid | `o_icon_text` | 4 |
| `forward-step` | fa-solid | `o_icon_slide_forward` | 6 |
| `gauge` | fa-solid | `o_icon_reviews` | 4 |
| `gavel` | fa-solid | `o_icon_proj_decision` | 8 |
| `gear` | fa-solid | `o_icon_customize` | 6 |
|  |  | `o_icon_edit_metadata` | 7 |
|  |  | `o_icon_gear` | 4 |
|  |  | `o_icon_tb_configuration` | 3 |
|  |  | `o_icon_tool` | 3 |
| `gears` | fa-solid | `o_icon_qitem_commands` | 3 |
|  |  | `o_icon_settings` | 8 |
|  |  | `o_icon_tb_method_auto` | 3 |
|  |  | `o_icon_tb_strategy` | 4 |
|  |  | `o_icon_tb_strategy_custom` | 3 |
| `gift` | fa-solid | `o_ac_free_icon` | 3 |
| `globe` | fa-solid | `o_FileResource-WIKI_icon` | 2 |
|  |  | `o_icon_catalog_extern` | 11 |
|  |  | `o_icon_globe` | 4 |
|  |  | `o_icon_language` | 10 |
|  |  | `o_icon_origin` | 5 |
|  |  | `o_wiki_icon` | 12 |
| `google` | fa-brands | `o_icon_provider_google` | 6 |
| `google-plus-square` | fa-brands | `o_icon_google` | 4 |
| `graduation-cap` | fa-solid | `o_FileResource-GLOSSARY_icon` | 5 |
|  |  | `o_icon_coach` | 11 |
|  |  | `o_icon_graduate` | 3 |
|  |  | `o_icon_repo_status_coachpublished` | 2 |
|  |  | `o_icon_user_vip` | 7 |
|  |  | `o_portlet_repository_teacher_icon` | 2 |
| `hand` | fa-regular | `o_icon_abstain` | 5 |
| `hand-back-fist` | fa-solid | `o_icon_pull` | 6 |
| `hand-point-right` | fa-solid | `o_icon_instruction` | 4 |
| `hand-point-up` | fa-solid | `o_icon_cns_status_selected` | 3 |
|  |  | `o_icon_hand_point_up` | 4 |
|  |  | `o_icon_tb_broker_enrollment_in_progress` | 3 |
| `hands-clapping` | fa-solid | `o_icon_qual_part_not_available` | 2 |
| `handshake` | fa-regular | `o_icon_disclaimer` | 10 |
| `hashtag` | fa-solid | `o_icon_number_of` | 3 |
| `hdd` | fa-regular | `o_icon_hdd` | 4 |
| `header` | fa-solid | `o_icon_header` | 6 |
| `heart` | fa-solid | `o_icon_heart` | 3 |
| `highlighter` | fa-solid | `o_icon_correction` | 12 |
|  |  | `o_icon_status_in_review` | 15 |
| `history` | fa-solid | `o_icon_version` | 9 |
| `home` | fa-solid | `o_icon_home` | 17 |
| `hourglass` | fa-solid | `o_icon_curriculum_status_provisional` | 3 |
|  |  | `o_icon_qual_part_participated` | 4 |
|  |  | `o_icon_tb_selection_waiting_list` | 3 |
| `hourglass-end` | fa-solid | `o_as_mode_followup` | 3 |
|  |  | `o_as_mode_leadtime` | 3 |
|  |  | `o_icon_timelimit_end` | 2 |
| `hourglass-half` | fa-regular | `o_ac_membership_confirmation_icon` | 4 |
|  |  | `o_ac_order_status_inprocess_icon` | 3 |
|  |  | `o_ac_order_status_open_icon` | 3 |
|  |  | `o_ac_order_status_pending_icon` | 4 |
|  |  | `o_ac_order_status_prepayment_icon` | 3 |
|  |  | `o_icon_candidate` | 3 |
|  |  | `o_icon_payment_open` | 5 |
|  |  | `o_icon_timelimit_half` | 5 |
|  |  | `o_membership_status_pending` | 5 |
|  |  | `o_membership_status_reservation` | 2 |
| `hourglass-start` | fa-solid | `o_icon_timelimit_start` | 4 |
| `house` | fa-solid | `o_icon_breadcrumb_root` | 3 |
| `html5` | fa-brands | `o_icon_html5` | 5 |
| `image` | fa-solid | `o_icon_image` | 9 |
|  |  | `o_icon_image_comparison` | 11 |
|  |  | `o_icon_media` | 9 |
| `images` | fa-solid | `o_icon_images` | 3 |
| `inbox` | fa-solid | `o_pf_icon` | 5 |
| `infinity` | fa-solid | `o_icon_openolat` | 4 |
|  |  | `o_icon_provider_olat` | 6 |
| `info-circle` | fa-solid | `o_icon_description` | 23 |
|  |  | `o_icon_impress` | 7 |
|  |  | `o_icon_info` | 44 |
|  |  | `o_icon_info_ap` | 7 |
|  |  | `o_icon_info_badge` | 5 |
|  |  | `o_icon_info_resource` | 5 |
|  |  | `o_icon_news` | 5 |
|  |  | `o_infomsg_icon` | 14 |
|  |  | `o_portlet_infomsg_icon` | 2 |
| `institution` | fa-solid | `o_portlet_institutions_icon` | 2 |
| `italic` | fa-solid | `o_icon_italic` | 3 |
| `k` | fa-solid | `o_icon_k` | 3 |
| `key` | fa-solid | `o_ac_token_icon` | 6 |
|  |  | `o_icon_owner` | 5 |
| `keyboard` | fa-regular | `o_icon_keyboard` | 3 |
| `laptop` | fa-solid | `o_icon_assessment_mode` | 23 |
| `leaf` | fa-solid | `o_icon_instructional_design` | 4 |
|  |  | `o_icon_proj_project` | 14 |
| `level-up` | fa-solid | `o_icon_reactivate` | 3 |
| `lightbulb` | fa-regular | `o_icon_details` | 22 |
|  |  | `o_icon_lightbulb` | 4 |
|  |  | `o_icon_qti_solution` | 2 |
|  |  | `o_portlet_dyk_icon` | 2 |
| `line-chart` | fa-solid | `o_icon_qual_ana_trend` | 4 |
| `link` | fa-solid | `o_icon_link` | 23 |
|  |  | `o_icon_link` | 23 |
|  |  | `o_icon_proj_reference` | 3 |
|  |  | `o_ll_icon` | 6 |
|  |  | `o_portlet_links_icon` | 2 |
| `linkedin` | fa-brands | `o_icon_linkedin` | 11 |
|  |  | `o_icon_linkedin` | 11 |
| `linkedin-in` | fa-brands | `o_icon_provider_linkedin` | 6 |
| `list` | fa-solid | `o_icon_list` | 7 |
|  |  | `o_icon_pool_collection` | 5 |
| `list-check` | fa-solid | `o_icon_list_check` | 3 |
| `list-ol` | fa-solid | `o_icon_list_num` | 6 |
|  |  | `o_mi_qtimatch_truefalse` | 4 |
| `location-crosshairs` | fa-solid | `o_icon_exact_location` | 7 |
| `location-dot` | fa-solid | `o_icon_location` | 19 |
| `lock` | fa-solid | `o_ac_membersonly_icon` | 5 |
|  |  | `o_icon_identity_permanent` | 3 |
|  |  | `o_icon_locked` | 14 |
|  |  | `o_icon_password` | 8 |
|  |  | `o_icon_pf_entry_closed` | 6 |
|  |  | `o_icon_pf_section_closed` | 6 |
|  |  | `o_icon_tb_group_restrictions` | 3 |
|  |  | `o_midlock` | 7 |
| `long-arrow-right` | fa-solid | `o_icon_eva_end_hide` | 3 |
|  |  | `o_icon_todo_date_range` | 3 |
| `magic` | fa-solid | `o_icon_wizard` | 5 |
| `magnifying-glass` | fa-solid | `o_icon_magnifying_glass` | 6 |
| `magnifying-glass-plus` | fa-solid | `o_icon_search_lookup` | 3 |
| `mail-reply` | fa-solid | `o_icon_node_under` | 5 |
| `map` | fa-regular | `o_mi_qtihotspot` | 4 |
| `map-signs` | fa-solid | `o_icon_learning_path` | 10 |
|  |  | `o_midlpexob` | 6 |
| `medal` | fa-solid | `o_icon_statement` | 5 |
|  |  | `o_icon_success_status` | 8 |
| `meh` | fa-regular | `o_FileResource-SURVEY_icon` | 2 |
|  |  | `o_iqsurv_icon` | 7 |
| `microphone` | fa-solid | `o_icon_audio_record` | 10 |
| `minus` | fa-solid | `o_ac_status_canceled_icon` | 6 |
|  |  | `o_icon_minus` | 4 |
|  |  | `o_icon_not_identified` | 3 |
|  |  | `o_icon_table_details_collaps` | 4 |
| `minus-circle` | fa-solid | `o_icon_delete` | 36 |
|  |  | `o_icon_member_skipped` | 6 |
| `minus-square` | fa-regular | `o_icon_check_mixed` | 4 |
|  |  | `o_icon_review_remove` | 2 |
| `mobile` | fa-solid | `o_icon_mobile` | 3 |
| `money-bill-1` | fa-solid | `o_icon_pay` | 5 |
| `mouse-pointer` | fa-solid | `o_icon_pointer` | 3 |
| `n` | fa-solid | `o_icon_tb_selection_not_enrolled` | 3 |
| `navicon` | fa-solid | `o_icon_pf_section` | 9 |
| `openid` | fa-brands | `o_icon_provider_openid` | 5 |
| `paint-brush` | fa-solid | `o_icon_brush` | 3 |
|  |  | `o_icon_proj_whiteboard` | 3 |
|  |  | `o_mi_qtidrawing` | 4 |
| `paper-plane` | fa-regular | `o_icon_show_send` | 6 |
|  |  | `o_portlet_quickstart_icon` | 2 |
| `paperclip` | fa-solid | `o_icon_paperclip` | 3 |
| `paragraph` | fa-solid | `o_icon_paragraph` | 2 |
| `pause` | fa-solid | `o_icon_certification_status_inactive` | 2 |
|  |  | `o_icon_qti_suspend` | 4 |
| `pause-circle` | fa-regular | `o_icon_identity_inactive` | 4 |
| `pen` | fa-solid | `o_icon_curriculum_status_preparation` | 3 |
| `pencil` | fa-solid | `o_icon_changes` | 7 |
|  |  | `o_icon_new_portfolio` | 16 |
|  |  | `o_icon_overridden` | 4 |
|  |  | `o_icon_pencil` | 5 |
|  |  | `o_icon_pf_entry_draft` | 6 |
|  |  | `o_icon_pf_new_entry` | 3 |
|  |  | `o_icon_qitem_draft` | 4 |
|  |  | `o_icon_rename` | 3 |
|  |  | `o_icon_repo_status_preparation` | 2 |
| `pencil-square` | fa-solid | `o_FileResource-IMSQTI21_icon` | 6 |
|  |  | `o_FileResource-TEST_icon` | 3 |
|  |  | `o_iqself_icon` | 5 |
|  |  | `o_iqtest_icon` | 7 |
|  |  | `o_qtiassessment_icon` | 14 |
| `people-group` | fa-solid | `o_icon_people` | 6 |
| `person-chalkboard` | fa-solid | `o_icon_room_management` | 3 |
| `person-circle-minus` | fa-solid | `o_icon_non_members` | 3 |
| `person-rays` | fa-solid | `o_icon_provider_guest` | 5 |
| `phone` | fa-solid | `o_icon_phone` | 4 |
| `play` | fa-solid | `o_icon_assessment_inspection_active` | 4 |
|  |  | `o_icon_certification_resume` | 2 |
|  |  | `o_icon_ms_pending` | 2 |
|  |  | `o_icon_play` | 4 |
|  |  | `o_icon_qual_part_execute` | 4 |
|  |  | `o_icon_status_in_progress` | 9 |
|  |  | `o_icon_tb_run_start` | 4 |
|  |  | `o_icon_video_play` | 7 |
|  |  | `o_icon_video_resume` | 3 |
| `play-circle` | fa-regular | `o_icon_qual_dc_ready` | 3 |
|  |  | `o_icon_qual_dc_running` | 3 |
|  |  | `o_icon_qual_exec_participating` | 2 |
|  |  | `o_icon_qual_exec_ready` | 2 |
| `plus` | fa-solid | `o_icon_not_correct_plus` | 5 |
|  |  | `o_icon_plus` | 7 |
|  |  | `o_icon_table_details_expand` | 5 |
| `plus-circle` | fa-solid | `o_icon_add` | 216 |
|  |  | `o_icon_lic_add` | 3 |
|  |  | `o_icon_qual_dc_create` | 3 |
|  |  | `o_icon_qual_gen_ce_add` | 3 |
|  |  | `o_icon_qual_gen_create` | 3 |
|  |  | `o_icon_qual_gen_re_add` | 3 |
| `plus-square` | fa-solid | `o_icon_review_add` | 2 |
| `podcast` | fa-solid | `o_FileResource-PODCAST_icon` | 2 |
|  |  | `o_podcast_icon` | 12 |
| `power-off` | fa-solid | `o_icon_close_resource` | 4 |
|  |  | `o_icon_lifecycle` | 2 |
| `print` | fa-solid | `o_icon_eva_print` | 4 |
|  |  | `o_icon_print` | 23 |
|  |  | `o_icon_private` | 2 |
|  |  | `o_icon_qual_ana_print` | 4 |
| `puzzle-piece` | fa-solid | `o_icon_eportfolio_add` | 7 |
|  |  | `o_icon_eportfolio_link` | 2 |
| `q` | fa-solid | `o_icon_q` | 3 |
| `qrcode` | fa-solid | `o_icon_qrcode` | 23 |
| `question` | fa-solid | `o_icon_immunity_proof_claimed` | 3 |
|  |  | `o_icon_question` | 5 |
|  |  | `o_icon_unselected` | 2 |
|  |  | `o_icon_user_anonymous` | 5 |
| `question-circle` | fa-solid | `o_icon_help` | 53 |
|  |  | `o_icon_qti_hint` | 3 |
| `quote-left` | fa-solid | `o_icon_citation` | 6 |
| `quote-right` | fa-solid | `o_icon_quote_right` | 3 |
| `radiation` | fa-solid | `o_icon_radiation` | 2 |
| `random` | fa-solid | `o_icon_shuffle` | 9 |
| `receipt` | fa-solid | `o_ac_invoice_icon` | 3 |
| `recycle` | fa-solid | `o_icon_recycle` | 7 |
| `refresh` | fa-solid | `o_grad_assignment_inprocess` | 3 |
|  |  | `o_icon_calendar_sync` | 4 |
|  |  | `o_icon_extend` | 4 |
|  |  | `o_icon_pf_section_progress` | 6 |
|  |  | `o_icon_proj_recurrence` | 3 |
|  |  | `o_icon_refresh` | 33 |
|  |  | `o_icon_response_feedback` | 2 |
|  |  | `o_icon_update` | 3 |
| `repeat` | fa-solid | `o_icon_qual_gen_enabled` | 4 |
|  |  | `o_icon_redo` | 4 |
|  |  | `o_icon_video_replay` | 3 |
| `reply` | fa-solid | `o_icon_reopen` | 8 |
|  |  | `o_icon_reply` | 4 |
| `reply-all` | fa-solid | `o_icon_reply_with_quote` | 3 |
| `retweet` | fa-solid | `o_icon_managed` | 11 |
| `right-left` | fa-solid | `o_icon_right_left` | 3 |
| `rotate-left` | fa-solid | `o_icon_attempts` | 4 |
|  |  | `o_icon_pf_entry_revision` | 6 |
|  |  | `o_icon_qitem_revised` | 4 |
|  |  | `o_icon_revoke` | 3 |
|  |  | `o_icon_tb_withdraw` | 7 |
| `rotate-right` | fa-solid | `o_icon_certification_status_recertifying` | 3 |
|  |  | `o_icon_retry` | 8 |
|  |  | `o_icon_tb_enroll` | 4 |
|  |  | `o_icon_tb_run` | 3 |
| `rss` | fa-solid | `o_icon_notification` | 8 |
|  |  | `o_icon_rss` | 12 |
|  |  | `o_icon_rss_unsubscribe` | 4 |
|  |  | `o_portlet_noti_icon` | 2 |
| `s` | fa-solid | `o_icon_s` | 3 |
| `save` | fa-solid | `o_icon_save` | 6 |
| `scale-balanced` | fa-solid | `o_icon_tb_priority` | 4 |
|  |  | `o_icon_tb_strategy_max_priorities` | 3 |
| `scale-unbalanced-flip` | fa-solid | `o_icon_score_unbalanced` | 5 |
| `scroll` | fa-solid | `o_icon_activity_log` | 3 |
| `search` | fa-solid | `o_icon_empty_indicator` | 10 |
|  |  | `o_icon_search` | 51 |
| `search-minus` | fa-solid | `o_icon_shrink` | 3 |
| `search-plus` | fa-solid | `o_icon_add_search` | 3 |
|  |  | `o_icon_browse` | 7 |
|  |  | `o_icon_enlarge` | 7 |
| `section` | fa-solid | `o_icon_legal_folder` | 4 |
| `share` | fa-solid | `o_icon_pf_page_shared` | 4 |
|  |  | `o_icon_pf_quick_links` | 2 |
|  |  | `o_icon_publish` | 5 |
|  |  | `o_icon_qitem_share` | 3 |
|  |  | `o_icon_share` | 4 |
| `share-alt` | fa-solid | `o_icon_pf_my_shares` | 3 |
| `share-alt-square` | fa-solid | `o_icon_pf_shared_with_me` | 3 |
|  |  | `o_icon_pool_pool` | 7 |
|  |  | `o_icon_share_alt` | 3 |
| `share-square` | fa-regular | `o_icon_export` | 23 |
|  |  | `o_icon_share_social` | 3 |
| `shield` | fa-solid | `o_icon_competences` | 12 |
| `shopping-cart` | fa-solid | `o_icon_booking` | 11 |
| `shuffle` | fa-solid | `o_icon_tb_method` | 3 |
| `sign-in` | fa-solid | `o_en_icon` | 7 |
|  |  | `o_icon_login` | 9 |
|  |  | `o_portlet_shibboleth_icon` | 2 |
| `sign-out` | fa-solid | `o_icon_logout` | 3 |
|  |  | `o_icon_sign_out` | 4 |
| `sitemap` | fa-solid | `o_icon_catalog` | 7 |
|  |  | `o_icon_levels` | 8 |
|  |  | `o_icon_sitemap` | 4 |
|  |  | `o_icon_structure` | 17 |
|  |  | `o_icon_taxonomy_levels` | 4 |
| `sliders` | fa-solid | `o_FileResource-FORM_icon` | 6 |
|  |  | `o_icon_rubric` | 3 |
|  |  | `o_survey_icon` | 4 |
| `soccer-ball` | fa-regular | `o_practice_icon` | 6 |
| `sort` | fa-solid | `o_icon_sort` | 3 |
| `sort-amount-asc` | fa-solid | `o_icon_sort_amount_asc` | 5 |
|  |  | `o_icon_sort_menu` | 4 |
| `sort-amount-desc` | fa-solid | `o_icon_sort_amount_desc` | 6 |
| `sort-asc` | fa-solid | `o_icon_sort_asc` | 6 |
| `sort-desc` | fa-solid | `o_icon_sort_desc` | 6 |
| `spinner` | fa-solid | `o_as_mode_assessment` | 3 |
|  |  | `o_icon_assessment_inspection_inprogress` | 4 |
|  |  | `o_icon_busy` | 8 |
|  |  | `o_icon_pending` | 7 |
| `square` | fa-regular | `o_grad_assignment_assigned` | 4 |
|  |  | `o_icon_calendar_disabled` | 2 |
|  |  | `o_icon_check_off` | 16 |
|  |  | `o_icon_checkbox` | 3 |
|  |  | `o_icon_pool_private` | 4 |
|  |  | `o_icon_quiz_multiple_choice_off` | 6 |
|  |  | `o_icon_rectangle` | 5 |
|  |  | `o_icon_single_element` | 4 |
| `square-caret-down` | fa-regular | `o_icon_show_more` | 2 |
| `square-caret-up` | fa-regular | `o_icon_show_less` | 2 |
| `square-root-variable` | fa-solid | `o_icon_math` | 5 |
| `square-rss` | fa-solid | `o_icon_square_rss` | 3 |
| `square-share-nodes` | fa-solid | `o_icon_curriculum_implementations` | 12 |
|  |  | `o_icon_taxonomy_level_type` | 3 |
| `square-x-twitter` | fa-brands | `o_icon_twitter` | 5 |
| `star` | fa-solid | `o_icon_default_config` | 3 |
|  |  | `o_icon_grade` | 9 |
|  |  | `o_icon_others` | 2 |
|  |  | `o_icon_qitem_review` | 4 |
|  |  | `o_icon_rating_off` | 9 |
|  |  | `o_icon_rating_on` | 5 |
|  |  | `o_icon_repo_status_review` | 2 |
|  |  | `o_icon_review` | 6 |
|  |  | `o_icon_star` | 6 |
|  |  | `o_portlet_iframe_icon` | 2 |
| `step-backward` | fa-solid | `o_icon_reset` | 6 |
| `sticky-note` | fa-solid | `o_icon_educational_type` | 2 |
|  |  | `o_icon_notes` | 20 |
|  |  | `o_icon_notes_empty` | 3 |
|  |  | `o_icon_proj_note` | 9 |
|  |  | `o_portlet_notes_icon` | 2 |
| `stop` | fa-solid | `o_as_mode_stop` | 5 |
|  |  | `o_icon_qti_cancel` | 3 |
| `street-view` | fa-solid | `o_icon_fake_participant` | 4 |
| `table` | fa-solid | `o_icon_report` | 3 |
|  |  | `o_mi_qtimatch` | 4 |
| `table-cells-large` | fa-solid | `o_icon_name` | 3 |
| `table-list` | fa-solid | `o_icon_table` | 15 |
| `tachometer` | fa-solid | `o_portlet_sysinfo_icon` | 2 |
| `tag` | fa-solid | `o_icon_tag` | 5 |
| `tags` | fa-solid | `o_icon_tags` | 16 |
| `tasks` | fa-solid | `o_gta_icon` | 9 |
|  |  | `o_ta_icon` | 5 |
| `th-large` | fa-solid | `o_icon_table_large` | 2 |
| `thumb-tack` | fa-solid | `o_icon_qual_ana_pres_edit` | 3 |
| `thumbs-down` | fa-regular | `o_icon_decline` | 16 |
|  |  | `o_icon_rating_no_off` | 4 |
|  |  | `o_icon_rating_no_on` | 4 |
|  |  | `o_icon_rejected` | 8 |
|  |  | `o_icon_revision` | 3 |
| `thumbs-up` | fa-regular | `o_icon_accepted` | 21 |
|  |  | `o_icon_browsercheck` | 2 |
|  |  | `o_icon_pending_confirmations` | 4 |
|  |  | `o_icon_rating_yes_off` | 4 |
|  |  | `o_icon_rating_yes_on` | 4 |
|  |  | `o_icon_restore` | 12 |
|  |  | `o_ms_icon` | 5 |
| `thumbtack` | fa-solid | `o_icon_thumbtack` | 3 |
| `timeline` | fa-solid | `o_icon_timeline` | 4 |
| `times` | fa-solid | `o_ac_status_error_icon` | 6 |
|  |  | `o_icon_absence` | 3 |
|  |  | `o_icon_addremove_remove` | 3 |
|  |  | `o_icon_close` | 19 |
|  |  | `o_icon_close_tab` | 3 |
|  |  | `o_icon_close_tool` | 3 |
|  |  | `o_icon_immunity_proof_none` | 3 |
|  |  | `o_icon_not_correct` | 8 |
|  |  | `o_icon_progress_danger` | 4 |
|  |  | `o_icon_reject` | 8 |
|  |  | `o_icon_remove` | 17 |
|  |  | `o_icon_review_removed` | 5 |
| `times-circle` | fa-solid | `o_icon_failed` | 23 |
|  |  | `o_icon_incorrect_response` | 4 |
|  |  | `o_icon_qti_summary_ended` | 6 |
|  |  | `o_icon_qual_exec_future` | 3 |
|  |  | `o_icon_qual_exec_over` | 2 |
|  |  | `o_icon_quiz_single_choice_incorrect` | 4 |
|  |  | `o_icon_remove_filters` | 10 |
|  |  | `o_icon_rubric_insufficient` | 6 |
|  |  | `o_icon_status_unavailable` | 22 |
| `times-square` | fa-solid | `o_icon_quiz_multiple_choice_incorrect` | 4 |
| `tint` | fa-solid | `o_icon_color_picker` | 2 |
|  |  | `o_icon_draw_color` | 9 |
| `toggle-off` | fa-solid | `o_icon_qitem_show_metadata` | 3 |
|  |  | `o_icon_qual_ana_show_filter` | 3 |
|  |  | `o_icon_toggle_off` | 6 |
| `toggle-on` | fa-solid | `o_icon_options` | 2 |
|  |  | `o_icon_qitem_hide_metadata` | 3 |
|  |  | `o_icon_qual_ana_hide_filter` | 3 |
|  |  | `o_icon_toggle_on` | 7 |
| `trash` | fa-solid | `o_icon_qitem_endOfLife` | 4 |
|  |  | `o_membership_status_resourcedeleted` | 3 |
| `trash-can` | fa-regular | `o_icon_building_status_deleted` | 2 |
|  |  | `o_icon_businessgroup_status_deleted` | 2 |
|  |  | `o_icon_businessgroup_status_trash` | 2 |
|  |  | `o_icon_clear_all` | 6 |
|  |  | `o_icon_curriculum_status_deleted` | 2 |
|  |  | `o_icon_delete_item` | 158 |
|  |  | `o_icon_deleted` | 21 |
|  |  | `o_icon_identity_deleted` | 6 |
|  |  | `o_icon_pf_entry_deleted` | 7 |
|  |  | `o_icon_pf_trash` | 4 |
|  |  | `o_icon_proj_project_status_deleted` | 4 |
|  |  | `o_icon_qitem_delete` | 3 |
|  |  | `o_icon_qual_dc_delete` | 3 |
|  |  | `o_icon_qual_gen_delete` | 3 |
|  |  | `o_icon_repo_status_deleted` | 3 |
|  |  | `o_icon_repo_status_trash` | 3 |
|  |  | `o_icon_todo_status_deleted` | 3 |
|  |  | `o_icon_trash` | 13 |
| `triangle-exclamation` | fa-solid | `o_icon_certification_status_expired_renewable` | 2 |
|  |  | `o_icon_recertification_warning` | 9 |
|  |  | `o_icon_triangle_exclamation` | 4 |
|  |  | `o_icon_validation_warning` | 7 |
| `trophy` | fa-solid | `o_icon_assessment_tool` | 18 |
|  |  | `o_icon_score` | 13 |
|  |  | `o_icon_trophy` | 7 |
| `tv` | fa-solid | `o_gotomeeting_icon` | 6 |
|  |  | `o_openmeetings_icon` | 7 |
|  |  | `o_vc_icon` | 33 |
|  |  | `o_vitero_icon` | 5 |
| `undo` | fa-solid | `o_icon_reload` | 8 |
|  |  | `o_icon_reset_data` | 13 |
|  |  | `o_icon_undo` | 2 |
| `universal-access` | fa-solid | `o_icon_disadvantage_compensation` | 15 |
| `university` | fa-solid | `o_icon_lrm` | 3 |
|  |  | `o_icon_provider_datenlotsen` | 4 |
|  |  | `o_icon_provider_ldap` | 3 |
|  |  | `o_icon_provider_shibboleth` | 4 |
|  |  | `o_icon_provider_switch_eduid` | 4 |
|  |  | `o_library_icon` | 3 |
| `unlink` | fa-solid | `o_icon_split` | 3 |
| `unlock` | fa-solid | `o_icon_unlocked` | 3 |
| `up-right-from-square` | fa-solid | `o_lti_icon` | 6 |
| `upload` | fa-solid | `o_icon_import` | 31 |
|  |  | `o_icon_qitem_import` | 3 |
|  |  | `o_icon_upload` | 17 |
|  |  | `o_mi_qtiupload` | 4 |
| `user` | fa-solid | `o_icon_pool_my_items` | 3 |
|  |  | `o_icon_tb_method_namually` | 3 |
|  |  | `o_icon_user` | 99 |
| `user-check` | fa-solid | `o_ac_membership_standard_icon` | 4 |
| `user-circle` | fa-solid | `o_ac_guest_icon` | 5 |
|  |  | `o_ac_guests_icon` | 5 |
|  |  | `o_icon_profile` | 4 |
| `user-group` | fa-solid | `o_icon_num_participants` | 8 |
| `user-large-slash` | fa-solid | `o_icon_assessment_inspection_noshow` | 2 |
| `user-md` | fa-solid | `o_icon_reviewer` | 4 |
| `user-plus` | fa-solid | `o_icon_add_member` | 24 |
| `user-secret` | fa-solid | `o_icon_provider_keycloak` | 3 |
|  |  | `o_mi_qtiunkown` | 7 |
|  |  | `o_unkown_icon` | 3 |
| `user-shield` | fa-solid | `o_icon_user_authentication` | 4 |
| `user-tie` | fa-solid | `o_icon_manager` | 4 |
| `user-times` | fa-solid | `o_icon_remove_member` | 4 |
| `users` | fa-regular | `o_ac_group_icon` | 5 |
|  |  | `o_cmembers_icon` | 6 |
|  |  | `o_icon_committee` | 6 |
|  |  | `o_icon_membersmanagement` | 10 |
|  |  | `o_icon_pool_share` | 7 |
|  |  | `o_portlet_groups_icon` | 2 |
| `v` | fa-solid | `o_icon_v` | 3 |
| `video-camera` | fa-solid | `o_icon_video_record` | 12 |
|  |  | `o_livestream_icon` | 8 |
| `volume-up` | fa-solid | `o_icon_audio` | 4 |
| `wand-magic-sparkles` | fa-solid | `o_icon_ai` | 6 |
|  |  | `o_icon_eva_coach_apply` | 3 |
| `warning` | fa-solid | `o_absences_col_warning` | 3 |
|  |  | `o_scorm_failed` | 3 |
|  |  | `o_scorm_incomplete` | 3 |
| `wheelchair` | fa-solid | `o_icon_accessibility` | 2 |
| `window-close` | fa-solid | `o_icon_qti_close_results` | 3 |
|  |  | `o_icon_qti_close_test` | 3 |
| `windows` | fa-brands | `o_icon_provider_adfs` | 10 |
|  |  | `o_teamsmeeting_icon` | 5 |
| `wrench` | fa-solid | `o_icon_tools` | 5 |
| `x-twitter` | fa-brands | `o_icon_provider_twitter` | 6 |
| `xing` | fa-brands | `o_icon_xing` | 5 |
| `yahoo` | fa-brands | `o_icon_yahoo` | 4 |
| `youtube-square` | fa-brands | `o_icon_lic_youtube` | 6 |
|  |  | `o_icon_youtube` | 8 |
