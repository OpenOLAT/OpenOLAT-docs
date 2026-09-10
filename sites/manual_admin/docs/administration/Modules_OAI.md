# Module OAI-PMH [:octicons-tag-16:{ title="available since release 17.2" }]() {: #oai_pmh}

The purpose of the "Open Archives Initiative - Protocol for Metadata Harvesting" (OAI-PMH): access to digital resources, in our case published learning resources for metadata sharing with portals, search engines or catalogues. More information can be found on the [Open Archives website](https://www.openarchives.org).

![Configuration page of the SEO / OAI-PMH metadata module with the sections API configuration, Restrictions and Search Engine Optimization](assets/modules_oai_v1_de.png){ class="shadow lightbox" }


## Metadata prefix {: #metadataprefix}

The metadata prefixes indicate two different metadata collections:

* OpenOlat specific (learning resource URL is included in the title): _www.yourwebsite.com/oaipmh?verb=listRecords&**metadataprefix=oai_oo**_

* Dublin Core metadata: _www.yourwebsite.com/oaipmh?verb=listRecords&**metadataprefix=oai_dc**_


The respective XML element in the corresponding metadata collection is described in brackets.

Metadaten | OAI OpenOlat | OAI Dublin Core
---------|----------|---------
 identifier | **x** | **x**
 url | **x** | --
 info_url | **x** | **x** (source)
 title | **x** (displayname) | **x**
 taxonomy | **x** | **x** (subject)
 resourcename| **x** | --
 initialauthor| **x** | **x** (creator)
 softkey| **x** | --
 location| **x** | --
 description| **x** | **x**
 publisher| **x** | **x**
 requirements| **x** | --
 credits| **x** | --
 allowtoleave| **x** | --
 authors | **x** | **x** (contributor)
 Date |  **x** (creationDate) | **x**
 r_identifier | **x** | --
 resname | **x** | **x** (format)
 expenditureofwork | **x** | --
 teaser | **x** | **x** (coverage)
 teaserImage | **x** | --
 canDownload | **x** | --
 canCopy | **x** | --
 canReference | **x** | --
 status_published_date | **x** | --
 language  |**x** (mainlanguage) | **x**
 license_name | **x** | **x** (rights = + license_licensor)
 license_licensor | **x** | --
 sets | **x** | **x**
 deleted | **x** | **x**

[To the top of the page ^](#oai_pmh)

---


## Administration {: #administration}

The module can be switched on under `Administration > Modules > SEO / OAI-PMH metadata`. It is deactivated by default on every instance. If the module is switched on, the API endpoint, where all published resources are listed via XML, is also available.

### API endpoint {: #endpoint}

This is the application interface from which the metadata is retrieved. Different parameters can be used to filter for different learning resources. You can test the API endpoint by clicking the button beneath the URL.

### Identifier format {: #identifier_type}

The identifier format can be used to set the format of the identifier. Either you use the Dublin Core namespace or OpenOlat's own identifier, which also contains the resource info, where you also see the info page.

### Licence restrictions {: #license_restrictions}

Learning resources can be restricted by licence. Either only learning resources with a licence or learning resources with a specific licence type are shared through the interface. If licences for learning resources are not activated, no learning resources are indexed when a restriction is applied.

[To the top of the page ^](#oai_pmh)

---


## API Configuration {: #API_config}

### Sets {: #API_config_sets}

Different sets can be selected. Sets categorize the metadata of learning resources of different types. 

* Taxonomy-based set
* Organisation-based set (based on administrative org relationship)
* OER-licence-based set, sorted by licence type
* Type-based set, sorted by learning resource types such as course, video, podcast.
* Offer-based set, sorted by the offer types such as private, bookable with account, guest.


## Search Engine Optimization {: #API_config_search_engine}

This allows you to actively make shared learning resources accessible to search engines. There are two methods: sitemap.xml, which is mainly used by Google, and [indexNow](https://www.indexnow.org/index) by Bing and others. This collection is actively triggered once a week.

![Search Engine Optimization switched on, with the fields Organisation name and Keywords and the options for sitemap.xml and indexNow](assets/modules_oai_search_engine_optimization_v1_de.png){ class="shadow lightbox" }

If you have your own search engine index, enter its URL under "Custom".

When "Search Engine publish" is switched on, two additional fields for the search engine metadata appear. [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9306)" }](https://track.frentix.com/issue/OO-9306){:target="_blank"} Both fields are optional; if left empty, the system uses the default values.

#### Organisation name {: #organisation_name }

Overrides the organisation name used in the search engine metadata (for example in the Open Graph field "og:site_name"). If left empty, the name of the default organisation is used.

#### Keywords {: #keywords }

Override the global meta keywords (meta tag "keywords") output on all pages. If left empty, the system uses the preset keywords.

[To the top of the page ^](#oai_pmh)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[Open Archives website](https://www.openarchives.org)<br>
[indexNow](https://www.indexnow.org/index)

[To the top of the page ^](#oai_pmh)

