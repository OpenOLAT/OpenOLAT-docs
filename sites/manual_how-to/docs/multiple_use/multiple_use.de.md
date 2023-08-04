# Wie kann ich dieselben Dateien in mehreren Kursen einsetzen?

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
* einen [Ressourcenordner](../../manual_user/authoring/Various_Types_of_Learning_Resources.de.md#ressourcenordner)
* mehrere Kurse
* Dateien, die Sie mehrfach verwenden wollen

## Vorgehensweise:

## 1. Ressourcenordner erstellen  

1.1 Gehen Sie hierfür in den [Autorenbereich](../../manual_user/authoring/index.de.md) und wählen Sie „Erstellen“ -> „Ressourcenordner“.

![ressourcenordner_erstellen_v1_de.png](assets/ressourcenordner_erstellen_v1_de.png){ class="shadow lightbox" }  
<br>

1.2 Vergeben Sie einen passenden Namen für den Ressourcenordner und füllen Sie das allgemeine Beschreibungsformular nach Bedarf aus. Da der Ressourcenordner eher für die interne Organisation verwendet wird, ist es nicht zwingend nötig, hier Infos zu hinterlegen. Die Beschreibung der Lernressource dient hier eher Ihrer eigenen Organisation.

![ressourcenordner_erstellen_titel_v1_de.png](assets/ressourcenordner_erstellen_titel_v1_de.png){ class="shadow lightbox" }   

!!! info "Hinweis"

    Ressourcenordner werden wie andere Lernressourcen im Autorenbereich aufgelistet. Technisch gesehen, ist ein kompletter Ressourcenordner eine einzelne Lernressource.
<br>

1.3 Wählen Sie im Autorenbereich den als Lernressource aufgelisteten Ressourcenordner.

![ressourcenordner_im_autorenbereich_v1_de.png](assets/ressourcenordner_im_autorenbereich_v1_de.png){ class="shadow lightbox" }   
<br>

1.4 Hier können Sie nun Dateien hochladen und ggf. Unterordner erstellen.

Nutzen Sie [**WebDAV**](../webdav/webdav.de.md), wenn Sie viele Dateien hochladen wollen.  

Es stehen Ihnen auch die üblichen Einstellmöglichkeiten für Lernressourcen zur Verfügung (Administration -> Einstellungen).

![ressourcenordner_dateien_v1_de.png](assets/ressourcenordner_dateien_v1_de.png){ class="shadow lightbox" } 


1.5 Alternativ können Sie hier Dateien auch direkt erstellen.

![ressourcenordner_datei_erstellen_v1_de.png](assets/ressourcenordner_datei_erstellen_v1_de.png){ class="shadow lightbox" }  
 
## 2. Ressourcenordner in Kurse einbinden  

2.1 Öffnen Sie den gewünschten Kurs und wählen Sie in der "Administration" im Untermenü "Einstellungen" den Reiter "Optionen".

![ressourcenordner_einstellungen_optionen_v1_de.png](assets/ressourcenordner_einstellungen_optionen_v1_de.png){ class="shadow lightbox" } 

 <br>

2.2 Klicken Sie unter "Gewählter Ressourcenordner" auf "Auswechseln".

![ressourcenordner_auswechseln_v1_de.png](assets/ressourcenordner_auswechseln_v1_de.png){ class="shadow lightbox" }  

 <br>

2.3 Hier können Sie nun Ihren im Vorfeld erstellten Ressourcenordner auswählen und
so mit dem Kurs verlinken. Wenn Sie einen Ressourcenordner ausgewählt haben, erscheint sein Name sowie
der Button "Auswahl löschen", mit dem Sie ihn wieder abwählen können.

<br>

2.4 Standardmässig sind die Dateien des Ressourcenordners innerhalb von Kursen schreibgeschützt. Das macht Sinn, da man die Dateien ja zentral ändern und aktualisieren möchte.<br>Ist es jedoch notwendig (einzelne) zentrale Dateien noch
einmal im Kurs und zwar nur für den jeweiligen Kurs zu überschreiben, können Sie den Schreibschutz im Menü "Optionen" des Kurses entfernen.

![ressourcenordner_aendern_v1_de.png](assets/ressourcenordner_aendern_v1_de.png){ class="shadow lightbox" } 
 
  
Wiederholen Sie das Vorgehen für alle relevanten Kurse.

## 3. Zugriff auf die Dateien organisieren  

3.1 Um auf die Dateien des Ressourcenordners innerhalb des Kurses zuzugreifen, gehen Sie in den Ablageordner des Kurses. Hier finden sie den automatisch
angelegten Unterordner „_sharedfolder“.

![ablageordner_menu_v1_de.png](assets/ablageordner_menu_v1_de.png){ class="shadow lightbox" } 

![ablageordner_ohne_menu_v1_de.png](assets/ablageordner_ohne_menu_v1_de.png){ class="shadow lightbox" } 
  
3.2 Die Dateien dierses Ordners können Sie nun wie alle anderen Dateien des Ablageordners über
den Kursbaustein "[Einzelne Seite](../../manual_user/learningresources/Knowledge_Transfer.de.md#single_page)" im Kurseditor
hinzufügen.

!!! warning "Zu beachten"

    Sie können lediglich <b>einen</b> Ressourcenordner <b>pro Kurs</b> einbinden. Überlegen Sie deshalb im Vorfeld genau, welche Dateien Sie über einen kursübergreifenden Ressourcenordner statt des kursbezogenen Ablageordners organisieren möchten.