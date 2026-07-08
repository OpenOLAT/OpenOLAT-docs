# External tools: AI module {: #ai}


In OpenOlat you are supported by AI at different points. To do this, the AI tools used must be configured in the external tools. The AI module supports multiple AI providers; you define per feature which provider and which model is used [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9253)" }](https://track.frentix.com/issue/OO-9253){:target="_blank"}.



## Configuration {: #config}

!!! info "Outlook on Release 21.0"

    In Release 20.3, all settings described below are displayed directly on one page under `Administration > External tools > AI module`. The screenshot shows a preview of Release 21.0: There the page is reworked and organised into the tabs "Configuration" and "Usage log". With the usage log it will be possible to trace in detail how AI is used on the instance. In addition, further AI features will be added, e.g. "Essay Question Generator" and "Essay Grading".

![admin_external_tools_ai_tab_config_v1_de.png](assets/admin_external_tools_ai_tab_config_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#ai)

---

### AI provider {: #ai_provider}

In OpenOlat, the term “AI provider” refers to the service provider whose AI models are used for the various AI-powered features on the platform.

Enable and configure the various AI providers you want to use by clicking the **"Add AI Provider" button** in the upper-right corner.

The following actions are available for each configured AI provider:

* **"Enable" toggle**: The provider can be temporarily disabled and enabled again. The configuration is retained.
* **"Check API key" button**: The stored key is validated directly with the provider. On success, the number of available models is displayed; in case of an error, the provider's error message is shown. For the generic AI provider the button is called "Check connection".
* **"Delete configuration" button**: Removes the provider including the API key and all configurations.

!!! note "Please note:"

    On the one hand, integrating many different AI tools allows users to leverage each tool’s specific strengths. On the other hand, AI tools train themselves and take previous dialogues into account. If tasks are distributed and assigned to many different AI tools, none of the tools has access to the complete history of the dialogues.

[To the top of the page ^](#ai)

---

### Anthropic Claude {: #anthropic_claude}

If you want to use Anthropic Claude's AI models, you can enter your API key here. Please note that using the Anthropic Claude service may incur charges on your Anthropic account.

[To the top of the page ^](#ai)

---

### OpenAI {: #open_ai}

If you want to use OpenAI's AI models, you can enter your API key here. Please note that using the OpenAI module may incur charges on your OpenAI account.

[To the top of the page ^](#ai)

---

### Generic AI provider {: #generic_ai_provider}

In this section, you can configure a generic OpenAI-compatible AI provider, such as

* vLLM
* Ollama 
* LiteLLM
* NeuralMagic
* ...

For further specification, list the model names available on this server.

[To the top of the page ^](#ai)

---

### AI functions {: #ai_functions}

The AI integration is configured individually for each function, with the available models being downloaded directly from the respective provider.

In the "AI functions" section, you can configure all locations and functions in OpenOlat that can be enhanced with AI.

* whether to use AI (toggle button to enable it),
* which AI provider
* and which model should be used.

Currently, AI can be integrated into the following functions:

* MC Question Generator (creation of multiple-choice questions)
* Image Description Generator (creation of image descriptions, alternative text, and keywords) [:octicons-tag-16:{ title="from Release 20.3.0 (OO-9355)" }](https://track.frentix.com/issue/OO-9355){:target="_blank"}

Copy a subject-specific text into the designated input field. OpenOlat will then automatically generate multiple-choice questions with answer options, as well as pre-fill a range of metadata for each question item (keywords, topic, and taxonomy).

For each function, you can view an AI-generated sample by clicking the "Run Test" link.

**Example MC Question Generator:**<br>
![admin_external_tools_ai_functions_MC_v1_de.png](assets/admin_external_tools_ai_functions_MC_v1_de.png){ class="shadow lightbox" }

**Example Image Description Generator:**<br>
![admin_external_tools_ai_functions_image_description_v1_de.png](assets/admin_external_tools_ai_functions_image_description_v1_de.png){ class="shadow lightbox" }

[To the top of the page ^](#ai)

---

### Preconfiguration via olat.properties [:octicons-tag-16:{ title="from Release 20.3.4 (OO-9546)" }](https://track.frentix.com/issue/OO-9546){:target="_blank"} {: #ai_properties}

AI providers and AI features can also be preset directly in the configuration file `olat.properties`. This is particularly suitable for centrally managed deployments (e.g. Ansible or Docker images) where the same AI provider should be preconfigured on all instances.

The following priority principle applies: The values from `olat.properties` act as default values. As soon as a value is saved in the administration interface, the saved value permanently takes precedence. The presets are loaded regardless of whether the provider or feature is enabled; to use them, enabling them in the administration interface is all that is needed.

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
# Provider (spi) and model per AI feature
# Possible spi values: OpenAI, Anthropic, Generic_0
ai.feature.mc-question-generator.spi=
ai.feature.mc-question-generator.model=
ai.feature.image-description-generator.spi=
ai.feature.image-description-generator.model=
```

!!! info "Important"

    The generic preset provider is available on every installation under the fixed ID `Generic_0`. It is displayed in the administration interface but cannot be deleted there. Additional generic providers can still be created via the administration interface.

[To the top of the page ^](#ai)

---


 