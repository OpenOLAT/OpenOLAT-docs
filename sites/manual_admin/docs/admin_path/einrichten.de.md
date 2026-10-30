---
title: System
description: Betrieb und Auftritt. Vor dem Start klären Sie, wer die Installation betreibt, Ihre Organisation selbst oder ein Anbieter wie frentix, und wie sie auftreten soll.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-trail" aria-label="Einführung für Administrator:innen" markdown="1">

1. [System](einrichten.de.md){ aria-current="page" }
1. [Zugang](zugang.de.md)
1. [Rollen](rollen.de.md)
1. [Module](module.de.md)
1. [Prüfen und Anbinden](anbinden.de.md)

</nav>

# System {: #einrichten}

<p class="oo-mh-sub">Betrieb und Auftritt</p>

Vor dem Start klären Sie, wer die Installation betreibt, Ihre Organisation selbst oder ein Anbieter wie frentix, und wie sie auftreten soll. Die Core-Konfiguration legt die Grundfunktionen fest, die Startseite den ersten Bildschirm nach dem Login und das Customizing Systemlayout, Logo und Fusszeile.

## Begriffe dieser Station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Bereich</p>

### System {: #platform_admin_system}

Der Abschnitt der Administration für den Betrieb: Systeminformation, Info messages, Aktive Sitzungen, Errors, Caches, Locks, Database ORM, Java VM Infos und Scheduler.

??? note "System im Detail"

    Der Abschnitt der Administration für den Betrieb: Systeminformation, Info messages, Aktive Sitzungen, Errors, Caches, Locks, Database ORM, Java VM Infos und Scheduler.

    **Englisch:** System

    **Wie Nutzende es nennen:** Systeminformation, Systemstatus, Fehlersuche

    [Im Handbuch lesen](../administration/System.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22System%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20das%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Bereich</p>

### Core Konfiguration {: #platform_admin_core_config}

Der Abschnitt der Administration mit den Grundfunktionen der Plattform: E-Mail, Dateien und Ordner, Startseite, REST API, WebDAV, Kalender, Benachrichtigungen und weitere.

??? note "Core Konfiguration im Detail"

    Der Abschnitt der Administration mit den Grundfunktionen der Plattform: E-Mail, Dateien und Ordner, Startseite, REST API, WebDAV, Kalender, Benachrichtigungen und weitere.

    **Englisch:** Core functions

    [Im Handbuch lesen](../administration/Core_functions.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Core%20Konfiguration%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20das%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Bereich</p>

### Customizing {: #platform_admin_customizing}

Der Abschnitt der Administration für das Erscheinungsbild und die Anpassung der Plattform: Bereiche, Hilfe, Benutzer:innen-Attribute, Impressum, Nutzungsbedingungen und Sprachen.

??? note "Customizing im Detail"

    Der Abschnitt der Administration für das Erscheinungsbild und die Anpassung der Plattform: Bereiche, Hilfe, Benutzer:innen-Attribute, Impressum, Nutzungsbedingungen und Sprachen.

    **Englisch:** Customizing

    [Im Handbuch lesen](../administration/Customizing.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Customizing%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20das%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Begriff</p>

### Startseite {: #platform_landing_page}

Die Seite, die eine Person nach der Anmeldung sieht.

??? note "Startseite im Detail"

    Die Seite, die eine Person nach der Anmeldung sieht. Die Administration legt Regeln nach Rolle oder nach Wert eines Benutzerattributs fest; die erste zutreffende Regel gilt. Eine Person überschreibt sie in den Einstellungen mit ihrer eigenen Startseite.

    **Englisch:** Landing page

    **Wie Nutzende es nennen:** Landingpage, Einstiegsseite, Seite nach dem Login, Startbereich

    [Im Handbuch lesen](../administration/Landing_pages.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Startseite%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20das%20ein%3F)

</div>

</div>

## Nachlesen {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Nachlesen</p>

[System](../administration/System.de.md)

Nach der Installation stehen die Einstellungen in der System-Administration unter:<br>`Administration > Core-Konfiguration`<br>`Administration > Customizing`

Bei der Einrichtung begleitet Sie die zuständige Kundenberatung bei frentix mit Support und Coaching.

</div>

</div>

## Vertiefen, wenn die Installation läuft {: #deepen}

Die Installation läuft. Jetzt lohnt sich, was am Anfang noch nicht wichtig war: Die Begriffe dieser Station haben Teile und Einstellungen, die die Installation genauer steuern.

- **System:** [Info messages](../administration/System.de.md), [Aktive Sitzungen](../administration/System.de.md).
- **Core Konfiguration:** [Dateien und Ordner](../administration/Files_and_Folders.de.md), Audit-Log, Limite für Anfragen, [E-Mail Postfach und Versand](../administration/E-Mail_Settings.de.md).
- **Customizing:** [Systemlayout](../administration/Customizing.de.md), [Bereiche](../administration/Customizing.de.md).

## Weiterführende Informationen {: #further_information}

[System >](../administration/System.de.md)<br>
[Core-Konfiguration: Übersicht >](../administration/Core_functions.de.md)<br>
[Customizing: Übersicht >](../administration/Customizing.de.md)<br>
[Startseite >](../administration/Landing_pages.de.md)<br>
[Dateien und Ordner >](../administration/Files_and_Folders.de.md)<br>
[E-Mail Einstellungen >](../administration/E-Mail_Settings.de.md)<br>
[Glossar >](../../reference_glossary/glossary.de.md)

[Zum Seitenanfang ^](#einrichten)
