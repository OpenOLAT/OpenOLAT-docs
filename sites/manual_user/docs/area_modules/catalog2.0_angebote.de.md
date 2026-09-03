# Katalog 2.0 - Angebote {: #offers}


## Was enthält der OpenOlat-Katalog? [:octicons-tag-16:{ title="ab Release 17.1 (OO-6201)" }](https://track.frentix.com/issue/OO-6201) {: #offers_catalog_content}

Wie in anderen Katalogen, werden auch im OpenOlat-Katalog in vielen kleinen Einträgen Kurzbeschreibungen zu "Produkten" angezeigt. In OpenOlat sind dies

- Kurse
- Durchführungen von Curricula/Produkten
- oder andere Lernressourcen, wie z.B. Tests oder Videos.


## Erscheinen alle Kurse im Katalog? {: #offers_display_decision}

Im Katalog werden **nicht automatisch** alle erstellten Kurse und Lernressourcen angezeigt. Die Autor:innen der jeweiligen Kurse und Lernressourcen entscheiden, ob etwas in den Katalog aufgenommen wird.

Dazu muss im jeweiligen Kurs bzw. der Lernressource ein **Angebot** erstellt werden.<br>
Wenn kein Angebot erstellt wird, erfolgt auch kein Katalogeintrag.

[Zum Seitenanfang ^](#offers)

---


## Wie wird ein Angebot erstellt? {: #offers_create}

Angebote hängen am Kurs und werden dort von Autor:innen in den Einstellungen definiert:<br>
`Kurs > Administration > Einstellungen > Tab "Freigabe"`

!!! note "Unterschied Katalog 1.0 und Katalog 2.0"

    Im Katalog 1.0 werden alle Angebote in den Kursen erstellt: `Kurs > Administration > Einstellungen > Tab "Freigabe"`. Anschliessend werden sie in der **Katalogverwaltung** zusammengestellt.

    Im Katalog 2.0 werden Angebote ebenfalls in den Kurseinstellungen erstellt. Zusätzlich werden hier noch Angaben gemacht, **wo** im Katalog das Angebot erscheinen soll. Anhand dieser Angaben kann der Katalog 2.0 die Angebote dann **dynamisch selbst zusammenstellen**.

![Fünf nummerierte Schritte vom Menü Administration über Einstellungen und Tab Freigabe zur Option Buchbare und offene Angebote und zum Button Angebot hinzufügen, Kurseinstellungen](assets/catalog20_angebot_erstellen_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#offers)

---


## Voraussetzung für ein Angebot {: #offers_requirements}

Auch der Zugang zu einem Kurs wird in den Kurseinstellungen konfiguriert: `Kurs > Administration > Einstellungen > Tab "Freigabe"`. Es stehen zwei grundsätzliche Varianten zur Verfügung:

![Optionen Privat und Buchbare und offene Angebote für den Zugang für Teilnehmer:innen, Tab Freigabe der Kurseinstellungen](assets/catalog20_freigabe_v1_de.png){ class="shadow lightbox" }

Bei der Wahl "Privat" werden die Teilnehmenden durch die Besitzer:innen bzw. Personen, die über das Recht der Mitgliederverwaltung verfügen, eingetragen. Was privat ist, soll auch nicht im Katalog veröffentlicht werden.

Bei Wahl der Option "Buchbare und offene Angebote" können die Lernenden einen Kurs/Lernressource selbst buchen, müssen aber eventuell (je nach Einstellung) ein Passwort eingeben.

Wird die zweite Option "Buchbare und offene Angebote" gewählt, können Sie anschliessend Angebote erstellen.

[Zum Seitenanfang ^](#offers)

---


## Was enthält ein Angebot? {: #offer_content}

Ein Angebot enthält die Bedingungen, zu denen der Kurs oder die Lernressource genutzt werden kann.

In einem **Angebot** wird definiert, wer sich unter welchen Umständen in die gewählte Lernressource bzw. den Kurs eintragen bzw. diese buchen kann. So ist ein Buchungsauftrag mit Zugangscode, ohne oder per PayPal (sofern von Administrator:innen aktiviert) möglich. Auch ein Zugang ohne Buchungsauftrag oder als Gast können konfiguriert werden. Buchen kann dabei als Synonym für belegen, einschreiben, einkaufen verstanden werden. Wählen Sie die Schaltfläche "Angebot hinzufügen", um Angebote hinzuzufügen.

![Angebotsarten Zugangscode, Frei verfügbar, Ohne Buchung und Gastzugang mit ihren Kurzbeschreibungen zur Auswahl, Dialog Angebot hinzufügen](assets/catalog20_auswahl_art_v1_de.png){ class="shadow lightbox" }

Es können zum gleichen Kurs mehrere verschiedene Angebote erstellt werden. Z.B. kann dann der gleiche Kurs für einige Teilnehmer:innen kostenlos, für andere kostenpflichtig angeboten werden.

![Zwei Angebote Zugangscode und Frei verfügbar desselben Kurses, jeweils für andere Organisationen angeboten, Abschnitt Angebot im Tab Freigabe](assets/catalog20_2angebote_v1_de.png){ class="shadow lightbox" }

Angebote können auch auf verschiedene Teilbereiche von Organisationen (Unterorganisationen) beschränkt werden.

!!! info "Organisationszugehörigkeit"

    Ist ein Angebot auf eine bestimmte Organisation oder Unterorganisation eingeschränkt, erscheint es im Katalog **nur für Benutzer:innen, die Mitglied dieser Organisation sind**. Benutzer:innen ausserhalb der Organisation sehen das Angebot nicht, auch wenn der Kurs veröffentlicht ist.

    Die Organisationszugehörigkeit wird in der [Benutzerverwaltung](../../manual_admin/usermanagement/index.de.md) gepflegt.


[Zum Seitenanfang ^](#offers)

---


## Angebote veröffentlichen {: #offer_publish}

Editieren Sie ein Angebot um festzulegen, wann und wo es im Katalog erscheinen wird.

![Link Angebot editieren in der Zeile eines Angebots vom Typ Zugangscode, Abschnitt Angebot im Tab Freigabe](assets/catalog20_offer_edit_v1_de.png){ class="shadow lightbox" }

Angebote können unabhängig vom Publikationsstatus des Kurses veröffentlicht werden. Dazu wählt man in der Angebotserstellung "zeitbeschränkt" aus und definiert einen zukünftigen Zeitraum. Das Angebot ist dann im Katalog für diesen definierten Zeitraum verfügbar.

![Option Mit zeitlicher Einschränkung und die Datumsfelder Von und bis markiert, Dialog Zugangscode](assets/catalog20_zeitbeschraenkt_v1_de.png){ class="shadow lightbox" }

Neben der **grundsätzlichen Aktivierung**, dass das Angebot in einem Katalog angezeigt werden soll, kann ein **Fachbereich** angegeben werden. Wird kein Fachbereich angegeben, kann das Angebot zwar z.B. über die Suchfunktion im Katalog gefunden werden, es wird jedoch in keinem Taxonomie-Launcher angezeigt, in dem Angebote mit gleichem Fachbereich zusammengefasst angezeigt werden.

Ausserdem muss je nach Angebotstyp z.B. der **Zugangscode** definiert werden.

![Checkbox Im OpenOlat Katalog anzeigen, Feld Fachbereiche / Katalog und Pflichtfeld Zugangscode markiert, Dialog Zugangscode](assets/catalog20_offer_activate_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#offers)

---


## Infoseite {: #offer_info}

Wer im Katalog auf eine Kachel klickt, bekommt eine nähere Beschreibung zum angebotenen Kurs bzw. der Lernressource, ohne dass der Kurs bereits gestartet wird. Auch wenn für den Kursstart evtl. eine Zugangsberechtigung eingerichtet wurde, ist diese Infoseite im Katalog einsehbar. Sie enthält Angaben, die die Autor:innen unter den Metadaten gemacht haben:<br>
`Kurs > Administration > Einstellungen > Tab "Info"`

![Button Infoseite in der Zeile eines Suchtreffers markiert, Suchergebnisse im Katalog](assets/catalog20_eintrag_v1_de.png){ class="shadow lightbox" }

![Beschreibung, Lernziele, Voraussetzungen und Bescheinigung eines Kurses mit dem Button Kurs starten und dem Fachbereich im Überblick, Infoseite im Katalog](assets/catalog20_infoseite_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#offers)

---


## Metadaten, Fachbereich {: #offer_metadata}

Es ist von grosser Bedeutung, welchem Fachbereich Autor:innen einen Kurs bzw. eine Lernressource zuordnen. Denn hinter dem Fachbereich steht die Taxonomie, nach der in den Taxonomie-Launchern des Katalogs Kurse zusammengestellt werden. Sie wählen den Fachbereich unter:<br>
`Kurs > Administration > Einstellungen > Tab "Metadaten"`

![Feld Fachbereiche / Katalog mit dem gewählten Fachbereich Software-Schulung und dem Pfeil zur Auswahl, Tab Metadaten der Kurseinstellungen](assets/catalog20_fachbereich_v1_de.png){ class="shadow lightbox" }

Die im Tab "**Metadaten**" gemachten Angaben zum Fachbereich können im Tab "**Freigabe**" bei der Erstellung eines Angebots genutzt werden. Die Fachbereiche dienen der **Verschlagwortung** im Katalog. Es können mehrere Fachbereiche als Schlagwort angegeben werden.

Wenn Sie auf den kleinen Pfeil am Ende der Zeile "Fachbereiche / Katalog" klicken, können Sie die Schlagworte auswählen. Zunächst erscheint ein Popup, in dem die verwendeten Fachbereiche aufgelistet sind.

![Popup mit Suchfeld, der Auswahl Software-Schulung und dem Button Browser öffnen, Feld Fachbereiche / Katalog im Tab Metadaten](assets/catalog20_metadata_subjects_popup_v1_de.png){ class="shadow lightbox" }

Sie können nun über das Suchfeld oder durch Öffnen eines Browsers weitere Fachbereiche hinzufügen.

![Taxonomiebaum mit den Ebenen Purchase, Software-Schulung und Verkauf zum Ankreuzen, Dialog Suche für die Fachbereiche](assets/catalog20_metadata_subjects_browser_v1_de.png){ class="shadow lightbox" }

Der dynamische Katalog 2.0 kann mit diesen Metadaten alle Angebote, die die gleiche Taxonomie verwenden (die gleichen Fachbereiche angegeben haben), zusammenfassen und in einem Katalogabschnitt (Launcher) zusammen anzeigen (Taxonomie-Launcher).

![Taxonomie-Launcher Online Schulungen mit der Kachel des Fachbereichs Software-Schulung, Startseite des Katalogs](assets/catalog20_taxonomylauncher_v1_de.png){ class="shadow lightbox" }

Nach Klick auf die Kachel des Taxonomie-Launchers öffnet sich die sogenannte Microsite mit der Liste aller Kurse und Lernressourcen, die diesem Fachbereich zugeordnet wurden.

![Vier Kurse des Fachbereichs Software-Schulung mit den Buttons Infoseite und starten, Microsite des Taxonomie-Launchers](assets/catalog20_taxonomylauncher_microsite_v1_de.png){ class="shadow lightbox" }


!!! note "Katalog 1.0"

    Informationen zum Erstellen von Angeboten im Katalog 1.0 finden Sie [hier](catalog1.0.de.md).

[Zum Seitenanfang ^](#offers)

---


## Weiterführende Informationen {: #further_information}

[Benutzerverwaltung (Administrationshandbuch) >](../../manual_admin/usermanagement/index.de.md)<br>
[Katalog 1.0 >](catalog1.0.de.md)

[Zum Seitenanfang ^](#offers)
