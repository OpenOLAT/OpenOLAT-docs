# Module OAI-PMH [:octicons-tag-16:{ title="available since release 17.2" }]() {: #oai_pmh}

The purpose of the "Open Archives Initiative - Protocol for Metadata Harvesting" (OAI-PMH): access to digital resources, in our case published learning resources for metadata sharing with portals, search engines or catalogues. More information can be found on the [Open Archives website](https://www.openarchives.org).

![Administration-Module Overview](assets/modules_oai_v1_de.png){ class="shadow lightbox" }


## Metadata prefix {: #metadataprefix}

The metadata prefixes indicate two different metadata collections:

* OpenOlat specific (Learningressource URL is included in the title): _www.yourwebsite.com/oaipmh?verb=listRecords&**metadataprefix=oai_oo**_

* Dublincore metadata: _www.yourwebsite.com/oaipmh?verb=listRecords&**metadataprefix=oai_dc**_


The respective XML element in the corresponding metadata collection is described in brackets.

Metadaten | OAI OpenOlat | OAI DublinCore
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
 authors | **x** | **x** (contributer)
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

The module can be switched on under `Administration-> Modules -> OAI PMH`. It is deactivated by default on every instance. If the module is switched on, the API endpoint, where all published resources are listed via XML, is also available.

### API Endpoint {: #endpoint}

This is the application interface from which the metadata is retrieved. Different parameters can be used to filter for different learning resources. You can test die API endpoint, by clicking onto the button beneath the URL.

### Identifier Type {: #identifier_type}

The identifier type can be set with the identifier type. Either you use the DublinCore namespace or OpenOlat's own identifier, which also contains the resource info, where you also see the info page.

## License restrictions {: #license_restrictions}

One can restrict learning resources. Either only learning resources with licences or learning resources with a specific licence type will send their metadata through the interface.

[To the top of the page ^](#oai_pmh)

---


## API Configuration {: #API_config}

### Sets {: #API_config_sets}

Different sets can be selected. Sets categorize the metadata of learning resources of different types. 

* Taxonomy-based set
* Organization-based set, (based on administrative org relationship).
* Licence-based set, sorted by licence type
* Type-based set, sorted by learning resource types such as course, video, podcast.
* Offer-based set, sorted by the offer types such as private, bookable with account, guest.


## Search Engine Optimization {: #API_config_search_engine}

This allows you to actively make shared learning resources accessible to search engines. There are two methods: sitemapxml, which is mainly used by google, and [indexnow](https://www.indexnow.org/index) by bing and others. This collection is actively triggered once a week.

![Administration Module Search Engine Optimization](assets/modules_oai_search_engine_optimization_v1_de.png){ class="shadow lightbox" }

If you have your own search engine index, you can enter its url under "custom".

Additionally, you can set two values for the search engine metadata. Both fields are optional; if left empty, the system uses the default values.

**Organisation name**: Overrides the organisation name used in the search engine metadata (for example in the Open Graph field "og:site_name"). If left empty, the name of the default organisation is used.

**Keywords**: Override the global meta keywords (meta tag "keywords") output on all pages. If left empty, the system uses the preset keywords.

[To the top of the page ^](#oai_pmh)

