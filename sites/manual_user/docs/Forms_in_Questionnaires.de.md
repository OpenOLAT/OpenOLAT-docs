#  [Formular in Umfragen](Formular+in+Umfragen.html)

Die Lernressource Formular wird im Kursbaustein "Umfrage" in Form eines
Fragebogens verwendet. Kursbesitzer können so Fragebögen in ihren Kurs
einbinden und Lernende können die bereitgestellten Umfragen ausfüllen. Die
Ergebnisse werden den Kursbesitzern und Betreuern, dann entsprechend im
angezeigt.

OpenOlat stellt sicher, dass Kursteilnehmende die Umfrage bzw. den Fragebogen
nur einmal ausfüllen können. Die Resultate werden standardmässig anonymisiert
gespeichert. Eine Personalisierung ist jedoch durch die Auswahl der passenden
Formular Elemente [Formular Editor](Formular+Editor.html) möglich.

Wie Sie Formulare erstellen und in Kurse einbinden erfahren Sie
[hier](Drei+Schritte+zu+Ihrem+Formular.html).

## Im Kurseditor:

Gehen Sie in den Kurseditor und fügen Sie den Kursbaustein Umfrage hinzu.
Nachdem Sie den Kursbaustein Umfrage dem Kurs hinzugefügt haben stehen Ihnen
im Kurseditor folgende Tabs zur Verfügung:

![](../../download/attachments/590041/Umfrage_Kurseditor.png)

  

Im Tab "Titel und Beschreibung" sowie "Layout" können allgemeine
Beschreibungen und Informationen zum jeweiligen Kursbaustein hinterlegt und
die optische Darstellung definiert werden. Im [Tab Lernpfad
](Lernpfad+Kurs++-+Kurseditor.html)werden spezielle Einstellungen die für
Lernpfad Kurse gelten definiert, z.B. kann als Erledigungskriterium "Umfrage
teilgenommen" gewählt werden.

Herkömmliche Kurs verfügen dagegen über die Tabs Sichtbarkeit und Zugang. Hier
wird definiert, wer diesen Kursbaustein sehen bzw. bearbeiten kann.

## Tab Umfrage im Kurseditor

Die zentrale Konfiguration erfolgt im Tab "Umfrage". Hier wird im ersten
Schritt entweder ein neues Formular erstellt oder ein existierendes
ausgewählt. In der erscheinenden Übersicht werden alle Formulare, bei denen
man Besitzer ist, angezeigt und können einfach per Klick auf den Haken
ausgewählt und so dem Kurs hinzugefügt werden.

![](../../download/attachments/108593751/Formular_auswahlmenue1%EF%B9%96version=1&modificationDate=1638725267000&api=v2.jpg)

Hat man noch kein Formular erstellt, kann eine neue Lernressource Formular
über den Button "Erstellen" erstellt oder ein extern vorliegendes Formular
importiert werden. Anschließend erscheint das gerade angelegte oder
importierte Formular ebenfalls in der Liste und kann ausgewählt werden.

Ein neu erstelltes Formular beinhaltet zunächst noch keine Elemente, Fragen
oder Textfelder. Diese müssen im Kurs über "Bearbeiten" oder alternativ direkt
in der Lernressource im [Formular Editor](Formular+Editor.html) hinzugefügt
werden.

Wenn ein Formular direkt im Kurseditor erstellt wird, wird automatisch eine
neue Lernressource Formular angelegt, die auch im [Autorenbereich
](Autorenbereich.html)unter "Meine Einträge" zu finden ist und in weiteren
Kursen eingebunden werden kann.

Nachdem ein Formular ausgewählt wurde kann es über den Link "Bearbeiten"
gestaltet werden. Wurde das Formular schon vorher passend eingerichtet ist
eine Bearbeitung nicht mehr notwendig.

![](../../download/attachments/590041/Umfrage_Tab.png)  

  

Anschliessend kann definiert werden, wer dir Umfrage ausfüllen und wer die
Ergebnisse der Umfrage sehen kann. Folgende Optionen können jeweils gewählt
werden:

  * die Besitzer des Kurses
  * die Betreuer des Kurses
  * die Teilnehmenden des Kurses: Alle Personen die in der Rolle „Teilnehmer“ in den Kurs eingetragen sind
  * Gäste: Personen ohne OpenOlat-Account

Aktiviert man die erweiterte Konfiguration, können noch weitere Einstellungen
vorgenommen werden, z.B. bestimmte Zeiträume der Teilnahme für bestimmte
Rollen definiert werden und die Teilnahme durch bestimmte Gruppen festgelegt
werden.

Auch die Ergebnisse können für all diese Gruppen frei gegeben und in der
erweiterten Konfiguration mit einem Beginn und Ende Datum verbunden werden.

Voraussetzung für die Bearbeitung der Umfrage ist jedoch, dass der gesamte
Kurs auch für die jeweilige Personengruppe freigegeben ist. Soll also
beispielsweise eine Umfrage auch von externen Personen (Gästen) ausfüllbar
sein, muss auch der Kurs im Menü „Einstellungen“- > unter [Freigabe
](Zugangskonfiguration.html)„offen ohne Buchung" für Gaste frei gegeben sein.

Wird ein Formular als Umfrage in einem Kurs eingebunden, kann das Formular im
Kurs über den Button „bearbeiten“ eingeschränkt geändert werden. Texte können
geändert aber einzelne Blöcke nicht mehr verschoben oder neue Bereiche
angelegt oder gelöscht werden. Im Formular erscheint die Meldung "Die
Ressource wird bereits verwendet...".

Sobald ein Formular von mindestens einem Teilnehmenden angesehen wurde, kann
es nicht mehr ersetzt werden. Der Button "Ersetzen" entfällt dann.

## Ansicht bei geschlossenem Kurseditor

Was Besitzer, Betreuer und Teilnehmende bei geschlossenem Editor sehen ist
davon abhängig welche Benutzerberechtigungen im Tab Umfrage ausgewählt wurden.
Hat die jeweilige Personengruppe das Recht den Fragebogen auszufüllen
(Teilnahme durch...), dann sieht sie als erstes auch den jeweiligen
Fragebogen.  Sobald die Person aber selbst den Fragebogen ausgeüllt hat,
erscheint die Fragebogen Statistik Übersicht direkt bei dem jeweiligen Umfrage
Baustein, sofern für die Benutzergruppe auch die Resultate sichtbar sind.

![](../../download/attachments/590041/Umfrage_Kurs%EF%B9%96version=1&modificationDate=1638726817000&api=v2.jpg)

Ist eine Personengruppe (z.B. Lernende) berechtigt die Umfrage auszufüllen
aber nicht berechtigt die Ergebnisse zu sehen, erscheint nach dem Ausfüllen
die Meldung:

![](../../download/attachments/590041/Umfrage_ausgefuellt%EF%B9%96version=1&modificationDate=1638727177000&api=v2.jpg)

Die Umfrage kann nur einmal ausgefüllt und nach dem abschicken nicht mehr
geändert werden. Der User sieht eine entsprechende Information. Soll der
Fragebogen noch nicht direkt abgeschickt werden, kann die Option
„Zwischenspeichern“ verwendet werden.

Ist eine Personengruppe weder berechtigt den Fragebogen auszufüllen noch die
Resultate zu sehen, erscheint die Meldung "kein Zugang"

  

## Ansicht der Resultate einer Umfrage

Folgende Auswertungstabs stehen den Berechtigten zur Verfügung:

  
|  
  
---|---  
Übersicht| Hier erfährt man wie viele Personen den Fragenbogen ausgefüllt
haben, den Abgabezeitraum sowie die Bearbeitungsdauer. Je nach Fragetyp werden
auch noch weitere Kennzahlen aufgeführt.  
Tabellen| Hier sehen Sie die einzelnen Fragen und Antworten sowie bei Rubriks
weitere statistische Auswertungen. Freitexte können zusätzlich als Excel
Tabelle heruntergeladen werden.  
Diagramme| Im Tab Diagramme sehen Sie eine grafische Darstellung der einzelnen
Fragen  
Einzelne Fragebögen| Hier hat man Zugriff auf die gesamten ausgefüllten,
anonymen Fragebogen einzelner Personen.  
  
Ferner können die Inhalte aller 4 Tabs auch ausgedruckt oder als Excel Tabelle
oder als PDF-Version heruntergeladen werden.

Dieselbe Auswertung finden Sie auch im Menü „Administration“ -> „Fragebogen
Statistiken“.

Die Ergebnisse können auch über das Menü
"[Datenarchivierung](Einsatz+der+Kurswerkzeuge.html)"  -> “Umfragen“
gespeichert werden. Es handelt sich dabei um dieselbe Datei wie unter „Export“
im Kursrun.

### Umfragen zurücksetzen

Kursbesitzer können schon ausgefüllte Fragebögen auch über den Link im
3-Punkte Menü des jeweiligen Kursbaustein „Zurücksetzen“. In diesem Fall
werden alle bereits eingereichten Fragebögen für diese Umfrage gelöscht. Ein
Zurücksetzen von einzelnen Fragebögen ist nicht möglich, da die Abgabe anonym
erfolgt.

![](../../download/attachments/590041/Umfrage_zuruecksetzen%EF%B9%96version=1&modificationDate=1638727621000&api=v2.jpg)

Ferner können die Inhalte aller 4 Tabs auch ausgedruckt oder als Excel Tabelle
oder als PDF-Version heruntergeladen werden.

  

