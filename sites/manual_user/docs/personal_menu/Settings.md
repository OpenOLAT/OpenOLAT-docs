# :o_icon_o_icon_settings: Personal Configuration: Settings {: #personal_configuration_settings}

![Entry System settings in the section Configuration of the personal menu, between the entries Profile and Password](assets/pers_menu_settings_v1_de.png){ class="aside-right lightbox"}

:octicons-device-camera-video-24: **Video Introduction (German)**: [User settings](<https://www.youtube.com/embed/7osBJ99FIN8>){:target="_blank"}

The settings allow you to adapt OpenOlat according to your needs.


## Tab System {: #tab_system}

![Four numbered sections of the tab System, from the general system settings to the reset of the configurations, in the personal settings](assets/pers_menu_settings_tab_system_v1_de.png){ class="shadow lightbox" }


### ![1](assets/1_green_24.png) General system settings {: #general}

Here you see your username and your OpenOlat roles. You can also select your individual system language. OpenOlat has been translated into numerous languages. Changing the language only becomes active after the next login.

!!! info "Important"

    The language of course content is not affected by the language selection here.

You can also set how often you want to receive e-mail notifications. You can choose between: never, monthly, weekly, daily, every six hours, every four hours and every two hours. You can also specify whether OpenOlat e-mails are only displayed in the inbox within the OpenOlat system or whether they are also sent to the external e-mail address configured in your profile. In the notification mail, you also find a note regarding new e-mails within the OpenOlat inbox, if you have selected the option "Send e-mails to the OpenOlat internal inbox".

Via the "Character set used in download" you determine in which character set files that you download via data archiving are stored. This concerns the download of test and questionnaire results as well as course results. By default, the character set UTF-8 is preset. If your tests or questionnaires contain e.g. Arabic characters, UTF-8 must be selected here.


### ![2](assets/2_green_24.png) Specific system settings {: #special}

In the specific system settings, you view and change the settings that can make it easier for you to get started and work with OpenOlat on a daily basis.

**Resume last session**<br>
In the selection "Resume last session" you specify what happens immediately after login:

  * "No": The landing page is loaded.
  * "Yes, automatically": OpenOlat loads the location last visited.
  * "Yes, on request": You decide after each login where you want to go.


**Landing page**<br>
If you have selected the setting "Yes, automatically", the field "Landing page" is hidden. This field allows you to set any page within OpenOlat as your personal landing page, thereby overriding the system-wide landing page.

You find page-specific links in the social sharing bar at the bottom left under "Copy link". It is even easier to click the landing page icon on the desired page. Any OpenOlat page you have access to can be selected as your personal landing page this way.

**Landing page icon in the footer:**
![Landing page icon in the footer marked with an arrow, below it the tooltip Set current page as personal start page in profile](assets/pers_menu_settings_tab_system_pers_startpage_v1_de.png){ class="shadow lightbox" }


### ![3](assets/3_green_24.png) User tools {: #personal_tools}

Here you select which personal tools appear directly at the top of the menu bar (to the left of your profile picture) so that you can access these tools quickly.<br>
Tools that are displayed in the quick access are no longer listed in the personal menu.

**Example: "System settings" and "Badges" have been moved from the personal menu to the quick access**
![Check boxes System settings and Badges marked in the section User tools, their icons appear in the header and are missing in the opened personal menu](assets/pers_menu_settings_tab_system_pers_tools_v1_de.png){ class="shadow lightbox" }

!!! tip "Tip"

    Do not try to enable all the tools; instead, select only the ones you use frequently. This keeps the menu bar uncluttered.


### ![4](assets/4_green_24.png) Reset configurations {: #reset}

Under "Reset configurations" in the tab "System" you can **reset** any system-related changes you have made **back to their default settings**. The following can be reset:

* the personalized interface components (menu, tool boxes, tables, portal, calendar, etc.),
* system configuration (notifications, e-mail, character set, etc.)
* as well as the settings for resuming the last session.

After the reset you are automatically logged out of OpenOlat.

[To the top of the page ^](#personal_configuration_settings)

---


## Tab WebDAV {: #webdav}

In the tab "WebDAV" you find the [WebDAV link to your OpenOlat instance](../basic_concepts/Using_WebDAV.md), which you can use to conveniently manage files. Via WebDAV you access your personal folder as an OpenOlat user. OpenOlat authors can organize their entire course files via WebDAV.

Under "Access data" you see your WebDAV username. With "Set password" you define a separate WebDAV password.

![WebDAV address of the instance and below it the access data with WebDAV username, WebDAV password not set and button Set password, tab WebDAV of the personal settings](assets/pers_menu_settings_tab_webdav_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#personal_configuration_settings)

---


## Tab Instant Messaging {: #tab_instant-messaging}

In the tab "Instant Messaging" you define the settings for the [chat function](../../manual_admin/administration/Instant_Messaging.md) and your communication status after login. With the option "Receive messages from all users" you specify whether all users may send you messages. Under "Default status after login" you choose between "Available", "Please do not disturb" and "Not available".

![Option Receive messages from all users and the three statuses Available, Please do not disturb and Not available, tab Instant Messaging of the personal settings](assets/pers_menu_settings_tab_instant-messaging_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#personal_configuration_settings)

---


## Tab Terms of use {: #tab_terms_of_use}

Here you can read the terms of use, which you confirmed the first time you logged in. The exact terms of use are determined by the OpenOlat administrators.

Furthermore you can request the deletion of your complete OpenOlat account here. The request is sent as an email to an address configured by the system administration; the deletion itself is carried out by the user management. More about this: [Data protection](../../manual_admin/usermanagement/Data_protection.md#request_account_deletion)

![Text of the terms of use with the date of consent, button Ask to delete your account and three confirmed check boxes, tab Terms of use of the personal settings](assets/Nutzungsbedingungen_20.png){ class="shadow lightbox" }

[To the top of the page ^](#personal_configuration_settings)

---


## Tab User data {: #tab_user_data}

In this section, you can request an overview of your data stored in OpenOlat from the operator in accordance with Article 15 of the GDPR. The relevant support link is provided here.

Once the export is complete, you can obtain the user data stored about you here with the **Download the data** button. The file stays available for one month, after that a new export is required.

How the export is triggered and who is allowed to do so is described on the page [Data protection](../../manual_admin/usermanagement/Data_protection.md#export_user_data) in the administration manual.

[To the top of the page ^](#personal_configuration_settings)

---


## Tab GUI preferences {: #tab_GUI}

The GUI (Graphical User Interface) settings are stored in variables. Experts can use this tab to reset specific variable values.

![Table of the stored GUI variables with the columns Assigned class and Key and one button Reset per row, tab GUI preferences of the personal settings](assets/pers_menu_settings_tab_GUI_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#personal_configuration_settings)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Using WebDAV >](../basic_concepts/Using_WebDAV.md)<br>
[Module Instant Messaging >](../../manual_admin/administration/Instant_Messaging.md)<br>
[Data protection >](../../manual_admin/usermanagement/Data_protection.md)

**Further reading**<br>
[Personal Configuration: Profile >](Profile.md)<br>
[Personal Configuration: Password >](Password.md)<br>
[Personal tools >](Personal_Tools.md)<br>
[Personal tools: E-Mail >](E-Mail.md)<br>
[Landing pages >](../../manual_admin/administration/Landing_pages.md)<br>
[Chat >](../basic_concepts/Chat.md)

**youtube**<br>
[User settings (German)](<https://www.youtube.com/embed/7osBJ99FIN8>){:target="_blank"}

[To the top of the page ^](#personal_configuration_settings)
