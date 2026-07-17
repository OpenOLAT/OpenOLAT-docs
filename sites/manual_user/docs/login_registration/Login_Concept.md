# Login Concept

Basically, there are 2 login concepts that can be used individually or in combination:

* Local authentication
* External authentication

## Local Authentication

With local authentication, the name and password are stored in OpenOlat (locally).

## External Authentication

With external authentication, the password is NOT stored in OpenOlat, but set and stored in an external tool. OpenOlat asks the external tool if this login name is authorized for access (LDAP, oAuth, Shibboleth).

## Combined local and external authentication

The combination of local and external authentication requires both a password stored in OpenOlat and a query from OpenOlat to an external tool.

* Is the locally stored password okay?
* Does the external tool confirm that the logged in name is authorized to access?

If both factors are met, access is granted.

## Passkey

Passkey is an alternative to passwords. Instead of a password being entered by a person, a key stored in the device is used. (Device-based instead of person-based authentication.)

More details can be found in a [separate section](../login_registration/Passkey.md) here in the manual.

## One Time Code [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509)

The one time code is another method for a second security level at login. After entering their username and password, account holders receive an 8-digit confirmation code by e-mail and complete the login with this code. The one time code can be activated independently of Passkey and, when Passkey is active, serves as a fallback for accounts without a stored passkey.

More details can be found in the [separate section One Time Code](../login_registration/One_Time_Code.md) here in the manual.