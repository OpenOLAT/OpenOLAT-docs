# Kursbaustein "Mitteilungen" [:octicons-tag-16:{ title="ab Release 21.1 (OO-9761)" }](https://track.frentix.com/issue/OO-9761){:target="_blank"} {: #notification}


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

Mit dem Kursbaustein "Mitteilungen" informieren Sie die Mitglieder eines Kurses an einer festen Stelle im Kursmenü, etwa über eine Terminänderung oder neue Unterlagen. Die Mitteilungen erscheinen im Kurs und zusätzlich unter `Persönliche Werkzeuge > Abonnements` bei den Benachrichtigungen aller, die sie abonniert haben. Eine Mitteilung kann ein kurzer Text sein oder umfangreichere Informationen als Datei-Anhang mitbringen (standardmässig höchstens 5 MB).

Eine Mitteilung lässt sich sofort oder zu einem späteren Zeitpunkt veröffentlichen und zusätzlich per E-Mail versenden. Wie Sie die Empfänger:innen wählen, beschreibt der Abschnitt [Mitteilung verfassen und versenden](#create_notification).

## Konfiguration im Kurseditor Tab "Mitteilungs-Konfiguration" {: #configuration_notification}

Im Tab "Mitteilungs-Konfiguration" bestimmen Sie, wie lange und wie viele Mitteilungen der Kursbaustein zeigt, ob sie automatisch abonniert werden und wer sie verfasst.

**Anzeige:** Die maximale Anzahl Tage legt fest, wie lange eine Mitteilung im Kurs sichtbar bleibt. Die maximale Anzahl Mitteilungen legt fest, wie viele Mitteilungen der Kursbaustein gleichzeitig zeigt. Standardmässig sind es 90 Tage und 10 Mitteilungen.

**Automatisch abonnieren:** Ist "Diese Mitteilungen bei Ansicht automatisch abonnieren" eingeschaltet (Standard), abonnieren die Mitglieder des Kurses die Mitteilungen, sobald sie den Kursbaustein öffnen. Schalten Sie die Option aus, abonnieren Teilnehmende die Mitteilungen bei Bedarf selbst.

:octicons-device-camera-video-24: **Video-Einführung**: [Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

Im Bereich "Berechtigungen" legen Sie fest, welche Kursrollen Mitteilungen verfassen und verwalten dürfen. Standardmässig verfassen und verwalten Besitzende und Betreuende die Mitteilungen, Teilnehmende lesen sie. Besitzende behalten beide Rechte in jedem Fall.

Abonnierte Mitteilungen sehen die Mitglieder des Kurses auch im persönlichen Menü unter `Persönliche Werkzeuge > Abonnements`, mehr dazu auf der Seite [Abonnements](../personal_menu/Subscriptions.de.md).

!!! info "Wichtig"

    Eine Mitteilung ist auf 32.000 Zeichen begrenzt. Rechts unten im Textfeld der Mitteilung zeigt OpenOlat, wie viele Zeichen bereits verbraucht sind, und meldet beim Speichern, wenn die Grenze überschritten ist. Gezählt wird der HTML-Code der Mitteilung, deshalb liegt die Zahl über der Anzahl sichtbarer Zeichen.

!!! tip "Tipp"

    Für eine Ankündigung an den ganzen Kurs, die keinen Platz im Kursmenü braucht, eignet sich das gleichnamige Werkzeug "[Mitteilungen](../learningresources/Using_Additional_Course_Features.de.md)" in der Toolbar. Es lässt sich nicht konfigurieren: Besitzende und Betreuende verfassen dort Mitteilungen, Teilnehmende abonnieren sie bei Bedarf selbst. Den Kursbaustein nehmen Sie, wenn die Mitteilungen an einer bestimmten Stelle im Kursmenü stehen sollen oder wenn Sie Anzeige, Berechtigungen, automatisches Abonnieren und Zugang selbst festlegen wollen.

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
