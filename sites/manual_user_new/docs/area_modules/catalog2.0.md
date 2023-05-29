# Catalog 2.0

:octicons-tag-24: Release 17.0

The catalog 2.0 is divided into different sections.

## Components of the catalog

## Start page

The home page is customizable by category launcher and offers a prominent search input field. Additionally, the background image can also be customized. The title is also customizable through an i18n. In the search can be

### Launcher

Launcher are the configurable lines of the start page. These can be added in the administration arbitrarily changed in the order. By default, a launcher of the type "Last added" is enabled. The launchers come in 3 types: Static Text, Static (Select Manually), Taxonomy Levels.
You can give all launchers a language dependent name. This name will then appear as a headline above the tiles.
Launchers can also be limited to one organisational unit.

### Taxonomy Launcher

Taxonomy launchers use the catalog subject structure to display the different tiers into sections.

### (Taxonomy) Microsite

Clicking on a level in a launcher takes you to the taxonomy microsite. All courses that have been classified under this level are displayed here. If the taxonomy has more than one level in this thread, the other levels will be displayed.

One can further refine the course list by filtering or searching.

### Search results page & filters

**Search results page**

A search brings you to this page. Here, using various filters, you can refine the search.

**Filter**

The filters of the search results page can be set under 'Administration > Modules > Catalog > Filters'. Here you can choose which filters should be available for participants. 

## Setting up and releasing new courses for the catalog 2.0

### Prerequisites

* Catalog 2.0 must be activated and a taxonomy should be created.
* At least 1 course must exist.

### Set up start page

The start page can be set up under 'Administration > Modules > Catalog > Start Page'. Here there is an option to add launcher on the top right to customize the start page.

### Add course to a subject area

On `Author Area > Course > Metadata` under "Subjects/Catalog" select the desired areas in which the catalog should appear and save.

### Create an Offer

Go to 'Authoring > Course > Release', activate 'Offer' and create an Offer. Release this for the desired organizational units.


## Migration from Catalog v1.0 to catalog v2.0

If there is already a catalog structure on your Instance, it can be easy migrated.
When you switch to the catalog v2.0 a new dialog will appear, prompting you to migrate the catalogstructure.

The following object are transfered to the new catalog:

* Title & Short Title
* Catalog images are converted. As a new image format, a rectangular display with the format 2:1 is recommended.
* Catalog structure is created as a new catalog taxonomy and is then available under Departments/Catalog.
* Subcategory titles, short titles & descriptions are available in redesigned subpages.