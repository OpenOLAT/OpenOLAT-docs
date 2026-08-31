# Catalog 2.0 - Management {: #catalog_mgmt}

## Short description of catalog management {: #description}

Catalog V2 management is not a responsibility assigned to a specific role. Rather, it is a feature for editing the taxonomies used in the catalog. Users with this permission ("Managing" competence) can edit these taxonomies and parts of them without being an administrator.

## Where can I access the catalog management? {: #access}

Access to the catalog management system is available via a link in the catalog.
In the catalog, authorized users will also find the following links in the top-right corner, below the header:

- **Catalog management**
- **To the administration**

![Highlighted links Catalog management and To the administration below the catalog header, in the Catalog menu](assets/catalog20_mgmt_access_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#catalog_mgmt)

---


## Who sees the access links in the catalog? {: #access_links}

The **"Catalog management"** link is available to

- Learning resource managers
- Administrators
- System administrators

The **"To the administration"** link is available to

- System administrators

[To the top of the page ^](#catalog_mgmt)

---

## How do you obtain the right (authority) to manage the catalog? [:octicons-tag-16:{ title="from Release 20.1 (OO-8544)" }](https://track.frentix.com/issue/OO-8544) {: #competence}

The "Manage" permission (the right to edit the taxonomies used in the catalog) can be granted in two ways:

**Option 1:**<br>
By system administrators in the system administration:<br>
`Administration > Modules > Taxonomy > "Taxonomy title" > "Taxonomy level" > "Management" tab > "Add manager" button`<br>
The taxonomy must be enabled for the catalog. Open it with "View/Edit".

**Option 2:**<br>
By user managers:<br>
`User management > "Person" > "Competencies" tab > "Add 'Manage' competency" button`

Once the permission has been granted, the "Catalog Management" link will appear for that person in the upper-right corner, below the catalog header.

!!! info "Important"

    Catalog management is not limited to a specific organizational unit, although the role of Learning Resources Manager may be restricted to a specific organizational unit. (Taxonomies are also not limited to organizational units.)

[To the top of the page ^](#catalog_mgmt)

---

## Is it possible to edit learning resources in catalog management? {: #functions}

The content of learning resources in the catalog is edited in the authoring area. You therefore edit courses [in the authoring area](../area_modules/Authoring.md). They are also deleted there, for example when they have ended.

### Tab Level  {: #tab_level}
The editing options for the subject areas (taxonomy levels) include:

- Edit
- Move
- Merge
- Assign level type
- Deleting elements of the taxonomy level / subtaxonomies
- Creating new sub-layers

Under the three dots to the right of the “Create New Taxonomy Level” button, you'll also find options to import taxonomy levels or export them all. The exported data can be downloaded as a ZIP archive, which contains an Excel spreadsheet showing the hierarchical structure of the taxonomy levels.

![Levels tab with the actions Assign level type, Move, Merge, Delete and the row menu of a level](assets/catalog20_mgmt_edit_v1_de.png){ class="shadow lightbox" }

!!! info "Important"

    The design of launchers, sections, etc., is reserved for system administrators.

[To the top of the page ^](#catalog_mgmt)

---

### Tab Metadata {: #tab_metadata}

![Metadata tab with ID, external ID, the required fields Reference and Title and the description editor](assets/catalog20_mgmt_tab_metadata_v1_de.png){ class="shadow lightbox" }

**ID:** The ID is generated automatically and allows the object to be uniquely identified.

**External ID:** If an external management system created the levels, the external ID is generated in addition to the automatically generated ID.

**Reference:** (Required field) Select a unique and logical reference for the taxonomy level. This reference appears in the “Taxonomy” tab of the table, in the "Level type" column, and is more practical for many purposes than the full title (which may be more understandable and colloquial).

**Title:** (Required field) The title is used in various places (Catalog 2.0, Document Pool, e-Portfolio, Question Pool). It should provide a brief and accurate description of the taxonomy level.

**Description:** Entering a more detailed description of the layer is optional.

[To the top of the page ^](#catalog_mgmt)

---


### Tab Level types {: #tab_leveltype}

Use the "Create new level type" button to add another level type. The following fields are available in the edit dialog.

![Level types tab with the list of level types and the Create new level type button](assets/catalog20_mgmt_tab_leveltype_v1_de.png){ class="shadow lightbox" }

![Edit dialog of a level type with Reference, Title, CSS class, Visible, Competences and Evidence of achievement](assets/catalog20_mgmt_tab_leveltype_edit_v1_de.png){ class="shadow lightbox" }


**Reference:** In addition to the title, a reference must be provided.

**Title:** Enter an appropriate title to describe the layer type.

**CSS class:** If a corresponding CSS class is defined in the theme, it can be selected here.

**Visible:** This setting determines whether all taxonomy levels of this type should be visible.

**Competences:** Users can be assigned competences in the user management section. Selecting this option enables taxonomy levels with this level type to be used as competences.

**Evidence of achievement:** Selecting this option enables taxonomy levels with this level type for grouping evidence of achievements.

**Description:** A more detailed description of the layer type is optional.

**Subtypes:** You can select a subtype from the existing level types. This allows you to create a hierarchical structure, which will then be visible when you create the taxonomy levels.

[To the top of the page ^](#catalog_mgmt)

---


### Tab Lost+found {: #tab_lost_found}

This is where the documents of deleted taxonomy levels are stored. If you delete a level without merging it, OpenOlat copies its documents into a subfolder. The folder name consists of the identifier and the ID of the deleted level. If you merge the level with another level instead, the documents move to the target level.

![Lost+found tab with the folders of deleted taxonomy levels and the views Folders, Files and Trash](assets/catalog20_mgmt_tab_lost_found_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#catalog_mgmt)

---

## Further information {: #further_information}

[Authoring >](../area_modules/Authoring.md)<br>
[Taxonomy (admin manual) >](../../manual_admin/administration/Modules_Taxonomy.md)<br>
[How do I show my courses in the OpenOlat catalog? >](../../manual_how-to/catalog/catalog.md)<br>
[Create offer >](../area_modules/catalog2.0_angebote.md)<br>
[Catalog design >](../area_modules/catalog2.0_design.md)<br>
[The web catalog >](../area_modules/catalog2.0_web.md)<br>
[Set up catalog (admin manual) >](../../manual_admin/administration/Modules_Catalog_2.0.md)<br>

[To the top of the page ^](#catalog_mgmt)