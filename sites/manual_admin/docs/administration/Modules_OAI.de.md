# Module: OAI PMH

!!! abstract ""
    zu :octicons-tag-24: Release 17.2 verfügbar


Der Zweck des "Open Archives Initiative - Protocol for Metadata Harvesting" (OAI-PMH): Zugang zu digitalen Ressourcen, in unserem Falle veröffentlichte Lernressourcen  für die Weitergabe von Metadaten an Portale, Suchmaschinen oder Kataloge. Weitergehende Informationen sind auf der [Open Archives Webseite](https://www.openarchives.org) zu finden.

## Administration

Das Modul kann unter `Administration-> Modules -> OAI PMH` eingeschaltet werden. Es ist standardmässig auf jeder Instanz deaktiviert. Wenn das Modul eingeschaltet ist, ist auch der API-Endpoint verfügbar, wo alle veröffentlichten Ressourcen über XML verfügbar sind.

## Lizenz Einschränkungen

Man kann Lernressourcen einschränken. Entweder nur Lernressourcen mit Lizenzen oder die Lernressourcen mit einer bestimmten Lizenzart werden ihre Metadaten über die Schnittstelle schicken.

## API Konfiguration

### Sets
Verschiedene Sets können angewählt werden. Sets kategorisieren die Metadaten der Lernressourcen verschiedener Art. 

* Taxonomie-basiertes Set
* Organisations-basierte Set, basierend auf administrativer Org-Beziehung)
* Lizenzbasierte Set, sortiert nach Lizenzarten
* Typ-basiertes Set, sortiert nach den Lernressourcentypen wie Kurs, Video, Podcast.
* Angebot-basiertes Set, sortiert nach den Angebotstypen wie privat, buchbar mit Konto, Gast
