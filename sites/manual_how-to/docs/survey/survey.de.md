# Wie kann ich am Ende eines Kurses eine Umfrage durchführen? {: #survey}


??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie haben bereits einen OpenOlat-Kurs erstellt?<br>
    Sie können zur Qualitätskontrolle und -verbesserung nach Kursende ein Feedback zum Kurs von den Teilnehmer:innen eingeholen, indem sie eine Umfrage ausfüllen lassen.
    Die folgende Anleitung zeigt Ihnen, wie Sie dies mit einem Kursbaustein "Unfrage" einrichten.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen [ ] Administrator:innen

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    * [Wie erstelle ich eine Formular-Lernressource? >](../../manual_how-to/create_a_form/create_a_form.de.md)<br>
    * Kurs mit Durchführungszeitraum versehen
    * Formular in Kurs einbinden
  

---


## Was versteht man in OpenOlat unter einer Umfrage? {: #survey_description}

Sie sollten 4 Begriffe unterscheiden:

- **Lernressource "Formular"**<br>
Ein Formular mit mehreren Fragen wird in OpenOlat als **Lernressource** erstellt und im Autorenbereich abgelegt. Diese Formular-Lernressource kann mehrfach in verschiedenen Kursbausteinen wiederverwendet werden.

- Die **Fragen** (Einzelauswahl, Mehrfachauswahl, Texteingabe, Rubrik, usw.) stellen Sie zusammen, indem Sie eine Lernressource "Formular" erstellen und editieren.

- **Kursbaustein "Formular"**<br>
In den **Kursbaustein** "Formular" wird eine **Lernressource** "Formular" eingefügt. Bitte verwechseln Sie Lernressource und Kursbaustein nicht. Der Kursbaustein bindet das Formular an einer bestimmten Stelle im Kurs ein – für eine Abschlussbefragung also am Ende des Kurses.

- **Kursbaustein "Umfrage"**<br>
Auch in diesen Kursbaustein wird eine Lernressource "Formular" eingefügt. Im Unterschied zum Kursbaustein "Formular" werden im Kursbaustein "Umfrage" die Fragen standardmässig **anonym beantwortet**. Wenn Betreuer:innen die abgegebenen Formulare begutachten, finden Sie dort keine namentliche Zuordnung. (Ausnahme: Wenn Sie in der Formular-Lernressource Eingabefelder für Name, Vorname usw. einfügen, ist die Umfrage natürlich auch nicht mehr annonym. Der Auswertungsmechanismus im Kursbaustein "Umfrage" ist aber prinzipiell auf Anonymität ausgelegt.)

[zum Seitenanfang ^](#survey)

---

## Schritt 1: Kursbaustein "Umfrage" in den Kurs einfügen {: #step1}

Wir gehen davon aus, dass Sie bereits einen Kurs erstellt haben. Dort können Sie am Ende des Kurses einen weiteren Kursbaustein einfügen. Wenn es eine anonyme Umfrage werden soll, verwenden Sie den Kursbaustein "Umfrage". (Im Folgenden gehen wir von diesem Kursbaustein aus.) Alternativ können Sie den Kursbaustein "Formular" verwenden, in dem die Antworten den jeweiligen Teilnehmenden zugeordnet werden können.

!!! info "Hinweis"

    Auch bei Verwendung des Kursbausteins "Umfrage" (anonymisierte Umfrage) stellt OpenOlat sicher, dass Teilnehmende die Umfrage nur einmal ausfüllen können.

Öffnen Sie in der Kurs-Administration den **Kurseditor** und fügen Sie den Kursbaustein **"Umfrage"** ein. Platzieren Sie ihn an das Ende der Kursstruktur, damit er als Abschlussbefragung erscheint.

Nach dem Einfügen stehen Ihnen im Kurseditor die folgenden Tabs zum Einrichten/Konfigurieren zur Verfügung:

* **Titel und Beschreibung** – allgemeine Angaben zum Kursbaustein
* **Layout** – optische Darstellung
* **Lernpfad** (bei Lernpfadkursen) bzw. **Sichtbarkeit** und **Zugang** (bei klassischen Kursen)
* **Umfrage** – die zentrale Konfiguration, in der Sie auch die Lernressource einbinden (siehe Schritt 2)

Nehmen Sie die gewünschten Einstellungen vor.

[zum Seitenanfang ^](#survey)

---

## Schritt 2: Formular-Lernressource erstellen {: #step2}

!!! hint "Empfehlung"

    Wenn Sie noch nie ein Formular für Befragungen erstellt haben, lesen Sie zuerst die Anleitung ["Wie erstelle ich eine Formular-Lernressource?"](../create_a_form/create_a_form.de.md). Dort wird gezeigt, wie Sie die Fragen zusammenstellen.

Bereiten Sie zunächst das Formular (genauer: die Formular-Lernressource) mit den gewünschten Fragen vor. Dafür haben Sie zwei Möglichkeiten:

#### Vorgehensweise 1: Lernressouce -> Kursbaustein
a) Erstellung der Formular-Lernressource im Autorenbereich<br>
b) Einfügen der Lernressource in den Kursbaustein

#### Vorgehensweise 2: Kursbaustein -> Lernressource
a) Wählen Sie im Kurseditor den Kursbaustein und dort den Tab "Umfrage".<br>
b) Klicken Sie auf den Button "Wählen, erstellen oder importieren".<br> 
Es wird Ihnen eine Liste bereits vorhandener Lernressourcen angezeigt, bei denen Sie Besitzer:in sind.<br>
Sie können dort eine auswählen oder mit dem Button über der Liste eine neue Formular-Lernressource erstellen.<br>
So gelangen Sie in den Editor des Formulars und können dort die Fragen erstellen.<br>
Sobald die Lernressource gespeichert ist, wird auch sie im Autorenbereich angezeigt.

!!! tip "Tipp"

    Für eine Abschlussumfrage zur Kursqualität eignen sich häufig **Single-Choice-Fragen** (nötigen zu einer eindeutigen Stellungnahme) oder **Rubrik-Elemente** (Ampel-/Skalensystem). So bleibt der Aufwand für die Teilnehmenden gering.

[zum Seitenanfang ^](#survey)

---

## Schritt 3: Formular-Lernressource in den Umfrage-Kursbaustein einfügen {: #step3}

Wenn Sie so vorgegangen sind, dass Sie zuerst den Kursbaustein gewählt und dann die Lernressource erstellt haben (Schritt2, Vorgehensweise 2), dann ist die Formular-Lernressource bereits in den Kursbausein eingefügt und dieser Schritt entfällt.

Haben Sie zunächst die Formular-Lernressource im Autorenbereich erstellt (Schritt 2, Vorgehensweise 1), dann muss die Lernressource noch in den Umfrage-Kursbaustein eingebunden werden.

- Öffnen Sie den **Kurseditor** und wählen Sie den **Kursbaustein** mit Ihrer Abschlussumfrage.
- Wählen Sie den **Tab "Umfrage"**.
- Mit dem **Button "Wählen, erstellen oder importieren"** binden Sie die Formular-Lernressource in den Kursbaustein ein. In der Übersicht werden alle Formulare angezeigt, bei denen Sie Besitzer:in sind. Wählen Sie das gewünschte Formular aus.

!!! warning "Achtung"

    Sobald ein Formular von mindestens einer teilnehmenden Person angesehen wurde, kann es **nicht mehr ersetzt** werden – der Button "Ersetzen" entfällt. Muss es dennoch ausgetauscht werden, legen Sie einen neuen Kursbaustein "Umfrage" an und binden Sie dort das gewünschte Formular ein.

[zum Seitenanfang ^](#survey)

---


## Schritt 4: Zugriff auf die Umfrage einrichten {: #step4}

Soll der Umfrage-Kursbaustein erst ab einem bestimmten Zeitpunkt sichtbar sein?<br>
Soll die Umfrage erst ab einem bestimmtem Zeitpunkt ausgefüllt werden können?<br>
Sollen nur bestimmte Personen die Umfrage ausfüllen können?<br>
Soll die Umfrage erst möglich sein, wenn ein bestimmter Bearbeitungsstand im Kurs erreicht ist?<br> 
(Z.B. alle Kursbausteine bearbeitet, ein Test bestanden, o.a.)<br>
Soll der Kurs erst als abgeschlossen gelten, wenn auch die Umfrage ausgefüllt wurde?<br>
Wer soll die Umfrageresultate einsehen und auswerten können?

All diese Fragen haben mit Zugriffsrechten zu tun, die Sie steuern

a) über den **Tab "Umfrage"**<br>
b) über den **Tab "Lernpfad"** (in Lernpfad-Kursen)<br>
c) über die **Tabs "Sichtbarkeit"** und **"Zugang"** (in herkömmlichen Kursen) 


### Schritt 4 a): Berechtigungen festlegen im Tab "Umfrage" {: #step4a}

Im Bereich **"Berechtigungen"** des Tabs "Umfrage" legen Sie fest, **wer die Umfrage ausfüllen** und **wer die Ergebnisse einsehen** darf. Zur Auswahl stehen jeweils:

* die **Besitzer:innen** des Kurses
* die **Betreuer:innen** des Kurses
* die **Teilnehmer:innen** des Kurses (alle Personen in der Rolle "Teilnehmer:in")
* **Gäste** (Personen ohne OpenOlat-Account)

Aktivieren Sie die **erweiterte Konfiguration**, können Sie zusätzliche Einstellungen vornehmen, z.B. bestimmte **Zeiträume** der Teilnahme für bestimmte Rollen definieren oder die Teilnahme auf bestimmte Gruppen festlegen. Auch die Freigabe der Ergebnisse lässt sich mit einem Beginn- und Enddatum verbinden.

!!! tip "Tipp"

    Voraussetzung für die Teilnahme ist, dass der **gesamte Kurs** für die jeweilige Personengruppe freigegeben ist. Soll die Abschlussumfrage z.B. auch von Gästen ausfüllbar sein, muss der Kurs ein Zugangs-Angebot für Gäste beinhalten. Beachten Sie: Eine Kursfreigabe für Gäste ist nur bei klassischen Kursen möglich, nicht bei Lernpfad-Kursen.


### Schritt 4 b): Berechtigungen festlegen im Tab "Lernpfad" (in Lernpfad-Kursen) {: #step4b}

Damit die Umfrage tatsächlich als **Abschluss** wirkt, möchten Sie vielleicht, dass die Umfrage erst erscheint oder ausfüllbar ist, wenn der Rest des Kurses bereits bearbeitet wurde.

- Mit eingeschalteten Ausnahmeregeln im Tab "Lernpfad" kann sehr gezielt bestimmt werden, dass nur bestimmte Personen die Umfrage im Kursmenü vorfinden.

- Wenn vorangehende Kursbausteine im Tab "Lernpfad" so konfiguriert sind, dass dort "obligatorisch" ein "erledigt" erreicht werden muss, können die Teilnehmenden erst am Ende des Kurses zur Umfrage gelangen. Der Kursbaustein ist aber ständig im Menü sichtbar.

- Im Tab "Lernpfad" können Sie das **Erledigungskriterium "Umfrage teilgenommen"** wählen. Wenn dann gleichzeitig das Kriterium für das Bestehen des gesamten Kurses die Erledigung aller oder bestimmter Kursbausteine erfordert (Administration > Einstellungen > Tab Bewertung), können Sie damit das Ausfüllen der Umfrage mit zur Bedingung für den Kursabschluss machen.


### Schritt 4 c): Berechtigungen festlegen in den Tabs "Sichtbarkeit" und "Zugang" (in herkömmlichen Kursen) {: #step4c}

In **klassischen/herkömmlichen Kursen** definieren Sie über die Tabs **"Sichtbarkeit"** und **"Zugang"**, wer den Kursbaustein "Umfrage" wann sehen bzw. bearbeiten darf. Über datumsabhängige Regeln kann die Umfrage z.B. erst gegen Kursende sichtbar oder zugänglich gemacht werden.

Die Vorgehensweise zur Einstellung der Sichtbarkeit im herkömmlichen Kurs ist folgende:<br>
Auf dem Umfrage-Baustein muss im Tab Sichtbarkeit eine Regel hinterlegt sein, um festzulegen, wann der Baustein sichtbar sein soll. Dies ist im einfachen Konfigurationsmodus nur mit absoluten Daten machbar. Um mit relativen Daten zu arbeiten, muss in den Expertenmodus gewechselt werden. Damit kann gesteuert werden, dass die Umfrage z.B. erst bei Kursende z.B. für eine Woche angezeigt wird.

1. Expertenmodus öffnen

- Im Kurseditor zum Baustein "Umfrage" navigieren<br>
- Tab "Sichtbarkeit" öffnen<br>
- Auf Schaltfläche "Expertenmodus anzeigen" klicken

2. Variante a): Expertenregel anlegen: Dauer nach Kursbeginn

- Fügen Sie folgende Expertenregel hinzu: (today <= getCourseBeginDate(0) + 7d)<br>
Diese Expertenregel besagt, dass die Umfrage nach dem Kursbeginn 7 Tage lang sichtbar sein soll.
Die Anzahl Tage kann nach Wunsch angepasst werden.

2. Variante b): Expertenregel anlegen: Dauer nach Kursende

- Fügen Sie folgende Expertenregel hinzu: (getCourseEndDate(0) >= today) & (getCourseEndDate(0) + 7d >= today)<br>
Diese Expertenregel besagt, dass die Umfrage nach dem Kursende 7 Tage lang sichtbar sein soll.
Die Anzahl Tage kann nach Wunsch angepasst werden.

3. Speichern

- Speichern Sie Ihre Expertenregeln und publizieren Sie Ihren Kurs erneut.

---

!!! info "Anonym oder personalisiert?"

    Die Resultate werden im Kursbaustein "Umfrage" standardmässig **anonymisiert** gespeichert. Eine personalisierte Auswertung ist möglich, indem im Formular-Editor das Element **"Informationen"** hinzugefügt wird – dadurch wird die Anonymität aufgehoben.

[zum Seitenanfang ^](#survey)

---


## Schritt 5: Erinnerungen einrichten {: #step5}

Über das Erinnerungswerkzeug (Administration > Erinnerungen) können Sie z.B. 3 Tage nach Kursende eine Erinnerung versenden, damit die Teilnehmer die Umfrage ausfüllen.

Erinnerung hinzufügen:

- Im Drop-Down-Menü "Administration" den Punkt "Erinnerung" öffnen
- Schaltfläche "Erinnerung erstellen" klicken. Eine neue Erinnerung öffnet sich.
- Beschreibung eingeben
- Bedingungen hinzufügen: Z.B. "Nach Kursende"
- E-Mail Betreff und Text einfügen
- Speichern


[zum Seitenanfang ^](#survey)

---


## Schritt 6: Ausfüllen der Umfrage durch die Teilnehmenden {: #step6}

Was die Teilnehmenden sehen, hängt von den im Tab "Umfrage" gesetzten Berechtigungen ab:

* Hat eine Person das Recht, das Formular auszufüllen, sieht sie zunächst das **Formular**.
* Die Umfrage kann **nur einmal** ausgefüllt und nach dem Abschicken **nicht mehr geändert** werden. Soll das Formular noch nicht abgeschickt werden, steht die Option **"Zwischenspeichern"** zur Verfügung.
* Ist die Person berechtigt auszufüllen, aber **nicht** die Ergebnisse zu sehen, erscheint nach dem Ausfüllen die Meldung: *"Sie haben das Formular bereits ausgefüllt. Vielen Dank für Ihre Teilnahme."*
* Ist die Person auch berechtigt, die Ergebnisse zu sehen, erscheint nach dem Ausfüllen direkt die **Statistik-Übersicht** beim Umfrage-Baustein.
* Ist eine Person weder zum Ausfüllen noch zum Einsehen der Resultate berechtigt, erscheint die Meldung **"Kein Zugang"**.

!!! warning "Achtung"

    Wenn Teilnehmende die Umfrage gerade ausführen, aber noch nicht abgeschlossen haben, gehen deren Resultate verloren, falls das Formular in dieser Zeit verändert wird.


[Zum Seitenanfang ^](#end_of_course_survey)

---

## Schritt 7: Ergebnisse auswerten {: #step7}

Kursbesitzer:innen und allen Betreuer:innen des Kurses werden bei Klick auf den Kursbaustein "Umfrage" folgende Tabs angezeigt:

* **Übersicht**: Anzahl der Personen, die den Fragebogen ausgefüllt haben, Abgabezeitraum sowie durchschnittliche Bearbeitungsdauer. Je nach Fragetyp werden weitere Kennzahlen aufgeführt.
* **Tabellen**: Die einzelnen Fragen und Antworten, bei Rubriks zusätzliche statistische Auswertungen. Freitexte lassen sich als Excel-Tabelle herunterladen.
* **Diagramme**: Grafische Darstellung der einzelnen Fragen als Balkendiagramme mit statistischen Daten wie Median, Varianz und Standardabweichung.
* **Einzelne Formulare**: Zugriff auf jedes einzelne (anonym) ausgefüllte Formular.

Die Inhalte aller Tabs können **ausgedruckt** oder als **Excel-Tabelle** bzw. **PDF** heruntergeladen werden.

!!! info "Weitere Zugriffswege auf die Auswertung"

    Dieselbe Auswertung finden Sie auch im Menü `Administration > Fragebogen Statistiken`. Zusätzlich können die Ergebnisse als Teil der **Kursarchivierung** gespeichert werden – dabei lassen sich sogar die Ergebnisse mehrerer Kursbausteine in einem ZIP-File bündeln.


[Zum Seitenanfang ^](#survey)

---

## Nachträgliche Änderungen an der Formular-Lernressource {: #changes}

Sobald ein im Kurs eingebundenes Formular aufgerufen wurde, kann es nur noch **eingeschränkt** geändert werden. Texte (z.B. Tippfehler) lassen sich korrigieren, aber einzelne Blöcke können nicht mehr verschoben und keine Bereiche neu angelegt oder gelöscht werden. Im Formular erscheint dann die Meldung *"Die Ressource wird bereits verwendet …"*.

Planen Sie den Inhalt der Abschlussumfrage daher möglichst vollständig, bevor die Teilnehmenden Zugriff erhalten.

[zum Seitenanfang ^](#survey)

---

## Umfrage zurücksetzen {: #reset}

Kursbesitzer:innen können bereits ausgefüllte Formulare über das **3-Punkte-Menü** des Kursbausteins mit **"Zurücksetzen"** löschen. Dabei werden **alle** bereits eingereichten Formulare dieser Umfrage gelöscht.

Ein Zurücksetzen **einzelner** Formulare ist im Kursbaustein "Umfrage" **nicht** möglich, da die Abgabe anonym erfolgt.

[Zum Seitenanfang ^](#survey)

---


## Checkliste {: #survey_checklist}

- [x] Ist das Formular mit allen gewünschten Fragen vollständig vorbereitet?
- [x] Ist der Kursbaustein "Umfrage" am Ende der Kursstruktur platziert?
- [x] Ist im Tab "Umfrage" das richtige Formular ausgewählt?
- [x] Ist festgelegt, wer die Umfrage ausfüllen darf?
- [x] Ist geklärt, ob die Umfrage anonym oder personalisiert erfolgen soll?
- [x] Ist der Kurs für die vorgesehenen Personengruppen freigegeben (ggf. inkl. Gäste)?
- [x] Erscheint die Umfrage über Lernpfad- bzw. Sichtbarkeits-/Zugangsregeln erst am Kursende?
- [x] Ist festgelegt, wer die Ergebnisse einsehen darf?

[zum Seitenanfang ^](#survey)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Wie erstelle ich eine Formular-Lernressource? >](../../manual_how-to/create_a_form/create_a_form.de.md)<br>
[Kursbaustein Umfrage >](../../manual_user/learningresources/Course_Element_Survey.de.md)<br>
[Kursbaustein Formular >](../../manual_user/learningresources/Course_Element_Form.de.md)<br>
[Der Formular-Editor >](../../manual_user/learningresources/Form_Editor.de.md)<br>
[Formular-Elemente >](../../manual_user/learningresources/Form_Elements.de.md)<br>
[Fragebogen Statistiken >](../../manual_user/learningresources/Statistics_Survey.de.md)<br>
[Formulare - Übersicht >](../../manual_user/learningresources/Form.de.md)<br>
[Zugangskonfiguration / Freigabe >](../../manual_user/learningresources/Access_configuration.de.md)<br>

**Weiterführend**<br>
[Erinnerungen >](../../manual_user/learningresources/Course_Reminders.de.md)<br>
[Formulare in Kursen >](../../manual_user/learningresources/Forms_in_Courses.de.md)<br>
[Lernpfadkurs - Kurseditor >](../../manual_user/learningresources/Learning_path_course_Course_editor.de.md)<br>
[Autorenbereich - Übersicht >](../../manual_user/area_modules/Authoring.de.md)<br>
[Zugangskonfiguration / Freigabe >](../../manual_user/learningresources/Access_configuration.de.md)<br>
[Kursadministration - Archivierung & Reports >](../../manual_user/learningresources/Course_Archiving.de.md)<br>


[zum Seitenanfang ^](#survey)

