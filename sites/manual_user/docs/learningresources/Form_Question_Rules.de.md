# Frageregeln in Formularen

Mit Frageregeln kann die Anzeige von Layout-Bereichen in Abhängigkeit von bestimmten Antworten der Einzel- oder Mehrfachauswahl (Bedingungsfeld) gesetzt werden. So wird ein Layout-Container mit den jeweiligen Elementen nur dann angezeigt, wenn Nutzende eine bestimmte vorgegebene Antwort ausgewählt haben.

Einem Formular können mehrere Regeln hinzugefügt werden. Dadurch können unterschiedliche Fragestränge erstellt werden.

## Erstellung einer Regel

Überlegen Sie sich zunächst, welche Bereiche Sie bei welcher Auswahl anzeigen wollen und setzen diese dann mit Hilfe der Frageregeln für das Formular um.

### Voraussetzungen
Um eine Frageregel zu erstellen, müssen folgende Bedingungen erfüllt sein:

* Mehrfachauswahl oder Einzelauswahl mit mind. 1 Antwort
* Ein Container-Layout, das einen anderen Fragebaustein oder Inhalt besitzt und nicht die oben genannten Fragebausteine.

Falls die Bedingungen nicht erfüllt sind, erfolgt eine Warnung und Sie können keine Regeln erstellen.

### Passende Namen vergeben

Wichtig, um den Überblick zu behalten, sollten Sie unbedingt für alle Layout- und Inhaltselemente, die Sie für die Frageregeln benötigen, sinnvolle Bezeichnungen vergeben. Dies erfolgt über den Inspektor, den Sie jeweils über das Zahnrad-Symbol aufrufen können, wenn er nicht bereits sichtbar ist.

Hier tragen Sie den Namen für ein Container-Layout-Element ein:

![Name eines Layout-Elements im Tab "Name" des über das Zahnrad-Symbol geöffneten Inspektors eintragen, hier "Sorten"](assets/Formular_Conatiner_Name1.jpg){ class="shadow lightbox" }

So tragen Sie den Namen für ein Einzel- oder Mehrfachauswahl-Element ein:

![Name eines Mehrfachauswahl-Elements im Tab "Allgemein" des über das Zahnrad-Symbol geöffneten Inspektors eintragen, hier "Obst"](assets/Formular_Name1.jpg){ class="shadow lightbox" }

### Frageregeln im Menü hinterlegen
Die Frageregeln können oben, rechts neben dem Administrationsmenü, aufgerufen werden.

![Symbol "Frageregeln" markiert, rechts neben "Administration" oben im Formular-Editor](assets/Fragebogen-icon.png){ class="shadow lightbox" }

Ein neues Popup-Fenster erscheint, in dem Frageregeln erstellt und angezeigt werden können.

![Leerer Zustand des Dialogs Frageregeln vor der ersten Regel, mit Button "Regel hinzufügen"](assets/image2021-5-6_8-50-14.png){ class="shadow lightbox" }

Eine Frageregel besteht immer aus einer Bedingung mit verschiedenen Optionen und einer zugeordneten Aktion, die angezeigt wird. Die Bedingung ist eine Mehrfachauswahl oder Einzelauswahl mit den konkreten Antwortmöglichkeiten. Für jede Antwortmöglichkeit kann dann ein Layout-Container ausgewählt werden, der z.B. konkrete Informationen oder weitere Fragen enthält. Speichern nicht vergessen.

![Drei Frageregeln, je mit Bedingung wie "MC Obst ist Kiwi" links und zugeordneter Aktion wie "zeige Container 2 mit Textelement" rechts](assets/Frageregeln_Beispiel.png){ class="shadow lightbox" }
