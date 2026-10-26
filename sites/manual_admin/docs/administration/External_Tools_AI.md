# External tools: AI module {: #ai}


In OpenOlat you are supported by AI at different points. For these points to work, you connect the AI providers you use in the AI module. The AI module supports multiple AI providers; you define per AI feature which provider and which model is used [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9253)" }](https://track.frentix.com/issue/OO-9253){:target="_blank"}.

The AI module is part of the external tools, see [External Tools: Overview >](External_Tools_-_Administration.md). It is located in the system administration, system administrators configure it there. Only the role system administrator opens the system administration, administrators do not reach it without this role either. How roles are granted is described in [Assign roles >](../usermanagement/Assign_roles.md).

!!! tip "Support by frentix"

    Customers of frentix please contact [contact@frentix.com](mailto:contact@frentix.com) for connecting an AI provider. frentix supports the choice of provider and model, the API key and the operation of a self-hosted model. For systems with the fx-Release, frentix takes care of these adjustments.

    **Not a frentix hosting-client?** Please ask your local system operator!


## Configuration {: #config}

The AI module settings are located in the system administration under:<br>
`Administration > External tools > AI module`

The page has the title "Artificial intelligence" and is organised into four areas (tabs):

* **"AI providers"**: connect the AI services used and store an API key.
* **"AI features"**: define per feature whether AI is used and with which provider and model.
* **"AI processing pools"**: control how many AI calls are processed simultaneously.
* **"Usage log"**: review all AI calls on the instance with tokens and status.

![The tabs AI providers, AI features, AI processing pools and Usage log highlighted, at the bottom right the button Add AI provider, so you find the areas of this page](assets/admin_external_tools_ai_tab_config_v2_en.png){ class="shadow lightbox" title="AI providers tab of the AI module · 2026.10.20" }

[To the top of the page ^](#ai)

---

### AI providers {: #ai_provider}

In OpenOlat, the term "AI provider" refers to the service provider whose AI models are used for the various AI features on the platform.

Enable and configure the AI providers you want to use with the button "Add AI provider" on the right below the notes of the tab.

As the operator of the platform you are legally obliged to inform your users about the usage of an AI service.

!!! warning "Attention"

    The "AI providers" tab points out that the AI functionality is a beta feature. Using it may result in unexpected behaviour.

The following actions are available for each configured AI provider:

* **Switch "Enable"**: The provider can be temporarily disabled and enabled again. The configuration is retained.
* **Button "Check API key"**: OpenOlat validates the stored key directly with the provider. On success, OpenOlat displays the number of available models; in case of an error, the provider's error message. For the generic AI provider the button is called "Check connection".
* **Button "Delete configuration"**: Removes the provider including the API key and all configurations.

![Provider Anthropic Claude with the highlighted switch Enable and the highlighted buttons Check API key and Delete configuration, so you find the actions per provider](assets/admin_external_tools_ai_provider_config_v2_en.png){ class="shadow lightbox" title="Provider Anthropic Claude in the AI providers tab · 2026.10.20" }


#### Anthropic Claude {: #ai_provider_anthropic}

If you want to use Anthropic Claude's AI models, enter your API key here. Please note that using the Anthropic Claude service may incur charges on your Anthropic account.


#### OpenAI {: #ai_provider_openai}

If you want to use OpenAI's AI models, enter your API key here. Please note that using the OpenAI module may incur charges on your OpenAI account.


#### Generic AI Provider {: #ai_provider_generic}

In this section, you configure a generic OpenAI-compatible AI provider, for example vLLM, Ollama, LiteLLM or NeuralMagic.

The following fields are available:

* **"Provider name"**: the name under which the provider is offered for selection in the AI features.
* **"Base URL"**: the address of the OpenAI-compatible interface, for example `https://my-server:8000/v1/`.
* **"API Key (optional)"**: only needed if the server requires authentication.
* **"Available models"**: comma-separated list of the model names on this server. Needed if the models are not auto-detectable.

Use the button "Check connection" to test whether the server can be reached.

[To the top of the page ^](#ai)

---

### AI features {: #ai_functions}

You configure each AI feature separately. OpenOlat loads the available models directly from the selected provider.

**You define**:

* whether to use AI (switch "Enable feature"),
* which AI provider (field "AI Provider"),
* which model should be used (field "Language model"; "Vision model" for the Image Description Generator, "Embedding model" for Taxonomy Matching),
* and whether the feature runs for persons without a choice of their own (switch "Default for users", only for "Image Description Generator" and "Essay Grading", see [Default for users](#ai_user_default)).

**AI can be integrated into the following features**:

* Taxonomy Matching (Embeddings): assignment to the matching taxonomy level via embedding model, see [Module Taxonomy: Automatic assignment by AI >](Modules_Taxonomy.md#ai_matching) [:octicons-tag-16:{ title="from Release 21.0 (OO-9428)" }](https://track.frentix.com/issue/OO-9428){:target="_blank"}
* MC Question Generator (creation of multiple-choice questions), used in [Question Bank: Create Questions >](../../manual_user/area_modules/Question_Bank_Create_Questions.md)
* Image Description Generator (creation of image descriptions, alternative text, and keywords), used in [Information and settings for items in the Media Center >](../../manual_user/basic_concepts/Media_Center_Items.md) [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9355)" }](https://track.frentix.com/issue/OO-9355){:target="_blank"}
* Essay Question Generator (creation of open-text questions with grading criteria)
* Essay Grading (formative AI feedback on open-text answers), used in the question bank and in the [Content Editor >](../../manual_user/basic_concepts/Content_Editor.md) [:octicons-tag-16:{ title="from Release 21.0 (OO-9496)" }](https://track.frentix.com/issue/OO-9496){:target="_blank"}

The benefit of these features for authors and the places where they take effect are shown in the concept study [AI features: Application map >](../../manual_user/area_modules/AI_Features_Map.md).

![Taxonomy Matching and Image Description Generator, highlighted the switch Default for users, which decides whether the feature runs for people without a choice of their own](assets/admin_external_tools_ai_functions_v3_en.png){ class="shadow lightbox" title="AI features tab of the AI module, top · 2026.10.20" }

For the MC Question Generator you copy a subject-specific text into the designated input field. OpenOlat generates, for example, multiple-choice questions with answer options from it and pre-fills a range of metadata for each question (keywords, topic and taxonomy).

For each feature except Taxonomy Matching, the "Run test" link shows an AI-generated sample. The link appears as soon as a provider and a model are selected.

**Example MC Question Generator:**<br>
![From the input text the AI generates title, topic, keywords, question and correct and wrong answers.](assets/admin_external_tools_ai_functions_MC_v1_en.png){ class="shadow lightbox" title="MC Question Generator Test dialogue" }

**Example Image Description Generator:**<br>
![From the input image the AI generates title, description, alt text and several tags.](assets/admin_external_tools_ai_functions_image_description_v1_en.png){ class="shadow lightbox" title="Image Description Generator Test dialogue" }


#### Default for users [:octicons-tag-16:{ title="from Release 21.1 (OO-9784)" }](https://track.frentix.com/issue/OO-9784){:target="_blank"} {: #ai_user_default}

Two AI features work with the content of a person without the person calling them: the "Image Description Generator" describes every uploaded image, "Essay Grading" corrects free-text answers in a quiz. For these two features you use the switch "Default for users" to define what applies to persons who have not made a choice themselves. Every person can override the default in their personal settings in the tab "AI settings", see [Personal Configuration: Settings](../../manual_user/personal_menu/Settings.md#tab_ai_settings). The other AI features are called by a person themselves, they need no default.

* **"On"**: The feature runs for everyone who has not chosen otherwise in their personal settings.
* **"Off"**: The feature only runs for persons who have switched it on themselves.

The switch can only be operated as long as "Enable feature" is switched on. For "Essay Grading", OpenOlat asks persons without a choice of their own at the start of a quiz in the dialog "AI correction" whether the AI may correct their answers. There the default determines which button is highlighted: "Allow once" for "On", "Not now" for "Off". The dialog appears in both cases.

A changed default only applies to persons without a stored choice. You cannot set a choice for a person, but you can delete stored choices. After that the default applies, and the dialog "AI correction" asks again:

* for one person in the user management in the tab "GUI preferences" of their user account, see [Manage user settings](../usermanagement/Configure_User.md),
* for all persons in the system administration under `Administration > Core functions > GUI preferences`, with "Reset" in the row of the attributed class `org.olat.core.commons.services.ai.AiUserPreferenceService`, see [Core functions](Core_functions.md).


#### Limits per feature [:octicons-tag-16:{ title="from Release 21.0.2 (OO-9677)" }](https://track.frentix.com/issue/OO-9677){:target="_blank"} {: #ai_function_limits}

For each AI feature you additionally define how much text is sent to the model, how much text the model may produce and how long OpenOlat waits for the response. The default values are also sufficient for reasoning models, that is, models that think before answering.

* **"Maximum output tokens"**: limits how much text the model may produce. A reasoning model uses part of it to think before answering. If the value is too small, nothing is left for the answer and the call fails. Smallest permitted value: 1024.
* **"Timeout (seconds)"**: defines how long OpenOlat waits for the response of the AI provider before the call is cancelled. Reasoning models and self-hosted models take considerably longer than models in the cloud. Smallest permitted value: 10.
* **"Maximum input characters"**: limits the source text that is sent to the model for question generation. Smallest permitted value: 1000.
* **"Maximum input words"**: limits the number of words of an answer that is accepted for essay grading. OpenOlat rejects longer answers with an error message before it calls the AI. The message states the configured value. Smallest permitted value: 50.

The default values per feature:

| AI feature | Maximum input characters / input words | Maximum output tokens | Timeout (seconds) |
|---|---|---|---|
| MC Question Generator | 60000 input characters | 16384 | 180 |
| Image Description Generator | none | 8192 | 180 |
| Essay Question Generator | 60000 input characters | 16384 | 180 |
| Essay Grading | 400 input words | 16384 | 600 |

![MC Question Generator and Essay Question Generator, each with AI provider, language model, input characters, output tokens and timeout, so you see the limits of both generators at a glance](assets/admin_external_tools_ai_functions_generators_v2_en.png){ class="shadow lightbox" title="AI features tab of the AI module, middle · 2026.10.20" }

![Essay Grading with the highlighted switch Default for users below Enable feature, so you find the default for AI feedback on free-text answers](assets/admin_external_tools_ai_functions_grading_v2_en.png){ class="shadow lightbox" title="AI features tab of the AI module, bottom · 2026.10.20" }

For a reasoning model or a self-hosted model, keep the default values or increase them. If the default is not sufficient, increase the timeout first and the output tokens afterwards.

[To the top of the page ^](#ai)

---

### AI processing pools {: #ai_pools}

In the "AI processing pools" tab, you define how many AI calls are executed simultaneously per server node. The appropriate size depends on the infrastructure behind the AI provider: cloud services handle many parallel calls, a self-hosted model on a single GPU only a few.

* **Pool "Interactive" (threads)**: for AI tasks a user is actively waiting on, for example the AI correction of free-text answers.
* **Pool "Batch" (threads)**: for long-running jobs such as question generation from page content; one job can take several minutes.

By default, 8 threads are available for "Interactive" and 2 threads for "Batch". The value per pool must be between 1 and 64.

Below the two fields, the load per pool shows how many calls are currently running and how many are waiting. The "Refresh" button reloads these values.

![Highlighted load per pool with the running and waiting calls, and the highlighted button Refresh, which reloads these values](assets/admin_external_tools_ai_pools_v2_en.png){ class="shadow lightbox" title="AI processing pools tab of the AI module · 2026.10.26" }

[To the top of the page ^](#ai)

---


### Usage log [:octicons-tag-16:{ title="from Release 21.0 (OO-9393)" }](https://track.frentix.com/issue/OO-9393){:target="_blank"} {: #ai_usage_log}

The "Usage log" records every AI call on the instance, making it traceable which AI features are used how often and how many tokens are consumed. The table contains, among other things, date, AI feature, provider, model, status and duration as well as Input tokens, Output tokens and Total tokens.

The following are available for analysis:

* **Time range**: "This month" (preselected), "Last month", "This year", "Last year" as well as "Custom" for an own time range.
* **Search filters** for the columns "AI feature" and "Status".
* **Download** of the filtered table as an Excel file.

The "Total tokens" widget above the table shows the sum of all tokens in the selected time range.

![Highlighted widget Total tokens and the highlighted table of AI calls with date, AI feature, duration, status, provider and model, so you see the consumption of the selected time range](assets/admin_external_tools_ai_usagelog_v2_en.png){ class="shadow lightbox" title="Usage log tab of the AI module · 2026.10.26" }

[To the top of the page ^](#ai)

---


### Preconfiguration via olat.properties [:octicons-tag-16:{ title="from Release 20.3.4 (OO-9546)" }](https://track.frentix.com/issue/OO-9546){:target="_blank"} {: #ai_properties}

If you manage your instances centrally (e.g. with Ansible or Docker images) and the same AI provider should be preconfigured on all of them, you preset AI providers and AI features directly in the configuration file `olat.properties`.

The following priority principle applies: The values from `olat.properties` act as default values. As soon as a value is saved in the AI module, the saved value permanently takes precedence. OpenOlat loads the presets regardless of whether the provider or feature is enabled; to use them, enabling them in the AI module is all that is needed.

The two keys `user.default` stand for the switch "Default for users" and are `true` by default. An existing installation therefore behaves as before after the update, until someone changes the default or their own choice, see [Default for users](#ai_user_default).

```properties
# OpenAI (GPT) provider
ai.openai.enabled=false
ai.openai.api.key=
# Anthropic (Claude) provider
ai.anthropic.enabled=false
ai.anthropic.api.key=
# Generic OpenAI-compatible provider (e.g. vLLM, Ollama, LiteLLM)
# An empty base URL means: no generic preset provider
ai.generic.preset.enabled=false
ai.generic.preset.name=
ai.generic.preset.base.url=
ai.generic.preset.api.key=
# Comma-separated list of model names if not auto-detectable
ai.generic.preset.models=
# Enabled flag, provider (spi) and model per AI feature
# Possible spi values: OpenAI, Anthropic, Generic_0
ai.feature.mc-question-generator.enabled=false
ai.feature.mc-question-generator.spi=
ai.feature.mc-question-generator.model=
ai.feature.image-description-generator.enabled=false
ai.feature.image-description-generator.spi=
ai.feature.image-description-generator.model=
# Default for users without a choice of their own
ai.feature.image-description-generator.user.default=true
ai.feature.essay-generation.enabled=false
ai.feature.essay-generation.spi=
ai.feature.essay-generation.model=
ai.feature.essay-grading.enabled=false
ai.feature.essay-grading.spi=
ai.feature.essay-grading.model=
# Default for users without a choice of their own
ai.feature.essay-grading.user.default=true
# Limits per AI feature
ai.mc.generator.max.input.chars=60000
ai.mc.generator.max.output.tokens=16384
ai.mc.generator.timeout.seconds=180
ai.img.desc.max.output.tokens=8192
ai.img.desc.timeout.seconds=180
ai.essay.generation.max.input.chars=60000
ai.essay.generation.max.output.tokens=16384
ai.essay.generation.timeout.seconds=180
ai.essay.grading.max.input.words=400
ai.essay.grading.max.output.tokens=16384
ai.essay.grading.timeout.seconds=600
# Size of the processing pools (worker threads per node)
ai.task.pool.interactive.size=8
ai.task.pool.batch.size=2
# Taxonomy matching
taxonomy.matching.enabled=false
taxonomy.matching.spi=
taxonomy.matching.model=
# Minimum score at which a taxonomy level is assigned
taxonomy.matching.min.score=0.65
# pgvector is used automatically when available (PostgreSQL with pgvector).
# If pgvector is not available, matching still works via the in-memory search path.
taxonomy.matching.pgvector.enabled=true
taxonomy.matching.local.model.dir=${userdata.dir}/ai/models
# Optional prefix overrides. Leave empty for auto-detection based on the model name.
taxonomy.matching.query.prefix=
taxonomy.matching.passage.prefix=
```

!!! info "Important"

    The generic preset provider is available on every installation under the fixed ID `Generic_0`. It is displayed in the "AI providers" tab but cannot be deleted there. Additional generic providers are created in the "AI providers" tab.

[To the top of the page ^](#ai)

---


## Further information {: #further_information}

**Mentioned on this page**<br>
[External Tools: Overview >](External_Tools_-_Administration.md)<br>
[Assign roles >](../usermanagement/Assign_roles.md)<br>
[Module Taxonomy >](Modules_Taxonomy.md)<br>
[Question Bank: Create Questions >](../../manual_user/area_modules/Question_Bank_Create_Questions.md)<br>
[Information and settings for items in the Media Center >](../../manual_user/basic_concepts/Media_Center_Items.md)<br>
[Content Editor >](../../manual_user/basic_concepts/Content_Editor.md)<br>
[AI features: Application map >](../../manual_user/area_modules/AI_Features_Map.md)<br>
[Personal Configuration: Settings >](../../manual_user/personal_menu/Settings.md)<br>
[Manage user settings >](../usermanagement/Configure_User.md)<br>
[Core functions: Overview >](Core_functions.md)

**Further reading**<br>
[How do I create an essay question with AI grading? >](../../manual_how-to/ai_essay/ai_essay.md)<br>
[Module Media Center >](Modules_Media_Center.md)

[To the top of the page ^](#ai)
