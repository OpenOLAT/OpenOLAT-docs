# Login Concept {: #login_concept}

Basically, there are two login concepts that can be used individually or in combination:

* Local authentication
* External authentication


## Local Authentication

With local authentication, OpenOlat stores username and password itself (locally).

## External Authentication

With external authentication, another system manages the password and checks the login. OpenOlat receives the confirmation from this system that the person is authorized for access. OpenOlat knows three such procedures:

- **Cloud login:** An identity provider such as Microsoft, Google or Switch edu-ID takes over the login. The procedure is based on OAuth 2.0 and OpenID Connect.
- **LDAP:** The login runs via the directory of your organisation, for example Active Directory.
- **Shibboleth:** You log in at your university.

Which procedures your organisation offers is defined by the system administrators. How they set up the procedures is described in the administration manual under [Login: Overview](../../manual_admin/administration/Login/index.md#login_methods).

## Combining several login procedures {: #combined_login_methods}

Your organisation can switch on several login procedures at the same time, so that each group of people logs in their own way. Each person chooses one of these procedures when logging in, a single one is enough. An example: employees log in via "Microsoft Azure AD" with the account they also use for the other services of the organisation. External people without such an account log in with their OpenOlat password, that is via local authentication.

The login page shows each procedure that is switched on in its own area, separated by "or". The identity providers of the cloud login are listed together under "Please select your identity provider.", each with its own button. For the OpenOlat password and for LDAP, people enter username and password in the same form. People from the LDAP directory use the password of their organisation there.

System administrators can switch on the option "Automatic redirect (local login via /maintenance/)" for one identity provider. Whoever calls OpenOlat then lands immediately at the login of this identity provider. People reach the login page with the other procedures only via the address of OpenOlat with the addition `/maintenance/`, for example `https://your.openolat.domain/maintenance/`. The redirect therefore suits organisations in which all people log in via the same identity provider.

How system administrators switch on the procedures is described in the administration manual under [Login: Overview](../../manual_admin/administration/Login/index.md#login_methods). The automatic redirect and the assignment at the first login via an identity provider, also for people without an account, are described on the page [Cloud login](../../manual_admin/administration/Login_Cloud_Login.md#automatic_redirect).

An additional proof after the password in the same login (second factor), for example a passkey or a one time code, is described on the page [Security Levels](../login_registration/Security_levels.md).

## Passkey [:octicons-tag-16:{ title="from Release 18.1 (OO-7180)" }](https://track.frentix.com/issue/OO-7180)

Passkey is an alternative to passwords. Instead of a password being entered by a person, a key stored in the device is used. The key is bound to the device, the person does not have to remember a password.

More details can be found in a [separate section](../login_registration/Passkey.md) here in the manual.

## One Time Code [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509)

The one time code is another method for a second security level at login. After entering their username and password, account holders receive an 8-digit confirmation code by e-mail and complete the login with this code. The one time code can be activated independently of Passkey and, when Passkey is active, serves as a fallback for accounts without a stored passkey.

More details can be found in the [separate section One Time Code](../login_registration/One_Time_Code.md) here in the manual.

## Further information {: #further_information}

[Login: Overview >](../../manual_admin/administration/Login/index.md)<br>
[Cloud login >](../../manual_admin/administration/Login_Cloud_Login.md)<br>
[Security Levels >](../login_registration/Security_levels.md)<br>
[Passkey >](../login_registration/Passkey.md)<br>
[One Time Code >](../login_registration/One_Time_Code.md)<br>
[Login Page >](../login_registration/Login_Page.md)

[To the top of the page ^](#login_concept)
