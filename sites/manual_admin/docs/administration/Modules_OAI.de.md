# Modul OAI PMH [:octicons-tag-16:{ title="ab Release 17.2 verfügbar" }]() {: #oai_pmh}

Der Zweck des "Open Archives Initiative - Protocol for Metadata Harvesting" (OAI-PMH): Zugang zu digitalen Ressourcen, in unserem Falle veröffentlichte Lernressourcen für die Weitergabe von Metadaten an Portale, Suchmaschinen oder Kataloge. Weitergehende Informationen sind auf der [Open Archives Webseite](https://www.openarchives.org) zu finden.

![Konfigurationsseite des Moduls SEO / OAI-PMH Metadaten mit den Abschnitten API Konfiguration, Einschränkungen und Suchmaschinenoptimierung](assets/modules_oai_v1_de.png){ class="shadow lightbox" }


## Metadataprefix {: #metadataprefix}

Die Metadatenprefixe zeigen zwei verschiedene Metadatensammlungen an:

* OpenOlat spezifisch (Lernressourcen-URL ist im Titel enthalten): _www.yourwebsite.com/oaipmh?verb=listRecords&**metadataprefix=oai_oo**_

* Metadaten nach Dublin Core: _www.yourwebsite.com/oaipmh?verb=listRecords&**metadataprefix=oai_dc**_


In Klammern ist das jeweilige XML Element in der passenden Metadatensammlung beschrieben.

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


[Zum Seitenanfang ^](#oai_pmh)

---


## Administration {: #administration}

Das Modul kann unter `Administration > Module > SEO / OAI-PMH Metadaten` eingeschaltet werden. Es ist standardmässig auf jeder Instanz deaktiviert. Wenn das Modul eingeschaltet ist, ist auch der API-Endpoint verfügbar, wo alle veröffentlichten Ressourcen über XML verfügbar sind.

### API Endpunkt {: #endpoint}

Dies ist die Anwendungsschnittstelle, woher die Metadaten abgefragt werden. Mittels verschiedener Parameter kann man hier nach unterschiedlichen Lernressourcen filtern. Der API-Endpunkt kann auch mittels Klick auf den Button getestet werden.


### Identifier Format {: #identifier_type}

Mit dem Identifier Format kann das Format des Identifiers eingestellt werden. Entweder man benutzt den Dublin-Core-Namespace oder den OpenOlat eigenen Identifier, welcher auch die Ressourceninfo enthält, wo man auch die Infoseite sieht.

### Lizenz Einschränkungen {: #license_restrictions}

Man kann Lernressourcen auf Lizenzen einschränken. Entweder werden nur Lernressourcen mit einer Lizenz oder Lernressourcen mit einer bestimmten Lizenzart über die Schnittstelle weitergegeben. Sind Lizenzen für Lernressourcen nicht aktiviert, werden bei einer Einschränkung keine Lernressourcen indexiert.

[Zum Seitenanfang ^](#oai_pmh)

---


## API Konfiguration {: #API_config}

### Sets {: #API_config_sets}

Verschiedene Sets können angewählt werden. Sets kategorisieren die Metadaten der Lernressourcen verschiedener Art. 

* Taxonomie-basiertes Set
* Organisations-basierte Set (basierend auf administrativer Org-Beziehung)
* OER-Lizenzbasierte Set, sortiert nach Lizenzarten
* Typ-basiertes Set, sortiert nach den Lernressourcentypen wie Kurs, Video, Podcast.
* Angebot-basiertes Set, sortiert nach den Angebotstypen wie privat, buchbar mit Konto, Gast


## Suchmaschinenoptimierung {: #API_config_search_engine}

Hiermit kann man freigegebene Lernressourcen aktiv für Suchmaschinen zugänglich machen. Dabei gibt es zwei Verfahren: sitemap.xml, was vor allem Google benutzt, und [indexNow](https://www.indexnow.org/index) von Bing und anderen. Diese Erfassung wird einmal pro Woche aktiv angestossen.

![Aktivierte Suchmaschinenoptimierung mit den Feldern Name der Organisation und Stichwörter sowie den Optionen für sitemap.xml und indexNow](assets/modules_oai_search_engine_optimization_v1_de.png){ class="shadow lightbox" }

Hat man einen eigenen Suchmaschinenindex, trägt man dessen URL unter "Frei wählbar" ein.

Ist "Suchmaschine veröffentlichen" eingeschaltet, erscheinen zwei weitere Felder für die Suchmaschinen-Metadaten. [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9306)" }](https://track.frentix.com/issue/OO-9306){:target="_blank"} Beide Felder sind optional; bleiben sie leer, verwendet das System die Standardwerte.

#### Name der Organisation {: #organisation_name }

Überschreibt den Organisationsnamen, der in den Suchmaschinen-Metadaten verwendet wird (zum Beispiel im Open-Graph-Feld "og:site_name"). Bleibt das Feld leer, wird der Name der Standardorganisation eingesetzt.

#### Stichwörter {: #keywords }

Überschreiben die globalen Meta-Stichwörter (Meta-Tag "keywords"), die auf allen Seiten ausgegeben werden. Bleibt das Feld leer, verwendet das System die voreingestellten Stichwörter.

[Zum Seitenanfang ^](#oai_pmh)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Open Archives Webseite](https://www.openarchives.org)<br>
[indexNow](https://www.indexnow.org/index)

[Zum Seitenanfang ^](#oai_pmh)
