# Kursbaustein "SCORM-Lerninhalt"

## Steckbrief

Name | SCORM-Lerninhalt
---------|----------
Icon | ![Scorm learning content Icon](assets/scorm.png){ class=size24  }
Verfügbar seit | 
Funktionsgruppe | Wissensvermittlung
Verwendungszweck | Integration von SCORM-Paketen, die mit anderen Autorenwerkzeugen erstellt wurden
Bewertbar | ja
Spezialität / Hinweis |

SCORM steht für "Sharable Content Object Reference Model" und ist ein standardisiertes E-Learning-Format für interaktive E-Learning Module, das von OpenOlat unterstützt wird. Über den Kursbaustein "SCORM Lerninhalt" können SCORM-Pakete (SCORM Version 1.2) in OpenOlat Kurse eingebunden werden. Das SCORM-Paket muss extern erstellt werden, beispielsweise mit [eLML](http://www.elml.org "eLML").

Gehen Sie in Ihren Kurs und fügen Sie einen Kursbaustein "SCORM-Lerninhalt" dem Kurs hinzu. Anschließend können Sie im Tab "Lerninhalt" die weitere Konfiguration vornehmen.

## Tab Lerninhalt

Wählen oder importieren Sie im ersten Schritt einen SCORM Inhalt. Klicken Sie auf "Importieren", um ein neues SCORM-Paket hochzuladen, oder wählen Sie ein bestehendes SCORM-Paket aus Ihren Einträgen aus. SCORM-Pakete können nicht nur im Kurseditor, sondern auch im "Autorenbereich" importiert werden, was im Kapitel "Aktionen im Autorenbereich" unter dem Punkt ["Importieren"](../area_modules/authoring_new_course.de.md#lernressourcen-importieren) erklärt wird. Wenn Sie noch keine ZIP-Datei als SCORM-Lerninhalt ausgewählt haben, erscheint beim Titel **Gewählter SCORM-Lerninhalt** die Meldung _Kein SCORM-Lerninhalt ausgewählt_.

Wenn Sie schon einen SCORM-Lerninhalt hinzugefügt haben, erscheint dessen Name als Link. Folgen Sie dem Link um zur Vorschau zu gelangen. Um die Zuordnung eines SCORM-Lerninhaltes nachträglich zu ändern, klicken Sie im Tab "Lerninhalt" auf "SCORM-Lerninhalt auswechseln" und wählen anschliessend ein anderes SCORM-Paket aus.

Unter "Einstellungen" im Tab "Lerninhalt" können Sie bestimmen, wie der Lerninhalt Ihren Kursteilnehmern angezeigt werden soll.

 **Menu anzeigen:** Bestimmen Sie, ob bei der Anzeige des Scorm-Packets links ein Navigations-Menu angezeigt werden soll.

 **Inhalt automatisch starten:** Bestimmen Sie, ob der SCORM-Lerninhalt automatisch startet, wenn der entsprechende Menu-Punkt im Kurs ausgewählt wird. Wenn Sie diese Option nicht aktivieren, wird stattdessen eine Startseite angezeigt.

 **Navigationsbuttons anzeigen:** Bestimmen Sie, ob innerhalb des Scorm- Inhaltes mit Vor- und Zurückbuttons navigiert werden kann.

 **Nur Modul anzeigen, LMS ausblenden:** Ist diese Checkbox markiert, wird OpenOlat mit dem Öffnen des Kursbausteins ausgeblendet. Stattdessen wird das SCORM Modul im ganzen Browserfenster dargestellt.

 **Modul automatisch schliessen wenn beendet:** Das SCORM Modul wird automatisch geschlossen sobald es beendet ist, und der Benutzer kehrt in die Kursansicht zurück.

 **Resultat aus SCORM übertragen:** Bestimmen Sie, ob die Summe aller im Scorm-Packet erreichten Punkte an das OLAT-Bewertungssystem weitergegeben werden soll.

 **Notwendige Punktzahl für 'bestanden':** Geben Sie eine Ganzzahl ein, die aussagt, wieviele Punkte erreicht werden müssen, damit der Scorm-Test als bestanden gilt.

 **Reduzieren von Punkten bei erneutem Versuch verhindern:** Falls dem Benutzer mehrere Lösungsversuche zur Verfügung stehen, kann mit Markieren dieser Checkbox verhindert werden, dass ein erneuter Anlauf ein bereits bestehendes Resultat verschlechtert.

 **Lösungsversuche nur zählen, wenn Punkte übertragen werden:** Die Lösungsversuche werden für den Benutzer nur dann gezählt, wenn auch Punkte vom Scorm an OpenOlat übertragen werden. Je nachdem, wann das Scorm die Punkte liefert (z.B. regelmässig oder nur am Ende der Bearbeitung), greift die Option bereits, wenn ein Benutzer einen Teil der Scorm-Aktivitäten bearbeitet hat, oder erst, wenn das Scorm geschlossen wird.

 **Maximale Anzahl Lösungsversuche:** Mittels des Drop-Down-Menus können Sie die Anzahl der Lösungsversuche einschränken. Der höchste zur Auswahl stehende Wert ist 20.

## Tab Layout

Im Tab "Layout" definieren Sie die Einstellungen für die Anzeige des SCORM- Lerninhaltes. Dazu können Sie entweder die Layout-Einstellungen der Lernressourcenverwaltung übernehmen, oder aber überschreiben. Wenn Sie die Option "Anpassen" wählen, stehen Ihnen die nachfolgenden Einstellungen zur Verfügung. So können Sie festlegen ob der SCORM-Lerninhalt unverändert, oder aber optimiert für OpenOlat angezeigt werden soll. Der Anzeigemodus "Optimiert für OpenOlat" gestattet Ihnen z.B. das Kurslayout auf den SCORM-Inhalt anzuwenden.

Unter "Einstellungen" können Sie bestimmen, wie der Lerninhalt Ihren Kursteilnehmern angezeigt werden soll.

### Optionen für die Anzeige

 * * *
 
 **Standardwerte übernehmen:** Werden Lernressourcen aus der Lernressourcenverwaltung in Kursen eingebunden, so können die Einstellungen für die Darstellung aus der Lernressourcenverwaltung übernommen werden (Option "Aus Layouteinstellungen der Lernressource übernehmen"). Möchten Sie für diesen Kurs die Standardwerte überschreiben, so wählen Sie die Option "Anpassen".

* * *

 **Anzeigemodus:** Wählen Sie den Modus "Standard" um die Ressource unverändert anzuzeigen. Dieser Modus ist geeignet für Ressourcen, bei denen es im Modus "Optimiert für OpenOlat" zu Anzeigeproblemen kommt. Wählen Sie den Modus "Optimiert für OpenOlat" wenn Sie das Kurslayout in der Seite einbinden wollen, eine JavaScript Bibliothek verwenden möchten, das OpenOlat Glossar auf dieser Seite anwenden wollen oder die Höhe der Seite automatisch berechnet werden soll. Bei SCORM Modulen ist der Modus "Standard" empfohlen.

* * *

 **JavaScript hinzufügen:** Um die Funktionen des Anzeigemodus "Optimiert für OpenOlat" nutzen zu können muss die JavaScript Bibliothek "jQuery" aktiviert sein. Die Option "Prototype" sollte nur gewählt werden wenn Ihre Inhalte diese Bibliothek voraussetzen. Wählen Sie keine Bibliothek wenn es zu Anzeigeproblemen mit Ihren Inhalten kommt.

* * *

 **Glossarbegriffe einbinden:** Wählen Sie diese Option um die Möglichkeit der Hervorhebung von Glossarbegriffen zu aktivieren falls Sie in Ihrem Kurs ein Glossar konfiguriert haben. Diese Option setzt die Verwendung der JavaScript Bibliothek "jQuery" voraus.

* * *

 **Höhe Anzeigefläche:** Mittels des Drop-Down-Menus können Sie die Höhe der Inhalte bestimmen. Sie haben die Möglichkeit, diese via "Automatisch" auf die jeweilige Fensterhöhe zu setzen oder auf einen bestimmten Wert zu setzen.

* * *

 **Layout anpassen:** Wählen Sie die Option "OpenOlat Stylesheets" um das OpenOlat und Kurslayout in Ihre Seite zu übernehmen (Schriftart, Farben, Grösse etc.). Wenn Sie diese Anpassung nicht wünschen wählen Sie die Option "Keine".

* * *

 **Zeichensatz Inhalt:** OpenOlat versucht, den Zeichensatz automatisch zu erkennen. Wenn die Option "Automatisch" nicht zu der gewünschten Anzeige führt, kann die Kodierung des Inhalts anhand eines vordefinierten Zeichensatzes konfiguriert werden (ist keine Kodierung vorhanden, wird per Default der Zeichensatz ISO-8899-1 verwendet).

* * *

 **Zeichensatz Javascript:** Erlaubt die Kodierung des Javascript Codes anhand eines vordefinierten Zeichensatzes (per Default wird der gleiche Zeichensatz für Inhalt und Javascript verwendet).

!!! info "Info"

    SCORM-Lerninhalte werden stets mit Startseite angezeigt. Wenn ein SCORM-Lerninhalt Aufgaben und Tests beinhaltet, werden auf dieser Startseite die erreichte Punktzahl und die verbleibenden Versuche, den Lerninhalt erfolgreich zu absolvieren, ermittelt.
