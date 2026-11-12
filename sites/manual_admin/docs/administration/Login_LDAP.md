# LDAP {: #ldap}

!!! info "frentix customers"
    The integration of LDAP is part of the server configuration. For frentix customers, their customer advisor at frentix takes care of the change.

Many organisations keep the accounts of their staff or students in a directory such as Active Directory. With the LDAP integration, OpenOlat takes over the accounts from this directory and checks username and password against the directory at login. People log in on the login page with the credentials they use in your organisation anyway, and you maintain the accounts in one place.

If LDAP is switched on, system administrators find the page "LDAP administration" in the system administration under:<br>
`Administration > Login > LDAP`


## What the server configuration defines {: #server_configuration}

The server configuration is the configuration file of the installation. This file is maintained by the body that operates OpenOlat. The connection to the directory is there, not in the user interface: which directory server is connected, in which areas of the directory OpenOlat looks for accounts and which details it takes over. In the default configuration, OpenOlat takes over username, e-mail address, first name and last name. Further profile fields can be mapped. On request, OpenOlat also takes over memberships in groups and organisations as well as roles such as author from the directory.

A change to this connection applies only from the next restart. Without LDAP switched on, the entry "LDAP" is missing from the menu `Administration > Login`.

If your OpenOlat matches organisations with LDAP groups, note the hint on the default organisation under [Module Organisations: Metadata](Modules_Organisations.md#edit_metadata).

[To the top of the page ^](#ldap)


## Start synchronization {: #synchronisation}

The synchronization matches the accounts in OpenOlat with the directory: it creates accounts for new people and updates the details taken over. In the default configuration, it runs every hour. If a new person logs in before the next synchronization, OpenOlat creates their account at login.

In the area "Start synchronization", the page shows when the "Last synchronization" ran. With "Start sync" you start it immediately, for example after many people have been added to the directory.

You also take over individual people from the directory in the user management, see [Take over accounts from LDAP or Azure](../usermanagement/Create_User.md#import_external_users).

Administrators see whether a single account logs in via LDAP in the "Authentications" tab of the account:<br>
`User management > "Account of the person" > Tab "Authentications"`<br>
More on this under [Manage user settings](../usermanagement/Configure_User.md).

[To the top of the page ^](#ldap)


## Life cycle user {: #account_lifecycle}

If a person leaves your organisation, they disappear from the directory. In the default configuration, their account in OpenOlat remains until you remove it. For this, you choose one of the two actions in the area "Life cycle user":

- **Deactivate:** The person can no longer log in, the account remains with all data. More on this under [Deactivation and reactivation](Life_cycles_-_Administration/index.md#account_reactivation). [:octicons-tag-16:{ title="from Release 17.1.5 (OO-6649)" }](https://track.frentix.com/issue/OO-6649)
- **Delete account:** OpenOlat deletes the accounts, see [Delete user](../usermanagement/Delete_User.md).

After a click on one of the two actions, a wizard lists the accounts that are missing from the directory. You select the accounts and confirm.

Until you remove an account, the person can continue to log in with the password last used if OpenOlat keeps a copy of the LDAP password (see [Maintenance](#maintenance)).

The server configuration can also define that the synchronization deletes or deactivates such accounts itself. So that a fault in the directory does not affect all accounts, the synchronization then changes nothing if the entry in the directory is missing for half or more of the OpenOlat accounts with LDAP login. This limit is the default value of the server configuration. If it is reached, you remove the accounts by hand in the area "Life cycle user".

[To the top of the page ^](#ldap)


## Maintenance {: #maintenance}

So that people can also log in when the directory server cannot be reached, OpenOlat can keep a copy of the LDAP password at login. If this copy is switched on in the server configuration, the page shows the area "Maintenance". With "Delete cached fallback-authentications" you remove the stored copies. Until a person has logged in successfully via LDAP again and OpenOlat creates the copy anew, OpenOlat checks their login only against the directory. If the directory server fails during this time, they cannot log in.

[To the top of the page ^](#ldap)


## Logging {: #logging}

If a synchronization does not run as expected, you find the cause in the area "Logging". It shows the messages of the LDAP integration continuously, for example the course of a synchronization or accounts that are missing from the directory.

[To the top of the page ^](#ldap)


## Further information {: #further_information}

**Mentioned on this page**<br>
[Module Organisations >](Modules_Organisations.md)<br>
[Create account >](../usermanagement/Create_User.md)<br>
[Manage user settings >](../usermanagement/Configure_User.md)<br>
[Life cycles - Overview >](Life_cycles_-_Administration/index.md)<br>
[Delete user >](../usermanagement/Delete_User.md)

**Further reading**<br>
[Login: Overview >](Login/index.md)<br>
[Cloud login >](Login_Cloud_Login.md)<br>
[Shibboleth >](Login_Shibboleth.md)

[To the top of the page ^](#ldap)
