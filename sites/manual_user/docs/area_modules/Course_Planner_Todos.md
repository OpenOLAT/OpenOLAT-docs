# Course Planner: To-dos [:octicons-tag-16:{ title="from Release 21.0 (OO-9417)" }](https://track.frentix.com/issue/OO-9417){:target="_blank"} {: #course_planner_todos}

In the Course Planner, tasks (to-dos) can be recorded at various levels: in the overview, on the product, on the implementation and on each individual element. All to-dos can be viewed centrally in one overview, without having to open individual implementations or elements. A widget on the dashboard shows open and overdue to-dos at a glance.


[To the top of the page ^](#course_planner_todos)

---


## "To-dos" tab on an element {: #element_tab_todos}

Every element in the Course Planner has a **"To-dos"** tab. There you create, edit and manage tasks that are assigned directly to this element.


### Permissions {: #todo_permissions}

* **Course Planners** and **element owners** can create, edit, assign and delegate to-dos.
* **Course owners** can mark to-dos assigned to their course as done; however, they cannot create or otherwise edit them.
* **Principals** can view to-dos but not edit them.

### Creating a to-do {: #create_todo}

In the "To-dos" tab of an element, click on **"Create to-do"**. The following dialog contains these fields:

* **Title** (mandatory field): Names the task.
* **Assigned** (mandatory field): The person responsible for completing it.
* **Delegated**: Execution can be delegated to another person; responsibility remains with the assigned person.
* **Status**: Sets the current processing state (Open, In progress, Done).
* **Priority**: Urgent, High, Medium or Low.
* **Start date** and **Due date**: Absolute or [relative to the implementation period](#relative_date).
* **Tags**: Freely assignable keywords.
* **Description**: Additional information about the task.

Select **"Start"** to set a to-do directly to the status "In progress". With **"Mark as done"** you complete it without opening it separately.

!!! info "Action menu"
    The action menu (3-dot symbol) of a to-do row provides **Edit**, **Duplicate** and **Delete**. With **Duplicate** you copy an existing to-do together with its properties. These actions require editing permissions.


#### Overview of the to-do statuses {: #todo_status}

| Status | Meaning |
|---|---|
| Open | The task has been created but not yet started. |
| In progress | Work on the task has begun. |
| Done | The task is completed. |
| Deleted | The to-do has been deleted and is only visible in the "Deleted" filter. |



[To the top of the page ^](#course_planner_todos)

---


## Central to-do overview [:octicons-tag-16:{ title="from Release 21.0 (OO-9418)" }](https://track.frentix.com/issue/OO-9418){:target="_blank"} {: #central_overview}

The central to-do overview brings together all to-dos across all products and elements in one table. You open it via the **"To-dos"** launcher in the **"Productivity"** launcher group on the CPL dashboard.

The overview shows all to-dos for which you are assigned or delegated, as well as all to-dos in products to which you have access.


### Predefined filters {: #predefined_filters}

Use the quick filters to narrow the view thematically:

| Filter | Shows |
|---|---|
| All | All visible to-dos |
| My to-dos | To-dos in which you are entered as "Assigned" |
| Open | To-dos with status "Open" |
| Overdue | To-dos whose due date has passed |
| Not assigned | To-dos without an assigned person |
| Done | To-dos with status "Done" |
| Deleted | Deleted to-dos |


### Table columns {: #table_columns}

Use the gear symbol to choose which columns are displayed. Shown by default:

* **Title** (for new to-dos with a "New" marker)
* **Product** (the associated product)
* **Element** (the associated element within the product)
* **Priority**
* **Due**
* **Status**
* **Assigned**
* **Delegated**
* **Tags**

Optionally displayable: Expenditure of work, Start date, Done date, Created, Created by, Changed, Deleted, Deleted by.


### Bulk actions {: #bulk_actions}

Activate the checkbox in the first column to select individual to-dos, or use the checkbox in the table header to select all to-dos of the current view at once. As soon as at least one to-do is selected, the bulk action **"Delete"** appears in the action bar.

After a confirmation prompt, the selected to-dos are deleted. Deleted to-dos are not permanently removed: they receive the status "Deleted" and remain viewable via the **"Deleted"** filter. In the "Deleted" view, the bulk action itself is not available.


[To the top of the page ^](#course_planner_todos)

---


## Create to-dos directly for several implementations [:octicons-tag-16:{ title="from Release 21.0 (OO-9539)" }](https://track.frentix.com/issue/OO-9539){:target="_blank"} {: #bulk_create}

In the implementation overview as well as in the "Implementations" tab of a product, you can use a bulk action to create a to-do for several implementations at the same time.

1. In the implementation overview, select the desired implementations (checkbox in the first column).
2. In the action bar, click on **"Create to-do"**.
3. Fill in the dialog. The context (product and element) is set automatically from the selected implementation and cannot be edited.

!!! info "Important"
    The selection fields "Assigned" and "Delegated" only show persons who have access rights in the relevant and selected implementations.


[To the top of the page ^](#course_planner_todos)

---


## Relative due date [:octicons-tag-16:{ title="from Release 21.0 (OO-9425)" }](https://track.frentix.com/issue/OO-9425){:target="_blank"} {: #relative_date}

When creating or editing a to-do in the Course Planner, the due date and start date can be set either **absolutely** (a fixed calendar date) or **relatively** (based on the implementation period).


### Configuring a relative date {: #configure_relative_date}

Under **Due date**, select the option **"Relative"**. In the popover you define:

* **Reference date**: "Begin of the execution period" or "End of the execution period".
* **With offset** (optional): Activate this switch to specify a distance from the reference date.
  * **Offset**: Number of units (days, weeks, months or years).
  * **Direction**: "before" or "after" the reference date.

The calculated date is shown as a preview as long as an implementation period is defined. If the implementation period changes later, the due date adjusts automatically.

!!! info "Important"
    A relative date is only available in the Course Planner. In the personal menu and in other contexts (project, course), only absolute dates are possible.


[To the top of the page ^](#course_planner_todos)

---


## To-do widget [:octicons-tag-16:{ title="from Release 21.0 (OO-9422)" }](https://track.frentix.com/issue/OO-9422){:target="_blank"} {: #todo_widget}

The **To-do** widget on the CPL dashboard shows at a glance which tasks require your immediate attention.

The widget shows to-dos in which you are entered as **"Assigned"**.

For each to-do, the title, priority and due date are displayed. A click on the title opens the to-do directly.

!!! note "Dashboard configuration"
    Like all CPL dashboard widgets, the widget can be shown and hidden via the dashboard configuration.


[To the top of the page ^](#course_planner_todos)

---


## Further information {: #further_information}

[Course Planner: Overview >](Course_Planner.md)<br>
[Course Planner: Implementations >](Course_Planner_Implementations.md)<br>
[To-dos (personal menu) >](../personal_menu/To-Dos.md)<br>
[General information on to-dos >](../basic_concepts/To_Dos_Basics.md)<br>
[Activate Course Planner (Admin) >](../../manual_admin/administration/Modules_Course_Planner.md)<br>

[To the top of the page ^](#course_planner_todos)
