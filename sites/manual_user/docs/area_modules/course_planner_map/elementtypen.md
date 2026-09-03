# Defining structure rules (element types) {: #element_types}

!!! warning "Concept study: possible new presentation"
    This page is part of an experiment exploring how the visual entry point to the Course Planner could look in the future. The content is deliberately abbreviated. The regular manual page [Course Planner](../../Course_Planner/) is authoritative.

[:material-arrow-left: Back to the overview](../../Course_Planner_Map/)

Before the first educational product is created, the administration sets the rules of the game: which components should a program consist of, what may or should be at the top, what lies within what? In OpenOlat these rules are called "element types"; they give all later structures a reliable framework.

## How do I do this?

Create an element type with title and reference via "Add new type" and define under "For use as" whether it serves as an implementation (topmost parent element) or as an element. Optionally configure "With content", "Allow as implementation" and features (absence, timetable, progress).

## Prerequisites

The Course Planner must be activated. For the absence management feature, the Absence management module must be active.

## Where do I find the setting

In the system administration under `Administration > Modules > Course Planner > Element types tab`

## Connections

Element types determine which elements a product may contain and their hierarchy (e.g. program > semester > module > course). Automation rules can be stored per type as a template, which individual elements adopt or override.

## Further information {: #further_information}

[Course Planner: Overview >](../Course_Planner.md)<br>
[Course Planner: Application map >](../Course_Planner_Map.md)<br>
[Module Course Planner >](../../../manual_admin/administration/Modules_Course_Planner.md)<br>
[Course Planner: Products >](../Course_Planner_Products.md)<br>
[Course Planner: Implementations >](../Course_Planner_Implementations.md)

[To the top of the page ^](#element_types)
