# Passkey

## What is Passkey?

* Passkey is a digital key. Not a password.
* This key is individually generated for a specific device. It is then either saved in the browser or on the device itself. Thus it is not connected to a person, but to a device.
* If Passkey was created, a password, which could easily be forgotten or stolen, is no longer necessary. So all you need to be able to do is gain access to your device (e.g. with your fingerprint or face id). All further accesses to applications with Passkey are then tested and granted.
* However, Passkey is not a general key for all applications you might want to login to. Each account has its own Passkey.
* When you log in, your device and the requested server contact each other and clarify (based on the Passkey) whether access can be granted. The actual key (private key) does not leave the device. This is why Passkey is considered particularly secure.

## How does Passkey work?

**Step 1:** <br>
A device (e.g. a smartphone or computer) receives a Passkey (private key). The creation of a private key is initiated by OpenOlat, for example. A private key is device-specific and always remains stored on the device (e.g. the smartphone). It never leaves the security chip.

**Step 2:** <br>
The private key is used to create a public key on the smartphone. The public key is mathematically "related" to the private key, but no copy of the private key can be made from it.

**Step 3:** <br>
The user wants to access an application on server X (a website) with his device (e.g. the smartphone on which the private key is stored).

**Step 4:** <br>
The public key is sent to server X.<br>
If another application on another server Y is to be called from the smartphone, the public key must also be sent to this server Y.

**Step 5:**<br>
Server X uses the public key to formulate a question that can only be answered by someone who has the private key. This question is called "Challenge" and is sent from server X to the requesting device (e.g. the smartphone).

**Step 6:**<br>
With the help of the private key, answering the challenge is no problem for the smartphone. The response is sent from the smartphone to the server X that asked the question.

**Step 7:**<br>
The server can now use the public key to check the answer for correctness. But he could never calculate the answer himself. This is only possible with the help of the private key on the smartphone.<br>
If the answer is correct, the server gives the green light: The challenge was answered correctly, access can be granted.

**Passkey with OpenOlat:**<br>
OpenOlat triggers the creation of a private key on the target device and receives a public key from there. (The private key is not created and transmitted outside the target device).

For future logins to OpenOlat from this device, process steps 3-7 will then be performed automatically each time. This simplifies the login a lot, because no password is needed.

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

