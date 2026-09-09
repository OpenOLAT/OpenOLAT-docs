# Verwaltung und Organisation


## Kursbaustein "Einschreibung" {: #enrolment}

:fontawesome-solid-right-to-bracket:

Der Kursbaustein "Einschreibung" wird verwendet, damit sich Teilnehmende in
eine oder mehrere OpenOlat-Gruppen eintragen können. Definieren Sie dazu im
Tab "Konfiguration", in welche und wie viele **Gruppen** sich Teilnehmende
einschreiben können. Sie können auch die Reihenfolge der Gruppen in der
Auswahlliste definieren. Sollten Sie noch keine Gruppen erstellt haben oder
weitere benötigen, so können Sie dies mit einem Klick auf „Auswählen“ und
„Erstellen“ direkt im Tab „Konfiguration“ tun. Bestehende und neu erstellte
Gruppen können in der [Mitgliederverwaltung](../learningresources/Members_management.de.md) bearbeitet werden.

Mittels "**Mehrere Eintragungen erlauben**" legen Sie optional fest, ob
Teilnehmende sich in mehrere Gruppen eintragen dürfen, und falls ja, in wie
viele.

Im Feld "**Austragen erlaubt**" bestimmen Sie optional, ob eine einmal
eingeschriebene Person die Möglichkeit hat, sich wieder aus einer
Gruppe auszutragen. In der Gruppenverwaltung können Sie beim Editieren der
Gruppe festlegen, ob es eine Warteliste und ob es ein automatisches Nachrücken
geben soll.

!!! info "Zugriff über Lernbereiche"

    Sofern Sie zuvor einen oder mehrere Lernbereiche in der Administration angelegt und hier Gruppen zugeordnet haben, können Sie auf diese Lernbereiche auch im Tab "Konfiguration" des Einschreibebausteins zugreifen.

## Kursbaustein "Mitteilungen" {: #notification}

:fontawesome-solid-circle-info:

:octicons-device-camera-video-24: **Video-Einführung**: [Mitteilungen](<https://www.youtube.com/embed/3tAj19Avfkk>){:target="_blank"}

Der Kursbaustein bietet die Möglichkeit, Mitteilungen in der Kursstruktur
einzubetten. Diese Mitteilungen sind sowohl im Kurs als auch bei den
Benachrichtigungen der einzelnen Benutzer:innen sichtbar. Bei der Mitteilung kann es
sich sowohl um einen kurzen Infotext handeln, als auch um umfangreiche Infos,
die per Datei-Anhang (max. 5 MB) beigefügt werden. Während der Erstellung
einer Mitteilung kann definiert werden, ob die Mitteilung zusätzlich per Mail
an bestimmte Nutzergruppen des Kurses (Abonnierte, Kursbesitzer:innen, Betreuer:innen,
Mitglieder oder Gruppen) erfolgen soll.

 **Anzeige:** Die maximale Anzahl Tage legt fest, wie lange (in Tagen) die
Mitteilungen im Kurs angezeigt werden. Die maximale Anzahl Mitteilungen legt
fest, wie viele Mitteilungen gleichzeitig im Kurs angezeigt werden.

 **Automatisch abonnieren:** Standardmässig wird der Kursbaustein automatisch
von Kursbesuchern abonniert. Diese Option können Sie hier ausschalten, so dass
Kursbesucher Mitteilungen manuell abonnieren können.

:octicons-device-camera-video-24: **Video-Einführung**: [Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

Mitteilungen können im persönlichen Menü unter "Abonnements" eingesehen
werden. Die Anzahl angezeigter Mitteilungen kann im Kurseditor eingestellt
werden.

Standardmässig dürfen nur Betreuer:innen und Besitzer:innen Mitteilungen erstellen. Alle
Teilnehmenden dürfen jedoch Mitteilungen lesen. Im Tab „Mitteilungs-
Konfiguration“ können Sie diese Einstellung Ihren Wünschen entsprechend
anpassen.

Die Anzahl der Zeichen für die Mitteilung ist auf 32.000 Zeichen begrenzt. Sie
erhalten eine entsprechende Information über die bereits verbrauchte
Zeichenzahl rechts unten im Mitteilungseditor. Wird die erlaubte Zeichenzahl
überschritten, erfolgt ein entsprechender Hinweis. Achtung: Die Anzahl der
angegebenen tatsächlichen Zeichen weicht von der Anzahl der sichtbaren Zeichen
ab, da für die tatsächliche Anzahl der HTML Code verwendet wird.

!!! tip "Tipp"

    Ein Element mit ähnlichen Funktionen, jedoch ohne spezifische Konfiguration, findet man auch in der Toolbar. Es handelt sich um die "[Teilnehmer Infos](../learningresources/Using_Additional_Course_Features.de.md)".



## Kursbaustein "E-Mail" {: #mail}
:fontawesome-regular-envelope:



Über den Kursbaustein "E-Mail" geben Sie Ihren Teilnehmenden die
Möglichkeit, eine E-Mail an einen von Ihnen definierten Empfängerkreis zu
senden.

Sie haben zwei Möglichkeiten, um Nachrichten zu versenden. Entweder geben Sie
im Tab "**Empfänger**" direkt die E-Mail-Adresse von bestimmten Personen ein, oder
sie wählen die Personengruppen aus, an die eine Nachricht versendet werden
soll. Sie können differenziert festlegen ob die Nachricht an Kursbesitzer:innen,
Betreuer:innen und/oder Teilnehmende von Kurs und/oder Gruppen geschickt wird.

Um im Feld "E-Mail-Adressen" mehrere Empfängeradressen einzutragen, müssen Sie
diese durch einen Zeilenumbruch trennen, d.h. jede E-Mail-Adresse muss auf
einer eigenen Zeile stehen.

### Versand an Kursbesitzer:innen/Betreuer:innen/Teilnehmende
Markieren Sie die
gewünschten Checkboxen, um die Mitgliedergruppen zu definieren, die Sie
anschreiben möchten. Markieren Sie bei Betreuer:innen und Teilnehmenden in einem
zweiten Schritt, ob Sie jeweils alle anschreiben möchten, oder nach Kurs und
Gruppen unterscheiden. Klicken Sie keine Checkbox an, wird keine Mail
verschickt.

In den Feldern „Betreff (Vorlage)“ und „Nachricht (Vorlage)“ können Sie
optional Standardwerte vorgeben.

 * *Betreff*: Wird der Betreff vorgegeben so kann dieser von den Teilnehmenden
nicht angepasst werden. Wird der Betreff in der Vorlage leer gelassen, so müssen
die Teilnehmenden einen eigenen Betreff festlegen (Pflichtfeld)
 * *Nachricht*: Die vordefinierte Nachricht kann beim Versand einer E-Mail durch
die Teilnehmenden beliebig editiert werden.

Zudem kann die Nachricht / der Betreff mit dem Einsatz von Variablen
persönlicher und kursbezogen gestaltet werden.

### Einsatz von Variablen

Folgende Variablen können im Betreff und im Text der E-Mail verwendet werden:


| Variable | Beschreibung |
| -----|----|
|    `$firstname` | Der Vorname der Person  |
| `$lastname` | Der Nachname der Person  |
| `$fullName` | Der volle Name der Person  |
| `$username` | Der Benutzername  |
| `$email` | Die E-Mail-Adresse der Person  |
| `$courseurl` | Die Internetadresse des Kurses  |
| `$coursename` | Der Name des Kurses wie auf der Infoseite  |
| `$coursedescription` | Die Beschreibung des Kurses wie auf der Infoseite  |

!!! info ""

    Die Variablen beziehen sich auf die Person, die die E-Mail über den **"Senden"-Button** auslöst und verschickt.





Geben Sie durch einen geeigneten Kurztitel des Kursbausteins "E-Mail" Ihren
Teilnehmenden einen Hinweis darauf, an welchen Empfängerkreis diese
Nachricht versendet wird. Im E-Mail-Formular selbst werden die
Empfängeradressen aus Gründen des Datenschutzes nicht angezeigt.

!!! tip "Tipp"

    Ein Element "E-Mail" mit ähnlichen Funktionen, jedoch ohne spezifische Konfiguration, findet man auch in der [Toolbar](../learningresources/Using_Additional_Course_Features.de.md#e-mail).

## Kursbaustein "Kalender" {: #cal}

:fontawesome-regular-calendar-days:

Mit dem Kursbaustein "Kalender" können Sie den Kurskalender in die
Kursstruktur einbetten. Es ist auch möglich mehrere Instanzen desselben
Kalenders dem Kurs hinzuzufügen.

Diese Einbindung ist eine Alternative gegenüber der Einbindung des Kalenders
in der Kurstoolbar (vgl. "[Einsatz weiterer Kursfunktionen der
Toolbar](../learningresources/Using_Additional_Course_Features.de.md#kurskalender)").

Standardmässig dürfen nur Besitzer:innen und Betreuer:innen Termine erstellen. Alle
Teilnehmenden dürfen jedoch Kalendereinträge lesen. Im Tab "Kalender-
Konfiguration" können Sie definieren, ob neben den Kursbesitzer:innen auch
Teilnehmende und Betreuer:innen des Kurses Kalendereinträge einstellen und bearbeiten
dürfen. Ferner können Sie hier konfigurieren, welches Datum angezeigt wird,
wenn der Kurskalender aus der Kursstruktur aufgerufen wird. Kurskalender
werden automatisch den [persönlichen Kalendern](../personal_menu/Calendar.de.md) der
Teilnehmenden hinzugefügt.



Wenn Sie im Kalender jeweils eine Semesterwoche anzeigen und Links auf
Kursbausteine einfügen, dient der Kalender als Übersichtsseite auf die Termine
und Aufgaben der Woche.



Prüfen Sie, ob der _Kursbaustein_ "Kalender" wirklich für Sie die optimale
Wahl darstellt. In vielen Fällen, insbesondere bei [Lernpfadkursen](../learningresources/Learning_path_course.de.md), ist es
sinnvoller in den Einstellungen den Kalender in der [Toolbar](../learningresources/Using_Additional_Course_Features.de.md#kurskalender) zu aktivieren.

!!! tip "Tipp"

    Wenn Sie in Ihrer OpenOlat Instanz keinen Kursbaustein "Kalender" finden können, so wurde dies systemweit von einem Administrator ausgeschaltet.

## Kursbaustein "Terminplanung" {: #appointment_scheduling}

:fontawesome-regular-calendar-check:

Mit dem Kursbaustein Terminplanung können sowohl Einschreibungen für bestimmte
Termine als auch Terminfindungen organisiert werden. Generell kann
konfiguriert werden, ob mehrere Termine ausgewählt werden können, ob es eine
Begrenzung der Teilnehmerzahl gibt, ob die Teilnehmenden sehen wer sich
eingetragen hat und ob ein BigBlueButton Raum zugeordnet werden soll.

Im Kurseditor wird der Kursbaustein hinzugefügt und es kann festgelegt werden,
ob Betreuer:innen Themen und Termine ebenfalls bearbeiten dürfen oder ob dies nur
durch die Kursbesitzer:innen möglich ist. Soll die Terminwahl nur innerhalb eines
bestimmten Zeitfensters möglich sein, müssen die Zeitangaben im Kurseditor im
Tab "Lernpfad" entsprechend angegeben werden bzw. bei herkömmlichen Kursen die
Sichtbarkeit oder der Zugang passend konfiguriert werden.

Die eigentliche Konfiguration und Einrichtung der Termine erfolgt jedoch im
Kursrun bei geschlossenem Editor. Dafür werden zunächst über den Button
"Anlass erstellen" eine neue Einschreibung oder Terminfindung angelegt und die
Basiskonfiguration vorgenommen sowie Termine eingetragen.

![Dialog Anlass erstellen mit Titel, Beschreibung, Typ Einschreibung, Konfigurationsoptionen, Organisator, Terminart Dauer und einem eingetragenen Termin](assets/Anlass_erstellen.png){ class="shadow lightbox" }

Über den Button "**Termin hinzufügen**" können Sie auch später noch weitere
Termine dieser Abstimmung hinzufügen.  Auch können bereits angelegte Termine
über den Drei-Punkte-Link wieder überarbeitet werden.

![Geöffnetes Dropdown-Menü Termin hinzufügen mit den Optionen Start/Ende, Start/Dauer und Wiederkehrende Termine, darunter ein bereits eingetragener Online-Termin](assets/Termin_hinzufuegen.jpg){ class="shadow lightbox" }

### Termine: erstellen & bearbeiten

!!! info "Menü Anlass erstellen"

    So konfigurieren Sie eine Einschreibung oder Terminfindung

**Titel:** Geben Sie hier die Bezeichnung des Termins an, z.B. "Abstimmung
Abschlussmeeting", "Kick-Off-Meeting" usw.. Die Eingabe ist notwendig
(Pflichtfeld).

 **Beschreibung:** Erläutern Sie die Terminwahl näher.

 **Typ:** Entscheiden Sie ob es sich um eine Terminfindung für einen
gemeinsamen Termin oder um die Einschreibung für einen oder mehrere Termine
aus einer Auswahl, z.B. Labortermine handelt.

 **Konfiguration:** Entscheiden sie ob die Teilnehmenden nur einen oder
mehrere Termine auswählen dürfen und ob die Namen der Teilnehmenden für andere
Teilnehmende sichtbar sein sollen. Bei der "Einschreibung" kann ergänzend noch
definiert werden ob der Coach (Betreuer:in) den Termin noch bestätigen muss.

 **Organisator:innen:** Definieren Sie hier, wer als Organisator:in der Terminplanung
angezeigt wird.

 **Ort:** Geben Sie hier den Veranstaltungsort ein.

 **Max. Teilnehmer:** Sie können die Mitgliederzahl für einen Termin begrenzen
(nur bei "Einschreibung")

 **Terminart:** Sie können Termine basierend auf der Dauer, basierend auf
einem Start- und Enddatum oder wiederkehrend nach bestimmten Wochentagen
anlegen. Die Auswahl erleichtert Ihnen die Erstellung von weiteren Terminen.

!!! info ""

    Wird "Dauer" gewählt, werden beim Hinzufügen von weiteren Terminen die Termine am gleichen Tag vorkonfiguriert und die Uhrzeiten entsprechend der Dauer angepasst.

    Wird Start/Ende gewählt bleiben die gewählten Uhrzeiten erhalten und man braucht bei neuen Einträgen nur das Datum anzupassen.

 **Termine:** Hier werden die konkreten Wahltermine eingetragen. Durch Klick
auf das "+ Zeichen" werden neue Termine hinzugefügt. Durch Klick auf das "-
Zeichen" werden Termine wieder gelöscht.

 **Online Termin:** Die Optionen sind: Nein, kein Online-Termin oder man wählt
direkt das gewünschte Tool BigBlueButton oder Teams aus, sofern von der
System-Administration die virtuellen Klassenzimmer aktiviert wurden.

!!! tip "Tipp"

    Wird BigBlueButton oder Teams aktiviert, kann für die gewählten Termine jeweils ein BigBlueButton bzw. Teams Raum hinzugefügt und weiter konfiguriert werden. Beim Ort wird in diesem Fall automatisch "online" angezeigt.



Ein erstellter "Anlass" kann später mit Klick auf das Zahnrad **bearbeitet,
dupliziert oder gelöscht** werden. Auch kann der Teilnehmerkreis für den Anlass
auf bestimmte Gruppen eingeschränkt werden. Ein Export der Teilnehmenden für
einen Anlass ist ebenfalls möglich.

![Liste der Anlässe Diskussionsrunde und Besprechung, beim ersten Anlass geöffnetes Zahnrad-Menü mit Anlass bearbeiten, Teilnehmerkreis, Teilnehmer exportieren, Anlass duplizieren und Löschen](assets/Terminplanung_anlass.jpg){ class="shadow lightbox" }

Die konkreten Termine von bereits angelegten Terminplanungen können über den
Link "Termine anzeigen" näher betrachtet und von den Kursbesitzer:innen bzw. Betreuer:innen
editiert werden. Sie können hier Teilnehmende hinzufügen, löschen, umbuchen,
die Beschreibung anpassen, Termine ändern oder Termine bestätigen.

![Liste zweier Online-Termine mit je 10 freien Plätzen, beim ersten Termin geöffnetes Drei-Punkte-Menü mit den Einträgen "Termin bearbeiten", "Benutzer hinzufügen" und "Löschen"](assets/Terminfindung_punkte.jpg){ class="shadow lightbox" }

Teilnehmende können über den Link "**Termine auswählen**" bzw. "**Eintragen**" die
gewünschten Termine sehen und auswählen. Wurde ein Termin bestätigt, ist das
ebenfalls sichtbar.

![Einschreibungsseite mit drei Terminen, dem bereits gebuchten und markierten Termin mit Status Geplant und Button Austragen, den übrigen mit Button Eintragen](assets/Einschreibung.png){ class="shadow lightbox" }

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Mitgliederverwaltung >](../learningresources/Members_management.de.md)<br>
[Einsatz weiterer Kursfunktionen der Toolbar >](../learningresources/Using_Additional_Course_Features.de.md)<br>
[Persönliche Werkzeuge: Kalender >](../personal_menu/Calendar.de.md)<br>
[Lernpfadkurs - Überblick >](../learningresources/Learning_path_course.de.md)

**Weiterführend**<br>
[Kursbaustein "Einschreibung" >](../learningresources/Course_Element_Enrolment.de.md)<br>
[Kursbaustein "Mitteilungen" >](../learningresources/Course_Element_Notifications.de.md)<br>
[Kursbaustein "E-Mail" >](../learningresources/Course_Element_EMail.de.md)<br>
[Kursbaustein "Kalender" >](../learningresources/Course_Element_Calendar.de.md)

[Zum Seitenanfang ^](#verwaltung-und-organisation)







