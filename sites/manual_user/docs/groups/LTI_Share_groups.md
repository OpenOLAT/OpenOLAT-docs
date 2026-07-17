# Configure LTI access to a group {: #LTI_access_to_a group}

:octicons-tag-24: Release 15.5 

With LTI, it is not only possible to use content (courses) on another LMS. LTI can also be used to exchange data about course participants and coaches (LTI services for the provisioning of names and roles, as well as the LTI "Assignments and Grades" services).

This allows, for example, grades to be exchanged securely with the examination office via API. Strengths and weaknesses of the submitted work can also be discussed with the students if the course attended originates from another LMS and the communication infrastructure of your own LMS is not available there.

## Direction of the exchange

Information about groups and members can generally be exchanged in both directions:

* from OpenOlat (= tool) to the other LMS (= platform)
* from the other LMS (= tool) to OpenOlat (= platform)


![LTI_share_groups_platform_tool_v1_de.png](assets/LTI_share_groups_platform_tool_v1_de.png){ class="lightbox" }


## Requirements

Administrator access must be ensured in both systems for the configuration. (In OpenOlat, this can also be the system administrator role.) Preferably, the configuration is carried out on both systems at the same time, as certain dialogs in both systems must be configured directly one after the other.

## Configuration procedure

1. Set up "External Tool" in Moodle
2. Set up "external platform" in OpenOlat
3. LTI release of the course in OpenOlat
4. Embedding the external tool (= OpenOlat) in the Moodle course
5. Connection test

The detailed procedure for a configuration is described under [Configure LTI access to a course](https://docs.openolat.org/en/manual_user/learningresources/LTI_Share_courses/?h=lti).



## Learner data in the LTI configuration

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_groups_course_element_page_content_v1_de.png" />
</details>

**Transmit firstname/name:**<br>
If you check this checkbox, the user's first and last name is passed to the external learning application. Otherwise, the user can use the external learning application anonymously.

**Transmit e-mail address:**<br>
If you check the checkbox, the user's e-mail address is passed to the external learning application.

**Additional attributes:**<br>
In this input field you can enter further parameters to be transmitted to the learning application. For example, the learning application can be informed that the request is transmitted by the OpenOlat learning platform. (The external learning application must be able to process the information passed on, which is why an agreement with the provider is necessary.) You can choose between static text attributes (the value is identical for all users) or additional dynamic user attributes (different for each user). You can define any number of additional attributes, but the LTI resource must know that these attributes exist, as they are not defined in the standard.

**OpenOlat roles:**<br>
In this area you can define which role the individual users take on when they start the LTI resource. The three OpenOlat course roles owner, coach and participant are supported. For each role, you can define exactly which roles are to be applied on the side of the LTI resource. The following LTI roles can be configured: learner, instructor, administrator, teaching assistant, content developer and mentor.

**Transfer score:**<br>
Select this checkbox if the LTI resource is to generate points and transmit them to OpenOlat using the LTI standard. This is optional. Transmitted points appear for the user on the start page of the LTI element as well as on the evidence of achievement. Please note that, according to the standard, LTI can only deliver a value between 0 and 1.

If the "Transfer score" option is activated, the LTI page can be added to the course as an assessable course element and then appears in the assessment tool. In addition, the transmitted points appear for the user on the start page of the LTI element.

**Scaling factor:**<br>
With the scaling factor, you can scale the LTI results, which according to the standard must have a value between 0 and 1, to a more practical value in the OpenOlat course. For example, if you want to award a maximum of 10 points for an LTI task in OpenOlat, you must enter the value "10" as the scaling factor. If you want to transfer the points unchanged, select the value "1".

**Score needed to pass:**<br>
Enter the optional threshold value here, from which the LTI element is considered passed. This threshold value refers to the scaled final result and not to the raw data transmitted by LTI. In the example above, a threshold value of "5" would be equivalent to "50%".


## Transferring group data via LTI

An OpenOlat group is shared for LTI access in the same way as a course. Sharing is configured in the group management in the "Share" tab, in the "LTI 1.3 access configuration" section, via the "Add deployment" button.

In the deployment dialog you enter the same details as when sharing a course: the previously configured "Platform", the "Deployment ID", the technical addresses ("Tool URL", "Initiate login URL", "Redirection URL") and the "Public Key". The detailed procedure including the counterpart configuration in the external LMS is described under [Configure LTI access to a course](https://docs.openolat.org/en/manual_user/learningresources/LTI_Share_courses/?h=lti) and applies to groups in the same way.

The exchange of member data (names and roles) uses the LTI standard service "Names and Role Provisioning Service" (NRPS). Which member data is transmitted is determined by the system that provides the connection as the platform. The basic LTI 1.3 settings are managed by administrators under `Administration > External tools > LTI 1.3`.

## Groups without course affiliation

A group can be shared via LTI independently of a course. This is useful when you do not want to share an entire course but only exchange data about users and their group membership. For example, only the results of an assessment can be transferred without sharing the associated course.

##  Further information {: #further_information}

User manual: [Configure LTI access to a course >](../../manual_user/learningresources/LTI_Share_courses.md)

User manual: [Course element "LTI page" >](../../manual_user/learningresources/Course_Element_LTI_Page.md)

Admin manual: [LTI 1.3 Integrations at a glance >](../../manual_admin/administration/LTI_Integrations.md)

Admin manual: [LTI - External tools >](../../manual_admin/administration/LTI_External_tools.md)

Admin manual: [LTI - External platforms >](../../manual_admin/administration/LTI_External_platforms.md)

Admin manual: [LTI - Deep Linking](../../manual_admin/administration/LTI_Deeplinking.md)

Admin manual: [LTI - Role mapping](../../manual_admin/administration/LTI_Role_Mapping.md)
