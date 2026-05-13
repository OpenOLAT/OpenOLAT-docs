# Self-registration  {: #self-registration}

## Tab Configuration {: #tab_configuration}

![login_self_registration_tab1_v1_de.png](assets/login_self_registration_tab1_v1_de.png){ class="shadow lightbox" }


### Section "Configuration"

The toggle button basically allows self-registration.


### Section "Self registration"

**Show on login page**<br>
The option for self-registration can already be offered on the login page.
If the option is not displayed there, self-registration can be carried out, for example, after selecting a corresponding offer in the catalog.


**Step Account verification**<br>
In an optional step, starting with :octicons-tag-24: Release 20, it is possible to check whether users already have an OpenOlat account. Users who already have an account should be able to continue using their old account if they wish. 
If administrators select the verification option, users who are already known will be asked for an existing account and a support form will be provided.

**Step E-Mail Validation**<br>
E-mail addresses entered during self-registration are checked for validity.


### Section "Restriction to domain"
The domains are defined in the organization module.<br>
See [Module Organizationen >](../administration/Modules_Organisations.md)


### Section "Validity period of login data"
The validity period of the login data can be specified separately for the GUI and the REST API.


[To the top of the page ^](#self-registration)

---

## Tab Account settings {: #tab_account_settings}

![login_self_registration_tab2_v1_de.png](assets/login_self_registration_tab2_v1_de.png){ class="shadow lightbox" }


### Section "Account Configuration"

The configurations entered here will be applied to new accounts:

**Users' home organization:**<br>
New users are automatically assigned to the organization specified here. Further assignments can be made later in user management.

**Account status:**<br>
**Active:** After self-registration, OpenOlat is immediately available.<br>
**Pending:** An administrator or user manager must activate the account after self-registration.
**Pending if one of the following account attributes applies:**  If one of the conditions applies, the account is created with the status "Pending." If none of the conditions apply, the account status "Active" is assigned.

**Email for outstanding accounts:**
The email address of a responsible person (preferably an administrator or user administrator) can be specified for checking and activating accounts with "pending" status.

**Book courses**<br>
If this option is enabled, people who register themselves can automatically be made members of the specified courses. 

**Course list:**<br>
The option to specify multiple courses refers to the "Book courses" option.

**Account expiration in days**<br>
The information provided here corresponds to the information in user management. The information is transferred there during self-registration.

### Section "Account attributes"
After self-registration, a default value can optionally be assigned to an account attribute. This can be used to easily identify self-registered users and thus distinguish them from LDAP users, for example.

[To the top of the page ^](#self-registration)

---

## Tab external integration {: #tab_configuration}

![login_self_registration_tab3_v1_de.png](assets/login_self_registration_tab3_v1_de.png){ class="shadow lightbox" }

### Section "External integration"

**Code for the registration**<br>

The call for self-registration can be accessed directly using the URL provided here.

Use case:<br>
If you do not want the "Self-registration" option to be displayed on the start page, potential users can be invited to self-register using the URL provided here.

[To the top of the page ^](#self-registration)




