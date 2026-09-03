# Externally available catalog {: #web_catalog}


## Situation without external catalog {: #without_web_catalog}

Courses are created in OpenOlat and can be offered in the catalog. In order to give participants feedback when attending courses or to save test results, certificates etc., the participants must be registered in OpenOlat. Only then can the results be saved.

Therefore, a user must be created in OpenOlat (registration process).
Without the external catalog, you also have to be registered in order to browse through the catalog.


## Situation with external catalog [:octicons-tag-16:{ title="from Release 20.0 (OO-8002)" }](https://track.frentix.com/issue/OO-8002) {: #with_web_catalog}

Offers can be stored in OpenOlat that are displayed in an external catalog. "External" means that the catalog is mirrored outside the "registration wall" and can be accessed there without registration. The initial version of the catalog (within the "registration wall"), which can only be accessed by registered users, must be a Catalog 2.0. A Catalog 1.0 cannot be displayed as an external catalog.

The prices and the number of places available in a course are also visible in the external catalog.

Users can then select and book these courses. They are only guided through the registration process once they have made their choice (in order to be able to save work results).

For users already registered in OpenOlat, the booking is assigned to their existing account. The booking is then confirmed.


## Accessing the external catalog {: #web_catalog_access}

The external catalog can be offered on the login screen. The external catalog and the display of the button are set up in the system administration: `Administration > Modules > Catalog > Tab "Settings"`.

![Section Catalog with the button Explore our offers below the guest access, login page of OpenOlat](assets/catalog20_webcatalog_login_v1_de.png){ class="shadow lightbox" }

The link to the external catalog can also be integrated elsewhere in a website.

[Direct links to an offer](#web_catalog_direct_link) can also be sent.

[To the top of the page ^](#web_catalog)


---

## Create offers for the external catalog {: #web_catalog_offers}

In order for a course to be advertised in the external catalog or in the internal catalog, an offer must be created under:<br>
`Course > Administration > Settings > Tab "Share"`

Before a new offer can be created, two requirements must be met.

![1](assets/1_green_24.png) In the section "Usage" the option "Standalone" must be selected.

![2](assets/2_green_24.png) In the "Share" section, the option "Bookable and open offers" must be selected as "Access for participants".

An offer can then be created. ![3](assets/3_green_24.png)

![Three highlighted steps: usage Standalone, access Bookable and open offers and the button Add offer with the four offer types, Share tab of the course settings](assets/catalog20_webcatalog_offer1_v1_de.png){ class="shadow lightbox" }


If you now select one of the offer types, you can also specify whether the offer should be published in the external catalog.<br>
If the offer should be the same for the internal and external catalog, tick both boxes.<br>
If there are to be differences between the internal and external catalog (e.g. internal free of charge, external chargeable), create two different offers.

![Checkboxes Internal catalog and External catalog under Published in highlighted, dialog PayPal Checkout for a new offer](assets/catalog20_webcatalog_offer2_v1_de.png){ class="shadow lightbox" }


!!! note "Note"

    Implementations created with the Course Planner can also be offered in the external catalog. In this case, the option "Use in Course Planner" is selected for the course under `Course > Administration > Settings > Tab "Share" > Section "Usage"` and no offer can be created in the course itself.

    More about offers of implementations can be found [here](Course_Planner_Implementations.md#tab_catalog).


### Direct link to an offer {: #web_catalog_direct_link}

If you want to send a direct link to a specific offer, e.g. by e-mail (external or internal catalog), you will find the links in the overview of the offers.

**Example: Links to the offer of an implementation**

![Link Links in the row Access of the offer overview opens the dialog with one link each for the external and the internal catalog, Catalog tab of an implementation](assets/catalog20_webcatalog_offer_link_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#web_catalog)

---


## Further information {: #further_information}

[Course Planner: Implementations >](Course_Planner_Implementations.md)<br>
[Set up external catalog (administration manual) >](../../manual_admin/administration/Modules_Catalog_2.0.md)

[To the top of the page ^](#web_catalog)
