---
title: Admin manual
description: The OpenOlat admin manual with the path to a running installation, the three phases knowledge, apply and deepen, and what is new in release 21.0.
hide:
  - toc
---

# Admin manual {: #admin_manual}

<p class="oo-mh-lede">How you configure, extend and operate an OpenOlat instance. Every chapter starts at the place in the administration where the setting lives.</p>
<p class="oo-mh-meta">Release 21.0 · Reference</p>

!!! note "Installation chapter"

    The chapter "Installation and operation" is available in English only.

## The path to a running installation {: #path}

<p class="oo-mh-role__text">Five stations from the basic settings to a connected installation.</p>

<!-- gen:authoring_path_tiles -->
<div class="oo-mh-stations" markdown>

1. [Set up <small>System and appearance</small>](admin_path/einrichten.md)
1. [Access <small>Who may enter</small>](admin_path/zugang.md)
1. [Roles <small>Accounts and organisation</small>](admin_path/rollen.md)
1. [Modules <small>Enable functions</small>](admin_path/module.md)
1. [Assess and connect <small>Exams and external tools</small>](admin_path/anbinden.md)

</div>
<!-- /gen:authoring_path_tiles -->

<p class="oo-mh-go" markdown>[<i class="o_icon o_icon_start" aria-hidden="true"></i> Open the whole path](admin_path/index.md)</p>

## How you get to a running installation {: #phases}

Three phases. frentix is there for you in each of them, and in each you can also continue on your own.

<div class="oo-mh-phasecards" markdown>

<article class="oo-mh-pcard oo-mh-pcard--know" markdown>

<div class="oo-mh-pcard__band"><span class="oo-mh-pcard__kicker">Knowledge</span><h3>Before you start</h3></div>

<div class="oo-mh-pcard__body" markdown>

Read what there is and what it is for. The path to a running installation explains the terms of the administration and shows what is easily confused.

[<i class="o_icon o_icon_start" aria-hidden="true"></i> The path to a running installation](admin_path/index.md){ .oo-mh-pcard__go }

</div>

</article>

<article class="oo-mh-pcard oo-mh-pcard--apply" markdown>

<div class="oo-mh-pcard__band"><span class="oo-mh-pcard__kicker">Apply</span><h3>Set up the installation</h3></div>

<div class="oo-mh-pcard__body" markdown>

You operate OpenOlat yourself? The installation guide leads from the database to the first login. Sophia helps along the way.

[<i class="o_icon o_icon_start" aria-hidden="true"></i> Installation guide](installation/installGuide.md){ .oo-mh-pcard__go }

<p class="oo-mh-pcard__aside" markdown>Rather a ready instance? frentix operates OpenOlat for you and offers training, workshops and coaching for the setup.<br>[support@frentix.com](mailto:support@frentix.com)</p>

</div>

</article>

<article class="oo-mh-pcard oo-mh-pcard--deepen" markdown>

<div class="oo-mh-pcard__band"><span class="oo-mh-pcard__kicker">Deepen</span><h3>Improve the installation</h3></div>

<div class="oo-mh-pcard__body" markdown>

Once the installation is running: read reports, set up lifecycles, adapt the wording of the interface, connect other systems.

[<i class="o_icon o_icon_start" aria-hidden="true"></i> Reports](administration/Reports.md){ .oo-mh-pcard__go }
[<i class="o_icon o_icon_start" aria-hidden="true"></i> Lifecycles](administration/Life_cycles_-_Administration.md){ .oo-mh-pcard__go }
[<i class="o_icon o_icon_start" aria-hidden="true"></i> Language adaption tool](administration/Customizing.md#language_adaption_tool){ .oo-mh-pcard__go }
[<i class="o_icon o_icon_start" aria-hidden="true"></i> REST API](administration/REST_API.md){ .oo-mh-pcard__go }

</div>

</article>

</div>

## New in 21.0 {: #new_in_21}

These functions have to be activated or configured in the system administration after the update.

<div class="oo-mh-news" markdown>

<div class="oo-mh-new" markdown>

[Coaching module mandatory](administration/e-Assessment_Administration.md#coaching){ .oo-mh-new__title }

`Administration > e-Assessment > Coaching`

[Release Notes: Separation of learning and supervising/coaching](../release_notes/Release_notes_21.0.md#separation-of-learning-and-supervisingcoaching){ .oo-mh-new__rn }

</div>

<div class="oo-mh-new" markdown>

[Rooms module](administration/Modules_Rooms.md){ .oo-mh-new__title }

`Administration > Modules > Rooms`

[Release Notes: New «Rooms» module](../release_notes/Release_notes_21.0.md#new-rooms-module){ .oo-mh-new__rn }

</div>

<div class="oo-mh-new" markdown>

[Course Planner: element types and automation](administration/Modules_Course_Planner.md#tab_element_types){ .oo-mh-new__title }

`Administration > Modules > Course Planner > Tab Element types`

[Release Notes: Element types with automation](../release_notes/Release_notes_21.0.md#element-types-with-automation){ .oo-mh-new__rn }

</div>

<div class="oo-mh-new" markdown>

[AI features](administration/External_Tools_AI.md){ .oo-mh-new__title }

`Administration > External tools > AI module`

[Release Notes: AI features](../release_notes/Release_notes_21.0.md#ai-features){ .oo-mh-new__rn }

</div>

<div class="oo-mh-new" markdown>

[One time code (2FA)](administration/Login_Password_and_Authentication.md){ .oo-mh-new__title }

`Administration > Login > Password and authentication > Tab Authentication`

[Release Notes: Two-factor authentication with One Time Code](../release_notes/Release_notes_21.0.md#two-factor-authentication-with-one-time-code){ .oo-mh-new__rn }

</div>

</div>

The full checklist after the update, with further items on learning resources and the Safe Exam Browser, is in the release notes: [Checklist after updating to 21.0](../release_notes/Release_notes_21.0.md#system-administrators-activate-configure-new-features)

## Reference {: #reference}

<div class="grid cards" markdown>

-   :fontawesome-solid-sliders:{ .lg .middle } __System and Core functions__

    ---

    The system settings decide how the whole instance behaves and how it presents itself. This is where you set the basics, the Core functions and the customisation of your OpenOlat.

    [:octicons-arrow-right-24: System](administration/System.md)

    [:octicons-arrow-right-24: Core functions](administration/Core_functions.md)

    [:octicons-arrow-right-24: Landing pages](administration/Landing_pages.md)

    [:octicons-arrow-right-24: Customizing](administration/Customizing.md)

    [:octicons-arrow-right-24: Reports](administration/Reports.md)

-   :fontawesome-solid-right-to-bracket:{ .lg .middle } __Login and access__

    ---

    Here you decide who reaches your instance and how people authenticate. The settings cover the login methods, the password rules, self-registration and access for guests.

    [:octicons-arrow-right-24: Login](administration/Login.md)

    [:octicons-arrow-right-24: Security](administration/Login_Security.md)

    [:octicons-arrow-right-24: Password and Authentication](administration/Login_Password_and_Authentication.md)

    [:octicons-arrow-right-24: Self-registration](administration/Login_Self-Registration.md)

    [:octicons-arrow-right-24: Anonymous guests and external users](administration/Guest_and_invitation.md)

-   :fontawesome-solid-cubes:{ .lg .middle } __Modules__

    ---

    A module switches a feature on for the whole instance and sets its defaults. Without the matching module, the feature does not appear in courses, groups or the personal menu.

    [:octicons-arrow-right-24: Modules overview](administration/Modules.md)

    [:octicons-arrow-right-24: Module Course](administration/Modules_Course.md)

    [:octicons-arrow-right-24: Module Catalog](administration/Modules_Catalog_2.0.md)

    [:octicons-arrow-right-24: Module Course Planner](administration/Modules_Course_Planner.md)

    [:octicons-arrow-right-24: Module Groups](administration/Modules_Groups.md)

-   :fontawesome-solid-clipboard-check:{ .lg .middle } __e-Assessment__

    ---

    Tests, the question bank, certificates and credit points are configured centrally. These settings apply to every course that assesses learners.

    [:octicons-arrow-right-24: e-Assessment overview](administration/e-Assessment_Administration.md)

    [:octicons-arrow-right-24: Question bank](administration/eAssessment_Question_bank.md)

    [:octicons-arrow-right-24: Test](administration/e-Assessment_Test.md)

    [:octicons-arrow-right-24: Certificates](administration/e-Assessment_Certificates.md)

    [:octicons-arrow-right-24: Credit points](administration/e-Assessment_Credit_Points.md)

-   :fontawesome-solid-plug:{ .lg .middle } __External tools and integrations__

    ---

    OpenOlat connects to video conferencing systems, document editors, AI providers and LTI tools. Each integration is configured once here and is then available in courses.

    [:octicons-arrow-right-24: External tools overview](administration/External_Tools_-_Administration.md)

    [:octicons-arrow-right-24: LTI 1.3 Integrations](administration/LTI_Integrations.md)

    [:octicons-arrow-right-24: BigBlueButton module](administration/BigBlueButton_module.md)

    [:octicons-arrow-right-24: Zoom integration](administration/Zoom.md)

    [:octicons-arrow-right-24: AI module](administration/External_Tools_AI.md)

-   :fontawesome-solid-credit-card:{ .lg .middle } __Life cycles and payment__

    ---

    Life cycles clean up courses, groups and accounts that are no longer in use. The payment modules define how bookings are paid for.

    [:octicons-arrow-right-24: Life cycles](administration/Life_cycles_-_Administration.md)

    [:octicons-arrow-right-24: Automatic Group Life Cycle](administration/Automatic_Group_Lifecycle.md)

    [:octicons-arrow-right-24: Payment modules](administration/Payment_modules.md)

    [:octicons-arrow-right-24: Invoice](administration/Payment_Invoice.md)

    [:octicons-arrow-right-24: PayPal Configuration](administration/Payment_PayPal.md)

-   :fontawesome-solid-users:{ .lg .middle } __User management__

    ---

    User managers and administrators create accounts, assign roles and maintain user data. This chapter also covers data protection and the deletion of accounts.

    [:octicons-arrow-right-24: User management overview](usermanagement/index.md)

    [:octicons-arrow-right-24: Create user](usermanagement/Create_User.md)

    [:octicons-arrow-right-24: Assign roles](usermanagement/Assign_roles.md)

    [:octicons-arrow-right-24: Manage user settings](usermanagement/Configure_User.md)

    [:octicons-arrow-right-24: Data protection](usermanagement/Data_protection.md)

-   :fontawesome-solid-server:{ .lg .middle } __Installation and operation__

    ---

    This chapter is for the people who run the server. It covers the installation, the update and the supporting tools OpenOlat needs for images, videos and PDF generation.

    [:octicons-arrow-right-24: Installation guide](installation/installGuide.md)

    [:octicons-arrow-right-24: Update guide](installation/updateGuide.md)

    [:octicons-arrow-right-24: imageMagick](installation/imageMagick.md)

    [:octicons-arrow-right-24: MySQL DB](installation/mysql.md)

    [:octicons-arrow-right-24: Windows support](installation/windows.md)

</div>

[To the top of the page ^](#admin_manual)
