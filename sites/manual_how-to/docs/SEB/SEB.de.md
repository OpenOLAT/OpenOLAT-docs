# Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor? {: #SEB}



!!! warning "Achtung"

    Dieser Artikel ist noch in Bearbeitung.



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

Statt eine Online-Prüfung mit Browsern wie Edge, Firefox, Safari oder Chrome durchzuführen, kann zum Aufruf der OpenOlat-Online-Prüfung der Safe Exam Browser zur Pflicht gemacht werden. Dieser spezielle Browser ermöglicht es, dass während des Prüfungszeitraums die Möglichkeit andere Websites aufzurufen oder Funktionen wie Copy&Paste deaktiviert sind (Kioskmodus). Dadurch wird die Verwendung unerlaubter Quellen während einer Prüfung unterbunden. 

Unter **Administration > Prüfungsverwaltung** kann ein [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md) konfiguriert werden, der Bedingungen (Zeitfenster usw.) einer Prüfung festlegt. Im Rahmen eines [Prüfungsmodus](../../manual_user/learningresources/Assessment_mode.de.md) kann auch bestimmt werden, ob der SEB verwendet werden soll. Wird diese Option aktiviert, kann direkt dort in OpenOlat eine Konfiguration des SEB vorgenommen und eine Konfigurationsdatei zum Versand an die Teilnehmer:innen erzeugt werden. 

!!! info "Der SEB ist ein Externes Tool"

    Der Safe Exam Browser wird nicht von Frentix entwickelt, deshalb können wir weder Garantien übernehmen noch direkt Einfluss auf die Funktionalität nehmen. Auch unser Support beschränkt sich auf die OpenOlat-seitigen Konfigurationsmöglichkeiten zum Aufruf dieses externen Tools.


[Zum Seitenanfang ^](#SEB)

---

## Wie richte ich als OpenOlat Autor:in eine Prüfung mit dem SEB ein? {: #SEB_setup}


### Schritt 1: SEB installieren {: #SEB_installation} 

Die Installationsdatei finden Sie auf der [Web Site des Herstellers](http://www.safeexambrowser.org/download_de.html).

Fordern Sie auch alle Prüfungsteilnehmer:innen auf, den SEB auf ihrem Rechner zu installieren. Bzw. wenn für die Prüfung gesonderte Rechner zur Verfügung gestellt werden, bereiten Sie diese Rechner alle entsprechend vor.


[Zum Seitenanfang ^](#SEB)

---


### Schritt 2: Prüfungsmodus erstellen {: #create_assessment_mode}

Als Autor:in des OpenOlat-Prüfungskurses erstellen Sie einen Prüfungsmodus unter<br> 
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus" > Button "Prüfungsmodus hinzufügen"**

![SEB_new_assessment_mode_v1_de.png](assets/SEB_new_assessment_mode_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#SEB)

---


### Schritt 3: SEB aktivieren {: #activate_SEB}

In einem Prüfungsmodus ist die Verwendung des SEB optional. Wird es gewünscht, aktivieren Sie diese Option unter<br>

**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus" > Modus auswählen/bearbeiten > Tab "Safe Exam Browser"**

![SEB_activate_v1_de.png](assets/SEB_activate_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#SEB)


---


### Schritt 4: Konfigurieren {: #SEB_configuration}
Sobald der SEB aktiviert wurde, werden die Konfigurationsoptionen angezeigt. Nachstehend sind die Optionen und Ihre Auswirkungen auf die Teilnehmersicht kurz beschrieben.

Bei Konfiguration in OpenOlat gilt:<br>
Die vorgeschlagenen Einstellungen können in der OpenOlat-Systemadministration so gesetzt werden. Sie können also als Empfehlung Ihres/Ihrer Administrator:in zum Übernehmen betrachtet werden.

![SEB_config_v1_de.png](assets/SEB_config_v1_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Typ von Anwendung**<br>
Wir empfehlen die Konfiguration hier auf dieser Seite in OpenOlat. Prinzipiell ist es aber auch möglich, die Konfigurationsdatei des SEB zu verwenden. Diese kann bei Bedarf mit einem Texteditor angepasst werden.


![2_green_24.png](assets/2_green_24.png) **Herunterladbare Konfigurationsdatei**<br>
Wird hier "Ja" gewählt, kann die Konfigurationsdatei aus OpenOlat heruntergeladen und an die Prüfungsteilnehmer:innen verschickt werden. Siehe [Schritt 6](#download_SEB_configfile).

Wird hier "Nein" gewählt, besteht die Downloadmöglichkeit wie in [Schritt 6](#download_SEB_configfile) beschrieben weiterhin. In diesem Fall ist aber ...???

![3_green_24.png](assets/3_green_24.png) **Beenden von SEB erlauben**<br>
Manche Prüfungsteilnehmer:innen sind teilweise früher fertig und können dann bis zum eingestellten Ende des Prüfungsmodus nicht auf OpenOlat oder ander Websites zugreifen.
Besteht keine Gefahr von Missbrauch (gegenseitiger Hilfe), kann den Prüfungsteilnehmer:innen das Beenden des SEB erlaubt werden, sobald sie ihre Prüfung abgegeben haben. In diesem Fall wird ein Quit-Button rechts unten auf dem Bildschirm angezeigt.

![4_green_24.png](assets/4_green_24.png) **Beenden/Entsperren-Kennwort**<br>
Dieses Eingabefeld wird als Konfigurationsmöglichkeit nur angezeigt, wenn das Beenden des SEB erlaubt wurde.
Klicken Prüfungsteilnehmer:innen den Quit-Button zum Beenden der Einschränkungen des SEB, werden sie zur Eingabe dieses Passworts aufgefordert. 

Bei einer Prüfung in einem gemeinsamen Prüfunsraum kann dieses Passwort zum Beispiel durch die Prüfungsaufsicht jeweils denjenigen Personen bekannt geben, die den Prüfungsraum verlassen.

![5_green_24.png](assets/5_green_24.png) **Link um SEB nach der Prüfung zu verlassen**<br>
Als

![6_green_24.png](assets/6_green_24.png) **Benutzer:in muss das Beenden bestätigen**<br>
Ist diese Option aktiviert, müssen alle Prüfungsteilnehmer:innen das Beenden der Prüfung nochmals bestätigen. Dies ist als Sicherheitsmassnahme vorgesehen, damit eine Prüfung nicht versehentlich beendet wird.

![7_green_24.png](assets/7_green_24.png) **Neuladen in Prüfung zulassen**<br>
Wird das erneute Laden der Website (Prüfungsseite) während der laufenden Prüfung zugelassen, erscheint bei den Prüfungsteilnehmer:innen rechts unten auf dem Bildschirm ein Button zum Neuladen. Wird er geklickt, ... 

![8_green_24.png](assets/8_green_24.png) **Browser-Ansichtsmodus**<br>
Wählen Sie einen der angegebenen Modi. Wenn keine weiteren Websites freigegeben wurden, empfiehlt sich der Vollbildmodus. Sollen die Prüfungsteilnehmer:innen auf bestimmte freigegebene Seiten zugreifen, kann die Verwendung von Browserfenstern sinnvoll sein. 

![9_green_24.png](assets/9_green_24.png) **SEB-Taskleiste anzeigen**<br>
Als

![10_green_24.png](assets/10_green_24.png) **Neuladen-Texte anzeigen**<br>
Als

![11_green_24.png](assets/11_green_24.png) **Uhrzeit anzeigen**<br>
Als

![12_green_24.png](assets/12_green_24.png) **Auswahl Tastaturbelegung anzeigen**<br>
Als

![13_green_24.png](assets/13_green_24.png) **WLAN-Auswahl anzeigen**<br>
Als

![14_green_24.png](assets/14_green_24.png) **Audio-Steuerung anzeigen**<br>
Als

![15_green_24.png](assets/15_green_24.png) **Stummschaltung beim Start**<br>
Als

![16_green_24.png](assets/16_green_24.png) **Audioaufnahme zulassen (Mikrofon, Win)**<br>
Als

![17_green_24.png](assets/17_green_24.png) **Videoaufnahmen zulassen (Webcam, Win)**<br>
Als

![18_green_24.png](assets/18_green_24.png) **Rechtschreibprüfung zulassen**<br>
Je nach Prüfungsgegenstand (z.B. Sprachen) kann die Rechtschreibprüfung deaktiviert oder verfügbar gemacht werden.

![19_green_24.png](assets/19_green_24.png) **Zoom in/out erlauben**<br>
Als

![20_green_24.png](assets/20_green_24.png) **URL-Filter aktivieren**<br>
Als
Bei 

![21_green_24.png](assets/21_green_24.png) **Konfigurationsschlüssel der gespeicherten Konfiguration**<br>
Als

**Hinweis:** Bei jeder Änderung an der Konfigurationsdatei ändert sich der generierte Schlüssel.
Sie sollten also nur den Schlüssel kopieren und verwenden, nachdem Sie alle Einstellungen vorgenommen haben.


![22_green_24.png](assets/22_green_24.png) **Safe Exam Browser Hinweis**<br>
Der hier eingegebene Hinweistext erscheint, sobald ...



[Zum Seitenanfang ^](#SEB)

---


### Schritt 5: Konfigurationsdatei erstellen {: #create_SEB_configfile}

Wählen Sie im Tab "Safe Exam Browser" die Option<br> **"Herunterladbare Konfigurationsdatei: Ja"**.<br>
Vergessen Sie nicht die Konfiguration zu speichern!

![SEB_configfile_create_v1_de.png](assets/SEB_configfile_create_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#SEB)

---


### Schritt 6: Konfigurationsdatei herunterladen {: #download_SEB_configfile}

Ist die Konfiguration abgeschlossen (Schritt 5), kehren Sie zum Exportieren der Konfigurationsdatei zurück zur vorherigen Ebene **"Prüfungsverwaltung"**, in der alle Prüfungsmodi aufgelistet sind.

Klicken Sie dort beim betreffenden Prüfungsmodus auf<br>
**Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus" > Icon "Herunterladen"**

![SEB_configfile_download_v1_de.png](assets/SEB_configfile_download_v1_de.png){ class="shadow lightbox" }

Beispiel: SEBClientSettings.seb


[Zum Seitenanfang ^](#SEB)

---


### Schritt 7: Konfigurationsdatei verschicken {: #distribute_SEB_configfile}

Damit die Prüfungsteilnehmer einen Test im SEB starten können, müssen Sie eine Konfigurationsdatei auf ihrem Rechner ausführen. (Beispiel: SEBClientSettings.seb) Die Datei kann den Prüfungsteilnehmern z.B. per Mail zugeschickt werden oder über eine Seite zum Download angeboten werden.

!!! tip "Hinweis zum Download"

    Speichern Sie die SEB-Konfigurationsdatei auf einer Seite, die nicht durch den Safe Exam Browser beschränkt wird, um auch während aktiviertem Prüfungsmodus jederzeit Zugriff zu ermöglichen. (Angabe einer erlaubten Download-Seite in der Konfiguration.)

!!! tip "Hinweis zu anderweitigem Prüfungsbetrug"

    Bedenken Sie: Der Safe Exam Browser schränkt nur die Nutzung des aktuellen Gerätes ein. Es kann jedoch auch Prüfungsbetrug durch Nutzung eines Smartphones, unerlaubte Unterlagen oder Austausch mit anderen Personen erfolgen.

[Zum Seitenanfang ^](#SEB)

---


## Wie starten Teilnehmer:innen eine OpenOlat-Prüfung mit dem SEB? {: #SEB_participants}


**Schritt 1: Installation des SEB**<br>
Der Safe Exam Browser muss im Voraus auf dem Gerät installiert werden. 
Die Installationsdatei finden Sie auf der [Web Site des Herstellers](http://www.safeexambrowser.org/download_de.html).

Um Schwierigkeiten zu erkennen, ist eine von den Betreuer:innen vorab organisierte Probeprüfung empfehlenswert.


**Schritt 2: Erhalt der Konfigurationsdatei**<br>
Alle Prüfungsteilnehmer:innen müssen von den Betreuer:innen die Konfigurationsdatei erhalten (z.B. per Mail oder als Download).


**Schritt 3: Prüfungsstart durch Aufruf der Konfigurationsdatei**<br>
Durch Öffnen dieser Konfigurationsdatei starten Prüfungsteilnehmer:innen die Prüfung. Sobald die Konfigurationsdatei doppelt geklickt wird, öffnet sich der SEB und die übrigen Funktionen des Rechners werden eingeschränkt. 

!!! tip "Hinweis"

    Haben Sie Prüfungsteilnehmer:innen, die den SEB nicht installieren wollen, können Sie als Prüfungsleitung evtl. spezielle Prüfungscomputer verleihen. Um sicher zu gehen, weisen Sie darauf hin, dass sich die Prüfungsteilnehmer:innen proaktiv bei den Lehrenden melden sollten.


!!! tip "Bring your own device (BYOD)"

    Der SEB ermöglicht sichere Prüfungen auch auf privaten Rechnern der Prüfungsteilnehmer:innen. Voraussetzung ist, dass der Safe Exam Browser im Voraus auf dem Gerät installiert worden ist. Dann kann mit der verschickten Konfgurationsdatei der SEB auf verschiedenen BYOD-Geräten aufgerufen werden.


[Zum Seitenanfang ^](#SEB)

---


## Wie kann ich als Betreuer:in eingreifen, während eine Prüfung mit dem SEB läuft? {: #SEB_intervention}

Grundsätzlich sollte bei laufendem Prüfungsmodus möglichst nicht mehr eingegriffen werden. Ist es aus zwingenden Gründen aber erforderlich, ..

tbd

!!! tip "Hinweis"

    Zur Kommunikation zwischen Betreuer:innen und Prüfungsteilnehmer:innen steht in OpenOlat ein spezieller Prüfungs-Chat zur Verfügung.

    Mehr zur Kommunikation während einer Prüfung erfahren Sie [hier.](../communication_during_exam/communication_during_exam.de.md)


[Zum Seitenanfang ^](#SEB)

---


## Wie wird eine Prüfung mit dem SEB beendet? {: #SEB_exit}

Eine Online-Prüfung in OpenOlat kann <br>
a) automatisch<br>
b) manuell<br>
beendet werden.

Wird die Prüfung **manuell** beendet, kann

- ein Betreuer/eine Betreuerin den SEB für alle Prüfungsteilnehmer:innen gleichzeitig stoppen<br>
- jeder/jede Prüfungsteilnehmer:in den SEB mit einem individuellen Exit-Link selbst stoppen

### Prüfung automatisch beenden

tbd

### Prüfung manuell beenden

tbd

### Gemeinsames Beenden der Prüfung durch Betreuer:innen

tbd

### Individuelles Beenden per Exit-Link

tbd

"Quit/unlock password". Benutzer können den Browser nur
beenden, wenn Sie dieses Passwort haben. Sie können das Passwort dann zum gegebenen
Zeitpunkt verkünden.


[Zum Seitenanfang ^](#SEB)

---


## SEB während der Einsichtnahme in die Prüfungsergebnisse {: #SEB_exam_inspection}

Durch Verwendung des SEB können alle anderen Aktivitäten auf dem Computer auch während der Einsichtnahme in die Prüfungsergebnisse gesperrt werden.

[Zu den Details > ](../../manual_user/learningresources/Assessment_inspection.de.md)<br>
[Zum Seitenanfang ^](#SEB)


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
- [x] x


## Weiterführende Informationen

[Web Site des Herstellers >](http://www.safeexambrowser.org)<br>
[Prüfungsmodus >](../../manual_user/learningresources/Assessment_mode.de.md)<br>
[Prüfungseinsicht > ](../../manual_user/learningresources/Assessment_inspection.de.md)<br>




