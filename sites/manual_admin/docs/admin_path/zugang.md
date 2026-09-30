---
title: Access
description: Who may enter. Here you decide who reaches your installation and how people log in.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-nav" aria-label="Navigation: The path to a running installation" markdown="1">

<span class="oo-mh-nav__label">Navigation: The path to a running installation</span>
[‹ Menu: Set up](einrichten.md){ .oo-mh-btn .oo-mh-btn--prev }
[Menu: Roles ›](rollen.md){ .oo-mh-btn .oo-mh-btn--next }

</nav>

# Access {: #zugang}

<p class="oo-mh-sub">Who may enter</p>

Here you decide who reaches your installation and how people log in. Authentication defines the login methods, self-registration opens the instance for new accounts, and guests only see what is explicitly released for guests. The one time code adds a second factor to the password.

## Terms of this station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Area</p>

### Login {: #platform_admin_login}

The Administration section for sign-in and access: password and authentication, self-registration, guests and external people, security, cloud login, LDAP, Shibboleth and passkey.

??? note "Login in detail"

    The Administration section for sign-in and access: password and authentication, self-registration, guests and external people, security, cloud login, LDAP, Shibboleth and passkey.

    **German:** Login

    [Read in the manual](../administration/Login.md) · [Ask Sophia](?sophia=What%20is%20%22Login%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Concept</p>

### Authentication {: #platform_authentication}

The proof that a person is who they claim to be.

??? note "Authentication in detail"

    The proof that a person is who they claim to be. OpenOlat supports several methods side by side, and one account can carry several of them.

    **German:** Authentifizierung

    [Read in the manual](../../manual_user/login_registration/Login_Concept.md) · [Ask Sophia](?sophia=What%20is%20%22Authentication%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### Self-registration {: #platform_self_registration}

The module a person uses to create an account themselves on the login page, without user management creating it.

??? note "Self-registration in detail"

    The module a person uses to create an account themselves on the login page, without user management creating it. The administration sets the home organisation, the permitted e-mail domains, the mandatory fields and whether the account is active at once or pending.

    **German:** Selbstregistrierung

    **What users call it:** registration, sign up, create account

    [Read in the manual](../administration/Login_Self-Registration.md) · [Ask Sophia](?sophia=What%20is%20%22Self-registration%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Concept</p>

### Guest access {: #platform_guest_access}

Access to OpenOlat without an account through the Guest access link on the login page.

??? note "Guest access in detail"

    Access to OpenOlat without an account through the Guest access link on the login page. Guests only see resources explicitly released for guests, and only in conventional courses.

    **German:** Gastzugang

    **What users call it:** as guest, anonymous access, without login

    **Not to be confused with [Guest](../../manual_user/basic_concepts/guest_access.md):** Guest is the access role of the person; guest access is the feature the administration switches on or off.

    [Read in the manual](../../manual_user/basic_concepts/guest_access.md) · [Ask Sophia](?sophia=What%20is%20%22Guest%20access%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

<p class="oo-mh-partof">Includes:</p>

??? note "Guest in detail"

    Access without signing in, with read access to the resources explicitly released for guests. Guests have no account, do not become members and leave no assessment behind.

    **German:** Gast

    **Not to be confused with [Guest access](../../manual_user/basic_concepts/guest_access.md):** Guest is the access role of the person; guest access is the feature the administration switches on or off.

    [Read in the manual](../../manual_user/basic_concepts/guest_access.md) · [Ask Sophia](?sophia=What%20is%20%22Guest%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Concept</p>

### One time code {: #platform_one_time_code}

An eight-digit confirmation code OpenOlat sends by e-mail after the username and password have been entered.

??? note "One time code in detail"

    An eight-digit confirmation code OpenOlat sends by e-mail after the username and password have been entered. It is the second factor for accounts without a passkey and is switched off by default.

    **German:** One Time Code

    **What users call it:** one-time password, OTP, e-mail code

    **Not to be confused with [Passkey](../../manual_user/login_registration/Passkey.md):** The one time code arrives by e-mail and needs no device; the passkey is bound to a device or a security key.

    [Read in the manual](../../manual_user/login_registration/One_Time_Code.md) · [Ask Sophia](?sophia=What%20is%20%22One%20time%20code%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

</div>

!!! info "Not to be confused: Guest access and Guest"

    Guest is the access role of the person; guest access is the feature the administration switches on or off.

## Read up {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Read up</p>

[Login](../administration/Login.md)

frentix accompanies you in the setup with support and coaching: [support@frentix.com](mailto:support@frentix.com)

</div>

</div>

## Deepen once the installation is running {: #deepen}

The installation is running. Now the things that did not matter while setting up pay off: the terms of this station have parts and settings that control the installation more precisely.

- **Login:** [Security](../administration/Login_Security.md).
- **Authentication:** [Local OpenOlat authentication](../../manual_user/login_registration/Login_Concept.md), Login for administrators, [Cloud login](../administration/Login.md), [Passkey](../../manual_user/login_registration/Passkey.md) and more.
- **Self-registration:** [Registration](../../manual_user/login_registration/index.md). More on the page [Self-registration](../administration/Login_Self-Registration.md).

## Further information {: #further_information}

**Mentioned on this page**<br>
[Login: Overview >](../administration/Login.md)<br>
[Login Concept >](../../manual_user/login_registration/Login_Concept.md)<br>
[Self-registration >](../administration/Login_Self-Registration.md)<br>
[Roles and Rights: Guest access >](../../manual_user/basic_concepts/guest_access.md)<br>
[Passkey >](../../manual_user/login_registration/Passkey.md)<br>
[One Time Code >](../../manual_user/login_registration/One_Time_Code.md)<br>
[Security >](../administration/Login_Security.md)<br>
[Login and Registration >](../../manual_user/login_registration/index.md)

**Further reading**<br>
[Password and Authentication >](../administration/Login_Password_and_Authentication.md)<br>
[Anonymous guests and external users >](../administration/Guest_and_invitation.md)<br>
[Glossary >](../../reference_glossary/glossary.md)

[To the top of the page ^](#zugang)
