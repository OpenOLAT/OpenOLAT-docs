# Kursbaustein "Mitteilungen" {: #notification}


## Steckbrief

Name | Mitteilungen
---------|----------
Icon | :o_icon_o_infomsg_icon:
Verfügbar seit | Neuauflage mit Release 18
Funktionsgruppe | Verwaltung und Organisation
Verwendungszweck | Mitteilungen innerhalb der Kursstruktur (Kursmenü)
Bewertbar | nein
Spezialität / Hinweis |



:octicons-device-camera-video-24: **Video-Einführung**: [Mitteilungen](<https://www.youtube.com/embed/3tAj19Avfkk>){:target="_blank"}

Der Kursbaustein bietet die Möglichkeit, Mitteilungen in der Kursstruktur einzubetten. Diese Mitteilungen sind sowohl im Kurs als auch unter `Persönliche Werkzeuge > Abonnements` bei den Benachrichtigungen der einzelnen Teilnehmenden sichtbar. Bei der Mitteilung kann es sich sowohl um einen kurzen Infotext handeln, als auch um umfangreiche Infos, die per Datei-Anhang (standardmässig höchstens 5 MB) beigefügt werden.

Eine Mitteilung lässt sich sofort oder zu einem späteren Zeitpunkt veröffentlichen und zusätzlich per E-Mail versenden. Wie Sie die Empfänger:innen wählen, beschreibt der Abschnitt [Mitteilung verfassen und versenden](#create_notification).

## Konfiguration im Kurseditor Tab "Mitteilungs-Konfiguration" {: #configuration_notification}

 **Anzeige:** Die maximale Anzahl Tage legt fest, wie lange (in Tagen) die
Mitteilungen im Kurs angezeigt werden. Die maximale Anzahl Mitteilungen legt
fest, wie viele Mitteilungen gleichzeitig im Kurs angezeigt werden.

 **Automatisch abonnieren:** Standardmässig wird der Kursbaustein automatisch
von Teilnehmenden abonniert. Diese Option können Sie hier ausschalten, so dass
Teilnehmende Mitteilungen manuell abonnieren können.

:octicons-device-camera-video-24: **Video-Einführung**: [Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

Im Bereich "Berechtigungen" kann definiert werden welche Kursrollen Mitteilungen verfassen und verwalten dürfen. Besitzende können grundsätzlich Mitteilungen verfassen und verwalten.

Mitteilungen können im persönlichen Menü unter `Persönliche Werkzeuge > Abonnements` eingesehen werden, mehr dazu auf der Seite [Abonnements](../personal_menu/Subscriptions.de.md). Die Anzahl angezeigter Mitteilungen kann im Kurseditor eingestellt werden.

Standardmässig dürfen nur Betreuende und Besitzende Mitteilungen erstellen. Alle Teilnehmenden dürfen jedoch Mitteilungen lesen. Im Tab "Mitteilungs-Konfiguration" können Sie diese Einstellung Ihren Wünschen entsprechend anpassen.

!!! info "Wichtig"

    Die Anzahl der Zeichen für die Mitteilung ist auf 32.000 Zeichen begrenzt. Sie
    erhalten eine entsprechende Information über die bereits verbrauchte
    Zeichenzahl rechts unten im Mitteilungseditor. Wird die erlaubte Zeichenzahl überschritten, erfolgt ein entsprechender Hinweis. Achtung: Die Anzahl der angegebenen tatsächlichen Zeichen weicht von der Anzahl der sichtbaren Zeichen
    ab, da für die tatsächliche Anzahl der HTML-Code verwendet wird.

!!! tip "Tipp"

    Ein Element mit ähnlichen Funktionen, jedoch ohne spezifische Konfiguration, findet man auch in der Toolbar. Es handelt sich um die "[Mitteilungen](../learningresources/Using_Additional_Course_Features.de.md)".

## Mitteilung verfassen und versenden [:octicons-tag-16:{ title="ab Release 21.1.0 (OO-9594)" }](https://track.frentix.com/issue/OO-9594) {: #create_notification}

Wer eine Mitteilung verfasst, bestimmt im selben Ablauf, wer davon erfährt: nur die Abonnent:innen oder zusätzlich ausgewählte Mitglieder per E-Mail, bis hinunter auf eine einzelne Gruppe.

Die Schaltfläche "Mitteilung erstellen" öffnet einen Assistenten mit zwei Schritten. Im ersten Schritt schreiben Sie die Mitteilung und legen unter "Veröffentlichung" fest, ob sie sofort erscheint ("Sofort") oder erst zu einem gewählten Zeitpunkt ("Individuelles Datum").

Im zweiten und letzten Schritt wählen Sie unter "Benachrichtigung" zwischen zwei Möglichkeiten:

- **Abonnement**: OpenOlat benachrichtigt nur die Abonnent:innen der Mitteilungen.
- **Abonnement & E-Mail**: OpenOlat benachrichtigt ebenfalls die Abonnent:innen und versendet mit der Veröffentlichung zusätzlich eine E-Mail.

Nur bei "Abonnement & E-Mail" erscheint die Auswahl "E-Mail Empfänger:innen":

- **Alle Mitglieder**: Die E-Mail geht an alle Besitzenden, Betreuenden und Teilnehmenden des Kurses, einschliesslich der Mitglieder zugeordneter Gruppen und Elemente des Course Planner (CPL). Die Zahl in Klammern nennt, wie viele Personen das sind.
- **Individuelle Mitglieder**: Sie wählen die Empfänger:innen selbst aus. Die Auswahl "Abonnent:innen" steht dabei für sich: Mit "Alle Abonnent:innen" erhalten alle, die die Mitteilungen abonniert haben, die E-Mail, unabhängig von ihrer Rolle im Kurs.

Welche Auswahl unter "Individuelle Mitglieder" erscheint, hängt davon ab, ob dem Kurs Gruppen oder Elemente des Course Planner zugeordnet sind. Hat der Kurs weder eine aktive Gruppe noch ein Element des Course Planner, erscheint eine einzige Auswahl "Mitglieder" mit den Optionen "Alle Besitzer:innen", "Alle Betreuer:innen" und "Alle Teilnehmer:innen".

Ist dem Kurs mindestens eine aktive Gruppe oder ein Element des Course Planner zugeordnet, gliedert sich die Auswahl nach Rollen:

- **Besitzer:innen**: "Alle Besitzer:innen".
- **Betreuer:innen**: "Alle Betreuer:innen" erreicht die Betreuenden des Kurses und aller zugeordneten Gruppen und Elemente. "Alle Kursbetreuer:innen" erreicht nur die Betreuenden, die direkt im Kurs eingetragen sind. Dazu kommt je Gruppe eine Option "Alle Gruppenbetreuer:innen" und je Element eine Option "Alle CPL Betreuer:innen", jeweils mit dem Namen der Gruppe oder des Elements.
- **Teilnehmer:innen**: dieselbe Gliederung mit "Alle Teilnehmer:innen", "Alle Kursteilnehmer:innen", "Alle Gruppenteilnehmer:innen" und "Alle CPL Teilnehmer:innen".

So geht eine Ankündigung, die nur den Kurs betrifft, mit "Alle Kursteilnehmer:innen" an die direkt im Kurs eingetragenen Teilnehmenden, ohne die E-Mail auch an die Teilnehmenden der zugeordneten Gruppen zu schicken. Dieselbe Auswahl steht beim Werkzeug "Mitteilungen" in der Toolbar zur Verfügung.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Abonnements >](../personal_menu/Subscriptions.de.md)<br>
[Einsatz weiterer Kursfunktionen der Toolbar >](../learningresources/Using_Additional_Course_Features.de.md)

**Weiterführend**<br>
[Mitgliederverwaltung >](../learningresources/Members_management.de.md)<br>
[Gruppenwerkzeuge nutzen >](../groups/Using_Group_Tools.de.md)<br>
[Course Planner: Übersicht >](../area_modules/Course_Planner.de.md)

**youtube**<br>
[Mitteilungen](<https://www.youtube.com/embed/3tAj19Avfkk>)<br>
[Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>)

[Zum Seitenanfang ^](#notification)
