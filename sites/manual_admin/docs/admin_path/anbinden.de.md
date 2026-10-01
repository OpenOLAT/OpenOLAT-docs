---
title: Prüfen und Anbinden
description: Prüfungen und externe Werkzeuge. Die Prüfungsverwaltung legt fest, wie Prüfungen ablaufen, der Safe Exam Browser sichert sie ab.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-nav" aria-label="Navigation: Der Weg zur laufenden Installation" markdown="1">

<span class="oo-mh-nav__label">Navigation: Der Weg zur laufenden Installation</span>
[‹ Menü: Module](module.de.md){ .oo-mh-btn .oo-mh-btn--prev }
[Der Weg zur laufenden Installation ›](index.de.md){ .oo-mh-btn .oo-mh-btn--next }

</nav>

# Prüfen und Anbinden {: #anbinden}

<p class="oo-mh-sub">Prüfungen und externe Werkzeuge</p>

Die Prüfungsverwaltung legt fest, wie Prüfungen ablaufen, der Safe Exam Browser sichert sie ab. Unter Externe Werkzeuge schalten Sie mit dem KI Modul die KI-Funktionen frei und verbinden über LTI Kurse mit externen Anwendungen. Die REST API in der Core Konfiguration öffnet OpenOlat für andere Systeme.

## Begriffe dieser Station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Modul</p>

### Prüfungsverwaltung {: #assessment_assessment_management}

Die Verwaltung von Prüfungsmodus und Prüfungseinsicht.

??? note "Prüfungsverwaltung im Detail"

    Die Verwaltung von Prüfungsmodus und Prüfungseinsicht. Im Kurs ist sie das Werkzeug der Kursadministration mit den beiden Tabs Prüfungsmodus und Prüfungseinsicht. In der Administration unter e-Assessment listet sie die Prüfungsmodi aller Kurse und hält die Einstellungen.

    **Englisch:** Assessment management

    **Wie Nutzende es nennen:** Prüfungsmanagement, Bewertungsverwaltung, Bewertungsmanagement, Prüfungsauswertung

    **Nicht verwechseln mit «[Bewertungswerkzeug](../../manual_user/learningresources/Assessment_tool_overview.de.md)»:** Das Bewertungswerkzeug bewertet Leistungen, die Prüfungsverwaltung legt Prüfungsfenster und Einsichten fest.

    [Im Handbuch lesen](../../manual_user/learningresources/Assessment_Management.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Pr%C3%BCfungsverwaltung%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Integration</p>

### Safe Exam Browser {: #assessment_safe_exam_browser}

Anbindung des Safe Exam Browser. Der Prüfungsmodus verlangt diesen Browser und sperrt damit während der Prüfung alle anderen Programme des Geräts.

??? note "Safe Exam Browser im Detail"

    Anbindung des Safe Exam Browser. Der Prüfungsmodus verlangt diesen Browser und sperrt damit während der Prüfung alle anderen Programme des Geräts.

    **Englisch:** Safe Exam Browser

    **Wie Nutzende es nennen:** SEB, Sichere Prüfungssoftware, Klausur-Browser, Prüfungsbrowser, Lockdown-Browser, Prüfungsschutz, Exam-Sicherheitsbrowser

    [Im Handbuch lesen](../../manual_how-to/SEB/SEB.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Safe%20Exam%20Browser%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Modul</p>

### KI Modul {: #ai_ai_module}

Das Modul, das die Anbindung an KI-Dienste verwaltet: welche Anbieter zur Verfügung stehen, welche Funktionen aktiv sind, welches Modell jede Funktion verwendet und wie viele Aufrufe gleichzeitig laufen dürfen.

??? note "KI Modul im Detail"

    Das Modul, das die Anbindung an KI-Dienste verwaltet: welche Anbieter zur Verfügung stehen, welche Funktionen aktiv sind, welches Modell jede Funktion verwendet und wie viele Aufrufe gleichzeitig laufen dürfen. Es liefert selbst keine Funktion für Lernende, sondern bedient die Funktionen anderer Module.

    **Englisch:** AI module

    **Wie Nutzende es nennen:** KI, Künstliche Intelligenz, AI, LLM, Sprachmodell-Anbindung, KI-Funktionen, AI-Assistent, KI-gestützte Module, KI-Funktionsmodule

    [Im Handbuch lesen](../administration/External_Tools_AI.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22KI%20Modul%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Standard</p>

### LTI {: #integrations_lti}

Standard Learning Tools Interoperability.

??? note "LTI im Detail"

    Standard Learning Tools Interoperability. Er verbindet eine Lernplattform mit einer externen Anwendung: die angemeldete Person braucht dort keine zweite Anmeldung, und die Anwendung kann Punkte zurückmelden. OpenOlat ist dabei Plattform, wenn es ein Tool im Kurs einbindet, und Tool, wenn es einen Kurs oder eine Gruppe für eine andere Plattform bereitstellt.

    **Englisch:** LTI

    **Wie Nutzende es nennen:** Learning Tools Interoperability, LTI 1.3, LTI-Schnittstelle, LTI-Anbindung, Externe Tools, Tool-Integration, LMS-Integration, Drittanwendungen

    [Im Handbuch lesen](../administration/LTI_Integrations.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22LTI%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Modul</p>

### REST API {: #integrations_rest_api}

Programmierschnittstelle nach dem REST-Muster.

??? note "REST API im Detail"

    Programmierschnittstelle nach dem REST-Muster. Fremdsysteme legen darüber Konten, Kurse und Einschreibungen an, ohne die Oberfläche zu bedienen.

    **Englisch:** REST API

    **Wie Nutzende es nennen:** Schnittstelle, API-Integration, Systemanbindung, API-Schnittstelle, Webservice

    [Im Handbuch lesen](../administration/REST_API.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22REST%20API%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

</div>

## Nachlesen {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Nachlesen</p>

[Externe Werkzeuge: Übersicht](../administration/External_Tools_-_Administration.de.md)

Für die Einrichtung begleitet Sie frentix mit Support und Coaching: [support@frentix.com](mailto:support@frentix.com)

</div>

</div>

## Vertiefen, wenn die Installation läuft {: #deepen}

Die Installation läuft. Jetzt lohnt sich, was beim Einrichten noch nicht wichtig war: Die Begriffe dieser Station haben Teile und Einstellungen, die die Installation genauer steuern.

- **Safe Exam Browser:** [Safe Exam Browser Konfigurationsvorlage](../administration/e-Assessment_AssessmentMgmt.de.md). Mehr dazu auf der Seite [Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor?](../../manual_how-to/SEB/SEB.de.md).
- **KI Modul:** [KI Anbieter](../administration/External_Tools_AI.de.md), [KI Funktion](../administration/External_Tools_AI.de.md), KI-Einstellungen, [KI-Verarbeitungs-Pool](../administration/External_Tools_AI.de.md) und weitere.
- **LTI:** [Plattform](../administration/LTI_External_platforms.de.md), [Deployment](../administration/LTI_External_tools.de.md), [Tool](../administration/LTI_External_tools.de.md), [Deep Linking](../administration/LTI_Deeplinking.de.md) und weitere. Mehr dazu auf der Seite [LTI 1.3 Integrationen](../administration/LTI_Integrations.de.md).

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Bewertungswerkzeug - Übersicht >](../../manual_user/learningresources/Assessment_tool_overview.de.md)<br>
[Prüfungsverwaltung: Übersicht >](../../manual_user/learningresources/Assessment_Management.de.md)<br>
[Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor? >](../../manual_how-to/SEB/SEB.de.md)<br>
[Externe Werkzeuge: KI Modul >](../administration/External_Tools_AI.de.md)<br>
[LTI 1.3 Integrationen >](../administration/LTI_Integrations.de.md)<br>
[REST API >](../administration/REST_API.de.md)<br>
[Externe Werkzeuge: Übersicht >](../administration/External_Tools_-_Administration.de.md)<br>
[e-Assessment Administration: Prüfungsverwaltung >](../administration/e-Assessment_AssessmentMgmt.de.md)<br>
[LTI - Externe Plattformen >](../administration/LTI_External_platforms.de.md)<br>
[LTI - Externe Werkzeuge >](../administration/LTI_External_tools.de.md)<br>
[LTI - Deep Linking >](../administration/LTI_Deeplinking.de.md)

**Weiterführend**<br>
[e-Assessment Administration: Übersicht >](../administration/e-Assessment_Administration.de.md)<br>
[Lebenszyklen: Übersicht >](../administration/Life_cycles_-_Administration.de.md)<br>
[Reports: Übersicht >](../administration/Reports.de.md)<br>
[Glossar >](../../reference_glossary/glossary.de.md)

[Zum Seitenanfang ^](#anbinden)
