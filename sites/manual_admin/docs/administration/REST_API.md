# REST API {: #REST-API}

Other systems such as a student administration, an external course administration or an external learning group administration exchange their data with OpenOlat via the REST API. The REST API is a programming interface following the Representational State Transfer architectural style. Through it, these systems manage users and learning groups, import courses, assemble catalogs or create many objects at once, without anyone carrying out these steps in the user interface.

You switch the REST API on and off in the system administration with the "Access REST API" switch, under:<br>
`Administration > Core functions > REST API`

The REST API page is available to system administrators. It has two tabs:

* **"Configuration"**: switch the REST API on and off, define the access and open the links to the documentation, plus the sections "Request limit (rate limiting)", "Audit log" and "Managed objects".
* **"Audit log"**: evaluate the recorded calls of the REST API, see [Audit log](#audit-log).

![REST API page with the tabs Configuration and Audit log, in the Configuration tab the Access REST API switch that turns the REST API on and off](assets/admin_core_config_rest_api_v2_en.png){ class="shadow lightbox" title="Configuration tab of the REST API page · 2026.10.20" }

[To the top of the page ^](#REST-API)

---

## Concept {: #concept}

REST is a style of architecture to be primarily used with the HTTP protocol, but not exclusively. In the case of HTTP, it utilizes all its features: URIs to describe resources, HTTP Methods as "verbs" to manipulate resources (GET to retrieve resources, PUT to create new ones, POST to modify them, DELETE...), HTTP Headers and Media Types for content negotiation...

In OpenOlat, the JSR-311: JAX-RS (The Java API for RESTful Web Services) is used as a backend for the implementation of the REST API. JSR-311 is a standard from J2EE. We use the reference implementation from the following standard: [Jersey](https://jersey.dev.java.net/).



### API Key for REST access [:octicons-tag-16:{ title="from Release 18.1.0 (OO-7290)" }](https://track.frentix.com/issue/OO-7290)

A dedicated API key is available for accessing the REST API. It is an automatically generated, long and therefore strong password and can be used even when Passkey or two-factor authentication (2FA) is required for signing in to the user interface.

The API key is stored encrypted, in the same way as the OpenOlat password. It is shown only once when it is generated and cannot be retrieved again afterwards. If the key is lost, it must be deleted and a new one generated.

The API key cannot be used to log in to the OpenOlat web application; it is only valid for accessing the REST API. Independently of this, access via a valid session remains possible, for example to access the course database via JavaScript.

API keys are generated in the user management, with the "Add API-Key" button in the "Authentications" tab of an account, see [Manage user settings](../usermanagement/Configure_User.md):<br>
`User management > open the account > "Authentications" tab`

To also allow users to generate a key themselves, activate the "Generation of API Key by user" option (disabled by default):<br>
`Administration > Core functions > REST API > "Configuration" tab`

!!! info "Important"

	As long as the Passkey feature is not enabled, the OpenOlat password can still be used for REST access.


### Limit access to users with API key [:octicons-tag-16:{ title="from Release 20.1.0 (OO-8745)" }](https://track.frentix.com/issue/OO-8745)

When the REST API is enabled, it can in principle be used by all users with an authenticated session. Often, however, access should be restricted to specific users.

The "API access" selection in the "Configuration" tab of the REST API page determines who may use the REST API:

* **for all users**: access is open to all authenticated users.
* **only for user with API key**: access is restricted to users who have an API key.

Combined with generating the keys exclusively through the user management, this allows access to the REST API to be granted to specific users in a targeted way.


[To the top of the page ^](#REST-API)

---  

###  Usage {: #usage}

The OpenOlat REST API is built for remote management applications. It does not implement all features available in the user interface, and many of the requests are reserved for administrative users such as administrators, user managers, group managers and authors.

The main functions of the REST API include, for example, creating and organizing users, courses, groups, organisations, products (curriculum) or calendar events.

The REST API reads roll calls, but it cannot execute them: you cannot set a person as present or absent through it. What you can change is the supervisor notification date, the comment and the reason.

While theoretically possible, it is not in the spirit of the concept to use the REST API for an alternative user interface.

[To the top of the page ^](#REST-API)

---

##  Security {: #security}

The security is based on a two level mechanism, as it is in OpenOlat.

  1. The first level is a servlet filter which collects all requests to the REST API. This filter determines whether the URI is open to everyone (`/api`, `/ping`, `/auth`...) or if it needs an authentication. The filter hands the authentication itself over to a web service.
  2. The second level applies to every call of the REST API. Every method checks if the user (if a user must be authenticated) has enough privileges to operate on the desired resource.

To maintain a valid authentication over several requests, the filter proposes two methods:

  1. Reuse the session cookie on every request. The advantage of this method is that OpenOlat doesn't need to create a session on every request.
  2. If you cannot use the session cookie, the filter always adds an HTTP Header (`X-OLAT-TOKEN`) to the response. Send this token with the next request to maintain your privileges.

###  Best practice usage

If the REST API is used to implement specific features in the OpenOlat web user interface such as using the course database, the OpenOlat web session cookie can be reused (method 1). The user is already authenticated in the browser

If the REST API is used by an external (server based) application, best- practice is to use basic authentication to authenticate the user and enable session cookies in the http client of the remote application.

If none of the above is possible, use method 2 using the `X-OLAT-TOKEN`. Note that a user can have only one `X-OLAT-TOKEN` at any time. If your remote application sends several requests concurrently, basic authentication should be used.

If you are building a remote portal and want to implement some kind of home- brew single-sign-on process, method 2 can be used to generate the X-OLAT-TOKEN for every user as a server request. The Token can then be added to each link in the portal to login the user based on the token (`?X-OLAT-TOKEN=xyz`). When clicking the link, OpenOlat will identify the user based on the token and create a valid session. Security wise there are better options to achieve the same. We recommend using OAuth instead which is supported by OpenOlat as well.

[To the top of the page ^](#REST-API)

---

## Audit log [:octicons-tag-16:{ title="from Release 21.1.0 (OO-9778)" }](https://track.frentix.com/issue/OO-9778){:target="_blank"} {: #audit-log}

An account has suddenly changed, a membership is missing, or a third-party system fails to log in. The audit log shows you which calls the REST API has received: who called which path, when and from which IP address, and how OpenOlat responded. You get this information without access to the database.

You evaluate the entries in the "Audit log" tab of the REST API page; the settings are in the "Configuration" tab, section "Audit log". Both are available to system administrators.

### Which calls appear in the audit log {: #audit_log_calls}

Whether a call creates an entry depends on its method and on the response:

* **Write calls**: Every call with PUT, POST, DELETE or PATCH creates an entry, even if it fails.
* **Denied calls**: Every call with the status 401, 403, 429 or 5xx creates an entry, including a read call.
* **Read calls**: A successful call with GET or HEAD creates an entry only when the option "Record read calls (GET)" is switched on. By default, it is switched off.

If a call is missing from the audit log, it was usually a successful read call. No entries are created either while the "Audit log" switch is set to "Off" or while the REST API is switched off.

If the request limit rejects a third-party system with the status 429, only the first rejection per minute appears in the audit log. OpenOlat counts per logged-in person, and per IP address for calls without login. A third-party system that ignores the rejection and keeps sending does not flood the audit log this way.

### Evaluate entries {: #audit_log_evaluation}

You find the table of the audit log in the system administration under:<br>
`Administration > Core functions > REST API > "Audit log" tab`

The newest entries are at the top. The following options are available for the evaluation:

* **Period**: "Today", "Last 7 days" (preselected), "This month", "Last month" and "Custom" for a time range of your own.
* **Filters**: "User", "Method", "Resource" and "Status". The "Status" filter groups the responses: "Success (2xx, 3xx)", "Denied (401, 403)", "Request limit (429)", "Client error (4xx)" and "Server error (5xx)". You add the "Channel" filter via "More...".
* **Columns**: The table shows "Date", "User", "Authentication", "IP address", "Method", "Path", "Resource", "Status" and "Duration (ms)". You show further columns such as "Request body" or "Login attempt" under: `Table settings > Displayed columns`
* **Details**: The "Details" link in each row opens the "Audit log entry" dialog with all data of the call.
* **Download**: The "Download" icon above the table downloads the filtered table as an Excel file.

![Filters User, Channel, Method, Resource and Status above the table, in it write calls with status 200 and a denied call with status 401](assets/admin_core_config_rest_api_audit_log_v1_en.png){ class="shadow lightbox" title="Audit log tab of the REST API page · 2026.10.20" }

### Data of an entry {: #audit_log_entry}

An entry tells who sent a call, what the call requested and how OpenOlat responded. The "Audit log entry" dialog shows all data:

![Call that creates an account: in the request body the password is replaced by three asterisks](assets/admin_core_config_rest_api_audit_log_details_v1_en.png){ class="shadow lightbox" title="Audit log entry dialog · 2026.10.20" }

| Field | Content |
|---|---|
| Date | Time of the call |
| Channel | Way the call came in, "REST" for the REST API |
| User | Logged-in person; empty if the call came without a valid login |
| Login attempt | User name of a failed login |
| Authentication | Type of login of the call |
| IP address | Address the call came from |
| User agent | Identifier of the calling program |
| Node | Server in the cluster that processed the call |
| Method | HTTP method, for example PUT |
| Path | Called path, for example `/olat/restapi/users`; it starts with the context path of the instance |
| Query | Parameters after the question mark in the address |
| Resource | Web service that processed the call, for example "UserWebService"; empty if the call did not reach a web service |
| Resource method | Method of the web service, for example "create" |
| Status | HTTP status of the response |
| Duration (ms) | Processing time in milliseconds |
| Reference | Internal identifier of the request |
| Path parameters | Values from the path, for example `{"groupKey":"2290515968"}` for a call to `/restapi/groups/{groupKey}` |
| Request body | Content of a write call in JSON format |

Passwords and other secret values never appear in plain text in the audit log. In the request body and in the query, OpenOlat replaces the values of the fields password, credential, secret, clientSecret, token and sharedSecret with `***`, regardless of upper and lower case. OpenOlat does not mask the path parameters. Only content in JSON format is stored; for a file upload, the request body only shows the content type and the size. If a content is larger than the "Maximum body size (bytes)", OpenOlat truncates it.

### Settings {: #audit_log_settings}

You define what the audit log records and for how long in the system administration, under:<br>
`Administration > Core functions > REST API > "Configuration" tab`

The "Audit log" section appears as soon as the "Access REST API" switch is set to "On". You apply your changes with "Save" at the end of the page. The defaults of these settings can also be set in the server configuration. frentix customers contact the frentix support for this: [support@frentix.com](mailto:support@frentix.com)

![Audit log switch on, read calls off, store request body on, maximum body size 16384 bytes and retention 365 days](assets/admin_core_config_rest_api_audit_log_settings_v1_en.png){ class="shadow lightbox" title="Audit log section in the Configuration tab · 2026.10.20" }

#### Audit log {: #audit_log_switch}

When the switch is set to "On", calls create entries according to the rules above, and the other fields of the section appear. When it is set to "Off", no new entries are created; existing entries remain readable until the end of their retention. By default, the switch is set to "On". When you switch the REST API on, OpenOlat also sets the "Audit log" switch to "On". When you switch the REST API off and save, OpenOlat also switches the audit log off.

#### Record read calls (GET) {: #audit_log_reads}

When switched on, every successful read call also creates an entry, and the audit log grows accordingly fast. Therefore switch the option on only temporarily, for example to analyse a third-party system with many read calls, and switch it off again afterwards. By default, the option is switched off.

#### Store request body {: #audit_log_body}

When switched on, OpenOlat stores the content of the request of write calls in JSON format, with masked passwords. This lets you see later which values a third-party system sent. When switched off, the "Request body" field remains empty. By default, the option is switched on.

#### Maximum body size (bytes) {: #audit_log_body_size}

OpenOlat truncates longer content to this size. Values from 1024 to 1048576 bytes are allowed, the default is 16384. The field appears only when "Store request body" is switched on.

#### Retention (days, 0 = unlimited) {: #audit_log_retention_days}

Number of days an entry is kept, by default 365. With 0, OpenOlat deletes no entries. The section [Retention and deletion](#audit_log_retention) describes how the deletion works.

### Retention and deletion {: #audit_log_retention}

The audit log only reaches as far back as the retention allows. Every night at 01:41 server time, OpenOlat deletes the entries that are older than the configured number of days. Deleted entries cannot be restored. If you need entries for longer, download them as an Excel file beforehand.

An entry can contain personal data, for example name and email address in the request body of a call that creates an account. When an account is deleted, such entries are kept until the retention deletes them. More about deleting accounts: [Data protection](../usermanagement/Data_protection.md#deletion_overview)

[To the top of the page ^](#REST-API)

---

##  Configuration {: #configuration}

A spring bean allows to configure Resources, Singletons and Providers; either statically with the XML configuration of the bean ( `/org/olat/restapi/_spring/restApiContext.xml` ) or programmatically by adding or removing classes and singletons to/from the bean (bean id is the same as its interface: `org.olat.restapi.support.RestRegistrationService` ).

OpenOlat uses the standard JAXB provider from Jersey to produce XML from java objects, as well as the JSON provider from [Jackson](http://jackson.codehaus.org/), which reuses the same JAXB annotations.

!!! info "Important"

	All configuration settings must be done before the Jersey's servlet starts.


###  Example

Here is a little example on how to create a user and add it to a learning group:

    PUT https://your.openolat.domain/olat/restapi/users
    HTTP Header: Content-Type application/json
    Response: 200
    GET https://your.openolat.domain/olat/restapi/groups
    HTTP Header: Accept application/json
    Response: 200
    Choose a group
    PUT https://your.openolat.domain/olat/restapi/groups/{groupId}/users/{identityKey}
    Response: 200

[To the top of the page ^](#REST-API)

---

## Documentation {: #documentation}

Whoever connects a third-party system to OpenOlat finds all endpoints of the REST API in its documentation. The documentation is based on the OpenAPI specification (formerly Swagger Specification), a description format for REST interfaces. It describes the available endpoints, the operations on each endpoint with parameters, input and output, as well as the objects used by the REST API.

The links to the documentation are in the "Configuration" tab of the REST API page under "Documentation OpenAPI 3.0", as soon as the REST API is switched on:

* **"Pretty docu with SwaggerUI"**: the readable documentation at the address `/restapi/api-docs/` of your instance.
* **"Raw JSON"**: the complete description in a single document, the file openapi.json at the address `/restapi/openapi.json` of your instance.

The SwaggerUI allows you to choose a specific server prefix and to execute the listed requests with the "try it out" button. These requests are binding: they change the data of the addressed system directly.

 [To the top of the page ^](#REST-API)

---

##  Externally managed courses and groups  {: #managed}

Courses and groups can be created via REST API. Such externally managed courses and groups are called "managed" as an external system is responsible for their lifecycle. You switch the use of this functionality on and off per object type in the "Configuration" tab, section "Managed objects", under:<br>
`Administration > Core functions > REST API > "Configuration" tab`

Via REST API an optional external ID can be attached to courses and groups. For courses an additional external reference can be used to help identify the resource for end users.

If such external ID's are used for courses or groups, the external systems must also configure for each external resource which elements in OpenOlat are managed by the external system and which can be modified within the OpenOlat user interface. This is configured with so called "managed flags". Either all elements are managed or the managed elements are listed in detail. The configuration of the "managed flags" are described in the technical documentation of the REST API.

If the external management is enabled, the user elements in the OpenOlat user interface configured to be "managed" are displayed non-editable. In addition, the external ID's are used in search fields, detail pages and tables. Other non managed resources can be used and managed within OpenOlat as usual.

??? abstract "Managed organisations"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * externalId
	    * type
	    * move
	    * members
	    * delete

??? abstract "Managed organisation types"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * cssClass
	    * externalId
	    * subTypes
	    * delete

??? abstract "Managed products"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * externalId
	    * delete
	    * members

??? abstract "Managed elements"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * externalId
	    * status
	    * dates
	    * type
	    * calendars
	    * units
	    * members
	    * resources
	    * move
	    * addChildren
	    * delete

??? abstract "Managed element types"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * cssClass
	    * description
	    * externalId
	    * calendars
	    * units
	    * subTypes
	    * copy
	    * delete

??? abstract "Managed groups"

	* Fully externally managed (all)
	    * Title, description and available seats/waiting list configuration (details)
	        * Group title (title)
	        * Description (description)
	        * Available seats/waiting list configuration (settings)
	    * Tools configuration (tools)
	    * Members management and configuration of members visibility (members)
	        * Visibility members (display)
	        * Members management (membersmanagement)
	    * Adding courses (resources)
	    * Booking rules (bookings)
	    * Delete group workflow (delete)

??? abstract "Managed learning resources (courses)"

	* Fully externally managed (all)
	    * Course Editor (editcontent)
	    * Details (details) 
	        * Title (title)
	        * Description (description)
	        * Objectives (objectives)
	        * Requirements (requirements)
	        * Credits (credits)
	        * Location (location)
	        * Organisations (organisations)
	    * Settings (settings)
	        * Access configuration (access)
	        * Search settings (search)
	        * Chat settings (chat)
	        * Layout settings (layout)
	        * Resource folder configuration (resourcefolder)
	        * Efficiency statement settings (efficencystatement)
	        * Calendar settings (calendar)
	        * Glossary settings (glossary)
	    * Units (unit)
	        * Unit configurations (unitconfig)
	        * Unit management (unitmanagement)
	    * Booking rules (bookings)
	    * Members management (membersmanagement)
	    * Group management (groups)
	    * Close course workflow (close)
	    * Delete course (delete)
	    * Copy course (copy)

??? abstract "Managed events"

	* Fully externally managed (all)
	    * details
	        * title
	        * compulsory
	        * plannedUnits
	        * teachers
	        * groups
	        * description
	        * preparation
	        * location
	        * dates
	    * settings
	    * delete

??? abstract "Managed taxonomies"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * externalId
	    * librarySettings

??? abstract "Managed taxonomy levels"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * externalId
	    * sortOrder
	    * type
	    * competences
	        * manageCompetence
	        * teachCompetence
	        * haveCompetence
	        * targetCompetence
	    * move
	    * delete

??? abstract "Managed taxonomy level types"

	* Fully externally managed (all)
	    * identifier
	    * displayName
	    * description
	    * cssClass
	    * externalId
	    * visibility
	    * subTypes
	    * librarySettings
	    * copy
	    * delete

??? abstract "Managed calendars"

	* Fully externally managed (all)
	    * details
	        * subject
	        * description
	        * location
	        * dates
	        * liveStreamUrl
	    * classification
	    * links

??? abstract "Managed roles"

	* Fully externally managed (all)
	    * name
	    * rights
	    * delete

??? abstract "Managed identity to identity relations"

	* Fully externally managed (all)
	    * delete


[To the top of the page ^](#REST-API)

---


## Further information {: #further_information}

[Jersey](<https://jersey.dev.java.net/>)<br>
[Manage user settings >](../usermanagement/Configure_User.md)<br>
[Data protection >](../usermanagement/Data_protection.md)<br>
[Jackson](<http://jackson.codehaus.org/>)<br>
[External tools: AI module >](External_Tools_AI.md)<br>
[Assign roles >](../usermanagement/Assign_roles.md)

[To the top of the page ^](#REST-API)

