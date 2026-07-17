# Icon Map

OpenOlat maps [FontAwesome](https://fontawesome.com/) icons, and a small set of custom
**OpenOlat font** glyphs, to its own CSS classes (`o_icon_*`). One FontAwesome icon can
correspond to multiple OpenOlat classes — each class represents its own semantic context.

The **OpenOlat font** is a small custom icon font (built with fontello) that OpenOlat
ships in addition to FontAwesome, for glyphs FontAwesome does not offer: brand/product
logos (card2brain, Opencast, edu-sharing, Jupyter, Mediasite), Creative Commons license
badges, and a few drawing-tool icons.

!!! info "Source data"
    393 FontAwesome icons · 1157 OpenOlat classes · 6644 references in source code (`src/main`)

## Usage

Icons are embedded with the `:o_icon_<class>:` MkDocs syntax, which renders the exact OpenOlat markup:

```html
<i class="o_icon o_icon_user" aria-hidden="true"></i>
```

## Icon Mapping Table

| Icon | FA Icon | Variant | OpenOlat CSS Class | Occurrences |
|------|---------|---------|---------------------|------------:|
| :o_icon_o_card2brain_icon: |  | OpenOlat font | `o_card2brain_icon` | 3 |
| :o_icon_o_edusharing_icon: |  | OpenOlat font | `o_edusharing_icon` | 2 |
| :o_icon_o_opencast_icon: |  | OpenOlat font | `o_opencast_icon` | 3 |
| :o_icon_o_icon_draw_align-bottom: |  | OpenOlat font | `o_icon_draw_align-bottom` | 2 |
| :o_icon_o_icon_draw_align-left: |  | OpenOlat font | `o_icon_draw_align-left` | 2 |
| :o_icon_o_icon_draw_align-right: |  | OpenOlat font | `o_icon_draw_align-right` | 2 |
| :o_icon_o_icon_draw_align-top: |  | OpenOlat font | `o_icon_draw_align-top` | 2 |
| :o_icon_o_icon_draw_distribute-h: |  | OpenOlat font | `o_icon_draw_distribute-h` | 2 |
| :o_icon_o_icon_draw_distribute-v: |  | OpenOlat font | `o_icon_draw_distribute-v` | 2 |
| :o_icon_o_icon_draw_equal-size: |  | OpenOlat font | `o_icon_draw_equal-size` | 2 |
| :o_icon_o_icon_draw_equal-size-width: |  | OpenOlat font | `o_icon_draw_equal-size-width` | 3 |
| :o_icon_o_icon_draw_equal-size-height: |  | OpenOlat font | `o_icon_draw_equal-size-height` | 3 |
| :o_icon_o_icon_lic_public_domain: |  | OpenOlat font | `o_icon_lic_public_domain` | 2 |
| :o_icon_o_icon_lic_cc0: |  | OpenOlat font | `o_icon_lic_cc0` | 2 |
| :o_icon_o_icon_lic_by: |  | OpenOlat font | `o_icon_lic_by` | 2 |
| :o_icon_o_icon_lic_by_sa: |  | OpenOlat font | `o_icon_lic_by_sa` | 2 |
| :o_icon_o_icon_lic_by_nd: |  | OpenOlat font | `o_icon_lic_by_nd` | 2 |
| :o_icon_o_icon_lic_by_nc: |  | OpenOlat font | `o_icon_lic_by_nc` | 2 |
| :o_icon_o_icon_lic_by_nc_sa: |  | OpenOlat font | `o_icon_lic_by_nc_sa` | 2 |
| :o_icon_o_icon_lic_by_nc_nd: |  | OpenOlat font | `o_icon_lic_by_nc_nd` | 2 |
| :o_icon_o_edubase_icon: |  | OpenOlat font | `o_edubase_icon` | 3 |
| :o_icon_o_icon_draw_front: |  | OpenOlat font | `o_icon_draw_front` | 2 |
| :o_icon_o_icon_draw_back: |  | OpenOlat font | `o_icon_draw_back` | 2 |
| :o_icon_o_mediasite_icon: |  | OpenOlat font | `o_mediasite_icon` | 3 |
| :o_icon_o_jupyter_icon: |  | OpenOlat font | `o_jupyter_icon` | 3 |
| :o_icon_o_icon_a: | `a` | fa-solid | `o_icon_a` | 8 |
| :o_icon_o_icon_billing_address: | `address-card` | fa-solid | `o_icon_billing_address` | 7 |
|  |  |  | `o_icon_visiting_card` | 1 |
| :o_icon_o_icon_todo_status_in_progress: | `adjust` | fa-solid | `o_icon_todo_status_in_progress` | 1 |
|  |  |  | `o_lectures_rollcall_warning` | 4 |
| :o_icon_o_icon_align_middle: | `align-center` | fa-solid | `o_icon_align_middle` | 0 |
| :o_icon_o_forum_all_flat_icon: | `align-justify` | fa-solid | `o_forum_all_flat_icon` | 1 |
|  |  |  | `o_icon_column` | 0 |
| :o_icon_o_icon_align_left: | `align-left` | fa-solid | `o_icon_align_left` | 4 |
|  |  |  | `o_icon_textinput` | 0 |
|  |  |  | `o_mi_qtiessay` | 3 |
| :o_icon_o_forum_all_icon: | `align-right` | fa-solid | `o_forum_all_icon` | 1 |
|  |  |  | `o_icon_align_right` | 0 |
| :o_icon_o_icon_cleanup: | `ambulance` | fa-solid | `o_icon_cleanup` | 1 |
| :o_icon_o_icon_modified: | `angle-double-down` | fa-solid | `o_icon_modified` | 0 |
|  |  |  | `o_icon_move_down` | 49 |
|  |  |  | `o_icon_todo_priority_low` | 1 |
| :o_icon_o_icon_move_left: | `angle-double-left` | fa-solid | `o_icon_move_left` | 4 |
|  |  |  | `o_icon_previous_page` | 8 |
|  |  |  | `o_icon_previous_step` | 1 |
| :o_icon_o_icon_move_right: | `angle-double-right` | fa-solid | `o_icon_move_right` | 4 |
|  |  |  | `o_icon_next_page` | 8 |
|  |  |  | `o_icon_next_step` | 1 |
| :o_icon_o_icon_move_up: | `angle-double-up` | fa-solid | `o_icon_move_up` | 50 |
| :o_icon_o_icon_details_expand: | `angle-down` | fa-solid | `o_icon_details_expand` | 28 |
| :o_icon_o_icon_details_collaps: | `angle-up` | fa-solid | `o_icon_details_collaps` | 28 |
| :o_icon_o_icon_forward: | `angles-right` | fa-solid | `o_icon_forward` | 1 |
| :o_icon_o_icon_apple: | `apple` | fa-brands | `o_icon_apple` | 1 |
| :o_icon_o_FileResource-IMSCP_icon: | `archive` | fa-solid | `o_FileResource-IMSCP_icon` | 0 |
|  |  |  | `o_FileResource-SCORMCP_icon` | 1 |
|  |  |  | `o_cp_icon` | 6 |
|  |  |  | `o_scorm_icon` | 4 |
|  |  |  | `o_scorm_org` | 2 |
| :o_icon_o_icon_left: | `arrow-circle-left` | fa-solid | `o_icon_left` | 1 |
| :o_icon_o_icon_qual_ana_trend_arrow: | `arrow-circle-right` | fa-solid | `o_icon_qual_ana_trend_arrow` | 1 |
|  |  |  | `o_icon_right` | 1 |
| :o_icon_o_icon_element_after: | `arrow-down` | fa-solid | `o_icon_element_after` | 0 |
| :o_icon_o_icon_arrow_right: | `arrow-right` | fa-solid | `o_icon_arrow_right` | 10 |
|  |  |  | `o_icon_qitem_status` | 0 |
|  |  |  | `o_membership_status_transfer` | 0 |
| :o_icon_o_icon_certification_certifying: | `arrow-rotate-right` | fa-solid | `o_icon_certification_certifying` | 1 |
|  |  |  | `o_icon_recertification` | 1 |
| :o_icon_o_icon_element_before: | `arrow-up` | fa-solid | `o_icon_element_before` | 0 |
|  |  |  | `o_membership_status_parentbooking` | 0 |
| :o_icon_o_icon_progress: | `arrow-up-right-dots` | fa-solid | `o_icon_progress` | 3 |
| :o_icon_o_icon_arrow_up_right_from_square: | `arrow-up-right-from-square` | fa-solid | `o_icon_arrow_up_right_from_square` | 12 |
| :o_icon_o_icon_move: | `arrows` | fa-solid | `o_icon_move` | 13 |
| :o_icon_o_icon_tb_select_last: | `arrows-down-to-line` | fa-solid | `o_icon_tb_select_last` | 3 |
| :o_icon_o_icon_eva_end_show: | `arrows-h` | fa-solid | `o_icon_eva_end_show` | 1 |
|  |  |  | `o_icon_spacer` | 3 |
| :o_icon_o_icon_mix: | `arrows-rotate` | fa-solid | `o_icon_mix` | 2 |
| :o_icon_o_icon_cns: | `arrows-turn-right` | fa-solid | `o_icon_cns` | 1 |
|  |  |  | `o_icon_shift` | 1 |
| :o_icon_o_icon_assign_new_item: | `arrows-turn-to-dots` | fa-solid | `o_icon_assign_new_item` | 1 |
| :o_icon_o_icon_tb_select_first: | `arrows-up-to-line` | fa-solid | `o_icon_tb_select_first` | 3 |
| :o_icon_o_icon_node_up_down: | `arrows-v` | fa-solid | `o_icon_node_up_down` | 1 |
|  |  |  | `o_icon_order` | 1 |
| :o_icon_o_ac_status_new_icon: | `asterisk` | fa-solid | `o_ac_status_new_icon` | 2 |
|  |  |  | `o_forum_new_icon` | 3 |
|  |  |  | `o_icon_compulsory` | 9 |
|  |  |  | `o_icon_mandatory` | 7 |
|  |  |  | `o_icon_new` | 6 |
| :o_icon_o_icon_badge: | `award` | fa-solid | `o_icon_badge` | 18 |
| :o_icon_o_icon_slide_backward: | `backward-step` | fa-solid | `o_icon_slide_backward` | 4 |
| :o_icon_o_CourseModule_icon_closed: | `ban` | fa-solid | `o_CourseModule_icon_closed` | 5 |
|  |  |  | `o_ac_billing_address_inactive_icon` | 1 |
|  |  |  | `o_ac_offer_finished_icon` | 1 |
|  |  |  | `o_ac_offer_fully_booked_icon` | 2 |
|  |  |  | `o_forum_status_closed_icon` | 1 |
|  |  |  | `o_forum_status_opened_icon` | 1 |
|  |  |  | `o_forum_status_sticky_closed_icon` | 0 |
|  |  |  | `o_grader_inactive` | 1 |
|  |  |  | `o_icon_assessment_inspection_withdrawn` | 0 |
|  |  |  | `o_icon_ban` | 20 |
|  |  |  | `o_icon_businessgroup_status_inactive` | 0 |
|  |  |  | `o_icon_cancelled` | 5 |
|  |  |  | `o_icon_certification_status_revoked` | 2 |
|  |  |  | `o_icon_check_disabled` | 4 |
|  |  |  | `o_icon_curriculum_status_finished` | 0 |
|  |  |  | `o_icon_deactivate` | 11 |
|  |  |  | `o_icon_identity_login_denied` | 1 |
|  |  |  | `o_icon_invitation_status_inactive` | 0 |
|  |  |  | `o_icon_proj_project_status_done` | 1 |
|  |  |  | `o_icon_qti_ended` | 0 |
|  |  |  | `o_icon_qual_ana_pres_delete` | 1 |
|  |  |  | `o_icon_qual_blacklist_add` | 1 |
|  |  |  | `o_icon_qual_gen_disabled` | 2 |
|  |  |  | `o_icon_qual_prev_blacklisted` | 1 |
|  |  |  | `o_icon_repo_status_closed` | 4 |
|  |  |  | `o_icon_rm_status_inactive` | 0 |
|  |  |  | `o_icon_seb_template_status_inactive` | 2 |
|  |  |  | `o_icon_status_not_ready` | 3 |
|  |  |  | `o_lp_not_accessible` | 1 |
| :o_icon_o_icon_institution: | `bank` | fa-solid | `o_icon_institution` | 2 |
|  |  |  | `o_icon_qpool` | 3 |
| :o_icon_o_icon_statistics_tool: | `bar-chart` | fa-regular | `o_icon_statistics_tool` | 10 |
| :o_icon_o_icon_menuhandel: | `bars` | fa-solid | `o_icon_menuhandel` | 3 |
|  |  |  | `o_mi_qtiorder` | 2 |
| :o_icon_o_icon_reminder: | `bell` | fa-regular | `o_icon_reminder` | 10 |
| :o_icon_o_icon_todo_priority_urgent: | `bell` | fa-solid | `o_icon_todo_priority_urgent` | 1 |
| :o_icon_o_mi_qtigapmixed: | `blender` | fa-solid | `o_mi_qtigapmixed` | 2 |
| :o_icon_o_bigbluebuttonmeeting_icon: | `bold` | fa-solid | `o_bigbluebuttonmeeting_icon` | 1 |
|  |  |  | `o_icon_bold` | 1 |
| :o_icon_o_icon_administrator: | `bolt` | fa-solid | `o_icon_administrator` | 1 |
|  |  |  | `o_icon_assignment` | 8 |
|  |  |  | `o_icon_bolt` | 1 |
| :o_icon_o_icon_bolt_lightning: | `bolt-lightning` | fa-solid | `o_icon_bolt_lightning` | 4 |
| :o_icon_o_icon_bomb: | `bomb` | fa-solid | `o_icon_bomb` | 1 |
| :o_icon_o_icon_lecture: | `book` | fa-solid | `o_icon_lecture` | 24 |
|  |  |  | `o_icon_manual` | 5 |
| :o_icon_o_icon_language: | `book-atlas` | fa-solid | `o_icon_language` | 17 |
| :o_icon_o_icon_catalog_intern: | `book-open` | fa-solid | `o_icon_catalog_intern` | 12 |
| :o_icon_o_icon_bookmark_add: | `bookmark` | fa-regular | `o_icon_bookmark_add` | 17 |
| :o_icon_o_forum_marked_icon: | `bookmark` | fa-solid | `o_forum_marked_icon` | 1 |
|  |  |  | `o_icon_bookmark` | 17 |
|  |  |  | `o_icon_bookmark_header` | 44 |
|  |  |  | `o_icon_pool_favorits` | 1 |
|  |  |  | `o_portlet_bookmark_icon` | 0 |
| :o_icon_o_icon_certification_status_archived: | `box-archive` | fa-solid | `o_icon_certification_status_archived` | 1 |
| :o_icon_o_icon_coursearchive: | `boxes-packing` | fa-solid | `o_icon_coursearchive` | 8 |
| :o_icon_o_BinderTemplate_icon: | `briefcase` | fa-solid | `o_BinderTemplate_icon` | 0 |
|  |  |  | `o_ep_icon` | 8 |
|  |  |  | `o_icon_pf_binder` | 8 |
| :o_icon_o_icon_bug: | `bug` | fa-solid | `o_icon_bug` | 1 |
|  |  |  | `o_icon_dev` | 2 |
| :o_icon_o_FileResource-BLOG_icon: | `bullhorn` | fa-solid | `o_FileResource-BLOG_icon` | 2 |
|  |  |  | `o_blog_icon` | 12 |
| :o_icon_o_icon_landingpage: | `bullseye` | fa-solid | `o_icon_landingpage` | 1 |
|  |  |  | `o_icon_objectives` | 2 |
|  |  |  | `o_icon_proj_milestone` | 2 |
| :o_icon_o_icon_c: | `c` | fa-solid | `o_icon_c` | 5 |
| :o_icon_o_icon_grade_scale: | `calculator` | fa-solid | `o_icon_grade_scale` | 1 |
|  |  |  | `o_mi_qtinumerical` | 2 |
| :o_icon_o_den_icon: | `calendar` | fa-regular | `o_den_icon` | 5 |
|  |  |  | `o_icon_qual_prev_regular` | 1 |
|  |  |  | `o_icon_timetable` | 1 |
| :o_icon_o_icon_lifecycle_date: | `calendar` | fa-solid | `o_icon_lifecycle_date` | 13 |
|  |  |  | `o_icon_proj_appointment` | 6 |
| :o_icon_o_appointment_icon: | `calendar-check` | fa-regular | `o_appointment_icon` | 3 |
|  |  |  | `o_icon_calendar_check` | 1 |
| :o_icon_o_icon_events: | `calendar-check` | fa-solid | `o_icon_events` | 8 |
| :o_icon_o_icon_calendar_day: | `calendar-day` | fa-solid | `o_icon_calendar_day` | 7 |
| :o_icon_o_cal_icon: | `calendar-days` | fa-regular | `o_cal_icon` | 11 |
|  |  |  | `o_calendar_icon` | 2 |
|  |  |  | `o_icon_calendar` | 81 |
| :o_icon_o_portlet_cal_icon: | `calendar-days` | fa-solid | `o_portlet_cal_icon` | 0 |
| :o_icon_o_icon_qual_prev_changed: | `calendar-plus` | fa-solid | `o_icon_qual_prev_changed` | 1 |
| :o_icon_o_icon_calendar_xmark: | `calendar-xmark` | fa-regular | `o_icon_calendar_xmark` | 1 |
| :o_icon_o_icon_caret: | `caret-down` | fa-solid | `o_icon_caret` | 38 |
|  |  |  | `o_icon_close_togglebox` | 177 |
|  |  |  | `o_icon_close_tree` | 4 |
|  |  |  | `o_icon_provider_performx` | 1 |
|  |  |  | `o_mi_qtiinlinechoice` | 3 |
| :o_icon_o_icon_previous_toolbar: | `caret-left` | fa-solid | `o_icon_previous_toolbar` | 6 |
| :o_icon_o_icon_caret_right: | `caret-right` | fa-solid | `o_icon_caret_right` | 3 |
|  |  |  | `o_icon_next_toolbar` | 6 |
|  |  |  | `o_icon_open_togglebox` | 178 |
|  |  |  | `o_icon_open_tree` | 4 |
| :o_icon_o_ac_order_pre: | `cart-arrow-down` | fa-solid | `o_ac_order_pre` | 1 |
| :o_icon_o_ac_offer_bookable_icon: | `cart-shopping` | fa-solid | `o_ac_offer_bookable_icon` | 4 |
| :o_icon_o_ac_paypal_icon: | `cc-paypal` | fa-brands | `o_ac_paypal_icon` | 0 |
| :o_icon_o_icon_certificate: | `certificate` | fa-solid | `o_icon_certificate` | 29 |
|  |  |  | `o_icon_certification_certified` | 1 |
|  |  |  | `o_portlet_eff_icon` | 0 |
| :o_icon_o_icon_coaching_tool: | `chalkboard-user` | fa-solid | `o_icon_coaching_tool` | 6 |
| :o_icon_o_icon_radar_chart: | `chart-line` | fa-solid | `o_icon_radar_chart` | 1 |
| :o_icon_o_icon_chart_simple: | `chart-simple` | fa-solid | `o_icon_chart_simple` | 5 |
| :o_icon_o_ac_billing_address_active_icon: | `check` | fa-solid | `o_ac_billing_address_active_icon` | 1 |
|  |  |  | `o_ac_status_success_icon` | 2 |
|  |  |  | `o_icon_accept` | 7 |
|  |  |  | `o_icon_addremove_add` | 1 |
|  |  |  | `o_icon_assessment_inspection_carriedout` | 0 |
|  |  |  | `o_icon_businessgroup_status_active` | 0 |
|  |  |  | `o_icon_certification_status_active` | 0 |
|  |  |  | `o_icon_certification_status_valid` | 0 |
|  |  |  | `o_icon_check` | 25 |
|  |  |  | `o_icon_correct_answer` | 5 |
|  |  |  | `o_icon_curriculum_status_active` | 0 |
|  |  |  | `o_icon_curriculum_status_confirmed` | 0 |
|  |  |  | `o_icon_immunity_proof_validated` | 1 |
|  |  |  | `o_icon_invitation_status_active` | 0 |
|  |  |  | `o_icon_line` | 1 |
|  |  |  | `o_icon_member_valid` | 2 |
|  |  |  | `o_icon_ms_done` | 0 |
|  |  |  | `o_icon_ok` | 18 |
|  |  |  | `o_icon_pf_entry_published` | 3 |
|  |  |  | `o_icon_presence` | 1 |
|  |  |  | `o_icon_progress_success` | 0 |
|  |  |  | `o_icon_proj_project_status_active` | 1 |
|  |  |  | `o_icon_qitem_finalVersion` | 2 |
|  |  |  | `o_icon_repo_status_published` | 1 |
|  |  |  | `o_icon_review_added` | 3 |
|  |  |  | `o_icon_rm_status_active` | 0 |
|  |  |  | `o_icon_seb_template_status_active` | 2 |
|  |  |  | `o_icon_select` | 27 |
|  |  |  | `o_icon_selected` | 2 |
|  |  |  | `o_icon_status_done` | 19 |
|  |  |  | `o_icon_submit` | 7 |
|  |  |  | `o_icon_tb_edit_enrollments` | 2 |
|  |  |  | `o_membership_status_finished` | 1 |
| :o_icon_o_grader_active: | `check-circle` | fa-regular | `o_grader_active` | 1 |
|  |  |  | `o_icon_activate` | 10 |
|  |  |  | `o_icon_correct_response` | 0 |
|  |  |  | `o_icon_dispensation_authorized` | 1 |
|  |  |  | `o_icon_notice_authorized` | 1 |
|  |  |  | `o_icon_radio_on` | 2 |
| :o_icon_o_icon_cns_status_done: | `check-circle` | fa-solid | `o_icon_cns_status_done` | 1 |
|  |  |  | `o_icon_passed` | 26 |
|  |  |  | `o_icon_proj_milestone_status_achieved` | 2 |
|  |  |  | `o_icon_qti_summary_correct` | 8 |
|  |  |  | `o_icon_qual_dc_finished` | 1 |
|  |  |  | `o_icon_qual_exec_participated` | 0 |
|  |  |  | `o_icon_quiz_single_choice_correct` | 4 |
|  |  |  | `o_icon_quiz_single_choice_on` | 12 |
|  |  |  | `o_icon_rubric_sufficient` | 1 |
|  |  |  | `o_icon_tb_broker_enrollment_done` | 2 |
|  |  |  | `o_icon_tb_selection_enrolled` | 2 |
|  |  |  | `o_icon_tb_selection_selected` | 1 |
|  |  |  | `o_icon_tb_topic_held` | 1 |
|  |  |  | `o_icon_todo_status_done` | 1 |
|  |  |  | `o_icon_toggle_button_on` | 1 |
|  |  |  | `o_lp_done` | 12 |
|  |  |  | `o_midpub` | 3 |
|  |  |  | `o_scorm_completed` | 0 |
|  |  |  | `o_scorm_passed` | 0 |
| :o_icon_o_cl_icon: | `check-square` | fa-regular | `o_cl_icon` | 5 |
|  |  |  | `o_grad_assignment_done` | 1 |
|  |  |  | `o_icon_calendar_enabled` | 6 |
|  |  |  | `o_icon_check_on` | 24 |
|  |  |  | `o_icon_eva_mc` | 1 |
|  |  |  | `o_icon_pool_public` | 2 |
|  |  |  | `o_icon_todo_task` | 25 |
|  |  |  | `o_mi_qtimc` | 2 |
| :o_icon_o_icon_checkbox_checked: | `check-square` | fa-solid | `o_icon_checkbox_checked` | 2 |
|  |  |  | `o_icon_quiz_multiple_choice_correct` | 4 |
|  |  |  | `o_icon_quiz_multiple_choice_on` | 4 |
|  |  |  | `o_mi_qtikprim` | 3 |
| :o_icon_o_icon_previous: | `chevron-circle-left` | fa-solid | `o_icon_previous` | 12 |
| :o_icon_o_icon_next: | `chevron-circle-right` | fa-solid | `o_icon_next` | 12 |
| :o_icon_o_icon_node_after: | `chevron-down` | fa-solid | `o_icon_node_after` | 1 |
|  |  |  | `o_icon_slide_down` | 4 |
| :o_icon_o_icon_back: | `chevron-left` | fa-solid | `o_icon_back` | 26 |
|  |  |  | `o_icon_course_previous` | 3 |
| :o_icon_o_icon_course_next: | `chevron-right` | fa-solid | `o_icon_course_next` | 3 |
|  |  |  | `o_icon_curriculum_status_transition` | 1 |
|  |  |  | `o_icon_start` | 87 |
| :o_icon_o_icon_node_before: | `chevron-up` | fa-solid | `o_icon_node_before` | 1 |
|  |  |  | `o_icon_slide_up` | 4 |
|  |  |  | `o_icon_top` | 2 |
| :o_icon_o_icon_circle: | `circle` | fa-regular | `o_icon_circle` | 4 |
|  |  |  | `o_icon_courseareas` | 12 |
|  |  |  | `o_icon_disabled` | 6 |
|  |  |  | `o_icon_inheritance_none` | 1 |
|  |  |  | `o_icon_proj_milestone_status_open` | 1 |
|  |  |  | `o_icon_provider_tocco` | 1 |
|  |  |  | `o_icon_qti_notAnswered` | 0 |
|  |  |  | `o_icon_qti_notPresented` | 0 |
|  |  |  | `o_icon_qti_summary_notAnswered` | 2 |
|  |  |  | `o_icon_qti_summary_notPresented` | 2 |
|  |  |  | `o_icon_quiz_single_choice_off` | 8 |
|  |  |  | `o_icon_radio_off` | 2 |
|  |  |  | `o_icon_read` | 2 |
|  |  |  | `o_icon_status_not_started` | 3 |
|  |  |  | `o_icon_tb_strategy_max_topics` | 1 |
|  |  |  | `o_icon_tb_topics` | 5 |
|  |  |  | `o_icon_todo_status_open` | 1 |
|  |  |  | `o_lectures_rollcall_danger` | 7 |
|  |  |  | `o_lp_ready` | 3 |
|  |  |  | `o_projectbroker_icon` | 5 |
| :o_icon_o_icon_qual_blacklist_remove: | `circle, minus` | fa-regular, fa-solid | `o_icon_qual_blacklist_remove` | 1 |
| :o_icon_o_black_led: | `circle` | fa-solid | `o_black_led` | 3 |
|  |  |  | `o_green_led` | 2 |
|  |  |  | `o_grey_led` | 1 |
|  |  |  | `o_icon_circle_color` | 19 |
|  |  |  | `o_icon_draw_ellipse` | 1 |
|  |  |  | `o_icon_enabled` | 0 |
|  |  |  | `o_icon_qti_answered` | 0 |
|  |  |  | `o_icon_status_available` | 14 |
|  |  |  | `o_icon_tb_broker_not_started` | 1 |
|  |  |  | `o_icon_to_read` | 11 |
|  |  |  | `o_icon_todo_priority_medium` | 1 |
|  |  |  | `o_icon_toggle` | 2 |
|  |  |  | `o_icon_toggle_button_off` | 1 |
|  |  |  | `o_lectures_absent` | 8 |
|  |  |  | `o_lectures_attended` | 4 |
|  |  |  | `o_lectures_authorized` | 4 |
|  |  |  | `o_lectures_closed` | 1 |
|  |  |  | `o_lectures_current` | 1 |
|  |  |  | `o_lectures_dispensed` | 4 |
|  |  |  | `o_lectures_pending` | 1 |
|  |  |  | `o_lectures_rollcall_free` | 3 |
|  |  |  | `o_lectures_rollcall_notice` | 1 |
|  |  |  | `o_lectures_rollcall_ok` | 5 |
|  |  |  | `o_red_led` | 3 |
|  |  |  | `o_yellow_led` | 2 |
| :o_icon_o_icon_videotask: | `circle, video-camera` | fa-solid, fa-solid | `o_icon_videotask` | 2 |
| :o_icon_o_icon_load_more: | `circle-arrow-down` | fa-solid | `o_icon_load_more` | 1 |
|  |  |  | `o_icon_proj_timeline_earlier` | 1 |
| :o_icon_o_icon_proj_timeline_later: | `circle-arrow-up` | fa-solid | `o_icon_proj_timeline_later` | 1 |
| :o_icon_o_icon_absence_authorized: | `circle-check` | fa-regular | `o_icon_absence_authorized` | 1 |
| :o_icon_o_ac_order_status_payed_icon: | `circle-check` | fa-solid | `o_ac_order_status_payed_icon` | 2 |
|  |  |  | `o_icon_certification_status_certified` | 0 |
|  |  |  | `o_icon_circle_check` | 4 |
|  |  |  | `o_icon_lecture_rollcall_closed` | 1 |
|  |  |  | `o_membership_status_active` | 2 |
| :o_icon_o_icon_selected_dot: | `circle-dot` | fa-regular | `o_icon_selected_dot` | 3 |
| :o_icon_o_icon_lecture_rollcall_open: | `circle-dot` | fa-solid | `o_icon_lecture_rollcall_open` | 1 |
| :o_icon_o_icon_inheritance_inherited: | `circle-down` | fa-regular | `o_icon_inheritance_inherited` | 2 |
| :o_icon_o_icon_inheritance_root: | `circle-down` | fa-solid | `o_icon_inheritance_root` | 2 |
| :o_icon_o_ac_offer_overbooked_icon: | `circle-exclamation` | fa-solid | `o_ac_offer_overbooked_icon` | 1 |
|  |  |  | `o_icon_circle_exclamation` | 3 |
|  |  |  | `o_icon_recertification_error` | 4 |
|  |  |  | `o_icon_validation_error` | 27 |
| :o_icon_o_ac_offer_almost_fully_booked_icon: | `circle-half-stroke` | fa-solid | `o_ac_offer_almost_fully_booked_icon` | 1 |
| :o_icon_o_icon_circle_info: | `circle-info` | fa-solid | `o_icon_circle_info` | 6 |
|  |  |  | `o_icon_metadata` | 1 |
| :o_icon_o_icon_memo: | `circle-info, clipboard` | fa-solid, fa-solid | `o_icon_memo` | 3 |
| :o_icon_o_as_mode_closed: | `circle-minus` | fa-solid | `o_as_mode_closed` | 1 |
|  |  |  | `o_icon_invalidate` | 5 |
|  |  |  | `o_icon_tb_selection_surplus` | 1 |
| :o_icon_o_icon_wait: | `circle-notch` | fa-solid | `o_icon_wait` | 1 |
| :o_icon_o_icon_cns_status_in_progress: | `circle-play` | fa-solid | `o_icon_cns_status_in_progress` | 1 |
|  |  |  | `o_icon_curriculum_implementation_avatar` | 1 |
|  |  |  | `o_icon_tb_broker_selection_in_progress` | 1 |
|  |  |  | `o_icon_todo_start` | 1 |
| :o_icon_o_ac_order_status_new_icon: | `circle-plus` | fa-solid | `o_ac_order_status_new_icon` | 0 |
|  |  |  | `o_icon_qitem_new` | 1 |
| :o_icon_o_icon_circle_radiation: | `circle-radiation` | fa-solid | `o_icon_circle_radiation` | 1 |
| :o_icon_o_icon_cancel: | `circle-stop` | fa-regular | `o_icon_cancel` | 8 |
| :o_icon_o_icon_assessment_inspection_cancelled: | `circle-stop` | fa-solid | `o_icon_assessment_inspection_cancelled` | 0 |
| :o_icon_o_ac_order_status_canceled_icon: | `circle-xmark` | fa-solid | `o_ac_order_status_canceled_icon` | 2 |
|  |  |  | `o_ac_order_status_error_icon` | 1 |
|  |  |  | `o_icon_certification_status_removed` | 0 |
|  |  |  | `o_icon_circle_xmark` | 5 |
|  |  |  | `o_icon_curriculum_status_cancelled` | 0 |
|  |  |  | `o_icon_error` | 79 |
|  |  |  | `o_icon_repo_status_deleted` | 2 |
|  |  |  | `o_icon_tb_topic_not_held` | 1 |
|  |  |  | `o_membership_status_cancel` | 1 |
|  |  |  | `o_membership_status_cancelwithfee` | 1 |
|  |  |  | `o_membership_status_declined` | 1 |
|  |  |  | `o_membership_status_removed` | 2 |
| :o_icon_o_icon_quiz: | `circle-xmark, circle-check` | fa-solid, fa-regular | `o_icon_quiz` | 0 |
| :o_icon_o_icon_form: | `clipboard` | fa-regular | `o_icon_form` | 2 |
| :o_icon_o_icon_view_all_rubrics: | `clipboard-check` | fa-solid | `o_icon_view_all_rubrics` | 1 |
| :o_icon_o_icon_info_list: | `clipboard-list` | fa-solid | `o_icon_info_list` | 2 |
|  |  |  | `o_icon_tb_enrollments` | 3 |
|  |  |  | `o_icon_tb_strategy_max_enrollments` | 1 |
|  |  |  | `o_icon_topicbroker` | 7 |
| :o_icon_o_icon_qual_prev_data_collection: | `clipboard-question` | fa-solid | `o_icon_qual_prev_data_collection` | 1 |
|  |  |  | `o_icon_qual_preview` | 5 |
| :o_icon_o_ac_status_waiting_icon: | `clock` | fa-regular | `o_ac_status_waiting_icon` | 1 |
|  |  |  | `o_grader_absence` | 1 |
|  |  |  | `o_icon_absence_leave` | 2 |
|  |  |  | `o_icon_change_notifications_settings` | 1 |
|  |  |  | `o_icon_expenditure` | 3 |
|  |  |  | `o_icon_extra_time` | 28 |
|  |  |  | `o_icon_identity_pending` | 1 |
|  |  |  | `o_icon_pf_history` | 2 |
|  |  |  | `o_icon_time` | 28 |
|  |  |  | `o_icon_timelimit` | 18 |
|  |  |  | `o_icon_visitingcard` | 1 |
|  |  |  | `o_icon_waiting` | 2 |
|  |  |  | `o_lectures_next` | 1 |
|  |  |  | `o_lectures_rollcall_` | 0 |
|  |  |  | `o_membership_status_booking` | 0 |
| :o_icon_o_ac_offer_pending_icon: | `clock` | fa-solid | `o_ac_offer_pending_icon` | 2 |
|  |  |  | `o_as_mode_none` | 1 |
|  |  |  | `o_icon_assessment_inspection_scheduled` | 2 |
|  |  |  | `o_icon_lecture_rollcall_autoclosed` | 1 |
| :o_icon_o_icon_certification_status_expired: | `clock-rotate-left` | fa-solid | `o_icon_certification_status_expired` | 0 |
|  |  |  | `o_icon_history` | 5 |
|  |  |  | `o_icon_lecture_rollcall_reopen` | 1 |
| :o_icon_o_icon_duplicate: | `clone` | fa-solid | `o_icon_duplicate` | 5 |
|  |  |  | `o_mi_qtimatch_draganddrop` | 2 |
| :o_icon_o_icon_onedrive: | `cloud` | fa-solid | `o_icon_onedrive` | 2 |
|  |  |  | `o_icon_provider_oauth` | 5 |
|  |  |  | `o_icon_provider_panther` | 1 |
| :o_icon_o_icon_add_html: | `code` | fa-solid | `o_icon_add_html` | 0 |
|  |  |  | `o_icon_code` | 6 |
| :o_icon_o_icon_code_branch: | `code-branch` | fa-solid | `o_icon_code_branch` | 1 |
| :o_icon_o_icon_branch: | `code-fork` | fa-solid | `o_icon_branch` | 5 |
| :o_icon_o_icon_inspect: | `cog` | fa-solid | `o_icon_inspect` | 2 |
| :o_icon_o_icon_coins: | `coins` | fa-solid | `o_icon_coins` | 8 |
| :o_icon_o_icon_columns: | `columns` | fa-solid | `o_icon_columns` | 0 |
|  |  |  | `o_icon_container` | 2 |
| :o_icon_o_forum_message_icon: | `comment` | fa-regular | `o_forum_message_icon` | 1 |
|  |  |  | `o_icon_chat` | 10 |
|  |  |  | `o_icon_comments_none` | 5 |
|  |  |  | `o_icon_post` | 1 |
|  |  |  | `o_portlet_infomessages_icon` | 0 |
| :o_icon_o_icon_comment: | `comment` | fa-solid | `o_icon_comment` | 2 |
|  |  |  | `o_icon_status_chat` | 6 |
| :o_icon_o_icon_comment_sms: | `comment-sms` | fa-solid | `o_icon_comment_sms` | 4 |
| :o_icon_o_fo_icon: | `comments` | fa-regular | `o_fo_icon` | 10 |
|  |  |  | `o_forum_status_thread_icon` | 10 |
|  |  |  | `o_icon_chats` | 3 |
| :o_icon_o_forum_status_sticky_icon: | `comments` | fa-solid | `o_forum_status_sticky_icon` | 1 |
|  |  |  | `o_icon_comments` | 11 |
| :o_icon_o_icon_compass: | `compass` | fa-regular | `o_icon_compass` | 1 |
| :o_icon_o_icon_courseplanner: | `compass-drafting` | fa-solid | `o_icon_courseplanner` | 2 |
| :o_icon_o_icon_compress: | `compress` | fa-solid | `o_icon_compress` | 1 |
|  |  |  | `o_icon_width_collapse` | 1 |
| :o_icon_o_icon_files: | `copy` | fa-regular | `o_icon_files` | 14 |
|  |  |  | `o_icon_replace` | 0 |
|  |  |  | `o_icon_taxonomy_templates` | 4 |
| :o_icon_o_icon_copy: | `copy` | fa-solid | `o_icon_copy` | 52 |
|  |  |  | `o_icon_qitem_copy` | 1 |
| :o_icon_o_icon_lic_all_rights_reserved: | `copyright` | fa-solid | `o_icon_lic_all_rights_reserved` | 2 |
|  |  |  | `o_icon_lic_freetext` | 2 |
|  |  |  | `o_icon_lic_general` | 2 |
| :o_icon_o_icon_crosshairs: | `crosshairs` | fa-solid | `o_icon_crosshairs` | 1 |
| :o_icon_o_CourseModule_icon: | `cube` | fa-solid | `o_CourseModule_icon` | 92 |
|  |  |  | `o_course_icon` | 8 |
|  |  |  | `o_icon_courserun` | 3 |
|  |  |  | `o_icon_curriculum_element` | 34 |
|  |  |  | `o_icon_taxonomy` | 8 |
| :o_icon_o_icon_curriculum: | `cubes` | fa-solid | `o_icon_curriculum` | 21 |
|  |  |  | `o_icon_taxonomy_level` | 3 |
|  |  |  | `o_mi_qtisection` | 8 |
|  |  |  | `o_portlet_repository_student_icon` | 0 |
|  |  |  | `o_st_icon` | 6 |
| :o_icon_o_icon_course_bundle: | `cubes-stacked` | fa-solid | `o_icon_course_bundle` | 3 |
|  |  |  | `o_icon_resources` | 1 |
| :o_icon_o_icon_coursedb: | `database` | fa-solid | `o_icon_coursedb` | 2 |
|  |  |  | `o_icon_database` | 3 |
|  |  |  | `o_icon_quota` | 1 |
|  |  |  | `o_icon_sharepoint_drive` | 2 |
|  |  |  | `o_mi_qpool_import` | 4 |
| :o_icon_o_icon_delicious: | `delicious` | fa-brands | `o_icon_delicious` | 0 |
| :o_icon_o_icon_diagram_project: | `diagram-project` | fa-solid | `o_icon_diagram_project` | 2 |
| :o_icon_o_icon_digg: | `digg` | fa-brands | `o_icon_digg` | 0 |
| :o_icon_o_icon_display: | `display` | fa-solid | `o_icon_display` | 2 |
| :o_icon_o_ac_openaccess_icon: | `door-open` | fa-solid | `o_ac_openaccess_icon` | 7 |
| :o_icon_o_icon_eva_sc: | `dot-circle` | fa-regular | `o_icon_eva_sc` | 1 |
|  |  |  | `o_icon_passed_undefined` | 6 |
|  |  |  | `o_icon_status_dnd` | 11 |
|  |  |  | `o_mi_qtisc` | 2 |
| :o_icon_o_icon_archive_tool: | `download` | fa-solid | `o_icon_archive_tool` | 5 |
|  |  |  | `o_icon_download` | 90 |
|  |  |  | `o_icon_eva_export` | 1 |
|  |  |  | `o_icon_qitem_export` | 1 |
|  |  |  | `o_icon_qual_ana_export` | 1 |
| :o_icon_o_icon_courseeditor: | `edit` | fa-solid | `o_icon_courseeditor` | 1 |
|  |  |  | `o_icon_edit` | 208 |
|  |  |  | `o_icon_edit_file` | 1 |
|  |  |  | `o_icon_inline_editable` | 1 |
|  |  |  | `o_icon_qual_dc_preparation` | 1 |
|  |  |  | `o_icon_readonly` | 1 |
|  |  |  | `o_icon_readwrite` | 1 |
| :o_icon_o_icon_breadcrumb_more: | `ellipsis` | fa-solid | `o_icon_breadcrumb_more` | 1 |
| :o_icon_o_icon_pageing: | `ellipsis-h` | fa-solid | `o_icon_pageing` | 0 |
|  |  |  | `o_mi_qtifib` | 3 |
| :o_icon_o_icon_actions: | `ellipsis-v` | fa-solid | `o_icon_actions` | 54 |
|  |  |  | `o_icon_commands` | 11 |
| :o_icon_o_co_icon: | `envelope` | fa-regular | `o_co_icon` | 8 |
|  |  |  | `o_icon_mail` | 80 |
| :o_icon_o_icon_message: | `envelope` | fa-solid | `o_icon_message` | 7 |
|  |  |  | `o_icon_send` | 1 |
| :o_icon_o_icon_message_open: | `envelope-open` | fa-solid | `o_icon_message_open` | 5 |
| :o_icon_o_icon_tb_notification: | `envelope-open-text` | fa-solid | `o_icon_tb_notification` | 2 |
| :o_icon_o_icon_mailto: | `envelope-square` | fa-solid | `o_icon_mailto` | 2 |
| :o_icon_o_icon_eraser: | `eraser` | fa-solid | `o_icon_eraser` | 1 |
|  |  |  | `o_icon_tb_unselect` | 2 |
|  |  |  | `o_middel` | 1 |
| :o_icon_o_icon_qitem_convert: | `exchange` | fa-solid | `o_icon_qitem_convert` | 1 |
|  |  |  | `o_icon_role` | 0 |
| :o_icon_o_icon_exclamation: | `exclamation` | fa-solid | `o_icon_exclamation` | 1 |
|  |  |  | `o_icon_not_available` | 2 |
|  |  |  | `o_icon_todo_priority_high` | 1 |
| :o_icon_o_absences_col_alert: | `exclamation-circle` | fa-solid | `o_absences_col_alert` | 1 |
|  |  |  | `o_grad_assignment_unassigned` | 1 |
|  |  |  | `o_icon_absence_unauthorized` | 1 |
|  |  |  | `o_icon_exclamation_circle` | 1 |
|  |  |  | `o_icon_info_msg` | 4 |
|  |  |  | `o_icon_qti_invalid` | 0 |
|  |  |  | `o_icon_rubric_neutral` | 1 |
|  |  |  | `o_miderr` | 6 |
| :o_icon_o_ac_order_status_warning_icon: | `exclamation-triangle` | fa-solid | `o_ac_order_status_warning_icon` | 1 |
|  |  |  | `o_icon_dispensation_unauthorized` | 1 |
|  |  |  | `o_icon_important` | 35 |
|  |  |  | `o_icon_member_not_valid` | 2 |
|  |  |  | `o_icon_notice_unauthorized` | 1 |
|  |  |  | `o_icon_warn` | 109 |
|  |  |  | `o_icon_warning` | 18 |
|  |  |  | `o_midwarn` | 14 |
| :o_icon_o_icon_expand: | `expand` | fa-solid | `o_icon_expand` | 1 |
|  |  |  | `o_icon_width_expand` | 1 |
| :o_icon_o_FileResource-SHAREDFOLDER: | `external-link` | fa-solid | `o_FileResource-SHAREDFOLDER` | 0 |
|  |  |  | `o_icon_content_popup` | 9 |
|  |  |  | `o_icon_external_link` | 33 |
|  |  |  | `o_icon_link_extern` | 45 |
|  |  |  | `o_tu_icon` | 4 |
| :o_icon_o_ac_offer_active_icon: | `eye` | fa-solid | `o_ac_offer_active_icon` | 1 |
|  |  |  | `o_forum_one_icon` | 1 |
|  |  |  | `o_forum_status_visible_icon` | 1 |
|  |  |  | `o_icon_curriculum_manager` | 1 |
|  |  |  | `o_icon_eye` | 12 |
|  |  |  | `o_icon_master_coach` | 1 |
|  |  |  | `o_icon_preview` | 77 |
|  |  |  | `o_icon_principal` | 1 |
|  |  |  | `o_icon_qti_review` | 0 |
|  |  |  | `o_icon_quickview` | 9 |
|  |  |  | `o_icon_results_visible` | 18 |
| :o_icon_o_ac_offer_inactive_icon: | `eye-slash` | fa-solid | `o_ac_offer_inactive_icon` | 1 |
|  |  |  | `o_ac_offer_not_available_icon` | 1 |
|  |  |  | `o_forum_status_hidden_icon` | 1 |
|  |  |  | `o_icon_eye_slash` | 2 |
|  |  |  | `o_icon_pf_section_draft` | 2 |
|  |  |  | `o_icon_qti_reviewInvalid` | 0 |
|  |  |  | `o_icon_qti_reviewNotAnswered` | 0 |
|  |  |  | `o_icon_qti_reviewNotSeen` | 0 |
|  |  |  | `o_icon_results_hidden` | 25 |
| :o_icon_o_icon_qti_incorrect: | `face-frown-open` | fa-solid | `o_icon_qti_incorrect` | 0 |
| :o_icon_o_icon_qti_correct: | `face-smile-beam` | fa-solid | `o_icon_qti_correct` | 0 |
| :o_icon_o_icon_provider_facebook: | `facebook` | fa-brands | `o_icon_provider_facebook` | 2 |
| :o_icon_o_icon_facebook: | `facebook-square` | fa-brands | `o_icon_facebook` | 1 |
| :o_icon_o_icon_authoring: | `feather-pointed` | fa-solid | `o_icon_authoring` | 2 |
| :o_icon_o_FileResource-FILE_icon: | `file` | fa-regular | `o_FileResource-FILE_icon` | 0 |
|  |  |  | `o_filetype_drawio` | 2 |
|  |  |  | `o_filetype_dwb` | 0 |
|  |  |  | `o_filetype_file` | 44 |
|  |  |  | `o_filetype_ico` | 1 |
|  |  |  | `o_icon_fileupload` | 1 |
|  |  |  | `o_icon_pf_page` | 8 |
|  |  |  | `o_icon_proj_file` | 5 |
|  |  |  | `o_scorm_item` | 2 |
| :o_icon_o_dialog_icon:{: style="padding-right:4px;" } | `file, comment` | fa-regular, fa-solid | `o_dialog_icon` | 6 |
| :o_icon_o_icon_file: | `file` | fa-solid | `o_icon_file` | 3 |
|  |  |  | `o_icon_inspection` | 8 |
|  |  |  | `o_icon_pf_entry` | 3 |
| :o_icon_o_filetype_gz: | `file-archive` | fa-regular | `o_filetype_gz` | 1 |
|  |  |  | `o_filetype_tar` | 1 |
|  |  |  | `o_filetype_tgz` | 1 |
|  |  |  | `o_filetype_zip` | 10 |
| :o_icon_o_icon_file_arrow_up: | `file-arrow-up` | fa-solid | `o_icon_file_arrow_up` | 1 |
| :o_icon_o_FileResource-SOUND_icon: | `file-audio` | fa-regular | `o_FileResource-SOUND_icon` | 0 |
|  |  |  | `o_filetype_audio` | 0 |
|  |  |  | `o_filetype_m3u` | 1 |
|  |  |  | `o_filetype_midi` | 1 |
|  |  |  | `o_filetype_mp3` | 1 |
|  |  |  | `o_filetype_wav` | 1 |
| :o_icon_o_icon_filehub_add: | `file-circle-plus` | fa-solid | `o_icon_filehub_add` | 6 |
| :o_icon_o_ac_order_status_written_off_icon: | `file-circle-xmark` | fa-solid | `o_ac_order_status_written_off_icon` | 3 |
| :o_icon_o_filetype_app: | `file-code` | fa-regular | `o_filetype_app` | 0 |
|  |  |  | `o_filetype_bat` | 1 |
|  |  |  | `o_filetype_bat_icon` | 0 |
|  |  |  | `o_filetype_css` | 1 |
|  |  |  | `o_filetype_exe` | 1 |
|  |  |  | `o_filetype_java` | 0 |
|  |  |  | `o_filetype_js` | 0 |
|  |  |  | `o_filetype_numbers` | 0 |
|  |  |  | `o_filetype_ods` | 1 |
|  |  |  | `o_filetype_sh` | 0 |
|  |  |  | `o_filetype_xml` | 1 |
|  |  |  | `o_filetype_xsl` | 1 |
|  |  |  | `o_icon_translation_item` | 4 |
| :o_icon_o_icon_qti_signature: | `file-code` | fa-solid | `o_icon_qti_signature` | 1 |
| :o_icon_o_FileResource-XLS_icon: | `file-excel` | fa-regular | `o_FileResource-XLS_icon` | 2 |
|  |  |  | `o_filetype_xls` | 12 |
|  |  |  | `o_filetype_xlsx` | 4 |
| :o_icon_o_icon_file_export: | `file-export` | fa-solid | `o_icon_file_export` | 1 |
| :o_icon_o_FileResource-IMAGE_icon: | `file-image` | fa-regular | `o_FileResource-IMAGE_icon` | 0 |
|  |  |  | `o_filetype_bmp` | 1 |
|  |  |  | `o_filetype_eps` | 0 |
|  |  |  | `o_filetype_gif` | 1 |
|  |  |  | `o_filetype_jpeg` | 1 |
|  |  |  | `o_filetype_jpg` | 2 |
|  |  |  | `o_filetype_odg` | 1 |
|  |  |  | `o_filetype_png` | 1 |
|  |  |  | `o_filetype_tiff` | 1 |
|  |  |  | `o_filetype_webp` | 0 |
|  |  |  | `o_icon_layout` | 1 |
| :o_icon_o_icon_file_lines: | `file-lines` | fa-regular | `o_icon_file_lines` | 2 |
| :o_icon_o_icon_courselog: | `file-lines` | fa-solid | `o_icon_courselog` | 3 |
| :o_icon_o_FileResource-PDF_icon: | `file-pdf` | fa-regular | `o_FileResource-PDF_icon` | 0 |
|  |  |  | `o_filetype_pdf` | 47 |
|  |  |  | `o_filetype_ps` | 1 |
|  |  |  | `o_icon_eva_pdf` | 2 |
|  |  |  | `o_icon_qual_ana_pdf` | 1 |
|  |  |  | `o_icon_tool_pdf` | 3 |
| :o_icon_o_FileResource-PPT_icon: | `file-powerpoint` | fa-regular | `o_FileResource-PPT_icon` | 2 |
|  |  |  | `o_filetype_key` | 0 |
|  |  |  | `o_filetype_odp` | 1 |
|  |  |  | `o_filetype_ppt` | 2 |
|  |  |  | `o_filetype_pptx` | 1 |
| :o_icon_o_cp_item: | `file-text` | fa-regular | `o_cp_item` | 3 |
|  |  |  | `o_filetype_README` | 0 |
|  |  |  | `o_filetype_htm` | 1 |
|  |  |  | `o_filetype_html` | 8 |
|  |  |  | `o_filetype_log` | 2 |
|  |  |  | `o_filetype_odf` | 1 |
|  |  |  | `o_filetype_readme` | 1 |
|  |  |  | `o_filetype_rtf` | 1 |
|  |  |  | `o_filetype_txt` | 4 |
|  |  |  | `o_sp_icon` | 6 |
| :o_icon_o_icon_log: | `file-text` | fa-solid | `o_icon_log` | 12 |
|  |  |  | `o_icon_new_document` | 1 |
|  |  |  | `o_page_icon` | 8 |
| :o_icon_o_FileResource-ANIM_icon: | `file-video` | fa-regular | `o_FileResource-ANIM_icon` | 0 |
|  |  |  | `o_FileResource-MOVIE_icon` | 2 |
|  |  |  | `o_filetype_avi` | 1 |
|  |  |  | `o_filetype_dvi` | 1 |
|  |  |  | `o_filetype_flv` | 0 |
|  |  |  | `o_filetype_m4v` | 0 |
|  |  |  | `o_filetype_mov` | 1 |
|  |  |  | `o_filetype_mp4` | 3 |
|  |  |  | `o_filetype_mpeg` | 1 |
|  |  |  | `o_filetype_mpg` | 1 |
|  |  |  | `o_filetype_ogg` | 0 |
|  |  |  | `o_filetype_psd` | 0 |
|  |  |  | `o_filetype_qt` | 1 |
|  |  |  | `o_filetype_ra` | 1 |
|  |  |  | `o_filetype_ram` | 1 |
|  |  |  | `o_filetype_swf` | 0 |
|  |  |  | `o_filetype_video` | 0 |
|  |  |  | `o_filetype_webm` | 0 |
| :o_icon_o_FileResource-DOC_icon: | `file-word` | fa-regular | `o_FileResource-DOC_icon` | 2 |
|  |  |  | `o_filetype_doc` | 3 |
|  |  |  | `o_filetype_docx` | 1 |
|  |  |  | `o_filetype_odt` | 1 |
|  |  |  | `o_filetype_pages` | 0 |
| :o_icon_o_FileResource-VIDEO_icon: | `film` | fa-solid | `o_FileResource-VIDEO_icon` | 1 |
|  |  |  | `o_icon_video` | 24 |
|  |  |  | `o_video_icon` | 6 |
| :o_icon_o_icon_filter: | `filter` | fa-solid | `o_icon_filter` | 3 |
| :o_icon_o_icon_fire: | `fire` | fa-solid | `o_icon_fire` | 1 |
|  |  |  | `o_mi_qtihottext` | 2 |
| :o_icon_o_icon_finished: | `flag-checkered` | fa-solid | `o_icon_finished` | 1 |
| :o_icon_o_icon_banned: | `flask` | fa-solid | `o_icon_banned` | 1 |
|  |  |  | `o_icon_flask` | 1 |
| :o_icon_o_icon_qti_end_testpart: | `floppy-disk` | fa-regular | `o_icon_qti_end_testpart` | 1 |
| :o_icon_o_icon_coursefolder: | `folder` | fa-regular | `o_icon_coursefolder` | 4 |
| :o_icon_o_filetype_folder: | `folder` | fa-solid | `o_filetype_folder` | 16 |
|  |  |  | `o_icon_catalog_sub` | 3 |
| :o_icon_o_FileResource-SHAREDFOLDER_icon: | `folder-open` | fa-regular | `o_FileResource-SHAREDFOLDER_icon` | 3 |
|  |  |  | `o_bc_icon` | 8 |
|  |  |  | `o_icon_taxonomy_level_leaf` | 1 |
|  |  |  | `o_icon_translation_package` | 3 |
| :o_icon_o_icon_mediacenter: | `folder-open` | fa-solid | `o_icon_mediacenter` | 2 |
| :o_icon_o_icon_new_folder: | `folder-plus` | fa-solid | `o_icon_new_folder` | 3 |
| :o_icon_o_icon_text: | `font` | fa-solid | `o_icon_text` | 2 |
| :o_icon_o_icon_slide_forward: | `forward-step` | fa-solid | `o_icon_slide_forward` | 4 |
| :o_icon_o_icon_reviews: | `gauge` | fa-solid | `o_icon_reviews` | 3 |
| :o_icon_o_icon_proj_decision: | `gavel` | fa-solid | `o_icon_proj_decision` | 6 |
| :o_icon_o_icon_customize: | `gear` | fa-solid | `o_icon_customize` | 4 |
|  |  |  | `o_icon_edit_metadata` | 5 |
|  |  |  | `o_icon_gear` | 2 |
|  |  |  | `o_icon_tb_configuration` | 1 |
|  |  |  | `o_icon_tool` | 1 |
| :o_icon_o_icon_qitem_commands: | `gears` | fa-solid | `o_icon_qitem_commands` | 1 |
|  |  |  | `o_icon_settings` | 6 |
|  |  |  | `o_icon_tb_method_auto` | 1 |
|  |  |  | `o_icon_tb_strategy` | 2 |
|  |  |  | `o_icon_tb_strategy_custom` | 1 |
| :o_icon_o_ac_free_icon: | `gift` | fa-solid | `o_ac_free_icon` | 1 |
| :o_icon_o_FileResource-WIKI_icon: | `globe` | fa-solid | `o_FileResource-WIKI_icon` | 0 |
|  |  |  | `o_icon_catalog_extern` | 13 |
|  |  |  | `o_icon_globe` | 3 |
|  |  |  | `o_icon_origin` | 3 |
|  |  |  | `o_wiki_icon` | 10 |
| :o_icon_o_icon_provider_google: | `google` | fa-brands | `o_icon_provider_google` | 2 |
| :o_icon_o_icon_google: | `google-plus-square` | fa-brands | `o_icon_google` | 0 |
| :o_icon_o_FileResource-GLOSSARY_icon: | `graduation-cap` | fa-solid | `o_FileResource-GLOSSARY_icon` | 3 |
|  |  |  | `o_icon_coach` | 11 |
|  |  |  | `o_icon_repo_status_coachpublished` | 0 |
|  |  |  | `o_icon_user_vip` | 5 |
|  |  |  | `o_portlet_repository_teacher_icon` | 0 |
| :o_icon_o_icon_abstain: | `hand` | fa-regular | `o_icon_abstain` | 4 |
| :o_icon_o_icon_pull: | `hand-back-fist` | fa-solid | `o_icon_pull` | 4 |
| :o_icon_o_icon_instruction: | `hand-point-right` | fa-solid | `o_icon_instruction` | 2 |
| :o_icon_o_icon_cns_status_selected: | `hand-point-up` | fa-solid | `o_icon_cns_status_selected` | 1 |
|  |  |  | `o_icon_hand_point_up` | 2 |
|  |  |  | `o_icon_tb_broker_enrollment_in_progress` | 1 |
| :o_icon_o_icon_qual_part_not_available: | `hands-clapping` | fa-solid | `o_icon_qual_part_not_available` | 0 |
| :o_icon_o_icon_disclaimer: | `handshake` | fa-regular | `o_icon_disclaimer` | 8 |
| :o_icon_o_icon_number_of: | `hashtag` | fa-solid | `o_icon_number_of` | 1 |
| :o_icon_o_icon_hdd: | `hdd` | fa-regular | `o_icon_hdd` | 2 |
| :o_icon_o_icon_header: | `header` | fa-solid | `o_icon_header` | 5 |
| :o_icon_o_icon_heart: | `heart` | fa-solid | `o_icon_heart` | 1 |
| :o_icon_o_icon_correction: | `highlighter` | fa-solid | `o_icon_correction` | 10 |
|  |  |  | `o_icon_status_in_review` | 13 |
|  |  |  | `o_lp_in_review` | 1 |
| :o_icon_o_icon_version: | `history` | fa-solid | `o_icon_version` | 7 |
| :o_icon_o_icon_home: | `home` | fa-solid | `o_icon_home` | 39 |
| :o_icon_o_icon_curriculum_status_provisional: | `hourglass` | fa-solid | `o_icon_curriculum_status_provisional` | 0 |
|  |  |  | `o_icon_qual_part_participated` | 2 |
|  |  |  | `o_icon_tb_selection_waiting_list` | 1 |
| :o_icon_o_as_mode_followup: | `hourglass-end` | fa-solid | `o_as_mode_followup` | 1 |
|  |  |  | `o_as_mode_leadtime` | 1 |
|  |  |  | `o_icon_timelimit_end` | 0 |
| :o_icon_o_ac_membership_confirmation_icon: | `hourglass-half` | fa-regular | `o_ac_membership_confirmation_icon` | 2 |
|  |  |  | `o_ac_order_status_inprocess_icon` | 1 |
|  |  |  | `o_ac_order_status_open_icon` | 1 |
|  |  |  | `o_ac_order_status_pending_icon` | 2 |
|  |  |  | `o_ac_order_status_prepayment_icon` | 1 |
| :o_icon_o_icon_candidate: | `hourglass-half` | fa-solid | `o_icon_candidate` | 1 |
|  |  |  | `o_icon_payment_open` | 3 |
|  |  |  | `o_icon_process_scheduled` | 1 |
|  |  |  | `o_icon_timelimit_half` | 3 |
|  |  |  | `o_membership_status_pending` | 2 |
|  |  |  | `o_membership_status_reservation` | 0 |
| :o_icon_o_icon_timelimit_start: | `hourglass-start` | fa-solid | `o_icon_timelimit_start` | 2 |
| :o_icon_o_icon_breadcrumb_root: | `house` | fa-solid | `o_icon_breadcrumb_root` | 1 |
| :o_icon_o_icon_html5: | `html5` | fa-brands | `o_icon_html5` | 1 |
| :o_icon_o_icon_image_comparison: | `image, image` | fa-regular, fa-solid | `o_icon_image_comparison` | 1 |
| :o_icon_o_icon_image: | `image` | fa-solid | `o_icon_image` | 7 |
|  |  |  | `o_icon_media` | 7 |
| :o_icon_o_icon_images: | `images` | fa-solid | `o_icon_images` | 1 |
| :o_icon_o_pf_icon: | `inbox` | fa-solid | `o_pf_icon` | 3 |
| :o_icon_o_icon_openolat: | `infinity` | fa-solid | `o_icon_openolat` | 2 |
|  |  |  | `o_icon_provider_olat` | 4 |
| :o_icon_o_icon_description: | `info-circle` | fa-solid | `o_icon_description` | 21 |
|  |  |  | `o_icon_impress` | 5 |
|  |  |  | `o_icon_info` | 46 |
|  |  |  | `o_icon_info_ap` | 5 |
|  |  |  | `o_icon_info_badge` | 3 |
|  |  |  | `o_icon_info_resource` | 10 |
|  |  |  | `o_icon_news` | 4 |
|  |  |  | `o_infomsg_icon` | 12 |
|  |  |  | `o_portlet_infomsg_icon` | 0 |
| :o_icon_o_portlet_institutions_icon: | `institution` | fa-solid | `o_portlet_institutions_icon` | 0 |
| :o_icon_o_icon_italic: | `italic` | fa-solid | `o_icon_italic` | 1 |
| :o_icon_o_icon_k: | `k` | fa-solid | `o_icon_k` | 5 |
| :o_icon_o_ac_token_icon: | `key` | fa-solid | `o_ac_token_icon` | 4 |
|  |  |  | `o_icon_owner` | 3 |
| :o_icon_o_icon_keyboard: | `keyboard` | fa-regular | `o_icon_keyboard` | 1 |
| :o_icon_o_icon_assessment_mode: | `laptop, pencil` | fa-solid, fa-solid | `o_icon_assessment_mode` | 20 |
| :o_icon_o_icon_instructional_design: | `leaf` | fa-solid | `o_icon_instructional_design` | 2 |
|  |  |  | `o_icon_proj_project` | 16 |
| :o_icon_o_icon_reactivate: | `level-up` | fa-solid | `o_icon_reactivate` | 1 |
| :o_icon_o_icon_details: | `lightbulb` | fa-regular | `o_icon_details` | 48 |
|  |  |  | `o_portlet_dyk_icon` | 0 |
| :o_icon_o_icon_lightbulb: | `lightbulb` | fa-solid | `o_icon_lightbulb` | 4 |
|  |  |  | `o_icon_qti_solution` | 0 |
| :o_icon_o_icon_qual_ana_trend: | `line-chart` | fa-solid | `o_icon_qual_ana_trend` | 2 |
| :o_icon_o_icon_link: | `link` | fa-solid | `o_icon_link` | 20 |
|  |  |  | `o_icon_proj_reference` | 1 |
|  |  |  | `o_ll_icon` | 4 |
|  |  |  | `o_portlet_links_icon` | 0 |
| :o_icon_o_icon_linkedin: | `linkedin` | fa-brands | `o_icon_linkedin` | 3 |
| :o_icon_o_icon_provider_linkedin: | `linkedin-in` | fa-brands | `o_icon_provider_linkedin` | 2 |
| :o_icon_o_icon_list: | `list` | fa-solid | `o_icon_list` | 5 |
|  |  |  | `o_icon_pool_collection` | 3 |
| :o_icon_o_icon_list_check: | `list-check` | fa-solid | `o_icon_list_check` | 1 |
| :o_icon_o_icon_list_num: | `list-ol` | fa-solid | `o_icon_list_num` | 4 |
|  |  |  | `o_mi_qtimatch_truefalse` | 2 |
| :o_icon_o_icon_exact_location: | `location-crosshairs` | fa-solid | `o_icon_exact_location` | 5 |
| :o_icon_o_icon_location: | `location-dot` | fa-solid | `o_icon_location` | 22 |
| :o_icon_o_ac_membersonly_icon: | `lock` | fa-solid | `o_ac_membersonly_icon` | 3 |
|  |  |  | `o_icon_identity_permanent` | 1 |
|  |  |  | `o_icon_locked` | 11 |
|  |  |  | `o_icon_password` | 6 |
|  |  |  | `o_icon_pf_entry_closed` | 2 |
|  |  |  | `o_icon_pf_section_closed` | 2 |
|  |  |  | `o_icon_tb_group_restrictions` | 1 |
|  |  |  | `o_midlock` | 3 |
| :o_icon_o_icon_eva_end_hide: | `long-arrow-right` | fa-solid | `o_icon_eva_end_hide` | 1 |
|  |  |  | `o_icon_todo_date_range` | 1 |
| :o_icon_o_icon_wizard: | `magic` | fa-solid | `o_icon_wizard` | 3 |
| :o_icon_o_icon_magnifying_glass: | `magnifying-glass` | fa-solid | `o_icon_magnifying_glass` | 4 |
| :o_icon_o_icon_search_lookup: | `magnifying-glass-plus` | fa-solid | `o_icon_search_lookup` | 1 |
| :o_icon_o_icon_node_under: | `mail-reply` | fa-solid | `o_icon_node_under` | 3 |
| :o_icon_o_mi_qtihotspot: | `map` | fa-regular | `o_mi_qtihotspot` | 2 |
| :o_icon_o_icon_learning_path: | `map-signs` | fa-solid | `o_icon_learning_path` | 15 |
|  |  |  | `o_midlpexob` | 3 |
| :o_icon_o_icon_statement: | `medal` | fa-solid | `o_icon_statement` | 3 |
|  |  |  | `o_icon_success_status` | 6 |
| :o_icon_o_FileResource-SURVEY_icon: | `meh` | fa-regular | `o_FileResource-SURVEY_icon` | 0 |
|  |  |  | `o_iqsurv_icon` | 5 |
| :o_icon_o_icon_audio_record: | `microphone` | fa-solid | `o_icon_audio_record` | 8 |
| :o_icon_o_ac_status_canceled_icon: | `minus` | fa-solid | `o_ac_status_canceled_icon` | 2 |
|  |  |  | `o_icon_minus` | 2 |
|  |  |  | `o_icon_not_identified` | 1 |
|  |  |  | `o_icon_table_details_collaps` | 2 |
| :o_icon_o_icon_delete: | `minus-circle` | fa-solid | `o_icon_delete` | 33 |
|  |  |  | `o_icon_member_skipped` | 2 |
| :o_icon_o_icon_check_mixed: | `minus-square` | fa-regular | `o_icon_check_mixed` | 2 |
| :o_icon_o_icon_review_remove: | `minus-square` | fa-solid | `o_icon_review_remove` | 0 |
| :o_icon_o_icon_mobile: | `mobile` | fa-solid | `o_icon_mobile` | 1 |
| :o_icon_o_icon_pay: | `money-bill-1` | fa-solid | `o_icon_pay` | 3 |
| :o_icon_o_icon_pointer: | `mouse-pointer` | fa-solid | `o_icon_pointer` | 1 |
| :o_icon_o_icon_tb_selection_not_enrolled: | `n` | fa-solid | `o_icon_tb_selection_not_enrolled` | 1 |
| :o_icon_o_icon_pf_section: | `navicon` | fa-solid | `o_icon_pf_section` | 7 |
| :o_icon_o_CourseModuleTemplate_icon: | `object-group` | fa-solid | `o_CourseModuleTemplate_icon` | 1 |
|  |  |  | `o_icon_template` | 6 |
| :o_icon_o_icon_provider_openid: | `openid` | fa-brands | `o_icon_provider_openid` | 1 |
| :o_icon_o_icon_brush: | `paint-brush` | fa-solid | `o_icon_brush` | 1 |
|  |  |  | `o_icon_proj_whiteboard` | 1 |
|  |  |  | `o_mi_qtidrawing` | 2 |
| :o_icon_o_icon_show_send: | `paper-plane` | fa-regular | `o_icon_show_send` | 4 |
|  |  |  | `o_portlet_quickstart_icon` | 0 |
| :o_icon_o_icon_paperclip: | `paperclip` | fa-solid | `o_icon_paperclip` | 1 |
| :o_icon_o_icon_paragraph: | `paragraph` | fa-solid | `o_icon_paragraph` | 0 |
| :o_icon_o_icon_certification_status_inactive: | `pause` | fa-solid | `o_icon_certification_status_inactive` | 0 |
|  |  |  | `o_icon_qti_suspend` | 2 |
| :o_icon_o_icon_identity_inactive: | `pause-circle` | fa-regular | `o_icon_identity_inactive` | 2 |
| :o_icon_o_icon_curriculum_status_preparation: | `pen` | fa-solid | `o_icon_curriculum_status_preparation` | 0 |
| :o_icon_o_icon_changes: | `pencil` | fa-solid | `o_icon_changes` | 11 |
|  |  |  | `o_icon_new_portfolio` | 14 |
|  |  |  | `o_icon_overridden` | 2 |
|  |  |  | `o_icon_pencil` | 4 |
|  |  |  | `o_icon_pf_entry_draft` | 2 |
|  |  |  | `o_icon_pf_new_entry` | 1 |
|  |  |  | `o_icon_qitem_draft` | 2 |
|  |  |  | `o_icon_rename` | 1 |
|  |  |  | `o_icon_repo_status_preparation` | 0 |
| :o_icon_o_FileResource-IMSQTI21_icon: | `pencil-square` | fa-solid | `o_FileResource-IMSQTI21_icon` | 4 |
|  |  |  | `o_FileResource-TEST_icon` | 1 |
|  |  |  | `o_iqself_icon` | 3 |
|  |  |  | `o_iqtest_icon` | 5 |
|  |  |  | `o_qtiassessment_icon` | 12 |
| :o_icon_o_icon_people: | `people-group` | fa-solid | `o_icon_people` | 4 |
| :o_icon_o_icon_room_management: | `person-chalkboard` | fa-solid | `o_icon_room_management` | 2 |
| :o_icon_o_icon_non_members: | `person-circle-minus` | fa-solid | `o_icon_non_members` | 1 |
| :o_icon_o_icon_provider_guest: | `person-rays` | fa-solid | `o_icon_provider_guest` | 1 |
| :o_icon_o_icon_phone: | `phone` | fa-solid | `o_icon_phone` | 3 |
| :o_icon_o_icon_assessment_inspection_active: | `play` | fa-solid | `o_icon_assessment_inspection_active` | 2 |
|  |  |  | `o_icon_certification_resume` | 0 |
|  |  |  | `o_icon_ms_pending` | 0 |
|  |  |  | `o_icon_play` | 3 |
|  |  |  | `o_icon_qual_part_execute` | 2 |
|  |  |  | `o_icon_status_in_progress` | 7 |
|  |  |  | `o_icon_tb_run_start` | 2 |
|  |  |  | `o_icon_video_play` | 6 |
|  |  |  | `o_icon_video_resume` | 1 |
| :o_icon_o_icon_qual_dc_ready: | `play-circle` | fa-regular | `o_icon_qual_dc_ready` | 1 |
|  |  |  | `o_icon_qual_exec_ready` | 0 |
|  |  |  | `o_lp_in_progress` | 1 |
| :o_icon_o_icon_qual_dc_running: | `play-circle` | fa-solid | `o_icon_qual_dc_running` | 1 |
|  |  |  | `o_icon_qual_exec_participating` | 0 |
| :o_icon_o_icon_not_correct_plus: | `plus` | fa-solid | `o_icon_not_correct_plus` | 1 |
|  |  |  | `o_icon_plus` | 5 |
|  |  |  | `o_icon_table_details_expand` | 3 |
| :o_icon_o_icon_add: | `plus-circle` | fa-solid | `o_icon_add` | 219 |
|  |  |  | `o_icon_lic_add` | 1 |
|  |  |  | `o_icon_qual_dc_create` | 1 |
|  |  |  | `o_icon_qual_gen_ce_add` | 1 |
|  |  |  | `o_icon_qual_gen_create` | 1 |
|  |  |  | `o_icon_qual_gen_re_add` | 1 |
| :o_icon_o_icon_review_add: | `plus-square` | fa-solid | `o_icon_review_add` | 0 |
| :o_icon_o_FileResource-PODCAST_icon: | `podcast` | fa-solid | `o_FileResource-PODCAST_icon` | 0 |
|  |  |  | `o_podcast_icon` | 10 |
| :o_icon_o_icon_close_resource: | `power-off` | fa-solid | `o_icon_close_resource` | 2 |
|  |  |  | `o_icon_lifecycle` | 0 |
| :o_icon_o_icon_eva_print: | `print` | fa-solid | `o_icon_eva_print` | 2 |
|  |  |  | `o_icon_print` | 21 |
|  |  |  | `o_icon_private` | 0 |
|  |  |  | `o_icon_qual_ana_print` | 2 |
| :o_icon_o_icon_eportfolio_add: | `puzzle-piece` | fa-solid | `o_icon_eportfolio_add` | 5 |
|  |  |  | `o_icon_eportfolio_link` | 0 |
| :o_icon_o_icon_q: | `q` | fa-solid | `o_icon_q` | 5 |
| :o_icon_o_icon_qrcode: | `qrcode` | fa-solid | `o_icon_qrcode` | 22 |
| :o_icon_o_icon_immunity_proof_claimed: | `question` | fa-solid | `o_icon_immunity_proof_claimed` | 1 |
|  |  |  | `o_icon_question` | 3 |
|  |  |  | `o_icon_unselected` | 0 |
|  |  |  | `o_icon_user_anonymous` | 3 |
| :o_icon_o_icon_help: | `question-circle` | fa-solid | `o_icon_help` | 58 |
|  |  |  | `o_icon_qti_hint` | 1 |
| :o_icon_o_icon_citation: | `quote-left` | fa-solid | `o_icon_citation` | 4 |
| :o_icon_o_icon_quote_right: | `quote-right` | fa-solid | `o_icon_quote_right` | 1 |
| :o_icon_o_icon_radiation: | `radiation` | fa-solid | `o_icon_radiation` | 0 |
| :o_icon_o_icon_shuffle: | `random` | fa-solid | `o_icon_shuffle` | 7 |
| :o_icon_o_ac_invoice_icon: | `receipt` | fa-solid | `o_ac_invoice_icon` | 1 |
| :o_icon_o_icon_recycle: | `recycle` | fa-solid | `o_icon_recycle` | 5 |
| :o_icon_o_grad_assignment_inprocess: | `refresh` | fa-solid | `o_grad_assignment_inprocess` | 1 |
|  |  |  | `o_icon_calendar_sync` | 3 |
|  |  |  | `o_icon_extend` | 2 |
|  |  |  | `o_icon_pf_section_progress` | 2 |
|  |  |  | `o_icon_proj_recurrence` | 1 |
|  |  |  | `o_icon_refresh` | 31 |
|  |  |  | `o_icon_response_feedback` | 0 |
|  |  |  | `o_icon_update` | 1 |
| :o_icon_o_icon_qual_gen_enabled: | `repeat` | fa-solid | `o_icon_qual_gen_enabled` | 8 |
|  |  |  | `o_icon_redo` | 2 |
|  |  |  | `o_icon_video_replay` | 1 |
| :o_icon_o_icon_reopen: | `reply` | fa-solid | `o_icon_reopen` | 6 |
|  |  |  | `o_icon_reply` | 2 |
| :o_icon_o_icon_reply_with_quote: | `reply-all` | fa-solid | `o_icon_reply_with_quote` | 1 |
| :o_icon_o_icon_managed: | `retweet` | fa-solid | `o_icon_managed` | 24 |
| :o_icon_o_icon_right_left: | `right-left` | fa-solid | `o_icon_right_left` | 1 |
| :o_icon_o_icon_attempts: | `rotate-left` | fa-solid | `o_icon_attempts` | 2 |
|  |  |  | `o_icon_pf_entry_revision` | 2 |
|  |  |  | `o_icon_qitem_revised` | 2 |
|  |  |  | `o_icon_revoke` | 1 |
|  |  |  | `o_icon_tb_withdraw` | 5 |
| :o_icon_o_icon_certification_status_recertifying: | `rotate-right` | fa-solid | `o_icon_certification_status_recertifying` | 1 |
|  |  |  | `o_icon_retry` | 6 |
|  |  |  | `o_icon_tb_enroll` | 2 |
|  |  |  | `o_icon_tb_run` | 1 |
| :o_icon_o_icon_notification: | `rss` | fa-solid | `o_icon_notification` | 6 |
|  |  |  | `o_icon_rss` | 9 |
|  |  |  | `o_icon_rss_unsubscribe` | 0 |
|  |  |  | `o_portlet_noti_icon` | 0 |
| :o_icon_o_icon_s: | `s` | fa-solid | `o_icon_s` | 5 |
| :o_icon_o_icon_save: | `save` | fa-solid | `o_icon_save` | 5 |
| :o_icon_o_icon_tb_priority: | `scale-balanced` | fa-solid | `o_icon_tb_priority` | 2 |
|  |  |  | `o_icon_tb_strategy_max_priorities` | 1 |
| :o_icon_o_icon_score_unbalanced: | `scale-unbalanced-flip` | fa-solid | `o_icon_score_unbalanced` | 3 |
| :o_icon_o_icon_activity_log: | `scroll` | fa-solid | `o_icon_activity_log` | 1 |
| :o_icon_o_icon_empty_indicator: | `search` | fa-solid | `o_icon_empty_indicator` | 6 |
|  |  |  | `o_icon_search` | 49 |
| :o_icon_o_icon_shrink: | `search-minus` | fa-solid | `o_icon_shrink` | 1 |
| :o_icon_o_icon_add_search: | `search-plus` | fa-solid | `o_icon_add_search` | 1 |
|  |  |  | `o_icon_browse` | 5 |
|  |  |  | `o_icon_enlarge` | 10 |
| :o_icon_o_icon_legal_folder: | `section` | fa-solid | `o_icon_legal_folder` | 3 |
| :o_icon_o_icon_pf_page_shared: | `share` | fa-solid | `o_icon_pf_page_shared` | 2 |
|  |  |  | `o_icon_pf_quick_links` | 0 |
|  |  |  | `o_icon_publish` | 3 |
|  |  |  | `o_icon_qitem_share` | 1 |
|  |  |  | `o_icon_share` | 2 |
| :o_icon_o_icon_pf_my_shares: | `share-alt` | fa-solid | `o_icon_pf_my_shares` | 1 |
| :o_icon_o_icon_pf_shared_with_me: | `share-alt-square` | fa-solid | `o_icon_pf_shared_with_me` | 1 |
|  |  |  | `o_icon_pool_pool` | 5 |
|  |  |  | `o_icon_share_alt` | 1 |
| :o_icon_o_icon_export: | `share-square` | fa-regular | `o_icon_export` | 21 |
| :o_icon_o_icon_share_social: | `share-square` | fa-solid | `o_icon_share_social` | 1 |
| :o_icon_o_icon_competences: | `shield` | fa-solid | `o_icon_competences` | 10 |
| :o_icon_o_icon_booking: | `shopping-cart` | fa-solid | `o_icon_booking` | 10 |
| :o_icon_o_icon_tb_method: | `shuffle` | fa-solid | `o_icon_tb_method` | 1 |
| :o_icon_o_en_icon: | `sign-in` | fa-solid | `o_en_icon` | 5 |
|  |  |  | `o_icon_login` | 12 |
|  |  |  | `o_portlet_shibboleth_icon` | 0 |
| :o_icon_o_icon_logout: | `sign-out` | fa-solid | `o_icon_logout` | 1 |
|  |  |  | `o_icon_sign_out` | 2 |
| :o_icon_o_icon_catalog: | `sitemap` | fa-solid | `o_icon_catalog` | 5 |
|  |  |  | `o_icon_levels` | 6 |
|  |  |  | `o_icon_sitemap` | 2 |
|  |  |  | `o_icon_structure` | 15 |
|  |  |  | `o_icon_taxonomy_levels` | 2 |
| :o_icon_o_FileResource-FORM_icon: | `sliders` | fa-solid | `o_FileResource-FORM_icon` | 4 |
|  |  |  | `o_icon_rubric` | 1 |
|  |  |  | `o_survey_icon` | 2 |
| :o_icon_o_practice_icon: | `soccer-ball` | fa-regular | `o_practice_icon` | 4 |
| :o_icon_o_icon_sort: | `sort` | fa-solid | `o_icon_sort` | 1 |
| :o_icon_o_icon_sort_amount_asc: | `sort-amount-asc` | fa-solid | `o_icon_sort_amount_asc` | 3 |
|  |  |  | `o_icon_sort_menu` | 2 |
| :o_icon_o_icon_sort_amount_desc: | `sort-amount-desc` | fa-solid | `o_icon_sort_amount_desc` | 4 |
| :o_icon_o_icon_sort_asc: | `sort-asc` | fa-solid | `o_icon_sort_asc` | 4 |
| :o_icon_o_icon_sort_desc: | `sort-desc` | fa-solid | `o_icon_sort_desc` | 4 |
| :o_icon_o_as_mode_assessment: | `spinner` | fa-solid | `o_as_mode_assessment` | 1 |
|  |  |  | `o_icon_assessment_inspection_inprogress` | 2 |
|  |  |  | `o_icon_busy` | 6 |
|  |  |  | `o_icon_pending` | 4 |
|  |  |  | `o_icon_process_running` | 1 |
| :o_icon_o_grad_assignment_assigned: | `square` | fa-regular | `o_grad_assignment_assigned` | 2 |
|  |  |  | `o_icon_calendar_disabled` | 6 |
|  |  |  | `o_icon_check_off` | 14 |
|  |  |  | `o_icon_checkbox` | 1 |
|  |  |  | `o_icon_pool_private` | 2 |
|  |  |  | `o_icon_quiz_multiple_choice_off` | 4 |
|  |  |  | `o_icon_rectangle` | 3 |
| :o_icon_o_icon_single_element: | `square` | fa-solid | `o_icon_single_element` | 2 |
|  |  |  | `o_icon_square` | 3 |
| :o_icon_o_icon_show_more: | `square-caret-down` | fa-regular | `o_icon_show_more` | 0 |
| :o_icon_o_icon_show_less: | `square-caret-up` | fa-regular | `o_icon_show_less` | 0 |
| :o_icon_o_icon_math: | `square-root-variable` | fa-solid | `o_icon_math` | 3 |
| :o_icon_o_icon_square_rss: | `square-rss` | fa-solid | `o_icon_square_rss` | 1 |
| :o_icon_o_icon_curriculum_implementations: | `square-share-nodes` | fa-solid | `o_icon_curriculum_implementations` | 11 |
|  |  |  | `o_icon_taxonomy_level_type` | 1 |
| :o_icon_o_icon_twitter: | `square-x-twitter` | fa-brands | `o_icon_twitter` | 1 |
| :o_icon_o_icon_qitem_review: | `star` | fa-regular | `o_icon_qitem_review` | 2 |
|  |  |  | `o_icon_rating_off` | 7 |
|  |  |  | `o_icon_repo_status_review` | 0 |
| :o_icon_o_icon_default_config: | `star` | fa-solid | `o_icon_default_config` | 1 |
|  |  |  | `o_icon_grade` | 8 |
|  |  |  | `o_icon_others` | 0 |
|  |  |  | `o_icon_rating_on` | 2 |
|  |  |  | `o_icon_review` | 3 |
|  |  |  | `o_icon_star` | 4 |
|  |  |  | `o_portlet_iframe_icon` | 0 |
| :o_icon_o_icon_reset: | `step-backward` | fa-solid | `o_icon_reset` | 4 |
| :o_icon_o_icon_notes_empty: | `sticky-note` | fa-regular | `o_icon_notes_empty` | 1 |
|  |  |  | `o_icon_proj_note` | 7 |
|  |  |  | `o_portlet_notes_icon` | 0 |
| :o_icon_o_icon_educational_type: | `sticky-note` | fa-solid | `o_icon_educational_type` | 0 |
|  |  |  | `o_icon_notes` | 18 |
| :o_icon_o_as_mode_stop: | `stop` | fa-solid | `o_as_mode_stop` | 3 |
|  |  |  | `o_icon_qti_cancel` | 1 |
| :o_icon_o_icon_fake_participant: | `street-view` | fa-solid | `o_icon_fake_participant` | 2 |
| :o_icon_o_icon_report: | `table` | fa-solid | `o_icon_report` | 1 |
|  |  |  | `o_mi_qtimatch` | 2 |
| :o_icon_o_icon_name: | `table-cells-large` | fa-solid | `o_icon_name` | 1 |
| :o_icon_o_icon_table: | `table-list` | fa-solid | `o_icon_table` | 13 |
| :o_icon_o_portlet_sysinfo_icon: | `tachometer` | fa-solid | `o_portlet_sysinfo_icon` | 0 |
| :o_icon_o_icon_tag: | `tag` | fa-solid | `o_icon_tag` | 3 |
| :o_icon_o_icon_tags: | `tags` | fa-solid | `o_icon_tags` | 12 |
| :o_icon_o_gta_icon: | `tasks` | fa-solid | `o_gta_icon` | 7 |
|  |  |  | `o_ta_icon` | 3 |
| :o_icon_o_icon_table_large: | `th-large` | fa-solid | `o_icon_table_large` | 0 |
| :o_icon_o_icon_qual_ana_pres_edit: | `thumb-tack` | fa-solid | `o_icon_qual_ana_pres_edit` | 1 |
| :o_icon_o_icon_decline: | `thumbs-down` | fa-regular | `o_icon_decline` | 14 |
|  |  |  | `o_icon_rating_no_off` | 0 |
| :o_icon_o_icon_rating_no_on: | `thumbs-down` | fa-solid | `o_icon_rating_no_on` | 0 |
|  |  |  | `o_icon_rejected` | 5 |
|  |  |  | `o_icon_revision` | 1 |
| :o_icon_o_icon_accepted: | `thumbs-up` | fa-regular | `o_icon_accepted` | 18 |
|  |  |  | `o_icon_rating_yes_off` | 0 |
|  |  |  | `o_ms_icon` | 3 |
| :o_icon_o_icon_browsercheck: | `thumbs-up` | fa-solid | `o_icon_browsercheck` | 0 |
|  |  |  | `o_icon_pending_confirmations` | 2 |
|  |  |  | `o_icon_rating_yes_on` | 0 |
|  |  |  | `o_icon_restore` | 10 |
| :o_icon_o_icon_thumbtack: | `thumbtack` | fa-solid | `o_icon_thumbtack` | 1 |
| :o_icon_o_icon_timeline: | `timeline` | fa-solid | `o_icon_timeline` | 2 |
| :o_icon_o_ac_status_error_icon: | `times` | fa-solid | `o_ac_status_error_icon` | 2 |
|  |  |  | `o_icon_absence` | 2 |
|  |  |  | `o_icon_addremove_remove` | 1 |
|  |  |  | `o_icon_close` | 13 |
|  |  |  | `o_icon_close_tab` | 1 |
|  |  |  | `o_icon_close_tool` | 1 |
|  |  |  | `o_icon_immunity_proof_none` | 1 |
|  |  |  | `o_icon_not_correct` | 4 |
|  |  |  | `o_icon_progress_danger` | 0 |
|  |  |  | `o_icon_reject` | 2 |
|  |  |  | `o_icon_remove` | 15 |
|  |  |  | `o_icon_review_removed` | 3 |
| :o_icon_o_icon_incorrect_response: | `times-circle` | fa-regular | `o_icon_incorrect_response` | 0 |
|  |  |  | `o_icon_qual_exec_future` | 1 |
|  |  |  | `o_icon_status_unavailable` | 18 |
| :o_icon_o_icon_failed: | `times-circle` | fa-solid | `o_icon_failed` | 26 |
|  |  |  | `o_icon_qti_summary_ended` | 2 |
|  |  |  | `o_icon_qual_exec_over` | 0 |
|  |  |  | `o_icon_quiz_single_choice_incorrect` | 2 |
|  |  |  | `o_icon_remove_filters` | 8 |
|  |  |  | `o_icon_rubric_insufficient` | 1 |
| :o_icon_o_icon_quiz_multiple_choice_incorrect: | `times-square` | fa-solid | `o_icon_quiz_multiple_choice_incorrect` | 2 |
| :o_icon_o_icon_color_picker: | `tint` | fa-solid | `o_icon_color_picker` | 0 |
|  |  |  | `o_icon_draw_color` | 7 |
| :o_icon_o_icon_qitem_show_metadata: | `toggle-off` | fa-solid | `o_icon_qitem_show_metadata` | 1 |
|  |  |  | `o_icon_qual_ana_show_filter` | 1 |
|  |  |  | `o_icon_toggle_off` | 4 |
| :o_icon_o_icon_options: | `toggle-on` | fa-solid | `o_icon_options` | 0 |
|  |  |  | `o_icon_qitem_hide_metadata` | 1 |
|  |  |  | `o_icon_qual_ana_hide_filter` | 1 |
|  |  |  | `o_icon_toggle_on` | 5 |
| :o_icon_o_icon_qitem_endOfLife: | `trash` | fa-solid | `o_icon_qitem_endOfLife` | 2 |
|  |  |  | `o_membership_status_resourcedeleted` | 1 |
| :o_icon_o_icon_businessgroup_status_deleted: | `trash-can` | fa-regular | `o_icon_businessgroup_status_deleted` | 0 |
|  |  |  | `o_icon_businessgroup_status_trash` | 0 |
|  |  |  | `o_icon_clear_all` | 4 |
|  |  |  | `o_icon_delete_item` | 173 |
|  |  |  | `o_icon_deleted` | 18 |
|  |  |  | `o_icon_identity_deleted` | 2 |
|  |  |  | `o_icon_pf_entry_deleted` | 3 |
|  |  |  | `o_icon_pf_trash` | 2 |
|  |  |  | `o_icon_proj_project_status_deleted` | 2 |
|  |  |  | `o_icon_qitem_delete` | 1 |
|  |  |  | `o_icon_qual_dc_delete` | 1 |
|  |  |  | `o_icon_qual_gen_delete` | 1 |
|  |  |  | `o_icon_repo_status_trash` | 2 |
|  |  |  | `o_icon_rm_status_deleted` | 0 |
|  |  |  | `o_icon_todo_status_deleted` | 1 |
|  |  |  | `o_icon_trash` | 10 |
| :o_icon_o_icon_curriculum_status_deleted: | `trash-can` | fa-solid | `o_icon_curriculum_status_deleted` | 0 |
| :o_icon_o_icon_certification_status_expired_renewable: | `triangle-exclamation` | fa-solid | `o_icon_certification_status_expired_renewable` | 0 |
|  |  |  | `o_icon_recertification_warning` | 5 |
|  |  |  | `o_icon_triangle_exclamation` | 2 |
|  |  |  | `o_icon_validation_warning` | 19 |
| :o_icon_o_icon_assessment_tool: | `trophy` | fa-solid | `o_icon_assessment_tool` | 16 |
|  |  |  | `o_icon_score` | 11 |
|  |  |  | `o_icon_trophy` | 2 |
| :o_icon_o_gotomeeting_icon: | `tv` | fa-solid | `o_gotomeeting_icon` | 4 |
|  |  |  | `o_openmeetings_icon` | 5 |
|  |  |  | `o_vc_icon` | 31 |
|  |  |  | `o_vitero_icon` | 3 |
| :o_icon_o_icon_reload: | `undo` | fa-solid | `o_icon_reload` | 6 |
|  |  |  | `o_icon_reset_data` | 11 |
|  |  |  | `o_icon_undo` | 0 |
| :o_icon_o_icon_disadvantage_compensation: | `universal-access` | fa-solid | `o_icon_disadvantage_compensation` | 20 |
| :o_icon_o_icon_lrm: | `university` | fa-solid | `o_icon_lrm` | 1 |
|  |  |  | `o_icon_provider_datenlotsen` | 2 |
|  |  |  | `o_icon_provider_ldap` | 1 |
|  |  |  | `o_icon_provider_shibboleth` | 2 |
|  |  |  | `o_icon_provider_switch_eduid` | 2 |
|  |  |  | `o_library_icon` | 1 |
| :o_icon_o_icon_split: | `unlink` | fa-solid | `o_icon_split` | 1 |
| :o_icon_o_icon_unlocked: | `unlock` | fa-solid | `o_icon_unlocked` | 1 |
| :o_icon_o_lti_icon: | `up-right-from-square` | fa-solid | `o_lti_icon` | 4 |
| :o_icon_o_icon_import: | `upload` | fa-solid | `o_icon_import` | 29 |
|  |  |  | `o_icon_qitem_import` | 1 |
|  |  |  | `o_icon_upload` | 26 |
|  |  |  | `o_mi_qtiupload` | 2 |
| :o_icon_o_icon_pool_my_items: | `user` | fa-solid | `o_icon_pool_my_items` | 1 |
|  |  |  | `o_icon_tb_method_namually` | 1 |
|  |  |  | `o_icon_user` | 104 |
| :o_icon_o_ac_membership_standard_icon: | `user-check` | fa-solid | `o_ac_membership_standard_icon` | 2 |
| :o_icon_o_ac_guests_icon: | `user-circle` | fa-regular | `o_ac_guests_icon` | 3 |
| :o_icon_o_ac_guest_icon: | `user-circle` | fa-solid | `o_ac_guest_icon` | 3 |
|  |  |  | `o_icon_profile` | 2 |
| :o_icon_o_icon_graduate: | `user-graduate` | fa-solid | `o_icon_graduate` | 1 |
| :o_icon_o_icon_num_participants: | `user-group` | fa-solid | `o_icon_num_participants` | 6 |
| :o_icon_o_icon_assessment_inspection_noshow: | `user-large-slash` | fa-solid | `o_icon_assessment_inspection_noshow` | 0 |
| :o_icon_o_icon_reviewer: | `user-md` | fa-solid | `o_icon_reviewer` | 2 |
| :o_icon_o_icon_exclude_member: | `user-minus` | fa-solid | `o_icon_exclude_member` | 2 |
| :o_icon_o_icon_add_member: | `user-plus` | fa-solid | `o_icon_add_member` | 25 |
| :o_icon_o_icon_provider_keycloak: | `user-secret` | fa-solid | `o_icon_provider_keycloak` | 1 |
|  |  |  | `o_mi_qtiunkown` | 5 |
|  |  |  | `o_unkown_icon` | 1 |
| :o_icon_o_icon_user_authentication: | `user-shield` | fa-solid | `o_icon_user_authentication` | 3 |
| :o_icon_o_icon_manager: | `user-tie` | fa-solid | `o_icon_manager` | 2 |
| :o_icon_o_icon_remove_member: | `user-times` | fa-solid | `o_icon_remove_member` | 2 |
| :o_icon_o_ac_group_icon: | `users` | fa-regular | `o_ac_group_icon` | 3 |
| :o_icon_o_BusinessGroup_icon: | `users` | fa-solid | `o_BusinessGroup_icon` | 0 |
|  |  |  | `o_cmembers_icon` | 4 |
|  |  |  | `o_icon_committee` | 3 |
|  |  |  | `o_icon_group` | 118 |
|  |  |  | `o_icon_membersmanagement` | 8 |
|  |  |  | `o_icon_pool_share` | 5 |
|  |  |  | `o_portlet_groups_icon` | 0 |
| :o_icon_o_icon_v: | `v` | fa-solid | `o_icon_v` | 1 |
| :o_icon_o_icon_video_record: | `video-camera` | fa-solid | `o_icon_video_record` | 10 |
|  |  |  | `o_livestream_icon` | 6 |
| :o_icon_o_icon_audio: | `volume-up` | fa-solid | `o_icon_audio` | 2 |
| :o_icon_o_icon_ai: | `wand-magic-sparkles` | fa-solid | `o_icon_ai` | 9 |
|  |  |  | `o_icon_eva_coach_apply` | 1 |
|  |  |  | `o_icon_qitem_aiDraft` | 1 |
| :o_icon_o_absences_col_warning: | `warning` | fa-solid | `o_absences_col_warning` | 1 |
|  |  |  | `o_scorm_failed` | 0 |
|  |  |  | `o_scorm_incomplete` | 0 |
| :o_icon_o_icon_accessibility: | `wheelchair` | fa-solid | `o_icon_accessibility` | 0 |
| :o_icon_o_icon_qti_close_results: | `window-close` | fa-solid | `o_icon_qti_close_results` | 1 |
|  |  |  | `o_icon_qti_close_test` | 1 |
| :o_icon_o_icon_provider_adfs: | `windows` | fa-brands | `o_icon_provider_adfs` | 6 |
|  |  |  | `o_teamsmeeting_icon` | 1 |
| :o_icon_o_icon_tools: | `wrench` | fa-solid | `o_icon_tools` | 3 |
| :o_icon_o_icon_provider_twitter: | `x-twitter` | fa-brands | `o_icon_provider_twitter` | 2 |
| :o_icon_o_icon_xing: | `xing` | fa-brands | `o_icon_xing` | 1 |
| :o_icon_o_icon_yahoo: | `yahoo` | fa-brands | `o_icon_yahoo` | 0 |
| :o_icon_o_icon_lic_youtube: | `youtube-square` | fa-brands | `o_icon_lic_youtube` | 2 |
|  |  |  | `o_icon_youtube` | 4 |
