# LTI - External tools

:octicons-tag-24: Release 15.5


## OpenOlat as a platform

If OpenOlat is used as a "platform" in the sense of LTI terminology, courses from other LMSs or other applications (tools) are displayed on OpenOlat. Typically, the LTI course element can be used in OpenOlat for this purpose.

Administrators must always enable (activate) the integration of external tools ("Configuration" tab).

The communication and secure connection to this tool must then be set up via the configuration in the "External tools" tab.

![LTI_admin_config_v1_de.png](assets/LTI_admin_tools_v1_de.png){ class="shadow lightbox" }

**Examples for external Tools:**

* Online courses from different providers
* Simulations, e.g. ...
* Flashcards, e.g. ...
* Apps, e.g. ...
* Interactive practice, e.g. ...
* Games, e.g. ...

A separate configuration must be set up for each external tool. Use the "Add new tool" button to create the connection to a new tool.

!!! info "Note"

	If an external tool is used in several different OpenOlat courses, it is sufficient to configure the external tool only once at administrator level. The further configuration per course is then carried out by the course owner in the settings of the respective course <br> (Course administration > Settings > Tab page content)

## Configuration

You can find a sample of an entire configuration under [Configuring LTI access to a course](../../manual_user/learningresources/LTI_Share_courses.md)

In OpenOlat, the following parameters of the external partner instance are entered under "Add new tool":

| Field					| Comment |
| --------------------- | ---------------------------------------------- |
| Name of Tools		| Freely definable |
| Tool URL				| URL to external tool |
| Client-ID				| Client ID from the "Platform configuration details" dialog of the external tool |
| Public key type | RSA key |
| Public key |  |
| URL the authentication request	| From the external instance |
| Redirect URL(s) 	|  |


![LTI_admin_tool_config_v1_de.png](assets/LTI_admin_tool_config_v1_de.png){ class="lightbox" }



## Links

IMS Global Learning Consortium: [Learning Tools Interoperability Core Specification](http://www.imsglobal.org/spec/lti/v1p3/)

Admin manual: [LTI 1.3 Integrations](../administration/LTI_Integrations.md)

Admin manual: [LTI - External platforms](../administration/LTI_External_platforms.md)

User manual: [Configure LTI access to course](../../manual_user/learningresources/LTI_Share_courses.md)

User manual: [Course element "LTI Page"](../../manual_user/learningresources/Course_Element_LTI_Page.md)

User manual: [Configure LTI access to a group](../../manual_user/groups/LTI_Share_groups.md)

User manual: [LTI Deep Linking](../administration/LTI_Deeplinking.de.md)


