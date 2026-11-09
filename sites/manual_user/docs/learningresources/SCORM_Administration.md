# SCORM 1.2: Administration {: #scorm_administration}

You import a SCORM package once as a learning resource "SCORM 1.2" and then integrate it into courses. In the "Administration" menu of the learning resource, you replace the package with a new version, define how OpenOlat displays it, and copy, export or delete the learning resource. The menu is visible to owners of the learning resource, learning resource managers and administrators.

The "Administration" menu contains these entries:

* **Settings**: see [Settings](#settings).
* **Members management**: Here you add further owners. With standalone usage, you also manage coaches and participants here, see [Members management](Members_management.md).
* **Offer types**: only active if the learning resource is configured as bookable, see [Offer types](Offer_Types.md).
* **Replace SCORM**: see [Replace SCORM](#replace_scorm).
* **Further entries**: "Copy", "Export content", "About this SCORM 1.2" and "Delete" work as for all learning resources, see [Detailed View of Learning Resources](Detailed_View_of_Learning_Resources.md). "Export content" downloads the SCORM package as a ZIP file.

The learning resource "SCORM 1.2" has no editor. You change a SCORM package outside OpenOlat and upload the new version with "Replace SCORM".

[To the top of the page ^](#scorm_administration)

---


## Replace SCORM [:octicons-tag-16:{ title="from Release 18.1.1 (OO-7096)" }](https://track.frentix.com/issue/OO-7096) {: #replace_scorm}

If you have revised a SCORM package, replace it in the existing learning resource. The learning resource stays the same, and the courses that integrate it show the new package afterwards. You open the dialog under:<br>
`SCORM 1.2 > Administration > Replace SCORM`

In the field "SCORM file upload", select the ZIP file of the new SCORM package. OpenOlat checks the file right after you select it. If it is a valid SCORM package, the button "Replace SCORM" becomes active, and a click on it replaces the previous package. If OpenOlat does not recognise the file, the dialog reports that the format or the version is not supported.

If the learning resource is already integrated into courses, the dialog states the number of these courses. Replacing a package that is already in use can lead to inconsistencies. Afterwards, check the configuration of the course elements "SCORM 1.2" that integrate the package, see [Course Element "SCORM 1.2"](Course_Element_SCORM_Learning_Content.md#editor_tab_learning_content).

[To the top of the page ^](#scorm_administration)

---


## Settings {: #settings}

You open the settings under:<br>
`SCORM 1.2 > Administration > Settings`

The tabs appear in this order:

* **Metadata**: see [Course Settings - Tab Metadata](Course_Settings_Metadata.md).
* **Info**: see [Course Settings - Tab Info](Course_Settings_Info.md).
* **Share**: see [Course Settings - Tab Share](Course_Settings_Share/index.md).
* **Catalog**: only if the catalog in version 1 is enabled and the learning resource has the usage "Standalone", see [Course Settings - Tab Catalog](Course_Settings_Catalog.md).
* **Layout**: see [below](#tab_layout).
* **Options**: the access for participants in status "Finished", see [Course Settings - Tab Options](Course_Settings_Options.md). The tab is missing if the usage "Embedding" is selected in the "Share" tab.

The pages on the course settings apply to all learning resources. Some fields there only exist for courses, which is noted at the field.

### Tab "Layout" {: #tab_layout}

In the "Layout" tab, you define how OpenOlat displays the SCORM package, for example unchanged in the display mode "Standard" or with the OpenOlat layout. The settings apply when you open the learning resource directly. In addition, the course element "SCORM 1.2" adopts them if the option "Use from learning resource layout configuration" is selected under "Use standard configuration" in its "Display content" tab.

The tab shows the same fields as the "Display content" tab of the course element: "Display mode", "Embed Javascript library", "Embed glossary terms", "Display height", "Adapt layout", "Content character set" and "Javascript character set". The fields are described in the section [Tab "Display content"](Course_Element_SCORM_Learning_Content.md#editor_tab_display_content). For SCORM packages, the display mode "Standard" is recommended because OpenOlat has no influence on the design of the package.

[To the top of the page ^](#scorm_administration)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Members management >](Members_management.md)<br>
[Offer types >](Offer_Types.md)<br>
[Detailed View of Learning Resources >](Detailed_View_of_Learning_Resources.md)<br>
[Course Element "SCORM 1.2" >](Course_Element_SCORM_Learning_Content.md)<br>
[Course Settings - Tab Metadata >](Course_Settings_Metadata.md)<br>
[Course Settings - Tab Info >](Course_Settings_Info.md)<br>
[Course Settings - Tab Share >](Course_Settings_Share/index.md)<br>
[Course Settings - Tab Catalog >](Course_Settings_Catalog.md)<br>
[Course Settings - Tab Options >](Course_Settings_Options.md)

**Further reading**<br>
[CP learning content: Administration >](CP_Administration/index.md)<br>
[Assessment of course modules >](Assessment_of_course_modules.md)

[To the top of the page ^](#scorm_administration)
