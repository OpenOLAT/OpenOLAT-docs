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

To display an OpenOlat course on another platform - in the following instructions this is Moodle - a connection is established according to the LTI 1.3 standard.<br>

So that the users of the Moodle platform can access the OpenOlat course from their system, the two platforms must communicate with each other, and on the OpenOlat side the course (and only this course...) must be released for this external access.


## Requirements {: #conditions}

Administrator access must be ensured in both systems for the configuration. (In OpenOlat, this can also be the System administrator role).  Preferably, the configuration is done on both systems at the same time, since certain dialogs have to be configured in both systems in direct succession.

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

![Entry External tool with Manage tools, in the Plugins menu of the Site administration in Moodle](assets/LTI_integrate_course_into_moodle-setup1_v1_en.png){ class="shadow lightbox" }

For the configuration with OpenOlat, the option "**configure a tool manually**" must be selected.

![The link 'configure a tool manually' to set up an external tool manually, in the Manage tools dialog in Moodle](assets/LTI_integrate_course_into_moodle-setup2_v1_en.png){ class="shadow lightbox" }


The following parameters must be defined in the dialog as minimum requirements:

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Tool name				| Freely definable |
| Tool URL				| Direct link to the OpenOlat course. <br> The URL has the following format: https:// < OpenOlat-URL > /auth/RepositoryEntry/ < CourseID > <br>(Make sure that no / is added at the end of the URL.) |
| LTI Version			| LTI 1.3 |
| Client ID				| Only becomes visible after saving in this form |
| Public key type		| RSA key |
| Public key			| Is generated in OpenOlat, can only be entered afterwards |
| Initiate Login URL	| Login URL (Form: hdps://<OpenOlat-URL/lT/login_iniTaTon) |
| Redirection URL(s)	| Redirection URL (Form: hdps://<OpenOlat-URL/lT/login) |
| Tool Configuration Usage| Show in activity chooser and as a preconfigured tool |
| Default Launch Container	| New window (OpenOlat only supports running the courses in a new window.) |

![Completed External tool configuration form with Tool URL, LTI version and public key, in Moodle](assets/LTI_integrate_course_into_moodle-setup3_v1_en.png){ class="shadow lightbox" }

After saving, you can call up further details in the overview via the details link in the LTI tool. The details are needed for the setup of the external platform in OpenOlat:

![Tool configuration details with Platform ID, Client ID and Deployment ID, in the tool overview in Moodle](assets/LTI_integrate_course_into_moodle-setup4_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 2. Setup "External platform" in OpenOlat {: #setup_step2}

The administration of LTI 1.3 is located in OpenOlat under the following path:<br>
`Administration > External tools > LTI`

![Module 'LTI 1.3' with platform ID and organisation, in the Configuration tab under External tools > LTI of the system administration](assets/LTI_integrate_course_into_moodle-setup5_v2_de.png){ class="shadow lightbox" }

Under "External platforms", the Moodle instance can be entered:

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Tool name				| Freely definable |
| Platform ID / Issuer	| URL of the Moodle instance |
| Client ID				| Client ID from the "Tool configuration details" dialog in Moodle |
| Public Key Type | Public Key -> this key is then added to the tool configuration on Moodle |
| Authorization	 		| From Moodle: Authentication request URL |
| Token URI	| From Moodle: Access token URL |
| JWK-Set URI | From Moodle: Public Keyset URL |


After completing the form, enter the public key on Moodle in the tool configuration.

![Completed platform edit form with platform ID, client ID and public key, in the Edit platform dialog in OpenOlat](assets/LTI_integrate_course_into_moodle-setup6_v2_en.png){ class="shadow lightbox" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 3. LTI release of the course in OpenOlat {: #setup_step3}

An OpenOlat course (or an OpenOlat group) is released in the settings under the following path:<br>
`OpenOlat course > Settings > Tab "Share" > LTI 1.3 access configuration`

![LTI 1.3 access configuration section with the configured deployment, in the Share tab of the course settings](assets/LTI_integrate_course_into_moodle-setup7_v2_en.png){ class="shadow lightbox" }

Add a deployment for the course (or the group):

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Platform				| Selection of the configured Moodle instance |
| Deployment ID 		| From Moodle: Deployment ID from the "Tool configuration details" dialog |

![Completed Add new tool form with platform and deployment ID, in the dialog for a new deployment in OpenOlat](assets/LTI_integrate_course_into_moodle-setup8_v2_en.png){ class="shadow lightbox" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 4. Embedding the external tool (=OpenOlat) in the Moodle course {: #setup_step4}

The external tool (OpenOlat) can now be inserted in the Moodle course.

![Search for External tool in the Add an activity or resource dialog, in the Moodle course](assets/LTI_integrate_course_into_moodle-setup9_v1_en.png){ class="shadow lightbox" }

The configured OpenOlat course can be selected here in the external tool on Moodle as a "preconfigured tool".

![Selecting the preconfigured tool in the Preconfigured tool field, when adding the external tool in the Moodle course](assets/LTI_integrate_course_into_moodle-setup10_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---


## 5. Connection test {: #setup_step5}

Whether the configuration has worked can be checked with a simple test call.

![The embedded external tool in the General course section, in the Moodle course](assets/LTI_integrate_course_into_moodle-setup11_v1_en.png){ class="shadow lightbox" }

The link in Moodle should open the desired OpenOlat course in a new window. 

!!! warning "Attention"

	If you are already logged in to OpenOlat in another tab, you will be logged out there.  


In the OpenOlat course, you can verify the test call in the Members management: The LTI call has created a new LTI user and added it to an LTI group:

![Newly created LTI user with the role coach in the LTI group, in the Members management of the course](assets/LTI_integrate_course_into_moodle-setup12_v1_en.png){ class="shadow lightbox" }

[To the top of the page ^](#LTI_integrate_course_into_moodle)

---

## Further information {: #further_information}

User manual: [Configure LTI access to a course >](../../manual_user/learningresources/LTI_Share_courses.md)<br>
User manual: [Configure LTI access to a group >](../../manual_user/groups/LTI_Share_groups.md)<br>
User manual: [Course element "LTI page" >](../../manual_user/learningresources/Course_Element_LTI_Page.md)<br>
Administration manual: [LTI 1.3 Integrations >](../../manual_admin/administration/LTI_Integrations.md)<br>
Administration manual: [LTI - External tools >](../../manual_admin/administration/LTI_External_tools.md)<br>
Administration manual: [LTI - External Platforms >](../../manual_admin/administration/LTI_External_platforms.md)<br>
Administration manual: [LTI - Deep Linking](../../manual_admin/administration/LTI_Deeplinking.md)<br>
Administration manual: [LTI - Role mapping](../../manual_admin/administration/LTI_Role_Mapping.md)

[To the top of the page ^](#LTI_integrate_course_into_moodle)


