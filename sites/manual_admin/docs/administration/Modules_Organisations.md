# Module Organisations {: #organisations}

The "Organisations" module is optionally available in OpenOlat. It is activated in the system administration under `Administration > Modules > Organisations`.

!!! tip "Activation"

    Customers of frentix please contact [contact@frentix.com](mailto:contact@frentix.com) for the activation. After activation, various additional settings can be made for the system-wide configuration. For systems with the fx-Release, these adjustments are made by frentix.

    **Not a frentix hosting customer?** Please ask your system operator!

## Tab Configuration {: #tab_configuration}

![Activation of the Organisations module, the e-mail domain mapping and the legal documents folder in the Configuration tab](assets/organisations_tab_config_v2_de.png){ class="shadow lightbox" }

In the "Configuration" tab

* the Organisations module is activated
* the e-mail domain mapping is activated (can only be activated if the Organisations module is activated)
* the folder for legal documents is activated
* the "Status" section, which shows information for administrators

The company structure can be mapped in the "Organisations" module. Roles, rights and the visibility of courses and content can then be made dependent on membership of a specific organisation.

The ability of course participants to self-register can also be made dependent on membership of a specific organisation. This restriction is set up by comparing the e-mail address of new users against the stored e-mail domains and automatically assigning them to a specific organisation.

[To the top of the page ^](#organisations)

---

## Tab Organisations structures {: #tab_structure}

The "Organisations structures" tab shows the organisations already created, together with their sub-organisations, as a tree structure.

### Creating and editing organisations {: #create_and_edit}

![Tree structure of the organisations with their sub-organisations in the Organisations structures tab](assets/organisations_tab_structure_v2_de.png){ class="shadow lightbox" }

New organisations can be added using the "Create new organisation" button at the top right, or for existing organisations by clicking the three dots and "Add new organisation under this one".

To move an existing organisation, click the three dots and "Move organisation". In the window, select the organisation under which it is to be placed in future and confirm with "Move organisation". If "Move organisation" is missing under the three dots, an external system prevents the organisation from being moved. Its sub-organisations move along. The window only offers organisations under which the [organisation type](#tab_types) of the moved organisation is allowed. Roles that the organisation inherited from its previous parent organisation are dropped; the inherited roles of the new parent organisation are added. When you move an organisation, OpenOlat resets the rights that you have set in it for [line managers](#edit_linemanager) and [education managers](#edit_education_manager). Note them down beforehand and set them again after the move.

!!! info "Moving upwards takes two steps"

    An organisation cannot be moved directly into an organisation that is above it in the tree structure. OpenOlat then reports "An organisation cannot be moved into a parent or sub-organisation of itself." First move the organisation into an organisation that is neither above it nor below the target organisation, and from there into the target organisation. frentix customers cannot carry out this intermediate step themselves and contact frentix support: [support@frentix.com](mailto:support@frentix.com)

If an organisation is selected in the tree structure, its metadata and other assignments can be adjusted or supplemented.

![Legal documents folder in the "Legal documents" tab of an organisation](assets/organisations_tab_structure_legal_documents_v1_de.png){ class="shadow lightbox" }

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "Legal documents"`<br>
If the folder has been activated under `Administration > Modules > Organisations > Tab "Configuration"`, this tab is displayed for administrators and other administrative roles. Administrators can store documents on organisation-specific matters in it. Other administrative roles only have read access. [:octicons-tag-16:{ title="from Release 20.0 (OO-8233)" }](https://track.frentix.com/issue/OO-8233){:target="_blank"}

### Metadata {: #edit_metadata}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "Metadata"`
![Identifier and name as mandatory fields, plus organisation type, location and description. Metadata tab of an organisation](assets/organisations_edit_tab_metadata_v1_de.png){ class="shadow lightbox" }

In the "Metadata" tab, you maintain the details by which an organisation is recognized in OpenOlat. In addition to the identifier and the name, a location and a description can be entered. OpenOlat only displays the ID and the External ID; they cannot be changed here.
The organisation type (as defined in the "Organisations types" tab) is also assigned here.
If every organisation is linked to a corresponding organisation type on creation, a hierarchical structure can be built. An organisation that belongs to several higher-level organisations at the same time cannot be represented.

On its first start, OpenOlat creates the default organisation. It has the name "OpenOLAT" and the identifier "default-org". Administrators can freely change the name in the "Metadata" tab, for example to the name of their own organisation. The identifier is locked because OpenOlat recognizes the default organisation by it. Courses, learning resources and roles remain assigned unchanged when you rename it. The default organisation cannot be deleted or moved.

!!! note "Note"

    If your OpenOlat synchronizes the organisations with LDAP groups, it assigns each LDAP group the organisation whose identifier, name or External ID matches the name of the group. Upper and lower case do not matter. For this reason, do not choose a name for the default organisation that an LDAP group also has. Otherwise LDAP manages the members of the default organisation.

### User management {: #edit_account_managment}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "User management"`
![Role selection when adding a user in the User management tab](assets/organisations_edit_tab_account_management_v1_de.png){ class="shadow lightbox" }

The "User management" tab shows a list of the users currently assigned to this organisation. Existing users can also be removed again.

The "Add user" button can be used to add further users with a specific role. Select the desired role from the listed roles. In the following dialog, you can search for users. They can be added according to the selection. It is also possible to add several users at once.

Members of various roles can be assigned to each level of the organisation.

The **role assignment** is possible

  * on a specific organisation
  * on a specific organisation and all sub-organisations below this organisation

### Learning resources {: #edit_learning_resources}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "Learning resources"`
!["Add courses" button above the still empty list of assigned courses. Learning resources tab of an organisation](assets/organisations_edit_tab_learning_resources_v1_de.png){ class="shadow lightbox" }

In the "Learning resources" tab, you see which courses are directly assigned to the organisation, and you adjust this assignment. Via "Add courses", a dialog lets you search for further own and available courses to assign to the organisation. To remove courses again, select the rows in the list and click "Remove". OpenOlat asks for confirmation in the dialog "Remove learning resources" before it removes the assignment.

"Add courses" only finds courses. You assign tests, videos and other learning resources to an organisation in the Administrative access of the learning resource, described under [Course settings - Tab Share](../../manual_user/learningresources/Course_Settings_Share.md#section_share). For several learning resources at once, use the [bulk action in Authoring](../../manual_user/area_modules/Authoring_BulkActions.md#bulk_administrative_access).

!!! warning "Warning"

    When you remove a course, OpenOlat does not check whether the course is still assigned to another organisation afterwards. If you want to move a course to another organisation, first click "Add courses" in the new organisation. Only then remove the course from the previous organisation with "Remove".

The **assignment of educational products** is done in the Course Planner, at the respective implementation.

### Line managers [:octicons-tag-16:{ title="from Release 15.3 (OO-4915)" }](https://track.frentix.com/issue/OO-4915){:target="_blank"} {: #edit_linemanager}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "Line managers"`
![Rights checkboxes for the Line manager role in the Line managers tab](assets/organisations_edit_tab_line_management_v1_de.png){ class="shadow lightbox" }

The rights assigned to line managers can be defined separately for each organisation.

### Education managers [:octicons-tag-16:{ title="from Release 20.0 (OO-7839)" }](https://track.frentix.com/issue/OO-7839){:target="_blank"} {: #edit_education_manager}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "Education managers"`
![Rights checkboxes for the Education manager role in the Education managers tab](assets/organisations_edit_tab_education_manager_v1_de.png){ class="shadow lightbox" }

The rights assigned to education managers can be defined separately for each organisation.

### Billing addresses [:octicons-tag-16:{ title="from Release 20.0 (OO-8212)" }](https://track.frentix.com/issue/OO-8212){:target="_blank"} {: #edit_billing_adresses}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "Billing addresses"`
![List of billing addresses with the "Create" button in the Billing addresses tab](assets/organisations_edit_tab_billing_addresses_v1_de.png){ class="shadow lightbox" }

Billing addresses for course and seminar management can be stored here.

### E-mail domains mappings {: #edit_mail_domain}

`Administration > Modules > Organisations > Tab "Organisations structures" > Tab "E-mail domains mappings"`
![List of the e-mail domain mappings in the E-mail domains mappings tab of the organisation](assets/organisations_edit_tab_email_domain_v1_de.png){ class="shadow lightbox" }

An e-mail domain can be specified for each organisation, which is used to check whether users belong to this organisation. This matters when users can self-register for courses, but the courses should only be available for a specific organisation.

[To the top of the page ^](#organisations)

---

## Tab Organisations types {: #tab_types}

![List of the organisation types with reference and name in the Organisations types tab](assets/organisations_tab_types_v1_de.png){ class="shadow lightbox" }

The organisation types define which elements an organisation structure can contain and give these elements a more specific meaning. The types can also map a hierarchical structure, but this is not mandatory. An example of organisation types is `Company --> Division --> Department`.

Further types can be created via "Create organisation type". In addition to the reference and the name, a description can be entered. At this point, a CSS class can be used to define a layout that only applies to this organisation type. In addition, existing types can be subordinated to the new organisation type.

[To the top of the page ^](#organisations)

---

## Tab E-mail domains mappings [:octicons-tag-16:{ title="from Release 20.0 (OO-8178)" }](https://track.frentix.com/issue/OO-8178){:target="_blank"} {: #tab_mail_domain_assignment}

!!! info "Visibility"

    This tab is only displayed if the e-mail domain mapping has been activated in the "Configuration" tab.

![List of the e-mail domains per organisation in the E-mail domains mappings tab](assets/organisations_tab_mail_domains_v1_de.png){ class="shadow lightbox" }

If organisations exist, self-registration can be restricted to specific e-mail domains. New users are then automatically assigned to an organisation based on their e-mail domain and are only allowed to self-register for content/courses of this organisation.

[To the top of the page ^](#organisations)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[Course settings - Tab Share >](../../manual_user/learningresources/Course_Settings_Share.md)<br>
[Authoring - Bulk Actions >](../../manual_user/area_modules/Authoring_BulkActions.md)

**Further reading**<br>
[Assign roles >](../usermanagement/Assign_roles.md)<br>
[Roles and Rights: Which roles are available? >](../../manual_user/basic_concepts/Roles.md)<br>
[Self-registration >](Login_Self-Registration.md)

[To the top of the page ^](#organisations)
