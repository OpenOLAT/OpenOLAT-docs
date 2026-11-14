# Cloud login {: #cloud_login}

Many organisations already keep the accounts of their people with an identity provider, for example in Microsoft 365, at Google or in their own Keycloak. With the cloud login, these people log in to OpenOlat with their existing account and need no OpenOlat password of their own. The identity provider checks username and password, OpenOlat only receives the confirmation and the details about the person that the identity provider releases.

System administrators set up the integrations in the system administration under:<br>
`Administration > Login > Cloud login`

The page is always in the menu, it requires no server configuration.


## Add authentication service [:octicons-tag-16:{ title="from Release 10.1 (OO-729)" }](https://track.frentix.com/issue/OO-729) {: #add_provider}

For the common identity providers, OpenOlat comes with ready-made integrations. You select the identity provider and enter the credentials it issues for OpenOlat.

The menu "More actions" with the three-dot icon at the top right of the page lists the ready-made integrations that are not yet added: Google, Facebook, LinkedIn, X (Twitter), Active Directory Federation Services, Microsoft Azure Active Directory, Keycloak, Switch edu-ID and Datenlotsen. If you select an entry, a section for this identity provider appears on the page. The menu no longer lists identity providers that are added.

![In the menu More actions you choose the identity provider to add, below it the two ways for your own OAuth 2.0 provider](assets/login_cloud_login_add_provider_menu_v1_en.png){ class="shadow lightbox" title="Menu More actions on the Cloud login page · 2026.11.12" }

How to connect an identity provider:

1. Register OpenOlat as an application with the identity provider. As the return address, enter the "Redirect URI" there that OpenOlat shows in the section "Login via OAuth, cloud services and social providers" directly below the menu "More actions".
2. Select the identity provider in the menu "More actions".
3. In the section of the identity provider, enter the credentials it has issued for OpenOlat, for example "Client ID" and "Client secret". With these two details, OpenOlat identifies itself to the identity provider.
4. Click "Save".

From then on, the login page offers the identity provider for selection. With "Remove" in the section of the identity provider and a confirmation, you take the integration away again.

### Active Directory Federation Services {: #adfs}

For the login with a Microsoft account of the organisation, OpenOlat comes with two integrations. Which one fits depends on where your organisation keeps the accounts:

- **Microsoft Azure Active Directory:** The accounts are in the cloud service of Microsoft that organisations with Microsoft 365 use. The next section describes the setup.
- **Active Directory Federation Services:** The organisation runs the login service itself, on its own Windows servers.

In the section "Active Directory Federation Services", enter the address of the login service of your organisation in the field "OAuth2 endpoint (oAuthEndpoint)", for example `https://adfs.openolat.org/adfs/oauth2`, plus "Client ID" and "Client secret". According to the hint in the form, the "Client secret" is only needed for ADFS 2016. Which version is in use and which values apply is known to the unit that runs the login service of your organisation.

According to the [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview), as of November 2026, AD FS (Active Directory Federation Services) is part of Windows Server, and Microsoft recommends moving to the cloud service Microsoft Entra ID, formerly Azure Active Directory. At AD FS, the addresses for the login via [OAuth 2.0](#authorization_code_flow) are under the path `/adfs/oauth2/` ([Microsoft: OIDC authentication with AD FS](https://learn.microsoft.com/en-us/SharePoint/security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-adfs)). "Client ID" and "Client secret" are created at AD FS when OpenOlat is registered there as a client; according to [Microsoft](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adfsod/7fc51569-b46d-4aba-8ae6-bad19cb9951b), AD FS only admits registered clients.

### Microsoft Azure Active Directory [:octicons-tag-16:{ title="from Release 15.3 (OO-4904)" }](https://track.frentix.com/issue/OO-4904) {: #azure}

If your organisation works with Microsoft 365, your staff log in with their Microsoft account. For this, you add "Microsoft Azure Active Directory". Microsoft has renamed this service to Microsoft Entra ID, and you find it under this name at Microsoft. On the login page, the entry is called "Microsoft Azure AD".

In the section "Microsoft Azure Active Directory", you enter three details that Microsoft issues for OpenOlat: "Client ID", "Client secret" and "Directory (tenant) ID", the identifier of the Microsoft 365 environment of your organisation. For this, you first register OpenOlat as an app at Microsoft. Then you enter the three details in OpenOlat and click "Save". From then on, the login page shows the entry "Microsoft Azure AD". This integration needs no mapping of attributes, "Edit attributes" is only available for your own providers.

The steps at Microsoft in the following paragraphs follow the Microsoft documentation, as of November 2026. Microsoft can change menus and labels at any time.

#### Register the app at Microsoft {: #azure_app_registration}

According to [Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app), you register OpenOlat as an app in the Microsoft Entra admin center under:<br>
`Entra ID > App registrations > New registration`<br>
For this, you need at least the role "Application Developer" at Microsoft. After the registration, the "Overview" page of the app shows the Application (client) ID. You enter it in OpenOlat in the field "Client ID".

#### Enter the redirect URI at Microsoft {: #azure_redirect_uri}

After the login, Microsoft only sends the person back to an address that is entered in the app as a redirect URI and matches exactly. Otherwise, the login stops with the error AADSTS50011 ([Microsoft: Error AADSTS50011](https://learn.microsoft.com/en-us/troubleshoot/entra/entra-id/app-integration/error-code-aadsts50011-redirect-uri-mismatch)). According to [Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri), you enter the address under:<br>
`App registrations > "Your app" > Authentication > Add Redirect URI > Web`<br>
As the redirect URI, enter the "Redirect URI" that OpenOlat shows on the Cloud login page in the section "Login via OAuth, cloud services and social providers", and finish at Microsoft with "Configure".

#### Create the client secret at Microsoft {: #azure_client_secret}

According to [Microsoft](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials), you create the secret for the field "Client secret" under:<br>
`App registrations > "Your app" > Certificates & secrets > Client secrets > New client secret`<br>
You enter a description and an expiration and click "Add". Microsoft then shows the value of the secret only once ([Microsoft: Create a client secret](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)). You enter this value in OpenOlat in the field "Client secret". According to Microsoft, a client secret is valid for 24 months at most, and Microsoft recommends less than 12 months. Create a new secret before it expires and enter it in OpenOlat, otherwise the login via Microsoft fails.

#### Look up the tenant at Microsoft {: #azure_tenant}

The tenant is the Microsoft 365 environment of your organisation. In the field "Directory (tenant) ID", enter its identifier so that only people of your organisation can log in. If the field stays empty, the login is open to all people with a Microsoft 365 account. Whether OpenOlat creates a new account for such a person is decided by "Allow registration", see [First login and new accounts](#first_login). Microsoft calls this identifier "Tenant ID" and, according to [Microsoft](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant), shows it in the Microsoft Entra admin center under:<br>
`Entra ID > Overview > Properties`<br>
For this, you need at least the role "Global Reader" at Microsoft.

If the module "Microsoft Teams" and its function "Meeting recording" are switched on, the login via "Microsoft Azure AD" requests an additional permission from Microsoft, and this requires the consent of the administration of your tenant at Microsoft, see [Microsoft Teams module: Function "Meeting recording"](Teams_module.md#recording_enabled). [:octicons-tag-16:{ title="from Release 21.1.1 (OO-9888)" }](https://track.frentix.com/issue/OO-9888)

### Switch edu-ID [:octicons-tag-16:{ title="from Release 16.2.6 (OO-6252)" }](https://track.frentix.com/issue/OO-6252) {: #switch_eduid}

Switch edu-ID is a personal account at SWITCH that stays with a person even after a change of university. Universities in Switzerland connect it as a cloud login, not via [Shibboleth](Login_Shibboleth.md). With "Enforce 2-factor authentication", OpenOlat requests a login with a second factor from Switch edu-ID; Switch edu-ID then asks the person for this factor in addition to the password.

### Datenlotsen {: #datenlotsen}

Datenlotsen is a provider of software for running universities and academies, among them a campus management system. Today, the provider runs its offer under the name octo. You only need the integration "Datenlotsen" if the people of your organisation log in with an account from a system of this provider. In the section "Datenlotsen", you then enter the "Client ID" and "Client secret" that the provider issues for OpenOlat, and under "OAuth2 endpoint" the address at which its login service can be reached.


## Add your own provider [:octicons-tag-16:{ title="from Release 16.2.6 (OO-6267)" }](https://track.frentix.com/issue/OO-6267) {: #own_provider}

If your identity provider is missing from the list, you connect it yourself, provided it supports OpenID Connect or OAuth 2.0, the open standards for a login via an identity provider. The menu "More actions" offers two ways for this:

- **Add OAuth 2.0 provider:** You enter all details of the identity provider by hand, among them "Provider name", "Display name", "Client Id", "Client secret", "Response type" and the addresses of the end points. End points are the addresses at the identity provider that OpenOlat calls during the login: at the "Authorization end point", the person logs in. Via the "Token URL", OpenOlat then fetches an access token, a proof of authorization for the details about the person. If "User info (optional)" is filled in, OpenOlat uses this token to fetch further details about the person there.
- **Add OAuth 2.0 provider with discovery URL:** You only enter the "URL" at which the identity provider publishes its configuration. With "Load configuration", OpenOlat takes over the other details into the form.

### Provider name and display name {: #provider_name}

You define both names when adding the provider. "Display name" is the label with which the login page offers the identity provider for selection. You can change it later in the section of the provider. "Provider name" is the internal identifier of the integration: 3 to 8 characters of letters without umlauts, digits, dot, hyphen and underscore, and each name only once. OpenOlat stores the logins of the people via this provider under this name, so it can no longer be changed after adding the provider.

### Discovery URL {: #discovery_url}

With "Add OAuth 2.0 provider with discovery URL", OpenOlat loads the configuration of the identity provider and pre-fills the form with it: "Issuer", "Authorization end point", "Token URL", "User info (optional)", "Response type" and "Scopes". Check the details and add "Provider name", "Display name", "Client Id" and "Client secret". "Client Id" is the same detail that is called "Client ID" in the ready-made integrations. For "Response type", the value "code" applies, see [OAuth 2.0 and OpenID Connect](#authorization_code_flow).

According to the standard [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html), section 4, an identity provider publishes its configuration at its issuer address with the addition `/.well-known/openid-configuration`. The exact address is given in the documentation of the identity provider.

Two terms come from the standards: the issuer is the address with which the identity provider identifies itself. Scopes are the ranges of details about the person that OpenOlat requests from the identity provider ([OAuth 2.0, RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749), section 3.3).

### Edit attributes {: #attribute_mapping}

With "Edit attributes" in the section of the provider, you define which attribute of the identity provider is taken over into which attribute of the OpenOlat account. On the left, you enter the name of the attribute at the identity provider, on the right, you select the attribute in OpenOlat.

For the login, OpenOlat needs at least an identifier that uniquely designates the person at the identity provider. If the identity provider delivers a token according to OpenID Connect, OpenOlat uses its value "sub" for this without any mapping, the identifier of the person that, according to the standard [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html), section 2, is contained in every such token. Otherwise, map such an attribute to the OpenOlat attribute "Identifier". If the identifier is missing, the login stops with the message "We were not able to identify you". So that OpenOlat finds an existing account at the first login, also map the e-mail address, see [First login and new accounts](#first_login). If OpenOlat is to create new accounts without registration dialog, it also needs "Nickname" for the username and all mandatory fields of the profile.

The names of the attributes are defined by the identity provider. The standard [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html), section 5.1, names among others `email` for the e-mail address, `given_name` for the first name, `family_name` for the last name and `preferred_username` for the preferred username. Which of them your identity provider delivers is stated in its documentation.

### OAuth 2.0 and OpenID Connect [:octicons-tag-16:{ title="from Release 20.2.6 (OO-9287)" }](https://track.frentix.com/issue/OO-9287) {: #authorization_code_flow}

For security reasons, OpenOlat supports only the authorization code flow for OpenID Connect and OAuth 2.0 integrations. In this flow, OpenOlat redirects the person to the identity provider for the login. The identity provider sends them back with a code that OpenOlat may redeem only once. OpenOlat exchanges this code directly at the identity provider for the access token, so the token never passes through the browser of the person. When creating a provider via "Add OAuth 2.0 provider" or via the discovery URL, you therefore select the value "code" in the field "Response type".

[To the top of the page ^](#cloud_login)


## Automatic redirect [:octicons-tag-16:{ title="from Release 13.1.1 (OO-3847)" }](https://track.frentix.com/issue/OO-3847) {: #automatic_redirect}

If all people log in via the same identity provider, you save them the detour via the login page. With "Automatic redirect (local login via /maintenance/)" in the section of the identity provider, OpenOlat immediately opens the login of the identity provider when it is called. The option is available for Active Directory Federation Services, Microsoft Azure Active Directory, Keycloak, Switch edu-ID, Datenlotsen and for your own providers. Switch it on for one identity provider only, OpenOlat always redirects to a single one.

The login page with the OpenOlat password remains reachable: call the address of your installation with the addition `/maintenance/`, for example `https://your.openolat.domain/maintenance/`. System administrators need this way, for example, when the identity provider cannot be reached.


## First login and new accounts {: #first_login}

How OpenOlat takes in a person at the first login via an identity provider, you define in the section "Login via OAuth, cloud services and social providers".

First, OpenOlat looks for an existing account: via the e-mail address that the identity provider delivers, and then via the username that the identity provider delivers. If OpenOlat finds an account, it links the login to it. The person keeps their courses and data and logs in via the identity provider from then on.

If OpenOlat finds no account, "Allow registration" decides:

- **Switched on:** OpenOlat creates a new account. The person completes their details in a registration dialog.
- **Switched off:** The person sees the message "Your account is not yet created on the OpenOlat service. This is required for being able to log in. Please contact the system administrator." You create the account beforehand in the user management, see [Create account](../usermanagement/Create_User.md).

If "Allow registration" is switched on, two further options appear:

- **Skip interactive registration dialog if possible:** OpenOlat creates the new account without registration dialog, provided the identity provider delivers a valid username and all mandatory fields of the profile. [:octicons-tag-16:{ title="from Release 15.5.0 (OO-5381)" }](https://track.frentix.com/issue/OO-5381)
- **Skip disclaimer dialog:** OpenOlat does not ask people who log in via an identity provider to agree to the terms of use.

Administrators see the login procedures of a single account in the "Authentications" tab of the account:<br>
`User management > "Account of the person" > Tab "Authentications"`<br>
There they also add or delete individual authentications, see [Manage user settings](../usermanagement/Configure_User.md).

Which messages a person sees when the login via the identity provider fails is described on the [Login Page](../../manual_user/login_registration/Login_Page.md#external_login) in the user manual.

[To the top of the page ^](#cloud_login)


## Further information {: #further_information}

**Mentioned on this page**<br>
[Microsoft: AD FS overview >](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview)<br>
[Microsoft: OIDC authentication with AD FS >](https://learn.microsoft.com/en-us/SharePoint/security-for-sharepoint-server/set-up-oidc-auth-in-sharepoint-server-with-adfs)<br>
[Microsoft: OAuth and OpenID Connect at AD FS >](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adfsod/7fc51569-b46d-4aba-8ae6-bad19cb9951b)<br>
[Microsoft: Register an application >](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)<br>
[Microsoft: Error AADSTS50011 >](https://learn.microsoft.com/en-us/troubleshoot/entra/entra-id/app-integration/error-code-aadsts50011-redirect-uri-mismatch)<br>
[Microsoft: Add a redirect URI >](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri)<br>
[Microsoft: Add credentials >](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials)<br>
[Microsoft: Create a client secret >](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)<br>
[Microsoft: Find your tenant ID >](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)<br>
[Microsoft Teams module >](Teams_module.md)<br>
[Shibboleth >](Login_Shibboleth.md)<br>
[OpenID Connect Discovery >](https://openid.net/specs/openid-connect-discovery-1_0.html)<br>
[OAuth 2.0, RFC 6749 >](https://datatracker.ietf.org/doc/html/rfc6749)<br>
[OpenID Connect Core >](https://openid.net/specs/openid-connect-core-1_0.html)<br>
[Create account >](../usermanagement/Create_User.md)<br>
[Manage user settings >](../usermanagement/Configure_User.md)<br>
[Login Page >](../../manual_user/login_registration/Login_Page.md)

**Further reading**<br>
[Login: Overview >](Login/index.md)<br>
[LDAP >](Login_LDAP.md)<br>
[Login Concept >](../../manual_user/login_registration/Login_Concept.md)

[To the top of the page ^](#cloud_login)
