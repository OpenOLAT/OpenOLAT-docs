# Customizing: Overview {: #customizing}

In the "Customizing" menu, administrators and system administrators adapt the appearance and the main navigation of the whole instance. You will find these settings in the system administration under:<br>
`Administration > Customizing`

## Profile

Name | Customizing
---------|----------
Available since | Release 8.0 (2011)

---

## Representation, layout {: #layout}

![Layout page in the Customizing menu: system layout as a selection list, logo upload with target URL and alternative text, footer line with target URL and text](assets/admin_customizing_layout_v1_en.png){ class="shadow lightbox" }

### Section Layout

The system layout, a company logo and properties relating to the footer can be stored here.

The background image of the login page is part of the layout theme and cannot be configured in the system administration. It is customized through an individual theme. For hosted instances, please contact your provider.

### Company or Institution Logo Section [:octicons-tag-16:{ title="from Release 10.0 (OO-1167)" }](https://track.frentix.com/issue/OO-1167){:target="_blank"}

You can upload your own logo (PNG file), which will then appear in the top-left corner of the header. Please note that this logo will be used within the theme (overall layout). The OpenOlat logo is displayed by default.

You also define where a click on the logo leads: to the landing page or to a target URL of your choice. In the field for the alternative text, you enter the text that appears in place of the logo.

### Footer Properties Section

In this section, you define the text of the footer in the bottom-right corner and the target URL that a click on the footer leads to. Email and web addresses in the text are automatically converted into a clickable link.

[To the top of the page ^](#customizing)


## Imprint [:octicons-tag-16:{ title="from Release 10.0 (OO-1166)" }](https://track.frentix.com/issue/OO-1166){:target="_blank"} {: #imprint}

Administrators determine,

* where the link to the legal notice appears (e.g., in the footer)
* whether a legal notice appears and what it says
* whether a text regarding the terms of use appears in the legal notice and what that text says
* whether a privacy policy appears within the legal notice and what the text says
* whether a contact form for general inquiries should be displayed and, if so, to whom the inquiry will be sent

All text can be entered in different languages.

![Imprint page in the Customizing menu: once switched on and set to position Footer, the imprint appears as a link in the footer line, and the three texts are maintained per language](assets/admin_customizing_imprint_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#customizing)


## Help [:octicons-tag-16:{ title="from Release 15.1 (OO-4562)" }](https://track.frentix.com/issue/OO-4562){:target="_blank"} {: #help}

Here you can specify which help pages are displayed via the help icon :fontawesome-solid-circle-question: in the main menu. You can also include a link to the support contact form.

![Edit help option dialog on the Help page: type, name per language, symbol and URL, plus the display locations authoring, user tools and login](assets/Hilfemoeglichkeiten.png){ class="shadow lightbox" }

[To the top of the page ^](#customizing)


## Language adaptation tool {: #language_adaption_tool}

Individual text elements can be adjusted here if required.

[To the top of the page ^](#customizing)


## System registration {: #system_registration}

OpenOlat is open source and needs an active community of users. You too can be part of this community.

[To the top of the page ^](#customizing)



## Portal {: #portal}

Various portlets can be selected for the "Portal" tab.

!!! tip "Tip"
    We recommend not using this feature. It has been superseded by numerous modules in OpenOlat and is thus a historical remnant that nevertheless cannot simply be switched off. Thank you for your understanding.

[To the top of the page ^](#customizing)


## User properties {: #user_properties}

Administrators can use this feature to select the attributes displayed in user management and group them.
In addition, the translations can be edited.

[To the top of the page ^](#customizing)


## Sites {: #sites}

On the "Sites" page, administrators define which sites the main navigation in the top row offers, in which order and for which roles. You will find the page in the system administration under:<br>
`Administration > Customizing > Sites`

What a site is and what decides whether a person sees it is explained in the user manual on the page [Area and modules](../../manual_user/area_modules/index.md#conditions).

### Tab Order

In the "Order" tab, you enable the sites for the whole instance and arrange them. The "Enabled" checkbox enables a site, and the "Up" and "Down" arrows set the order. Some entries in the list are named differently from the site in the main navigation. The entry "My courses" appears there as "Courses".

The "Coaching tool" entry cannot be deactivated, because coaches and owners reach their learning resources through Coaching. The "Enabled" checkbox is greyed out. Order and access remain adjustable. [:octicons-tag-16:{ title="from Release 21.0.1 (OO-9661)" }](https://track.frentix.com/issue/OO-9661)

The list applies to the whole instance. Three further points decide together whether a person sees a site.

**The module must be active.** An entry only appears if the corresponding module is switched on as well. An activated "Catalog" entry has no effect as long as the [Module Catalog](Modules_Catalog_2.0.md) is switched off. While a module is switched off, the "Enabled" checkbox of its entry is greyed out.

**The "Access" column decides per role.** It determines which roles see the site, for example "Registered users without guests/external users" or "Learning resource managers and authors only". Two people with different roles therefore see a different main navigation.

**The space in the bar decides the presentation.** Sites that no longer fit into the top row are collected by OpenOlat in the "More" menu on the right. This depends on the screen width of the viewer and cannot be configured.


### Other tabs [:octicons-tag-16:{ title="from Release 9.1 (OO-715)" }](https://track.frentix.com/issue/OO-715){:target="_blank"}

In the tabs "Info page n°1" to "Info page n°4", you add one course each as a separate site to the main navigation, for example for information addressed to all people of the instance.

For each language you store a separate title and a separate learning resource. With "Choose" you open the search for the referenceable learning resource. Only there do you connect the site with a course. The "Default" checkbox determines the entry that applies when no entry is stored for the language of a person.

In the "Icon CSS Class" field, you set the symbol of the site. With the "Show toolbar for all users" checkbox, all people see the toolbar of the course. Without a checkmark, only people who may manage the course see it, for example owners.

![Select the course from the list, or use Create and Import file to add a new learning resource instead, in the Search for referenceable learning resources dialog](assets/admin_customizing_infopage_select_v1_en.png){ class="shadow lightbox" }

In the tabs "External page n°1" and "External page n°2", you add an external URL with its own title per language as a site. [:octicons-tag-16:{ title="from Release 18.2 (OO-7398)" }](https://track.frentix.com/issue/OO-7398)

[To the top of the page ^](#customizing)



## Further information {: #further_information}

**Mentioned on this page**<br>
[Area and modules >](../../manual_user/area_modules/index.md)<br>
[Module Catalog >](Modules_Catalog_2.0.md)

**Further reading**<br>
[Modules: Overview >](Modules.md)<br>
[Landing pages >](Landing_pages.md)<br>
[Navigation >](../../manual_user/basic_concepts/Navigation.md)

[To the top of the page ^](#customizing)