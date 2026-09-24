# Module Instant Messaging {: #instant_messaging}

With Instant Messaging you enable the "chat" and "messaging" features and
define who can contact whom. You find these settings in the system
administration under:<br>
`Administration > Modules > Instant Messaging`

Administrators and system administrators have access to the system
administration. How roles are assigned is described in
[Assign roles](../usermanagement/Assign_roles.md).

### Instant-Messaging module [:octicons-tag-16:{ title="from Release 8.4 (OO-448)" }](https://track.frentix.com/issue/OO-448) {: #im_module }

Here you decide whether chat and messaging are available in OpenOlat at all.

#### Enable chat and messaging {: #enable_chat }

With this setting you enable and disable the entire Instant Messaging
functionality. If it is disabled, chat and messaging are turned off, and none
of the other settings on this page can be edited.

### Chat room configuration {: #chat_rooms }

Here you define whether groups and courses can get their own chat room, in
which all members exchange messages together.

#### Chat as group tool {: #chat_group_tool }

If this setting is enabled, group coaches can configure a chat room for each
group. With "Allow anonymous participation", the members may write in the chat
room without showing their real name. With "Anonym by default", they enter the
chat room anonymously and show their real name themselves if needed. "Anonym by
default" can only be selected if "Allow anonymous participation" is enabled.

#### Chat as course tool {: #chat_course_tool }

If this setting is enabled, course owners can configure a chat room in each
course. The two settings "Allow anonymous participation" and "Anonym by
default" work in the course the same way as in the group.

### Instant messages to single users {: #direct_messages }

Here you define whom users can contact directly, what they see of the status
of others and with which default values new users start.

#### All users can be contacted {: #all_users_contactable }

With this setting you allow chatting and sending messages between all users.
If it is enabled, the visiting card shows a link below the profile image, via
which a message can be sent. Users can override this setting individually with
their personal configuration.

#### Show group peers {: #show_group_contacts }

With this setting you allow chatting and sending messages between group
participants. If it is enabled, the list of all group members of the groups
one is a member of appears. These persons can be selected directly for a chat
or a message. In addition, the group must allow the display of its members:<br>
[Group Administration, Tab Members](../../manual_user/groups/Group_Administration.md#members)

#### Show online status {: #show_online_status }

With this setting you choose whether users see the current online status of
other users or group participants. If it is disabled, a speech bubble appears
instead of the status icon. Users then do not know whether their message can
be sent immediately.

#### Default status for new users [:octicons-tag-16:{ title="from Release 21.0 (OO-9466)" }](https://track.frentix.com/issue/OO-9466) {: #default_status }

With this setting you define the online status new users start with. The
options are "Available", "Please do not disturb" and "Not available". The
default is "Available".

#### Receive messages from all users by default {: #receive_messages_default }

With this setting you define whether the personal setting "Receive messages
from all users" is enabled for new users. By default it is enabled.

OpenOlat applies the two default values to a person's personal settings for
chat and messaging at their first login with Instant Messaging enabled. A later
change of the default values therefore only applies to persons for whom no
personal settings have been saved yet. After that, each person can adjust
their settings themselves:<br>
[Personal Configuration: Settings](../../manual_user/personal_menu/Settings.md)

More information about the usage of the Instant-Messaging module can be found
here: [Chat](../../manual_user/basic_concepts/Chat.md)

## Further information {: #further_information}

[Assign roles >](../usermanagement/Assign_roles.md)<br>
[Group Administration >](../../manual_user/groups/Group_Administration.md)<br>
[Personal Configuration: Settings >](../../manual_user/personal_menu/Settings.md)<br>
[Chat >](../../manual_user/basic_concepts/Chat.md)<br>
[Using Group Tools >](../../manual_user/groups/Using_Group_Tools.md)<br>
[Course Settings - Tab Toolbar >](../../manual_user/learningresources/Course_Settings_Toolbar.md)

[To the top of the page ^](#instant_messaging)
