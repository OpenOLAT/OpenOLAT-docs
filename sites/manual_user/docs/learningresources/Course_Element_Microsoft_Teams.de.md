# Kursbaustein "Microsoft Teams" {: #microsoft_teams}

## Steckbrief

Name | Microsoft Teams
---------|----------
Icon | :o_icon_o_vc_icon:
Verfügbar seit | Release 15.4
Funktionsgruppe | Kommunikation und Kollaboration
Verwendungszweck | Integration der Webkonferenz-Software Microsoft Teams
Bewertbar | nein
Spezialität / Hinweis | Microsoft Teams ist eine kommerzielle Software. Um den Kursbaustein zu nutzen, ist eine separate Lizenz und ein Serverhosting erforderlich.


:octicons-device-camera-video-24: **Video-Einführung**: [Microsoft Teams](<https://www.youtube.com/embed/eyHOaF-ujuE>){:target="_blank"}

## Funktionen der Software  {: #software_functions}

Microsoft Teams ermöglicht virtuelle Räume für synchrone Online-Termine mit Webcam- und Audio-Unterstützung.

## Systemvoraussetzungen {: #system_requirements}

MS Teams kann sowohl als App als auch im MS Browser Edge verwendet werden.

!!! tip "Empfehlung"

    Für die vollständige Nutzung aller Funktionen, insbesondere der **Breakout-Räume**, wird die MS Teams **Desktop-App** auf Windows oder macOS empfohlen. Im Webbrowser sowie auf Linux, iOS und Android stehen nicht alle Funktionen zur Verfügung.

## Rollen in MS Teams {: #teams_roles}

In einem Online-Termin mit MS Teams gibt es drei Rollen:

| Rolle | Wer | Rechte |
|-------|-----|--------|
| **Organizer** | Automatisch die Person, die den Online-Termin zuerst startet, genau eine Person pro Online-Termin | Breakout-Räume erstellen, Einstellungen in MS Teams, volle Kontrolle |
| **Presenter** | Alle Personen gemäss der Einstellung **Moderator:in** des Online-Termins (siehe [Moderator-Optionen im Detail](#moderator_options)) | Bildschirm teilen, Inhalte verwalten |
| **Attendee** | Alle übrigen Teilnehmenden | Zuhören und zuschauen |

!!! warning "Achtung: First-Joiner = Organizer"

    Die erste Person, die einen Online-Termin startet, erhält automatisch die Rolle **Organizer**, unabhängig von der Einstellung **Moderator:in** in OpenOlat. Diese Rolle kann nachträglich weder in OpenOlat noch in Microsoft Teams geändert oder neu vergeben werden.

    Bei **permanenten Reservierungen** mit wechselnden Betreuenden hat daher nur diejenige Person, die den Online-Termin zuerst gestartet hat, dauerhaft Zugriff auf erweiterte Funktionen wie Breakout-Räume. Soll eine andere Person als Organizer auftreten, muss ein neuer Online-Termin angelegt werden.

## Online-Termine anlegen bei geschlossenem Kurseditor [:octicons-tag-16:{ title="ab Release 15.4 (OO-5124)" }](https://track.frentix.com/issue/OO-5124) {: #closed_editor_configuration}

Damit Teilnehmende einen Online-Termin mit Microsoft Teams direkt aus dem Kurs betreten können, legen Besitzer:innen und Betreuer:innen des Kurses dafür Online-Termine an. Das geschieht im laufenden Kurs, nicht im Kurseditor: Kursbaustein "Microsoft Teams" öffnen, dann im Tab **Terminverwaltung** die Auswahl **Online-Termin hinzufügen** öffnen:<br>
`Kursbaustein "Microsoft Teams" > Terminverwaltung > Online-Termin hinzufügen`

### Varianten beim Anlegen von Online-Terminen {: #meeting_variants}

Die Auswahl **Online-Termin hinzufügen** bietet vier Varianten an:

  * **Online-Termin hinzufügen**: ein einzelner Online-Termin mit Beginn und Ende.
  * **Permanente Reservierung hinzufügen**: ein Online-Termin ohne Datum, der dauerhaft offen steht. Die Variante erscheint nur, wenn die System-Administration die Option [Online-Termine ohne Datum/permanent](../../manual_admin/administration/Teams_module.de.md#permanent_meetings) auf "Ein" belassen hat. "Ein" ist der Standard. [:octicons-tag-16:{ title="ab Release 21.1.0 (OO-9666)" }](https://track.frentix.com/issue/OO-9666)
  * **Täglich wiederkehrende Online-Termine hinzufügen**: ein Online-Termin pro Werktag, Montag bis Freitag, in einer gewählten Zeitspanne.
  * **Wöchentlich wiederkehrende Online-Termine hinzufügen**: ein Online-Termin pro Woche in einer gewählten Zeitspanne.

Jede Variante legt eigenständige Online-Termine an, bei wiederkehrenden Terminen einen je Datum. Im Tab **Terminverwaltung** öffnet der Link **Bearbeiten** jeden Online-Termin einzeln. Bei vergangenen Online-Terminen steht dort **Ansehen**.

## Online-Termin hinzufügen: Die Einstellungen im Detail {: #add_meeting}

### Konfiguration Online-Termin

  *  **Name**: Bezeichnung des Online-Termins. Pflichtfeld.
  *  **Erstellt durch**: Der Name der Person, die den Online-Termin anlegt, wird automatisch angezeigt.
  *  **Beschreibung**: Beschreibung des Online-Termins. Sie erscheint in der Detailansicht des Online-Termins, bevor Teilnehmende dem Online-Termin beitreten.
  *  **Hauptmoderator:in**: Hier kann der Name einer Person eingetragen werden. Vorbelegt ist der Name der Person, die den Online-Termin anlegt.
  *  **Gäste**: Das Kontrollkästchen **erlauben** lässt nicht angemeldete Personen am Online-Termin teilnehmen. Diese Option ist nur sichtbar, wenn der Kurs öffentlich zugänglich und der Gastzugang aktiviert ist.
  *  **Zugang externe Benutzer:innen**: Ein Kennzeichen, ein eindeutiges Wort ohne Sonderzeichen. OpenOlat erzeugt daraus einen Link, den Sie mit externen Personen teilen, z. B. per E-Mail. Bleibt das Feld leer, ist der Zugang über den Link deaktiviert.
  *  **Raumbuchungen anzeigen**: Kalenderansicht zur Prüfung von belegten Online-Terminen.
  *  **Terminaufzeichnung**: Schaltet die Aufzeichnung für diesen Online-Termin ein oder aus. Der Schalter erscheint nur, wenn die System-Administration die Funktion eingeschaltet hat. Was die Einstellung bewirkt und welche Felder dazukommen, steht im Abschnitt [Terminaufzeichnung](#meeting_recording).
  *  **Teilnehmer:innen können den Termin eröffnen** :octicons-tag-16:{ title="ab Release 15.4.1 (OO-5250)" }: Bestimmt, ob Teilnehmende den Online-Termin starten dürfen, ohne dass eine Betreuer:in anwesend ist. Zur Wahl stehen zwei Karten. "Nicht erlaubt" ist vorausgewählt. Mit "Erlaubt" dürfen Teilnehmer:innen mit einem Microsoft-Konto der Organisation den Online-Termin mit eingeschränkten Berechtigungen eröffnen. Eröffnet eine Teilnehmer:in den Online-Termin, stehen den Betreuer:innen keine Gruppenräume ([Breakout-Räume](#breakout_rooms)) zur Verfügung. Ist die Terminaufzeichnung eingeschaltet, steht die Auswahl fest auf "Nicht erlaubt". Die Karten erscheinen nur, wenn die Serverkonfiguration dafür eingerichtet ist.
  *  **Moderator:in**: Bestimmt, wer in MS Teams die Rolle **Presenter** erhält (siehe [Rollen in MS Teams](#teams_roles)). Pflichtfeld.

#### Moderator-Optionen im Detail {: #moderator_options}

| OO-Einstellung | Wer wird Presenter in Teams |
|---|---|
| **Rolle Betreuer:in / Besitzer:in** | Nur Kursbetreuer:innen und -besitzer:innen; alle anderen Teilnehmenden werden Attendees |
| **Organisation** | Alle Benutzer:innen der Azure-Organisation erhalten beim Beitritt automatisch die Rolle Presenter |
| **Alle** | Alle Teilnehmenden werden Presenter |

!!! info "Wichtig"

    Die Einstellungen eines Online-Termins lassen sich nur ändern, solange er noch nicht gestartet wurde. Danach zeigt das Formular die Einstellungen nur noch an. Sollen andere Moderator-Einstellungen gelten, muss ein neuer Online-Termin angelegt werden.

#### Bei Online-Terminen mit Datum

  *  **Beginn**: Datum und Uhrzeit, zu der der Online-Termin beginnt.
  *  **Vorlaufzeit (Min.)**: Zeit in Minuten vor dem Beginn, in der Besitzer:innen und Betreuer:innen den Online-Termin bereits starten und betreten können. Für Teilnehmende öffnet der Online-Termin erst zum Beginn.
  *  **Ende**: Datum und Uhrzeit, zu der der Online-Termin endet.
  *  **Nachlaufzeit (Min.)**: Nachlaufzeit, in der der Online-Termin für alle Personen verlängert werden kann.

!!! info "Wichtig"

    Bei täglich oder wöchentlich wiederkehrenden Online-Terminen legen Sie zusätzlich **Start wiederkehrendes Datum** und **Ende wiederkehrendes Datum** fest. Im nächsten Schritt listet der Assistent alle Termine dieser Zeitspanne auf. Dort lassen sich einzelne Termine löschen oder über **Online-Termin hinzufügen** ergänzen.

In der Konfiguration eines Online-Termins öffnet der Link **Raumbuchungen anzeigen** beim Anlegen und beim Bearbeiten eine Übersicht über alle gebuchten Microsoft Teams Online-Termine der Instanz. Das erleichtert es, zeitliche Engpässe bzw. eine starke Auslastung des Systems frühzeitig zu erkennen und gegebenenfalls einen anderen Termin zu wählen.

Im Tab **Online-Termine** öffnen Sie einen bestimmten Online-Termin.

## Terminaufzeichnung [:octicons-tag-16:{ title="ab Release 21.1 (OO-9665)" }](https://track.frentix.com/issue/OO-9665) {: #meeting_recording}

Wer einen Online-Termin aufzeichnet, will die Aufzeichnung danach den Teilnehmenden zeigen, ohne Dateien zu verschicken. Mit der Terminaufzeichnung holt OpenOlat die fertige Aufzeichnung aus Microsoft Teams ab, legt sie beim Online-Termin ab und zeigt sie dort an. Wer sie sehen darf, bestimmen Sie über Rollen. Ist in der System-Administration bei "Terminaufzeichnung automatisch löschen" eine Zahl Tage eingetragen, löscht OpenOlat die Aufzeichnung danach automatisch.

Die Terminaufzeichnung gehört zum Online-Termin, nicht zum Kursbaustein. Sie wirkt darum an allen Orten gleich, an denen Online-Termine mit Microsoft Teams entstehen: Kursbaustein "Microsoft Teams", "Kurs Termine", Kursbaustein "Terminplanung", Gruppen und Betreuer:innen-Chat.

Voraussetzung ist, dass die System-Administration die Funktion "Terminaufzeichnung" eingeschaltet hat, siehe [Modul Microsoft Teams](../../manual_admin/administration/Teams_module.de.md#meeting_recording). Sonst fehlen die Einstellungen im Online-Termin, und OpenOlat holt keine Aufzeichnung ab. Eine Aufzeichnung, die jemand direkt in Microsoft Teams startet, bleibt dann in Microsoft Teams.

### Einstellungen im Online-Termin {: #recording_settings}

Beim Anlegen oder Bearbeiten eines Online-Termins legen Sie fest, ob und wie er aufgezeichnet wird. Die Standardwerte kommen aus der System-Administration, Sie können sie je Online-Termin ändern.

  *  **Terminaufzeichnung**: Mit "Ein" darf der Online-Termin aufgezeichnet werden. Alle Personen müssen dann vor dem Betreten zustimmen, und die Auswahl "Teilnehmer:innen können den Termin eröffnen" steht fest auf "Nicht erlaubt". Mit "Aus" wird nichts aufgezeichnet, und die Seite des Online-Termins zeigt keine Aufzeichnungen.
  *  **Aufnahme starten**: "Automatisch, sobald das Meeting beginnt" oder "Manuell durch die Sitzungsleitung". Wer den Online-Termin startet, sieht neben dem Button **Online-Termin starten** das Kontrollkästchen **Aufzeichnung automatisch starten**. Es ist nach dieser Einstellung vorbelegt und lässt sich vor dem Start ändern.
  *  **Aufnahme automatisch veröffentlichen für**: Die Rollen, die die Aufzeichnung nach dem Online-Termin sehen: "Besitzer:innen / Betreuer:innen", "Teilnehmer:innen des Kurses / der Gruppe", "Alle Teilnehmer:innen des Meetings (ausser Gäste)" und "Gäste". Ist keine Rolle angekreuzt, veröffentlicht OpenOlat die Aufzeichnung nicht automatisch. Sie publizieren sie dann nach dem Online-Termin von Hand.

Die beiden Felder "Aufnahme starten" und "Aufnahme automatisch veröffentlichen für" erscheinen erst, wenn die Terminaufzeichnung eingeschaltet ist.

### Aufzeichnungen nach dem Online-Termin {: #recordings_list}

Nach dem Online-Termin finden Sie die Aufzeichnung auf der Seite des Online-Termins in der Liste **Aufzeichnungen**. Sie erscheint nicht sofort: OpenOlat holt fertige Aufzeichnungen einmal pro Stunde ab, frühestens 15 Minuten nach dem Ende des Online-Termins. Bis dahin zeigt die Liste "Es ist zur Zeit noch keine Aufzeichnung für diesen Online-Termin vorhanden."

Die Liste zeigt je Aufzeichnung **Name**, **Beginn**, **Ende** und den Link **Öffnen**. "Öffnen" zeigt die Aufzeichnung in OpenOlat an, dort lässt sie sich auch herunterladen. Der Link erscheint nur, wenn die Aufzeichnung für eine Rolle der Person veröffentlicht ist. Das gilt auch für Besitzer:innen und Betreuer:innen.

Besitzer:innen und Betreuer:innen sehen zusätzlich die Spalte **Publizieren** und je Aufzeichnung das Menü **Weitere Aktionen** am Zeilenende. Ist in der System-Administration bei "Terminaufzeichnung automatisch löschen" eine Zahl Tage eingetragen, zeigt ihnen die Spalte "Wird nicht automatisch gelöscht" (Schloss-Symbol), welche Aufzeichnungen davon ausgenommen sind.

**Publizieren** öffnet das Fenster "Publizieren für:" mit denselben vier Rollen wie im Online-Termin. Angekreuzt sind die Rollen, für die die Aufzeichnung bereits veröffentlicht ist. Der Button **Publizieren** übernimmt die Auswahl. So geben Sie eine Aufzeichnung nachträglich frei oder ziehen die Freigabe zurück.

Das Menü **Weitere Aktionen** einer Aufzeichnung bietet drei Aktionen:

  *  **Öffnen**: zeigt die Aufzeichnung an, wie der Link in der Liste.
  *  **Aufzeichnung nicht löschbar**: nimmt die Aufzeichnung vom automatischen Löschen aus, zum Beispiel eine Vorlesung, die dauerhaft gebraucht wird. Für eine so markierte Aufzeichnung steht an derselben Stelle **Aufzeichnung löschbar**, das die Ausnahme wieder aufhebt.
  *  **Löschen**: löscht die Aufzeichnung nach einer Rückfrage endgültig. Der Online-Termin bleibt bestehen.

Das automatische Löschen betrifft nur Aufzeichnungen, nie den Online-Termin. Die Zahl Tage legt die System-Administration fest.

## Breakout-Räume {: #breakout_rooms}

Breakout-Räume können ausschliesslich vom **Organizer** eines Online-Termins erstellt und verwaltet werden (siehe [Rollen in MS Teams](#teams_roles)).

**Unterstützte Plattformen:** Breakout-Räume stehen nur in der Teams Desktop-App unter Windows und macOS zur Verfügung: nicht im Webbrowser und nicht auf mobilen Geräten.

**Einschränkungen bei der Teilnehmerzuweisung:** Folgende Personen können Breakout-Räumen nicht zugewiesen werden:

  * Personen mit einem Teams-Free-Account
  * Personen auf nicht unterstützten Geräten (z.B. CVI-Konferenzgeräte)
  * Offline-Teilnehmende oder Personen mit veralteter Teams-Version

**Weitere Einschränkungen:** Breakout-Räume sind nicht verfügbar bei abgesagten oder gelöschten Online-Terminen, in privaten oder geteilten Kanälen sowie bei entsprechenden Admin-Richtlinien.

**Kapazität:** Pro Online-Termin sind maximal 300 Teilnehmende möglich. Bei Überschreitung wird die Breakout-Funktion automatisch deaktiviert. Räume verfallen nach 60 Tagen Inaktivität.

## Anzeige im Kurskalender {: #calender_view}

Wer die Online-Termine des Kurses im Blick behalten will, findet sie im Kurskalender: OpenOlat trägt jeden Online-Termin mit Datum, der im Kursbaustein angelegt wird, automatisch dort ein. Der Kalendereintrag enthält einen Link, der direkt zum Online-Termin führt. Teilnehmende können den Kurskalender abonnieren.

!!! info "Wichtig"
    Im Kurskalender erscheinen nur Termine mit einem definierten Start- und Enddatum. Permanente Reservierungen ohne Datum werden im Kalender nicht angezeigt.

  :octicons-device-camera-video-24: **Video-Einführung**: [Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank"}

## Sicht der Teilnehmenden {: #participant_perspective}

Ruft ein:e Teilnehmer:in den Kursbaustein auf, erscheinen zwei Listen: **Aktuelle und zukünftige Online-Termine** und **Vergangene Online-Termine**. Online-Termine ohne Datum sind in der Spalte **Ohne Datum** markiert und stehen immer in der ersten Liste. Ein Klick auf **Auswählen** öffnet die Detailansicht des jeweiligen Online-Termins.

![Zwei Listen mit aktuellen und vergangenen Online-Terminen, Spalten Name, Ohne Datum, Beginn, Ende und Link Auswählen](assets/course_element_teams_overview_v1_de.png){ class="shadow lightbox" title="Übersicht im Kursbaustein Microsoft Teams" }

Über **Meeting beitreten** öffnet sich der Online-Termin in Microsoft Teams in einem neuen Fenster. Solange noch niemand den Online-Termin gestartet hat, ist der Button für Teilnehmende nicht aktiv. Besitzer:innen und Betreuer:innen sehen an seiner Stelle **Online-Termin starten**. Ob Teilnehmende den Online-Termin auch ohne Betreuer:in eröffnen dürfen, hängt von der Konfiguration des Online-Termins ab (siehe oben).

![Button Meeting beitreten, daneben der Name, unter dem die Person dem Online-Termin beitritt](assets/course_element_teams_join_v1_de.png){ class="shadow lightbox" title="Detailansicht eines Online-Termins" }

Ist für den Online-Termin die Terminaufzeichnung eingeschaltet, steht über dem Button der Abschnitt **Aufzeichnungen**: "Dieser Online-Termin kann aufgezeichnet werden. Die Aufzeichnung kann nach dem Online-Termin in OpenOlat veröffentlicht werden." Den Online-Termin betreten Sie erst, wenn Sie **Ich bin einverstanden** angekreuzt haben. Nach dem Online-Termin erscheint die Aufzeichnung auf derselben Seite in der Liste **Aufzeichnungen**. Mit **Öffnen** sehen Sie sie an, sofern sie für Ihre Rolle veröffentlicht ist. Gäste sehen eine Aufzeichnung nur, wenn die Rolle "Gäste" gewählt ist. Details: [Terminaufzeichnung](#meeting_recording).

!!! info "Wichtig"

    Bei beendeten Online-Terminen ist der Beitritt nicht mehr möglich.

## Bei Problemen {: #troubleshooting}

Bei anwendungsspezifischen Herausforderungen steht die Microsoft-Hilfe zur Verfügung:

[Microsoft-Hilfe: Problembehandlung in Microsoft Teams](https://support.microsoft.com/de-de/teams/platform/troubleshoot-in-microsoft-teams){:target="_blank"}

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Microsoft Teams >](../../manual_admin/administration/Teams_module.de.md)<br>
[Microsoft-Hilfe: Problembehandlung in Microsoft Teams](https://support.microsoft.com/de-de/teams/platform/troubleshoot-in-microsoft-teams){:target="_blank"}

**Weiterführend**<br>
[Virtuelle Klassenzimmer >](../basic_concepts/Virtual_classrooms.de.md)<br>
[Kursbaustein "Zoom" >](zoom/index.de.md)<br>
[Termine und Absenzen >](../basic_concepts/Events_and_Absences.de.md)<br>
[Gruppenwerkzeuge nutzen >](../groups/Using_Group_Tools.de.md)

**youtube**<br>
[Microsoft Teams](<https://www.youtube.com/embed/eyHOaF-ujuE>)<br>
[Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>)

[Zum Seitenanfang ^](#microsoft_teams)
