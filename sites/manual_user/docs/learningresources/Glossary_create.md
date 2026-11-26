# Glossary - create {: #glossary_create}

If participants should be able to look up the technical terms of a course, you create a glossary, enter the terms with their definitions and embed the glossary in the course. Participants then read the explanation of a term directly in the learning content, without leaving the course. A glossary is created by persons with the role author, learning resource manager or administrator.

## Where is a new glossary created? {: #where}

You create a glossary like other learning resources in the authoring area:<br>
`Authoring > Create > Glossary`

![Expanded Create menu in the authoring area with the highlighted entry Glossary](assets/glossary_create_authoring_v1_en.png){ class="shadow lightbox" title="Authoring area page · 2026.11.09" }

You can also create a glossary directly in the course, under `Course > Administration > Settings > Tab "Options"`. The button "Select glossary" opens a window in which you select an existing glossary or create a new glossary.

![Options tab of the course settings with the highlighted button Select glossary, which you use to select or create a glossary](assets/glossary_create_settings_v2_en.png){ class="shadow lightbox" title="Options tab in the course settings · 2026.11.09" }

!!! note "Note"

    In the authoring area you create as many glossaries as you like. You embed one glossary per course.

[To the top of the page ^](#glossary_create)

---


## Create glossary entries {: #create_entries}

``1.`` Open the glossary in the authoring area: with a click on the title, on the edit icon or in the three-dot menu of the row.

![Row of a glossary in the authoring area with title, edit icon and three-dot menu highlighted](assets/glossary_authoring_edit_v1_en.png){ class="shadow lightbox" title="List in the authoring area · 2026.11.09" }

``2.`` Click on one of the two buttons "Add entry".

![Two Add entry buttons highlighted, top right and below the glossary entries](assets/glossary_add_entry_v1_en.png){ class="shadow lightbox" title="Glossary page · 2026.11.09" }

``3.`` Enter the term. You can add synonyms, for example the synonym "IT" for the term "information technology".

``4.`` Save the term. After that, the "Definition" tab can be opened.

![Mandatory field Term with the term Information technology, field Synonyms with IT and the still inactive Definition tab](assets/glossary_edit_entry_v1_en.png){ class="shadow lightbox" title="Add term dialog · 2026.11.09" }

``5.`` In the "Definition" tab you enter the explanation of the term. You can change or delete entered terms later.

![Active Definition tab with rich text editor for entering the term's explanation](assets/glossary_entry_definition_v1_en.png){ class="shadow lightbox" title="Add term dialog · 2026.11.09" }

Learners can also fill in the content of a glossary. How to give all users write permission is described on the page [Glossary: Administration](Glossary_administration.md#tab_write_permissions).

### Writing permission for selected users {: #write_selected_users}

If only certain persons are to edit the glossary, for example some participants of a course, you grant the write permission via the members management of the course. Create a group there and add the persons as participants of the group. Then, in the "Rights" area of the members management, tick the right "Glossary tool" for the participants of the group. After that, the persons of the group add and change glossary entries. What the right enables is described in the section [Glossary tool](Members_management.md#right_glossary_tool).

!!! info "Important"

    The owners of a course are not automatically the owners of the "Glossary" learning resource. In the course, they edit the integrated glossary nevertheless: they open it via the "Glossary" tool in the course toolbar and create, change and delete entries there.

    If you open the glossary as a learning resource instead, for example in the authoring area, only the owners of the "Glossary" learning resource edit the entries. If further course owners are to work there as well, enter them as owners of the "Glossary" learning resource.

[To the top of the page ^](#glossary_create)

---


## Design glossary {: #design}

You edit the definitions in a simple editor. Besides text, it offers for example

* Font selection
* Indentation
* Tables
* Links

Whether the glossary groups the terms by initial letter with an alphabetical index is set in the settings of the glossary, see [Glossary: Administration](Glossary_administration.md#tab_register).

[To the top of the page ^](#glossary_create)

---


## Integrate glossary {: #integrate}

You usually embed a glossary in a course. Participants then see the terms explained in the course. You can also use a glossary standalone and offer it, for example, as an offer of its own in the catalog.

Glossaries are available in every OpenOlat instance, without any setting in the system administration. Everyone who opens the [course settings](Course_Settings/index.md) can embed one: owners of the course, learning resource managers and administrators, and also persons with the right "Course editor".

``1.`` Open `Course > Administration > Settings > Tab "Options"`. Select the glossary with the button "Select glossary" and click "Save".

![Options tab of the course settings with the highlighted button Select glossary, which you use to select or create a glossary](assets/glossary_create_settings_v2_en.png){ class="shadow lightbox" title="Options tab in the course settings · 2026.11.09" }

``2.`` Switch the glossary on as a tool: checkbox "Glossary" under `Course > Administration > Settings > Tab "Toolbar"`. Only then does the glossary take effect in the course: the menu "Glossary" appears in the toolbar, and the terms can be explained in the learning content.

![Toolbar tab of the course settings with the highlighted, switched-on checkbox Glossary under Activate tools in toolbar](assets/glossary_settings_toolbar_activate_v2_en.png){ class="shadow lightbox" title="Toolbar tab in the course settings · 2026.11.09" }

In the menu "Glossary" of the toolbar, participants select "Show glossary terms in learning content". After that, OpenOlat shows the explanation of a term as soon as they point at the term in the learning content with the mouse. Find out more on the page [Glossary - Usage](Glossary_usage.md).

!!! note "Note"

    You embed one glossary per course. Several glossaries can exist in the authoring area, so that different courses use different glossaries.

If you want to embed a different glossary in your course, select it under `Course > Administration > Settings > Tab "Options"` with "Select glossary". If you no longer use a glossary, remove it there with "Delete selection" and click "Save". The glossary itself remains as a learning resource in the authoring area.

[To the top of the page ^](#glossary_create)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[Glossary: Administration >](Glossary_administration.md)<br>
[Members management >](Members_management.md)<br>
[Course Settings >](Course_Settings/index.md)<br>
[Glossary - Usage >](Glossary_usage.md)

**Further reading**<br>
[Glossary >](Glossary/index.md)

[To the top of the page ^](#glossary_create)

