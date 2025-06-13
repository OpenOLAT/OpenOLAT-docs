# Modul Termine und Absenzen {: #module_events_and_absences}


Bevor das Modul "Termine und Absenzen" genutzt werden kann, muss es in der Administration aktiviert werden.

!!! tip "Aktivierung"
	Kunden von frentix kontaktieren für die Aktivierung bitte
	[contact@frentix.com.](mailto:contact@frentix.com.) Sobald das Modul "Termine und Absenzen" aktiviert ist, können diverse zusätzliche Einstellungen für die systemweite Konfiguration vorgenommen werden. Bei Systemen mit dem fx-Release werden diese Anpassung durch frentix vorgenommen.  
		
	:material-alert: **Nicht Hosting-Kunde von frentix?** Fragen Sie Ihren Systembetreiber!


[Zum Seitenanfang ^](#module_events_and_absences)
  
---

## Tab Konfiguration



![modules_events_and_absences_tab_configuration_v1_de.png](assets/modules_events_and_absences_tab_configuration_v1_de.png){ class="shadow lightbox" }  



### Konfiguration - auf Kursebene übersteuerbar

![1_green_24.png](assets/1_green_24.png) **Termin- und Absenzenverwaltung einschalten**

![2_green_24.png](assets/2_green_24.png) **Absenzen / Abmeldungen / Dispensen einschalten**

![3_green_24.png](assets/3_green_24.png) **Überschreiben der Standard-Konfiguration zulassen**: Die Standard-Konfiguration, welche in der Administration gesetzt wird, kann auf Kursebene
überschrieben werden. Dies gilt nicht für die "Globale Konfiguration".

![4_green_24.png](assets/4_green_24.png) **Anwesenheitskontrolle einschalten**: Nur wenn diese Optionen eingeschaltet
ist, kann ich eine Anwesenheitskontrolle durchführen und sehe die
Teilnehmenden und die Checkboxen.

![5_green_24.png](assets/5_green_24.png) **Berechnung der Anwesenheitsrate**: Wenn diese Option eingeschaltet ist,
wird eine Prozentquote der Anwesenheit berechnet.

![6_green_24.png](assets/6_green_24.png) **Absenzenquote global in %**: Diese Quote gibt an, wie viel Prozent
Anwesenheit gefordert ist, um die Bedingungen eines Kurses zu erfüllen.

![7_green_24.png](assets/7_green_24.png) **Dozentenkalender synchronisieren**: Dozierende (Kursbetreuer) bekommen
Einträge in ihrem persönlichen Kalender (nicht im Kurskalender) für diejenigen
Lektionenblöcke, bei welchen sie als Dozierende zugewiesen sind (Für Px-Kunden
muss diese Funktion ausgeschaltet sein).

![8_green_24.png](assets/8_green_24.png) **Kurskalender synchronisieren**: Durch diese Option werden die erfassten
Lektionenblöcke gleich direkt im Kurskalender angezeigt für alle Teilnehmer,
Dozenten und Kursbesitzer.

![9_green_24.png](assets/9_green_24.png) **Prüfungsmodus für Lektionen erlauben**

![10_green_24.png](assets/10_green_24.png) **Vorlaufzeit**

![11_green_24.png](assets/11_green_24.png) **Nachlaufzeit**

![12_green_24.png](assets/12_green_24.png) **Erlaubte IP-Adressen**

![13_green_24.png](assets/13_green_24.png) **Safe Exam Browser - Art der Benutzung**

![14_green_24.png](assets/14_green_24.png) **Herunterladbare Konfigurationsdatei**



### Globale Konfiguration

![15_green_24.png](assets/15_green_24.png) **Tageserfassung Absenzen**: ja oder nein

![16_green_24.png](assets/16_green_24.png) **Termine partiell durchgeführt zulassen**: Beim Abschliessen eines Lektionenblocks kann unter "Effektive Lektionen" die Anzahl Lektionen
ausgewählt werden, welche tatsächlich durchgeführt worden sind. Die
Anwesenheitsquote wird dadurch auch nur partiell berechnet.

![17_green_24.png](assets/17_green_24.png) **Terminstatus** : Wenn diese Option gewählt wird, können ganze
Termine abgesagt werden. Dieser Termin zahlt dann nicht zur Anwesenheitsquote.

![18_green_24.png](assets/18_green_24.png) **Default Anzahl von geplanten Einheiten**

![19_green_24.png](assets/19_green_24.png) **Erinnerungsfunktion einschalten**: Hiermit wird die Erinnerungsfunktion
aktiviert. Anschliessend sind die Erinnerungs- und die Sperrfrist zu
definieren.

![20_green_24.png](assets/20_green_24.png) **Erinnerungsfrist**: Hier wird die Erinnerungsfrist in Anzahl Tagen eingetragen. Nachdem diese Anzahl Tage erreicht worden ist, wird der/die Dozent:in daran erinnert, die Anwesenheitskontrolle durchzuführen. Ein Tag entspricht 24 Stunden und die Zählung beginnt beim eingetragenen Ende des Termins.

![21_green_24.png](assets/21_green_24.png) **Sperrfrist**: Wiederum wird die Anzahl Tage eingetragen. Nachdem diese Frist abgelaufen ist, wird der Status des Termins automatisch auf erledigt gesetzt. Die bereits eingetragene Anwesenheitskontrolle wird gespeichert. Falls nichts eingetragen ist, werden alle Teilnehmenden als anwesend gespeichert. Die Sperrfristzählung beginnt am Folgetag, nachdem der Termin die Endzeit erreicht hat und läuft bis am Ende des Tages.

![22_green_24.png](assets/22_green_24.png) **Entschuldigte Absenzen**: Diese Option erlaubt Absenzen zu entschuldigen. Wenn diese Option nicht aktiviert ist, gelten alle Absenzen als unentschuldigt.

![23_green_24.png](assets/23_green_24.png) **Entschuldigte Absenzen als anwesend zählen**: Mit dieser Option werden die Absenzen, welche entschuldigt sind, für die Berechnung der Absenzenquote als anwesend gerechnet.

![24_green_24.png](assets/24_green_24.png) **Absenzen standardmässig als entschuldigt zählen**: Grundsätzlich gelten
eingetragene Absenzen als unentschuldigt. Diese Option setzt alle
eingetragenen Absenzen automatisch auf entschuldigt. Falls dies nicht
zutrifft, muss die Absenz manuell auf unentschuldigt gesetzt werden.

![25_green_24.png](assets/25_green_24.png) **Kursbesitzer dürfen alle Kurse in Elementen sehen**

![26_green_24.png](assets/26_green_24.png) **Rekursmöglichkeit gewähren**: Wenn die Rekursfrist aktiviert ist, bekommen
die Kursteilnehmenden die Möglichkeit, für eine eingetragenen Absenz Rekurs
einzureichen. Dies kann beispielsweise notwendig sein, wenn eine Absenz im
Nachhinein als entschuldigt anerkannt wird oder wenn der Dozierende eine
Absenz falsch eingetragen hat.

![27_green_24.png](assets/27_green_24.png) **Rekursfrist**: Die Rekursfrist beginnt, sobald der Termin erledigt ist. Entweder hat der Dozent den Termin manuell auf erledigt gesetzt oder die Sperrfrist ist abgelaufen und der Termin wurde automatisch auf erledigt gesetzt. Die Zählung der Tage beginnt am Folgetag, nachdem der Status des Termins auf erledigt gesetzt worden ist. Anschliessend werden ganze
Tage gezählt, Rekursfristschluss ist jeweils am Ende des Tages.

![28_green_24.png](assets/28_green_24.png) **Anzeige in Kursen**: Termine aller Dozenten oder nur eigene


[Zum Seitenanfang ^](#module_events_and_absences)
  
---


## Tab Berechtigungen

In diesem Tab werden die Berechtigungen für Dozenten / Klassenlehrer hinsichtlich der Termine und Absenzen festgelegt.

![modules_events_and_absences_tab_permissions_v1_de.png](assets/modules_events_and_absences_tab_permissions_v1_de.png){ class="shadow lightbox" }  



[Zum Seitenanfang ^](#module_events_and_absences)
  
---


## Tab Begründungen Termine

Termine können automatisch oder manuell beendet werden. Wird ein Termin z.B. früher beendet, soll dafür ein Grund angegeben werden. Der **Grund für einen abweichenden Terminabschluss** kann aus einer Liste ausgewählt werden.

Die zur Auswahl stehenden Begriffe und Beschreibungen für diese Begründungen können hier durch Administrator:innen definiert werden.

Werden hier keine Begründungen hinterlegt, erscheint die Begründungsauswahl beim Schliessen des Termins
nicht.


[Zum Seitenanfang ^](#module_events_and_absences)
  
---


## Tab Begründungen Absenzen

In der Kursadministration können Besitzer:innen/Betreuer:innen Absenzen erfassen. 
Für die Begründung der Absenzen kann dabei aus verschiedenen Begriffen ausgewählt werden, wie z.B. "Krankheit", "Unfall", "Dozent:in krank", u.ä.

Diese dort angebotene Auswahl an Begriffen und Beschreibungen kann hier definiert werden.  

[Zum Seitenanfang ^](#module_events_and_absences)
  
---


## Tab Report

Hier können Reports für bestimmte Zeiträume angezeigt werden. Es kann nach dem Status der Termine /Absenzen vorselektiert werden:

- Offen
- Erledigt
- Autoerledigt
- Wiedergeöffnet

Alle Reports können auch als Excel-Datei heruntergeladen werden.

[Zum Seitenanfang ^](#module_events_and_absences)
  
