# How do I integrate an OpenOlat course into Moodle? {: #LTI_integrate_course_into_moodle}


??? abstract "Objectives and content of this instruction"

    You have created a course in OpenOlat and would like to offer it outside your OpenOlat on a Moodle platform?<br>
    The following instructions show you the procedure step by step.

??? abstract "Target group"

    [x] Authors [ ] Coaches  [ ] Participants

    [ ] Beginners [x] Advanced users  [x] Experts

??? abstract "Expected previous knowledge"

    * Administration manual: [LTI 1.3 Integrations >](../../manual_admin/administration/LTI_Integrations.md)
    * Administration manual: [LTI - External Platforms >](../../manual_admin/administration/LTI_External_platforms.md)
    * User manual: [Configure LTI access to a course >](../../manual_user/learningresources/LTI_Share_courses.md)


---

To display an OpenOlat course on another platform, in the following instructions this is Moodle, a connection is established according to the LTI 1.3 standard (Learning Tools Interoperability).<br>

So that the users of the Moodle platform can access the OpenOlat course from their system, the two platforms must communicate with each other, and on the OpenOlat side the course (and only this course) must be released for this external access.


## Requirements {: #conditions}

Administrator access must be ensured in both systems for the configuration. In OpenOlat, the System administrator role opens the system administration, where the external platform is entered. Who may release a course via LTI is defined by the system administration in the "Configuration" tab under `Administration > External tools > LTI`. Preferably, the configuration is done on both systems at the same time, since certain dialogs have to be configured in both systems in direct succession.

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## Configuration procedure {: #config_process}

1. [Setup "External Tool" in Moodle](#setup_step1)
2. [Setup "External platform" in OpenOlat](#setup_step2)
3. [LTI release of the course in OpenOlat](#setup_step3)
4. [Embedding the external tool (=OpenOlat) in the Moodle course](#setup_step4)
5. [Connection test](#setup_step5)


## 1. Setup "External Tool" in Moodle  {: #setup_step1}

The administration of the external tools in Moodle is located under the following path:<br>
`Site administration > Plugins > External Tool > Manage Tools`

![Marked entry External tool with Manage tools in the Plugins tab](assets/LTI_integrate_course_into_moodle-setup1_v1_en.png){ class="shadow lightbox" title="Site administration in Moodle" }

For the configuration with OpenOlat, the option "**configure a tool manually**" must be selected.

![Marked link configure a tool manually to set up an external tool manually](assets/LTI_integrate_course_into_moodle-setup2_v1_en.png){ class="shadow lightbox" title="Manage tools page in Moodle" }


The following parameters must be defined in the dialog as minimum requirements:

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Tool name				| Freely definable |
| Tool URL				| Direct link to the OpenOlat course. <br> The URL has the following format: `https://<OpenOlat-URL>/auth/RepositoryEntry/<Course-ID>` <br>(Make sure that no / is added at the end of the URL.) |
| LTI Version			| LTI 1.3 |
| Client ID				| Only becomes visible after saving in this form |
| Public key type		| RSA key |
| Public key			| Is generated in OpenOlat, can only be entered afterwards |
| Initiate Login URL	| Initiate login URL, format: `https://<OpenOlat-URL>/lti/login_initiation` |
| Redirection URL(s)	| Redirection URL, format: `https://<OpenOlat-URL>/lti/login` |
| Tool Configuration Usage| Show in activity chooser and as a preconfigured tool |
| Default Launch Container	| New window (OpenOlat only supports running the courses in a new window.) |

![Completed form with Tool URL, LTI version, public key, initiate login URL and redirection URL](assets/LTI_integrate_course_into_moodle-setup3_v1_en.png){ class="shadow lightbox" title="External tool configuration form in Moodle" }

After saving, you can call up further details in the overview via the details link in the LTI tool. The details are needed for the setup of the external platform in OpenOlat:

![Platform ID, Client ID, Deployment ID and the three URLs for keyset, access token and authentication](assets/LTI_integrate_course_into_moodle-setup4_v1_en.png){ class="shadow lightbox" title="Tool configuration details dialog in Moodle" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 2. Setup "External platform" in OpenOlat {: #setup_step2}

The administration of LTI 1.3 is located in the system administration of OpenOlat under the following path:<br>
`Administration > External tools > LTI`

![Switched-on module LTI 1.3 with platform ID and organisation, below it the roles allowed to add a deployment](assets/LTI_integrate_course_into_moodle-setup5_v2_de.png){ class="shadow lightbox" title="Configuration tab of the LTI administration" }

In the "External platforms" tab, enter the Moodle instance with the "Add external platform" button:

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Name				| Freely definable |
| Platform ID / Issuer	| URL of the Moodle instance |
| Client ID				| Client ID from the "Tool configuration details" dialog in Moodle |
| Public Key Type | Public Key -> this key is then added to the tool configuration on Moodle |
| Authorization	 		| From Moodle: Authentication request URL |
| Token URI	| From Moodle: Access token URL |
| JWK-Set URI | From Moodle: Public Keyset URL |


After completing the form, enter the public key on Moodle in the tool configuration.

![Completed form with name, platform ID, client ID, public key and the three URLs from Moodle](assets/LTI_integrate_course_into_moodle-setup6_v2_en.png){ class="shadow lightbox" title="Edit platform dialog in OpenOlat" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 3. LTI release of the course in OpenOlat {: #setup_step3}

An OpenOlat course (or an OpenOlat group) is released in the settings under the following path:<br>
`Course > Administration > Settings > Tab "Share" > Section "LTI 1.3 access configuration"`

![LTI 1.3 access configuration section with the Add deployment button and the configured deployment](assets/LTI_integrate_course_into_moodle-setup7_v2_en.png){ class="shadow lightbox" title="Share tab of the course settings" }

Add a deployment for the course (or the group) with the "Add deployment" button:

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Platform				| Selection of the configured Moodle instance |
| Deployment ID 		| From Moodle: Deployment ID from the "Tool configuration details" dialog. The same deployment ID may be used in several courses of the same platform, but only once in the same course. |
| Tool URL				| Provided by OpenOlat, read-only. The Tool URL of the external tool in Moodle from step 1 must begin with this address. |
| Initiate login URL, Redirection URL | Provided by OpenOlat, read-only. The same addresses are entered in Moodle in step 1 under Initiate Login URL and Redirection URL(s). |
| Public Key | The public key of the selected platform, read-only. It is the same key as in the dialog of the external platform from step 2. "Public Key Type" switches the display between "Public Key" and "URL". |

![Marked fields Deployment ID and Tool URL, the Tool URL pre-filled with the address of the course](assets/LTI_integrate_course_into_moodle-setup8_v3_en.png){ class="shadow lightbox" title="Create a new tool dialog in OpenOlat · 2026.10.07" }

If several OpenOlat courses are to be reachable via the same deployment ID, share each course individually. More about this in the user manual under:<br>
[One deployment ID for several courses >](../../manual_user/learningresources/LTI_Share_courses.md#deployment_id_several_courses)

You can find more about the LTI 1.3 access configuration section in the user manual under:<br>
[Course settings - Tab Share >](../../manual_user/learningresources/Course_Settings_Share.md#section_LTI)

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 4. Embedding the external tool (=OpenOlat) in the Moodle course {: #setup_step4}

The external tool (OpenOlat) can now be inserted in the Moodle course.

![Search for External tool with one result, for adding an activity](assets/LTI_integrate_course_into_moodle-setup9_v1_en.png){ class="shadow lightbox" title="Add an activity or resource dialog in Moodle" }

The configured OpenOlat course can be selected here in the external tool on Moodle as a "preconfigured tool".

![Selected preconfigured tool in the Preconfigured tool field](assets/LTI_integrate_course_into_moodle-setup10_v1_en.png){ class="shadow lightbox" title="Adding a new External tool page in Moodle" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 5. Connection test {: #setup_step5}

Whether the configuration has worked can be checked with a simple test call.

![The embedded external tool as a link in the General course section](assets/LTI_integrate_course_into_moodle-setup11_v1_en.png){ class="shadow lightbox" title="Course page in Moodle" }

The link in Moodle should open the desired OpenOlat course in a new window.

!!! warning "Attention"

    If you are already logged in to OpenOlat in another tab, you will be logged out there.


In the OpenOlat course, you can verify the test call in the members management: the LTI call has created a new account and added it to the group "LTI: name of the platform".

![Newly created account with the role group coach in the group LTI: fxTest Moodle](assets/LTI_integrate_course_into_moodle-setup12_v1_en.png){ class="shadow lightbox" title="Members management of the course" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---

## Further information {: #further_information}

**Mentioned on this page**<br>
[LTI 1.3 Integrations >](../../manual_admin/administration/LTI_Integrations.md)<br>
[LTI - External Platforms >](../../manual_admin/administration/LTI_External_platforms.md)<br>
[Configure LTI access to a course >](../../manual_user/learningresources/LTI_Share_courses.md)<br>
[Course settings - Tab Share >](../../manual_user/learningresources/Course_Settings_Share.md)

**Further reading**<br>
[Configure LTI access to a group >](../../manual_user/groups/LTI_Share_groups.md)<br>
[Course Element "LTI Page" >](../../manual_user/learningresources/Course_Element_LTI_Page.md)<br>
[LTI - External tools >](../../manual_admin/administration/LTI_External_tools.md)<br>
[LTI - Deep Linking >](../../manual_admin/administration/LTI_Deeplinking.md)<br>
[LTI - Role mapping >](../../manual_admin/administration/LTI_Role_Mapping.md)

[To the top of the page ^](#LTI_integrate_course_into_moodle)

