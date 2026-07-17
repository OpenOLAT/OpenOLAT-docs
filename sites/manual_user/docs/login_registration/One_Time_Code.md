# One Time Code {: #one_time_code}

If, when you log in, an additional step "Login - Validation" appears after your username and password, your organisation has activated the one time code as a second factor. OpenOlat then sends you a confirmation code by e-mail, which you enter to complete the login. This page explains what a one time code is and how logging in with it works.

## What is a one time code? [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509) {: #about}

A one time code is an 8-digit confirmation code that OpenOlat sends you by e-mail during login. It serves as a second factor (two-factor authentication) in addition to your password and is valid only for the current login.

A valid e-mail address must be stored on your account, otherwise the code cannot be delivered.

[Back to top ^](#one_time_code)

---

## How to log in with a one time code {: #login}

1. Enter your username and password as usual.
2. OpenOlat shows the step "Login - Validation" and sends you an e-mail with the subject "Validation code for \<instance name\> Login".
3. Open the e-mail and copy the 8-digit code into the "Confirmation code" field.
4. Click "Login" to complete the sign-in.

If the code is wrong, the message "Validation code (OTP) is not valid" appears and you can enter the code again.

[Back to top ^](#one_time_code)

---

## I did not receive a code {: #no_code}

On the validation page, click "Resend the email". OpenOlat generates a new code and sends it to the stored e-mail address. All previously sent codes then become invalid. Check your spam folder as well. If no e-mail address is stored on your account or the code repeatedly fails to arrive, contact your support.

[Back to top ^](#one_time_code)

---

## Relationship to Passkey {: #passkey}

One time code and [Passkey](Passkey.md) do not exclude each other:

* If only the one time code is activated, you log in with your password and a code sent by e-mail.
* If Passkey is also activated and you have a passkey stored, the passkey acts as the second factor. The one time code then serves as a fallback in case no passkey is available yet.

Whether and which methods are active is determined by the administration.

[Back to top ^](#one_time_code)

---

## Further information {: #further_information}

[Login Concept >](Login_Concept.md)<br>
[Passkey >](Passkey.md)<br>
[Login Page >](Login_Page.md)<br>

[Back to top ^](#one_time_code)
