# Badges {: #badges}

## Was ist ein Badge? {: #what_is_a_badge}

Open Badges ist ein System digitaler Zertifikate oder **Lernabzeichen**, mit dem Sie individuelle Fortschritte auszeichnen können.<br>
Ein Badge ist ein Online-Beweis für ein erreichtes Ziel. Er besteht aus

* einem Bild (svg oder png)
* (evtl. mit einem editierbaren Schlüsselbegriff auf dem Bild)
* Metainformation (Beschreibung des erreichten Ziels, Gültigkeitsdauer des Badges, Aussteller des Badges, Datum der Ausstellung, usw.)
* einem Link

Der Unterschied zwischen einem Papier-Zertifikat und einem Online-Badge besteht darin, dass der Badge online über Links geteilt werden kann. So kann er z.B. in Lebenslauf, Portfolio mitgegeben werden.
Ein Badge-Erwerber kann z.B. auch auf seinem LinkedIn-Profil die Badges einbinden.

Im Unterschied zu einem formalen Zertifikat, ist die Idee des Badges eher spielerisch (Gamifikation, zur Auflockerung und Motivation, die Lerner:innen gewinnen etwas).



---

## Wo können Badges erworben werden? {: #badge_categories}

Es können grundsätzlich 3 Kategorien von Badges erworben werden:

* **Badges für einen Kurs**<br> (für das Bestehen des Kurses, bzw. das Erfüllen der dort gestellten Bedingungen)
* **Badges für einen bestimmten Kursbaustein**<br> (wie Kursbadges, mit einer Bedingung für einen bestimmten Kursbaustein, [siehe Liste der Kursbausteine mit Badges](#create_for_course_elements))
* und **globale Badges**<br> (kursübergreifend, können nur von Administrator:innen erstellt werden) 

Globale Badges sind unabhängig von Kursen. Andere Badges beziehen sich auf einen spezifischen Kursbaustein oder Kurs. Der gleiche Badge kann nicht an unterschiedlichen Stellen, z.B. für unterschiedliche Kursbausteine vergeben werden.

[Zum Seitenanfang ^](#badges)

---

## Wie werden Kurs-Badges vergeben? {: #award_a_course-badge}

Sie können manuell oder automatisch anhand definierter Regeln vergeben werden.

### Kurs-Badges manuell vergeben

In jedem Kurs kann unter<br>
**Administration > Einstellungen > Tab Bewertung > Abschnitt "Badges"**<br>
eine manuelle Vergabe durch Kursbesitzer:innen und Betreuer:innen ermöglicht werden.

### Kurs-Badges im Bewertungstool vergeben

Badges können im Bewertungstool manuell auch über eine Massenaktion vergeben werden.

### Kurs-Badges automatisch vergeben

Während der Erstellung eines Badges mit dem Wizard können im Schritt "Vergabekriterien" Regeln für die automatische Vergabe eines Badges festgelegt werden.

[Zum Seitenanfang ^](#badges)

---

## Wie werden globale Badges vergeben? {: #award_a_course-badge}

Auch globale Badges können manuell oder automatisch anhand definierter Regeln vergeben werden.
Sowohl manuelle Vergabe, wie auch die Definition der Regeln für eine automatische Vergabe globaler Badges können jedoch nur durch [Administrator:innen](../../manual_admin/administration/e-Assessment_openBadges.de.md) erfolgen.

### Globale Badges manuell vergeben

Globale Badges können durch Administrator:innen manuell vergeben werden unter<br>
**Administration > e-Assessment > OpenBadges > Tab "Globale Badges" > Button "Badge manuell vergeben"**.<br>

### Globale Badges automatisch vergeben

Administrator:innen können die Regeln für eine automatische Vergabe einrichten unter<br>
**Administration > e-Assessment > OpenBadges > Tab "Globale Badges"**.<br>
Wenn dort das Badge-Tool zur Erstellung eines globalen Badges aufgerufen wird, können im Wizard die Regeln angegeben werden. 

[Zum Seitenanfang ^](#badges)


---

## Erstellen und Bearbeiten eines Badges {: #create}

Badges können innerhalb eines Kurses grundsätzlich nur durch Kursbesitzer:innen erstellt werden.


### Wo können Badges für _Kursbausteine_ erstellt werden? {: #create_for_course_elements}

**Im Kurseditor:**<br> 
Kursbausteine, die ein "Bestanden" ausgeben können, haben einen zusätzlichen Tab "Badges". Dort finden Sie einen Button "Neuen Badge erstellen".
Er ist vorhanden bei den Kursbausteinen:

* Test
* SCORM-Lerninhalt
* Aufgabe
* Gruppenaufgabe
* Bewertung
* Checkliste
* LTI-Seite
* Teilnehmer:innenordner
* Portfolioaufgabe
* Struktur

[Zum Seitenanfang ^](#badges)


### Wo können Badges für den _Kurs_ erstellt werden?

**Im Kurseditor:**<br>
Auch bei Klick auf dem obersten "Knoten", den Kurstitel im Kursmenü, erscheint rechts ein Tab "Badges". Sie erstellen dort wie bei den Kursbausteinen einen Badge durch Klick auf den Button "Neuen Badge erstellen". Hier bezieht sich der Badge jedoch auf den Kurs als Ganzes. 

**Unter Administration > Badges**:<br>
Hier erscheint ein Liste aller Badges, die in diesem Kurs erworben werden können. Mit dem Button "Neuen Badge erstellen" können weitere Badges für den Kurs und/oder einzelne Kursbausteine erstellt werden.

Eine Schritt-für-Schritt-Anleitung für **Kurs-Badges** finden Sie [hier](../../manual_how-to/badges/badges.de.md).


[Zum Seitenanfang ^](#badges)


### Wo können _globale_ Badges erstellt werden?

Die Möglichkeit zur Erstellung von **globalen Badges** finden Sie [hier](../../manual_admin/administration/e-Assessment_openBadges.de.md) beschrieben.

[Zum Seitenanfang ^](#badges)


### Das Badge-Tool {: #badge_tool}

Badges werden im Badge-Tool erstellt. Ein Wizard führt durch die Erstellung.<br> Das Tool wird (mit kleinen Unterschieden) sowohl für die **Kurs-Badges** als auch für die **globalen Badges** verwendet.

[Zum Seitenanfang ^](#badges)


### Der Wizard

Sobald Sie sich zum Erstellen eines neuen Badges entschlossen haben (Klick auf den Button "Neuen Badge erstellen"), führt Sie ein Wizard in Schritten durch den Erstellungsprozess.

1. **Vorlage**: Der erste Schritt ist die Auswahl einer Vorlage oder das Hochladen eines eigenen Bildes. Derzeit wird SVG und PNG unterstützt.
![Wizard Schritt 1](assets/badges-wizard-1.de.jpg)

2. **Anpassung**: Wenn die Vorlage unter Berücksichtigung von Variablen erstellt wurde, können Sie Farben und Text in einer Vorlage ändern.
![Wizard Schritt 2](assets/badges-wizard-2.de.jpg)

3. **Details & Validierungszeitraum:** Obligatorische Details sind der Name, die Version und die Beschreibung des Badge sowie der Aussteller. Sie können zusätzlich eine URL und einen Kontakt zu den Ausstellereigenschaften hinzufügen. Die Gültigkeitsdauer kann auch so festgelegt werden, dass sie nie abläuft oder z.B. 12 Monate beträgt.
![Wizard Schritt 3](assets/badges-wizard-3.de.jpg)

4. **Kriterien**: Geben Sie die Kriterien und die Erklärung für die von Ihnen gewählten Regeln an.
![Wizard Schritt 4](assets/badges-wizard-4.de.jpg)

5. **Zusammenfassung**: Bildschirm mit einer Zusammenfassung aller Details.
![Wizard Schritt 5](assets/badges-wizard-5.de.jpg)

6. **Earners**: Zeigt die Earners in einer Tabelle an, um zu sehen, welcher Teilnehmer sich bereits für die von Ihnen gewählten Kriterien qualifiziert.

!!! note "Hinweis"

    Werden ganze Kurse kopiert, wird die Möglichkeit zum Erwerb von Badges auch in die Kopie übernommen.


[Zum Seitenanfang ^](#badges)


### Wo können Badges bearbeitet werden?

!!! note "Hinweis"

    Badges können nur bearbeitet werden, so lange noch niemand diesen Badge erworben hat.

**In der Kursadministration:**<br>
Administration > Badges > Klick auf die 3 Punkte am Ende einer Zeile > Option "Bearbeiten"

Wurde auch an Betreuer:innen das Recht zum manuellen Vergeben von Badges erteilt (Administration > Einstellungen > Tab Bewertung > Abschnitt Badges), dann ist auch für Betreuer:innen im Menü "Administration" eine Übersicht unter "Badges" abrufbar. Allerdings können Betreuer:innen keine Badges neu erstellen, sondern lediglich manuell vergeben.


**Im Kursmenü (als Kursbesitzer:in):**<br> 
Wählen Sie einen Kursbaustein, dem ein Badge hinzugefügt werden kann. [(Siehe Liste der Kursbausteine mit Badges)](#create_for_course_elements). Klicken Sie anschliessend auf den Tab "Badges". Wurde für diesen Kursbaustein eine Badge-Vergabe eingerichtet, können Sie auch hier auf die 3 Punkte am Ende einer Zeile klicken und Sie finden dort die Option "Bearbeiten".<br>


[Zum Seitenanfang ^](#badges)

---

## Ansicht vergebener Kurs-Badges {: #assigned_badges}

Die Vergabe von **Kurs-Badges** wird durch Kursbesitzer:innen in jedem Kurs unter<br>
**Einstellungen > Tab Bewertung > Abschnitt Badges** <br>
ermöglicht. Das Recht zur manuellen Vergabe kann hier auch Betreuer:innen gegeben werden.

Wurden Badges aktiviert, ist nach dem nächsten Login in der **Kursadministration** die Option **Badges** vorhanden. Hier können die Vergaberegeln der Badges für den Kurs eingerichtet werden.

Wurden durch Teilnehmer:innen Badges erworben, sind sie ersichtlich in der **Leistungsübersicht** des betreffenden Teilnehmers / der Teilnehmerin.



### Ansicht vergebener Badges in LinkedIn und anderen Websites {: #assigned_badges_LinkedIn}

Grundsätzlich kann die Anzeige von OpenOlat-Badges auf anderen Websites manuell durch Export und Import gemacht werden.

LinkedIn ermöglicht es Ihnen, Zertifikate in Ihrem persönlichen Profil anzuzeigen. Das Zertifikat oder Abzeichen wird mit einer hostbasierten Verifizierung überprüft.
Ein ähnliches Verfahren wird zur Überprüfung des Zertifikats oder Badges verwendet. 


[Zum Seitenanfang ^](#badges)

---

## Weiterführende Informationen  {: #further_information}

[Wie vergebe ich in meinem Kurs Badges? >](../../manual_how-to/badges/badges.de.md)<br>
[Globale Badges >](../../manual_admin/administration/e-Assessment_openBadges.de.md#global_badges)<br>
[OpenBadges Administration >](../../manual_admin/administration/e-Assessment_openBadges.de.md)<br>
[Der OpenBadges-Standard >](https://www.imsglobal.org/activity/openbadges)<br>
