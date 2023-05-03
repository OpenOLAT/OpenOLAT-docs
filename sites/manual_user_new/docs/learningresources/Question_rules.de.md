# Frageregeln

Frageregeln (Arbeitsname: "Branching") können ab in OpenOlat im [Fragebogeneditor](../forms/Form_editor_Questionnaire_editor.de.md) eingebaut werden. Abhängig von bestimmten Antworten im Fragebaustein ![Icon Checkmark](assets/image2021-5-5_9-32-45.png){ class=size24 } "Mehrfachauswahl" und ![Icon Circle](assets/image2021-5-5_9-31-51.png){ class=size24 } "Einfachauswahl" können Aktionen ausgeführt werden.

Aktuell ist es nur möglich, bestimmte Fragecontainer anzeigen zu lassen. Dadurch können unterschiedliche Fragestränge gebaut werden.

## Erstellung einer Regel

Um eine Frageregel zu erstellen, müssen diese Bedingungen erfolgt sein:

* Mehrfachauswahl/Einfachauswahl mit mind. 1 Antwort
* Ein Container, der ein anderen Fragebaustein oder Inhalt besitzt und nicht die oben genannten Fragebausteine.

Falls die Bedingungen nicht erfüllt sind, erfolgt eine Warnung und sie können keine Regeln erstellen.

* Der Container kann zur besseren Verständigung benannt werden. Ohne eigene Benahmung enthält dieser den Standardnamen _< Unbenannt>[Container ID]_.

    !!! info "Verschiedene Ebenen"

        Durch die Verschachtelung von Containern, kann es schnell unübersichtlich werden. Empfehlenswert ist es nicht mehr als 2 verschachtelte Container mit Frageregeln zu benutzen

    ![Container benennen](assets/image2021-5-19_14-16-38.png){ class="shadow lightbox" }

* Namen sind bei Hover über den jeweiligen Container sichtbar.

    ![Container Name](assets/image2021-5-19_14-27-15.png){ class="shadow lightbox" }

* Die Frageregeln können oben rechts neben dem Administrationsmenü aufgerufen werden.

    ![Frageregeln aufrufen](assets/Fragebogen-icon.png){ class="shadow lightbox" }

* Ein neues Popup-Fenster taucht auf, das die Frageregeln beinhaltet. Auf "Regel hinzufügen", kann man diese erstellen.

    ![Dialog zu Erstellung von Frageregeln](assets/image2021-5-6_8-50-14.png){ class="shadow lightbox" }

* Links werden die "Bedingungen" definiert, rechts die "Aktionen". Zunächst kann ganz links ein Frage-Item ausgewählt werden und im zweiten Dropdown-Menü die zu bestimmende Antwort. Unter Aktion wird der Container selektiert, dessen Inhalt angezeigt werden soll. Zum Schluss die Frageregel noch unten links speichern.

    ![Frageregel Editor](assets/image2021-5-6_8-55-31.png){ class="shadow lightbox" }
