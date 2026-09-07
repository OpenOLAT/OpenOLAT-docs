# Security Levels {: #security_levels}


## Which security levels are available? [:octicons-tag-16:{ title="from Release 18.1 (OO-7180)" }](https://track.frentix.com/issue/OO-7180) {: #levels}

[Passkey](Passkey.md) is part of a three-level security concept in OpenOlat:

**Level 1 - Password**: login with password only<br>
**Level 2 - Passkey**: login with passkey only<br>
**Level 3 - Password & Passkey (2FA)**: login with password and passkey (2-factor authentication)

In addition, the administration can activate the [One Time Code](One_Time_Code.md). Users without a stored passkey then confirm their login with a confirmation code sent by e-mail. [:octicons-tag-16:{ title="from Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509)


## Security levels set by administrators {: #admin_levels}

For some roles a higher security level makes sense, e.g. for user managers or administrators. In OpenOlat, a minimum required security level can therefore be set separately for each role. Administrators set the level per role in the system administration under:<br>
`Administration > Login > Password and authentication > Tab "Authentication"`

With the button "Set all roles at level…" one level is applied to all roles at once.

![Selection of the minimum level 1 to 3 per role and option to increase the security level independently, Passkey configuration in the system administration](assets/security_levels_v1_de.png){ class="shadow lightbox" }


## Change of a security level {: #change_level}

With the option "Increase security level independently", administrators can allow users to set their security level themselves.

The change is made with the button "Change security level" under:<br>
`Personal Menu > Password`

![Current security level 2 - Passkey, next to it the choice between level 3 and level 1 with the button Change security level, tab Password in the personal menu](assets/security_levels_user_settings_v1_de.png){ class="shadow lightbox" }

If a passkey is required for upgrading, users can generate the passkey themselves, also under `Personal Menu > Password`.

If users are allowed to change their security level themselves, upgrading and downgrading are possible in principle. Whether a downgrade is possible, however, depends on the default set by the administrators.

The minimum level is set by administrators. If, for example, level 2 is specified for the role of user manager, a user manager cannot downgrade to level 1 (password only), but can only choose between level 2 (passkey only) and level 3 (2-factor authentication).


## Further information {: #further_information}

[Passkey >](Passkey.md)<br>
[One Time Code >](One_Time_Code.md)

[To the top of the page ^](#security_levels)
