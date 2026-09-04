# Licenses {: #licences}

The license management in OpenOlat is optional. Administrators configure it in
the system administration under:<br>
`Administration > Core functions > Licenses`

## Activating license sections {: #licences_activation}

![License management in the core functions: under Activate licenses in, the sections Folder, Question pool and Learning resources are listed as checkboxes, all three selected](assets/LizenzMgmt_aktivieren_EN.png){ class="shadow lightbox aside-right-lg" }

Licenses can be used in the following OpenOlat sections:

  * Folder
  * Question pool
  * Learning resources
  * Media Center

Under "Activate licenses in" the licenses are activated or deactivated for
these sections. After each change, OpenOlat reminds you to start the full text
search indexer so that the licenses are shown correctly in the search results.

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

In addition, own licenses can be created if the default license types are not
sufficient. "Create license" opens a dialog in which the license name, a
corresponding license text and a CSS class can be entered. License types
created in this way can only be edited afterwards, not deleted.

![Mandatory field Name, multi-line field License text and field CSS class with the buttons Cancel and Save in the dialog Create license](assets/LizenzMgmt_eigeneLizenz_EN.png){ class="shadow lightbox" }

All available licenses are listed in the overview. Use the arrows in the
columns "Up" and "Down" to change the display order of the licenses. The link
in the column "Translation" allows you to store the license name in another
language. Own licenses can be changed via the column "Edit".

The columns "Folder", "Question pool", "Learning resources" and "Media Center"
are only visible in the overview if the licenses are generally activated for
the respective section. Here it is possible to activate only specific license
types for the individual sections.

![Button Create license highlighted above the overview of license types with the activation checkboxes per section Folder, Question pool and Learning resources](assets/LizenzMgmt_Lizenztypen_EN.png){ class="shadow lightbox" }

License types that qualify as Open Educational Resource carry an OER flag.
Among the default license types, these are the seven Creative Commons licenses
and "Public domain". For own licenses, the flag is set in the dialog "Create
license" or "Edit license" with the checkbox "Qualifies as OER License". The
column "OER-License" of the overview shows the flag. [:octicons-tag-16:{ title="from Release 17.2 (OO-6683)" }](https://track.frentix.com/issue/OO-6683)

[To the top of the page ^](#licences)

---

## Set initial licenses {: #licences_initial}

![Drop-down Initial licensor opened with the options No licensor, Current user and Constant licensor, next to the drop-down Initial license for each section](assets/LizenzMgmt_initiale_EN.png){ class="shadow lightbox aside-right-lg" }

For the individual sections "Folder", "Question pool", "Learning resources" and
"Media Center", an initial license and an initial licensor can be set.

  *  **Initial license:** A license can be selected from all licenses available for this section.
  *  **Initial licensor:** You can choose between "No licensor", "Current user" and "Constant licensor". The "Constant licensor" can be entered or edited in the next step.

When a new document is added to the course element Folder, a new question to
the Question bank, a new learning resource in Authoring or a new media in the
Media Center, the stored license and the specified licensor are assigned
automatically.

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
