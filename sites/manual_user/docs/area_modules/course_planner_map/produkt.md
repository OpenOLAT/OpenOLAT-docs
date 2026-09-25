# Creating and structuring a product {: #product}

!!! warning "Concept study: possible new presentation"
    This page is part of an experiment exploring how the visual entry point to the Course Planner could look in the future. The content is deliberately abbreviated. The regular manual page [Course Planner](../../Course_Planner/) is authoritative.

The person responsible for education creates a product and builds up its structure: study programme, modules, single courses. Every element passes through the status values "Preparation", "Provisional", "Confirmed" and "Active" to "Finished" or "Cancelled". For the implementation, this sequence is called the implementation life cycle. [:octicons-tag-16:{ title="from Release 20.0 (OO-8092)" }](https://track.frentix.com/issue/OO-8092)

The implementation life cycle does not delete anything and is not one of the three life cycles for groups, courses and accounts under `Administration > Life cycles`. You can set the status values manually or via [automation](../Course_Planner_Implementations.md#tab_settings_automation). The element type specifies the rules, and the individual implementation can override them.

## How do I do this?

Open the "Products" area in the Course Planner and create a product. Title and reference are mandatory fields; optionally add the organisation, absence management and a description.

## Prerequisites

Course Planner activated. For the restriction to an organisation, the module "Organisations" must be active. For absence management, the system administration must have activated and released the module:<br>
`Administration > Modules > Events / Absences`

## Where do I find the setting

`Course Planner > Products > Create product`

## Connections

The product is the central copy template on which the implementations are based. Structured products map courses and learning resources in a tree structure of elements.

## Further information {: #further_information}

[Course Planner: Overview >](../Course_Planner.md)<br>
[Course Planner: Application map >](../Course_Planner_Map.md)<br>
[Course Planner: Implementations >](../Course_Planner_Implementations.md)<br>
[Course Planner: Products >](../Course_Planner_Products.md)<br>
[Life cycles: Overview >](../../../manual_admin/administration/Life_cycles_-_Administration.md)

[To the top of the page ^](#product)
