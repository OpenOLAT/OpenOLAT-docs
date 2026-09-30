---
title: Assess and connect
description: Exams and external tools. Assessment management defines how exams run, the Safe Exam Browser secures them.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-nav" aria-label="Navigation: The path to a running installation" markdown="1">

<span class="oo-mh-nav__label">Navigation: The path to a running installation</span>
[‹ Menu: Modules](module.md){ .oo-mh-btn .oo-mh-btn--prev }
[The path to a running installation ›](index.md){ .oo-mh-btn .oo-mh-btn--next }

</nav>

# Assess and connect {: #anbinden}

<p class="oo-mh-sub">Exams and external tools</p>

Assessment management defines how exams run, the Safe Exam Browser secures them. Under External tools you enable the AI features with the AI module and connect courses to external applications via LTI. The REST API in the core functions opens OpenOlat to other systems.

## Terms of this station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### Assessment management {: #assessment_assessment_management}

The management of assessment mode and assessment inspection.

??? note "Assessment management in detail"

    The management of assessment mode and assessment inspection. In the course it is the tool of the course administration with the two tabs assessment mode and assessment inspection. In the administration under e-Assessment it lists the assessment modes of all courses and holds the settings.

    **German:** Prüfungsverwaltung

    **Not to be confused with [Assessment tool](../../manual_user/learningresources/Assessment_tool_overview.md):** The assessment tool assesses performances, the assessment management sets exam windows and inspections.

    [Read in the manual](../../manual_user/learningresources/Assessment_Management.md) · [Ask Sophia](?sophia=What%20is%20%22Assessment%20management%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Integration</p>

### Safe Exam Browser {: #assessment_safe_exam_browser}

The connection to the Safe Exam Browser.

??? note "Safe Exam Browser in detail"

    The connection to the Safe Exam Browser. The assessment mode requires this browser and thereby locks every other program on the device during the exam.

    **German:** Safe Exam Browser

    **What users call it:** SEB

    [Read in the manual](../../manual_how-to/SEB/SEB.md) · [Ask Sophia](?sophia=What%20is%20%22Safe%20Exam%20Browser%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### AI module {: #ai_ai_module}

The module that manages the connection to AI services: which providers are available, which features are active, which model each feature uses and how many calls may run at the same time.

??? note "AI module in detail"

    The module that manages the connection to AI services: which providers are available, which features are active, which model each feature uses and how many calls may run at the same time. It provides no feature for learners itself but serves the features of other modules.

    **German:** KI Modul

    **What users call it:** AI, artificial intelligence, LLM

    [Read in the manual](../administration/External_Tools_AI.md) · [Ask Sophia](?sophia=What%20is%20%22AI%20module%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Standard</p>

### LTI {: #integrations_lti}

The Learning Tools Interoperability standard.

??? note "LTI in detail"

    The Learning Tools Interoperability standard. It connects a learning platform with an external application: the signed-in person needs no second sign-in there, and the application can report points back. OpenOlat is the platform when it embeds a tool in the course, and the tool when it provides a course or a group to another platform.

    **German:** LTI

    **What users call it:** Learning Tools Interoperability, LTI 1.3, LTI integration

    [Read in the manual](../administration/LTI_Integrations.md) · [Ask Sophia](?sophia=What%20is%20%22LTI%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Module</p>

### REST API {: #integrations_rest_api}

A programming interface following the REST pattern.

??? note "REST API in detail"

    A programming interface following the REST pattern. Third-party systems use it to create accounts, courses and enrolments without going through the interface.

    **German:** REST API

    [Read in the manual](../administration/REST_API.md) · [Ask Sophia](?sophia=What%20is%20%22REST%20API%22%20in%20OpenOlat%20and%20how%20do%20I%20set%20it%20up%3F)

</div>

</div>

## Read up {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Read up</p>

[External tools: overview](../administration/External_Tools_-_Administration.md)

frentix accompanies you in the setup with support and coaching: [support@frentix.com](mailto:support@frentix.com)

</div>

</div>

## Deepen once the installation is running {: #deepen}

The installation is running. Now the things that did not matter while setting up pay off: the terms of this station have parts and settings that control the installation more precisely.

- **Safe Exam Browser:** [Safe Exam Browser configuration template](../administration/e-Assessment_AssessmentMgmt.md). More on the page [How do I prepare an exam with the Safe Exam Browser (SEB)?](../../manual_how-to/SEB/SEB.md).
- **AI module:** [AI Provider](../administration/External_Tools_AI.md), [AI Feature](../administration/External_Tools_AI.md), AI settings, [AI processing pool](../administration/External_Tools_AI.md) and more.
- **LTI:** [Platform](../administration/LTI_External_platforms.md), [Deployment](../administration/LTI_External_tools.md), [Tool](../administration/LTI_External_tools.md), [Deep Linking](../administration/LTI_Deeplinking.md) and more. More on the page [LTI 1.3 Integrations](../administration/LTI_Integrations.md).

## Further information {: #further_information}

**Mentioned on this page**<br>
[Assessment tool - overview >](../../manual_user/learningresources/Assessment_tool_overview.md)<br>
[Assessment Management: Overview >](../../manual_user/learningresources/Assessment_Management.md)<br>
[How do I prepare an exam with the Safe Exam Browser (SEB)? >](../../manual_how-to/SEB/SEB.md)<br>
[External tools: AI module >](../administration/External_Tools_AI.md)<br>
[LTI 1.3 Integrations >](../administration/LTI_Integrations.md)<br>
[REST API >](../administration/REST_API.md)<br>
[External Tools: Overview >](../administration/External_Tools_-_Administration.md)<br>
[e-Assessment Administration: Assessment management >](../administration/e-Assessment_AssessmentMgmt.md)<br>
[LTI - External Platforms >](../administration/LTI_External_platforms.md)<br>
[LTI - External tools >](../administration/LTI_External_tools.md)<br>
[LTI - Deep Linking >](../administration/LTI_Deeplinking.md)

**Further reading**<br>
[e-Assessment Administration: Overview >](../administration/e-Assessment_Administration.md)<br>
[Life cycles - Overview >](../administration/Life_cycles_-_Administration.md)<br>
[Reports: Overview >](../administration/Reports.md)<br>
[Glossary >](../../reference_glossary/glossary.md)

[To the top of the page ^](#anbinden)
