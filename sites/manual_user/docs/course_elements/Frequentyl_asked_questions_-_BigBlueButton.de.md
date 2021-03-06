# Häufig gestellte Fragen - BigBlueButton

!!! note "Open Source Lösung BigBlueButton"

    BigBlueButton ist eine Open Source Lösung für virtuelle Konferenz-, Meeting und Klassenraum-Szenarien. Die offiziellen Dokumentationen und Hilfestellungen finden Sie unter den nachfolgenden Links. Die Zusammenstellung der häufigste gestellten Fragen (FAQ) auf dieser Seite sind nicht abschliessend und beziehen sich auf die Nutzung von BigBlueButton in Kombination mit OpenOlat.
    
    * [Hilfe-Videos von BigBlueButton](https://bigbluebutton.org/html5/){target=_blank}
    * [FAQ BigBlueButton](https://docs.bigbluebutton.org/support/faq.html){target=_blank}
    * [Weitere FAQ BigBlueButton](https://support.blindsidenetworks.com/hc/en-us/categories/360000379651-BigBlueButton-HTML5){target=_blank}


## :material-devices: Geräte, Internet Browser & Fehlermeldungen

**Welche Browser werden von BigBlueButton unterstützt?**

BigBlueButton ist eine browser-basierte Software und kann ohne zusätzliche Plugins oder Software-Installationen verwendet werden. Die Technologie von BigBlueButton setzt voraus, dass ein moderner und aktueller Browser eingesetzt wird.

_Für Teilnehmende:_ Wir empfehlen den Einsatz von Google Chrome. Für Teilnehmende eignet sich zudem auch eine aktuelle Version von Firefox oder Microsoft Edge (mit Chromium). Auf mobilen Geräten ist die Teilnahme mit Safari (iOS) und Chrome (Android) ebenfalls möglich.

_Für Moderierende/Dozierende:_ Wir empfehlen den Einsatz von Google Chrome - nur mit Google Chrome werden sämtliche Funktionalitäten wie beispielsweise Screensharing optimal unterstützt. Andere Browser können verwendet werden - es wird jedoch empfohlen, das eigene Setup vor der ersten Präsentation/dem ersten Unterricht zu überprüfen.

**Mit welchen Geräten kann an BigBlueButton-Meetings teilgenommen werden?**

Es eignen sich alle Geräte, welche die Browser-Voraussetzungen (vgl. oben) erfüllen. Mobile Geräte wie Smartphones und Tablets werden ebenfalls unterstützt - bieten teilweise nicht den vollen Funktionsumfang (bspw. für Moderatoren/Dozierende).

**Kann ich das Whiteboard von BigBlueButton mit dem Tablet (bspw. iPad) nutzen?**

Ja - dieses Setup ist möglich. Dazu sollte das Meeting über einen externen Gäste-Link verfügen. Melden Sie sich dazu mit Ihrem normalen Betreuer-Account im Meeting an und zusätzlich melden Sie sich mit dem Tablet über den Gästelink an. Wir empfehlen dabei einen Benutzernamen wie "Peter Meier - iPad". Via Rechtsklick auf den Tablet-Benutzer können Sie diesen zum Präsentator aufstufen und können anschliessend auf dem Tablet die Präsentation steuern und die Whiteboard-Funktion benutzen (Tipp: Den Upload der Präsentation können Sie zu Beginn mit dem normalen Benutzer erledigen).

**Es wird eine der nachfolgenden Fehlermeldungen angezeigt:**

Error-Code| Fehlerbeschreibung / Grund  
---|---  
1020| Video-Fehler (vgl. unten "Ich kann meine Kamera nicht aktivieren")  
1002| Ihre Firewall blockiert den Zugang oder der BigBlueButton-Server ist nicht erreichbar  
1001| Die Internetverbindung ist verloren gegangen - verbinden Sie sich neu mit dem Internet  
1003| Der gewählte Internet Browser wird nicht unterstützt (ggf. wird eine veraltete Version des Browsers eingesetzt)  
1005| Der Aufbau der Session (Beitritt zum Meeting) war erfolgreich, endet aber plötzlich - starten Sie ihren Browser und ggf. Ihr Gerät neu  
1006 | Session-Timeout (keine Antwort) - bisher nur vereinzelt bei Firefox aufgetreten  
1007| Ihre Firewall blockiert den Zugang oder der BigBlueButton-Server ist nicht erreichbar  
  

**Welche Ports werden bei BigBlueButton verwendet?**  

Falls bei Ihnen kein Zugriff auf das BigBlueButton möglich ist, kann dies auch an Einstellung an der Firewall liegen. Testen können Sie dies, indem Sie mit Ihrem Gerät aus einem anderen Netzwerk (Gäste WLAN etc.) oder via Hotspot über das Mobil-Telefon auf das Online-Meeting zugreifen. Falls dies funktioniert, müssten Sie auf Ihrer Firewall (im geschäftlichen Umfeld durch Ihren IT- Dienst/Support) die nachfolgenden Ports/Freigaben prüfen:

Ports| Beschreibung  
---|---  
80 (TCP/IP)| HTTP  
443 (TCP/IP) | HTTPS  
16384-32768 (UDP) | Verschlüsseltes WebRTC Audio, Video und Screensharing  

## :material-cast-audio: Audio-Probleme

**Warum kann ich im BigBlueButton-Meeting nichts hören?**

Folgende Möglichkeiten stehen zur Problembehebung zur Verfügung:

  * Vergewissern Sie sich, dass Sie andere Audio-Quellen hören können (bspw. YouTube Video)
  * Haben Sie noch ein anderes Konferenz-Tool geöffnet wie Microsoft Teams, Skype, weitere Browser Fenster mit  ähnlichen Funktionen, Wire etc.
  * Klicken Sie auf das Audio-Symbol in BigBlueButton und verbinden Sie sich erneut
  * Wählen Sie in Ihrer Systemsteuerung eine alternative Audio-Quelle oder verwenden Sie ein anderes Headset
  * Starten Sie Ihren Internet Browser neu oder verwenden Sie einen alternativen Browser
  * Starten Sie Ihren PC oder Ihr Notebook neu

**Andere Teilnehmende hören mich schlecht oder können mich nicht verstehen. Woran liegt das?**

  * Vergewissern Sie sich, dass Ihr Headset korrekt eingesteckt ist
  * Haben Sie beim Betreten des Meetings in Ihrem Browser (bei der erstmaligen Nutzung von BigBlueButton) den Zugriff auf Ihr Mikrofon zugelassen?
  * Klicken Sie auf das Audio-Symbol in BigBlueButton und verbinden Sie sich erneut und prüfen Sie Ihr Audio im Echo-Test
  * Ist in Ihren Systemeinstellungen das korrekte Mikrofon aktiviert (bspw. ist das Notebook eingetragen anstelle des Headsets?)
  * Ist die Lautstärken-Einstellung in den Systemeinstellungen korrekt und ausreichend hoch konfiguriert?
  * Haben Sie die Möglichkeit anstelle von WLAN ein Netzwerk-Kabel zu verwenden oder einen Hotspot via Mobiltelefon?


## :material-video-box: Video-Probleme

**Ich kann meine Kamera nicht aktivieren. Woran liegt das?**

* In einigen Setups ist es nur Moderatoren möglich, die Kamera zu aktivieren - nicht aber den Teilnehmenden (der Moderator kann Sie temporär aber zum Co-Moderatoren aufstufen)
* Beim erstmaligen Betreten eines BigBlueButton-Meetings müssen Sie in Ihrem Browser den Zugriff auf die Webcam zulassen (meist findet sich dazu oben in der Adresszeile ein Kamera-Symbol - mit Klick darauf erfahren Sie mehr auf Zugriff auf Kamera/Mikrofon)
* Haben Sie noch ein anderes Video-Konferenz-Tool geöffnet wie Microsoft Teams, Skype, weitere Browser Fenster mit ähnlichen Funktionen, Wire etc.
* Starten Sie Ihren Internet Browser neu oder verwenden Sie einen alternativen Browser
* Starten Sie Ihren PC oder Ihr Notebook neu

  
**Die Präsentation ist zu klein und die Videos der Teilnehmenden und Moderatoren sind sehr gross. Wie kann ich das verändern?**

Zwischen den Videos und der Präsentation/Screensharing kann mit der Maus das Verhältnis der beiden Bereiche vergrössert und verkleinert werden. Zusätzlich kann die Präsentation/Screensharing jederzeit Vollbild angezeigt werden (Klick auf das Symbol in der rechten oberen Ecke der Präsentation)


## :material-projector-screen-outline: Moderatoren/Presenter

**Welche Dateien kann ich über BigBlueButton als Präsentation zeigen?**

BigBlueButton unterstützt beim Upload sowohl gängige Office-Formate (Word, PowerPoint) als auch PDF. Wir empfehlen,wenn immer PDF-Dateien zu verwenden - mit diesen wird die beste Qualität für die Teilnehmenden erzeugt. Andere Formate werden nach dem Upload umgewandelt - dies kann zu veränderten Darstellungen führen. Animationen werden beim Upload nicht unterstützt. Sollten Animationen benötigt werden, kann die Präsentation alternativ via Screensharing oder als Youtube/Vimeo-Video geteilt werden.  

**Wie kann ich Audio-Dateien über BigBlueButton teilen?**

BigBlueButton unterstützt keine direkte Wiedergabe von Audio-Dateien.
Folgende Varianten können Sie aber in Ihrem persönlichen Setup überprüfen:

* Abspielen des Audios in Kombination mit einem Video auf Youtube oder Vimeo
* Beim Einsatz von Google Chrome unter Mac OSX wird beim Screensharing auch das Audio übertragen
* Sie stellen die Audio-Dateien für die Teilnehmenden auf OpenOlat in einem Ordner zur Verfügung

**Kann ich Videos über Screensharing zeigen?**

Für das Abspielen von Videos eignet sich die separate Funktion "Externes Video teilen" - dazu müssen Sie das Video vorgängig über YouTube oder Vimeo bereitstellen.  
In Google Chrome unter Mac OSX kann das Video mit Audio auch im Screensharing gezeigt werden.

**Warum kann ich beim Screensharing nicht ein einzelnes Fenster auswählen?**

Der Dialog zur Selektion eines spezifischen Fensters/Applikation oder eines zweiten Monitors wird nur in Google Chrome angezeigt. Das Screensharing kann teilweise auch in anderen Internet Browsern aktiviert werden, teilt aber direkt und ausschliesslich den Bildschirm mit dem aktuellen BigBlueButton-Meeting-Fenster.

## :material-record: Aufzeichnungen (Recordings)

**Welche Bereiche werden bei der Aufzeichnung aufgezeichnet?**

Bei der Aufzeichnung in BigBlueButton werden sämtliche Aktivitäten aufgezeichnet und stehen anschliessend in einem interaktiven Viewer zur Verfügung.  

_Das Recording beinhaltet:_ Sämtliches Audio, alle aktivierten Kameras, Präsentationen/Screensharing, Notizen auf Folien (Whiteboard-Aktivitäten) gemeinsamer Chat

**Ab wann steht die Aufzeichnung im OpenOlat-Kurs zur Verfügung?**

Allfällige Recordings stehen einige Minuten nach Abschluss/Beendigung des Meetings in OpenOlat zur Verfügung. Unter "abgelaufene Online-Termine" können Sie die Publikation steuern.