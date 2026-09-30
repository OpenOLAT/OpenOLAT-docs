---
title: Modules
description: Enable functions. A module enables a function for the whole installation and sets its default values.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-nav" aria-label="Navigation: The path to a running installation" markdown="1">

<span class="oo-mh-nav__label">Navigation: The path to a running installation</span>
[‹ Menu: Roles](rollen.md){ .oo-mh-btn .oo-mh-btn--prev }
[Menu: Assess and connect ›](anbinden.md){ .oo-mh-btn .oo-mh-btn--next }

</nav>

# Modules {: #module}

<p class="oo-mh-sub">Enable functions</p>

A module enables a function for the whole installation and sets its default values. Learning resource and course are the core, the catalog makes offers visible, Coaching separates supervising from learning, and Rooms and the Course Planner plan the offer.

## Terms of this station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Concept</p>

### Learning resource {: #resources_learning_resource}

A content object managed in the authoring area: course, test, form, video, wiki and others.

??? note "Learning resource in detail"

    A content object managed in the authoring area: course, test, form, video, wiki and others. It carries metadata, owners and a lifecycle and can be embedded into courses.

    **German:** Lernressource

    **What users call it:** resource, content, material, repository entry

    [Read in the manual](../../manual_user/learningresources/index.md) · [Ask Sophia](?sophia=What%20is%20%22Learning%20resource%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Learning resource</p>

### Course {: #course_course}

A course is a learning resource, but a special one: it is the only one that keeps members, roles and assessments.

??? note "Course in detail"

    A course is a learning resource, but a special one: it is the only one that keeps members, roles and assessments. No other learning resource has any of that, and they are embedded into a course in order to reach participants. The course ties content, activities and assessment into one structured sequence.

    **German:** Kurs

    **What users call it:** course, class, training

    [Read in the manual](../../manual_user/learningresources/index.md) · [Ask Sophia](?sophia=What%20is%20%22Course%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### Catalog {: #catalog_catalog}

The module that puts learning resources and implementations with an offer on display for booking.

??? note "Catalog in detail"

    The module that puts learning resources and implementations with an offer on display for booking. It is structured through the taxonomy and the launchers. Without an offer a resource does not appear. Without signing in it is reachable as the web catalog, if that is switched on.

    **German:** Katalog

    **What users call it:** catalogue, course catalog, offering

    [Read in the manual](../../manual_user/area_modules/catalog2.0.md) · [Ask Sophia](?sophia=What%20is%20%22Catalog%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Area</p>

### Coaching {: #coaching_coaching_tool}

The area where coaches follow their learners across all courses, with progress, assessments, attendance and certificates in one place.

??? note "Coaching in detail"

    The area where coaches follow their learners across all courses, with progress, assessments, attendance and certificates in one place.

    **German:** Coaching

    [Read in the manual](../../manual_user/area_modules/Coaching.md) · [Ask Sophia](?sophia=What%20is%20%22Coaching%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### Rooms {: #attendance_rooms_module}

The module for the physical rooms: buildings, rooms with a number of seats and their booking by events.

??? note "Rooms in detail"

    The module for the physical rooms: buildings, rooms with a number of seats and their booking by events. The administration maintains buildings and rooms, room scheduling shows all bookings; without the module no rooms can be booked on events.

    **German:** Räume

    **What users call it:** room module, rooms and buildings

    **Not to be confused with [Room management](../../manual_user/area_modules/Course_Planner_Rooms.md):** The Rooms module is the switch with the maintenance in the administration, room management the read-only view of it in the Course Planner.

    [Read in the manual](../administration/Modules_Rooms.md) · [Ask Sophia](?sophia=What%20is%20%22Rooms%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### Course Planner {: #curriculum_course_planner}

The module that switches on the planning of the educational offering in OpenOlat: products with elements and implementations, element types, course templates, automation, to-dos and reports.

??? note "Course Planner in detail"

    The module that switches on the planning of the educational offering in OpenOlat: products with elements and implementations, element types, course templates, automation, to-dos and reports. It replaces the earlier Curriculum module and grants the memberships of the courses it embeds.

    **German:** Course Planner

    **What users call it:** curriculum management, course planning

    **Not to be confused with [Course Planner](../../manual_user/area_modules/Course_Planner.md):** The module is the switch in the administration, the site is the Course Planner entry in the main navigation that the module unlocks.

    [Read in the manual](../administration/Modules_Course_Planner.md) · [Ask Sophia](?sophia=What%20is%20%22Course%20Planner%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

</div>

## Read up {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Read up</p>

[Modules: overview](../administration/Modules.md)

frentix accompanies you in the setup with support and coaching: [support@frentix.com](mailto:support@frentix.com)

</div>

</div>

## Deepen once the installation is running {: #deepen}

The installation is running. Now the things that did not matter while setting up pay off: the terms of this station have parts and settings that control the installation more precisely.

- **Learning resource:** [Form](../../manual_user/learningresources/Form.md), [Test](../../manual_user/learningresources/Course_Element_Test.md), [Questionnaire](../../manual_user/learningresources/Course_Element_Survey.md), [Wiki](../../manual_user/learningresources/Course_Element_Wiki.md) and more. More on the page [Various Types of Learning Resources](../../manual_user/learningresources/index.md).
- **Course:** [Course element](../../manual_user/learningresources/Course_Elements.md), [Course editor](../../manual_user/learningresources/Learning_path_course_Course_editor.md), [Publication](../../manual_user/learningresources/Using_additional_Course_Editor_Tools.md), [Course archive](../../manual_user/learningresources/Course_Archiving.md) and more. More on the page [Various Types of Learning Resources](../../manual_user/learningresources/index.md).
- **Catalog:** [Launcher](../administration/Modules_Catalog_2.0.md), [Web catalog](../../manual_user/area_modules/catalog2.0_web.md). More on the page [Catalog 2.0: Overview](../../manual_user/area_modules/catalog2.0.md).
- **Coaching:** [Overview](../../manual_user/area_modules/Coaching.md), [Scope](../../manual_user/area_modules/Coaching.md), [Assignments](../../manual_user/area_modules/Coaching.md), [Communication](../../manual_user/area_modules/Coaching.md) and more. More on the page [Coaching - Overview](../../manual_user/area_modules/Coaching.md).
- **Rooms:** [Building](../administration/Modules_Rooms.md), [Room scheduling](../../manual_user/area_modules/Course_Planner_Rooms.md).
- **Course Planner:** [Product](../../manual_user/area_modules/Course_Planner_Products.md), [Element type](../administration/Modules_Course_Planner.md), [Course template](../../manual_user/area_modules/Course_Planner_Implementations.md), [Reports](../../manual_user/area_modules/Course_Planner_Reports.md). More on the page [Module Course Planner](../administration/Modules_Course_Planner.md).

## Further information {: #further_information}

**Mentioned on this page**<br>
[Various Types of Learning Resources >](../../manual_user/learningresources/index.md)<br>
[Catalog 2.0: Overview >](../../manual_user/area_modules/catalog2.0.md)<br>
[Coaching - Overview >](../../manual_user/area_modules/Coaching.md)<br>
[Course Planner: Room management >](../../manual_user/area_modules/Course_Planner_Rooms.md)<br>
[Module Rooms >](../administration/Modules_Rooms.md)<br>
[Course Planner: Overview >](../../manual_user/area_modules/Course_Planner.md)<br>
[Module Course Planner >](../administration/Modules_Course_Planner.md)<br>
[Modules: Overview >](../administration/Modules.md)<br>
[Forms - Overview >](../../manual_user/learningresources/Form.md)<br>
[Course Element Test >](../../manual_user/learningresources/Course_Element_Test.md)<br>
[Course Element Survey >](../../manual_user/learningresources/Course_Element_Survey.md)<br>
[Course Element Wiki >](../../manual_user/learningresources/Course_Element_Wiki.md)<br>
[Types of Course Elements >](../../manual_user/learningresources/Course_Elements.md)<br>
[Learning path course - Course editor >](../../manual_user/learningresources/Learning_path_course_Course_editor.md)<br>
[Course editor tools >](../../manual_user/learningresources/Using_additional_Course_Editor_Tools.md)<br>
[Course administration - Archiving & Reports >](../../manual_user/learningresources/Course_Archiving.md)<br>
[Module Catalog >](../administration/Modules_Catalog_2.0.md)<br>
[Externally available catalog >](../../manual_user/area_modules/catalog2.0_web.md)<br>
[Course Planner: Products >](../../manual_user/area_modules/Course_Planner_Products.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.md)

**Further reading**<br>
[Module Learning resource >](../administration/Modules_Learning_Resource.md)<br>
[Module Course >](../administration/Modules_Course.md)<br>
[Glossary >](../../reference_glossary/glossary.md)

[To the top of the page ^](#module)
