# LTI - Deep Linking {: #LTI_deeplinking}


OpenOlat supports deep linking according to the [LTI 1.3 Deep Linking Protocol](https://www.imsglobal.org/spec/lti-dl/v2p0).

## Functional description

Deep linking is an LTI 1.3 service that enables authors to guide course participants directly to a specific point in external content that is integrated via LTI.

**Example:**<br>
Instead of providing a link to a book in the course element and letting learners search for a recommended chapter themselves (scrolling), a specific chapter can be displayed directly.

The deep linking function can be activated by the administrator of the OpenOlat instance so that the OpenOlat authors can enable the deep links to the external tool in the course elements without having to repeatedly provide information on registration and parameter transfer. This simplifies the work of the authors when configuring an LTI course element.

## Available features

Various information about the course and course participants can be exchanged between OpenOlat and the integrated tool. In OpenOlat this includes:

* Content Types
* ResourceLink
* Link
* Image
* File
* HTML
* Properties
* type
* url
* title
* text
* thumbnail
* window
* iframe


## Configuration

### Global configuration

If an LTI tool is set up by administrators at a global level, an option for Deep Links can also be activated. Activation means that all settings made for the tool (enabling use without having to log in again separately) also apply to deep links that course authors specify in the LTI course element.

**Administration > External Tools > LTI 1.3 > Tab "External Tools" > Button "Edit" > Toggle-Button "Activate Deep Linking"**

![LTI_admin_deeplinking_activate_v1_de.png](assets/LTI_admin_deeplinking_activate_v1_de.png){ class=" shadow lightbox" }  

### Configuration in courses

If deep linking has been permitted for authors, they can select preconfigured links under "LTI versions" when configuring the LTI course element.

If one of the pre-configurations is selected, the required URL is entered immediately and the author no longer has to worry about it.

![LTI_page_content_version_v1_de.png](assets/LTI_page_content_version_v1_de.png){ class=" shadow lightbox" }  

![LTI_page_content_version_select_v1_de.png](assets/LTI_page_content_version_select_v1_de.png){ class=" shadow lightbox" } 


The Client ID and Deployment ID parameters generated in the process can then be used to complete the process on the integrated tool side.

!!! note "Note"

    In order for the deployment ID to be generated, a change in the Page content tab must first be saved. (Especially if a preconfigured link has been selected under "LTI versions".)



### Page view

If the external content is to be started immediately in the course element "LTI page", the option "Start content automatically" must be selected in the "Page content" tab in the course editor. Otherwise, a button appears with which the learner must explicitly start the integrated page.

![LTI_page_content_launch_v1_de.png](assets/LTI_page_content_launch_v1_de.png){ class=" shadow lightbox" } 


## Further information {: #further_information}

IMS Global Learning Consortium: [Learning Tools Interoperability Core Specification](http://www.imsglobal.org/spec/lti/v1p3/)

IMS Global Learning Consortium: [LTI 1.3 Deep-Linking protocol](https://www.imsglobal.org/spec/lti-dl/v2p0)

Admin manual: [LTI 1.3 Integrations](../administration/LTI_Integrations.md)

Admin manual: [LTI - External tools](../administration/LTI_External_tools.md)

Admin manual: [LTI - External platforms](../administration/LTI_External_platforms.md)

Admin manual: [LTI - Role mapping](../administration/LTI_Role_Mapping.md)

User manual: [Configure LTI access to a course](../../manual_user/learningresources/LTI_Share_courses.md)

User manual: [Course element "LTI Page"](../../manual_user/learningresources/Course_Element_LTI_Page.md)

User manual: [Configure LTI access to a group](../../manual_user/groups/LTI_Share_groups.md)



