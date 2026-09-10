# Module Document Pool {: #module_document_pool}

!!! info "What is the document pool?"

	The document pool is a taxonomy based document management which can be
	unlocked competence based. For example the resource management of learning
	material based on the teach competence can be built.

	The document pool can be activated for all OpenOlat users, also for learners.

	The documents in the document pool are only available in the document pool and
	cannot be added into a course.

	Further information can be found in the chapter [taxonomy](../administration/Modules_Taxonomy.md).

The document pool can be added as a site in the main navigation on top.

![Site Document pool in the main navigation with the taxonomy tree on the left and the file storage of the selected level on the right, here the folders Grammatik and Texte](assets/Dokumentenpool_beispiel_DE.png){ class="shadow lightbox" }

## Tab Document pool

In the tab "Document pool" the document pool can be activated. In the main
navigation it becomes only visible if the corresponding site is activated.

Afterward the WebDAV mount point can be defined here. Then a
taxonomy must be chosen. The content of the taxonomy is defined under
`Administration > Modules > Taxonomy`.

Additionally templates can be activated. The templates are shown in the
document pool directly below the main navigation. There only system
administrators can upload file. They are available for everybody, independent
of the access rights in the document pool.

![Tab Document pool in the system administration with the checkbox Enable document pool, the fields WebDAV mount point and Taxonomy, and the checkbox Enable templates](assets/documentpool_documentpool.png){ class="shadow lightbox" }

## Tab Access permission

Here the rights of the single level types of the taxonomy can be defined. In
order that a competence type appears it must have been created under
`Administration > Modules > Taxonomy` in the tab "Level types".

* **Use in document pool**: With this option it is defined if this competence type appears in the document pool.
* **Documents enabled**: Only if this option is activated files can be uploaded on this level. Otherwise this level is only shown as structure without folder content.
* **Manager competence**: Allow or not.<br>
* **Teacher competence**: The teacher competence defines the access rights for the individual levels in the document pool. First it is selected whether users with teacher competence get read access to this level. If yes, these users can read the content of this level. In addition, a number defines how many levels above should also get read access.<br>
If "Allow write access" is also enabled, these users can also upload
documents.<br>
* **Have competence**: Allow read access or not.<br>
* **Target competence**: Allow read access or not.

These settings need to be repeated for all defined competence types.

Additionally the corresponding competence need to be added to the users. This
happens either by the synchronization of an external management system or
directly in OpenOlat. In OpenOlat this can be done either in the user
management or in `Administration > Modules > Taxonomy`.

Settings can also be made here for the "Field of action" and "Subject" competence types.

![Tab Access permission, competence type "Handlungsfeld": switches for use, documents, manager, have and target competence, teacher competence additionally with a number for levels above](assets/documentpool_ap.png){ class="shadow lightbox" }

## Tab Info page

Finally an info page can be designed. It appears on the top level of the
document pool. It is recommended to add here a user manual for the usage of
the document pool.

![Info page at the top level of the site Document pool with the welcome text](assets/Dokumentenpool_Infoseite.png){ class="shadow lightbox" }

## Further information {: #further_information}

**Mentioned on this page**<br>
[Module Taxonomy >](Modules_Taxonomy.md)

[To the top of the page ^](#module_document_pool)
