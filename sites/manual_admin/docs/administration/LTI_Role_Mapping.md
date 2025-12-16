# LTI - Role mapping {: #LTI_role_mapping}

:octicons-tag-24: Release 20.2


When configuring an LTI course element in the course editor, the author can specify which LTI roles are automatically
assigned to a user based on their role in the course. Typically, there are certain limitations as to which LTI roles
can be assigned to which course roles. 

In the example below, assigning the LTI role 'Administrator' to a course user with roles 'Author', 'Coach', or 
'Participant' is disabled:

![LTI_role_mapping_course_element_editor_admin_disabled_v1_en.png](assets/LTI_role_mapping_course_element_editor_admin_disabled_v1_en.png){ class="shadow lightbox" }

When OpenOlat establishes the connection to the LTI tool when running the course, OpenOlat automatically sends the LTI 
roles to the LTI tool, along with the user's email address, the deployment ID and other attributes.

The configuration tab 'Role mapping' in the LTI administration specifies which LTI roles a course owner is allowed to 
assign to the three course roles "Owner", "Coach" and "Participant" in the course editor: 

![LTI_role_mapping_admin_v1_en.png](assets/LTI_role_mapping_admin_v1_en.png){ class="shadow lightbox" }

The system uses default values similar to the ones in the screenshots above. These default values are stored in the
olat.properties file and do not need to be changed unless you want to apply other restrictions. The default values
in olat.properties are:

```
# LTI roles (capitalized) that can be assigned to users based on their OpenOlat roles in the course editor by the course owner.
lti13.roles.configurable.by.course.owner=LEARNER,INSTRUCTOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR

# The following is an exhaustive list of possible values for the field above:
lti13.roles.configurable.by.course.owner.values=LEARNER,INSTRUCTOR,ADMINISTRATOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR

# Default LTI roles for given OpenOlat roles in courses:
lti13.default.role.settings.for.owners=INSTRUCTOR,ADMINISTRATOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR
lti13.default.role.settings.for.coaches=INSTRUCTOR,TEACHING_ASSISTANT,MENTOR
lti13.default.role.settings.for.participants=LEARNER

# The following is an exhaustive list of possible values for the fields above:
lti13.default.role.settings.for.xxx.values=LEARNER,INSTRUCTOR,ADMINISTRATOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR
```

If you want to override the values in olat.properties, you can do so by editing the corresponding properties in the 
olat.local.properties file.

The settings in the olat.local.properties file override the default settings in olat.properties, and the 
settings in the OpenOlat administration override the settings in olat.local.properties.


## Further information {: #further_information}

IMS Global Learning Consortium: [Learning Tools Interoperability Core Specification](http://www.imsglobal.org/spec/lti/v1p3/)

Admin manual: [LTI 1.3 Integrations](../administration/LTI_Integrations.md)

Admin manual: [LTI - External tools](../administration/LTI_External_tools.md)

Admin manual: [LTI - External platforms](../administration/LTI_External_platforms.md)

Admin manual: [LTI - Deep Linking](../administration/LTI_Deeplinking.md)

User manual: [Configure LTI access to course](../../manual_user/learningresources/LTI_Share_courses.md)

User manual: [Course element "LTI Page"](../../manual_user/learningresources/Course_Element_LTI_Page.md)

User manual: [Configure LTI access to a group](../../manual_user/groups/LTI_Share_groups.md)