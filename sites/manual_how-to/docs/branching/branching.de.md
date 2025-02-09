# Wie erstelle ich kursinterne Verzweigungen? (Branching) {: #branching}




??? abstract "Ziel und Inhalt dieser Anleitung"

    Verzweigte Szenarien bieten die Möglichkeit interaktive Lehr-/Lernsettings zu erstellen, die es erforderlich machen, dass die Lernenden Entscheidungen treffen. Je nach gewählter Option werden die Lernenden dann auf unterschiedliche Seiten bzw. zu unterschiedlichen weiterführenden Informationen oder Aktionen geleitet. 
Die folgende Anleitung zeigt, wie man derartige Lehr-/Lernsettings mit OpenOlat umsetzen kann. 


??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [ ] Anfänger:innen [x] Fortgeschrittene  [x] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * Sie haben bereits einen OpenOlat Kurs erstellt und kennen sich mit dem Hinzufügen von Kursbausteinen aus. 
    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    

---


## Wie können Verzweigungen in einem Kurs aufgebaut sein? {: #description}

Es gibt verschiedene Möglichkeiten, wie man die Struktur für Branching-Szenarien gestalten kann. Hier drei typische Beispiele:

a) **Lineares Branching (Perlenkettenmodell):**
Die Hauptknoten/Seiten werden nacheinander abgearbeitet. Die Entscheidungen führen nur zu kleinen Einschüben/Schleifen oder stellen unterschiedliche Informationen bereit. 
Ein eher einfacher Ansatz.

b) **Verzweigtes Branching**
Bei dieser Struktur gibt es mehrere Entscheidungspunkte, an denen Lernende zwischen verschiedenen Optionen wählen können. Jede Wahl führt zu unterschiedlichen Verzweigungen, die neue Entscheidungsmöglichkeiten eröffnen aber sie auch auf bestimmte Wege beschränken können. 
Je nachdem ob auch zunächst nicht gewählte Wege weiter zugänglich sind oer nicht ist der Aufbau eher hierarchisch oder durchlässig.

c) **Netzwerk-Branching** 
Diese Struktur erlaubt es Lernenden, zwischen verschiedenen Entscheidungspunkten zu navigieren, unabhängig von der Reihenfolge. Das Szenario ist nicht-linear und bietet eine Vielzahl von Möglichkeiten, um verschiedene Wege zu erkunden. Diese Struktur eignet sich besonders für komplexe Themen, die viele Facetten haben oder Stories, die mit vielen Auswahloptionen starten wollen. 


[Zum Seitenanfang ^](#branching)

---


## Wie plane ich ein Branching Szenario? {: #plan}

Die Gestaltung von Branching-Szenarien erfordert eine sorgfältige Planung: Lehrende sollten klare Lernziele definieren und eine nachvollziehbare Handlungswege entwickeln. 

Ein Branching-Szenario ist narrativ und besteht aus einer Gesamt-Story, die auch das Lernziel widerspiegelt. Die Gesamt-Story verteilt sich auf mehrere Seiten, auch Knoten genannt, die über die jeweiligen Wahlmöglichkeiten miteinander verbunden sind.  Planen Sie jeden dieser Knoten  und behalten Sie die gesamte Story im Blick. 

Eine einzelne Seite besteht aus mindestens folgenden Elementen:

* Einem eindeutigen Namen bzw. **Titel**. Dieser wird auch für die Verknüpfung benötigt.
* Einem **Story-Element**, meist ein Text aber auch Bilder, Videos oder Kombinationen verschiedener Multimedia-Elemente sind möglich
* Zwei bis fünf **Wahlmöglichkeiten**, die aus der Story abgeleitet werden. Jede Wahlmöglichkeit führt dann jeweils zu einer neuen Seite bzw. einem neuen Knoten. Diese neuen Seiten bilden gleichzeitig auch das Feedback bezüglich der getroffenen Wahl für die Lernenden.

### Finden Sie Ihr Thema, Ihre Story
* Was ist Ihr Thema, Ihr Inhalt?
* Wer ist ihre Zielgruppe? Sind die Wahlentscheidungen interessant und relevant für die Zielgruppe?
* Was sind Lernziele?
* Welche Wahlentscheidungen wären thematisch gut und wichtig?
* Wie wollen sie Spannung einbauen?
* Überlegen Sie auch wie Sie das Szenario konkret einsetzen wollen z.B. zur individuellen Nutzung, Dozentengeleitet im Plenum, als Wettbewerb, wer als erstes den Zielknoten erreicht? Usw.
* Ist das Branching-Szenario Teil eines komplexeren Settings? Soll es noch mit anderen OpenOlat Elementen wie Quiz, Evaluation, Reflexion u.ä. kombiniert werden? 

### Herangehensweise
Es gibt mehrere Möglichkeiten, wie man konkret vorgehen könnte um ein Branching-Szenario für und mit OpenOlat zu erstellen.

**a)	Erst Struktur dann Inhalte umsetzen**

Mann kann zunächst die gesamte Verzweigungsstruktur planen, diese dann in OpenOlat umsetzen und die passenden (HTML-)Seiten anlegen. Die OpenOlat Navigation spiegelt dann die Struktur des verzweigten Szenarios wider. Anschliessend werden die angelegten (HTML-)Seiten mit den konkreten Inhalten bzw. Story-Teilen gefüllt.  Dieses Vorgehen ist gut geeignet für verzweigtes Branching und Netzwerk Branching. 

**b)	Sukzessiver Aufbau**

Sie haben eine spannende Idee, aber noch keine konkrete Verzweigungsstruktur und möchten Ihr Szenario nach und nach entwickeln? Dann gehen Sie so vor: Starten Sie mit der Story der Startseite und den ersten Wahlmöglichkeiten. Gestalten Sie nun nach und nach die unterschiedlichen Wahlmöglichkeiten aus. Achten Sie aber darauf die Teile wieder gut zusammenzuführen. Dieses Vorgehen ist gut geeignet für hierarchische Strukturen und verzweigtes Branching.

**c) Aus linear mach verzweigt**

Sie verfügen bereits über eine passende lineare Story? Dann ergänzen Sie diese mit passenden Verzweigungen an bestimmten Stellen. Diese Wahlmöglichkeiten können zu einer unterschiedlichen Fokussierung oder Vertiefung, führen führe aber letztendlich immer wieder zum nächsten Kapitel. Teilen Sie hierfür ihre Story in passende „Kapitel“ und verzweigen Sie bei jedem Kapitel. Dieses Vorgehen passt gut zum Perlenkettenmodell.



[Zum Seitenanfang ^](#branching)


---

## Wie erstelle ich mein geplantes Szenario in OpenOlat?  {: #create}

Sie benötigen: 
* einen **herkömmlichen Kurs**
* viele **Kursbausteine "HTML-Seite"**. Die Bearbeitung erfolgt dann im HTML-Editor. Alternativ kann auch der Kursbaustein Seite verwendet werden.
* OpenOlat interne **JavaScript Links** der Kursbausteine. Diese können im Kurseditor ausgelesen werden.
* Passende Konfiguration in den Kurs **"Einstellungen"** unter „Administration“ zum ausblenden der Navigation

Je nach Ausgestaltung benötigen Sie eventuell noch weitere Kursbausteine wie Test, Webcam-Aufnahmen, Formulare usw. In den meisten Fällen werden Sie auch Grafiken für die Visualisierung benötigen. 
Im Folgenden wird das Vorgehen bei Verwendung des Kursbausteins „HTML-Seite“ beschrieben. 

### Schritt 1: Kurs erstellen

Erstellen Sie einen neuen klassischen (herkömmlichen) OpenOlat Kurs.

!!! info „Hinweis“

    Warum kein Lernpfad-Kurs? Der Kurs-Typ Lernpfad bringt für dieses Szenario keinen Mehrwert und schränkt auch die Nutzung für Gäste ein. Ferner sind die Wege durch den Kurs je nach Entscheidungen der User unterschiedlich. Ziel ist es also in der Regel gar nicht 100% Fortschritt zu erreichen. 


### Schritt 2: Startseite anlegen

Gehen Sie in den Kurseditor und fügen Sie einen Kursbaustein „HTML-Seite“ hinzu. Vergeben Sie als Titel im Tab „Titel und Beschreibung“ einen sinnvollen Titel z.B. „Startseite.“ Achten Sie auch im Weiteren auf eine möglichst eindeutige Bezeichnung von allen weiteren zu erstellenden Kursbausteinen. Das hilft Ihnen bei der Orientierung im Szenario.

Gehen Sie in den Tab „Seiteninhalt“ und erstellen Sie eine neue Datei HTML-Seite. Es ist sinnvoll hierfür denselben Titel wie im Tab Titel und Beschreibung zu verwenden. Erlauben Sie sofern notwendig auch den Link im gesamten Ablageordner. 

### Schritt 3: Seite ausgestalten und Verzweigungen einbauen

Nun können Sie die angelegte HTML-Seite über den Link „Seite bearbeiten“ ausgestalten und mit Inhalten/Story und Wahlmöglichkeiten füllen.  
Sie benötigen für jeden Knoten mindestens zwei Wahloptionen, sollten aber zumindest zu Beginn darauf achten, nicht zu viele Wahloptionen bereitzustellen, damit das Szenario nicht zu komplex wird. 
Damit ist die erste Seite fertig. 

### Schritt 4: Wahl-Seiten anlegen und ausgestalten 

Gehen Sie wieder in den Kurseditor und legen Sie für jede der auf der Startseite genannten Wahloptionen eine neue HTML-Seite an. Gehen Sie dabei ähnlich wie in Schritt 2 vor. Vergeben Sie wieder einen kurzen, eindeutigen Titel, der die Wahloption deutlich macht. Ergänzen Sie zur Orientierung eventuell noch eine Nummer. 

Anschliessend müssen die neuen HTML-Seiten mit der jeweiligen Story-Fortsetzung und den nächsten Wahlmöglichkeiten ausgestaltet werden. Das Vorgehen erfolgt dabei in Anlehnung an Schritt 3. 

Gehen Sie nun für jeden Knoten in derselben Weise vor:<br> 
Kursbaustein „HTML-Seite“ einfügen -> Titel vergeben -> Seite erstellen -> Seite inhaltlich ausgestalten -> Wahloptionen einfügen.

!!! info „Tipp“

    Nutzen Sie am besten drei Wahloptionen für ein interessantes, aber noch überschaubares Szenario. In Ausnahmefällen können Sie im Verlauf des Szenarios auch nur einen weiterführenden Link verwenden, wenn Sie den Usern keine wirkliche Wahl lassen wollen. 

### Schritt 5: Verlinkungen auslesen 

Damit die diversen erstellten (HTML-)Seiten miteinander verbunden werden, müssen Sie noch die jeweils passenden kurbausteininternen Links auslesen und diese bei den Wahloptionen einfügen. 

#### Wo findet man die benötigten Links?

Hierfür nutzen wir die interne Verlinkungsmöglichkeit, die generell für alle OpenOlat Kursbausteine zur Verfügung steht.
Gehen Sie im Kurseditor zur gewünschten Zielseite einer Wahloption. Scrollen Sie im Tab "Titel und Beschreibung" nach unten und wählen Sie -> Link auf diesen Kursbaustein setzen. -> Kursinterner Link (JavaScript). 

Der Link könnte z.B. so ähnlich aussehen: 
"javascript:parent.gotonode(111293110549156)"
Kopieren Sie den bei Ihnen angezeigten Link. 

!!! info „Tipp“

    Dieses Vorgehen funktioniert nicht nur für Branching-Szenarien sondern generell für Baustein-Verlinkungen innerhalb eines Kurses und bietet viel Potenzial! 

### Schritt 6: Verlinkungen setzen

Navigieren Sie nun zu der HTML-Seite auf der die zuvor aufgerufene Seite als Wahl-Option hinterlegt ist. Gehen Sie wieder in den HTML-Editor (Siehe Schritt 3). Markieren Sie die entsprechende Wahloption, wählen Sie „Einfügen“ -> Link bzw. nutzen direkt das entsprechend Symbol im HTML-Editor. 

Beispiel: Sie haben den JavaScript Link für Option 1 der Startseite ausgewählt, dann rufen Sie anschliessend die Startseite auf, gehen in den HTML-Editor und fügen die Verlinkung für Wahloption 1 ein. 

Gehen Sie in gleicher Weise für die anderen Wahloptionen bzw. Zielseiten vor.

!!! info „Tipp“

    Sie können auch im Kurseditor nacheinander alle internen Links für eine Wahlseite kopieren und erst dann in den HTML-Seite Editor des Wahlknotens wechseln. Das geht meist schneller.

### Schritt 7: Testen und optimieren

Um ein gutes, stimmiges Branching-Scenario zu kreieren sollten Sie die einzelnen Wege und Möglichkeiten auch gut testen. Funktioniert alles? Ist der Aktionsfluss passend? Gibt es vielleicht Unstimmigkeiten, Unlogiken oder Fehler bei den Links? Wechseln Sie in die Teilnehmenden Rolle und folgen Sie unterschiedlichen Wegen. Korrigieren und optimieren Sie Dinge.

Gestalten Sie nun Ihre Szenarien auch noch etwas plastischer aus. Ergänzen Sie für jede HTML-Seite z.B. eine passende Visualisierung. 

!!! info „Tipp“

    Experimentieren Sie auch mit Videos. Im einfachsten Fall könnten OpenOlat interne Webcam Aufnahmen verwenden. Besonders spannend für die Lehre ist auch die Kombination mit weiteren Aktionselementen. Hierfür stellt OpenOlat ja bereits eine Menge Potenzial bereit. 

### Schritt 8: Finalisieren

Bevor Sie Ihr Branched-Scenario Ihren Lernenden zugänglich machen können, müssen Sie den Kurs noch publizieren, den Zugang einrichten und ein paar Dinge ausblenden. Schließlich sollen sich die Lernenden ja eben nicht durch die linke Navigation arbeiten, sondern wirklich den vorbereiteten Wegen folgen.

#### Kurs Navigation (und Toolbar) ausblenden

Gehen Sie in die Kursadministration und wählen Sie die Einstellungen.
* im Tab „Layout“ kann nun die Navigation ausgeblendet werden. 
Kurs Administration -> Einstellungen -> Tab "Layout" -> Im Bereich Navigation alle Haken entfernen, keine Menü Navigation und keine Krümelnavigation
* im Tab „Toolbar“ kann ferner die Toolbar für Teilnehmende ausgeblendet werden.
Kurs Administration -> Einstellungen -> Tab "Toolbar" -> „Toolbar sichtbar für Teilnehmende“ Haken entfernen

!!! warning „Wichtig“

    Machen Sie diesen Schritt wirklich erst zum Schluss.

[Zum Seitenanfang ^](#branching)

---
## Generelle Tipps
* Nutzen Sie den Kursbaustein Test um  "Geheimcodes" abzufragen die im Verlauf gesammelt werden konnten. Vielleicht brauchen die User ja den Code um zur finalen Seite zu gelangen. 
* Nutzen Sie QR-Codes und hinterlegen Sie dort wichtige Informationen oder zusätzliche Infos, Rätsel oder Belohnungen. Das macht es spannender.
* KI kann generell sehr bei bei der Entwicklung von branched scenarios unterstützen, z.B. um eine zum Ziel passende Handlung, Wahlmöglichkeiten und sogar eine sinnvolle Verzweigungsstruktur für Ihr Vorhaben zu entwickeln und auch um passende Grafiken zu erstellen. 
* Wer sich schwer tut die Struktur mit OpenOlat aufzubauen kann für die Strukturentwicklung auch zunächst spezifische Tools wie Twine verwenden und anschliessend die Struktur in OpenOlat übertragen. 
* Wenn Sie mit dem Kursbaustein „Seite“ arbeiten: Nutzen Sie doch für die Wahloptionen die „Hinweis-Box“ Typ, Benutzerdefiniert. So können die Wahlmöglichkeiten durchgehend einheitlich hervorgehoben werden. 

[Zum Seitenanfang ^](#branching)

## Weiterführende Informationen und Links zu passenden Handbuch-Seiten   {: #further_information}


[Beispiel: Wähle gut](https://olat.vcrp.de/url/RepositoryEntry/4575461519?guest=true&lang=de) <br>

* Kursbaustein HTML-Seite
* Kursbaustein Seite
* Administration -> Einstellungen
* Kurseditor
* Video Nutzung
* Quiz
