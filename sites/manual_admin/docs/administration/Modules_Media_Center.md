# Module Media Center {: #module_media_center}

Administrators configure the Media Center in the System Administration under:<br>
`Administration > Modules > Media Center`

![All settings of the Media Center module on one page, opened via the highlighted entry Media Center in the Modules menu of the System Administration](assets/modules_media_center_admin_v2_de.png){ class="shadow lightbox" }

This module does not define the quota (storage space) of the Media Center itself. You set the quota in the System Administration under:<br>
`Administration > Core functions > Files and folders > Tab "Quotas"`

See also [Files and Folders](Files_and_Folders.md#files_and_folders_quotas).<br>
[To the top of the page ^](#module_media_center)

---

## Licences {: #licences}

If every new medium in the Media Center must carry licence information, make the licence a mandatory field here. To do so, activate the checkbox "Force license check on new files". It takes effect when the Media Center is selected under "Activate licenses in" in the System Administration under `Administration > Core functions > Licenses`.

[More on the usage of licences >](Licenses.md)<br>
[To the top of the page ^](#module_media_center)

---


## Taxonomy {: #taxonomy}

All contents of the media center can be assigned to a taxonomy (meta data). Since OpenOlat can manage multiple taxonomies at the same time, administrators define under "Linked taxonomies" which taxonomies are used in the media center.

You can find further information in the chapter [Taxonomy](../administration/Modules_Taxonomy.md).

[To the top of the page ^](#module_media_center)

---


## Shares [:octicons-tag-16:{ title="ab Release 18.1 (OO-7274)" }](https://track.frentix.com/issue/OO-7274) {: #shares}

If contents are deposited in the media center, they can be shared for others to use. Administrators define in the section "Shares" which sharing options are available to authors and other roles.

For "With user", "With group" and "With course" you choose "All" or "Specific roles" in each case. With "All", all users may share this way, even without an additional role. With "Specific roles", you select the roles author, learning resource manager and administrator individually. "With organisation" is only open to the roles learning resource manager and administrator, which you select there individually.

| My role           | If "With user"<br>is allowed by an admin | If "With course" <br>is allowed by an admin | If "With group" <br>is allowed by an admin | If "With organisation" <br>is allowed by an admin |
| ----------------- | ---------------------| ------ | ------ | ------------ |
| I am user (without additional roles)| I can give co-users access, when they belong to org units where they are authorised to use the media center. | I can give co-users access in all courses, where the co-user is an owner. | I can co-users of all groups give access, if the co-user is a group member. | media sharing is not possible |
| I am author       | I can give co-users access, when they belong to org units where they are authorised to use the media center. | I can give co-users access in all courses, where the co-user is an owner. | I can co-users of all groups give access, if the co-user is a group member. | media sharing is not possible |
| I am learning resource manager | I can give co-users access, when they belong to org units where they are authorised to use the media center. | I can give co-users access in all courses in org units, where the co-user is authorised to use the media center. | I can co-users of all groups give access, if the co-user is a group member. | I can give co-users access in all organisations where the co-user is authorised to use the media center. |
| I am administrator  | I can give co-users access, when they belong to org units where they are authorised to use the media center.| I can give co-users access in all courses in org units, where the co-user is authorised to use the media center. | I can co-users of all groups give access. | I can give co-users access in all organisations where the co-user is authorised to use the media center. |


[To the top of the page ^](#module_media_center)

---


## Further information {: #further_information}

[Files and Folders >](Files_and_Folders.md)<br>
[Licenses >](Licenses.md)<br>
[Module Taxonomy >](Modules_Taxonomy.md)<br>
[Media Center Concept >](../../manual_user/basic_concepts/Media_Center_Concept.md)<br>
[Personal tools: Media Center >](../../manual_user/personal_menu/Media_Center.md)<br>
[Configure user >](../usermanagement/Configure_User.md)

[To the top of the page ^](#module_media_center)

