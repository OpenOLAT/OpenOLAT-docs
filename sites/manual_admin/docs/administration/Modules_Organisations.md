# Modules: Organisations

##  Activation of the organizational structures

The Organizations module is optionally available in OpenOlat and must be
activated in Administration. 

!!! tip "Activation"
	Customers of frentix please contact
	[contact@frentix.com](mailto:contact@frentix.com) for this. After activation,
	various additional settings can be made for the system-wide configuration. For
	systems with the fx-Release, these adjustments are made by frentix.

	:material-alert: **Not a frentix hosting-client?** Please ask your local system operator!

![](assets/Org_Aktivierung_DE.png){ class="shadow lightbox" }

## Creating organizational structures

In the tab "Organizational structure" you can find the already created
organizations with their sub-organizations displayed as a tree structure.

New organizations can be created using the "Create new organization" button,
or for existing organizations using the cogwheel and "Create suborganization".
In addition to the designation and the name, a description for the element can
be entered. Furthermore, the assignment of the organization type is done here.

During creation, each organizational element can be linked to a corresponding
organizational type and thus a hierarchical structure can be built. The
representation of process and organizational structures is possible, but a
matrix organization cannot be represented.

On the one hand, members of various roles can be assigned to each level of the
organization.  On the other hand, learning resources and curricula can also be
linked to the organizational structures.

 **Role assignment** is possible

  * on a specific organization
  * on a specific organization and all organizational structures subordinated to this organization
  * on a specific organization and all organizational structures subordinate to this organization

 **Course (or learning resource) assignment** can be directly assigned on each
organizational element.

The **assignment of curricula** is done in the curriculum management at the
respective curriculum.

Further options can be accessed via the cogwheel on the respective
organizational element. Thus, the organization can be edited or deleted. It is
also possible to move the element in the organization tree or to create a new
suborganization directly.

  

![](assets/Org_Optionen_de1.png){ class="shadow lightbox" }

### Metadata

If an organizational structure is selected, the metadata of the organizational
element can be adjusted or supplemented. Next to the name and label, the
description or the assigned organization type for the element can be updated.

![](assets/Org_Metadata_DE.png){ class="shadow lightbox" }

### User administration

In the tab "User administration" you get a list with the users currently
assigned to this element. Existing users can also be removed.

Via "Add user" further users can be added to a certain role. For this purpose,
the desired role is selected from the listed roles. In the following dialog,
users can be searched for and added according to the selection. It is possible
to add multiple users.

![](assets/Org_Benutzerverwaltung_DE.png){ class="shadow lightbox" }

### Learning resources

The "Learning resources" tab displays courses directly assigned to the
organizational element. These can also be removed here. Via "Add courses" you
can search for further own and available resources in a dialog in order to
assign them to the organizational element.

  
## Defining organization types

The organization types define which elements an organizational structure can
contain and give a closer meaning to these elements. The types can also
represent a hierarchical structure, but this is not mandatory. An example for
organization types is `Company --> Division --> Department`.

Further types can be created via "Create organization type". In addition to
the designation (indicator) and the name, a description can be entered. At
this point, it is possible to define a layout that is only valid for this
organization type via CSS class. In addition, already existing types can be
subordinated to the new organization type.

