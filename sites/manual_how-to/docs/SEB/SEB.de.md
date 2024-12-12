# Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor? {: #SEB}


??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie haben bereits einen Kurs mit einem Test-Kursbaustein erstellt und wollen nun die Prüfung mit dem Safe Exam Browser durchführen.<br>
    Die folgende Anleitung zeigt Ihnen, wie Sie dabei den SEB verwenden.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [ ] Anfänger:innen [x] Fortgeschrittene  [x] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    * ["Wie gehe ich vor, wenn ich einen Test erstelle?"](../test_creation_procedure/test_creation_procedure.de.md)


---


## Der SEB - Was ist das? {: #SEB_description}

Statt eine Online-Prüfung mit Browsern wie Edge, Firefox, Safari oder Chrome durchzuführen, kann zum Aufruf der OpenOlat-Online-Prüfung der [Safe Exam Browser](http://www.safeexambrowser.org) zur Pflicht gemacht werden. Dieser spezielle Browser ermöglicht es, dass während des Prüfungszeitraums die Möglichkeit andere Websites aufzurufen oder Funktionen wie Copy&Paste deaktiviert sind (Kioskmodus). Dadurch wird die Verwendung unerlaubter Quellen während einer Prüfung unterbunden. 

In einem Kurs unter **Administration > Prüfungsverwaltung** kann ein [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md) konfiguriert werden, der Bedingungen (Zeitfenster usw.) einer Prüfung festlegt. Im Rahmen eines [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md) kann auch bestimmt werden, ob der SEB verwendet werden soll. Wird diese Option aktiviert, kann direkt dort in OpenOlat eine Konfiguration des SEB vorgenommen und eine Konfigurationsdatei zum Versand an die Teilnehmer:innen erzeugt werden. 

!!! info "Der SEB ist ein externes Tool"

    Der Safe Exam Browser wird nicht von der frentix GmbH entwickelt, deshalb können wir weder Garantien übernehmen noch direkt Einfluss auf die Funktionalität nehmen. Auch unser Support beschränkt sich auf die OpenOlat-seitigen Konfigurationsmöglichkeiten zum Aufruf dieses externen Tools.


[zum Seitenanfang ^](#SEB)

---

## Wie richte ich als OpenOlat Autor:in eine Prüfung mit dem SEB ein? {: #SEB_setup}


### Schritt 1: SEB installieren {: #SEB_installation} 

Die Installationsdatei finden Sie auf der [Web Site des Herstellers](http://www.safeexambrowser.org/download_de.html).

Fordern Sie auch alle Prüfungsteilnehmer:innen auf, den SEB auf ihrem Rechner zu installieren. Bzw. wenn für die Prüfung gesonderte Rechner zur Verfügung gestellt werden, bereiten Sie diese Rechner alle entsprechend vor.

[zum Seitenanfang ^](#SEB)

---


### Schritt 2: Prüfungsmodus erstellen {: #create_assessment_mode}

Als Autor:in des OpenOlat-Prüfungskurses erstellen Sie einen Prüfungsmodus unter<br> 
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus" > Button "Prüfungsmodus hinzufügen"**

![SEB_new_assessment_mode_v1_de.png](assets/SEB_new_assessment_mode_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#SEB)

---


### Schritt 3: SEB aktivieren {: #activate_SEB}

In einem Prüfungsmodus ist die Verwendung des SEB optional. Wird es gewünscht, aktivieren Sie diese Option unter<br>

**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus" > Modus auswählen/bearbeiten > Tab "Safe Exam Browser"**

![SEB_activate_v1_de.png](assets/SEB_activate_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#SEB)


---


### Schritt 4: Konfigurieren {: #SEB_configuration}
Sobald der SEB aktiviert wurde, werden die Konfigurationsoptionen angezeigt. Nachstehend sind die Optionen und Ihre Auswirkungen auf die Teilnehmersicht kurz beschrieben.

Bei Konfiguration in OpenOlat gilt:<br>
Die vorgeschlagenen Einstellungen können in der OpenOlat-Systemadministration so gesetzt werden. Sie können also als Empfehlung Ihres/Ihrer Administrator:in zum Übernehmen betrachtet werden.

![SEB_config_v1_de.png](assets/SEB_config_v1_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Typ von Anwendung**<br>
Wir empfehlen die Konfiguration hier auf dieser Seite in OpenOlat. Prinzipiell ist es aber auch möglich, die Konfigurationsdatei des SEB zu verwenden. Diese kann bei Bedarf mit einem Texteditor angepasst werden. Bei Verwendung der mitgelieferten Konfiguration, müssen in OpenOlat die Safe Exam Browser Keys eingetragen werden. (Mehr dazu auf der [Web Site des Herstellers](http://www.safeexambrowser.org).) Bis auf den Hinweistext erübrigen sich in diesem Fall die nachfolgend aufgelisteten Konfigurationsptionen. 


![2_green_24.png](assets/2_green_24.png) **Herunterladbare Konfigurationsdatei**<br>
Wird hier "Ja" gewählt, kann die Konfigurationsdatei durch die Prüfungsteilnehmer:innen bei gestartetem Prüfungsmodus aus OpenOlat heruntergeladen werden. Auch Autor:innen können die Datei jederzeit herunterladen und an die Prüfungsteilnehmer:innen verschicken. Siehe [Schritt 6](#download_SEB_configfile).

Wird hier "Nein" gewählt, besteht die Downloadmöglichkeit für Teilnehmer:innen nicht mehr, für Autor:innen jedoch weiterhin, wie in [Schritt 6](#download_SEB_configfile) beschrieben.

![3_green_24.png](assets/3_green_24.png) **Beenden von SEB erlauben**<br>
Manche Prüfungsteilnehmer:innen sind teilweise früher fertig und können dann bis zum eingestellten Ende des Prüfungsmodus nicht auf OpenOlat oder ander Websites zugreifen.
Besteht keine Gefahr von Missbrauch (gegenseitiger Hilfe), kann den Prüfungsteilnehmer:innen das Beenden des SEB erlaubt werden, sobald sie ihre Prüfung abgegeben haben. In diesem Fall wird ein Quit-Button rechts unten auf dem Bildschirm angezeigt.

![4_green_24.png](assets/4_green_24.png) **Beenden/Entsperren-Kennwort**<br>
Dieses Eingabefeld wird als Konfigurationsmöglichkeit nur angezeigt, wenn das Beenden des SEB erlaubt wurde.
Klicken Prüfungsteilnehmer:innen den Quit-Button zum Beenden der Einschränkungen des SEB, werden sie zur Eingabe dieses Passworts aufgefordert. 

Bei einer Prüfung in einem gemeinsamen Prüfungsraum kann dieses Passwort zum Beispiel die Prüfungsaufsicht jeweils denjenigen Personen bekannt geben, die den Prüfungsraum verlassen.

![5_green_24.png](assets/5_green_24.png) **Link um SEB nach der Prüfung zu verlassen**<br>
Wenn kein Quit-Button angezeigt werden soll, kann dieser Link innerhalb der Prüfung an geeigneter Stelle angegeben werden. Mit ihm können die Prüfungsteilnehmer:innen dann den Safe Exam Browser verlassen.

![6_green_24.png](assets/6_green_24.png) **Benutzer:in muss das Beenden bestätigen**<br>
Ist diese Option aktiviert, müssen alle Prüfungsteilnehmer:innen das Beenden der Prüfung nochmals bestätigen. Dies ist als Sicherheitsmassnahme vorgesehen, damit eine Prüfung nicht versehentlich beendet wird.

![7_green_24.png](assets/7_green_24.png) **Neuladen in Prüfung zulassen**<br>
Wird das erneute Laden der Website (Prüfungsseite) während der laufenden Prüfung zugelassen, erscheint bei den Prüfungsteilnehmer:innen rechts unten auf dem Bildschirm ein Button zum Neuladen. 

![8_green_24.png](assets/8_green_24.png) **Browser-Ansichtsmodus**<br>
Wählen Sie einen der angegebenen Modi. Wenn keine weiteren Websites freigegeben wurden, empfiehlt sich der Vollbildmodus. Sollen die Prüfungsteilnehmer:innen auf bestimmte freigegebene Seiten zugreifen, kann die Verwendung von Browserfenstern sinnvoll sein. 

![9_green_24.png](assets/9_green_24.png) **SEB-Taskleiste anzeigen**<br>
Diese Option hat Einfluss auf einige andere Optionen. Wenn die Taskleiste nicht angezeigt wird, fehlen auch die Anzeigen für den Beenden-Button, Audio-Steuerung, Uhrzeit, Tastaturbelegung und WLAN-Auswahl.

![10_green_24.png](assets/10_green_24.png) **Neuladen-Taste anzeigen**<br>
Ist das erneute Laden erlaubt, wird links oben eine Button zum Neuladen angezeigt. Bei "Nein" ist er ausgegraut und kann nicht verwendet werden.

![11_green_24.png](assets/11_green_24.png) **Uhrzeit anzeigen**<br>
Ein hilfreiches Feature für die Prüfungsteilnehmer:innen, um die verbleibende Restzeit im Blick zu behalten. 

![12_green_24.png](assets/12_green_24.png) **Auswahl Tastaturbelegung anzeigen**<br>
Es wird eine Auswahl für Tastaturbelegungen zum Sprachenwechsel angezeigt. 

![13_green_24.png](assets/13_green_24.png) **WLAN-Auswahl anzeigen**<br>
Die Auswahl erreichbarer WLAN-Netze wird rechts unten in der Taskleiste angezeigt, wenn die Option auf "Ja" gesetzt ist.

![14_green_24.png](assets/14_green_24.png) **Audio-Steuerung anzeigen**<br>
Die Audiosteuerung kann rechts unten in der Taskleiste angezeigt werden. Diese Option wird für Prüfungen mit Video oder Audio benötigt.

![15_green_24.png](assets/15_green_24.png) **Stummschaltung beim Start**<br>
Mit deaktivierter Audio-Steuerung verhindert diese Option das Verwenden von Audio Devices.

![16_green_24.png](assets/16_green_24.png) **Audioaufnahme zulassen (Mikrofon, Win)**<br>
Es empfiehlt sich, diese Option nur zu aktivieren, wenn ausdrücklich Audioaufnahmen während der Prüfung erwünscht sind.

![17_green_24.png](assets/17_green_24.png) **Videoaufnahmen zulassen (Webcam, Win)**<br>
Es empfiehlt sich, diese Option nur zu aktivieren, wenn ausdrücklich Videoaufnahmen während der Prüfung erwünscht sind.

![18_green_24.png](assets/18_green_24.png) **Rechtschreibprüfung zulassen**<br>
Je nach Prüfungsgegenstand kann die Rechtschreibprüfung (derzeit nur Englisch) deaktiviert oder verfügbar gemacht werden. Wenn die Option auf "Ja" gesetzt ist, werden falsch geschriebene Wörter rot unterstrichen.

![19_green_24.png](assets/19_green_24.png) **Zoom in/out erlauben**<br>
Gründe für eine Unterdrückung des Zoom könnten z.B. sein, dass die Prüfungsteilnehmer:innen auf Bildmaterial durch Zoom unerwünscht Schrift lesen könnten. In der Regel sollte jedoch Zoom erlaubt sein, um (insbesondere bei BYOD - Bring your own device) eine gute Lesbarkeit zu gewährleisten. Gezoomt werden kann mit Strg + und Strg -, sowie im Menü oben rechts.

![20_green_24.png](assets/20_green_24.png) **URL-Filter aktivieren**<br>
Ist der Filter aktiviert, werden alle Webseiten bis auf die Prüfung blockiert. Mit der aktivierung werden weitere Optionen zur Konfiguration angezeigt. Dort können Sie genauer steuern, welche URLs während der Prüfung ausserdem noch aufgerufen werden dürfen.

![SEB_config_url_filter_v1_de.png](assets/SEB_config_url_filter_v1_de.png){ class="shadow lightbox" }

**Eingebetteten Inhalt ebenfalls filtern**<br>
Wird diese Option gewählt, wird auch im Inhalt einer Seite geprüft, ob erlaubte/nicht erlaubte Ausdrücke enthalten sind und entsprechend ein Zugriff freigegeben oder blockiert.

**Erlaubte Ausdrücke**<br>
Die in dieser Positivliste angegebenen Ausdrücke dürfen von den Prüfungsteilnehmer:innen während aktivem Prüfungsmodus gesucht werden.

**Erlaubte Regex**<br>
Regex sind "Regular Expressions" (= Platzhalter). Es kann in dieser Positivliste angegeben werden, welche Ausdrücke mit Platzhaltern von den Prüfungsteilnehmer:innen während aktivem Prüfungsmodus gesucht werden dürfen.

**Blockierte Ausdrücke**<br>
Hier angegebene Ausdrücke blockieren den Zugriff auf URLs und Dateinamen auf dem eigenen Rechner, die diese Ausdrücke enthalten.
Wenn die Option "Eingebetteten Inhalt ebenfalls filtern" gewählt ist, auch wenn sie in deren Inhalten gefunden werden. 

**Blockierte Regex**<br>
URLs mit den hier angegebene Regex-Ausdrücken (Ausdrücken mit Platzhaltern) werden blockiert. Wird der eingebettete Inhalt ebenfalls gefiltert, werden auch solche Seiten blockiert.


![21_green_24.png](assets/21_green_24.png) **Konfigurationsschlüssel der gespeicherten Konfiguration**<br>
Wird die Konfigurationsdatei in OpenOlat erstellt, muss dieser Schlüssel nicht separat eingetragen werden. Lediglich wenn Sie eine Konfigurationsdatei selbst bearbeiten, wird er benötigt.

**Hinweis:** Bei jeder Änderung an der Konfigurationsdatei ändert sich der generierte Schlüssel.
Sie sollten also nur den Schlüssel kopieren und verwenden, nachdem Sie alle Einstellungen vorgenommen haben.


![22_green_24.png](assets/22_green_24.png) **Safe Exam Browser Hinweis**<br>
Der hier eingegebene Hinweistext erscheint, sobald die Prüfungsteilnehmer:innen mit den SEB starten. Sie können hier z.B. nochmals auf die Prüfungsbedingungen und die Einschränkungen durch den SEB hinweisen.



[zum Seitenanfang ^](#SEB)

---


### Schritt 5: Konfigurationsdatei erstellen {: #create_SEB_configfile}

Wählen Sie im Tab "Safe Exam Browser" die Option<br> **"Herunterladbare Konfigurationsdatei: Ja"**.<br>
Vergessen Sie nicht die Konfiguration zu speichern!

![SEB_configfile_create_v1_de.png](assets/SEB_configfile_create_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#SEB)

---


### Schritt 6: Konfigurationsdatei herunterladen {: #download_SEB_configfile}

Ist die Konfiguration abgeschlossen (Schritt 5), kehren Sie zum Exportieren der Konfigurationsdatei zurück zur vorherigen Ebene **"Prüfungsverwaltung"**, in der alle Prüfungsmodi aufgelistet sind.

Klicken Sie dort beim betreffenden Prüfungsmodus auf<br>
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus" > Icon "Herunterladen"**

![SEB_configfile_download_v1_de.png](assets/SEB_configfile_download_v1_de.png){ class="shadow lightbox" }

Beispiel: SEBClientSettings.seb


[zum Seitenanfang ^](#SEB)

---


### Schritt 7: Konfigurationsdatei verschicken {: #distribute_SEB_configfile}

Damit die Prüfungsteilnehmer einen Test im SEB starten können, müssen Sie eine Konfigurationsdatei auf ihrem Rechner ausführen. (Beispiel: SEBClientSettings.seb) Die Datei kann den Prüfungsteilnehmern z.B. per Mail zugeschickt werden oder über eine Seite zum Download angeboten werden.

!!! tip "Hinweis zum Download"

    Speichern Sie die SEB-Konfigurationsdatei auf einer Seite, die nicht durch den Safe Exam Browser beschränkt wird, um auch während aktiviertem Prüfungsmodus jederzeit Zugriff zu ermöglichen. (Angabe einer erlaubten Download-Seite in der Konfiguration.)

!!! tip "Hinweis zu anderweitigem Prüfungsbetrug"

    Bedenken Sie: Der Safe Exam Browser schränkt nur die Nutzung des aktuellen Gerätes ein. Es kann jedoch auch Prüfungsbetrug durch Nutzung eines Smartphones, unerlaubte Unterlagen oder Austausch mit anderen Personen erfolgen.

[zum Seitenanfang ^](#SEB)

---


## Starten der Prüfung durch Betreuer:innen

Der Start und die Dauer der Prüfung wird durch die Angabe in der Konfiguration des [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md) bestimmt. Wird ein manueller Start durch Betreuer:innen gewünscht, kann der Prüfungsmodus unter 
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"** 
durch Klicken auf den **Starten-Button** begonnen werden. 

![SEB_start_assessment_mode_v1_de.png](assets/SEB_start_assessment_mode_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#SEB)

---


## Wie starten Teilnehmer:innen eine OpenOlat-Prüfung mit dem SEB? {: #SEB_participants}


**Schritt 1: Installation des SEB**<br>
Der Safe Exam Browser muss im Voraus auf dem Gerät installiert werden. 
Die Installationsdatei finden Sie auf der [Website des Herstellers](http://www.safeexambrowser.org/download_de.html).

Um Schwierigkeiten zu erkennen, ist eine von den Betreuer:innen vorab organisierte Probeprüfung empfehlenswert. So kann vorab sicher gestellt werden, dass auf allen Rechnern der SEB installiert ist.


**Schritt 2: Erhalt der Konfigurationsdatei**<br>
Alle Prüfungsteilnehmer:innen müssen von den Betreuer:innen die Konfigurationsdatei erhalten (z.B. per Mail oder als Download).


**Schritt 3: Prüfungsstart durch Aufruf der Konfigurationsdatei**<br>
Durch Öffnen dieser Konfigurationsdatei starten Prüfungsteilnehmer:innen die Prüfung. Sobald die Konfigurationsdatei doppelt geklickt wird, öffnet sich der SEB und die übrigen Funktionen des Rechners werden eingeschränkt. 

!!! tip "Hinweis"

    Haben Sie Prüfungsteilnehmer:innen, die den SEB nicht installieren wollen, können Sie als Prüfungsleitung evtl. spezielle Prüfungscomputer verleihen. Um sicher zu gehen, weisen Sie darauf hin, dass sich die Prüfungsteilnehmer:innen proaktiv bei den Lehrenden melden sollten.


!!! tip "Bring your own device (BYOD)"

    Der SEB ermöglicht sichere Prüfungen auch auf privaten Rechnern der Prüfungsteilnehmer:innen. Voraussetzung ist, dass der Safe Exam Browser im Voraus auf dem Gerät installiert worden ist. Dann kann mit der verschickten Konfgurationsdatei der SEB auf verschiedenen BYOD-Geräten aufgerufen werden.


[zum Seitenanfang ^](#SEB)

---


## Wie kann ich als Betreuer:in eingreifen, während eine Prüfung mit dem SEB läuft? {: #SEB_intervention}

Grundsätzlich sollte bei laufendem Prüfungsmodus möglichst nicht mehr eingegriffen werden. Ist es aus zwingenden Gründen aber erforderlich, erfolgt der Eingriff über den [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md).

!!! tip "Hinweis"

    Zur Kommunikation zwischen Betreuer:innen und Prüfungsteilnehmer:innen steht in OpenOlat ein spezieller Prüfungs-Chat zur Verfügung.

    Mehr zur Kommunikation während einer Prüfung erfahren Sie [hier.](../communication_during_exam/communication_during_exam.de.md)


[zum Seitenanfang ^](#SEB)

---


## Wie wird eine Prüfung mit dem SEB beendet? {: #SEB_exit}

Eine Online-Prüfung in OpenOlat kann <br>
a\) automatisch oder<br>
b) manuell<br>
beendet werden.

Wird die Prüfung **manuell** beendet, kann<br>
\- ein Betreuer/eine Betreuerin den SEB für alle Prüfungsteilnehmer:innen gleichzeitig stoppen.<br>
oder
\- jeder/jede Prüfungsteilnehmer:in den SEB mit einem individuellen Exit-Link selbst stoppen.

### Prüfung automatisch beenden

Der SEB wird im Rahmen eines **Prüfungsmodus** in OpenOlat verwendet. Wird der Prüfungsmodus beendet, wird auch der SEB beendet.
Das automatische Beenden eines Prüfungsmodus wird konfiguriert unter<br> 
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"**

### Prüfung manuell beenden (Prüfung gleichzeitig für alle Beenden, durch Betreuer:innen)

Es gilt auch hier: Wird der **Prüfungsmodus** durch den/die Betreuer:in beendet, wird auch der SEB beendet. Das manuelle Beenden eines laufenden Prüfungsmodus erfolgt durch Betreuer:innen unter<br>
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"**<br> 
Sobald ein Prüfungsmodus aktiviert wurde, wird ein Button "Beenden" bzw "Prüfung beenden" angezeigt. Klicken Sie einen der beiden Buttons. Anschliessend wechselt der Status des Prüfungsmodus auf "Beendet".

![SEB_quit_exam_mode_v1_de.png](assets/SEB_quit_exam_mode_v1_de.png){ class="shadow lightbox" }


### Individuelles Beenden per Exit-Link

Wurde es entsprechend konfiguriert (siehe [Schritt 4](#SEB_configuration)), wird in der rechten unteren Ecke des SEB ein Quit-Button angezeigt. Klicken Prüfungsteilnehmer:innen auf diesem Link, werden Sie aufgefordert, das Passwort zum Verlassen einzugeben. Teilnehmer:innen können den Browser nur beenden, wenn Sie dieses Passwort haben. Als Betreuer:in können Sie das Passwort zum gegebenen Zeitpunkt verkünden. (Z.B. wenn Prüfungsteilnehmer:innen das Prüfungszimmer verlassen möchten.)


[zum Seitenanfang ^](#SEB)

---


## SEB während der Einsichtnahme in die Prüfungsergebnisse {: #SEB_exam_inspection}

Durch Verwendung des SEB können alle anderen Aktivitäten auf dem Computer auch während der Einsichtnahme in die Prüfungsergebnisse gesperrt werden.

[zu den Details > ](../../manual_user/learningresources/Assessment_inspection.de.md)<br>
[zum Seitenanfang ^](#SEB)


---


## Checkliste {: #SEB_checklist}

- [x] Prüfungsteilnehmer:innen informiert, dass Verwendung des SEB Pflicht ist?
- [x] Download und Installation des Safe Exam Browsers auf allen Geräten der Teilnehmer:innen?
- [x] Kommunikation während der Prüfung vorher geklärt? (z.B. Verwendung des Prüfungs-Chats)
- [x] Ggf. Mitteilung des Passworts für Exit geregelt? (z.B. individuelle Bekanntgabe kurz vor Verlassen des Prüfungsraums)
- [x] Verfahren zum Beenden der Prüfung vorab geklärt?
- [x] Probeklausur durchgeführt? Mit allen Prüfungsteilnehmer:innen?
- [x] Prüfungsmodus konfiguriert?
- [x] SEB im Prüfungsmodus aktiviert?
- [x] SEB-Konfigurationsdatei erstellt?
- [x] SEB-Konfigurationsdatei verschickt?
- [x] Instruktion zum Beenden der Prüfung gegeben? 

[zum Seitenanfang ^](#SEB)

---


## Weiterführende Informationen

[Website des Herstellers >](http://www.safeexambrowser.org)<br>
[Prüfungsmodus >](../../manual_user/learningresources/Assessment_mode.de.md)<br>
[Prüfungseinsicht > ](../../manual_user/learningresources/Assessment_inspection.de.md)<br>




