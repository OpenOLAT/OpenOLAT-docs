# Kursbaustein "E-Mail“ {: #mail}


## Steckbrief

Name | E-Mail
---------|----------
Icon | ![E-Mail Icon](assets/contact.png){ class=size24  }
Verfügbar seit | Neuauflage mit Release 18.0
Funktionsgruppe | Verwaltung und Organisation
Verwendungszweck | Kontaktformular mit E-Mail-Versand
Bewertbar | nein
Spezialität / Hinweis |



Der Kursbaustein "E-Mail" dient als Kontaktformular und gibt Kursteilnehmenden die Möglichkeit, eine E-Mail an einen von Ihnen definierten Empfängerkreis zu senden.

Sie haben zwei Möglichkeiten, um Nachrichten zu versenden. Entweder geben Sie im Tab „**Empfänger**“ direkt die E-Mail-Adresse von bestimmten Personen ein, oder sie wählen die Personengruppen aus, an die eine Nachricht versendet werden soll. Sie können differenziert festlegen ob die Nachricht an Kursbesitzer, Betreuer und / oder Teilnehmer von Kurs und / oder Gruppen geschickt wird.

Um im Feld "E-Mailadressen" mehrere Empfängeradressen einzutragen, müssen Sie diese durch einen Zeilenumbruch trennen, d.h. jede E-Mailadresse muss auf einer eigenen Zeile stehen.

## Versand an Kursbesitzer/Betreuer/Teilnehmer

Markieren Sie die gewünschten Checkboxen, um die Mitgliedergruppen zu definieren, die Sie anschreiben möchten. Markieren Sie bei Betreuern und Teilnehmern in einem zweiten Schritt, ob Sie jeweils alle anschreiben möchten, oder nach Kurs und Gruppen unterscheiden. Klicken Sie keine Checkbox an, wird keine Mail verschickt.

In den Feldern „Betreff (Vorlage)“ und „Nachricht (Vorlage)“ können Sie optional Standardwerte vorgeben.

 * *Betreff*: Wird der Betreff vorgegeben so kann dieser von den Teilnehmenden nicht angepasst werden. Wird der Betreff in der Vorlage leer gelassen, so müssen die Teilnehmenden einen eigenen Betreff festlegen (Pflichtfeld)
 * *Nachricht*: Die vordefinierte Nachricht kann beim Versand einer E-Mail durch die Teilnehmenden beliebig editiert werden.

Zudem kann die Nachricht / der Betreff mit dem Einsatz von Variablen
persönlicher und kursbezogen gestaltet werden.

## Einsatz von Variablen

Folgende Variablen können im Betreff und im Text der E-Mail verwendet werden:

| Variable | Beschreibung |
| -----|----|
|    `$firstname` | Der Vorname des Benutzers  |
| `$lastname` | Der Nachname des Benutzers  |
| `$fullName` | Der volle Name des Benutzers  |
| `$username` | Der Benutzername  |
| `$email` | Die E-Mailadresse des Benutzers  |
| `$courseurl` | Die Internetadresse des Kurses  |
| `$coursename` | Der Name des Kurses wie auf der Infoseite  |
| `$coursedescription` | Die Beschreibung des Kurses wie auf der Infoseite  |
  
!!! info ""

    Die Benutzervariablen beziehen sich auf denjenigen, der die E-Mail über den **"Senden"-Button** auslöst und verschickt.

Geben Sie durch einen geeigneten Kurztitel des Kursbausteins „E-Mail“ Ihren Kursteilnehmern einen Hinweis darauf, an welchen Empfängerkreis diese Nachricht versendet wird. Im E-Mailformular selbst werden die Empfängeradressen aus Gründen des Datenschutzes nicht angezeigt.

!!! tip "Tipp"

    Ein Element "E-Mail" mit ähnlichen Funktionen, jedoch ohne spezifische Konfiguration, findet man auch in der [Toolbar](../learningresources/Using_Additional_Course_Features.de.md).
