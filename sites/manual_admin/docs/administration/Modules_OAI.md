# Modules: OAI-PMH
The purpose of the "Open Archives Initiative - Protocol for Metadata Harvesting" (OAI-PMH): access to digital resources, in our case published learning resources for metadata sharing with portals, search engines or catalogues.

## Administration

The module can be switched on under 'Administration-> Modules -> OAI PMH'. It is deactivated by default on every instance. If the module is switched on, the API endpoint is also available, where all published resources are available via XML.

## Licence restrictions

One can restrict learning resources. Either only learning resources with licences or learning resources with a specific licence type will send their metadata through the interface.

## API Configuration

**Sets**: Different sets can be selected. Sets categorise the metadata of learning resources of different types. 
* Taxonomy-based set
* Organisation-based set, based on administrative org relationship).
* Licence-based set, sorted by licence type
* Type-based set, sorted by learning resource types such as course, video, podcast.
* Offer-based set, sorted by the offer types such as private, bookable with account, guest.