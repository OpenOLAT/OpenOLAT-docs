# Wie bereite ich eine Online-Prüfung vor? {: #exam_preparation}


??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie haben bereits einen Kurs mit einem Test-Kursbaustein erstellt und wollen nun eine Prüfung durchführen.<br>
    Damit Sie für mögliche Probleme gewappnet sind, zeigt Ihnen die folgende Auflistung, wo und wie Sie Vorkehrungen treffen können.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    * ["Wie gehe ich vor, wenn ich einen Test erstelle?"](../test_creation_procedure/test_creation_procedure.de.md)


---

## Ausgangssituation {: #initial_situation}

Sie haben bereits

- einen Kurs erstellt (siehe ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)),
- in diesem Kurs einen Kursbaustein "Test" eingefügt (siehe ["5. Kursbausteine hinzufügen"](../my_first_course/my_first_course.de.md#5-kursbausteine-hinzufugen)),
- eine Test-Lernressource mit allen Fragen fertiggestellt und in den Kursbaustein eingefügt
(siehe ["6. Kursbausteine konfigurieren und Lernressourcen hinzufügen"](../my_first_course/my_first_course.de.md#6-kursbausteine-konfigurieren-und-lernressourcen-hinzufugen)).

Jetzt geht es darum, mit diesem Kurs/Test eine Prüfung zu planen und durchzuführen. Damit Sie für mögliche Probleme gewappnet sind, zeigt Ihnen die folgende Auflistung, wo eventuell ein Stolperstein liegt und wie Sie Vorkehrungen treffen können.

[zum Seitenanfang ^](#exam_preparation)

---

## Wie konfiguriere ich meine Prüfung? {: #config_exam}

Die Einstellungen (Konfiguration) wird an verschiedenen Stellen und auf verschiedenen Ebenen vorgenommen.

![exam_preparation_overview_v1_de.png](assets/exam_preparation_overview_v1_de.png){ class="shadow lightbox" }

Ebene **Kurs**<br>
Auf dieser Ebene wird z.B. festgelegt, wann der Gesamtkurs als "bestanden" gilt.<br>
**Autorenbereich > Kurs wählen > Administration > Einstellungen**

Ebene **Kursbaustein**<br>
Für Prüfungen wird der Kursbaustein "Test" verwendet. Innerhalb eines Kurses kann es mehrere Test-Kursbausteine geben, z.B. einen Einstiegstest, Tests pro Themengebiet und einen Abschlusstest. Jeder Test-Kursbaustein kann anders konfiguriert werden, z.B. ob die Bewertung automatisch oder manuell erfolgen soll.<br>
**Autorenbereich > Kurs wählen > Administration > Kurseditor > Kursbaustein wählen > verschiedene Tabs**

Ebene **Lernressource**<br>
Eine Test-Lernressource kann in verschiedenen Kursbausteinen verwendet werden. Alle Einstellungen (z.B. die Anzahl erlaubter Versuche) werden dann in den jeweiligen Kursbaustein übernommen, können dort aber übersteuert werden.<br>
**Autorenbereich > Lernressource wählen > Administration > Einstellungen**

Ebene **Frage**<br>
Auf Ebene einer Frage werden z.B. Feedbacks definiert.<br>
**Autorenbereich > Lernressource wählen > Administration > Inhalt editieren > Frage wählen > verschiedene Tabs**

[zum Seitenanfang ^](#exam_preparation)

---


## Kann ich die Prüfung zur Probe einmal durchspielen? {: #test_run}

Als Autor:in möchten Sie verständlicherweise einen fertiggestellten Test zunächst selbst einmal probeweise aufrufen oder durch jemand kontrollieren lassen. Dies führt jedoch zu einem Problem:

Sobald ein Test einmal von Prüfungsteilnehmer:innen ausgefüllt und abgeschlossen wurde, werden Ergebnisse gespeichert. Wenn anschliessend der Test z.B. um eine Frage erweitert wird, haben diese Teilnehmer:innen eine andere Version bearbeitet und abgeschlossen. Sie haben möglicherweise den Test nach der neuen erweiterten Version nicht bestanden, konnten aber die zusätzlich hinzugefügten Fragen gar nie sehen und beantworten. Im Nachhinein geänderte Tests wären Urkundenfälschung und OpenOlat lässt deshalb keine Bearbeitung einmal benutzter Tests zu.

Solange Sie als Autor:in in die Teilnehmeransicht wechseln und keine Ergebnisse speichern, gilt der Test als "unbenutzt".<br>
Wenn Sie Ihren Test aber probeweise "unter realen Bedingungen" oder durch ausgewählte Personen probeweise ausfüllen lassen, gilt die Test-Lernressource als "benutzt" und kann nicht mehr abgeändert werden. Dessen sollten Sie sich bewusst sein.

Möchten Sie dennoch einen Probelauf mit Ihrem Test machen, bleibt Ihnen als Ausweg, eine Kopie der Test-Lernressource zu erstellen und mit dieser zu testen. So bleibt der eigentliche Test "unbenutzt" und Sie können die Lernressource weiterhin verändern. 

Mehr Informationen zum Vorgehen finden Sie hier:
[Wie wechsle ich einen Test aus? >](../../manual_how-to/exchange_tests/exchange_tests.de.md)<br>

[zum Seitenanfang ^](#exam_preparation)

---

## Wie wird die Prüfung gestartet und beendet? {: #start_end_exam}

Der Start und die Dauer der Prüfung wird durch die Angaben in der Konfiguration des [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md) bestimmt.

Ein Prüfungsmodus kann automatisch oder manuell aktiviert und deaktiviert werden. Diese wird von Autor:innen voreingestellt.
Für automatischen Start und Ende muss ein entsprechendes Zeitfenster eingerichtet werden unter<br> 
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"**

Wird ein manueller Start/Beendigung durch Betreuer:innen gewünscht, kann der Prüfungsmodus unter 
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"** 
durch Klicken auf den **Starten-Button** begonnen und beendet werden.<br>
Sobald ein Prüfungsmodus aktiviert wurde, wird ein Button "Beenden" bzw "Prüfung beenden" angezeigt. Klicken Sie einen der beiden Buttons. Anschliessend wechselt der Status des Prüfungsmodus auf "Beendet".

[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn Teilnehmende zu spät erscheinen? {: #participants_too_late}

Ihre Reaktion auf diese Situation hängt davon ab, wie Sie die Prüfung geplant und konfiguriert haben.

- Wurde ein automatischer Beginn und ein automatisches Beenden der Prüfung eingerichtet?
- Kommen alle Teilnehmende zu spät oder handelt es sich um eine Einzelperson? 

Wenn **alle** Prüfungsteilnehmer:innen später beginnen, kann evtl. noch das voreingestellte automatische Beenden der Prüfung angepasst werden. Dann gelten für alle Teilnehmenden die gleichen Einstellungen. Bei manuellem, verspätetem Start bleibt die konfigurierte Dauer gleich, das Ende verschiebt sich entsprechend nach hinten.

Kommen **einzelne Teilnehmer:innen** zu spät, liegt es im Ermessen der Aufsichtsperson, individuelle Verlängerung zu gewähren. 

**Vorgehen Variante 1:**

- Wählen Sie im Kurs unter Administration das Bewertungswerkzeug.
- Wählen Sie dort den Test-Kursbaustein.
- Als Betreuer:in finden Sie im Tab "Teilnehmer:innen" alle Prüfungsteilnehmer:innen mit ihrem Status angezeigt.
- Selektieren Sie bei allen betroffenen Personen die Checkbox in der ersten Spalte. Sobald mindestens eine Person ausgewählt ist, werden Ihnen über der Liste zusätzliche Buttons angezeigt.
- Wählen Sie den Button "Verlängern".
- Geben Sie die Verlängerungszeit in Minuten an. 

!!! info "Hinweis zur Verlängerungszeit"

    Die Verlängerungszeit kann nur Personen gewährt werden, die den Test bereits gestartet haben.<br> 
    Sie gilt für alle ausgewählten Personen gleich.

- Für Einzelpersonen finden Sie unter den 3 Punkten am Ende einer Zeile auch die Option "Testzeit verlängern". 

**Vorgehen Variante 2:**

Sie können die Prüfung auch wie geplant durchführen und Sie lassen auch eine automatische Beendigung durch OpenOlat zu. Nach dem Beenden können alle nicht betroffenen Personen den Prüfungsraum verlassen. Anschliessend können Sie als Betreuer:in im Bewertungswerkzeug für die betreffenden Einzelpersonen die geschlossene Prüfung manuell erneut öffnen und sie nach einer bestimmten Zeit auch manuell beenden.

[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn technische Störungen auftreten? {: #technical_problems}

Wenn technische Störungen auftreten, ist es wichtig, die genaue Ursache zu kennen. Es ist zu unterscheiden zwischen Fehlern in der Infrastruktur (ausserhalb von OpenOlat) und Problemen, die in OpenOlat selbst auftreten könnten. 

- **Stromausfall**<br>
Von Stromausfall an den Geräten der Prüfungsteilnehmer:innen ist das OpenOlat-System selbst nicht betroffen, da es auf anderen Servern läuft und im Browser angezeigt wird. In OpenOlat ist gesichert, was mit dem letzten Speichervorgang gespeichert wurde. Beim erneuten Aufruf ist der zuletzt gespeicherte Zustand wieder vorhanden.

- **Unterbrechungen im WLAN**<br>
Bei Netzwerkstörungen muss evtl. die verfügbare Prüfungszeit manuell verlängert werden um die Ausfallzeit zu kompensieren. (Vorgehen wie beschrieben unter ["Was tue ich, wenn Teilnehmende zu spät erscheinen?"](#participants_too_late).) Um schon vorher mögliche Störungen einschätzen zu können, kann einige Tage vorher schon ein sogenannter "Stress-Test" im gleichen Raum durchgeführt werden, bei dem z.B. eine mangelhafte Bandbreite des WLAN entdeckt werden kann. 

- **Zugriff auf das Internet**<br>
Ist für alle Prüfungsteilnehmer:innen der Zugriff auf OpenOlat unterbrochen, probieren Sie aus, ob auch andere Websites nicht erreichbar sind. Wenn ja, deutet das möglicherweise auf eine Störung beim Internet-Provider. Wenden Sie sich in diesem Fall für weitere Abklärungen an Ihren Techniker vor Ort.

- **Probleme in OpenOlat**<br>
Handelt es sich eindeutig um ein Problem in OpenOlat, können Sie sich an unseren Support wenden (support@openolat.com).<br> 
Ist OpenOlat bei frentix gehostet, können Sie uns bei grossen Teilnehmerzahlen gern auch vorher über Ihre Prüfung informieren, damit unsere Techniker während der laufenden Prüfung ein besonderes Auge auf Ihre OpenOlat-Instanz haben.<br>
Informationen zum Betriebsstatus unserer Webserver können Sie jederzeit abrufen unter [https://www.openolat.com/betriebsstatus/](https://www.openolat.com/betriebsstatus/).

[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn Teilnehmende bei einer laufenden Prüfung von zu Hause aus Fragen / Probleme haben? {: #communication}

Um diese mögliche Situation von vornherein zu entschärfen, kommunizieren Sie am besten schon vor Beginn der Prüfung, was die Teilnehmer:innen in einem solchen Fall tun sollen. <br>
Machen Sie sich als Betreuer:in dazu mit den Möglichkeiten von OpenOlat zur [Kommunikation während einer Prüfung](../../manual_how-to/communication_during_exam/communication_during_exam.de.md) vertraut.<br>
Evtl. können Sie auch im Prüfungskurs selbst einen Hinweis auf das Vorgehen im Notfall und eine Anleitung ergänzen. 

[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn Teilnehmende einen Test versehentlich zu früh beenden und ihn nicht mehr starten können? {: #reset_trials}

Wurde konfiguriert, dass nur 1 Lösungsversuch möglich ist, kann es passieren, dass Teilnehmende nach einem versehentlichen (zu frühen) Beenden den Test nicht mehr starten können. Gehen Sie in diesem Fall folgendermassen vor:

- Wählen Sie im Kurs unter Administration das Bewertungswerkzeug.
- Wählen Sie dort den Test-Kursbaustein.
- Als Betreuer:in finden Sie im Tab "Teilnehmer:innen" alle Prüfungsteilnehmer:innen mit ihrem Status angezeigt.
- Klicken Sie bei der betreffenden Person auf die 3 Punkte am Ende der Zeile.
- Sie finden dort die Option "Anzahl Versuche zurücksetzen".

[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn der Prüfungsmodus fehlerhaft konfiguriert ist? {: #wrong_config_assessment_mode}

Ein Prüfungsmodus wird erstellt und eingerichtet unter<br>
**Kurs → Administration → Prüfungsverwaltung → Konfiguration Prüfungsmodus**<br>
Solange der Prüfungsmodus noch nicht gestartet wurde, kann er dort bearbeitet werden. 
Bei einer bereits laufenden Prüfung ist eine nachträgliche Bearbeitung des Prüfungsmodus nicht mehr ohne weiteres möglich.

Empfehlungen:

- Während einer bereits laufenden Prüfung sollte möglichst keine Live-Änderung vorgenommen werden, die alle Teilnehmenden trifft.
- Bevor Sie einen laufenden Prüfungsmodus für alle Prüfungsteilnehmer:innen abändern, können Sie evtl. die Wirkung Ihrer Änderung an einem Testaccount prüfen.
- Wenn möglich, sollten Sie lieber die Prüfung sauber beenden, korrekt neu aufsetzen und den Versuch für die Betroffenen zurücksetzen.<br>

Vorgehen:

1. Prüfung beenden<br> (Bei manuellem Modus durch Betreuer:innen oder Kursbesitzer:innen mit dem Ende-Button im Bewertungswerkzeug.)
2. Neuen, korrekten Prüfungsmodus mit manuellem Start/Beenden anlegen.<br> Achtung: Der Start-Button wird für Betreuende erst sichtbar, sobald das konfigurierte Zeitfenster erreicht ist. Für einen sofortigen Neustart als Beginn eine unmittelbar bevorstehende Zeitangabe machen und „manuell" wählen.<br>


!!! tip "Tipp"

    Als Vorbereitung für den Notfall können Sie einen Prüfungsmodus kopieren. Legen Sie eine **Kopie** der Prüfungskonfiguration **mit späterem Startzeitpunkt** an. Diese ist wieder editierbar und die Einstellungen können dort neu eingerichtet werden. Es darf aber nicht vergessen werden, diesen Ersatz-Prüfungsmodus bei erfolgreichem Durchlauf der regulär geplanten Prüfung wieder zu löschen.

!!! warning "Nicht empfohlen"

    Der Prüfungsmodus wird auch beendet, wenn der gesamte Kurs beendet oder gelöscht wird. Dies ist jedoch ein Nebeneffekt und kein sauberer Weg. 


[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn die Testdauer/der Zeitraum fehlerhaft konfiguriert ist? {: #wrong_config_period}

Zunächst muss geklärt werden, was unter Testdauer/Zeitraum verstanden werden kann:<br>
A) die Angaben im Kursbaustein<br>
B) die Angabe im Prüfungsmodus

<h3>A) Angaben im Kursbaustein Test</h3>

**Kurs → Administration → Kurseditor → Kursbaustein wählen → Tab Lernpfad**<br>
Jeder Kursbaustein in einem Lernpfadkurs kann eine Angabe zur Freigabe enthalten. Es kann ein Zeitfenster angegeben werden, in dem auf den Kursbaustein zugegriffen werden kann. Die Angabe "zu bearbeiten bis" definiert, bis wann der Kursbaustein geöffnet werden kann. Ist ein Kursbaustein geöffnet und wird bearbeitet, während die Frist abläuft, bleibt der Baustein weiter geöffnet und kann weiter bearbeitet werden. Es erfolgt kein automatisches Beenden des Zugriffs.<br>
**Kurs → Administration → Kurseditor → Kursbaustein "Test" wählen → Tab Test-Konfiguration**<br>
Hier finden Sie einen Toggle-Button "Testzeitraum festlegen". Während diesem Testzeitraum kann der Test gestartet werden. Sobald die "bis-Zeit" erreicht ist, wird der Test automatisch beendet. Dies auch dann, wenn die definierte Testzeit noch nicht aufgebraucht ist.

Änderungen im Kurseditor in diesen Tabs während einer laufenden Prüfung sollten vermieden werden. Empfehlenswert ist in der Regel die Verwendung des Prüfungsmodus. Während eines aktiven Prüfungsmodus sind übrige Aktivitäten in OpenOlat unterbunden. Wird lediglich eine Freigabe und Zugriffsmöglichkeit im Kursbaustein konfiguriert, können weiterhin andere Kurse in OpenOlat aufgerufen werden.

<h3>B) Angabe im Prüfungsmodus</h3>

**Kurs → Administration → Prüfungsverwaltung → Konfiguration Prüfungsmodus**

Diese Angabe bezieht sich auf die Phase, in der der Prüfungsmodus aktiv ist. Also die Zeitspanne, in der die Prüfungsteilnehmer:innen in OpenOlat ausschliesslich diese Prüfung bearbeiten können.

Wurde ein Prüfungsmodus bereits gestartet, kann die Dauer nicht mehr geändert werden. Bei einem automatischen Start wird auch automatisch gemäss der eingestellten Zeit beendet. Bei einem manuellen Start wird auch manuell beendet und Sie können Dauer und Ende des Prüfungsmodus selbst bestimmen. 

<h3>Verlängerung der Testzeit</h3>

Im Fall einer automatischen Beendigung des Prüfungsmodus kann die Prüfungszeit für Teilnehmer:innen, die den Test gestartet haben, verlängert werden.

- Wählen Sie als Betreuer:in den Test-Kursbaustein
- wählen Sie den Tab Teilnehmer:innen
- Selektieren Sie in der ersten Spalte alle Checkboxen der Teilnehmer:innen, die eine Verlängerung erhalten sollen.
- Sobald mindestens eine Checkbox markiert ist, erscheint über der Liste auch der Button "Verlängern".
- Wenn Sie "Verlängern" geklickt haben, können Sie im Popup-Fenster angeben um wieviele Minuten die Testzeit verlängert werden soll.

Für Einzelpersonen finden Sie die Option zur Testzeitverlängerung auch unter den 3 Punkten am Ende einer Zeile der Teilnehmerliste.

!!! note "Hinweis"

    Beachten Sie, dass eine Verlängerung nur bei Personen gegeben werden kann, die den Test bereits gestartet haben. (Wird ein Test z.B. bereits korrigiert, kann die Bearbeitungszeit nicht mehr verlängert werden.)


Als weitere legitime Möglichkeit zur Verlängerung der Testzeit, könnte auch der Nachteilsausgleich verwendet werden. Sie finden diese Option ebenfalls unter den 3 Punkten am Ende einer Zeile.

!!! note "Hinweis"

    Bei manuellem, verspätetem Start bleibt die konfigurierte Dauer gleich, das Ende verschiebt sich entsprechend nach hinten.


[zum Seitenanfang ^](#exam_preparation)

---


## Was tue ich, wenn Testfragen fehlerhaft waren und nachträglich eine Anpassung vorgenommen werden soll? {: #questions_with_mistakes}

Ist eine Prüfung bereits von einigen Teilnehmer:innen bearbeitet worden, kann die Prüfung bzw. eine Frage selbst nicht mehr abgeändert werden.

* Handelt es sich um einen einfachen Fehler (z.B. Schreibfehler), der problemlos allen Teilnehmer noch kommuniziert werden kann, bietet sich eine Information an alle Prüfungsteilnehmer:innen an. Entweder mündlich im Prüfungsraum oder auch z.B. im Prüfungs-Chat. (Siehe [Kommunikation während einer Prüfung](../../manual_how-to/communication_during_exam/communication_during_exam.de.md)). 

* Kann eine Frage wegen des Fehlers gar nicht gelöst werden, bleibt der Ausweg, dass alle Teilnehmer:innen z.B. die vorgesehene volle Punktzahl für diese Frage erhalten. Dazu kann im Bewertungswerkzeug eine manuelle Bewertung vorgenommen werden. Informieren Sie während der laufenden Prüfung die Teilnehmer:innen und bewerten Sie die Frage dann wie angekündigt. Es empfiehlt sich, die Vergabe der Punkte mit einem entsprechenden Kommentar zur Begründung zu ergänzen.<br> 
(Siehe ["So bewerten Sie die Lösungen ausgehend von einem bestimmten Kursbaustein"](../../manual_user/learningresources/Assessment_of_learners.de.md#assess_solutions)). 

* Ist der Test so fehlerhaft, dass die Test-Lernressource ausgewechselt werden sollte?<br>
Beachten Sie in diesem Fall die Anleitung ["Wie wechsle ich einen Test aus?"](../../manual_how-to/exchange_tests/exchange_tests.de.md).

[zum Seitenanfang ^](#exam_preparation)

---

## Was kann ich gegen Betrugsversuche tun? {: #fraud_attempts}

Betrugsversuche während eine Prüfung lassen sich nie zu 100% ausschliessen. Bei Prüfungen in einem gemeinsamen Raum haben deshalb die Aufsichtspersonen eine besondere Verantwortung. 

Wenn es der Prüfungsstoff zulässt, werden oft auch "Open Book Prüfungen" durchgeführt, an denen die Benutzung von Hilfsmitteln grundsätzlich erlaubt ist. Die Prüfungszeit wird dann aber so begrenzt, dass keine Zeit zum "Just-in-time-Lernen" bleibt.

Seitens OpenOlat kann zu Beginn einer Prüfung den Teilnehmenden vorab eine Erklärung zur Bestätigung vorgelegt werden. Insbesondere muss z.B. die Verwendung von KI-Tools klar geregelt sein. Evtl. kann z.B. zur Bedingung gemacht werden, dass die Prüfungsteilnehmer:innen der Überwachung und Protokollierung des gesamten Datenverkehrs von und zu ihrem Rechner während der Prüfung zustimmen müssen.

Eine Erklärung kann für einzelne Kurse in OpenOlat (in diesem Fall den Kurs mit der Prüfung) eingerichtet werden unter<br>
**Administration > Einstellungen > Tab "Nutzungsbedingungen"**.<br>
Siehe auch [Kursspezifische Nutzungsbedingungen >](../../manual_user/basic_concepts/Terms_Of_Use.de.md#terms_of_use_course)<br>

Um nach dem Start eines Tests alle anderen Aktivitäten in OpenOlat zu unterbinden, verwenden Sie einen [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md).

Um nach dem Start eines Tests auch alle sonstigen Aktivitäten auf dem Rechner der Prüfungsteilnehmer einzuschränken, verwenden Sie den [Safe Exam Browser (SEB)](../../manual_how-to/SEB/SEB.de.md).

In einem Prüfungsmodus kann auch eine Einschränkung auf bestimmte IP-Adressen vorgenommen werden. So kann die Teilnahme an der Prüfung auf die ausschliessliche Nutzung von Geräten in einem Prüfungsraum begrenzt werden.

[zum Seitenanfang ^](#exam_preparation)

---

## Was tue ich, wenn der Test versehentlich ein zweites Mal gestartet wurde, aber der erste Versuch bewertet werden soll? {: #asses_other_attempts}

Es kann vorkommen, dass Prüfungsteilnehmer:innen versehentlich einen nicht vollständig bearbeiteten Test beendet haben und dann den Test ein zweites Mal starten. Ein Neustart wird als zweiter Versuch gespeichert, bei dem wieder ganz von vorne begonnen werden kann. Die Einträge des vorangehenden Versuchs werden nicht übernommen. Alle Versuche werden jedoch gespeichert und können von Betreuer:innen und Kursbesitzer:innen im Bewertungswerkzeug eingesehen werden.

- Wählen Sie als Betreuer:in oder Kursbesitzer:in den Kurs.
- Öffnen Sie das Bewertungswerkzeug unter Administration > Bewertungswerkzeug.
- Wählen Sie den betreffenden Test-Kursbaustein.
- Wählen Sie den Tab "Teilnehmer:innen".
- Öffnen Sie die Übersicht der betreffende Person durch Klick auf einen Namen.
- Es werden alle Testversuche dieser Person angezeigt. 
- Klicken Sie beim Testversuch auf die 3 Punkte am Ende der Zeile. Dort können Sie die einzelnen Testversuche annullieren und den ersten Versuch wieder.

[zum Seitenanfang ^](#exam_preparation)

---

## Wie kann ich die Einsichtnahme in die Prüfungsergebnisse vorbereiten? {: #assesment_inspection}

Um nach einer Prüfung individuelle Prüfungseinsichten für Teilnehmer:innen von Tests erstellen zu können, müssen Sie die [Prüfungseinsicht](../../manual_user/learningresources/Assessment_inspection.de.md) entsprechend konfigurieren unter<br>
**Kurs → Administration → Prüfungsverwaltung → Tab Konfiguration Prüfungseinsicht**<br>
Hier können Sie z.B. die Dauer, die Resultatanzeige, sowie Einschränkungen festlegen.

Betreuer:innen können dann im Bewertungswerkzeug mit diesen Vorgaben für einzelne Teilnehmer:innen Einsichtnahmen terminieren.

[zum Seitenanfang ^](#exam_preparation)

---


## Checkliste {: #checklist}

- [x] Regeln zur Prüfung erstellt? (Erlaubtes und Unerlaubtes)
- [x] Prüfungsteilnehmer:innen über die Regeln informiert? ([Nutzungsbedingungen eines Kurs definiert?)
- [x] Kommunikation während der Prüfung vorher geklärt? (z.B. Verwendung des Prüfungs-Chats)
- [x] Verfahren zum Starten und Beenden der Prüfung vorab geklärt? (Automatisch? Manuell? Durch wen?)
- [x] Instruktion zum Beenden der Prüfung gegeben? 
- [x] Probeklausur durchgeführt? Mit allen Prüfungsteilnehmer:innen?
- [x] Prüfungsmodus konfiguriert?
- [x] Safe Exam Browser konfiguriert?
- [x] Bei sehr grosser Teilnehmerzahl: frentix vorab über den Prüfungstermin informiert?
- [x] Ist nach der Prüfung eine Prüfungseinsicht vorgesehen/eingerichtet?

[zum Seitenanfang ^](#exam_preparation)

---


## Weiterführende Informationen {: #further_information}

[Nutzungsbedingungen eines Kurs definieren >](../../manual_user/basic_concepts/Terms_Of_Use.de.md#nutzungsbedingungen-eines-kurs-definieren)<br>
[Prüfungsmodus >](../../manual_user/learningresources/Assessment_mode.de.md)<br>
[Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor? >](../../manual_how-to/SEB/SEB.de.md)<br>
[Wie wechsle ich einen Test aus? >](../../manual_how-to/exchange_tests/exchange_tests.de.md)<br>
[Prüfungseinsicht > ](../../manual_user/learningresources/Assessment_inspection.de.md)<br>

[zum Seitenanfang ^](#exam_preparation)
