# Barrierefreiheit: Farben {: #colors}

## Hintergrundfarben [:octicons-tag-16:{ title="ab Release 19.1 (OO-8090)" }](https://track.frentix.com/issue/OO-8090){:target="_blank"} {: #background_colors}

Ein Aspekt der [WCAG-2.1-AA-Richtlinie](https://www.w3.org/TR/WCAG21/) sind Vorgaben in Bezug auf das Kontrastverhältnis von Schriften zum jeweiligen Hintergrund. In OpenOlat werden Linkelemente mit zu hellen Farben daher automatisch abgedunkelt, sodass sie den Mindestkontrast gemäss WCAG 2.1 erfüllen. Auf grauem Hintergrund kann dies zu sichtbaren Unterschieden der Schriftfarbe gegenüber dem weissen Hintergrund führen.

In der Regel ist dies nur der Fall, wenn die gewählte Standardfarbe bereits einen sehr tiefen Kontrastwert hat. Dies kann z.B. mit folgendem Tool überprüft werden:<br>
[https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)

## Empfehlungen {: #recommendations}

A) Wenn die "Corporate Color" über einen tiefen Kontrastwert verfügt, so sollte diese nur in Layoutelementen wie dem Logo oder als Hintergrundfarbe in der Topnavigation präsent sein und nicht als Linkfarbe verwendet werden. Als Linkfarbe könnte verwendet werden:

- eine kontrastreiche Variante der Hauptfarbe
- eine Komplementärfarbe, welche mit der Hauptfarbe harmoniert
- eine sekundäre "Corporate Color"

B) Ist keine alternative Farbe für die Links möglich, so kann die automatische Kontrastanpassung deaktiviert und wieder die kontrastschwache Hauptfarbe verwendet werden. Wir weisen darauf hin, dass damit keine WCAG-AA-Konformität erreicht werden kann.

## Beispiele {: #examples}

Wir achten darauf, dass der Kontrast (insbesondere der Primärfarben) eine besonders gute Lesbarkeit ermöglicht. Zum Beispiel enthält das **Farbwahl-Werkzeug** ausschliesslich Farben, die auf Kontrast getestet sind.

![Zwölf auf Kontrast geprüfte Farben, jede mit weisser Schrift auf dem Farbfeld als Lesbarkeitsprobe, im Dropdown Farbe des Tabs Annotationen im Video-Editor](assets/accessability_color_chooser_v1_de.png){ class="shadow lightbox" }

## Weiterführende Informationen {: #further_information}

[WCAG 2.1 (W3C) >](https://www.w3.org/TR/WCAG21/)<br>
[WebAIM Contrast Checker >](https://webaim.org/resources/contrastchecker/)<br>
[Barrierefreiheit: Grundsätze >](Accessibility_Principals.de.md)<br>
[Lernressource: Video >](../learningresources/Learning_resource_Video.de.md)<br>
[Customizing: Übersicht >](../../manual_admin/administration/Customizing.de.md)

[Zum Seitenanfang ^](#colors)
