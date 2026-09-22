# Module Taxonomy {: #module_taxonomy}

You find the module in the system administration under:<br>
`Administration > Modules > Taxonomy`

!!! note "What is a taxonomy?"

    In OpenOlat, a taxonomy is a hierarchical indexing, often with a competence approach.
    Taxonomy can be activated and used in several OpenOlat areas:

    * [Document pool](Modules_Document_pool.md)
    * [Question bank](../../manual_user/area_modules/Question_Bank.md)
    * [ePortfolio](eAssessment_ePortfolio.md)
    * [Catalog](Modules_Catalog_2.0.md)

![Overview page of the taxonomies with activation status per area, menu item Taxonomy in the Modules menu of the system administration](assets/modules_taxonomy_entry_v1_en.png){ class="shadow lightbox" }

Directly on the overview page a new taxonomy structure can be created.

Several taxonomy structures can be created and activated for different purposes. The overview shows per taxonomy for which areas it is activated: Learning resources / Catalog, Question bank, Document pool, ePortfolio, Course Planner and Media Center. [:octicons-tag-16:{ title="Available from Release 20.3.0 (OO-9185)" }](https://track.frentix.com/issue/OO-9185){:target="_blank"}

Thus on one hand taxonomy structures can for example be built in the form of
subject, sphere of activity or competence structures. On the other hand
competences can be added to users which allows them access to the taxonomy.

**Example** of an elaborated taxonomy structure, according to subjects for the document pool:

![Example taxonomy structure HFM with the subjects MINT, Sport and Sprachen (languages), Taxonomy tab](assets/Taxonomie_Struktur_DE.png){ class="shadow lightbox" }

## Metadata {: #metadata}

When creating the metadata reference, title and if desired a description can
be inserted. These data can be edited in the tab "Metadata" afterward.
Additionally an ID is created automatically and if an external management
system has created the taxonomy, an external ID is created as well.
![Metadata tab of a taxonomy with the fields ID, External ID, identifier, name and description](assets/modules_taxonomy_metadata_de.png){ class="shadow lightbox" }

## Level types {: #level_types}

Level types are used to give a significance to the taxonomy structure. The can
for example be created for competence → sphere of activity → subject and sub
types can be created underneath each other. Therefore it is not necessary that
a level type is alway at the same place or on the same level of the taxonomy
structure.

To the level types certain configurations can be added.

In the tab "Level types" a new type can be created with "Add new level type".

#### Reference {: #level_type_identifier}

Often an abbreviation of the corresponding level is added here. The reference is shown in the table in the tab "Levels" in the column "Level type". The column is not shown by default, you switch it on with the gear icon above the table under "Displayed columns". It is thus recommended to choose a unique and logic reference.

#### Title {: #level_type_display_name}

This name is shown under Modules → document pool in the tab "Access permissions" in a written form and can therefore be longer than the reference.

#### CSS class {: #level_type_css_class}

If a corresponding css class is added in the theme it can be chosen here. Only icons can be added.

#### Visible {: #level_type_visible}

Here can be defined if the taxonomy level of this type should be visible.

#### Competences {: #level_type_competences}

If activated, this level type is available as a competence and can be used e.g. for competence-based keywording in ePortfolio entries.

#### Evidence of achievement {: #level_type_achievements}

Taxonomy levels with this level type can be activated here for the grouping of certificates of achievement.

#### Description {: #level_type_description}

If desired a short description of the level type can be added.

#### Sub types {: #level_type_sub_types}

Out of the already existing level types a sub type can be chosen. Like this it becomes possible to create a hierarchical structure. It will get visible when creating the taxonomy level.

![Level types tab with the list of level types and button "Add new level type"](assets/taxonomy-leveltypes.jpg){ class="shadow lightbox" }

## Create taxonomy {: #taxonomy}

In this tab the single taxonomy levels are created, imported, exported and shown.

When creating the following attributes are necessary:

#### Path {: #level_path}

With the path the position of the taxonomy level can be defined directly.

#### Reference {: #level_identifier}

With the reference an abbreviation of the level can be defined.

#### Type {: #level_type}

In the type the beforehand created level type can be chosen.

#### Order {: #level_sort_order}

*Currently Beta Feature.* Hereby a manual order is possible by adding a number from 1-XX. The taxonomy-tiers will get ordered ascending by the numbers ( 1,2,3,4, / 01,02,03,04,..)

#### Teaser image {: #level_teaser_image}

The image is uploaded as a file. Best results with size 240x100px, maximum 2 MB.

#### Background image {: #level_background_image}

The image is uploaded as a file. Best results with size 1324x240px, maximum 5 MB.

#### Title {: #level_display_name}

The title depends on the language and is used in different places: Catalog 2.0, Document Pool, e-Portfolio.

#### Description {: #level_description}

If desired a short description of the taxonomy level can be added. Displayed in the catalog below the level.

![Dialog "Create new taxonomy level" with the fields Path, Reference, Type, Order, Title and Description and the section Images with Teaser image and Background image](assets/modules_taxonomy_level_create_v1_en.png){ class="shadow lightbox" }

In the overview a hierarchical structure is now visible.

![Expanded list of the taxonomy ABC in the tab "Levels" with the columns Level, Reference, External ID and Sublevels](assets/modules_taxonomy_levels_overview_v1_en.png){ class="shadow lightbox" }

!!! tip "Competences"
    In the detail view competences can be added afterwards. Like this users get "access rights" for the single taxonomy levels.

4 different competences are distinguished. Following they are outlined
shortly:

  * **Teach**: A user with teach competence is qualified in this competence. Mostly this means he has a certain expert knowledge which he can hand over. Therefore learners will never have teach competences as the teach competence cannot be gained in OpenOlat. The teach competence is either added to a user manually or by an external management system. This competence manages the access to the [document pool](Modules_Document_pool.md) as well as to the question bank.
  * **Manage**: User can have a managing function for a certain area of the taxonomy. Therefore the must not have teach competence at the same time. This competence is mainly used in the question bank.
  * **Have**: This competence is not yet used in OpenOlat. In the future this competence can be gained by a learner through learning activities in OpenOlat (e.g. test). This competence has an expiry date.
  * **Target**: A learner has a target he wants to reach. It is the target to gain this competence.

!!! note "Note on Target"
    This competence is not yet used in OpenOlat.


### Export taxonomy  {: #export}

The taxonomy is downloaded as a .zip archive by clicking on the menu item (see image). This contains an EXCEL table with the hierarchical structure of the taxonomy level and a folder structure (media/level1/background;media/level1/teaser;) with teaser and background images of the taxonomy, if any are available. (more under -> [Catalog 2.0](../../manual_user/area_modules/catalog2.0.md))
![Opened three-dot menu with the entries Export taxonomy levels and Import taxonomy levels, on the right above the list of taxonomy levels](assets/Taxonomie_exportieren.png){ class="shadow lightbox" }


### Import taxonomy [:octicons-tag-16:{ title="from Release 15.4 (OO-5177)" }](https://track.frentix.com/issue/OO-5177){:target="_blank"} {: #import}

**Insert data**

![Step "Insert data" of the import wizard with the column names of the taxonomy structure (A) and the upload of the background/teaser images (B)](assets/taxonomy-import-overview.png){ class="shadow lightbox" }

Here we have the choice between different options:
We can import only the structure (**A**), add images to an existing structure (**B**) or import a structure including images (**A+B**).

**Review changes**

![Step "Review changes" with a warning icon per row when the taxonomy level already exists and can be updated](assets/taxonomy-import-step2.jpg){ class="shadow lightbox" }

After the import, the taxonomy and the added images are reviewed again in the second step. An icon indicates whether the taxonomy level already exists and should be completed and overwritten with the files and uploaded information.

**Select update mode**

![Step "Select update mode" with checkbox "Update taxonomies" and the number of affected taxonomy levels](assets/taxonomy-import-step3.jpg){ class="shadow lightbox" }

Here you can decide whether you want to overwrite the existing taxonomy levels or just add new taxonomy levels. If you want to add media, you _must_ overwrite the changes here.

### Import/add taxonomy structure only {: #import_add_structure}

1. First download the current taxonomy. If you don't have one yet, use the template.

![Excel template of the taxonomy structure with the columns Path, Identifier, Type, Order as well as Language, Display name and Description per language](assets/taxonomystructure-import.jpg){ class="shadow lightbox" }

2. Inside the excel sheet you add new taxonomy levels or change existing ones. The path that indicates the hierarchical structure is important. If this is incorrect, certain layers cannot be imported.
If you have activated different languages in OpenOlat and use the [Catalog 2.0](../../manual_user/area_modules/catalog2.0.md), it is advisable to make the title and description language-dependent. Additional languages can be added by copying the columns "Language", "Title" & "Description" and adding a new, existing language, title + description for each taxonomy level.

3. The modified table is now selected _without_ the header and copied into the input field. When proceeding to the next wizard step, the cells are checked for correctness. In case of errors, error messages appear directly at the input field.

### Import/add background/teaser image only {: #import_add_media}

![Folder structure of the unpacked taxonomy export with the subfolders "background" and "teaser" per taxonomy level](assets/taxonomy-media-folder-structure.jpg){ class="shadow lightbox" }

1. If you want to add background images to an existing taxonomy, you should first export the taxonomy.
2. Unzip the archive and place the images in the "media" folder.
3. zip the entire archive again and insert it under paragraph B in the wizard.

Alternatively, it is also possible to download the existing templates under the respective links and adapt them accordingly.

## Automatic assignment by AI [:octicons-tag-16:{ title="from Release 21.0 (OO-9428)" }](https://track.frentix.com/issue/OO-9428){:target="_blank"} {: #ai_matching}

The AI works out what an image or a text is about and assigns the result to a taxonomy level on its own. It compares the meaning, not the exact wording. An English text therefore also finds a level with a German name, a synonym finds the intended level, and a related term finds the one that is closest in content.

The assignment takes effect when you upload an image in the [Media Center](../../manual_user/basic_concepts/Media_Center_Items.md#metadata_ai) and when you [import Markdown files into the Content Editor](../../manual_user/basic_concepts/Content_Editor.md#markdown). The result appears in the field "Subjects" of the metadata and can be changed there. A taxonomy level that hangs on a media item or on a learning resource is called a subject there.

OpenOlat only searches the taxonomies that are selected for the Media Center. You set these in the system administration under `Administration > Modules > Media Center` in the field "Linked taxonomies", see [Module Media Center: Taxonomy](Modules_Media_Center.md#taxonomy). The overview under `Administration > Modules > Taxonomy` shows per taxonomy for which areas it is activated.

### Requirements {: #ai_matching_requirements}

The assignment via embedding model needs three settings in the AI module, see [External tools: AI module](External_Tools_AI.md#ai_functions):

* The AI feature "Taxonomy Matching (Embeddings)" is activated.
* An AI provider is selected that offers an embedding model.
* An embedding model is selected.

If one of these settings is missing, OpenOlat only assigns a level when the result of the AI is identical to the title or to the reference of the level. Upper and lower case does not matter.


### What the AI compares {: #ai_matching_maintenance}

The title and the description of a taxonomy level decide whether the AI finds it. You maintain both under `Administration > Modules > Taxonomy` in the tab "Levels", not in the Media Center.

OpenOlat compares the result of the AI with three entries per taxonomy level, in German and in English:

* the title,
* the title together with the parent levels,
* the title, the parent levels and the description together.

The third entry is dropped when the level has no description. A level with a meaningful title and a description is therefore found more reliably than a level that only carries an abbreviation. Maintain both entries in the second language as well.

### Interplay of AI and subjects {: #ai_matching_interplay}

Which subject a media item receives depends on the trigger:

| Trigger | What OpenOlat assigns | What is needed for it |
|---|---|---|
| Button "Generate metadata with AI" when uploading an image | the best matching subject, exactly one | The AI feature "Image Description Generator" supplies what the image is about. |
| Import of a Markdown file into the Content Editor | all matching subjects, up to three per taxonomy | The same AI feature. The assignment runs in the background after saving. |
| Enter metadata manually | nothing | You select the subject yourself in the field "Subjects". |

The AI therefore supplies what the media item is about, and the taxonomy matching looks for the matching subject. Without the AI feature "Image Description Generator" this entry stays empty, and the taxonomy matching has nothing to compare. The assigned subject is a suggestion and can be changed in the metadata at any time.

If the field "Subjects" stays empty although the AI has generated title, description and tags, first check whether a taxonomy is selected for the Media Center.

[To the top of the page ^](#module_taxonomy)

## Lost+Found {: #lost_found}
**Last tab in the overview**

All deleted elements of the tab "Levels" end up here.

!!! note "Note"
    Deleted objects cannot currently be restored.

## Further information {: #further_information}

**Mentioned on this page**<br>
[Document pool >](Modules_Document_pool.md)<br>
[Question bank >](../../manual_user/area_modules/Question_Bank.md)<br>
[ePortfolio >](eAssessment_ePortfolio.md)<br>
[Catalog >](Modules_Catalog_2.0.md)<br>
[Catalog 2.0 >](../../manual_user/area_modules/catalog2.0.md)<br>
[Media Center: information and settings for individual media >](../../manual_user/basic_concepts/Media_Center_Items.md)<br>
[Content Editor >](../../manual_user/basic_concepts/Content_Editor.md)<br>
[External tools: AI module >](External_Tools_AI.md)<br>
[Module Media Center >](Modules_Media_Center.md)

**Further reading**<br>
[Course Planner >](Modules_Course_Planner.md)

[To the top of the page ^](#module_taxonomy)