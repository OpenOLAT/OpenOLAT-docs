# Externe Werkzeuge: KI Modul {: #ai}

:octicons-tag-16: (ab Release 21)

In OpenOlat erstellte Fragen können auch KI-unterstützt erstellt werden. Dazu müssen die verwendeten KI-Tools in den externen Werkzeugen konfiguriert werden. 

Es werden z.B. Multiple-Choice-Fragen mit Antwortmöglichkeiten erstellt, sowie eine Reihe von Metadaten zu den einzelnen Frage-Items (Schlagworte, Thema und Taxonomie) vorausgefüllt.


## Tab Konfiguration {: #config}

![admin_external_tools_ai_tab_config_v1_de.png](assets/admin_external_tools_ai_tab_config_v1_de.png){ class="shadow lightbox" }



### KI Anbieter {: #ai_provider}

Aktivieren und konfigurieren Sie die KI Anbieter, die Sie verwenden möchten mit dem Button "KI Anbieter hinzufügen".

!!! hint "Beachten Sie:"

    Einerseits erlaubt das Einbinden vieler verschiedener KI-Werkzeuge die Nutzung der jeweiligen Stärken eines Tools. Andererseits trainieren KI-Tools sich selbst und berücksichtigen vorhergehende Dialoge. Werden Aufgaben an viele verschiedene KI-Tools verteilt und vergeben, hat keines der Tools die Dialoge gesamthaft zur Verfügung.



### Anthropic Claude {: #anthropic_claude}

Wenn Sie die KI Modelle von Anthropic Claude benutzen wollen, können Sie hier Ihren API Schlüssel hinterlegen. Bitte beachten Sie, dass die Verwendung des Anthropic Claude Dienstes Kosten in Ihrem Anthropic Konto verursachen kann.



### OpenAI {: #open_ai}


### Generischer KI Anbieter {: #generic_ai_provider}



### KI Funktionen {: #ai_functions}

In OpenOlat können KI-Modell an verschiedenen Stellen eingebunden werden. Im Abschnitt "KI Funktionen" bestimmen Sie für alle Einsatzorte bzw. mit KI erweiterbare Funktionen in OpenOlat

* ob KI verwendet werden soll (Toggle-Button zur Aktivierung)
* welcher KI Anbieter
* und welches Modell verwendet werden soll

Derzeit kann KI in den folgenden Funktionen eingebunden werden:

* MC-Fragengenerator (Erstellung von MC-Fragen)
* Bildbeschreibungsgenerator (Erstellung von Bildbeschreibungen, Alternativ-Texten, Schlagwörtern)
* Essay-Fragengenerator
* Essay-Bewertung

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

 