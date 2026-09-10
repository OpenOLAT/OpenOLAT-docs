# Module Organisations {: #organisations}

The "Organizations" module is optionally available in OpenOlat. It is activated in the system administration under `Administration > Modules > Organizations`.

!!! tip "Activation"

    Customers of frentix please contact [contact@frentix.com](mailto:contact@frentix.com) for the activation. After activation, various additional settings can be made for the system-wide configuration. For systems with the fx-Release, these adjustments are made by frentix.

    **Not a frentix hosting customer?** Please ask your system operator!

## Tab Configuration {: #tab_configuration}

![Activation of the Organizations module, the e-mail domain mapping and the legal documents folder in the Configuration tab](assets/organisations_tab_config_v2_de.png){ class="shadow lightbox" }

In the Configuration tab

* the Organization structures module is activated
* the e-mail domain mapping is activated (can only be activated if the Organizations module is activated)
* the folder for legal documents is activated
* the "Status" section, which shows information for administrators

The company structure can be mapped in the "Organizations" module. Roles, rights and the visibility of courses and content can then be made dependent on membership of a specific organizational unit.

The ability of course participants to self-register can also be made dependent on membership of a specific organizational unit. This restriction is set up by comparing the e-mail address of new users against the stored e-mail domains and automatically assigning them to a specific organizational unit.

[To the top of the page ^](#organisations)

---

## Tab Organization structure {: #tab_structure}

The "Organization structure" tab shows the organizations already created, together with their sub-organizations, as a tree structure.

### Creating and editing organizations {: #create_and_edit}

![Organization tree with sub-organizations in the Organization structure tab](assets/organisations_tab_structure_v2_de.png){ class="shadow lightbox" }

New organizations can be added using the "Create new organization" button at the top right, or for existing organizations by clicking the three dots and "Create sub-organization". It is also possible to move the element within the organization tree or to create a new sub-organization directly.

If an organizational element is selected in the tree structure, the metadata of the organizational element and other assignments can be adjusted or supplemented.

![Legal documents folder in the "Legal documents" tab of an organizational element](assets/organisations_tab_structure_legal_documents_v1_de.png){ class="shadow lightbox" }

**Tab Organization structure > tab "Legal documents"**<br>
If the folder has been activated under `Administration > Modules > Organizations > Tab "Configuration"`, this tab is displayed for administrators and other administrative roles. Administrators can store documents on organization-specific matters in it. Other administrative roles only have read access.

### Metadata {: #edit_metadata}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "Metadata"`
![Metadata of an organizational element: designation, name, organization type, location and description](assets/organisations_edit_tab_metadata_v1_de.png){ class="shadow lightbox" }

In addition to the designation and the name, a description for the element can be entered.
The organization type (as defined in the "Organization types" tab) is also assigned here.
If every organizational element is linked to a corresponding organization type on creation, a hierarchical structure can be built. This makes it possible to map process and functional organizations, but a matrix organization cannot be represented.

### Account management {: #edit_account_managment}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "Account management"`
![Role selection when adding an account in the Account management tab](assets/organisations_edit_tab_account_management_v1_de.png){ class="shadow lightbox" }

The "Account management" tab shows a list of the users currently assigned to this organizational unit. Existing users can also be removed again.

The "Add account" button can be used to add further users with a specific role. Select the desired role from the listed roles. In the following dialog, you can search for users. They can be added according to the selection. It is also possible to add several users at once.

Members of various roles can be assigned to each level of the organization.

The **role assignment** is possible

  * on a specific organization
  * on a specific organization and all organization structures subordinate to this organization

### Learning resources {: #edit_learning_resources}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "Learning resources"`
![List of the assigned courses with the button "Add courses" in the Learning resources tab](assets/organisations_edit_tab_learning_resources_v1_de.png){ class="shadow lightbox" }

The "Learning resources" tab shows the courses directly assigned to the organizational element. These can also be removed again here. Via "Add courses", a dialog lets you search for further own and available courses to assign to the organizational element.

The **assignment of curricula** is done in the Course Planner, at the respective implementation.

### Line manager {: #edit_linemanager}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "Line manager"`
![Rights checkboxes for the Line manager role in the Line manager tab](assets/organisations_edit_tab_line_management_v1_de.png){ class="shadow lightbox" }

The rights assigned to line managers can be defined separately for each organizational unit.

### Education manager {: #edit_education_manager}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "Education manager"`
![Rights checkboxes for the Education manager role in the Education manager tab](assets/organisations_edit_tab_education_manager_v1_de.png){ class="shadow lightbox" }

The rights assigned to education managers can be defined separately for each organizational unit.

### Billing addresses {: #edit_billing_adresses}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "Billing addresses"`
![List of billing addresses with the "Create" button in the Billing addresses tab](assets/organisations_edit_tab_billing_addresses_v1_de.png){ class="shadow lightbox" }

Billing addresses for course and seminar management can be stored here.

### E-mail domain mapping {: #edit_mail_domain}

`Administration > Modules > Organizations > Tab "Organization structure" > Tab "E-mail domain mapping"`
![List of the e-mail domain mappings in the tab of the same name of the organizational element](assets/organisations_edit_tab_email_domain_v1_de.png){ class="shadow lightbox" }

An e-mail domain can be specified for each organizational element, which is used to check whether users belong to this organizational unit. This matters when users can self-register for courses, but the courses should only be available for a specific organizational unit.

[To the top of the page ^](#organisations)

---

## Tab Organization types {: #tab_types}

![List of the organization types with designation and name in the Organization types tab](assets/organisations_tab_types_v1_de.png){ class="shadow lightbox" }

The organization types define which elements an organization structure can contain and give these elements a more specific meaning. The types can also map a hierarchical structure, but this is not mandatory. An example of organization types is `Company --> Division --> Department`.

Further types can be created via "Create organization type". In addition to the designation (identifier) and the name, a description can be entered. At this point, a CSS class can be used to define a layout that only applies to this organization type. In addition, existing types can be subordinated to the new organization type.

[To the top of the page ^](#organisations)

---

## Tab E-mail domain mappings {: #tab_mail_domain_assignment}

!!! info "Visibility"

    This tab is only displayed if the e-mail domain mapping has been activated in the "Configuration" tab.

![List of the e-mail domains per organization in the E-mail domain mappings tab](assets/organisations_tab_mail_domains_v1_de.png){ class="shadow lightbox" }

If organizational units exist, self-registration can be restricted to specific e-mail domains. New users are then automatically assigned to an organizational unit based on their e-mail domain and are only allowed to self-register for content/courses of this organizational unit.

[To the top of the page ^](#organisations)
