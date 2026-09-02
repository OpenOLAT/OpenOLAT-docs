# Catalog 2.0 - Management {: #catalog_mgmt}


## Short description of catalog management {: #description}

Catalog management of Catalog 2.0 is not a responsibility assigned to a specific role. Rather, it is a function for editing the taxonomies used in the catalog. Users who hold this right (the "Manage" competence) can edit these taxonomies and parts of them without being an administrator.


## Where can I access the catalog management? {: #access}

Access to catalog management is via a link in the catalog.
In the catalog, authorized users will also find the following links in the top-right corner, below the header:

- **Catalog management**
- **Jump to administration**

![Highlighted links Catalog management and Jump to administration below the catalog header, in the Catalog menu](assets/catalog20_mgmt_access_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#catalog_mgmt)

---


## Who sees the access links in the catalog? {: #access_links}

The **"Catalog management"** link is available to

- Learning resource managers
- Administrators
- System administrators
- Users who hold the "Manage" competence on a taxonomy level

Whether learning resource managers get the link is set by system administrators in the system administration: `Administration > Modules > Catalog > Settings`, field "Taxonomy editable by".

The **"Jump to administration"** link is available to

- System administrators

[To the top of the page ^](#catalog_mgmt)

---


## How do you obtain the right (the competence) for catalog management? [:octicons-tag-16:{ title="from Release 20.1 (OO-8544)" }](https://track.frentix.com/issue/OO-8544) {: #competence}

The "Manage" competence (the right to edit the taxonomies used in the catalog) can be granted in two ways:

**Option 1:**<br>
By system administrators in the system administration:<br>
`Administration > Modules > Taxonomy > "Taxonomy title" > "Taxonomy level" > Tab "Management" > Button "Add manager"`<br>
The taxonomy must be enabled for the catalog. Open it with "view / edit".

**Option 2:**<br>
By user managers:<br>
`User management > "Person" > Tab "Competences" > Button Add "Manage"`

Once the competence has been granted, the "Catalog management" link appears for that person in the top-right corner, below the catalog header.

!!! info "Important"

    Catalog management is not limited to a specific organizational unit, although the role of learning resource manager may be restricted to a specific organizational unit. (Taxonomies are also not limited to organizational units.)

[To the top of the page ^](#catalog_mgmt)

---


## Is it possible to edit learning resources in catalog management? {: #functions}

The content of learning resources in the catalog is edited in the authoring area. You therefore edit courses [in the authoring area](../area_modules/Authoring.md). They are also deleted there, for example when they have ended.

### Tab Levels  {: #tab_level}
The editing options for the subjects (taxonomy levels) include:

- Edit
- Move
- Merge
- Assign level type
- Deleting elements of the taxonomy level / subtaxonomies
- Creating new sub-levels

Under the three dots to the right of the "Create new taxonomy level" button, you also find options to import taxonomy levels or export them all. The export can be downloaded as a ZIP archive, which contains an Excel spreadsheet with the hierarchical structure of the taxonomy levels.

![Actions Assign level type, Move, Merge, Delete and the row menu of a level, in the Levels tab](assets/catalog20_mgmt_edit_v1_de.png){ class="shadow lightbox" }


!!! info "Important"

    The design of launchers, sections, etc., is reserved for system administrators.


[To the top of the page ^](#catalog_mgmt)

---


### Tab Metadata {: #tab_metadata}

The "Metadata" tab holds the data of the taxonomy itself, not of its levels. You open the metadata of an individual taxonomy level through its row in the "Levels" tab.

![ID and External ID fixed, required fields Reference and Title, plus the description editor, in the Metadata tab](assets/catalog20_mgmt_tab_metadata_v1_de.png){ class="shadow lightbox" }


**ID:** The ID is generated automatically and allows the object to be uniquely identified.

**External ID:** If an external management system created the taxonomy, the external ID is generated in addition to the automatically generated ID.

**Reference:** (Required field) Select a unique and logical reference for the taxonomy. This reference appears in the header above the title and is more practical for many purposes than the full title (which may be more understandable and colloquial).

**Title:** (Required field) The title is used in various places (Catalog 2.0, Document Pool, e-Portfolio, Question Pool). It should provide a brief and accurate description of the taxonomy.

**Description:** Entering a more detailed description of the taxonomy is optional.

[To the top of the page ^](#catalog_mgmt)

---


### Tab Level types {: #tab_leveltype}

Use the "Add new level type" button to add another level type. The following fields are available in the edit dialog.


![List of level types with their competence and evidence-of-achievement settings and the Add new level type button, in the Level types tab](assets/catalog20_mgmt_tab_leveltype_v1_de.png){ class="shadow lightbox" }

![Reference and Title as required fields, plus CSS class, Visible, Competences and Evidence of achievement, in the Edit dialog](assets/catalog20_mgmt_tab_leveltype_edit_v1_de.png){ class="shadow lightbox" }


**Reference:** In addition to the title, a reference must be provided.

**Title:** Enter an appropriate title to describe the level type.

**CSS class:** If a corresponding CSS class is defined in the theme, it can be selected here.

**Visible:** This setting determines whether all taxonomy levels of this type should be visible.

**Competences:** Users can be assigned competences in user management. Selecting this option enables taxonomy levels with this level type to be used as competences.

**Evidence of achievement:** Selecting this option enables taxonomy levels with this level type for grouping evidence of achievements.

**Description:** A more detailed description of the level type is optional.

**Sub types:** You can select a subtype from the existing level types. This allows you to create a hierarchical structure, which will then be visible when you create the taxonomy levels.


[To the top of the page ^](#catalog_mgmt)

---


### Tab Lost+found {: #tab_lost_found}

This is where the documents of deleted taxonomy levels are stored. If you delete a level without merging it, OpenOlat copies its documents into a subfolder. The folder name consists of the reference and the ID of the deleted level. If you merge the level with another level instead, the documents move to the target level.

![Folders of deleted taxonomy levels with the views Folder, Files and Trash, in the Lost+found tab](assets/catalog20_mgmt_tab_lost_found_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#catalog_mgmt)

---


## Further information {: #further_information}

[Authoring >](../area_modules/Authoring.md)<br>
[Taxonomy (admin manual) >](../../manual_admin/administration/Modules_Taxonomy.md)<br>
[How do I show my courses in the OpenOlat catalog? >](../../manual_how-to/catalog/catalog.md)<br>
[Create offer >](../area_modules/catalog2.0_angebote.md)<br>
[Catalog design >](../area_modules/catalog2.0_design.md)<br>
[The web catalog >](../area_modules/catalog2.0_web.md)<br>
[Set up catalog (admin manual) >](../../manual_admin/administration/Modules_Catalog_2.0.md)

[To the top of the page ^](#catalog_mgmt)
