# External available catalog) {: #web_catalog}


## Situation without external Catalog {: #without_web_catalog}

Courses are created in OpenOlat and can be offered in the catalog. Participants must be registered in OpenOlat in order to be able to give feedback to participants when attending courses or to save test results, certificates etc. Only then can the results be saved.

Therefore, a user must be created in OpenOlat (registration process).
You also have to be registered without the external catalog in order to browse through the catalog. This was often perceived as an obstacle, which is why an externally usable catalog was implemented in Release 20.


## Situation with external Catalog {: #with_web_catalog}

As of Release 20, offers can be stored in OpenOlat that are displayed in an external catalog. "External" means that the catalog is mirrored outside the "registration wall" and can be accessed there without registration. The initial version of the catalog (within the "registration wall"), which can only be accessed by registered users, must be a catalog V2. A catalog V1 cannot be displayed as an external catalog.

The prices and the number of places available in a course can also be seen in the external catalog.

Users can then select and book these courses. They will only be guided through the registration process once they have made their choice (in order to be able to save work results).

For users already registered in OpenOlat, the booking is assigned to their existing account. The booking is then confirmed.


## Accessing the external catalog {: #web_catalog_access}

The external catalog can be offered on the login screen from Release 20. (The external catalog and the display of the button must be set up in the administration).

![catalog20_webcatalog_login_v1_de.png](assets/catalog20_webcatalog_login_v1_de.png){ class="shadow lightbox" }

The link to the external catalog can also be integrated elsewhere in a website.

[Direct links to an offer](#web_catalog_direct_link) can also be sent.


[To the top of the page ^](#web_catalog)

---


## Create offers in the external catalog {: #web_catalog_offers}

In order for a course to be advertised in the external catalog or in the internal catalog, an offer must be created under: **(Course) Administration > Settings > Tab "Share"**<br>

Before a new offer can be created, two requirements must be met.

![1_green_24.png](assets/1_green_24.png) In the section "Usage" the option "Standalone" must be selected.

![2_green_24.png](assets/2_green_24.png) In the "Share" section, the option "Bookable and open offers" must be selected as "Access for participants".

An offer can then be drawn up. ![3_green_24.png](assets/3_green_24.png) 

![catalog20_webcatalog_offer1_v1_de.png](assets/catalog20_webcatalog_offer1_v1_de.png){ class="shadow lightbox" }


If you now select one of the offer types, you can also specify whether the offer should be published in the external catalog. <br>
If the offer should be the same for internal and external catalogs, check both boxes.<br>
If there are to be differences between the internal and external catalog (e.g. internal free of charge - external chargeable), create 2 different offers.

![catalog20_webcatalog_offer2_v1_de.png](assets/catalog20_webcatalog_offer2_v1_de.png){ class="shadow lightbox" }


!!! hint "Note"

    Courses created with the Course Planner can also be offered in the external catalog. In this case, the option "Integration in product" is selected for the course under **Settings > "Share" tab > "Usage"** section and no offer can be created in the course itself.

    More about offers of implementations can be found [here](../../manual_user/area_modules/Course_Planner_Implementations.md#tab_catalog)


### Direct link to an offer {: #web_catalog_direct_link}

If you want to send a direct link to a specific offer, e.g. by e-mail (external or internal catalog), you will find the links in the overview of offers.

**Example: Links to an offer for an implementation**

![catalog20_webcatalog_offer_link_v1_de.png](assets/catalog20_webcatalog_offer_link_v1_de.png){ class="shadow lightbox" }


[To the top of the page ^](#web_catalog)

---


## Further information {: #further_information}

[Set up external catalog (admin manual) >](../../manual_admin/administration/Modules_Catalog_2.0.md)<br>
