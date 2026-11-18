# Content Editor

## Was ist der Content Editor? {: #content_editor}

Mit dem Content Editor gestalten Sie eine Seite aus verschiedenen Inhaltselementen, angeordnet nach einem Layout, das Sie selbst wählen. Die Seite ist für Mobilgeräte optimiert. OpenOlat speichert Ihre Änderungen automatisch.

Der Content Editor wird an verschiedenen Stellen in OpenOlat verwendet. Wer ihn nutzt, hängt vom Ort ab: im Kursbaustein "Seite" die Besitzer:innen des Kurses und berechtigte Betreuer:innen, in der Lernressource "Formular" deren Besitzer:innen, im Portfolio die Besitzer:innen der Mappe.

![Eine Seite im Bearbeitungsmodus: markierter Titel-Block mit Werkzeugleiste, rechts der Inspektor mit den Tabs Stil und Layout, darunter weitere Blöcke und der Link Inhalt hinzufügen](../assets/content_editor_v2_de.png){ class="shadow lightbox" title="Content Editor im Kursbaustein Seite · 2026.11.10" }

!!! note "Hinweis"

    Neben dem Content Editor existiert in OpenOlat noch der HTML-Editor "TinyMCE", der z.B. im [Kursbaustein "HTML-Seite"](../../learningresources/Course_Element_HTML_Page.de.md) verwendet wird. 


## Aufgaben im Content Editor {: #tasks}

Für jede Aufgabe im Content Editor gibt es eine eigene Seite:

| Seite | Wozu |
|---|---|
| [Layout](Editor_Layout.de.md) | Eine Seite in Bereiche gliedern, Inhalte darin anordnen und Abstände, Hintergrund und Hinweis-Boxen festlegen. |
| [Inhalt hinzufügen](Editor_Add_Content.de.md) | Texte, Bilder, Videos, Dokumente und weitere Inhalte einfügen, auch aus Ihrem Media Center, der Ablage für Ihre Mediendateien. |
| [Quiz und KI-Feedback](Editor_Quiz.de.md) | Im Kursbaustein "Seite" Lernenden Fragen zum Inhalt stellen und ihnen eine Rückmeldung der KI auf Freitextantworten geben. |
| [Importieren](Editor_Import.de.md) | Eine Markdown- oder Word-Datei in eine Seite übernehmen und, sofern die KI-Funktion eingerichtet ist, Fragen von der KI erzeugen lassen. |

[Zum Seitenanfang ^](#content_editor)

---


## Wo kommt der Content Editor zum Einsatz? {: #content_editor_use}

Der Content Editor wird im [Kursbaustein Seite](../../learningresources/Course_Element_Page.de.md), in der [Lernressource "Formular"](../../learningresources/Form/index.de.md) und im ["Portfolio 2.0"](../../area_modules/The_portfolio_editor_17_1.de.md) verwendet.


### Kursbaustein Seite [:octicons-tag-16:{ title="ab Release 18.0.0 (OO-6966)" }](https://track.frentix.com/issue/OO-6966){:target="_blank"} {: #course_element_page}

Im Kursbaustein "Seite" öffnen Sie den Content Editor auf zwei Wegen: im Kurseditor im Tab "Seiteninhalt" mit "Seite editieren", oder bei geschlossenem Kurseditor direkt im Kursbaustein, indem Sie den Bearbeitungsmodus einschalten. Den Kurseditor erreichen Sie unter: `Kurs > Administration > Kurseditor`.

**Bei geschlossenem Kurseditor:**

![Der Schalter Bearbeitungsmodus steht auf Aus, türkis hervorgehoben.](../assets/content_editor_page_run_mode_v1_de.png){ class="shadow lightbox" title="Kursbaustein Seite im Kurs" }

Der Schalter "Bearbeitungsmodus" schaltet die Bearbeitung der Seite ein und aus.

**Im Kurseditor:**

![Drei markierte Schritte: Kursbaustein Seite, Tab Seiteninhalt, Button Seite editieren.](../assets/content_editor_page_edit_v1_de.png){ class="shadow lightbox" title="Kursbaustein Seite im Kurseditor" }

Im Tab "Seiteninhalt" legen Sie unter "Berechtigungen" fest, ob neben den Kursbesitzer:innen auch Betreuer:innen die Seite bei geschlossenem Kurseditor bearbeiten dürfen: Option "Seite editieren" für "Betreuer:innen". Mit "Erweiterte Konfiguration anzeigen" vergeben Sie das Recht zusätzlich an einzelne Rollen, Gruppen oder Benutzer:innen, auf Wunsch mit Beginn und Ende.

![Die Option Seite editieren ist für Betreuer:innen angehakt.](../assets/content_editor_page_edit_right_coach_v1_de.png){ class="shadow lightbox" title="Tab Seiteninhalt des Kursbausteins Seite" }

Die Medien-Inhalte des [Kursbausteins "Seite"](../../learningresources/Course_Element_Page.de.md) (Bilder, Audio, Video, Diagramme, Zitate, Dokumente usw.) speichert OpenOlat im [Media Center](../../personal_menu/Media_Center.de.md), nicht im Ablageordner des Kurses wie beim [Kursbaustein "HTML-Seite"](../../learningresources/Course_Element_HTML_Page.de.md).

Auch die Medien einer Portfolio-Mappe liegen im Media Center. Die Lernressource "Formular" speichert Bilder dagegen in der Lernressource selbst.

[Zum Seitenanfang ^](#content_editor)

---


### Lernressource Formular {: #form}

Auch die [Lernressource Formular](../../learningresources/Form/index.de.md) und alle Elemente, die ein Formular nutzen, verwenden den Content Editor.

Die angezeigten Optionen zum Einfügen von Inhalt sind an das Formular angepasst, z.B. stehen hier verschiedene Fragetypen zur Auswahl.

![Der Dialog Inhalt hinzufügen im Formulareditor mit der zusätzlichen Gruppe Fragetypen.](../assets/Formular_Inhalt_hinzufuegen19.jpg){ class="shadow lightbox" title="Dialog Inhalt hinzufügen im Formulareditor" }

[Zum Seitenanfang ^](#content_editor)

---


### E-Portfolio [:octicons-tag-16:{ title="ab Release 11.0 (OO-2057)" }](https://track.frentix.com/issue/OO-2057){:target="_blank"} {: #portfolio}

Auch für Einträge in [Mappen](../../area_modules/My_portfolio_binders.de.md), die sowohl kursunabhängig als auch in Verbindung mit [Portfoliovorlagen](../../learningresources/Portfolio_template_Creation.de.md) und [Portfolioaufgaben](../../learningresources/Course_Element_Portfolio_Task.de.md) verwendet werden können, wird der Content Editor verwendet.

![Auswahl der Layout-Vorlagen mit neun Rastern, geöffnet über Neues Layout einfügen.](../assets/content_editor_layout_portfolio_v1_de.png){ class="shadow lightbox" title="Layout-Vorlagen einer Portfolio-Mappe" }

[Portfolio >](../../area_modules/The_portfolio_editor_17_1.de.md)

[Zum Seitenanfang ^](#content_editor)

---


## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Media Center: Konzept >](../Media_Center_Concept/index.de.md)<br>
[Barrierefreiheit: Grundsätze >](../Accessibility_Principals.de.md)

[Zum Seitenanfang ^](#content_editor)
