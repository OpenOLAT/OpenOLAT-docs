# Lektionen- und Absenzenmanagement

Bevor das Lektionen- und Absenzenmanagement genutzt werden kann, muss dies in
der Administration aktiviert werden. Kunden von frentix kontaktieren dafür
bitte [contact@frentix.com.](mailto:contact@frentix.com.) Sobald das
Lektionen- und Absenzenmanagement aktiviert ist, können diverse zusätzliche
Einstellungen für die systemweite Konfiguration vorgenommen werden. Bei
Systemen mit dem fx-Release werden diese Anpassung durch frentix vorgenommen.

# Modul Lektionen

## Tab Berechtigungen

Hier wird das Lektionen- und Absenzmanagement sowie Absenzen/Dispenzen
eingeschaltet.

### Konfiguration - auf Kursebene übersteuerbar

 **Überschreiben der Standard-Konfiguration zulassen** : Die Standard-
Konfiguration, welche in der Administration gesetzt wird, kann auf Kursebene
überschrieben werden. Dies gilt nicht für die "Globale Konfiguration".

 **Anwesenheitskontrolle einschalten** : Nur wenn diese Optionen eingeschaltet
ist, kann ich eine Anwesenheitskontrolle durchführen und sehe die
Teilnehmenden und die Checkboxen.

 **Berechnung der Anwesenheitsrate** : Wenn diese Option eingeschaltet ist,
wird eine Prozentquote der Anwesenheit berechnet.

 **Absenzenquote global in %**: Diese Quote gibt an, wie viel Prozent
Anwesenheit gefordert ist, um die Bedingungen eines Kurses zu erfüllen.

 **Dozentenkalender synchronisieren** : Dozierende (Kursbetreuer) bekommen
Einträge in ihrem persönlichen Kalender (nicht im Kurskalender) für diejenigen
Lektionenblöcke, bei welchen sie als Dozierende zugewiesen sind (Für Px-Kunden
muss diese Funktion ausgeschaltet sein).

 **Kurskalender synchronisieren** : Durch diese Option werden die erfassten
Lektionenblöcke gleich direkt im Kurskalender angezeigt für alle Teilnehmer,
Dozenten und Kursbesitzer.

 **Prüfungsmodus für Lektionen erlauben**

  

### Globale Konfiguration

 **Tageserfassung Absenzen** : ja oder nein

 **Lektionen partiell durchgeführt zulassen** : Beim Abschliessen eines
Lektionenblocks kann unter "Effektive Lektionen" die Anzahl Lektionen
ausgewählt werden, welche tatsächlich durchgeführt worden sind. Die
Anwesenheitsquote wird dadurch auch nur partiell berechnet.

 **Lektionen Status** : Wenn diese Option gewählt wird, können ganze
Lektionenblöcke abgesagt werden. Dieser Lektionenblock zahlt dann nicht zur
Anwesenheitsquote.

 **Erinnerungsfunktion einschalten** : Hiermit wird die Erinnerungsfunktion
aktiviert. Anschliessend sind die Erinnerungs- und die Sperrfrist zu
definieren.

 **Erinnerungsfrist** : Hier wird die Erinnerungsfrist in Anzahl Tagen
eingetragen. Nachdem diese Anzahl Tage erreicht worden ist, wird der/die
DozentIn daran erinnert, die Anwesenheitskontrolle durchzuführen. Ein Tag
entspricht 24 Stunden und die Zählung beginnt beim eingetragenen Ende des
Lektionenblocks.

 **Sperrfrist** : Wiederum wird die Anzahl Tage eingetragen. Nachdem diese
Frist abgelaufen ist, wird der Status des Lektionenblocks automatisch auf
erledigt gesetzt. Die bereits eingetragene Anwesenheitskontrolle wird
gespeichert. Falls nichts eingetragen ist, werden alle Teilnehmenden als
anwesend gespeichert. Die Sperrfristzählung beginnt am Folgetag, nachdem der
Lektionenblock die Endzeit erreicht hat und läuft bis am Ende des Tages.

 **Entschuldige Absenzen** : Diese Option erlaubt Absenzen zu entschuldigen.
Wenn diese Option nicht aktiviert ist, gelten alle Absenzen als
unentschuldigt.

 **Entschuldigte Absenzen als anwesend zählen** : Mit dieser Option werden die
Absenzen, welche entschuldigt sind, für die Berechnung der Absenzenquote als
anwesend gerechnet.

 **Dispense als anwesend zählen** : ja, nein

 **Absenzen standardmässig als entschuldigt zählen** : Grundsätzlich gelten
eingetragene Absenzen als unentschuldigt. Diese Option setzt alle
eingetragenen Absenzen automatisch auf entschuldigt. Falls dies nicht
zutrifft, muss die Absenz manuell auf unentschuldigt gesetzt werden.

 **Kursbesitzer dürfen alle Kurse in Curriculum Elementen sehen**

 **Rekursmöglichkeit gewähren** : Wenn die Rekursfrist aktiviert ist, bekommen
die Kursteilnehmenden die Möglichkeit, für eine eingetragenen Absenz Rekurs
einzureichen. Dies kann beispielsweise notwendig sein, wenn eine Absenz im
Nachhinein als entschuldigt anerkannt wird oder wenn der Dozierende eine
Absenz falsch eingetragen hat.

 **Rekursfrist** : Die Rekursfrist beginnt, sobald der Lektionenblock erledigt
ist. Entweder hat der Dozent den Block manuell auf erledigt gesetzt oder die
Sperrfrist ist abgelaufen und der Lektionenblock wurde automatisch auf
erledigt gesetzt. Die Zählung der Tage beginnt am Folgetag, nachdem der Status
des Lektioneblocks auf erledigt gesetzt worden ist. Anschliessend werden ganze
Tage gezählt, Rekursfristschluss ist jeweils am Ende des Tages.

 **Anzeige in Kursen:** alle Lektionenblöcke oder nur eigene

## Tabs Begründungen für Lektionen und Absenzen

In der Administration werden auch die Begründungen erfasst und zwar jeweils
mit einem Titel und einer Beschreibung. Diese Begründungen können nur hier
erfasst und bearbeitet werden. Dozenten können keine eigenen Begründungen
erfassen.

Immer wenn ein Lektionenblock geschlossen wird, muss eine Begründung
ausgewählt werden. Wenn in der Administration keine Begründungen hinterlegt
sind, erschient die Begründungsauswahl beim Schliessen des Lektionenblocks
nicht.

![](assets/Absenz_Begruendung.png)

## Tab Lektionenblockreport

Hier können Reports für bestimmte Zeiträume angezeigt werden.

