# Licenses {: #licences}

With a license, you state for files, questions, learning resources and media
how others may use them. Licenses are optional in OpenOlat. Administrators
configure them in the system administration under:<br>
`Administration > Core functions > Licenses`

## Activate licenses in areas [:octicons-tag-16:{ title="from Release 12.4 (OO-3170)" }](https://track.frentix.com/issue/OO-3170) {: #licences_activation}

![Highlighted checkboxes under Activate licenses in: Folder, Media Center, Question bank and Learning resources, all four switched on](assets/licenses_activate_v1_en.png){ class="shadow lightbox aside-right-lg" }

Licenses can be used in the following OpenOlat areas:

  * Folder
  * Media Center
  * Question bank
  * Learning resources

Under "Activate licenses in", you switch the licenses on or off per area.
After each change, OpenOlat reminds you to start the full text search indexer
so that the search results show the licenses correctly.

[To the top of the page ^](#licences)

---

## License types {: #licences_types}

OpenOlat provides 12 default license types: seven Creative Commons licenses
(CC0, CC BY, CC BY-SA, CC BY-ND, CC BY-NC, CC BY-NC-SA, CC BY-NC-ND), "Public
domain", "All rights reserved", "YouTube license", "Free text" and "No
license". These default license types cannot be deleted. Information on
Creative Commons can be found in the
[Wikipedia](http://en.wikipedia.org/wiki/Creative_Commons "Wikipedia") and on
[www.creativecommons.org](http://www.creativecommons.org/
"www.creativecommons.org"). While the Creative Commons licenses all allow
copying and redistributing a protected work, the "All rights reserved" license
only permits use in the context intended by the author.

If the default license types are not sufficient, you create your own
licenses. The button "Create license" opens a dialog with the fields "Name",
"License text" and "CSS class". Own license types cannot be deleted.

![Mandatory field Name, multi-line field License text and field CSS class with the buttons Cancel and Save](assets/LizenzMgmt_eigeneLizenz_EN.png){ class="shadow lightbox" title="Dialog Create license" }

The overview lists all available licenses. With the link in the column
"Translation", you store the license name in another language.

The columns "Folder", "Media Center", "Question bank" and "Learning resources"
only appear in the overview if the licenses are switched on for the respective
area. In these columns, you switch individual license types on or off for each
area.

![Highlighted button Create license and highlighted columns Folder, Media Center, Question bank and Learning resources, in which you switch each license type on or off per area](assets/licenses_types_v1_en.png){ class="shadow lightbox" title="Overview of license types · 2026.10.26" }

License types that qualify as Open Educational Resource carry an OER flag.
Among the default license types, these are the seven Creative Commons licenses
and "Public domain". For own licenses, you set the flag in the dialog "Create
license" with the checkbox "Qualifies as OER License". The
column "OER-License" of the overview shows the flag. [:octicons-tag-16:{ title="from Release 17.2 (OO-6683)" }](https://track.frentix.com/issue/OO-6683)

[To the top of the page ^](#licences)

---

## Set initial licenses {: #licences_initial}

![Highlighted fields Initial license and Initial licensor of the area Folder, below them the same fields with their own values for Media Center and Question bank](assets/licenses_initial_v1_en.png){ class="shadow lightbox aside-right-lg" }

For the areas "Folder", "Media Center", "Question bank" and "Learning
resources", you set an initial license and an initial licensor. The settings
appear for each area in which licenses are switched on.

  *  **Initial license:** All licenses that are switched on for this area are available for selection.
  *  **Initial licensor:** "No licensor", "Current user" and "Constant licensor" are available for selection. If "Constant licensor" is selected, you enter the name with the button "Edit" in the dialog "Edit licensor".

When someone adds a new document to the course element Folder, a new question
to the Question bank, a new learning resource in Authoring or a new medium in
the Media Center, OpenOlat automatically assigns the stored license and the
specified licensor.

[To the top of the page ^](#licences)

---

## Further information {: #further_information}

[Creative Commons in the Wikipedia >](http://en.wikipedia.org/wiki/Creative_Commons)<br>
[www.creativecommons.org >](http://www.creativecommons.org/)<br>
[Module Media Center >](Modules_Media_Center.md)<br>
[Files and Folders >](Files_and_Folders.md)<br>
[Module OAI-PMH >](Modules_OAI.md)<br>
[Course Settings - Tab Metadata >](../../manual_user/learningresources/Course_Settings_Metadata.md)

[To the top of the page ^](#licences)
