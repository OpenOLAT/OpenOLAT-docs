# Externe Werkzeuge: KI Modul {: #ai}

:octicons-tag-16: ab Release 21

In OpenOlat werden Sie an verschiedenen Stellen durch KI unterstützt. Dazu müssen die verwendeten KI-Tools in den externen Werkzeugen konfiguriert werden. 



## Tab Konfiguration {: #config}

![admin_external_tools_ai_tab_config_v1_de.png](assets/admin_external_tools_ai_tab_config_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#ai)

---


### KI Anbieter {: #ai_provider}

In OpenOlat bezieht sich der Begriff „KI Anbieter“ auf den Dienstleister, dessen KI-Modelle für die verschiedenen KI-gestützten Funktionen in der Plattform genutzt werden.

Aktivieren und konfigurieren Sie die verschiedenen KI Anbieter, die Sie verwenden möchten mit dem **Button "KI Anbieter hinzufügen"** rechts oben.

!!! hint "Beachten Sie:"

    Einerseits erlaubt das Einbinden vieler verschiedener KI-Werkzeuge die Nutzung der jeweiligen Stärken eines Tools. Andererseits trainieren KI-Tools sich selbst und berücksichtigen vorhergehende Dialoge. Werden Aufgaben an viele verschiedene KI-Tools verteilt und vergeben, hat keines der Tools die Dialoge gesamthaft zur Verfügung.

[Zum Seitenanfang ^](#ai)

---


### Anthropic Claude {: #anthropic_claude}

Wenn Sie die KI-Modelle von Anthropic Claude benutzen wollen, können Sie hier Ihren API Schlüssel hinterlegen. Bitte beachten Sie, dass die Verwendung des Anthropic Claude Dienstes Kosten in Ihrem Anthropic Konto verursachen kann.

[Zum Seitenanfang ^](#ai)

---


### OpenAI {: #open_ai}

Wenn Sie die KI-Modelle von OpenAI benutzen wollen, können Sie hier Ihren API Schlüssel hinterlegen. Bitte beachten Sie, dass die Verwendung des OpenAI Moduls Kosten in Ihrem OpenAI Konto verursachen kann.

[Zum Seitenanfang ^](#ai)

---


### Generischer KI Anbieter {: #generic_ai_provider}

In diesem Abschnitt können Sie einen generischen OpenAI-kompatiblen KI Anbieter konfigurieren, z.B.

* vLLM
* Ollama 
* LiteLLM
* NeuralMagic
* ...

Zur weiteren Spezifizierung geben Sie in einer Liste die auf diesem Server verfügbaren Modellnamen an.

[Zum Seitenanfang ^](#ai)

---


### KI Funktionen {: #ai_functions}

Die Konfiguration der KI-Integration erfolgt individuell pro Funktion, wobei die verfügbaren Modelle direkt vom jeweiligen Anbieter geladen werden.

Im Abschnitt "KI Funktionen" bestimmen Sie für alle Einsatzorte bzw. mit KI erweiterbare Funktionen in OpenOlat

* ob KI verwendet werden soll (Toggle-Button zur Aktivierung),
* welcher KI Anbieter
* und welches Modell verwendet werden soll.

Derzeit kann KI in den folgenden Funktionen eingebunden werden:

* MC-Fragengenerator (Erstellung von MC-Fragen)
* Bildbeschreibungsgenerator (Erstellung von Bildbeschreibungen, Alternativ-Texten, Schlagwörtern)
* Essay-Fragengenerator
* Essay-Bewertung

Kopieren Sie einen Fachtext in das vorgesehen Eingabefeld. Direkt in OpenOlat werden dann z.B. Multiple-Choice-Fragen mit Antwortmöglichkeiten erstellt, sowie eine Reihe von Metadaten zu den einzelnen Frage-Items (Schlagworte, Thema und Taxonomie) vorausgefüllt.

Zu jeder Funktion kann unter dem Link "Test ausführen" ein KI-generiertes Muster angesehen werden.

**Beispiel MC-Fragengenerator:**<br>
![admin_external_tools_ai_functions_MC_v1_de.png](assets/admin_external_tools_ai_functions_MC_v1_de.png){ class="shadow lightbox" }

**Beispiel Bildbeschreibungsgenerator:**<br>
![admin_external_tools_ai_functions_image_description_v1_de.png](assets/admin_external_tools_ai_functions_image_description_v1_de.png){ class="shadow lightbox" }

**Beispiel Essay-Fragengenerator:**<br>
![admin_external_tools_ai_functions_essay_question2_v1_de.png](assets/admin_external_tools_ai_functions_essay_question2_v1_de.png){ class="shadow lightbox" }

**Beispiel Essay-Bewertung:**<br>
![admin_external_tools_ai_functions_essay_grading2_v1_de.png](assets/admin_external_tools_ai_functions_essay_grading2_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#ai)

---


## Tab Nutzungsprotokoll {: #usage_log}

Im Tab "Nutzungsprotokoll" finden Sie detaillierte Nutzungsdaten, wie KI in OpenOlat verwendet wurde.

Blenden Sie sich für die benötigten Details unter dem Zahnradsymbol die entsprechenden Spalten ein. 

![admin_external_tools_ai_tab_usage_log_v1_de.png](assets/admin_external_tools_ai_tab_usage_log_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#ai)

 