# AI features: Application map {: #ai_features_map}

!!! warning "Concept study: possible new presentation"
    This page is an experiment on how the entry point to the AI features could look in the future. The content is deliberately condensed. The linked manual pages are authoritative.

AI supports you in creating content at several places in OpenOlat, and these places are far apart: in the question pool, in the Media Center, in the Content Editor and in the taxonomy. Anyone who wants to know where it pays off has to gather four manual pages today. The map shows the outcome instead: what the AI takes off your hands, where you find it, and which feature is behind it. Each card leads to the responsible manual page. The base below names what the administration has to set up once so that the cards are available at all.

<div style="max-width:1450px">
<svg viewBox="0 0 1040 716" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Four outcomes for authors, below them the prerequisites in the system administration">
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

<text x="40" y="34" class="h0">What the AI takes off authors' hands</text>

<!-- Card 1: question pool -->
<a href="../Question_Bank_Create_Questions/#create_with_AI"><title>Question pool: Create Questions</title><g>
<rect class="card" x="40" y="60" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="40" y="60" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="68" y="90" class="place">QUESTION POOL</text>
<text x="68" y="122" class="out">Questions from a subject text</text>
<text x="68" y="152" class="body">Paste a text and the AI suggests multiple-choice</text>
<text x="68" y="175" class="body">and open-text questions with grading criteria.</text>
<text x="68" y="198" class="body">Answers receive formative AI feedback.</text>
<text x="68" y="226" class="fn">MC Question Generator · Essay Question Generator</text>
<text x="68" y="246" class="fn">Essay Grading</text>
</g></a>

<!-- Card 2: Media Center -->
<a href="../../basic_concepts/Media_Center_Items/#metadata_ai"><title>Media Center: generate metadata with AI</title><g>
<rect class="card" x="530" y="60" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="530" y="60" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="558" y="90" class="place">MEDIA CENTER</text>
<text x="558" y="122" class="out">Image metadata at the touch of a button</text>
<text x="558" y="152" class="body">One click fills title, description, alt text and</text>
<text x="558" y="175" class="body">keywords of an uploaded image. On import into</text>
<text x="558" y="198" class="body">the Content Editor this runs in the</text>
<text x="558" y="221" class="body">background.</text>
<text x="558" y="248" class="fn">Image Description Generator</text>
</g></a>

<!-- Card 3: Content Editor -->
<a href="../../basic_concepts/Content_Editor/#ai_feedback"><title>Content Editor: AI feedback in the quiz</title><g>
<rect class="card" x="40" y="280" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="40" y="280" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="68" y="310" class="place">CONTENT EDITOR</text>
<text x="68" y="342" class="out">Quiz with AI feedback</text>
<text x="68" y="372" class="body">Open-text questions in a quiz on a content page.</text>
<text x="68" y="395" class="body">Learners retrieve an assessment of their answer</text>
<text x="68" y="418" class="body">with strengths, gaps and the next step.</text>
<text x="68" y="441" class="body">No points are awarded.</text>
<text x="68" y="468" class="fn">Essay Grading</text>
</g></a>

<!-- Card 4: taxonomy -->
<a href="../../basic_concepts/Media_Center_Items/#metadata_ai"><title>Example in the Media Center: assignment on image upload</title><g>
<rect class="card" x="530" y="280" width="470" height="200" rx="12" fill="#FFFDFA" stroke="#C06613" stroke-width="2"/>
<rect x="530" y="280" width="7" height="200" rx="3.5" fill="#C06613"/>
<text x="558" y="310" class="place">TAXONOMY</text>
<text x="558" y="342" class="out">Assignment to the subject area</text>
<text x="558" y="372" class="body">The AI assigns a text to the matching taxonomy</text>
<text x="558" y="395" class="body">level via an embedding model. This applies to</text>
<text x="558" y="418" class="body">question generation and to image metadata.</text>
<text x="558" y="468" class="fn">Taxonomy matching</text>
</g></a>

<!-- Base -->
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
<text x="60" y="562" class="bh">Prerequisite, set up once in the system administration</text>

<a href="../../../manual_admin/administration/External_Tools_AI/#ai_provider"><title>AI provider</title><g>
<rect class="cbox" x="60" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="148" y="602" class="chip" text-anchor="middle">AI provider</text>
<text x="148" y="624" class="cap" text-anchor="middle">three provider types</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_function_limits"><title>Limits per feature</title><g>
<rect class="cbox" x="246" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="334" y="602" class="chip" text-anchor="middle">Limits per feature</text>
<text x="334" y="624" class="cap" text-anchor="middle">Tokens, timeout</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_pools"><title>AI processing pools</title><g>
<rect class="cbox" x="432" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="520" y="602" class="chip" text-anchor="middle">Processing pools</text>
<text x="520" y="624" class="cap" text-anchor="middle">Interactive 8, Batch 2</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_usage_log"><title>Usage log</title><g>
<rect class="cbox" x="618" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2"/>
<text x="706" y="602" class="chip" text-anchor="middle">Usage log</text>
<text x="706" y="624" class="cap" text-anchor="middle">Tokens per call</text>
</g></a>
<a href="../../../manual_admin/administration/External_Tools_AI/#ai_properties"><title>Preconfiguration via olat.properties</title><g>
<rect class="cbox" x="804" y="578" width="176" height="64" rx="9" fill="#FFFFFF" stroke="#2276D9" stroke-width="2" stroke-dasharray="6 4"/>
<text x="892" y="602" class="chip" text-anchor="middle">olat.properties</text>
<text x="892" y="624" class="cap" text-anchor="middle">optional</text>
</g></a>

<text x="60" y="666" class="cap">One provider can serve several features. For each feature you choose a provider and a model.</text>

<text x="40" y="704" class="cap">Each card leads to the responsible manual page, each box in the base to the matching section in the admin manual.</text>
</g>
</svg>
</div>

## Further information {: #further_information}

[Question pool: Create Questions >](Question_Bank_Create_Questions.md)<br>
[Information and settings for items in the Media Center >](../basic_concepts/Media_Center_Items.md)<br>
[Content Editor >](../basic_concepts/Content_Editor.md)<br>
[Module Taxonomy >](../../manual_admin/administration/Modules_Taxonomy.md)<br>
[External tools: AI module >](../../manual_admin/administration/External_Tools_AI.md)

[To the top of the page ^](#ai_features_map)
