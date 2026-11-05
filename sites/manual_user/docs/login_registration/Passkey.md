# Passkey {: #passkey}

## What is Passkey?

* Passkey is a digital key, not a password.
* This key is individually created for a specific device and then saved in the browser or on the device. Thus it is bound to a device, not to a person.
* Once Passkey is created, a password that could be forgotten or stolen is no longer necessary. So all you need is access to your device (e.g. with your fingerprint or face recognition). All further accesses to applications secured with Passkey are then checked and granted by the device.
* However, Passkey is not a general key for all applications you want to log in to. Each account has its own Passkey.
* When you log in, your device and the requested server contact each other and clarify (based on the Passkey) whether access can be granted. The actual key (private key) does not leave the device. This is why Passkey is considered particularly secure.

!!! note "Further information"

    On Passkey and how it works you can find many entries on the internet, e.g.

    * [passkey.org](https://passkey.org)
    * [Wikipedia on Fido/Passkey](https://de.wikipedia.org/wiki/FIDO2#Passkey)
    * [loginwithfido.com](https://loginwithfido.com)


## Activate Passkey [:octicons-tag-16:{ title="from Release 18.1 (OO-7180)" }](https://track.frentix.com/issue/OO-7180) {: #activate}

System administrators switch Passkey on in OpenOlat and thereby define whether Passkey can or must be used.

The users then create the passkey themselves on their devices, in OpenOlat under `Personal Menu > Password`. Administrators do not create passkeys, they can only delete them.

Passkey can be configured role-based and is part of a three-level security concept in OpenOlat:

**Level 1 - Password**<br>
**Level 2 - Passkey**<br>
**Level 3 - Password & Passkey (2FA)**

Details on the [Security Levels](Security_levels.md) page.

If a security level with passkey is configured in OpenOlat, the users are prompted at the next login to create a passkey and to use it for logging in from then on. Depending on the configuration, this step can be skipped a few times; OpenOlat shows how often this is still possible.

If system administrators have additionally activated the one time code, account holders without a stored passkey can still log in with their password and a confirmation code by e-mail. [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509) Details on the [One Time Code](One_Time_Code.md) page.


!!! tip "Tip"

    Level 2 is recommended for certain roles (e.g. user managers and administrators).


## What are Recovery Keys?

If your passkey gets lost, you need a replacement key, a recovery key. It is not a copy of the original key (private key). Recovery keys are one-time passwords that cannot be used a second time.

With level 2 you log in with a passkey only, and your account then has no password. You therefore do not use the link "Forgot password?" to get back into your account, but a recovery key. With level 3 you have a password in addition to the passkey. If your organisation switches passkey off, it helps you back into your account with new login credentials, see [Password](Password.md#reset_password).


## Request new Recovery Keys

You create new recovery keys under `Personal Menu > Password` with the button "Create new recovery key".

!!! note "Note"

    If new recovery keys are created, all old ones are invalid, even if they have never been used.

User managers and administrators can additionally send you a temporary recovery key: in the user management in the tab "Password" with "Send recovery key". OpenOlat sends the key to the stored e-mail address. It is valid for 2 hours and allows a single login.


## Passkey for multiple devices

Proceed as follows:

1. Set up Passkey on the main device<br>
System administrators can require passkeys for specific roles. Users can also increase the security level themselves if system administrators allow it.<br>`Personal Menu > Password`

2. Save the recovery keys<br>(for single use only)

3. If Passkey is activated, OpenOlat requires the creation of a passkey (private key) at the first login. This is device-specific and is only saved on the device.

4. Now change the device and log in on the other device. A message appears there that a passkey is required to log in.

5. Click "Use a recovery key" and log in with a recovery key. This is how you access OpenOlat from the other device.

6. To avoid needing a recovery key every time, go back to `Personal Menu > Password` after logging in on the new device. The button "Create passkey" is available there again.

7. Use the button to create a new passkey. Another private key is created for the current device.

8. The various passkeys/devices are then listed under `Personal Menu > Password`.


## Further information {: #further_information}

**Mentioned on this page**<br>
[passkey.org >](https://passkey.org)<br>
[Wikipedia on Fido/Passkey >](https://de.wikipedia.org/wiki/FIDO2#Passkey)<br>
[loginwithfido.com >](https://loginwithfido.com)<br>
[Security Levels >](Security_levels.md)<br>
[One Time Code >](One_Time_Code.md)<br>
[Password >](Password.md)

**Further reading**<br>
[Personal Configuration: Password >](../personal_menu/Password.md)<br>
[Login Concept >](Login_Concept.md)

[To the top of the page ^](#passkey)
