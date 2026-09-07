# Global search {: #search_global}

You will find the global search in the top right-hand corner of the header. Click on the magnifying glass icon.

If you enter a search term here and confirm it by pressing the Enter key or clicking on the magnifying glass next to it, a **search across everything** takes place.

This means that the **entire OpenOlat** is searched, including the content of documents. It is a [full-text search](Search_General.md#full_text_search).

![Expanded search field of the global search with the button Search next to the magnifying glass icon in the top right-hand corner of the header](assets/search_global_v1_de.png){ class="shadow lightbox" }


## Search results [:octicons-tag-16:{ title="from Release 20.1 (OO-8767)" }](https://track.frentix.com/issue/OO-8767) {: #search_results}

The search results of the global search contain:

* Data / documents from courses in which you are a member and to which you also have access as a course member
* Data / documents from courses that are configured as follows under `Course > Administration > Settings > Share`: "Without booking" or "Freely available"

Personal data such as profiles, visiting cards or personal folders is not indexed and does not appear in the search results.


## Activation {: #activation}

The global search is only visible and usable if the search service is switched on for your OpenOlat instance. Administrators make this setting in the server configuration (property `search.service`). The settings for indexing are located in the system administration under `Administration > Core functions > Full-text search`, see [Core functions: Overview](../../manual_admin/administration/Core_functions.md). If the search is not visible for you, please contact the administrator of your OpenOlat instance.


## Further information {: #further_information}

[General information on the search >](Search_General.md)<br>
[Core functions: Overview >](../../manual_admin/administration/Core_functions.md)<br>
[Local search >](Search_Local.md)<br>
[Search other users >](Search_Person.md)<br>
[Search in a course >](Search_in_Course.md)<br>
[Search in the File Hub >](Search_in_FileHub.md)

[To the top of the page ^](#search_global)
