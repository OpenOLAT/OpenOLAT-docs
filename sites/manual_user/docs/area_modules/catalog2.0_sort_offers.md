# Catalog 2.0 - Sorting/order  {: #catalog_sort}

In Catalog 2.0, offers can be compiled manually or dynamically. If course owners have specified during configuration that they want their course to appear in the catalog, entries are dynamically added to the catalog.

This raises the question of where in the catalog the offers are displayed.

## Sorting/order on the catalog start page {: #sorting_startpage}

On the **home page** of the catalog, the order of the objects is determined by the launchers. The sections are referred to as launchers.

![Four numbered launchers determine the order on the catalog start page: welcome text, categories, popular courses, recently published resources](assets/catalog20_sort_offers_startpage_v1_de.png){ class="shadow lightbox" }

!!! info "How do I display my courses in the catalog?"
    Instructions on how to display courses in the catalog.<br>
    [How do I display my courses in the catalog? >](../../manual_how-to/catalog/catalog.md)


### Set the order of launchers {: #sorting_startpage_launcher}

The order of the launchers (sections on the start page) is defined under:<br>
`Administration > Module > Catalog > Tab "Start page"`

The order can be set by clicking on the double arrows at the beginning of the lines.

![Four launchers with double arrows in the Position column for re-ordering, Start page tab of the catalog module](assets/catalog20_sort_offers_startpage_launchers_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#catalog_sort)

---


### Sorting within the launcher {: #sorting_startpage_inside_launcher}

Within a launcher, the order of the offers depends on the launcher type:

!!! info "Launcher type"
    Configuration of launcher types in the administration.<br>
    [Launcher type >](../../manual_admin/administration/Modules_Catalog_2.0.md#tab_start_page)


**Launcher type "Static text":**<br>
There is no automatic sorting.

**Launcher type "Popular courses":**<br>
The order of the offers is determined by the number of clicks on course components during the last 28 days. 
Only courses with the status "Published" are taken into account.

**Launcher type "Last published":**<br>
The order of offers is determined by publishing date.

**Launcher type "Random":**<br>
Random order.

**Launcher type "Taxonomy level":**<br>
In a “Taxonomy Level” launcher, courses and learning resources are not displayed directly; rather, the taxonomy levels shown correspond to folders where the courses and learning resources can be found.<br> 
The offerings are automatically selected based on the taxonomy and then listed alphabetically on a microsite that opens when you click on one of the taxonomy levels in a taxonomy launcher.

**Launcher type "Selected learning resources":**<br>
The manually added learning resources can be sorted by clicking on the double arrows in front of the entries.  

**Launcher type "Selected implementations":**<br>
The manually added implementations can be sorted by clicking on the double arrows in front of the entries.

[To the top of the page ^](#catalog_sort)

---


### Set the order of subpages/categories {: #sorting_startpage_categories}

If a launcher is to display subcategories, a launcher of the "taxonomy level" type is used.

![Launcher Course offerings with nine category tiles as sub-pages, start page of the catalog](assets/catalog20_sort_offers_microsites_taxonomy1_v1_de.png){ class="shadow lightbox" }

The order of entries within the taxonomy launcher (order of subpages/categories in the catalog) is determined by the structure of the taxonomy and must therefore be changed via taxonomy.<br>
`Administration > Module > Taxonomy > Activation of a taxonomy for learning resources/catalog`

Example: Taxonomy structure for the taxonomy launcher displayed above: 
![Taxonomy levels of the catalog with the open row menu and the Edit option, Levels tab of the taxonomy](assets/catalog20_sort_offers_microsites_taxonomy2_v1_de.png){ class="shadow lightbox" }

* Select the option to edit a taxonomy level from the 3 dots. <br>
* In the "Metadata" tab, you will find the field for specifying the sorting order. 
* The number specified here for the taxonomy also determines the position within the launcher. (In the example shown above: 0 = 1. Subpage/Category, 1 = 2. Subpage/Category, 2 = 3. Subpage/Category => third in the catalog)

![The Sorting field with the value 2 determines the position of the sub-page, Metadata tab of a taxonomy level](assets/catalog20_sort_offers_microsites_taxonomy3_v1_de.png){ class="shadow lightbox" }

!!! note "Note"

    A change in the taxonomy structure not only affects the catalog, but also everywhere else where this taxonomy is used for selection. 


[To the top of the page ^](#catalog_sort)

---


## Sorting/order within categories (microsites) of the catalog {: #sorting_microsites}


### Choosing the sort order {: #sorting_microsites_button}

The sort button sits at the top right above the list of a category. It always carries the active criterion as its label, and the arrow symbol shows the direction. A click opens the list **"Sorted by"**.

![Sort button Relevance and the open Sorted by list with all criteria, table view of a catalog category](assets/catalog20_sort_offers_microsites_sort_button_v1_de.png){ class="shadow lightbox" }

"Relevance" is available as well as all sortable columns of the list, among them "Time period" and "Time period desc.".

!!! info "Important"
    The sort button only appears when "Sorting by priority" is activated. Without this setting the list is sorted by title in ascending order and can only be re-sorted through the column titles. The section [Sorting by priority](#sorting_microsites_by_priority) describes the activation.

!!! note "Module Time periods"
    The "Time period" column appears in the list as soon as the system administration has switched on the "Time periods" module.<br>
    [Module Time periods >](../../manual_admin/administration/Modules_Time_Period.md)

[To the top of the page ^](#catalog_sort)

---


### Sorting through the column titles [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9218)" }](https://track.frentix.com/issue/OO-9218){:target="_blank"} {: #sorting_microsites_lists}

As with all lists in OpenOlat, the offerings in the catalog can also be sorted by **clicking on a column title**.

!!! note "Note"
    The "Time period" column sorts chronologically by the time frame and not alphabetically by the short label: first by the begin date, then by the end date, and finally by the title. Entries without a time period always appear at the end of the list.

    The "Time period desc." criterion sorts alphabetically by the description. Entries without a description appear at the end of the list.

[To the top of the page ^](#catalog_sort)

---


### Sorting by priority [:octicons-tag-16:{ title="from Release 20.2.0 (OO-9039)" }](https://track.frentix.com/issue/OO-9039){:target="_blank"} {: #sorting_microsites_by_priority}

An administrator activates "Sorting by priority" in the system administration under:<br>
`Administration > Modules > Catalog > "Settings" tab > "Sorting by priority" toggle button`

The sort button then appears at the top right above a list. Its default criterion is "Relevance".

![Sort button with the default criterion Relevance above an offer list, tile view of a catalog category](assets/catalog20_sort_offers_microsites_button_relevance_v1_de.png){ class="shadow lightbox" }

When "Sort by Priority" is selected, a multi-stage sorting process takes place:<br>
1. Criterion: Sorting by priority<br>
2. Criterion: Sorting by start date<br>
3. Criterion: Sorting by end date<br>
4. Criterion: Sorting by title (alphabetically)

If no date is specified, entries without a date are displayed after those with a date.

[To the top of the page ^](#catalog_sort)

---


### Where can I set priorities? {: #sorting_microsites_define_priority}

**In a course:**<br>
`Course > Administration > Settings > section "Offer Overview" > click on "change"`

**In Course Planner:**<br>
`Course Planner > Implementation > tab Catalog > button "Offers" > section "Offer Overview" > click on "change"`

Example Course Planner:
![Row Catalog priority for sorting with the adjust link, Catalog tab of an implementation in the Course Planner](assets/catalog20_sort_offers_microsites_cp_change_priority_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#catalog_sort)

---


### What priorities can be set? {: #sorting_microsites_priorities}

As a priority, you can select a preset boost value or enter your own boost value. The higher the boost value, the further up an offer will appear in the catalog. With your own user-defined boost values, you can fine-tune the display order.

- normal (boost value 0)
- medium (boost value 1000)
- high (boost value 2000)
- very high (boost value 3000)
- ultimative (boost value 4000)
- custom (define your own boost value)

![Priority selection High with the corresponding boost value 2000, dialog Adjust priority](assets/catalog20_sort_offers_microsites_boost_v1_de.png){ class="shadow lightbox" }

!!! note "Note"

    Sorting by priority does not affect the sorting on the start page. There, the order of the offers is determined by the respective launcher types and the manual arrangement in the administration.




[To the top of the page ^](#catalog_sort)

---


## Further information {: #further_information}

[How do I present my courses in the OpenOlat catalog? >](../../manual_how-to/catalog/catalog.md)<br>
[Offers >](../../manual_user/area_modules/catalog2.0_angebote.md)<br>
[Design >](../../manual_user/area_modules/catalog2.0_design.md)<br>
[External catalog >](../../manual_user/area_modules/catalog2.0_web.md)<br>
[Activate priorities in administration >](../../manual_admin/administration/Modules_Catalog_2.0.md)<br>
[Module Time periods >](../../manual_admin/administration/Modules_Time_Period.md)

[To the top of the page ^](#catalog_sort)


