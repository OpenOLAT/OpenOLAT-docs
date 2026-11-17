# Wie kann ich dieselben Dateien in mehreren Kursen einsetzen? {: #multiple_use}

Wenn Sie ein Lehrszenario mit mehreren Kursen, z.B. einen Studiengang umsetzen wollen und dabei viele Dateien in allen Kursen verwendet werden sollen, bietet es sich an, diese Dateien zentral im **Ressourcenordner** abzulegen und dann in allen gewünschten Kursen einzubinden. Das hat den Vorteil, dass Sie Änderungen an den Dateien nur einmal vornehmen müssen und diese automatisch in allen verlinkten Kursen sichtbar werden.

Typische Beispiele für derartige Dateien sind:

* grundsätzliche Rahmenbedingungen,
* AGBs,
* organisatorische Infos,
* Infos zur generellen Betreuung bzw. Ansprechpartnern,
* kursübergreifende Lehrmaterialien
* usw.

## Was Sie benötigen

* Autorenrechte
* einen [Ressourcenordner](../../manual_user/learningresources/Resource_Folder.de.md)
* mehrere Kurse
* Dateien, die Sie mehrfach verwenden wollen

## Vorgehensweise: {: #procedure} 

## 1. Ressourcenordner erstellen  

1.1 Gehen Sie hierfür in den [Autorenbereich](../../manual_user/area_modules/Authoring/index.de.md) und wählen Sie "Erstellen" -> "Ressourcenordner".

![Das Menü Erstellen im Autorenbereich enthält den Eintrag Ressourcenordner](assets/ressourcenordner_erstellen_v1_de.png){ class="shadow lightbox" title="Menü Erstellen im Autorenbereich" }
<br>

1.2 Vergeben Sie einen passenden Namen für den Ressourcenordner und füllen Sie das allgemeine Beschreibungsformular nach Bedarf aus. Da der Ressourcenordner eher für die interne Organisation verwendet wird, ist es nicht zwingend nötig, hier Infos zu hinterlegen. Die Beschreibung der Lernressource dient hier eher Ihrer eigenen Organisation.

![Der Dialog zum Erstellen verlangt nur einen Titel, die übrigen Felder sind optional](assets/ressourcenordner_erstellen_titel_v1_de.png){ class="shadow lightbox" title="Dialog Ressourcenordner erstellen" }

!!! info "Hinweis"

    Ressourcenordner werden wie andere Lernressourcen im Autorenbereich aufgelistet. Technisch gesehen, ist ein kompletter Ressourcenordner eine einzelne Lernressource.
<br>

1.3 Wählen Sie im Autorenbereich den als Lernressource aufgelisteten Ressourcenordner.

![Der neue Ressourcenordner steht wie eine Lernressource in der Liste des Autorenbereichs](assets/ressourcenordner_im_autorenbereich_v1_de.png){ class="shadow lightbox" title="Liste im Autorenbereich" }
<br>

1.4 Hier können Sie nun Dateien hochladen und ggf. Unterordner erstellen.

Nutzen Sie [**WebDAV**](../webdav/webdav.de.md), wenn Sie viele Dateien hochladen wollen.  

Es stehen Ihnen auch die üblichen Einstellmöglichkeiten für Lernressourcen zur Verfügung (Administration -> Einstellungen).

![Im leeren Ressourcenordner laden Sie Dateien hoch, erstellen Ordner oder Dokumente und finden den WebDAV-Link](assets/ressourcenordner_dateien_v1_de.png){ class="shadow lightbox" title="Leerer Ressourcenordner" }


1.5 Alternativ können Sie hier Dateien auch direkt erstellen.

![Beim Erstellen eines Dokuments wählen Sie den Dateityp, etwa Text, HTML, Word, Excel oder PowerPoint](assets/ressourcenordner_datei_erstellen_v1_de.png){ class="shadow lightbox" title="Dialog Neues Dokument erstellen" }

## 2. Ressourcenordner in Kurse einbinden  

2.1 Öffnen Sie den gewünschten Kurs und wählen Sie in der "Administration" im Untermenü "Einstellungen" den Reiter "Optionen".

![Der Reiter Optionen der Kurseinstellungen enthält den Bereich Gewählter Ressourcenordner mit Auswechseln](assets/ressourcenordner_einstellungen_optionen_v1_de.png){ class="shadow lightbox" title="Reiter Optionen in den Kurseinstellungen" }

 <br>

2.2 Klicken Sie unter "Gewählter Ressourcenordner" auf "Auswechseln".

![Mit Auswechseln verknüpfen Sie einen Ressourcenordner mit dem Kurs](assets/ressourcenordner_auswechseln_v1_de.png){ class="shadow lightbox" title="Bereich Gewählter Ressourcenordner" }

 <br>

2.3 Hier können Sie nun Ihren im Vorfeld erstellten Ressourcenordner auswählen und
so mit dem Kurs verlinken. Wenn Sie einen Ressourcenordner ausgewählt haben, erscheint sein Name sowie
der Button "Auswahl löschen", mit dem Sie ihn wieder abwählen können.

<br>

2.4 Standardmässig sind die Dateien des Ressourcenordners innerhalb von Kursen schreibgeschützt. Das macht Sinn, da man die Dateien ja zentral ändern und aktualisieren möchte.<br>Ist es jedoch notwendig (einzelne) zentrale Dateien noch
einmal im Kurs und zwar nur für den jeweiligen Kurs zu überschreiben, können Sie den Schreibschutz im Menü "Optionen" des Kurses entfernen.

![Ein verknüpfter Ressourcenordner ist standardmässig schreibgeschützt, das Häkchen hebt den Schutz auf](assets/ressourcenordner_aendern_v1_de.png){ class="shadow lightbox" title="Gewählter Ressourcenordner mit Schreibschutz" }


Wiederholen Sie das Vorgehen für alle relevanten Kurse.

## 3. Zugriff auf die Dateien organisieren  

3.1 Um auf die Dateien des Ressourcenordners innerhalb des Kurses zuzugreifen, gehen Sie in den Ablageordner des Kurses. Hier finden sie den automatisch
angelegten Unterordner "_sharedfolder".

![Im Menü Administration des Kurses öffnet der Eintrag Ablageordner den Ordner mit den Kursdateien](assets/ablageordner_menu_v1_de.png){ class="shadow lightbox" title="Menü Administration im Kurs" }

![Im Ablageordner des Kurses liegt der automatisch angelegte Unterordner _sharedfolder](assets/ablageordner_ohne_menu_v1_de.png){ class="shadow lightbox" title="Ablageordner des Kurses" }

3.2 Die Dateien dieses Ordners können Sie nun wie alle anderen Dateien des Ablageordners über
den Kursbaustein "[HTML-Seite](../../manual_user/learningresources/Course_Element_HTML_Page.de.md)" im Kurseditor
hinzufügen.

!!! warning "Zu beachten"

    Sie können lediglich <b>einen</b> Ressourcenordner <b>pro Kurs</b> einbinden. Überlegen Sie deshalb im Vorfeld genau, welche Dateien Sie über einen kursübergreifenden Ressourcenordner statt des kursbezogenen Ablageordners organisieren möchten.

## Weiterführende Informationen {: #further_information}

[Ressourcenordner >](../../manual_user/learningresources/Resource_Folder.de.md)<br>
[Autorenbereich - Übersicht >](../../manual_user/area_modules/Authoring/index.de.md)<br>
[Wie kann ich mittels WebDAV Dateien übertragen? >](../webdav/webdav.de.md)<br>
[Kursbaustein "HTML-Seite" >](../../manual_user/learningresources/Course_Element_HTML_Page.de.md)

[Zum Seitenanfang ^](#multiple_use)
