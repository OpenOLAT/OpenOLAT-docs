# Password and Authentication

## Tab "Authentication"

![login_password_and_authentication_auth_v2_de.png](assets/login_password_and_authentication_auth_v2_de.png){ class="shadow lightbox" }

<h3>1 Use security levels/passkey</h3>

OpenOlat has a a three-stage security concept:<br>
**Step 1: Password only**<br>
**Step 2: Passkey only**<br>
**Step 3: Passkey + Password**<br>

Switching on activates the option for level 2 and 3 and the other configuration options for administrators are displayed.

<h3>2 Start button for OpenOlat Login</h3>

By switching this on, a **button** is displayed on the login page **instead of the input field** for the user name, with which the input field can be called up.

**Purpose:**<br>
If the primary login method is not the OpenOlat login, then the input field for the OpenOlat login should often not be displayed directly and prominently. An input field has a high prompt character and users immediately enter their (incorrect) login name instead of considering the other login options.<br>
With a button next to other buttons (other login options), the decision for a specific login procedure is more considered.

![login_password_and_authentication_login_v1_de.png](assets/login_password_and_authentication_login_v1_de.png){ class="lightbox" }

<h4>3 One Time Code</h4>

With the "Use one time code" option, you activate an additional second security level by e-mail. [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509) After entering their username and password, account holders receive an 8-digit confirmation code by e-mail and complete the login with this code on a validation page.

Without an active passkey, the one time code is the second security level for all local logins. If Passkey is also activated, the one time code serves as a fallback for account holders without a stored passkey.

A valid e-mail address on the account and a functioning e-mail dispatch configured in OpenOlat are required so that the code can be delivered.

<h4>4 Security level per role</h4>

The levels set here define the **minimum requirement** for the respective role. 

<h4>5 Increase the security level yourself</h4>

With the "Increase security level yourself" option, account holders can decide for themselves whether they want to switch to a higher security level. It is not possible to downgrade below the minimum level set by the administrator.

<h4>6 Expert</h4>

If the security level has been increased by an administrator, the persons concerned will be asked to set up a passkey when they log in. This setting determines how often a user can skip this prompt.

## Tab "Password Syntax"

As the administrator, you define here which criteria a password must fulfill.
A minimum and maximum length must be defined.

![login_password_and_authentication_syntax_v2_de.png](assets/login_password_and_authentication_syntax_v2_de.png){ class="shadow lightbox" }

## Tab "Password change policy"

Here you can define how often users have to change their password and whether a password can be reused. The lifetime of the password can be defined for each role.

![login_password_and_authentication_pw_change_policies_v2_de.png](assets/login_password_and_authentication_pw_change_policies_v2_de.png){ class="shadow lightbox" }


