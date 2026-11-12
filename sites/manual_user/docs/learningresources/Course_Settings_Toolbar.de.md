# Toolbar {: #tab_toolbar}

<a id="toolbar"></a>

Die Toolbar (Werkzeugleiste) steht im Kopf der Seite direkt unter der Hauptnavigation und zeigt die Icons der Werkzeuge. So erreichen Teilnehmende die Werkzeuge, die sie während des ganzen Kurses brauchen, an einer zentralen Stelle. Im Tab "Toolbar" legen Sie fest, ob die Teilnehmer:innen im Kurs die Toolbar sehen und welche Werkzeuge darin erscheinen:<br>
`Kurs > Administration > Einstellungen > Tab "Toolbar"`

Diese Seite beschreibt zuerst die Einstellungen im Tab "Toolbar" und danach, was Teilnehmende in der Toolbar sehen.

## Steckbrief

Name | Toolbar
---------|----------
Verfügbar seit | Release 10.0 (2014)

---

## Werkzeuge in Toolbar aktivieren {: #activate_tools}

Ist die Checkbox "Toolbar sichtbar für Teilnehmer:innen" eingeschaltet, wählen Sie darunter die Werkzeuge aus. Den Tab bearbeiten Besitzer:innen des Kurses, Lernressourcenverwalter:innen, Administrator:innen und Personen mit dem Recht "Kurseditor".

![Tab Toolbar mit den aktivierbaren Werkzeugen: Kurskalender eingeschaltet, darunter die Checkbox "Betreuer:innen dürfen den Kalender bearbeiten" mit Hinweistext](assets/course_settings_toolbar1_v3_de.png){ class="shadow lightbox" title="Tab Toolbar der Kurseinstellungen · 2026.11.10" }

Betreuer:innen und Besitzer:innen sehen die Toolbar immer. Jedes Werkzeug, das Sie für den Kurs einschalten, erscheint mit seinem Icon in der Toolbar.<br>
[Mehr dazu >](#show_icons)

Zu den [Werkzeugen](#available_icons) der Toolbar zählen neben der Kurssuche, dem Glossar und dem Kurs-Chat Werkzeuge, die es auch als Kursbausteine gibt, z.B. Kurskalender, Liste der Teilnehmer:innen, E-Mail, Blog, Wiki, Forum und Dokumente. Bei [Wiki](../learningresources/Wiki.de.md) und [Blog](Blog/index.de.md) können Sie auch auf bereits erstellte Lernressourcen zurückgreifen. Die übrigen Werkzeuge ähneln den entsprechenden Kursbausteinen, bieten aber nicht alle Konfigurationsmöglichkeiten, die die Kursbausteine im Kurseditor haben.

Planen Betreuer:innen die Termine des Kurses, erlauben Sie ihnen mit der Checkbox "Betreuer:innen dürfen den Kalender bearbeiten", im Kurskalender Termine hinzuzufügen, zu ändern und zu löschen. Die Checkbox erscheint direkt unter "Kurskalender", sobald Sie den Kurskalender einschalten. Teilnehmer:innen lesen die Termine. Schalten Sie den Kurskalender oder die Toolbar aus, speichert OpenOlat auch diese Option als ausgeschaltet.<br>
[Mehr zu den Rechten im Kurskalender >](#calendar)

Besonders in linear aufgebauten [Lernpfadkursen](Learning_path_course/index.de.md) stellt die Toolbar wichtige Werkzeuge bereit, unabhängig von der Reihenfolge der Lernschritte.

[Zum Seitenanfang ^](#tab_toolbar)

---

## Externe Kurstools [:octicons-tag-16:{ title="ab Release 21.0 (OO-9488)" }](https://track.frentix.com/issue/OO-9488) {: #external_tools}

Arbeiten Ihre Teilnehmer:innen neben dem Kurs mit weiteren Webanwendungen, etwa einem Stundenplan oder einem Schulportal, legen Sie die Links dorthin als externe Kurstools direkt in die Toolbar des Kurses. Externe Kurstools führen zum Beispiel zu einem Absenzmanagementsystem, einer Schulinfoseite, einem Partnerportal, einem Raumbuchungstool oder einem externen Mail- oder Kalendersystem. Pro Kurs stehen vier externe Kurstools zur Verfügung.

Eingerichtet werden sie unter `Kurs > Administration > Einstellungen > Tab "Toolbar"`. Die Zeilen "Externes Kurstool 1" bis "Externes Kurstool 4" stehen unter den Werkzeugen der Toolbar. Sie erscheinen nur, wenn bei "Toolbar sichtbar für Teilnehmer:innen" die Checkbox "Ein" aktiviert ist. Aktivieren Sie bei einem Tool die Checkbox "Ein", erscheinen darunter die Felder "Name", "URL", "Icon" und "Sichtbar für".

![Tab Toolbar und Zeilen Externes Kurstool 1 bis 4 markiert, Kurstool 1 eingeschaltet mit ausgefülltem Name, URL, Icon und Sichtbar für](assets/course_settings_toolbar_external_tools_entry_v1_de.png){ class="shadow lightbox" title="Externe Kurstools im Tab Toolbar der Kurseinstellungen · 2026.10.02" }

| Feld | Beschreibung |
|---|---|
| **Name** | Bezeichnung in der Toolbar, max. 64 Zeichen. Pflichtfeld. |
| **URL** | Absolute URL beginnend mit `http://` oder `https://`. Relative URLs, Anker, `javascript:`, `data:`, `mailto:`, `tel:` und protokollrelative Links werden abgelehnt. Pflichtfeld. |
| **Icon** | Auswahl aus dem Icon-Katalog (rund 30 Einträge, z.B. Link, E-Mail, Kalender, Stundenplan, Absenzen-Management, Schulportal, Buchungen, Videos, Dateien). Pflichtfeld. |
| **Sichtbar für** | Separate Checkboxen für "Teilnehmer:innen", "Betreuer:innen" sowie "Besitzer:innen und Personen mit administrativen Rollen". Jede Option gilt nur für ihre Rolle: Ein Tool, das nur für Teilnehmer:innen sichtbar ist, sehen Betreuer:innen nicht. Administrator:innen, Lernressourcenverwalter:innen, Principals und Kursplaner:innen sehen das Tool, wenn die Option für Besitzer:innen ausgewählt ist. Bei einem neu eingeschalteten Tool ist diese Option vorausgewählt. Ist keine Option gewählt, zeigt das Formular die Warnung "Das Tool ist aktiviert, aber für niemanden sichtbar. Wählen Sie mindestens eine Option." Gespeichert wird das Tool trotzdem, in der Toolbar sieht es dann niemand. |

In der Toolbar sehen die Rollen, die unter "Sichtbar für" ausgewählt sind, das Tool mit seinem Namen und Icon.

![Externes Kurstool Stundenplan mit Kalender-Icon rechts neben der Kurssuche markiert](assets/course_toolbar_with_external_tools_v2_de.png){ class="shadow lightbox" title="Externes Kurstool in der Toolbar des Kurses · 2026.10.02" }

!!! warning "Achtung"
    Entfernen Sie bei einem Tool die Checkbox "Ein" oder schalten Sie "Toolbar sichtbar für Teilnehmer:innen" aus, löscht OpenOlat beim Speichern Name, URL und Icon der betroffenen Tools, die Auswahl unter "Sichtbar für" wird zurückgesetzt. Beim erneuten Einschalten erfassen Sie die Angaben neu.

**Kurs kopieren / importieren**

- Die Konfiguration aller vier externen Kurstools wird beim Kopieren eines Kurses mitübernommen.
- Beim Importieren eines Kurses sind alle vier Tools ausgeschaltet. Name, URL und Icon werden nicht übernommen und müssen im importierten Kurs neu erfasst werden.

!!! info "Wichtig"
    Externe Kurstools öffnen immer in einem neuen Browserfenster. Es werden keine Nutzerdaten (Name, E-Mail usw.) an das Zielsystem übertragen. Teilen OpenOlat und das Zielsystem denselben Identity Provider, funktioniert Single Sign-on automatisch.

[Zum Seitenanfang ^](#tab_toolbar)

---

## Verfügbare Icons {: #available_icons}

Welche Icons eine Person in der Toolbar sieht, hängt von den eingeschalteten Werkzeugen und von ihrer Rolle im Kurs ab.

**Beispiel Teilnehmer:in**:

![Toolbar aus Sicht einer Teilnehmer:in mit den Werkzeugen von Infoseite (Info-Symbol) bis Kurssuche, darunter Mitteilungen (Megafon) und Blog (Blog-Symbol), rechts Mein Kurs](assets/toolbar_example_course_participant_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Teilnehmer:in · 2026.10.27" }

**Beispiel Kursbesitzer:in/Betreuer:in**:

![Toolbar aus Sicht einer Kursbesitzer:in mit zusätzlich Administration, Status Veröffentlicht und Rollenwechsler, dazwischen dieselben Werkzeuge von Infoseite bis Kurssuche](assets/toolbar_example_course_owner_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Kursbesitzer:in · 2026.10.27" }

### Administration {: #admin}

![Werkzeug Administration ganz links in der Toolbar markiert: Menü, über das Besitzer:innen und berechtigte Betreuer:innen den Kurs verwalten. Daneben Status Veröffentlicht und Werkzeuge ab Infoseite](assets/toolbar_admin_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Das Menü "Administration" sehen nur Personen, die den Kurs verwalten, Teilnehmer:innen sehen es nicht. Dort öffnen sie unter anderem die Einstellungen und den Kurseditor.<br>
[Mehr dazu >](Administration/index.de.md)

---

### Status [:octicons-tag-16:{ title="ab Release 13.0 (OO-3584)" }](https://track.frentix.com/issue/OO-3584) {: #status}

![Status Veröffentlicht als grüne Schaltfläche mit Auswahlpfeil markiert: hier wechseln Berechtigte den Status des Kurses. Rechts daneben die Werkzeuge ab Infoseite mit dem Info-Symbol](assets/toolbar_status_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Den Status sehen nur Personen, die den Kurs verwalten, Teilnehmer:innen sehen ihn nicht. Hier wechseln sie den Status des Kurses.<br>
[Mehr dazu >](../learningresources/Access_configuration.de.md)

---

### Infoseite [:octicons-tag-16:{ title="ab Release 21.1 (OO-9758)" }](https://track.frentix.com/issue/OO-9758){:target="_blank"} {: #info_page}

![Werkzeug Infoseite mit dem Info-Symbol als erstes Werkzeug der Toolbar markiert](assets/toolbar_course_info_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Wer wissen möchte, worum es in einem Kurs geht, öffnet über das Werkzeug "Infoseite" mit dem Info-Symbol die Beschreibung des Kurses, etwa mit Durchführungszeitraum und Ort. Dieselben Angaben sehen Interessierte schon, bevor sie den Kurs betreten.<br>
[Mehr dazu >](../learningresources/Info_page.de.md)

---

### Lernpfad [:octicons-tag-16:{ title="ab Release 15.0 (OO-4300)" }](https://track.frentix.com/issue/OO-4300) {: #learning_path}

![Werkzeug Lernpfad in der Toolbar markiert, links daneben die Infoseite mit dem Info-Symbol, rechts Kalender, Mitteilungen und die weiteren Werkzeuge](assets/toolbar_learning_path_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Das Werkzeug "Lernpfad" erscheint in Lernpfadkursen.

**Aufruf durch Teilnehmer:innen**<br>
Über das Lernpfad-Icon in der Toolbar erhalten Lernende einen Überblick über ihren Fortschritt in allen Kursbausteinen. Je nach gewählten Spalten können ausserdem zusätzliche Informationen wie die Art der Durchführung und Termine angezeigt werden. So behalten Lernende ihre Aktivitäten im Kurs im Blick.

![Mein Lernpfad mit allen Kursbausteinen des Kurses: je Baustein Fortschritt, Status, Durchführung und Datum erledigt, so sehen Lernende auf einen Blick, was noch offen ist](assets/toolbar_learning_path_table_v1_de.png){ class="shadow lightbox" title="Lernpfad aus Sicht der Teilnehmer:in · 2026.11.10" }

**Aufruf durch Kursbesitzer:innen und Betreuer:innen**<br>
Kursbesitzer:innen und Betreuer:innen erhalten über den Link "Lernpfad" zunächst eine Übersicht über alle Teilnehmenden und können dann im nächsten Schritt eine Person auswählen, um sich ihren Lernfortschritt anzeigen zu lassen.<br>
[Mehr dazu >](Learning_path_course/index.de.md)

---

### Kalender {: #calendar}

![Werkzeug Kalender in der Toolbar markiert, links davon Infoseite und Lernpfad](assets/toolbar_calendar_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Mit dem Werkzeug "Kalender" sehen die Kursmitglieder alle Termine des Kurses an einer zentralen Stelle. Der Kalender öffnet sich in einem eigenen Fenster. Jeder Kurs hat genau einen Kurskalender. Sie zeigen ihn in der Toolbar, als [Kursbaustein "Kalender"](../learningresources/Course_Element_Calendar.de.md) in der Kursstruktur oder an beiden Orten. Beide zeigen dieselben Termine.

Neben dem Kurskalender gibt es in OpenOlat noch weitere Kalender:

- [Persönlicher Kalender >](../personal_menu/Calendar.de.md)
- [Gruppenkalender >](../groups/Using_Group_Tools.de.md)

Einen neuen Termin erstellen Sie mit Klick auf das gewünschte Datum. Danach legen Sie Titel, Beschreibung, Beginn und Ende fest, bei Bedarf auch Ort, Wiederholung und Sichtbarkeit. Der Termin erscheint im Kurskalender und damit überall, wo der Kurs den Kalender zeigt. Um den Termin zu überarbeiten, klicken Sie darauf und wählen "Bearbeiten".

Über "Bearbeiten" erreichen Sie weitere Tabs des Termins und verknüpfen ihn mit Kursbausteinen des Kurses oder mit externen Webseiten. Möchten Sie alle Termine eines Kurskalenders löschen, klicken Sie im Kalenderbereich auf das Zahnradsymbol und wählen "Kalender zurücksetzen".

Den Kurskalender sehen die Kursmitglieder automatisch auch in ihrem persönlichen OpenOlat-Kalender. Gleiches gilt für Gruppenkalender. Bei Gruppenkalendern legen Sie in der Gruppenadministration fest, welche Schreib- und Leserechte die Mitglieder erhalten.

Im Kalender der Toolbar erstellen und bearbeiten Besitzer:innen des Kurses Termine. Betreuer:innen bearbeiten Termine, wenn im Tab "Toolbar" die Option "Betreuer:innen dürfen den Kalender bearbeiten" eingeschaltet ist, siehe [Werkzeuge in Toolbar aktivieren](#activate_tools). So tragen die Betreuer:innen, die die Termine planen, diese selbst ein, ohne dass Sie dafür einen Kursbaustein "Kalender" einfügen. Teilnehmer:innen lesen die Termine. Die Option gilt auch für die Termine des Kurskalenders im [Kursbaustein "Video Livestream"](../learningresources/Course_Element_Video_Livestream.de.md#events). [:octicons-tag-16:{ title="ab Release 21.2 (OO-9968)" }](https://track.frentix.com/issue/OO-9968)

Im Kursbaustein "Kalender" regeln Sie die Rechte getrennt davon: Im Kurseditor legen Sie im Tab "Kalender-Konfiguration" unter "Termine bearbeiten" fest, ob dort auch Betreuer:innen und Teilnehmende Termine bearbeiten. Das ist der Weg für einen Kurs ohne Toolbar.<br>
[Mehr dazu >](../learningresources/Course_Element_Calendar.de.md)

Die Checkbox "Kurskalender" und damit die Option für Betreuer:innen erscheinen, wenn Systemadministrator:innen in der [Core-Konfiguration](../../manual_admin/administration/Core_functions/index.de.md#calendar_administration) den Kalender und die Checkbox "Kurswerkzeug einschalten" eingeschaltet haben. Verwaltet ein externes System den Kalender des Kurses, lässt sich die Option nicht ändern. Beim Kopieren und beim Import eines Kurses übernimmt OpenOlat die Einstellung.

---

### Liste der Teilnehmer:innen [:octicons-tag-16:{ title="ab Release 15.0 (OO-4168)" }](https://track.frentix.com/issue/OO-4168) {: #participant_list}

![Werkzeug Liste der Teilnehmer:innen mit dem Personen-Symbol in der Toolbar markiert, links daneben Infoseite, Lernpfad und Kalender, rechts Mitteilungen und die weiteren Werkzeuge](assets/toolbar_participant_list_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Teilnehmer:in · 2026.10.27" }

Mit dem Werkzeug "Liste der Teilnehmer:innen" sehen die Kursmitglieder, wer im Kurs Besitzer:in, Betreuer:in oder Teilnehmer:in ist, und schreiben diesen Personen über "E-Mail versenden" direkt eine Nachricht. Anders als der gleichnamige Kursbaustein lässt sich das Werkzeug nicht konfigurieren: Es zeigt immer alle drei Rollen.<br>
[Mehr dazu >](../learningresources/Course_Element_Participant_List.de.md)

---

### Mitteilungen {: #notifications}

![Werkzeug Mitteilungen mit dem Megafon-Symbol in der Toolbar markiert](assets/toolbar_notifications_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Mit dem Werkzeug "Mitteilungen" richten Sie eine Ankündigung an den ganzen Kurs, ohne dafür einen Kursbaustein ins Kursmenü zu setzen. Besitzer:innen und Betreuer:innen verfassen die Mitteilungen. Teilnehmende abonnieren das Werkzeug bei Bedarf selbst und werden dann benachrichtigt, wenn eine neue Mitteilung erscheint.

Anders als der Kursbaustein "Mitteilungen" lässt sich das Werkzeug nicht konfigurieren. Anzeige, Berechtigungen, automatisches Abonnieren und Zugang legen Sie nur im Kursbaustein fest. Den Kursbaustein nehmen Sie deshalb, wenn die Mitteilungen an einer bestimmten Stelle im Kursmenü stehen sollen oder wenn Sie diese Einstellungen brauchen.<br>
[Mehr dazu >](../learningresources/Course_Element_Notifications.de.md)

---

### E-Mail {: #email}

![Werkzeug E-Mail mit dem Briefsymbol in der Toolbar markiert](assets/toolbar_email_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Über das Werkzeug "E-Mail" erreichen die Kursmitglieder die E-Mail-Funktion des Kurses mit einem Klick. E-Mails versenden Sie ausserdem über das [persönliche Menü](../personal_menu/E-Mail.de.md).<br>
[Mehr dazu >](../learningresources/Course_Element_EMail.de.md)

---

### BigBlueButton (oder andere virtuelle Klassenzimmer) [:octicons-tag-16:{ title="ab Release 15.4 (OO-5151)" }](https://track.frentix.com/issue/OO-5151) {: #BBB}

![Werkzeug BigBlueButton mit dem Bildschirm-Symbol in der Toolbar markiert, links daneben E-Mail, rechts Blog](assets/toolbar_bbb_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Teilnehmer:in · 2026.10.27" }

Statt über einen Kursbaustein öffnen die Kursmitglieder ein virtuelles Klassenzimmer auch über ein Icon in der Toolbar. Neben BigBlueButton zeigt die Toolbar auch andere eingerichtete Videokonferenz-Tools, etwa Microsoft Teams oder Zoom.<br>
[Mehr dazu >](../learningresources/bigbluebutton/index.de.md)

---

### Blog {: #blog}

![Werkzeug Blog mit dem Blog-Symbol in der Toolbar markiert, links neben Wiki](assets/toolbar_blog_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Bezieht sich ein Blog auf den ganzen Kurs, öffnen ihn die Kursmitglieder über das Icon in der Toolbar. Weitere Blogs binden Sie als Kursbausteine ein.<br>
[Mehr dazu >](../learningresources/Course_Element_Blog.de.md)

---

### Wiki {: #wiki}

![Werkzeug Wiki mit dem Globus-Symbol in der Toolbar markiert, links daneben Blog, rechts Forum](assets/toolbar_wiki_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Gilt ein Wiki für den ganzen Kurs, richten Sie es als zentrales Wiki in der Toolbar ein.<br>
[Mehr zum Erstellen eines Wikis >](../learningresources/Wiki.de.md)<br>
[Mehr zum Kursbaustein Wiki >](../learningresources/Course_Element_Wiki.de.md)

---

### Forum {: #forum}

![Werkzeug Forum mit dem Sprechblasen-Symbol in der Toolbar markiert, links daneben Wiki, rechts Dokumente](assets/toolbar_forum_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Neben dem Kursbaustein "Forum" zeigen Sie bei Bedarf ein zentrales Forum für den ganzen Kurs in der Toolbar. Das bietet sich an, wenn der Kurs nur *ein* Forum umfasst, das permanent zur Verfügung stehen soll. Einstellungen wie Pseudonymisierung oder Moderationsrechte lassen sich hier jedoch nicht festlegen.<br>
[Mehr dazu >](../learningresources/Course_Element_Forum.de.md)

---

### Dokumente {: #documents}

![Werkzeug Dokumente mit dem Ordner-Symbol in der Toolbar markiert, rechts daneben die Kurssuche](assets/toolbar_documents_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Mit dem Werkzeug "Dokumente" stellen Sie wichtige Dokumente des Kurses zentral zum Herunterladen bereit. Die Lernenden können die Dokumente herunterladen, sich benachrichtigen lassen, wenn neue Dokumente bereitstehen (abonnieren) und bei Bedarf die Dateien per Mail versenden. Die Konfigurationsmöglichkeiten sind aber nicht so umfangreich wie beim Kursbaustein "Ordner".<br>
[Mehr dazu >](../learningresources/Storage_folder.de.md)

---

### Termine {: #events}

![Werkzeug Termine mit dem Buch-Symbol in der Toolbar markiert, links daneben Infoseite und Lernpfad, rechts Kurssuche](assets/toolbar_events_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Ist das Termin- und Absenzenmanagement eingeschaltet, öffnen die Kursmitglieder hier die Termine und Absenzen des Kurses.<br>
[Mehr dazu >](../learningresources/Toolbar_Events.de.md)

---

### Glossar {: #glossary}

![Werkzeug Glossar mit dem Doktorhut-Symbol und Auswahlpfeil in der Toolbar markiert, links daneben Dokumente, rechts Kurssuche](assets/toolbar_glossary_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Teilnehmer:in · 2026.10.27" }

Ist ein Glossar mit dem Kurs verbunden, öffnen die Kursmitglieder es auch über die Toolbar. Ein Glossar erklärt die Begriffe eines Kurses, eines Fachs oder einer Veranstaltung. OpenOlat sortiert die Begriffe alphabetisch, mit Klick auf einen Anfangsbuchstaben springen Sie zu den passenden Begriffen.<br>
[Mehr dazu >](Glossary/index.de.md)

---

### Kurs-Chat {: #chat}

![Werkzeug Kurs-Chat mit dem einfachen Sprechblasen-Symbol in der Toolbar markiert, links daneben Dokumente, rechts Kurssuche](assets/toolbar_course_chat_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Teilnehmer:in · 2026.10.27" }

Der Chat ermöglicht den synchronen Austausch unter den Kurs-Mitgliedern.<br>
[Mehr dazu >](../basic_concepts/Chat.de.md)

---

### Kurssuche [:octicons-tag-16:{ title="ab Release 11.3 (OO-2581)" }](https://track.frentix.com/issue/OO-2581) {: #course_search}

![Werkzeug Kurssuche mit dem Lupensymbol in der Toolbar markiert](assets/toolbar_search_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Mit dem Icon in der Toolbar durchsuchen Sie die Inhalte dieses Kurses. Eine Suche, die Sie an anderer Stelle in OpenOlat starten, durchsucht andere Bereiche.<br>
[Mehr dazu >](../basic_concepts/Search_in_Course.de.md)

Rechts neben der Kurssuche stehen die [externen Kurstools](#external_tools), sofern sie eingerichtet sind.

---

### Rolle {: #role}

![Rollenwechsler mit der aktiven Rolle Besitzer:in und der Beschriftung Rolle in der Toolbar markiert, rechts daneben Mein Kurs](assets/toolbar_role_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses · 2026.10.27" }

Hat eine Person in diesem Kurs mehrere Rollen, wechselt sie hier die Rolle.<br>
[Mehr dazu >](../basic_concepts/Roles/index.de.md#course)

---

### Mein Kurs {: #my_course}

![Geöffnetes Menü Mein Kurs mit Leistungsnachweis, To-dos, Notizen, Bookmark und, abgesetzt davon, Kurs verlassen](assets/toolbar_my_course_v2_de.png){ class="shadow lightbox" title="Menü Mein Kurs in der Toolbar, Sicht Teilnehmer:in · 2026.10.27" }

Das Dropdown-Menü "Mein Kurs" der Toolbar bietet Zugriff auf personalisierte Bestandteile des Kurses.<br>
[Mehr dazu >](../learningresources/Toolbar_My_Course.de.md)

---

### Fortschrittsanzeige {: #progress}

![Fortschrittsanzeige als Kreisdiagramm mit 88 Prozent am rechten Rand der Toolbar markiert, links daneben Mein Kurs](assets/toolbar_progress_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses, Sicht Teilnehmer:in · 2026.10.27" }

Kursteilnehmer:innen sehen in Lernpfadkursen hier ihren Bearbeitungsstand in Form eines Kreisdiagramms. Für andere Rollen ist die Fortschrittsanzeige nicht relevant und wird deshalb nicht angezeigt. In herkömmlichen Kursen gibt es keinen Lernpfad, deshalb kann dort auch kein Lernfortschritt berechnet werden. Sie sehen die Fortschrittsanzeige nur, wenn Sie Teilnehmer:in des Kurses sind und der Kurs mindestens einen Kursbaustein enthält, bei dem unter "Durchführung" die Option "Obligatorisch" gewählt ist.<br>
[Mehr dazu >](../learningresources/Creating_learning_path_courses.de.md#konfiguration-zur-berechnung-des-lernfortschritts)

[Zum Seitenanfang ^](#tab_toolbar)

---

## Icons (Tools) anzeigen {: #show_icons}

### Anzeige durch Kursbesitzer:innen [:octicons-tag-16:{ title="ab Release 10.5 (OO-1967)" }](https://track.frentix.com/issue/OO-1967) {: #show_icons_by_owners}

Als Kursbesitzer:in legen Sie unter `Kurs > Administration > Einstellungen > Tab "Toolbar"` fest, ob die Teilnehmer:innen eine Toolbar angezeigt bekommen und, wenn ja, welche Icons (Werkzeuge) in der Toolbar angezeigt werden. Die Checkboxen dafür beschreibt der Abschnitt [Werkzeuge in Toolbar aktivieren](#activate_tools).

![Geöffnetes Menü Administration mit markiertem Eintrag Einstellungen und markiertem Tab Toolbar: der Weg zu den Einstellungen der Toolbar](assets/toolbar_show_icons1_v2_de.png){ class="shadow lightbox" title="Menü Administration eines Kurses · 2026.11.10" }

### Ständig angezeigte Tool-Icons {: #show_icons_permanently}

Einige Icons werden nicht im Tab "Toolbar" geschaltet, sondern in jedem Kurs angezeigt, sobald die Toolbar angezeigt wird. Welche davon eine Person sieht, hängt von ihrer Rolle ab. Dazu gehören:

- [Administration](#admin)
- [Status](#status)
- [Infoseite](#info_page)
- [Lernpfad](#learning_path) (wenn Lernpfadkurs)
- [Rolle](#role)
- [Mein Kurs](#my_course)
- [Fortschrittsanzeige](#progress) (wenn Lernpfadkurs)

### Automatisch angezeigte Tool-Icons {: #show_icons_automatically}

Das Icon "Termine" erscheint automatisch in der Toolbar, sobald das Termin- und Absenzenmanagement für den Kurs eingeschaltet ist.<br>
[Mehr dazu >](../learningresources/Toolbar_Events.de.md)

[Zum Seitenanfang ^](#tab_toolbar)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Wiki erstellen >](Wiki.de.md)<br>
[Blog: Übersicht >](Blog/index.de.md)<br>
[Lernpfadkurs - Überblick >](Learning_path_course/index.de.md)<br>
[Kurs-Administration: Übersicht >](Administration/index.de.md)<br>
[Zugangskonfiguration / Freigabe >](Access_configuration.de.md)<br>
[Toolbar: Infoseite >](Info_page.de.md)<br>
[Kursbaustein "Kalender" >](Course_Element_Calendar.de.md)<br>
[Persönliche Werkzeuge: Kalender >](../personal_menu/Calendar.de.md)<br>
[Gruppenwerkzeuge nutzen >](../groups/Using_Group_Tools.de.md)<br>
[Kursbaustein "Video Livestream" >](Course_Element_Video_Livestream.de.md)<br>
[Core-Konfiguration: Übersicht >](../../manual_admin/administration/Core_functions/index.de.md)<br>
[Kursbaustein "Liste der Teilnehmer:innen" >](Course_Element_Participant_List.de.md)<br>
[Kursbaustein "Mitteilungen" >](Course_Element_Notifications.de.md)<br>
[Persönliche Werkzeuge: E-Mail >](../personal_menu/E-Mail.de.md)<br>
[Kursbaustein "E-Mail" >](Course_Element_EMail.de.md)<br>
[Kursbaustein "BigBlueButton" >](bigbluebutton/index.de.md)<br>
[Kursbaustein "Blog" >](Course_Element_Blog.de.md)<br>
[Kursbaustein "Wiki" >](Course_Element_Wiki.de.md)<br>
[Kursbaustein "Forum" >](Course_Element_Forum.de.md)<br>
[Ablageordner >](Storage_folder.de.md)<br>
[Toolbar: Termine >](Toolbar_Events.de.md)<br>
[Glossar >](Glossary/index.de.md)<br>
[Chat >](../basic_concepts/Chat.de.md)<br>
[Suche in einem Kurs >](../basic_concepts/Search_in_Course.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../basic_concepts/Roles/index.de.md)<br>
[Toolbar: Mein Kurs >](Toolbar_My_Course.de.md)<br>
[Lernpfadkurse erstellen >](Creating_learning_path_courses.de.md)

**Weiterführend**<br>
[Kurseinstellungen >](Course_Settings/index.de.md)<br>
[Kurseinstellungen - Tab Optionen >](Course_Settings_Options.de.md)

[Zum Seitenanfang ^](#tab_toolbar)
