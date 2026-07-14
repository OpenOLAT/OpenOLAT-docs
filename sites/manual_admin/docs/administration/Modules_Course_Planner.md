# Module Course Planner {: #module_course_planner}


## Activation of the Course Planner {: #activation}

The Course Planner module is optionally available in OpenOlat instead of the Curriculum module and must be activated in Administration.

!!! tip "frentix hosting customers"
    For activation, please contact [contact@frentix.com](mailto:contact@frentix.com). <br> After activation, the display of the personal curriculum ("Courses") in the "Courses" area can also be enabled.


### Tab Course Planner {: #tab_course_planner}

![modules_course_planner_tab_cp_v2_de.png](assets/modules_course_planner_tab_cp_v2_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Turn on Course Planner**<br>
This checkbox activates the entire module.

![2_green_24.png](assets/2_green_24.png) **Product in "My courses"**<br>
All participants will find the menu item "Courses" in the header of the main navigation bar. Curricula can also be displayed to participants under this menu item. 

![3_green_24.png](assets/3_green_24.png) **User overview**<br>
Hier bestimmen Sie als Administrator:in, welche Optionen die Rollen.

* Course Planner
* Education Manager and
* Line manager

are displayed. For example, what a person working with the Course Planner is allowed to see of the users.

![4_green_24.png](assets/4_green_24.png) **Linked taxonomies**<br>
From the taxonomies created in the "Taxonomy" module, you can select those that should also be available in the Course Planner.

**Note:**<br>
The taxonomies selected here should be the same as those used in the catalog. Only then can these taxonomies be searched for in the catalog.

![5_green_24.png](assets/5_green_24.png) **Standard purpose for new courses**<br>

Courses can be intended for stand-alone use or for integration into a product. As an administrator, you specify here which use is preset by default.

**Independent**: An independent course has a member administration. Access can be gained using the "Private" offer type by registering as a member (e.g. by course owners), by assigning an access code or by publication in the catalog. 

**Integration into product**: If the course is integrated into a product, memberships are assigned and managed by the Course Planner. The course then does not require a second, independent membership administration.

!!! tip "Tip"

	If Course Planner is used extensively, it is advisable to set the default purpose for new courses under `System administration > Course Planner settings` to "Integration into product".

[To the top of the page ^](#module_course_planner)

---

## Tab "Element types" {: #tab_element_types}

### Element type overview [:octicons-tag-16:{ title="from Release 21.0 (OO-8924)" }](https://track.frentix.com/issue/OO-8924){:target="_blank"} {: #element_types_overview}

Element types define which elements a product can contain and give these elements a meaning. A hierarchical structure can be mapped when creating the element types. An example of a hierarchical product is `Training program > Semester > Module > Course`.

The overview table shows all element types that have been created. An element type is edited via the :fontawesome-regular-pen-to-square: symbol. The type can be copied or deleted via the 3-dot link.

**Table columns:**

| Column | Meaning |
|---|---|
| Type | Name and reference of the element type |
| For use as | Function of the element type in the product: "Implementation", "Element" or "Implementation or element (legacy)" |
| Active / Inactive | Whether the type is available for selection for new elements |
| #Parents | Number of superordinate element types that allow this type as a child element |
| #Children | Number of element types defined as child elements of this type |
| #Uses | Number of elements of this type present in the system |
| With content | Whether elements of this type can contain courses as content |

**Bulk action Change type** [:octicons-tag-16:{ title="from Release 21.0 (OO-9583)" }](https://track.frentix.com/issue/OO-9583){:target="_blank"}

By activating the checkbox in the first column, you select several elements. Using the **"Change type"** action, you assign a different element type to all selected elements.


[To the top of the page ^](#module_course_planner)

---


### Create and edit element types {: #create_element_types}

Use the **"Add new type"** button to create additional element types. The form contains the following fields:

**Title** (mandatory field)<br>
The name of the element type that is shown in the selection when an element is created.

**Reference** (mandatory field)<br>
A unique identifier used to distinguish between elements with the same title. Appears as a selection option when a new curriculum element is created.

**For use as**<br>
Determines the function of elements of this type in the product:

* **Implementation**: Elements of this type are implementations (the topmost parent element). They have an implementation period and are the starting point for automation rules.
* **Element**: Elements of this type are sub-elements below an implementation and have no implementation period of their own.
* **Implementation or element (legacy)**: Elements of this type can be used both as an implementation and as a sub-element. This mode is used for backward compatibility with existing product structures.

**Status**<br>
* **Active**: The type is available for selection when creating new elements.
* **Inactive**: The type is hidden and is no longer available for selection for new elements. Existing elements of this type are retained.

!!! note "CSS class"
	Here you can define a type-specific layout via a CSS class. If you are interested in specific layouts, please contact frentix: [contact@frentix.com](mailto:contact@frentix.com).

**Description**<br>
Explanatory text for the element type.

**Features**<br>
* **Absence management**: Course Planners get the "Absences" tab on elements of this type and can view the absences of all participants. Prerequisite: the Absence management module is activated.
* **Schedule**: Combines all course calendar dates of the courses assigned to the product element.
* **Progress**: Shows the learning progress in learning path courses as a pie chart. With several sub-elements, the average of the sub-elements is calculated.

**Allow as implementation**<br>
Determines which element may be a parent element. An implementation is the topmost parent element in the product.

**With content**<br>
Switch on this option if elements of this type should contain courses as content. Elements without course content are pure structure elements, comparable to the course element "Structure".

**Composite type**<br>
When activated, existing element types can be subordinated as sub-types.


[To the top of the page ^](#module_course_planner)

---


### Automation rules per element type [:octicons-tag-16:{ title="from Release 21.0 (OO-9452)" }](https://track.frentix.com/issue/OO-9452){:target="_blank"} {: #automation_rules}

Automation rules can be defined for each element type. These rules serve as a template for all elements of this type: elements can adopt the template or override it individually (see [Automation in the settings of an implementation](../../manual_user/area_modules/Course_Planner_Implementations.md#tab_settings_automation)).

**Configuring automation rules**

Open the desired element type via the :fontawesome-regular-pen-to-square: symbol and switch to the **"Automation"** tab. Use **"Add automation rule"** to add new rules.

Each automation rule contains:

* **Trigger type**:
  * **On status change**: The action is triggered as soon as the implementation or element status reaches a defined value.
  * **Time-controlled**: The action is triggered relative to the start or end of the implementation period. You define the reference date (start or end) and an optional offset (number of days/weeks/months before or after the reference date).
* **Action**: What is executed automatically, e.g. create course from template (instantiation) or set course status.


[To the top of the page ^](#module_course_planner)

---

## Further information {: #further_information}

[How can I plan and run courses with the Course Planner? >](../../manual_how-to/course_planner_courses/course_planner_courses.md)<br>
[How can I plan and run a course with the Course Planner? >](../../manual_how-to/course_planner_curriculum/course_planner_curriculum.md)<br>
[Course Planner: Overview >](../../manual_user/area_modules/Course_Planner.md)<br>
[Course Planner: Products >](../../manual_user/area_modules/Course_Planner_Products.md)<br>
[Course Planner: Implementations >](../../manual_user/area_modules/Course_Planner_Implementations.md)<br>
[Course Planner: Events >](../../manual_user/area_modules/Course_Planner_Events.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.md)<br>

[To the top of the page ^](#module_course_planner)















