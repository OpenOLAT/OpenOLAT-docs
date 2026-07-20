# Häufig gestellte Fragen (FAQ) - Zoom

!!! note "Zoom in OpenOlat"

    Zoom ist ein kommerzielles Web-Konferenzsystem, das über die Schnittstelle LTI 1.3 in OpenOlat eingebunden wird. Die eigentlichen Meetings, Aufzeichnungen und alle weiteren Inhalte werden von Zoom bereitgestellt und verwaltet. OpenOlat stellt den Zugang, die automatische Rollenzuordnung und die Einbettung des Meetings bereit. Die folgenden Fragen und Antworten beziehen sich auf die Nutzung von Zoom in Kombination mit OpenOlat und sind nicht abschliessend.

    * Informationen des Herstellers finden Sie auf der [Zoom-Homepage](https://zoom.us){target=_blank}.
    * Die Verwendung als Kursbaustein ist unter [Kursbaustein "Zoom"](Course_Element_Zoom.md) beschrieben.
    * Die Einrichtung durch Administrator:innen ist im [OpenOlat-Administrationshandbuch](https://docs.openolat.org/de/manual_admin/administration/Zoom/){target=_blank} beschrieben.


## :material-map-marker-question: Zoom finden und konfigurieren

**Wo finde ich Zoom in OpenOlat?**

Zoom kann an drei Stellen zur Verfügung stehen:

* als Kursbaustein "Zoom" im Kurs,
* als Kurswerkzeug in der Toolbar eines Kurses,
* als Gruppenwerkzeug in einer Gruppe.

Welche dieser Varianten verfügbar sind, entscheidet Ihre Administratorin oder Ihr Administrator. Sehen Sie Zoom an einer erwarteten Stelle nicht, ist die Variante auf Ihrer Instanz möglicherweise nicht freigeschaltet.

**Was muss ich als Autor:in oder Betreuer:in konfigurieren?**

Sehr wenig. Für Zoom wählen Sie lediglich das vordefinierte Zoom-Profil aus. Beim Kursbaustein geschieht dies im Kurseditor im Tab "Zoom-Konfiguration", beim Kurs- und beim Gruppenwerkzeug im Dialog "Zoom konfigurieren". Alle weiteren Einstellungen (Meeting anlegen, Termin, Aufzeichnung und so weiter) nehmen Sie direkt in der eingebetteten Zoom-Oberfläche vor.

!!! danger "⚡ Neues Bild erforderlich"

    Screenshot des Tabs "Zoom-Konfiguration" im Kurseditor mit der Auswahl des Zoom-Profils.

**Warum erscheint die Meldung "Zoom ist noch nicht konfiguriert"?**

Es wurde noch kein Zoom-Profil ausgewählt. Wählen Sie das Profil an der passenden Stelle aus:

* Kursbaustein: im Kurseditor den Zoom-Kursbaustein öffnen und im Tab "Zoom-Konfiguration" ein Profil wählen.
* Kurswerkzeug: in den Kurseinstellungen das Werkzeug "Zoom" in der Toolbar konfigurieren.
* Gruppenwerkzeug: in der Administration der Gruppe das Werkzeug "Zoom" konfigurieren.

**Warum ist mein Zoom-Profil inaktiv?**

Erscheint der Hinweis, dass das gewählte Zoom-Profil momentan inaktiv ist, wurde das Profil auf Instanzebene deaktiviert. Ein inaktives Profil kann keine Meetings starten. Wenden Sie sich in diesem Fall an Ihre Administratorin oder Ihren Administrator.


## :material-account-key: Rollen, Identität und Datenschutz

**Bin ich im Meeting Host oder Teilnehmer:in?**

Ihre Rolle im Zoom-Meeting wird automatisch aus Ihrer Rolle in OpenOlat abgeleitet und ist nicht separat einstellbar:

* Betreuer:innen sowie Besitzer:innen des Kurses erhalten in Zoom die Rolle einer moderierenden Person (Instructor) und damit Host-Rechte.
* Teilnehmende erhalten die Rolle Learner.

**Warum werde ich in Zoom nicht korrekt erkannt?**

Beim Beitritt übergibt OpenOlat ausschliesslich Ihre E-Mail-Adresse an Zoom. Zoom ordnet Sie über diese E-Mail-Adresse Ihrem Zoom-Konto zu. Stimmt die in OpenOlat hinterlegte E-Mail-Adresse nicht mit der Adresse Ihres Zoom-Kontos überein, kann die Zuordnung fehlschlagen. Verwenden Sie in beiden Systemen dieselbe E-Mail-Adresse.

**Warum muss ich eine Datenübertragung akzeptieren?**

Bevor das Zoom-Meeting zum ersten Mal geladen wird, erscheint der Dialog "Datenübermittlung akzeptieren". Die eingebettete Seite wird von Zoom Video Communications, Inc. geladen, dabei werden einige Ihrer persönlichen Daten an Zoom übertragen. Erst nach Klick auf "Ich akzeptiere die Datenübertragung" wird das Meeting geladen.


## :material-alert-circle-outline: Meeting starten und beitreten

**Das Zoom-Meeting lässt sich nicht starten oder bleibt leer.**

Bei einigen Browser-Konfigurationen, insbesondere wenn Cookies von Drittanbietern blockiert werden, kann das Meeting nicht innerhalb von OpenOlat geladen werden. Öffnen Sie das Meeting in diesem Fall über die Schaltfläche "Zoom in einem neuen Fenster öffnen" in einem eigenen Browser-Fenster.

**Teilnehmende erhalten beim Beitritt eine 401-Fehlermeldung.**

Erhalten Teilnehmende beim Beitritt eine Fehlermeldung mit einer Correlation ID (401-artig), während Betreuende das Meeting normal starten können, liegt dies in der Regel an abweichenden Zeitzonen zwischen dem Zoom LTI Pro Credential und dem OpenOlat-Server. Die Behebung erfolgt administrativ. Melden Sie das Problem Ihrer Administratorin oder Ihrem Administrator. Details finden sich im [OpenOlat-Administrationshandbuch](https://docs.openolat.org/de/manual_admin/administration/Zoom/){target=_blank}.


## :material-feature-search-outline: Aufzeichnungen, Teilnehmende und Kalender

**Kann ich Aufzeichnungen in OpenOlat sehen?**

Nein. OpenOlat verwaltet und speichert keine Zoom-Aufzeichnungen. Sofern Zoom Aufzeichnungen bereitstellt, sind diese ausschliesslich innerhalb von Zoom zugänglich.

**Gibt es über die Zoom-Integration eine Teilnehmer- oder Anwesenheitsliste?**

Nein. Die Zoom-Integration erfasst keine Anwesenheit und stellt in OpenOlat keine Teilnehmerliste des Meetings bereit. Solche Informationen stehen nur innerhalb von Zoom zur Verfügung.

**Werden Zoom-Meetings im Kalender angezeigt?**

Nur wenn Ihre Administratorin oder Ihr Administrator die Kalenderfunktion aktiviert hat. Ist sie aktiv, trägt Zoom Meetings in den Kurs- oder Gruppenkalender ein. Dabei gelten zwei Einschränkungen: Bei einer Meeting-Serie wird nur das erste Meeting eingetragen, und beim Löschen eines Meetings in Zoom wird der zugehörige Kalendereintrag nicht automatisch entfernt.
