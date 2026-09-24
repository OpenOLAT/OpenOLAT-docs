# Projekte - Administration {: #administration}

Um zur Projektadministration Ihres Projektes zu gelangen, öffnen Sie das gewünschte Projekt und klicken rechts oben auf die 3 Punkte. Im aufgeklappten Menü erscheinen mehrere administrative Möglichkeiten.

Zur Administration eines Projektes gehören

* die Konfiguration und Darstellung der Startseite (Projekt bearbeiten)
* die [Verwaltung der Mitglieder](../area_modules/Project_Member_Management.de.md) des Projektes
* die Möglichkeit, [Reports](../area_modules/Project_Report.de.md) herunterzuladen
* Projekte zu kopieren
* Projekte als Vorlage zu speichern
* Projekte zu beenden und abzuschliessen
* Projekte zu löschen

!!! info "Wichtig"

    Welche Menüpunkte in dem Bereich erscheinen, ist von der Projektrolle abhängig.

## Projekt bearbeiten

Mit "Projekt bearbeiten" ist nicht die inhaltliche Bearbeitung gemeint (Termine eintragen, To-dos erstellen, usw.), sondern die **Bearbeitung der Startseite** des Projektes. Öffnen Sie dazu im Cockpit des Projekts rechts oben das 3-Punkte-Menü und wählen Sie "Projekt bearbeiten".

![Eintrag Projekt bearbeiten im 3-Punkte-Menü rechts oben im Cockpit eines Projekts](assets/projekte_admin_projekt_bearbeiten_v2_de.png){ class="shadow lightbox" }

Es öffnet sich der Dialog "Projekt bearbeiten". Die Nummern im Bild zeigen, wo die Angaben aus dem Dialog auf der Startseite des Projekts erscheinen.

![Dialog Projekt bearbeiten, die Nummern 1 bis 4 verbinden die Felder Titel, Teaser, Avatar und Hintergrund Bild mit ihrer Stelle auf der Startseite des Projekts dahinter](assets/projekte_admin_projekt_bearbeiten_popup_v1_de.png){ class="shadow lightbox" }

* ![1](assets/1_green_24.png) **Titel**: Pflichtfeld. Der Titel steht als Überschrift auf der Startseite und bezeichnet das Projekt in der Projektliste.
* ![2](assets/2_green_24.png) **Teaser**: Kurztext, der auf der Startseite direkt unter dem Titel erscheint.
* ![3](assets/3_green_24.png) **Avatar**: Quadratisches Bild links oben auf der Startseite. Beste Resultate mit der Grösse 240x240px, maximale Dateigrösse 2 MB.
* ![4](assets/4_green_24.png) **Hintergrund Bild**: Bild über die ganze Breite der Startseite. Beste Resultate mit der Grösse 2588x500px, maximale Dateigrösse 2 MB.

Drei weitere Felder erscheinen nicht oder nur klein auf der Startseite:

* **Administrative Freigabe**: Pflichtfeld. Die Organisationen, denen das Projekt zugeordnet ist. Projektverwalter:innen und Administrator:innen dieser Organisationen sehen das Projekt im Tab "Administration". Ohne eine dieser Rollen ist Ihre eigene Organisation vorbelegt und nicht änderbar.
* **Kennzeichen**: Frei wählbare Referenz, zum Beispiel eine Projektnummer. Sie erscheint klein unter dem Titel und als einblendbare Spalte in der Projektliste.
* **Beschreibung**: Ausführlicher Text zum Projekt. Er wird auf der Startseite nicht angezeigt.


## Projekt kopieren [:octicons-tag-16:{ title="ab Release 18.0 (OO-6840)" }](https://track.frentix.com/issue/OO-6840)

![Eintrag Projekt kopieren im 3-Punkte-Menü rechts oben im Cockpit eines Projekts](assets/projekte_admin_projekt_kopieren_v2_de.png){ class="shadow lightbox" }

Kopiert werden:

* alle To-dos
* alle Entscheide
* alle Notizen
* alle Dateien

**Nicht** kopiert werden:

* Projektmitglieder

**Teilweise** kopiert werden:

* Termine und Meilensteine (werden ohne Datum kopiert)


## Projektvorlagen

Wenn Sie ähnliche Projekte wiederholt anlegen, sparen Sie mit einer Vorlage die Einrichtung jedes einzelnen Projekts.

Ein angelegtes Projekt kann als Vorlage gespeichert werden. Wählen Sie hierfür im 3-Punkte-Menü die Option "Als Vorlage speichern".

![Eintrag Als Vorlage speichern im 3-Punkte-Menü rechts oben im Cockpit eines Projekts](assets/projekte_admin_als_vorlage_speichern_v3_de.png){ class="shadow lightbox" }

Es öffnet sich der Dialog "Als Vorlage speichern". Eine private Vorlage steht nur Ihnen zur Verfügung. Eine organisationsweite Vorlage steht allen Mitgliedern der gewählten Organisationen zur Verfügung. Die Auswahl "Sichtbarkeit" mit den Optionen "Nur für mich" und "Für alle Mitglieder der Organisation" sehen nur Personen mit der Organisationsrolle Administrator:in oder Projektverwalter:in. Erlaubt die System-Administration unter `Administration > Module > Projekte` auch Autor:innen, Projekte und Vorlagen hinzuzufügen, sehen auch Autor:innen diese Auswahl. Alle übrigen Personen erstellen immer eine private Vorlage. Bei der Option "Für alle Mitglieder der Organisation" wählen Sie im Feld "Vorlage Organisationen" die Organisationen aus, in denen Sie eine dieser Rollen haben. :octicons-tag-16:{ title="ab Release 21.0.3 (OO-9719)" }

![Auswahl Sichtbarkeit mit den Optionen Nur für mich und Für alle Mitglieder der Organisation, darunter das Pflichtfeld Vorlage Organisationen, im Dialog Leere Vorlage erstellen](assets/projekte_admin_vorlage_sichtbarkeit_v1_de.png){ class="shadow lightbox" }

Darüber hinaus kann eine leere Vorlage im Tab "Projektvorlagen" erstellt werden, was häufig ein sinnvollerer Weg ist: `Projekte > Tab "Projektvorlagen" > Button "Leere Vorlage erstellen"`. Für die Sichtbarkeit gilt dort dieselbe Regel wie beim Speichern eines Projekts als Vorlage.

![Button Leere Vorlage erstellen im Tab Projektvorlagen des Bereichs Projekte](assets/projekte_admin_leere_vorlage_v1_de.png){ class="shadow lightbox" }


## Projekte abschliessen

![Eintrag Projekt abschliessen im 3-Punkte-Menü rechts oben im Cockpit eines Projekts](../area_modules/assets/projekt_abschliessen_v1_de.png){ class="shadow lightbox" }

Wird ein Projekt abgeschlossen, haben alle Projektmitglieder anschliessend nur noch schreibgeschützten Zugriff.

Abgeschlossen werden kann ein Projekt nur durch

* Projektbesitzer:innen,
* Projektleiter:innen,
* Projektbüro-Mitarbeiter:innen,
* Administrator:innen,
* und Projektverwalter:innen.

!!! info "Wichtig"

    Durch diese Personen kann ein Projekt auch wieder reaktiviert werden.


## Projekt löschen

![Eintrag Projekt löschen im 3-Punkte-Menü rechts oben im Cockpit eines Projekts](assets/projekte_admin_loeschen_v2_de.png){ class="shadow lightbox" }

Gelöscht werden können Projekte nur durch

* den/die Projektbesitzer:in,
* Administrator:innen,
* und Projektverwalter:innen.


!!! info "Wichtig"

    Durch das Löschen eines Projektes erscheint es in der Liste "Gelöschte". Die Projekte können dort nur noch angesehen, aber nicht mehr bearbeitet werden.


## Tab Projektadministration [:octicons-tag-16:{ title="ab Release 18.0 (OO-6845)" }](https://track.frentix.com/issue/OO-6845)

OpenOlat-Administrator:innen und Projektverwalter:innen haben unter dem Menüpunkt "Projekte" einen weiteren Tab: `Projekte > Tab "Administration"`.

![Tab Administration im Bereich Projekte mit den Filtern Ohne kürzliche Aktivität, Zu löschen, Abgeschlossen und Gelöschte oberhalb der Projektliste](assets/projekte_admin_admin_v1_de.png){ class="shadow lightbox" }

Für Ihre Verwaltungsaufgaben stehen dort folgende (Filter-)Funktionen zur Verfügung:

* **Ohne kürzliche Aktivität**<br>
In dieser Liste befinden sich Projekte, in denen seit mehr als 28 Tagen keine Aktivität stattgefunden hat. Ihr Status kann "aktiv" oder "abgeschlossen" sein. Projekte in dieser Liste sollten geprüft werden, ob sie nicht evtl. abgeschlossen bzw. gelöscht werden können. (Man kann bei dem/der Projektbesitzer:in evtl. nachfragen.)

* **Zu löschen**<br>
Die Liste "Zu löschen" erscheint nur im Tab "Administration". In ihr werden Projekte mit Status "abgeschlossen" angezeigt, die ausserdem ohne kürzliche Aktivität sind.

* **Abgeschlossen**<br>
Sind Projekte seit längerem abgeschlossen, können Projektverwalter:innen auf Grund dieser Liste evtl. nachfragen, ob Projekte gelöscht werden können.<br>
Abgeschlossene Projekte können noch reaktiviert werden.

* **Gelöschte**<br>
Gelöschte Projekte können nur noch angesehen, aber nicht mehr bearbeitet werden.


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Projekte: Mitgliederverwaltung >](../area_modules/Project_Member_Management.de.md)<br>
[Projekte - Projektreport >](../area_modules/Project_Report.de.md)

**Weiterführend**<br>
[Projekte: Überblick >](../area_modules/Project_Overview.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../basic_concepts/Roles.de.md)<br>
[Modul Projekte >](../../manual_admin/administration/Modules_Projects.de.md)

[Zum Seitenanfang ^](#administration)
