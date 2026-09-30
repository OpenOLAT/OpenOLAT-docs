---
title: Rollen
description: Konten und Organisation. In der Benutzerverwaltung erstellen Sie Konten und weisen Rollen zu.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-nav" aria-label="Navigation: Der Weg zur laufenden Installation" markdown="1">

<span class="oo-mh-nav__label">Navigation: Der Weg zur laufenden Installation</span>
[‹ Menü: Zugang](zugang.de.md){ .oo-mh-btn .oo-mh-btn--prev }
[Menü: Module ›](module.de.md){ .oo-mh-btn .oo-mh-btn--next }

</nav>

# Rollen {: #rollen}

<p class="oo-mh-sub">Konten und Organisation</p>

In der Benutzerverwaltung erstellen Sie Konten und weisen Rollen zu. Die Systemrolle Systemadministrator:in konfiguriert die Installation, Administrator:in verwaltet die Organisation. Benutzerverwalter:in und Rollenverwalter:in teilen die Arbeit an den Konten, Autor:innen bauen Kurse. Jedes Konto gehört zu einer Organisation.

## Begriffe dieser Station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Rolle</p>

### Systemadministrator:in {: #roles_role_sysadmin}

Systemrolle. Sie öffnet den Bereich Administration und damit die Systemkonfiguration.

??? note "Systemadministrator:in im Detail"

    Systemrolle. Sie öffnet den Bereich Administration und damit die Systemkonfiguration. Sie erteilt keine Rechte an Objekten: ohne zusätzliche Organisationsrolle sieht eine systemadministrierende Person weder Kurse noch Konten.

    **Englisch:** System administrator

    **Wie Nutzende es nennen:** IT-Administrator:in, Serveradministrator:in

    [Im Handbuch lesen](../../manual_user/basic_concepts/Roles.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Systemadministrator%3Ain%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Rolle</p>

### Administrator:in {: #roles_role_administrator}

Organisationsrolle, die alle administrativen Rollen einer Organisation vereinigt.

??? note "Administrator:in im Detail"

    Organisationsrolle, die alle administrativen Rollen einer Organisation vereinigt. Sie ist der Superuser dieser Organisation. Ihr Zugriff endet an der eigenen Organisation und deren Unterorganisationen; sie wirkt nicht systemweit und öffnet die Systemkonfiguration nicht.

    **Englisch:** Administrator

    **Wie Nutzende es nennen:** Systemverwalter:in, Systembetreuer:in

    [Im Handbuch lesen](../../manual_user/basic_concepts/Roles.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Administrator%3Ain%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Rolle</p>

### Benutzerverwalter:in {: #roles_role_usermanager}

Administrative Organisationsrolle. Sie verwaltet die Konten der eigenen Organisation: anlegen, bearbeiten, importieren, sperren und löschen.

??? note "Benutzerverwalter:in im Detail"

    Administrative Organisationsrolle. Sie verwaltet die Konten der eigenen Organisation: anlegen, bearbeiten, importieren, sperren und löschen.

    **Englisch:** User manager

    **Wie Nutzende es nennen:** User-Admin, Kontoverwalter:in

    [Im Handbuch lesen](../../manual_user/basic_concepts/Roles.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Benutzerverwalter%3Ain%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Rolle</p>

### Rollenverwalter:in {: #roles_role_rolesmanager}

Administrative Organisationsrolle. Sie vergibt und entzieht Rollen an den Konten der eigenen Organisation.

??? note "Rollenverwalter:in im Detail"

    Administrative Organisationsrolle. Sie vergibt und entzieht Rollen an den Konten der eigenen Organisation.

    **Englisch:** Roles manager

    **Wie Nutzende es nennen:** Rechteverwalter:in, Berechtigungsmanager:in

    [Im Handbuch lesen](../../manual_user/basic_concepts/Roles.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Rollenverwalter%3Ain%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Rolle</p>

### Autor:in {: #roles_role_author}

Organisationsrolle. Sie erlaubt es, im Autorenbereich Lernressourcen zu erstellen.

??? note "Autor:in im Detail"

    Organisationsrolle. Sie erlaubt es, im Autorenbereich Lernressourcen zu erstellen. Autorinnen und Autoren verwalten ihre eigenen Ressourcen, nicht die der Organisation.

    **Englisch:** Author

    **Wie Nutzende es nennen:** Kursersteller:in, Content-Ersteller:in, E-Learning-Autor:in, Content-Autor:in, Lerninhalte-Ersteller:in, Kursautor:in

    [Im Handbuch lesen](../../manual_user/basic_concepts/Roles.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Autor%3Ain%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Begriff</p>

### Organisation {: #platform_organisation}

Eine Einheit in der Struktur der Plattform, zum Beispiel eine Schule, ein Institut oder eine Abteilung.

??? note "Organisation im Detail"

    Eine Einheit in der Struktur der Plattform, zum Beispiel eine Schule, ein Institut oder eine Abteilung. Organisationen sind hierarchisch, tragen die Rollen ihrer Mitglieder und begrenzen, worauf verwaltende Rollen zugreifen.

    **Englisch:** Organisation

    **Wie Nutzende es nennen:** Organisationsstruktur, Abteilungsverwaltung, Mandantenverwaltung, Einrichtung, Abteilung

    [Im Handbuch lesen](../administration/Modules_Organisations.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Organisation%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

</div>

## Nachlesen {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Nachlesen</p>

[Benutzerverwaltung](../usermanagement/index.de.md)

Für die Einrichtung begleitet Sie frentix mit Support und Coaching: [support@frentix.com](mailto:support@frentix.com)

</div>

</div>

## Vertiefen, wenn die Installation läuft {: #deepen}

Die Installation läuft. Jetzt lohnt sich, was beim Einrichten noch nicht wichtig war: Die Begriffe dieser Station haben Teile und Einstellungen, die die Installation genauer steuern.

Diese Station hat keine tieferen Teile. Die nächste Station wartet.

## Weiterführende Informationen {: #further_information}

[Rollen und Rechte: Welche Rollen gibt es? >](../../manual_user/basic_concepts/Roles.de.md)<br>
[Modul Organisationen >](../administration/Modules_Organisations.de.md)<br>
[Benutzerverwaltung >](../usermanagement/index.de.md)<br>
[Konto erstellen >](../usermanagement/Create_User.de.md)<br>
[Rollen zuweisen >](../usermanagement/Assign_roles.de.md)<br>
[Rollen und Rechte: Übersicht >](../../manual_user/basic_concepts/Roles_Rights.de.md)<br>
[Glossar >](../../reference_glossary/glossary.de.md)

[Zum Seitenanfang ^](#rollen)
