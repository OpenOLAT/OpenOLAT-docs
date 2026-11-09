# CP learning content: Administration {: #cp_administration}

You create a CP learning content once and then integrate it into as many courses as you like. In the "Administration" menu of the CP learning content, you edit its pages, define how OpenOlat displays them, and copy, export or delete the learning content. The menu is visible to owners of the learning resource, learning resource managers and administrators.

The "Administration" menu contains these entries:

* **Settings**: see [Settings](#settings).
* **Members management**: Here you add further owners. With standalone usage, you also manage coaches and participants here, see [Members management](../Members_management.md).
* **Edit content**: opens the CP editor, see [Edit content](#edit_content).
* **Offer types**: only active if the CP learning content is configured as bookable, see [Offer types](../Offer_Types.md).
* **Further entries**: "Copy", "Export content", "About this CP content" and "Delete" work as for all learning resources, see [Detailed View of Learning Resources](../Detailed_View_of_Learning_Resources.md). "Export content" downloads the CP learning content as a ZIP file.

[To the top of the page ^](#cp_administration)

---


## Edit content {: #edit_content}

You edit the pages and the structure of the CP learning content in the CP editor. You open it under:<br>
`CP learning content > Administration > Edit content`

How to add, import, move and edit pages in the CP editor is described on the page [CP editor](../CP_Editor.md). If an external system manages the content, the entry cannot be selected.

[To the top of the page ^](#cp_administration)

---


## Settings {: #settings}

You open the settings under:<br>
`CP learning content > Administration > Settings`

The tabs appear in this order:

* **Metadata**: see [Course Settings - Tab Metadata](../Course_Settings_Metadata.md).
* **Info**: see [Course Settings - Tab Info](../Course_Settings_Info.md).
* **Share**: see [Course Settings - Tab Share](../Course_Settings_Share/index.md).
* **Catalog**: only if the catalog in version 1 is enabled and the CP learning content has the usage "Standalone", see [Course Settings, Tab Catalog](../Course_Settings/index.md#catalog).
* **Quota**: see [below](#tab_quota).
* **Layout**: see [below](#tab_layout).
* **Options**: the access for participants in status "Finished", see [Course Settings - Tab Options](../Course_Settings_Options.md). The tab is missing if the usage "Embedding" is selected in the "Share" tab.

The pages on the course settings apply to all learning resources. Some fields there only exist for courses, which is noted at the field.

### Tab "Quota" {: #tab_quota}

Images, videos and PDF files make a CP learning content grow quickly. In the "Quota" tab, you define how much storage space it may occupy at most: "Quota (KB)" limits the whole learning content, "Upload limit (KB)" a single uploaded file.

Below the fields, the tab lists the system-wide "Default quotas" and highlights the row "Learning resources". This default value applies as long as the CP learning content has no quota of its own. With "Reset to default quota", the default value applies again. System administrators define the default values, see [Files and Folders](../../../manual_admin/administration/Files_and_Folders.md#files_and_folders_quotas).

Only administrators, system administrators, learning resource managers, user managers and role managers see the "Quota" tab.

### Tab "Layout" {: #tab_layout}

In the "Layout" tab, you define how OpenOlat displays the pages of the CP learning content, for example whether the OpenOlat layout is applied to the pages and how high the display area is. The settings apply when you open the CP learning content directly. In addition, the course element "CP learning content" adopts them if the option "Use from learning resource layout configuration" is selected under "Use standard configuration" in its "Display content" tab.

The tab shows the same fields as the "Display content" tab in the course element "HTML page": "Display mode", "Embed Javascript library", "Embed glossary terms", "Display height", "Adapt layout", "Content character set" and "Javascript character set". The fields are described in the section [Tab Display content](../Course_Element_HTML_Page.md#layout).

[To the top of the page ^](#cp_administration)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Members management >](../Members_management.md)<br>
[Offer types >](../Offer_Types.md)<br>
[Detailed View of Learning Resources >](../Detailed_View_of_Learning_Resources.md)<br>
[CP editor >](../CP_Editor.md)<br>
[Course Settings - Tab Metadata >](../Course_Settings_Metadata.md)<br>
[Course Settings - Tab Info >](../Course_Settings_Info.md)<br>
[Course Settings - Tab Share >](../Course_Settings_Share/index.md)<br>
[Course Settings >](../Course_Settings/index.md)<br>
[Course Settings - Tab Options >](../Course_Settings_Options.md)<br>
[Files and Folders >](../../../manual_admin/administration/Files_and_Folders.md)<br>
[Course Element "HTML page" >](../Course_Element_HTML_Page.md)

**Further reading**<br>
[Course Element "CP learning content" >](../Course_Element_CP_Learning_Content.md)<br>
[How do I create a content package? >](../../../manual_how-to/content_package/content_package.md)

[To the top of the page ^](#cp_administration)
