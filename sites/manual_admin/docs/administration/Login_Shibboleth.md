# Shibboleth {: #shibboleth}

!!! info "frentix customers"
    The integration of Shibboleth is part of the server configuration. For frentix customers, their customer advisor at frentix takes care of the change.

Universities that belong to a Shibboleth federation check the login of their members themselves. A federation is an association of universities that recognise these logins mutually, for example the federation of SWITCH in Switzerland. With Shibboleth, these people log in to OpenOlat with the account of their home university. OpenOlat receives no password, only the attributes that the university releases, for example name, e-mail address and field of study. You manage no passwords in OpenOlat, and new members of the university receive their account at the first login.

If Shibboleth is switched on, system administrators find the page in the system administration under:<br>
`Administration > Login > Shibboleth`


## What the server configuration defines {: #server_configuration}

The server configuration is the configuration file of the installation. This file is maintained by the body that operates OpenOlat. The basic configuration is there: the connection to the federation, which attributes OpenOlat takes over into which profile fields and to which organisation new accounts are assigned. The page in the administration only holds the optional authorization rules.

A change to the basic configuration applies only from the next restart. Without Shibboleth switched on, the entry "Shibboleth" is missing from the menu `Administration > Login`.

Depending on the server configuration, the login page shows a selection of the university via the selection service of SWITCH for Shibboleth, or a simple login form that forwards to the login at the university. The page in the administration is the same in both cases.

[To the top of the page ^](#shibboleth)


## First login {: #first_login}

When a person logs in via Shibboleth for the first time, OpenOlat guides them through a registration and creates their account. At every further login, OpenOlat matches the profile with the released attributes. If the account is inactive, OpenOlat reactivates it automatically at login, see [Deactivation and reactivation](Life_cycles_-_Administration/index.md#account_reactivation). [:octicons-tag-16:{ title="from Release 15.2.8 (OO-5045)" }](https://track.frentix.com/issue/OO-5045)

Administrators see whether a single account logs in via Shibboleth in the "Authentications" tab of the account:<br>
`User management > "Account of the person" > Tab "Authentications"`<br>
More on this under [Manage user settings](../usermanagement/Configure_User.md).

[To the top of the page ^](#shibboleth)


## Attribute access control [:octicons-tag-16:{ title="from Release 10.3.3 (OO-1588)" }](https://track.frentix.com/issue/OO-1588) {: #attribute_access_control}

Not every person who can log in at their university should use OpenOlat. With "Activate attribute access control", you only let in people whose attributes carry an allowed value, for example only members of a certain university or field of study.

You define up to two attributes:

- **Shibboleth attribute 1:** the name of the attribute that OpenOlat checks, as the university delivers it to OpenOlat. The names are known to whoever connected Shibboleth in the server configuration.
- **Allowed values for attribute 1:** the allowed values, separated by line break, comma or semicolon. Upper and lower case do not matter.
- **Shibboleth attribute 2** and **Allowed values for attribute 2:** a second attribute with its values, following the same pattern.

A person gets access if one of the two attributes carries one of the allowed values. To everyone else, OpenOlat shows the message "You are not authorized to log in OpenOlat."

[To the top of the page ^](#shibboleth)


## Direct link for SSO access [:octicons-tag-16:{ title="from Release 10.3.4 (OO-1651)" }](https://track.frentix.com/issue/OO-1651) {: #direct_link}

If the login via Shibboleth should start directly from the website of your university, place the "Direct link for SSO access" there. SSO (single sign-on) means: the person logs in once at their university and is thereby also logged in to OpenOlat. The page shows this address. It leads to the login via Shibboleth without a detour via the login page of OpenOlat.

[To the top of the page ^](#shibboleth)


## Shibboleth and Switch edu-ID {: #switch_eduid}

Switch edu-ID is a personal account at SWITCH that stays with a person even after a change of university. With Shibboleth, by contrast, the person logs in with the account of their university. You connect Switch edu-ID as a cloud login, not via Shibboleth, see [Cloud login: Switch edu-ID](Login_Cloud_Login.md#switch_eduid). Shibboleth and Switch edu-ID can be switched on side by side.

[To the top of the page ^](#shibboleth)


## Further information {: #further_information}

**Mentioned on this page**<br>
[Life cycles - Overview >](Life_cycles_-_Administration/index.md)<br>
[Manage user settings >](../usermanagement/Configure_User.md)<br>
[Cloud login >](Login_Cloud_Login.md)

**Further reading**<br>
[Login: Overview >](Login/index.md)<br>
[LDAP >](Login_LDAP.md)<br>
[Login Page >](../../manual_user/login_registration/Login_Page.md)

[To the top of the page ^](#shibboleth)
