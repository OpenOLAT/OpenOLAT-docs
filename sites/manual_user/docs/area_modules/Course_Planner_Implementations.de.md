# Course Planner: Durchführungen [:octicons-tag-16:{ title="ab Release 20.0 (OO-7834)" }](https://track.frentix.com/issue/OO-7834){:target="_blank"} {: #implementations}

![Der Einstieg zu den Durchführungen, hervorgehoben im Bereich Produkte auf der Startseite des Course Planners, neben Produkte, Termine, To-dos, Reports, Zertifikatsprogramme und Raumverwaltung](assets/course_planner_implementations_v4_de.png){ class="shadow lightbox" } 


## Was ist eine Durchführung? {: #definition}

Ein Bildungsprogramm/Produkt (aus einem oder mehreren Kursen bestehend) kann mehrfach angeboten und durchgeführt werden. Jede Durchführung kann zu einem anderen Termin stattfinden und an jeder Durchführung sind dann andere Teilnehmer:innen dabei.

In einem Bildungsprogramm/Produkt werden zu jeder Durchführung ein oder mehrere Kurse zugeordnet. Der oder die mehrfach verwendeten Kurse sind nur einmal vorhanden.

Soll ein Kurs mehrfach verwendet werden und dabei immer genau gleich bleiben, kann er auch als Template angelegt werden. Die Kurse werden dann für jede Durchführung instanziert (aus der Template-Vorlage erstellt). Diese Instanzierung kann auch automatisiert zu einem bestimmten Termin erfolgen. Z.B. einige Tage vor Beginn einer Durchführung. Bis dahin können die Templatebesitzer:innen noch an der Fertigstellung der Template-Kurse arbeiten. Das Organisatorische zur Durchführung (Termin, Katalogangebot, usw.) kann aber mit dem Course Planner bereits vorbereitet sein.

Von dieser Konzeptidee her, werden in der Regel in jeder Durchführung die gleichen Kurse zugeordnet und verwendet. Es ist aber in OpenOlat auch möglich, die Inhalte in jeder Durchführung anzupassen.

[zum Seitenanfang ^](#implementations)

---


## Die Liste der Durchführungen {: #listing}

Haben Sie in der Übersicht des Course Planners den Button "Durchführungen" gewählt, gelangen Sie zunächst zu einer Liste aller Durchführungen dieses Produkts. Sie können mit Filtern die Auswahl eingrenzen.

![Alle Durchführungen eines Produkts in einer filterbaren Liste mit Kennzeichen, Typ und Status, hier mit geöffnetem Filter Belegungsstatus, auf der Seite Durchführungen im Course Planner](assets/course_planner_implementations_list_v1_de.png){ class="shadow lightbox" }  

Mit **Filter speichern** können häufig verwendete Filterkombinationen als eigene Voreinstellung gespeichert und wiederverwendet werden. [:octicons-tag-16:{ title="ab Release 20.3 (OO-9223)" }](https://track.frentix.com/issue/OO-9223){:target="_blank"}

![Die Aktion Filter speichern im Menü rechts über der Tabelle, mit der eine Filterkombination als eigene Voreinstellung erhalten bleibt, auf der Seite Durchführungen im Course Planner](assets/course_planner_implementations_list_filter_v1_de.png){ class="shadow lightbox" }  

Über die individuelle Spaltenauswahl lassen sich zusätzlich die standardmässig ausgeblendeten Spalten **Fachbereiche** und **Fachbereich Pfade** einblenden (zwischen den Spalten "Status" und "Kalender"). [:octicons-tag-16:{ title="ab Release 20.3.1 (OO-9392)" }](https://track.frentix.com/issue/OO-9392){:target="_blank"}

!!! info "Wichtig"
    Die Fachbereiche werden in der System-Administration zur Verfügung gestellt, unter `Administration > Module > Taxonomie`.

### Sammelaktion «Typ ändern» [:octicons-tag-16:{ title="ab Release 21.0 (OO-9583)" }](https://track.frentix.com/issue/OO-9583){:target="_blank"} {: #change_type}

Durch Aktivieren der Checkbox in der ersten Spalte markieren Sie mehrere Durchführungen. Oberhalb der Tabelle erscheint dann die Aktion **«Typ ändern»**. Im Dialog wählen Sie den neuen Elementtyp und bestätigen mit **«Typ ändern»**. Zur Wahl stehen nur Typen, die zu den markierten Elementen passen.

Dieselbe Aktion steht in der Suche des Course Planners und im Tab «Struktur» einer Durchführung zur Verfügung.

![Drei markierte Durchführungen mit der eingeblendeten Aktion «Typ ändern» und dem Dialog zur Auswahl des neuen Elementtyps, in der Durchführungsübersicht des Course Planners](assets/course_planner_implementations_change_type_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#implementations)

---

## Navigation in den Durchführungen [:octicons-tag-16:{ title="ab Release 20.0 (OO-8128)" }](https://track.frentix.com/issue/OO-8128){:target="_blank"} {: #navigation}

Haben Sie in der Liste eine Durchführung gewählt und geöffnet, lassen sich in den angezeigten Tabs alle Einstellungen zu dieser Durchführung vornehmen:

- rechts oben durch Klick auf den Button "**Gehe zu**" innerhalb der aktuellen Durchführung zu einem Element springen.

- mit den **Pfeiltasten** rechts oben zu anderen Durchführungen  wechseln.

- durch Klick auf die verschiedenen **Tabs** diese Durchführung konfigurieren.

- durch Klick auf eine der **Überschriften** direkt zum entsprechenden Tab springen.



![Die Wege durch eine Durchführung: Button Gehe zu, Pfeiltasten zum Wechsel zwischen Durchführungen und die Tabs von Übersicht bis Reports, im Kopfbereich einer geöffneten Durchführung](assets/course_planner_implementations_navigation_v2_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#implementations)


---






### Tab Übersicht [:octicons-tag-16:{ title="ab Release 20.2 (OO-8953)" }](https://track.frentix.com/issue/OO-8953){:target="_blank"} {: #tab_overview}

Im Tab "Übersicht" werden Ihnen die Mitglieder, die nächsten Termine, die Angebote im Katalog und Kursinhalte dieses Produkts angezeigt. Dies erleichtert Ihnen die Navigation innerhalb der Durchführungsbezogenen Aktivitäten.

Über den Button **Alle anzeigen** im Widget **Termine** gelangen Sie direkt zum Tab Termine.

Die Widgets **Kursinhalt** und **Katalog** zeigen zusätzlich ein Icon im Titel sowie den Button **Details** [:octicons-tag-16:{ title="ab Release 20.3 (OO-9244)" }](https://track.frentix.com/issue/OO-9244){:target="_blank"}, über den Sie direkt zum Tab Kursinhalt bzw. zum Tab Katalog gelangen.

![Die Widgets für Termine, Kursinhalt, Mitglieder und Katalog mit den Buttons Alle anzeigen und Details, im Tab Übersicht einer Durchführung](assets/course_planner_implementations_tab_overview_v2_de.png){ class="shadow lightbox" }

#### Mitglieder-Widget [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9243)" }](https://track.frentix.com/issue/OO-9243){:target="_blank"} {: #widget_members}

Das Widget **Mitglieder** zeigt die Kennzahl **"Teilnehmer:innen"** dieser Durchführung, aufgeschlüsselt nach **"Aktiv"** und **"Ausstehend"**. Sind noch keine Kursverantwortlichen erfasst, zeigt das Widget den Hinweis "Noch keine Kursverantwortlichen." Über den Button **"Details"** gelangen Sie direkt zum Tab Mitglieder dieser Durchführung. [:octicons-tag-16:{ title="ab Release 21.0 (OO-9405)" }](https://track.frentix.com/issue/OO-9405){:target="_blank"}

![Die Kennzahl Teilnehmer:innen mit Aktiv und Ausstehend sowie der Hinweis Noch keine Kursverantwortlichen, im Mitglieder-Widget im Tab Übersicht einer Durchführung](assets/course_planner_implementations_widget_members_v1_de.png){ class="shadow lightbox" }

Sind Kursverantwortliche erfasst, erscheinen sie anstelle des Hinweises mit ihrer Rolle (z.B. Betreuer:innen, Klassenlehrer:innen, Kursbesitzer:innen, Elementbesitzer:innen).

Ist eine maximale bzw. minimale Teilnehmerzahl definiert, ergänzt ein zusätzlicher Hinweistext die Kennzahl "Teilnehmer:innen":

* Bei gesetztem Maximum: **"\<Anzahl\> verbleibende Plätze"**
* Bei gesetztem Minimum: **"\<Anzahl\> bis Mindestanzahl"**
* Bei ausgebuchten oder überbuchten Durchführungen erscheint die entsprechende Meldung.

![Verbleibende Plätze und Abstand zur Mindestanzahl unter der Teilnehmerzahl, dazu die Kursverantwortlichen mit ihren Rollen, im Mitglieder-Widget im Tab Übersicht](assets/course_planner_implementations_widget_members2_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#implementations)

---


### Tab Struktur [:octicons-tag-16:{ title="ab Release 20.0 (OO-8634)" }](https://track.frentix.com/issue/OO-8634){:target="_blank"} {: #tab_structure}

Wenn es sich um eine strukturierte Durchführung handelt (der Typ wird beim Erstellen einer neuen Durchführung ausgewählt) wird das Tab "Struktur" angezeigt.
In der angezeigten Baumstruktur kann jedes einzelne Element der Durchführung bearbeitet werden, bzw. es können Informationen dazu abgefragt werden.

![Die Baumstruktur der Elemente mit dem geöffneten Menü Erstellen und den Spalten Ref., #Teilnehmer:innen und Status, im Tab Struktur einer Durchführung](assets/course_planner_implementations_tab_structure1_v1_de.png){ class="shadow lightbox" }

![1](assets/1_green_24.png) Möchten Sie für diese Durchführung abweichend von der Produkt-Struktur ("Kopiervorlage" dieser Struktur) andere Elemente hinzufügen, finden Sie unter dem Button **Erstellen** die verfügbaren Element-Typen, wie sie in der System-Administration unter `Administration > Module > Course Planner > Tab Elementtypen` definiert wurden. 

![2](assets/2_green_24.png) Mit dem **Download-Button** können Sie die angezeigte Struktur auch als Excel-Datei herunterladen. 

![3](assets/3_green_24.png) In der Spalte **Ref.** können Sie die in diesem Element referenzierten Inhalte anzeigen lassen; der Detailbereich heisst "Referenzierte Kurse".

![4](assets/4_green_24.png) In dieser Spalte finden Sie die **Stundenpläne** der jeweiligen Elemente. 

![5](assets/5_green_24.png) In dieser Spalte finden Sie die **Absenzen**. (Vorausgesetzt, das Absenzenmanagement ist aktiviert.) 

![6](assets/6_green_24.png) Wurde das Modul "Qualitätsmanagement" aktiviert, können Sie bei jedem Element zur zugeordneten **Datenerhebungsvorschau** springen.

![7](assets/7_green_24.png) In der Spalte **Lernfortschritt** wird der durchschnittliche Fortschritt aller Teilnehmer:innen angezeigt. Berücksichtigt werden dabei alle Lernpfadkurse dieses Elements. (Herkömmliche Kurse liefern keine Daten zum Lernfortschritt.)

![8](assets/8_green_24.png) Unter den **3 Punkten** finden Sie Optionen zum Bearbeiten der Elemente.

![Die Aktionen am Element: In neuem Tab öffnen, Bearbeiten, Neues Unterelement erstellen, Element kopieren, Mitgliederverwaltung und Löschen, im Menü der drei Punkte im Tab Struktur](assets/course_planner_implementations_tab_structure2_v1_de.png){ class="shadow lightbox" }

#### Ein Element verschieben [:octicons-tag-16:{ title="ab Release 20.3 (OO-8841)" }](https://track.frentix.com/issue/OO-8841){:target="_blank"}

Über die Aktion **Element verschieben** unter den **3 Punkten** öffnen Sie den Verschiebe-Dialog. Das zu verschiebende Element ist darin farblich hervorgehoben.

Jede mögliche Zielposition wird als Radiobutton angezeigt. Nicht erlaubte Zielpositionen (z. B. ein nicht kompatibler Elementtyp) sind ausgegraut und nicht auswählbar.

Nach der Auswahl einer Zielposition erscheinen direkt am Element die Aktionen:

* **Oben**
* **Unten**
* **Unterelement**

Mit einem Klick auf **Element verschieben** wird die Verschiebung ausgeführt.

![Die möglichen Zielpositionen als Radiobuttons mit den Aktionen Oben, Unten und Unterelement, das zu verschiebende Element farbig hervorgehoben, im Dialog Element verschieben](assets/course_planner_implementations_move_element_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#implementations)

---


### Tab Kursinhalt {: #tab_content}

Die Liste zeigt alle zu dieser Durchführung gehörenden Kurse.

Sollen für diese Durchführung (abweichend von der ursprünglichen Struktur) weitere Kurse hinzugefügt werden, verwenden Sie den Button "**Kurs hinzufügen**" rechts oben.

Die Option zum **Entfernen** eines **einzelnen Kurses** aus dieser Durchführung finden Sie unter den 3 Punkten am Ende einer Zeile.<br>
Für das **Entfernen mehrerer Kurse** markieren Sie die Kurse mit den Checkboxen der ersten Spalte. Dann wird Ihnen ein Button zum Entfernen über der Liste angezeigt.

![Die Kurse einer Durchführung mit Freigabe, Erstellerin und Status, dazu die Buttons Kurs hinzufügen und Entfernen für markierte Zeilen, im Tab Kursinhalt einer Durchführung](assets/course_planner_implementations_tab_content_v1_de.png){ class="shadow lightbox" }

<br>

**Automatisch gesteuerte Kursinhalte** [:octicons-tag-16:{ title="ab Release 21.0 (OO-9578)" }](https://track.frentix.com/issue/OO-9578){:target="_blank"}<br>
Steuern Automatisierungsregeln den Inhalt dieser Durchführung, erscheint oberhalb der Liste der Abschnitt «Übersicht Automatisierung». Aufgeführt sind nur aktive Regeln, die den Inhalt betreffen. Zu jeder Regel sehen Sie die Art der Regel, also «Instanziierung» oder den Zielstatus, dazu das Datum der geplanten Ausführung und die Bedingung, die die Ausführung auslöst. Über den Link «Einstellungen» wechseln Sie direkt zur [Konfiguration der Automatisierung](#tab_settings_automation).

![Die Infobox Übersicht Automatisierung mit Art, geplantem Ausführungsdatum und auslösender Bedingung je Regel sowie dem Link Einstellungen, im Tab Kursinhalt einer Durchführung](assets/course_planner_implementations_tab_content_automation_v1_de.png){ class="shadow lightbox" }

<br>

**Kurstemplates als Kursinhalt**<br>
Wenn es dem gewählten Durchführungstyp (Einzelkurs erforderlich) entspricht, besteht die Möglichkeit auch ein Kurstemplate hinzuzufügen, das zu einem späteren Zeitpunkt instanziert werden kann. Das heisst, zum Zeitpunkt der Planung im Course Planner ist ein Kurs nur angekündigt, aber noch nicht hinzugefügt. Erst wenn die Kursdurchführung tatsächlich stattfindet, weil z.B. genügend Buchungsaufträge vorhanden sind, wird der Kurs der Durchführung hinzugefügt (instanziert). 

Die Verwendung eines Templates zur Instanzierung empfiehlt sich, wenn es sich um einen immer wiederkehrenden gleichen Kurs handelt.

![Der Abschnitt Kurstemplate mit dem Button Kurstemplate hinzufügen unterhalb der noch leeren Kursliste, im Tab Kursinhalt einer Durchführung vom Typ Einzelkurs](assets/course_planner_implementations_tab_content_template1_v1_de.png){ class="shadow lightbox" }

Die Buttons "Kurs hinzufügen" und "Kurstemplates hinzufügen" werden inaktiv, sobald die Anzahl Kurse oder Templates hinzugefügt ist, die dem gewählten Durchführungstyp entsprechen.

**Erstellung von Kurstemplates**<br>
Kurstemplates werden erstellt, indem im Kurs unter `Kurs > Administration > Einstellungen > Freigabe > Verwendungszweck` die Option "Template" gewählt wird. 
Die Templates für Kursinhalte im Course Planner sind ohne eigenständige Mitgliederverwaltung, da die Mitglieder für jede Durchführung im Course Planner hinzugefügt werden.


!!! info "Wichtig"

    Templates werden kopiert. Bei späterer Änderung des Templates bleibt die früher erstellte Kopie unverändert.

[zum Seitenanfang ^](#implementations)

---


### Tab Termine [:octicons-tag-16:{ title="ab Release 20.0 (OO-8064)" }](https://track.frentix.com/issue/OO-8064){:target="_blank"} {: #tab_events}

- Bestehen viele Termine, sind die **Filter** oberhalb der Tabelle nützlich um den Überblick zu behalten.
- Mit dem **Button "Termin hinzufügen"** lassen sich neue Termine zur aktuell gewählten Durchführung hinzufügen.
- Ein Klick auf das **+** am Anfang einer Zeile zeigt die **Details** dieses Termins.
- Es besteht auch die Möglichkeit, Termine zu **importieren**. Klicken Sie dazu auf den kleinen Pfeil neben dem Button "Termin hinzufügen".

![Die Termine einer Durchführung mit Datum, Zeit, Einheiten und Dozierenden, den Umschaltern Alle Ebenen und Diese Ebene und dem Button Termin hinzufügen, im Tab Termine](assets/course_planner_implementations_tab_events_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#implementations)

---


### Tab Mitglieder [:octicons-tag-16:{ title="ab Release 20.3 (OO-8514)" }](https://track.frentix.com/issue/OO-8514){:target="_blank"} {: #tab_members}

![Die Mitglieder einer Durchführung nach Rollen gefiltert, mit den Ansichten Aktiv, Ausstehend, Nichtmitglieder und Mitglieder-Historie, im Tab Mitglieder](assets/course_planner_implementations_tab_members_v1_de.png){ class="shadow lightbox" }

Wie bereits weiter oben erwähnt, kann ein Bildungsprodukt (aus einem oder mehreren Kursen bestehend) mehrfach durchgeführt werden. An jeder Durchführung sind andere Teilnehmer:innen dabei.

Deshalb werden Teilnehmer:innen zu Mitgliedern einer bestimmten Durchführung gemacht (nicht zu Mitgliedern einzelner Kurse oder eines Bildungsprodukts). Es kann bestimmt werden, ob sie Mitglieder der gesamten Durchführung oder nur eines Teilbereiches werden.

Die Spalte **"Teilnehmer:inkommentar"** der Mitgliederliste zeigt mit einem Notiz-Symbol, ob zur Buchung ein Kommentar der Teilnehmer:in vorliegt; ein Klick darauf öffnet den Kommentar. Dieselbe Spalte führt die Tabelle der Buchungsaufträge im Tab Katalog [:octicons-tag-16:{ title="ab Release 21.1.0 (OO-9484)" }](https://track.frentix.com/issue/OO-9484){:target="_blank"}.

Würden die Teilnehmer:innen zu Mitgliedern des Bildungsprodukts (der "Kopiervorlage") gemacht, wären sie in allen Durchführungen dieses Produkts als Teilnehmer:innen dabei. Dies ist nicht erwünscht. Deshalb können zu einem Produkt nur Besitzer:innen als Mitglieder hinzugefügt werden, keine Teilnehmer:innen.

!!! info "Mitgliederverwaltung im Course Planner"
    Weil die Mitgliederverwaltung bei Verwendung des Course Planners in der Durchführung gemacht wird, gibt es in den Einstellungen der Kurse den Verwendungszweck "Verwendung im Course Planner":<br>
    `Kurs > Administration > Einstellungen > Tab Freigabe > Abschnitt Verwendung`

**Der Kurs hat dann *keine* eigenständige Mitgliederverwaltung mehr**, die Mitgliederverwaltung erfolgt nun ausschliesslich in der Mitgliederverwaltung der Durchführung, **innerhalb des Course Planners**.

<br>

#### Tab Mitglieder > Mitglieder hinzufügen {: #add_members}


Um Teilnehmer:innen zu einer Durchführung als Mitglieder hinzuzufügen, verwenden Sie:<br>
`Course Planner > Durchführungen > "Ihre Durchführung" > Tab Mitglieder > Button "Teilnehmer:innen hinzufügen"`

![Der Button Teilnehmer:innen hinzufügen rechts über der Mitgliederliste, mit dem der Assistent zur Aufnahme startet, im Tab Mitglieder einer Durchführung](assets/course_planner_implementations_add_member_v1_de.png){ class="shadow lightbox" }

<br>

#### Tab Mitglieder > Einladung und Mitgliedschaftsanfragen [:octicons-tag-16:{ title="ab Release 20.3 (OO-9156)" }](https://track.frentix.com/issue/OO-9156){:target="_blank"} {: #invitation_flow}

Wenn Teilnehmer:innen einer Durchführung zugewiesen werden, erhalten sie je nach Kontext eine Systembenachrichtigung per E-Mail:

- Zuweisung zu einem **Kurs**: Benachrichtigung mit Link in den Kursbereich
- Zuweisung zu einem **Bildungsprodukt**: Benachrichtigung mit Link in den Kursbereich
- Zuweisung zu einer **Gruppe**: Benachrichtigung mit Link in den Gruppenbereich

Im Kursbereich, im Gruppenbereich sowie direkt auf der Kurs- oder Bildungsprodukt-Info-Seite erscheint die Hinweisbox **"Anfragen zur Mitgliedschaft akzeptieren"**. Teilnehmer:innen können die Anfrage dort annehmen oder ablehnen. Eine Annahme ist an allen drei Stellen gleichermassen möglich.

![Die Hinweisbox Anfragen zur Mitgliedschaft akzeptieren mit den Aktionen Details, Akzeptieren und Ablehnen, wie sie eingeladene Personen im Kursbereich vorfinden](assets/course_planner_implementations_accept_membership_v1_de.png){ class="shadow lightbox" }

!!! info "Wichtig"

    Ob eine Bestätigung durch die eingeladenen Personen erforderlich ist, hängt von der Konfiguration der Reservierungspflicht ab. Details dazu finden Sie im Abschnitt zur Bestätigung der Mitgliedschaft weiter unten.

Für Administrator:innen: [Systemweite Konfiguration der Einladung >](../../manual_admin/administration/Modules_Groups.de.md#accept_membership)

<br>

#### Tab Mitglieder > Bestätigung der Mitgliedschaft durch Linienvorgesetzte/Ausbildungsverantwortliche {: #confirm_membership}


Im Course Planner kann eingerichtet werden, dass ein Buchungswunsch von einer administrativen Rolle (z.B. Linienvorgesetzte:r oder Ausbildungsverantwortliche:r) bestätigt werden muss. Mit dieser Einstellung können Teilnehmende einen Kurs buchen; die vorgesetzte Person muss die Buchung aber in einem Zwischenschritt bestätigen oder ablehnen.

Dieser Genehmigungsschritt kann auch in allen Angeboten eingerichtet werden, ausser bei Bezahlung mit Paypal (denn dort wird sofort bezahlt/gebucht).

![Die Wahl zwischen Standard und Mit Bestätigung, dazu Bestätigung durch administrative Rollen und die Frist, im Schritt Mitgliedschaft des Assistenten Teilnehmer:innen hinzufügen](assets/course_planner_implementations_confirm_member_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#implementations)

---


### Tab Katalog [:octicons-tag-16:{ title="ab Release 20.0 (OO-8236)" }](https://track.frentix.com/issue/OO-8236){:target="_blank"} {: #tab_catalog}

Die verschiedenen Durchführungen können im Katalog angeboten werden. Dazu muss ein [Angebot](../../manual_user/area_modules/catalog2.0_angebote.de.md) erstellt werden, wie zu jedem Katalogeintrag.


![Die Angebote einer Durchführung mit dem Button Angebot hinzufügen und den Angebotsarten Zugangscode, Frei verfügbar, PayPal Checkout und Rechnung, im Tab Katalog](assets/course_planner_implementations_tab_catalog1_v1_de.png){ class="shadow lightbox" }

Um potenzielle Teilnehmer:innen auf ein Angebot im Katalog aufmerksam zu machen, können Sie einen Direktlink auf das Angebot z.B. in einer Mail verschicken. Sie finden die Links in der Übersicht der Angebote (je Durchführung im Tab Katalog).

![Die Direktlinks auf das Angebot für externen und internen Katalog, geöffnet über Zugang und Links in der Angebotsübersicht, im Tab Katalog einer Durchführung](assets/course_planner_implementations_tab_catalog3_v1_de.png){ class="shadow lightbox" }

Wurden im Katalog Angebote mit Buchungsmöglichkeit ergänzt, sind die Buchungsaufträge und ihre Details ebenfalls unter dem Tab "Katalog" im Teilbereich "Buchungsaufträge" zu finden.  

![Die Buchungsaufträge mit Status, Angebotstyp, Preis und Rechnungsadresse, dazu der Download der Liste und die Aktionen je Auftrag, im Teilbereich Buchungsaufträge im Tab Katalog](assets/course_planner_implementations_tab_catalog2_v1_de.png){ class="shadow lightbox" }



[zum Seitenanfang ^](#implementations)

---


### Tab Einstellungen {: #tab_settings}

Die Vielzahl der möglichen Einstellungen zu einer Durchführung sind unter mehreren untergeordneten Tabs zu finden. Permanent ist eine Vorschau-Info-Seite verfügbar.

![Die Unter-Tabs der Einstellungen von Metadaten bis Optionen und der Button Vorschau Info-Seite, im Tab Einstellungen einer Durchführung](assets/course_planner_implementations_tab_settings_v2_de.png){ class="shadow lightbox" }

#### Metadaten der Einstellungen

Die hier eingegebenen Metadaten werden verwendet um z.B. Suchprozesse zu vereinfachen.

![Die Pflichtfelder Titel, Kennzeichen und Typ sowie Durchführungsformat und Fachbereiche, im Unter-Tab Metadaten der Einstellungen einer Durchführung](assets/course_planner_implementations_tab_settings_metadata_v1_de.png){ class="shadow lightbox" }


#### Infos in den Einstellungen

Die im Tab "Infos" gemachten Angaben werden z.B. für die Anzeige im Katalog verwendet.

![Die Angaben für die Informationsseite: Teaser, Titelbild, Beschreibung, Lernziele, Voraussetzungen und Zeitaufwand, im Unter-Tab Infos der Einstellungen](assets/course_planner_implementations_tab_settings_infos_v1_de.png){ class="shadow lightbox" }

#### Durchführung in den Einstellungen

Zu den Einstellungen der Durchführung gehören der Durchführungszeitraum, der Ort und die Anzahl der Teilnehmer:innen.

![Durchführungszeitraum, Durchführungsort und die Mindest- und Maximalzahl der Teilnehmer:innen, im Unter-Tab Durchführung der Einstellungen](assets/course_planner_implementations_tab_settings_execution_v1_de.png){ class="shadow lightbox" }


#### Automatisierung konfigurieren [:octicons-tag-16:{ title="ab Release 21.0 (OO-9578)" }](https://track.frentix.com/issue/OO-9578){:target="_blank"} {: #tab_settings_automation}

Im Unterabschnitt **«Automatisierung»** der Tab-Einstellungen legen Sie fest, wann Kurse automatisch [instanziert](#tab_content) und wann Statuswechsel automatisch ausgelöst werden.

Der Unterabschnitt erscheint bei Elementen, deren Elementtyp die Verwendung «Durchführung» oder «Element» hat. Bei der Verwendung «Durchführung oder Element (legacy)» fehlt er.

Soll ein Kurs mehrfach und dabei immer genau gleich verwendet werden, kann er als Template angelegt werden. Die Kurse werden dann für jede Durchführung aus der Template-Vorlage erstellt. Die [Instanzierung](#tab_content) kann automatisiert zu einem bestimmten Zeitpunkt sowie rollenspezifisch erfolgen, z.B. einige Tage vor Beginn einer Durchführung zugänglich für Betreuer:innen. Bis dahin können die Templatebesitzer:innen noch am Template arbeiten, während die organisatorische Planung im Course Planner bereits läuft.

**Geltungsbereich der Automatisierungsregeln:**

Automatisierungsregeln werden auf zwei Ebenen definiert:

* **Elementtyp-Ebene** in der System-Administration unter `Administration > Module > Course Planner > Tab Elementtypen`: Administrator:innen hinterlegen Standardregeln für jeden Elementtyp. Diese Regeln gelten als Vorlage für alle Elemente dieses Typs.
* **Element-Ebene** `Tab Einstellungen > Automatisierung`: Für jedes einzelne Element entscheiden Sie, ob die Regeln des Elementtyps übernommen oder individuell überschrieben werden sollen.

Für das einzelne Element stehen zwei Modi zur Wahl:

* **«Vom Typ "Elementtyp" übernehmen»**: Das Element verwendet die Standardregeln des Elementtyps. Die Beschriftung nennt den Namen des Typs und ob dort Regeln aktiv sind. Passen Administrator:innen die Vorlage an, wirkt sich das automatisch auf alle Elemente aus, die diesen Modus verwenden.
* **«Überschreiben»**: Das Element verwendet abweichende, individuell konfigurierte Regeln, unabhängig vom Elementtyp.

**Typen von Automatisierungsregeln:**

| Typ | Auslöser |
|---|---|
| Bei Statuswechsel | Eine Aktion wird ausgelöst, sobald der Durchführungs- oder Elementstatus einen bestimmten Wert annimmt. |
| Zeitgesteuert | Eine Aktion wird relativ zum Beginn oder Ende des Durchführungszeitraums ausgelöst. |

**Ausführung der Regeln:**

Aktivierte Automatisierungen laufen einmal täglich zu einer festen Uhrzeit. Die Uhrzeit nennt der Informationstext oberhalb der Konfiguration.

Sobald mindestens eine Regel aktiv ist, zeigt der Kopfbereich der Durchführung oberhalb der Tabs unter «Automatisierung» das Datum der nächsten Ausführung. Steht keine Ausführung mehr an, erscheint dort ein Strich.

![Der Modus Überschreiben und die Regeltabelle mit Kontext, Automatisierung, Zielstatus, Bedingung und geplanter Ausführung, im Unter-Tab Automatisierung der Einstellungen einer Durchführung](assets/course_planner_implementations_tab_settings_automation_v3_de.png){ class="shadow lightbox" }

[Zu den Elementtypen und Automatisierungsregeln (Admin) >](../../manual_admin/administration/Modules_Course_Planner.de.md#tab_element_types)<br>
[Zu den To-dos auf CPL-Elementen >](Course_Planner_Todos.de.md)


#### Bewertung in den Einstellungen [:octicons-tag-16:{ title="ab Release 21.0 (OO-9499)" }](https://track.frentix.com/issue/OO-9499){:target="_blank"} {: #tab_settings_assessment}

Der Unter-Tab "Bewertung" wird bei Durchführungen vom Typ Einzelkurs angezeigt sowie bei jeder Durchführung, die bereits einem Zertifikatsprogramm zugeordnet ist. Hier verknüpfen Sie die Durchführung direkt mit einem Zertifikatsprogramm, ohne den Weg über das Programm selbst zu gehen.

* Mit dem Schalter **"Zertifikatsprogramm"** aktivieren oder deaktivieren Sie die Verknüpfung.
* Ist noch kein Programm verknüpft, wählen Sie über die Aktion **"Auswählen"** ein Programm aus. Der Dialog "Zertifikatsprogramm auswählen" zeigt Titel, Bezeichnung, Gültigkeitsdauer, Rezertifizierung und benötigte Kreditpunkte. Angezeigt werden nur Programme, auf die Sie Zugriff haben.
* Ist ein Programm verknüpft, zeigt ein Panel den Programmtitel. Gültigkeitsdauer, Rezertifizierung und benötigte Kreditpunkte erscheinen dort, sofern sie am Programm hinterlegt sind. Von dort öffnen Sie das Programm in einem neuen Tab (sofern Sie Zugriff auf das Programm haben) oder heben mit **"Entfernen"** die Verknüpfung auf; die Sicherheitsabfrage "Zertifikatsprogramm entfernen" bestätigt den Schritt. Das Entfernen erfordert die Rolle Kursplaner:in oder Produktbesitzer:in und muss bestätigt werden. Teilnehmer:innen, die bereits ein Zertifikat erhalten haben, bleiben Mitglieder des Programms.

![Der Schalter Zertifikatsprogramm und der Button Auswählen, solange kein Programm verknüpft ist, im Unter-Tab Bewertung der Einstellungen einer Durchführung](assets/course_planner_implementations_tab_settings_assessment_v1_de.png){ class="shadow lightbox" }

![Die Programmliste mit Bezeichnung, Gültigkeitsdauer, Rezertifizierung und benötigten Kreditpunkten, im Dialog Zertifikatsprogramm auswählen](assets/course_planner_implementations_tab_settings_assessment_select_v1_de.png){ class="shadow lightbox" }

![Das verknüpfte Programm mit den Aktionen Entfernen und Öffnen, angezeigt bei eingeschaltetem Schalter Zertifikatsprogramm, im Unter-Tab Bewertung der Einstellungen](assets/course_planner_implementations_tab_settings_assessment_linked_v1_de.png){ class="shadow lightbox" }

Eine Durchführung kann auch direkt über das [Zertifikatsprogramm](Course_Planner_Certification_Programs.de.md#config_tab_implementations) hinzugefügt werden.

Beim [Kopieren einer Durchführung](#copy) wird die Verknüpfung zum Zertifikatsprogramm übernommen, sofern Sie die Berechtigung für das Programm besitzen. Fehlt die Berechtigung, zeigt der Assistent die Warnung "Das Zertifizierungsprogramm kann aufgrund fehlender Berechtigungen nicht übernommen werden." Beim Kopieren entsteht ein Eintrag im Aktivitätslog des Programms.


#### Optionen in den Einstellungen

Für jede Durchführung können hier separat Einstellungen vorgenommen werden für: 

- Kalenderkonfiguration
- Stundenplan
- Absenzenkonfiguration
- Absenzenmanagement
- Fortschrittskonfiguration

![Kalender-, Absenzen- und Fortschrittskonfiguration je Element übernommen oder überschrieben, dazu die Schalter Stundenplan und Absenzmanagement, im Unter-Tab Optionen](assets/course_planner_implementations_tab_settings_options_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#implementations)

---


### Tab Absenzen [:octicons-tag-16:{ title="ab Release 20.0 (OO-8442)" }](https://track.frentix.com/issue/OO-8442){:target="_blank"} {: #tab_absences}

Dieser Tab erscheint nur, wenn auf dem Element die Absenzen aktiviert wurden.

Die Aktivierung erfolgt in den Einstellungen der Durchführung: `Tab Einstellungen > Optionen > Absenzenkonfiguration`.

![Anwesenheiten und Absenzen der Teilnehmenden mit Einheiten, entschuldigten und unentschuldigten Abwesenheiten und Anwesenheitsquote, im Tab Absenzen einer Durchführung](assets/course_planner_implementations_tab_absences_v1_de.png){ class="shadow lightbox" }


[zum Seitenanfang ^](#implementations)

---


### Tab Reports [:octicons-tag-16:{ title="ab Release 20.0 (OO-8387)" }](https://track.frentix.com/issue/OO-8387){:target="_blank"} {: #tab_reports}

Die hier erstellbaren Reports beziehen sich auf die aktuell gewählte Durchführung.

Im Unterschied dazu bezieht sich die Report-Erstellung, die in der [Übersicht](../../manual_user/area_modules/Course_Planner_Reports.de.md) aufgerufen werden kann, auf **alle** Durchführungen. 
Die Struktur der Excel-Dateien (Spalten) und das Vorgehen zum Erstellen ist bei beiden identisch.

![Die Reportvorlagen mit Kategorie, Beschreibung und Typ, die Spalte Ausführen und darunter die erzeugten Excel-Dateien mit Download, im Tab Reports einer Durchführung](assets/course_planner_implementations_tab_reports1_v1_de.png){ class="shadow lightbox" }


Durch Klick auf die **Pfeile in der Spalte "Ausführen"** werden anhand der aufgelisteten Vorlagen Excel-Dateien mit den aktuellen Daten erzeugt.

Die so erstellten Excel-Dateien finden Sie dann im unteren Bereich des Screens aufgeführt. Sie können kopiert und heruntergeladen werden.


[zum Seitenanfang ^](#implementations)

---

## Kopieren einer Durchführung [:octicons-tag-16:{ title="ab Release 20.0 (OO-8418)" }](https://track.frentix.com/issue/OO-8418){:target="_blank"} {: #copy}

Die Aktion **"Element kopieren"** finden Sie in der Liste der Durchführungen am Ende einer Zeile unter den 3 Punkten.

![Die Aktion Element kopieren im Menü der drei Punkte am Ende einer Zeile, mit der der Kopier-Assistent startet, in der Liste der Durchführungen](assets/course_planner_implementations_copy1_v1_de.png){ class="shadow lightbox" } 

Im ersten Schritt des kleinen Wizards kann gewählt werden, ob auch Kursinhalte, Termine, Mitglieder, To-dos und Raumbuchungen kopiert werden sollen.

![Titel und Kennzeichen der Kopie sowie die Optionen für Kursinhalt, eigenständige Termine, To-dos und Mitgliedschaften, im Schritt Allgemeine Einstellungen des Assistenten Element kopieren](assets/course_planner_implementations_copy2_v2_de.png){ class="shadow lightbox" }  

Der zweite Schritt des Wizards zeigt Ihnen eine Übersicht der Elemente, die nun kopiert werden.<br>
Sie können hier noch Anpassungen (insbesondere der Termine) vornehmen.<br>
Durch Klick auf das + vor einem Element zeigen Sie die Kurse und Termine des Elements an.

![Die zu kopierenden Elemente mit Beginn, Ende und den Zählern #Kurse, #Templates und #Termine, ein Element mit Kursen und Terminen aufgeklappt, im Schritt Übersicht Elemente](assets/course_planner_implementations_copy3_v1_de.png){ class="shadow lightbox" }  

In einer Durchführung hat es viele verschiedene Terminangaben, die in einer bestimmten Reihenfolge angelegt sind. Beim Kopieren können alle diese Daten automatisch angepasst werden und gemeinsam verschoben werden. Verwenden Sie dazu in der Übersicht der Elemente den Button **"Alle Daten schieben"**. Der Dialog zeigt das "Bezugsdatum (frühestes)". Unter "Verschiebung nach" wählen Sie zwischen "Datum" und "Tage" und geben anschliessend das "Neue Datum" bzw. die Anzahl Tage an.

![Der Button Alle Daten schieben rechts über der Elementübersicht, mit dem sich alle Datumsangaben gemeinsam verschieben lassen, im Schritt Übersicht Elemente](assets/course_planner_implementations_copy4_v2_de.png){ class="shadow lightbox" }

![Bezugsdatum, die Wahl der Verschiebung nach Datum oder Tage und das neue Datum, im Dialog Alle Daten schieben des Assistenten Element kopieren](assets/course_planner_implementations_copy5_v2_de.png){ class="shadow lightbox" } 

### To-dos beim Kopieren übernehmen [:octicons-tag-16:{ title="ab Release 21.0 (OO-9419)" }](https://track.frentix.com/issue/OO-9419){:target="_blank"} {: #copy_todos}

To-dos einer Durchführung werden beim Kopieren mitübernommen. Im ersten Schritt des Wizards bestimmen Sie mit der Auswahl "To-dos", wie dabei vorgegangen wird:

* **Standard:** To-dos mit Zuweisungen kopieren.
* **Nur To-dos:** To-dos ohne Zuweisungen kopieren.
* **Nicht kopieren:** To-dos werden nicht kopiert.

In der Übersicht der Elemente zeigt die Spalte **"#To-dos"**, wie viele To-dos ein Element enthält. In der Detailansicht eines Elements listet der Bereich "To-dos" alle To-dos mit Titel, Priorität, Datumseingabe (absolut oder relativ), Fälligkeitsdatum, Status, Zuweisung, Delegation und Tags auf. Über die Checkbox am Zeilenanfang wählen Sie einzelne To-dos vom Kopieren ab. Sind keine To-dos vorhanden, erscheint der Hinweis "Keine To-dos verfügbar."

![Die Zähler #Kurse, #Templates, #Termine und #To-dos und darunter die Detailbereiche Kurse, Termine und To-dos eines aufgeklappten Elements, im Schritt Übersicht Elemente](assets/course_planner_implementations_copy_todos_details_v1_de.png){ class="shadow lightbox" }

### Raumbuchungen beim Kopieren übernehmen [:octicons-tag-16:{ title="ab Release 21.0.2 (OO-9710)" }](https://track.frentix.com/issue/OO-9710){:target="_blank"} {: #copy_rooms}

Ist das Modul «Räume» aktiviert, zeigt der erste Schritt des Wizards zusätzlich den Abschnitt **«Raumverwaltung»**. Mit der Auswahl **«Raumplanung»** bestimmen Sie dort, ob die Raumbuchungen der Termine mitkopiert werden:

* **Kopieren:** Die Raumbuchungen werden zusammen mit den Terminen kopiert. Diese Option ist vorausgewählt.
* **Nicht kopieren:** Die Raumbuchungen werden nicht kopiert.

Die Auswahl ist nur aktiv, wenn überhaupt Termine kopiert werden, also wenn bei **Kursinhalt** oder bei **Eigenständige Termine** die Option «Kopieren» gewählt ist. Andernfalls ist sie ausgegraut und es entstehen keine Buchungen.

!!! note "Sie sehen den Abschnitt «Raumverwaltung» nicht?"

    Der Abschnitt erscheint nur, wenn ein:e Systemadministrator:in das Modul «Räume» aktiviert hat.<br>
    [Räume verwalten (Administration) >](../../manual_admin/administration/Modules_Rooms.de.md#activation)

Die Kopie übernimmt den Raum der ursprünglichen Buchung. Der Zeitraum der Buchung folgt dem kopierten Termin: Verschieben Sie mit **«Alle Daten schieben»** die Termine, verschieben sich die Buchungen mit. OpenOlat prüft beim Kopieren nicht, ob der Raum im neuen Zeitraum noch frei ist. Konflikte wie eine Doppelbuchung erscheinen erst danach als Warnung in der [Raumplanung](Course_Planner_Rooms.de.md#room_scheduling).

Im Schritt **«Übersicht Elemente»** erscheint bei aktivem Modul und gewählter Option «Kopieren» zusätzlich die Spalte **"#Räume"**. Klappen Sie ein Element auf, führt die Tabelle «Termine» dort die Spalte **"Räume"** mit den gebuchten Räumen.

Die Aktion **«Element kopieren»** steht Administrator:innen, Kursplaner:innen und Produktbesitzer:innen zur Verfügung. Die vollständige Übersicht finden Sie in der [Rechte-Matrix](Course_Planner.de.md#rights_matrix) des Course Planners.

Einzelne Termine kopieren Sie stattdessen in der Terminliste einer Durchführung mit der Aktion **«Kopieren»**. Markieren Sie dort mehrere Termine und kopieren Sie diese gemeinsam, übernimmt OpenOlat die Raumbuchungen automatisch. Kopieren Sie einen einzelnen Termin, öffnet sich der Bearbeitungsdialog der Kopie mit leerem Feld **«Räume»**; die Räume wählen Sie dort selbst.

[zum Seitenanfang ^](#implementations)

---


## Löschen einer Durchführung [:octicons-tag-16:{ title="ab Release 20.0 (OO-8354)" }](https://track.frentix.com/issue/OO-8354){:target="_blank"} {: #delete}

Auch die Option zum Löschen finden Sie in der Liste der Durchführungen am Ende einer Zeile unter den 3 Punkten.

![Die Aktion Löschen im Menü der drei Punkte am Ende einer Zeile, in der Liste der Durchführungen im Course Planner](assets/course_planner_implementations_delete1_v1_de.png){ class="shadow lightbox" } 

Haben Sie eine Durchführung bereits angezeigt, finden Sie die Option zum Löschen auch rechts oben unter den 3 Punkten.

![Die Aktion Löschen im Menü der drei Punkte rechts oben, verfügbar in einer geöffneten Durchführung oberhalb der Tabs](assets/course_planner_implementations_delete2_v1_de.png){ class="shadow lightbox" } 


[zum Seitenanfang ^](#implementations)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Gruppen (Administration) >](../../manual_admin/administration/Modules_Groups.de.md)<br>
[Katalog 2.0 - Angebote >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>
[Modul Course Planner (Administration) >](../../manual_admin/administration/Modules_Course_Planner.de.md)<br>
[Course Planner: To-dos >](Course_Planner_Todos.de.md)<br>
[Course Planner: Zertifikatsprogramme >](Course_Planner_Certification_Programs.de.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.de.md)<br>
[Modul Räume (Administration) >](../../manual_admin/administration/Modules_Rooms.de.md)<br>
[Course Planner: Raumverwaltung >](Course_Planner_Rooms.de.md)<br>
[Course Planner: Übersicht >](Course_Planner.de.md)

**Weiterführend**<br>
[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../../manual_how-to/my_first_course/my_first_course.de.md)<br>
[Course Planner: Produkte >](../../manual_user/area_modules/Course_Planner_Products.de.md)<br>
[Course Planner: Termine >](../../manual_user/area_modules/Course_Planner_Events.de.md)<br>
[Wie kann ich mit dem Course Planner Kursdurchführungen planen und durchführen? >](../../manual_how-to/course_planner_courses/course_planner_courses.de.md)<br>
[Wie kann ich mit dem Course Planner einen Bildungsgang planen und durchführen? >](../../manual_how-to/course_planner_curriculum/course_planner_curriculum.de.md)

[zum Seitenanfang ^](#implementations)
