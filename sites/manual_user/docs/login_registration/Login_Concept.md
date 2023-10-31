# Login Concept

Basically, there are 2 login concepts that can be used individually or in combination:

* Local authentication
* External authentication

## Local Authentication

With local authentication, the name and password are stored in OpenOlat (locally).

## External Authentication

With external authentication, the password is NOT stored in OpenOlat, but set and stored in an external tool.
OpenOlat asks the external tool if this login name is authorized for access.

## 2-Factor Authentication

The combination of local and external authentication requires both a password stored in OpenOlat and a query from OpenOlat to an external tool.

* Is the locally stored password ok?
* Does the external tool confirm that the logged in name is authorized to access?

If both factors are met, access is granted.

## Passkey

The passkey (private key) is located on the device, so passkey is actually a local authentication method. However, with special features. More details can be found in a [separate section](../login_registration/Passkey.en.md) here in the manual.