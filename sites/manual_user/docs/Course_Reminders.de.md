#  [Erinnerung](Erinnerung.html)

Mit der Erinnerungsfunktion erstellen Sie Regellisten, bei deren Erfüllung
eine zuvor definierte Mail automatisch an eine in den Regeln festgelegte
Benutzergruppe des Kurses versandt wird. Häufigkeit und Sendezeit wird von
Ihrem Systemadministrator systemweit festgelegt. Erinnerungen können auch
gezielt ausgelöst werden - dabei werden Erinnerungen aber dennoch nur an jene
Benutzer geschickt, für die alle Bedingungen als erfüllt
gelten.![](../../download/attachments/590041/Erinnerungen_16.png)

  

Auf der Übersichtsseite sehen Sie alle für einen Kurs bereits erstellten
Erinnerungen und können sich auch bereits versendete Erinnerungen anzeigen
lassen.  Die Liste der bereits versendeten Erinnerungen enthält Informationen
zum Empfänger sowie die Sendezeit. Einzelne Erinnerungen aus dieser Liste
können über den Link „Wieder schicken“ einfach verschickt werden.

## Erinnerung erstellen

Erinnerungen können jederzeit erstellt werden. Klicken Sie dazu auf die
Schaltfläche "Erinnerung erstellen". Es erscheint ein Wizard der Sie Schritt
für Schritt durch den Erstellungsprozess führt.

![](../../download/attachments/590041/Erinnerung_neu.png)

Geben Sie als erstes die Beschreibung für die Erinnerung ein. Diese
Beschreibung ist nur für die Autoren sichtbar und dient der übersichtlichen
und informativen Darstellung aller Erinnerungen eines Kurses. Wählen Sie dann
die Bedingungen für den Versand aus. Im nächsten Schritt werden die
Bedingungen überprüft und noch einmal angezeigt. Im letzten Schritt geben Sie
dann den konkreten E-Mail Text ein und können auch noch auswählen ob auch
Betreuer oder Besitzer eine Kopie erhalten sollen oder eine Kopie an eine
externe Adresse verschickt werden soll.

Neben der Konfiguration in der Kursadministration können für bestimmte
Assessment Kursbausteine Erinnerungen auch direkt bei dem jeweiligen
Kursbaustein eingerichtet werden. In diesem Fall ist der entsprechenden
Kursbaustein bereits vorausgewählt. So kann beispielweise rasch eine
Erinnerung für Lernende erstellt werden, die einen bestimmten Test noch gar
nicht durchgeführt haben (Versuche  = 0) oder eine E-Mail verschickt werden an
alle Personen die eine Aufgabe bestanden haben.

### Bedingungen für den Versand von Erinnerungen

Zur Konfiguration von Erinnerungen stehen verschiedene Bedingungen zur
Verfügung, die nach Wunsch kombiniert werden können. Dadurch können diverse
auf den individuellen Bedarf zugeschnittene Erinnerungen per Mail ausgelöst
werden.

Bei der Verknüpfung handelt es sich um eine "und" Verknüpfung. Das heißt, nur
wenn alle Bedingungen erfüllt sind wird die Erinnerungsmail ausgelöst.

Legen Sie fest unter welchen Bedingungen eine Erinnerung versandt werden soll.
Im Dropdown-Menü legen Sie den Typ der Bedingung fest, während Sie in den
nachfolgenden Feldern die Bedingung anhand von z.B. einem Datum oder einer
Punktezahl spezifizieren. Über die Schaltflächen rechts von der Bedingung
entfernen Sie diese oder fügen eine weitere Bedingung hinzu. Es muss
mindestens ein Kriterium gewählt werden, damit ein Versand ausgelöst werden
kann.

Es gibt verschiedene Arten von Bedingungen: Im Folgenden finden Sie eine kurze
Erklärung zu den Arten ein und wie sie generell angewandt werden.

a) Zeitspanne  
---  
Diese Bedingungen bauen darauf auf, wie lange etwas schon her ist, oder wie
lange ein bestimmter Zeitpunkt noch entfernt ist.|

 **Beispiel** : 5 Wochen bevor die Zuweisung für die Gruppenaufgabe schliesst.

 **Beispiel** : 5 Tage nachdem der User den Kurs zum ersten Mal aufgerufen
hat.  
  
  * Einschreibedatum
  * Beginn Datum von Kurs-Durchführungszeitraum
  * Enddatum von Kurs-Durchführungszeitraum
  * Erster Kursbesuch
  * Letzter Kursbesuch
  * Termin: Aufgabe Zuweisung
  * Termin: Aufgabe Dokumente abgeben
  * Termin Formular ausfüllen
  * Datum des ersten Versuchs

  
  
b) Anzahl Versuche  
---  
Hier wird die Anzahl der Versuche von bewertbaren Kurselementen für den
Versand als Bedingung berücksichtigt.|  **Beispiel** : Ein Test wurde noch
kein Mal (0) durchgeführt.  
Versuche  
  
c) Bewertung  
---  
Bewertbare Kurselemente, für die eine Punktezahl oder ein Bestanden-Status im
Editor konfiguriert wurde, können hier als Bedingung eingebunden werden.|
**Beispiel** : In einer Checkliste wurden weniger als 3 Punkte erreicht.  
  
  * Bestanden
  * Punkte

  
  
Operatoren

 Klicken Sie hier, um zu erweitern...

Für die zwei Bedingungen "Versuche" und "Punkte" werden Operatoren benötigt um
die verschiedenen Zustände "mehr als, weniger als, weniger oder gleich, mehr
oder gleich, gleich" und "ungleich" korrekt darzustellen. Sie dienen dazu
Ausdrücke miteinander zu vergleichen, und in Abhängigkeit davon einen
logischen Rückgabewert zu erzeugen.

<|

kleiner

| korrekt wenn a kleiner b ist|

In unseren Bedingungen wird in diesem Fall z.B. das Ergebnis eines Testes (a)  
mit dem eingegebenen Wert in der Bedingungsregel (b) verglichen. Ist der
logische  
Rückgabewert "True", also trifft die Bedingung zu, dann wird die Erinnerung
ausgelöst.  
  
---|---|---|---  
<=| kleiner gleich| korrekt, wenn a kleiner oder gleich b ist  
=| gleich| korrekt, wenn a gleich b ist  
=>| grösser gleich| korrekt, wenn a grösser oder gleich b ist  
>| grösser| korrekt, wenn a grösser b ist  
!=| ungleich| korrekt, wenn a ungleich b ist  
  
Ein Beispiel: Eine Erinnerung soll verschickt werden, wenn ein Teilnehmer in
einem Test maximal 5 Punkte erreicht hat. In OpenOlat sieht die Bedingung dann
folgendermassen aus:

![](../../download/attachments/590041/reminder_operator_DE.png)

d) Datum  
---  
Zum eingetragenen Datum (inkl. Uhrzeit) wird die Erinnerung zur nächst
möglichen Sendezeit verschickt.|  **Beispiel** : 24.06.2021 16:30  
  
  * Bis Datum
  * Nach Datum

|  
  
  
e) Zugehörigkeit  
---  
Hier basierend auf der OLAT Rolle wird festgelegt an welche Kurs-Teilnehmer
die Erinnerung geschickt wird.|  **Beispiel** : An alle Besitzer und Betreuer
schicken.  
  
  * Kursrolle
  * Gruppenmitglieder

  
  
f) Benutzereigenschaft|  
  
---|---  
Hier erfolgt der Versand basierend auf bestimmten benutzerspezifischen
Eigenschaften. Erinnerungen werden an jene Kursteilnehmer verschickt, die das
ausgewählte Profilattribut besitzen.|  **Beispiel** : Benutzer aus der Stadt
Zürich.  
  
g) Fortschritt (nur bei [Lernpfad
Kursen](../../pages/viewpage.action%EF%B9%96pageId=108593191.html))|  
  
---|---  
  
Hier erfolgt der Versand basierend auf dem prozentualen Kursfortschritt der
Teilnehmenden, wie er in den Einstellungen der Administration konfiguriert
wurde.

  

|  **Beispiel** : Benutzer die mindestens 80% eines Kurses erfolgreich
abgeschlossen haben.  
  
Sie können so viele Bedingungen kombinieren wie gewünscht. Es ist sicher
sinnvoll sich zuvor Gedanken darüber zu machen wer unter welcher Bedingung zu
welchem Zeitpunkt eine Erinnerung erhalten soll.

 **E-Mail Text**

Mit Hilfe des E-Mail-Textes, der nach Bedarf angepasst werden kann, erstellen
Sie ganz spezifische, auf die Situation angepasste E-Mail-Erinnerungen.

  

Am besten verwenden Sie die bereits eingetragenen Variablen um die Erinnerung
so persönlich und hilfreich wie möglich zu gestalten.

    
    
    $firstName

| Der Vorname des Benutzers  
---|---  
      
    
    $lastName

| Der Nachname des Benutzers  
      
    
    $fullName

| Der vollständige Name je nach Systemkonfiguration. Der Standardwert ist
"Nachname, Vorname"  
      
    
    $email

| Die Emailadresse des Benutzers  
      
    
    $userName

| Der Benutzername  
      
    
    $courseUrl

| Die Internetadresse des Kurses  
      
    
    $courseName

| Der Name des Kurses wie auf der Infoseite  
      
    
    $courseDescription

| Die Beschreibung des Kurses wie auf der Infoseite  
  
Hier ein Beispiel:

![](../../download/attachments/590041/Erinnerung_Mail-Text.png)

  

Am obersten Kursknoten werden zusätzlich alle Erinnerungen aufgelistet, die an
keinen bestimmten Kursbaustein gebunden sind. Auch können sowohl hier als auch
bei anderen Assessment Bausteinen mit dem Tab "Erinnerungen" weitere
Konfigurationen vorgenommen werden, z.B. konfigurierte Erinnerungen editiert,
dupliziert, versendet, gelöscht werden. Auch die Anzeige des Versands ist
möglich.

