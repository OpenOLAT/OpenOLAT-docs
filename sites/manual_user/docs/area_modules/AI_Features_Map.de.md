# KI-Funktionen: Anwendungsmap {: #ai_features_map}

!!! warning "Konzeptstudie: mögliche neue Darstellung"
    Diese Seite ist ein Versuch, wie der Einstieg in die KI-Funktionen künftig aussehen könnte. Die Inhalte sind bewusst verkürzt. Verbindlich sind die verlinkten Handbuchseiten.

!!! info "Kontakt"

    Die KI-Funktionen auf dieser Seite richtet die System-Administration ein. Für die Aktivierung wenden Sie sich an Ihre Organisation.

KI unterstützt Sie beim Erstellen von Inhalten und Ihre Lernenden beim Üben, an mehreren Stellen in OpenOlat, und diese Stellen liegen weit auseinander: im Fragenpool, im Media Center, im Content Editor und bei der Taxonomie. Wer wissen will, wo sich der Einsatz lohnt, muss heute vier Handbuchseiten zusammensuchen. Die Grafik unten zeigt stattdessen das Ergebnis: was die KI Ihnen abnimmt, wo Sie es finden, und welche KI-Funktion die Administration dafür einrichtet. Jede Karte führt auf die zuständige Handbuchseite.

Die letzten Zeilen jeder Karte nennen die KI-Funktionen, die dafür eingerichtet sein müssen. Die Namen stehen so in der System-Administration: "MC" steht dort für Multiple-Choice-Fragen, "Essay" für Freitextfragen. Diese Einrichtung übernehmen Systemadministrator:innen einmal in der System-Administration unter `Administration > Externe Werkzeuge > KI-Modul`. Was dort dazugehört, zeigt der Kasten "Voraussetzung" unter den Karten: KI-Anbieter, Limits, Verarbeitungs-Pools und Nutzungsprotokoll. Im Tab "KI-Funktionen" aktivieren Systemadministrator:innen jede Funktion einzeln und wählen dazu einen KI-Anbieter und ein Modell. Den Button "KI-Fragen" im Fragenpool zeigt OpenOlat zum Beispiel erst, wenn dort die KI-Funktion "MC Fragen Generator" konfiguriert ist.

Das KI-Feedback zu Freitextantworten und die KI-Bildbeschreibungen beim Hochladen schaltet zudem jede Person für sich ein oder aus, auch Lernende. Wer das KI-Feedback ausschaltet, erhält im Quiz keines. Die Wahl treffen Sie im [Tab KI-Einstellungen](../personal_menu/Settings.de.md#tab_ai_settings) Ihrer persönlichen Einstellungen:<br>
`Persönliches Menü > Einstellungen > Tab "KI-Einstellungen"`

<div style="max-width:1450px">
<svg viewBox="0 0 1040 716" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Was die KI Autor:innen abnimmt: Fragen im Fragenpool, Bild-Metadaten im Media Center, KI-Feedback im Quiz einer Seite, Zuordnung zum Fachbereich. Darunter die Einrichtung im KI-Modul">
<style>
  .cm text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-weight: 600; fill: #344054; }
  .cm .h0 { font-size: 22px; font-weight: 700; }
  .cm .out { font-size: 21px; font-weight: 700; fill: #8A4A0B; }
  .cm .place { font-size: 16px; font-weight: 700; fill: #C06613; letter-spacing: 0.4px; }
  .cm .body { font-size: 17px; font-weight: 500; fill: #344054; }
  .cm .fn { font-size: 16px; font-weight: 600; fill: #64748b; }
  .cm .bh { font-size: 18px; font-weight: 700; fill: #344054; }
  .cm .chip { font-size: 16px; font-weight: 600; fill: #1F4E8C; }
  .cm .cap { font-size: 16px; font-weight: 600; fill: #64748b; }
  .cm a:hover .card { stroke-width: 3.5; }
  .cm a:hover .cbox { stroke-width: 3; }
  .cm a { cursor: pointer; }
</style>
<g class="cm">

<text x="40" y="34" class="h0">Was die KI Autor:innen abnimmt</text>

<!-- Karte 1: Fragenpool -->
<a href="../Question_Bank_Create_Questions/#create_with_AI"><title>Fragenpool: Fragen erstellen</title><g>
<rect class="card" x="40" y="60" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="40" y="60" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="68" y="90" class="place">FRAGENPOOL</text>
<text x="68" y="122" class="out">Fragen aus einem Lerntext</text>
<text x="68" y="152" class="body">Text einfügen oder hochladen, die KI schlägt</text>
<text x="68" y="175" class="body">Multiple-Choice- und Freitextfragen vor, diese samt</text>
<text x="68" y="198" class="body">Musterantwort für das KI-Feedback im Quiz.</text>
<text x="68" y="226" class="fn">MC Fragen Generator · Essay Fragen Generator</text>
<text x="68" y="246" class="fn">Essay Bewertung</text>
</g></a>

<!-- Karte 2: Media Center -->
<a href="../../basic_concepts/Media_Center_Items/#metadata_ai"><title>Media Center: Metadaten mit KI generieren</title><g>
<rect class="card" x="530" y="60" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="530" y="60" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="558" y="90" class="place">MEDIA CENTER</text>
<text x="558" y="122" class="out">Bild-Metadaten auf Knopfdruck</text>
<text x="558" y="152" class="body">Der Button "Metadaten mit KI generieren" füllt Titel,</text>
<text x="558" y="175" class="body">Beschreibung, Alt-Text und Tags eines Bildes. Beim</text>
<text x="558" y="198" class="body">Hochladen und beim Markdown-Import läuft das</text>
<text x="558" y="221" class="body">auch im Hintergrund.</text>
<text x="558" y="248" class="fn">Bildbeschreibungs-Generator</text>
</g></a>

<!-- Karte 3: Content Editor -->
<a href="../../basic_concepts/Content_Editor/Editor_Quiz/#ai_feedback"><title>Content Editor: KI-Feedback im Quiz</title><g>
<rect class="card" x="40" y="280" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="40" y="280" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="68" y="310" class="place">CONTENT EDITOR</text>
<text x="68" y="342" class="out">Quiz mit KI-Feedback</text>
<text x="68" y="372" class="body">Freitextfragen im Quiz des Kursbausteins "Seite".</text>
<text x="68" y="395" class="body">Lernende senden ihre Antwort mit "Überprüfen" und</text>
<text x="68" y="418" class="body">erhalten eine Beurteilung mit Stärken, Lücken und</text>
<text x="68" y="441" class="body">nächstem Schritt. Das Feedback vergibt keine Punkte.</text>
<text x="68" y="468" class="fn">Essay Bewertung</text>
</g></a>

<!-- Karte 4: Taxonomie -->
<a href="../../../manual_admin/administration/Modules_Taxonomy/#ai_matching"><title>Modul Taxonomie: Automatische Zuordnung per KI</title><g>
<rect class="card" x="530" y="280" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="530" y="280" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="558" y="310" class="place">TAXONOMIE</text>
<text x="558" y="342" class="out">Zuordnung zum Fachbereich</text>
<text x="558" y="372" class="body">Die KI erkennt, worum es in einem Bild geht, und</text>
<text x="558" y="395" class="body">ordnet es dem passenden Fachbereich zu: beim</text>
<text x="558" y="418" class="body">Hochladen und beim Markdown-Import.</text>
<text x="558" y="446" class="fn">Bildbeschreibungs-Generator ·</text>
<text x="558" y="466" class="fn">Taxonomie-Zuordnung (Embeddings)</text>
</g></a>

<!-- Sockel -->
<path d="M 275 480 L 275 506" stroke="#1F4E8C" stroke-width="2" fill="none"/>
<path d="M 765 480 L 765 506" stroke="#1F4E8C" stroke-width="2" fill="none"/>
<path d="M 275 506 L 765 506" stroke="#1F4E8C" stroke-width="2" fill="none"/>
<path d="M 520 506 L 520 526" stroke="#1F4E8C" stroke-width="2" fill="none" marker-end="url(#ah-b)"/>
<defs>
  <marker id="ah-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1F4E8C"/>
  </marker>
</defs>

<rect x="40" y="532" width="960" height="146" rx="12" fill="#F4F7FB" stroke="#1F4E8C" stroke-width="2"/>
<text x="60" y="562" class="bh">Voraussetzung, einmal in der System-Administration eingerichtet</text>

<a href="../../../manual_admin/administration/External_Tools_AI/#ai_provider"><title>KI-Anbieter</title><g>
<rect class="cbox" x="60" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="148" y="602" class="chip" text-anchor="middle">KI-Anbieter</text>
<text x="148" y="624" class="cap" text-anchor="middle">drei Anbietertypen</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_function_limits"><title>Limits pro Funktion</title><g>
<rect class="cbox" x="246" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="334" y="602" class="chip" text-anchor="middle">Limits pro Funktion</text>
<text x="334" y="624" class="cap" text-anchor="middle">Tokens, Timeout</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_pools"><title>KI-Verarbeitungs-Pools</title><g>
<rect class="cbox" x="432" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="520" y="602" class="chip" text-anchor="middle">Verarbeitungs-Pools</text>
<text x="520" y="624" class="cap" text-anchor="middle">Interaktiv 8, Batch 2</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_usage_log"><title>Nutzungsprotokoll</title><g>
<rect class="cbox" x="618" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="706" y="602" class="chip" text-anchor="middle">Nutzungsprotokoll</text>
<text x="706" y="624" class="cap" text-anchor="middle">Tokens je Aufruf</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_properties"><title>Vorkonfiguration via olat.properties</title><g>
<rect class="cbox" x="804" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2" stroke-dasharray="6 4"/>
<text x="892" y="602" class="chip" text-anchor="middle">olat.properties</text>
<text x="892" y="624" class="cap" text-anchor="middle">optional</text>
</g></a>

<text x="60" y="666" class="cap">Ein Anbieter kann mehrere Funktionen bedienen. Je Funktion wählt die Administration Anbieter und Modell.</text>

<text x="40" y="704" class="cap">Jede Karte führt auf ihre Handbuchseite, jeder Kasten der Voraussetzung auf seinen Abschnitt im Administrationshandbuch.</text>
</g>
</svg>
</div>

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Persönliche Konfiguration: Einstellungen >](../personal_menu/Settings.de.md)<br>
[Fragenpool: Fragen erstellen >](Question_Bank_Create_Questions.de.md)<br>
[Media Center: Informationen und Einstellungen zu Einzelmedien >](../basic_concepts/Media_Center_Items.de.md)<br>
[Content Editor: Quiz und KI-Feedback >](../basic_concepts/Content_Editor/Editor_Quiz.de.md)<br>
[Modul Taxonomie >](../../manual_admin/administration/Modules_Taxonomy.de.md)<br>
[Externe Werkzeuge: KI-Modul >](../../manual_admin/administration/External_Tools_AI.de.md)

**Weiterführend**<br>
[Content Editor >](../basic_concepts/Content_Editor/index.de.md)<br>
[Content Editor: Importieren >](../basic_concepts/Content_Editor/Editor_Import.de.md)

[Zum Seitenanfang ^](#ai_features_map)
