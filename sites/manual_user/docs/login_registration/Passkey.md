# Passkey {: #passkey}

## What is Passkey?

* Passkey is a digital key, not a password.
* This key is individually created for a specific device and then saved in the browser or on the device. Thus it is bound to a device, not to a person.
* Once Passkey is created, a password that could be forgotten or stolen is no longer necessary. So all you need is access to your device (e.g. with your fingerprint or face recognition). All further accesses to applications secured with Passkey are then checked and granted by the device.
* However, Passkey is not a general key for all applications you want to log in to. Each account has its own Passkey.
* When you log in, your device and the requested server contact each other and clarify (based on the Passkey) whether access can be granted. The actual key (private key) does not leave the device. This is why Passkey is considered particularly secure.

!!! info "Further information"

    On Passkey and how it works you can find many entries on the internet, e.g.

    * [passkey.org](https://passkey.org)
    * [Wikipedia on Fido/Passkey](https://de.wikipedia.org/wiki/FIDO2#Passkey)
    * [loginwithfido.com](https://loginwithfido.com)


## Activate Passkey {: #activate}

The activation of Passkey in OpenOlat is done by the administrators. The activation determines whether Passkey can or must be used.

However, the **creation** of the passkey is then done by the users on their respective devices, in OpenOlat under `Personal Menu > Password`. Administrators can only remove passkeys.

Passkey can be configured role-based and is part of a three-level security concept in OpenOlat:

**Level 1: password only**<br>
**Level 2: passkey only**<br>
**Level 3: passkey + password** (2-factor authentication)<br>

Details on the [Security Levels](Security_levels.md) page.

If a security level with passkey is configured in OpenOlat, the users are prompted at the next login to create a passkey and to use it for logging in from then on. Depending on the configuration, this step can be skipped a few times; OpenOlat shows how often this is still possible.

If the administration has additionally activated the one time code, account holders without a stored passkey can still log in with their password and a confirmation code by e-mail. [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509) Details on the [One Time Code](One_Time_Code.md) page.


!!! note "Note"

    Level 2 is recommended for certain roles (e.g. user managers and administrators).


## What are Recovery Keys?

If there is no password any more, it can no longer be reset by administrators. If Passkey is activated in OpenOlat as the sole authentication method, passwords can no longer be assigned. (With 2-factor authentication, however, they can, in addition to Passkey.)

If the key is lost nevertheless, a replacement key is needed. With Passkey, however, the replacement key is not a copy of the original key (private key). Recovery keys are one-time passwords that cannot be used a second time.


## Request new Recovery Keys

You create new recovery keys under `Personal Menu > Password` with the button "Create new recovery key".

!!! note "Note"

    If new recovery keys are created, all old ones are invalid, even if they have never been used.

User managers and administrators can additionally send you a temporary recovery key: in the user management in the tab "Password" with "Send recovery key". OpenOlat sends the key to the stored e-mail address. It is valid for 2 hours and allows a single login.


## Passkey for multiple devices

Proceed as follows:

1. Set up Passkey on the main device<br>
Administrators can require passkeys for specific roles. Users can also increase the security level themselves if the administration allows it.<br>`Personal Menu > Password`

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
[One Time Code >](One_Time_Code.md)

**Further reading**<br>
[Password >](Password.md)<br>
[Personal Configuration: Password >](../personal_menu/Password.md)<br>
[Login Concept >](Login_Concept.md)

[To the top of the page ^](#passkey)
