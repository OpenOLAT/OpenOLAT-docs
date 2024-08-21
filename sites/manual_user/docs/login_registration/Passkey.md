# Passkey

## What is Passkey?

* Passkey is a digital key. Not a password.
* This key is individually generated for a specific device. It is then either saved in the browser or on the device itself. Thus it is not connected to a person, but to a device.
* If Passkey was created, a password, which could easily be forgotten or stolen, is no longer necessary. So all you need to be able to do is gain access to your device (e.g. with your fingerprint or face id). All further accesses to applications with Passkey are then tested and granted.
* However, Passkey is not a general key for all applications you might want to login to. Each account has its own Passkey.
* When you log in, your device and the requested server contact each other and clarify (based on the Passkey) whether access can be granted. The actual key (private key) does not leave the device. This is why Passkey is considered particularly secure.

!!! info "Further information"

    On passkey and how it works you can find a lot of information in the internet, e.g.
    
    * [passkey.org](https://passkey.org)
    * [Wikipedia on Fido/Passkey](https://de.wikipedia.org/wiki/FIDO2#Passkey)
    * [loginwithfido.com](https://loginwithfido.com)


## Activate Passkey {: #activate}

The activation of Passkey in OpenOlat is done by the administrator. Activation determines that the passkey can or must be used.

However, the creation of the passkey is then done by the user(s) on the respective devices. (In OpenOlat in the **personal menu** at **"password"**.) Administrators can only remove passkeys.

Passkey can be configured on a role-based basis and is part of a three-tier security concept in OpenOlat:

**Step 1: only Password**<br>
**Step 2: only Passkey**<br>
**Step 3: Passkey + Password**  (2-factor authentication)<br>

If a security level with passkey has been configured in OpenOlat, then the users will be prompted to create a passkey the next time they log in and to use this passkey for logging in in the future.

!!! note "Note"

    Level 2 is recommended for certain roles (e.g. user administrators and administrators).

## What are Recovery Keys?

If there is no password, it cannot be reset by the administrator. If Passkey has been activated as the sole authentication method in OpenOlat, passwords can no longer be assigned. (With 2-factor authentication, however, it does, in addition to Passkey).

If the key is lost nevertheless once, it needs a spare key. With Passkey, however, the replacement key is not a copy of the original key (private key). Recovery keys are one-time passwords that cannot be used a second time.

## Request new Recovery Keys

The recovery keys can be requested **in the personal menu** under **"Password"**.

!!! note "Note"

    If new recovery keys have been ordered, all old ones are invalid, even if they have never been used.


## Passkey for multiple devices

Proceed as follows:

1. Setting up Passkey on the main device<br>
The administrator can request role-specific passkeys, but other users can also increase the security level themselves if necessary.<br> (Personal menu > Password)

2. Save recovery keys<br>(for single use only)

3. If Passkey has been activated, you will be asked to create a passkey (private key) the first time you log in. This is device-specific and is only saved on the device.

4. Now change the device and log in on the other device. This triggers a message there: "A passkey is required to log in" or similar.

5. Now log in with a recovery key. This will allow you to access OpenOlat from the other device.

6. To avoid needing a recovery key every time, go back to the personal menu after logging in on the new device and go to "Password". The "Create passkey" button is available there again.

7. Use the button to create a new passkey. Another private key is created for the current device.

8. The various passkeys/devices are then listed in the personal menu under "Password".




