# Coaching - Kurse {: #courses}


![Markierter Button Kurse in der Gruppe Coaching führt zur Liste Ihrer betreuten Kurse, auf der Einstiegsseite Coaching.](assets/coaching_courses1_v1_de.png){ class="shadow lightbox" }

![Kursliste in Kacheldarstellung mit dem Fokus Als Betreuer:in, den Filter-Tabs Favoriten bis Beendet und Filtern wie Durchführungszeitraum und Erfolgsstatus, im Werkzeug Kurse.](assets/coaching_courses2_v2_de.png){ class="shadow lightbox" }


### WELCHE Kurse zeigt die Liste? {: #courses_which}

Der Menüpunkt "Kurse" im Coaching Tool zeigt die Liste aller **Kurse**, in denen Sie **Betreuer:in** oder **Besitzer:in** sind.

* Es werden die Teilnehmenden aus **allen** von Ihnen betreuten Kursen angezeigt. (Im Unterschied zum [Bewertungswerkzeug](../learningresources/Assessment_tool_overview.de.md) des Kurses. Dort werden nur Teilnehmende des aktuellen Kurses angezeigt.)
* Betreuer:innen sehen nur die von ihnen betreuten Teilnehmenden.
* Die betreuten Teilnehmenden sind **gruppiert und den Rollen zugeordnet**, die Sie als Betreuer:in gegenüber dieser Person haben.<br>
Im oben gezeigten Beispiel kann die betreuende Person vorsortierte Listen abrufen, die ihren beiden Rollen als Betreuer:in und als Besitzer:in entsprechen.
* In der Liste für Betreuer:innen sehen Sie nur Kurse, die veröffentlicht, beendet oder zumindest für Betreuer:innen zugänglich sind.


[Zum Seitenanfang ^](#courses)

---

### Vordefinierte Filter-Tabs [:octicons-tag-16:{ title="ab Release 20.0.4 (OO-8677)" }](https://track.frentix.com/issue/OO-8677) {: #courses_filters}

Oberhalb der Liste stehen vordefinierte Filter-Tabs zur Verfügung. Sie schränken ein, welche Kurse angezeigt werden:

* **Favoriten**: nur die von Ihnen als Favorit markierten Kurse.
* **Alle**: alle Kurse unabhängig vom Status.
* **Relevant** [:octicons-tag-16:{ title="ab Release 20.2.2 (OO-9167)" }](https://track.frentix.com/issue/OO-9167) (Standard beim Öffnen): Kurse im Status "Veröffentlicht" und "Freigabe Betreuer:innen", also die aktuell aktiven Kurse, bei denen Handlungsbedarf bestehen kann.
* **Veröffentlicht**: nur Kurse im Status "Veröffentlicht".
* **Freigabe Betreuer:innen**: nur Kurse im Status "Freigabe Betreuer:innen".
* **Beendet**: nur Kurse im Status "Beendet".

Weitere Informationen zum allgemeinen Umgang mit Filtern und Filter-Tabs finden Sie unter [Mit Tabellen arbeiten](../basic_concepts/Table_Concept.de.md).

[Zum Seitenanfang ^](#courses)

---

### Kurse suchen {: #courses_search}

Mit dem Suchfeld oberhalb der Liste grenzen Sie die Kurse nach Titel, Kennzeichen oder externer ID ein. Die Suche unterscheidet nicht zwischen Gross- und Kleinschreibung. Ohne weitere Zeichen findet sie alle Kurse, die den Suchbegriff an beliebiger Stelle enthalten.

Kennen Sie die genaue Schreibweise nicht, setzen Sie den Stern `*` als Platzhalter ein. Er steht für beliebig viele beliebige Zeichen [:octicons-tag-16:{ title="ab Release 20.3.7 (OO-9630)" }](https://track.frentix.com/issue/OO-9630){:target="_blank"}:

* `Blog*` findet Kurse, deren Titel mit "Blog" beginnt.
* `*2026` findet Kurse, deren Titel auf "2026" endet.
* `ab*cd` findet Kurse, deren Titel mit "ab" beginnt und auf "cd" endet, unabhängig davon, was dazwischen steht.

Der Platzhalter verhält sich damit gleich wie im Bereich [Kurse](Courses.de.md).

[Zum Seitenanfang ^](#courses)

---

### WAS zeigt die Liste? [:octicons-tag-16:{ title="ab Release 20.1.1 (OO-8806)" }](https://track.frentix.com/issue/OO-8806) {: #courses_what}

!!! tip "Tipp"

    Mit Klick auf die kleinen Buttons rechts oben über der Liste können Sie jederzeit zwischen der Listen- und der Kacheldarstellung wechseln.

![Kursliste in Listendarstellung mit Spalten von Typ und Titel über Teilnehmer:innen und Besuche bis Fortschritt, Erfolgsstatus, Punkte und Zertifikate, Umschalter rechts oben.](assets/coaching_courses3_v2_de.png){ class="shadow lightbox" }


Sie sehen auf einen Blick zum Beispiel

* in welchen Kursen (Lernressourcen) Sie Betreuer:in sind,
* wie viele Teilnehmende in diesen Kursen sind
* und wie weit die Bearbeitung dieser Kurse insgesamt fortgeschritten ist.

Von dieser Liste aus können Sie gezielt in einen Kurs und das dortige Bewertungswerkzeug wechseln.<br>
Ein Klick auf einen Kursnamen führt direkt zum Kurs. Dort können Sie weiter gezielt zu einzelnen Teilnehmenden navigieren und Leistungsübersichten oder das Absenzenmanagement anzeigen lassen.

Welche Spalten angezeigt werden, können Sie selbst festlegen, indem Sie rechts oben auf das Zahnrad-Icon klicken.

* **ID** (eindeutige Nummer)
* **Favorit**
* **Typ** (Würfel-Symbol für "Kurs", bei Stand-alone-Lernressourcen ein entsprechendes anderes Symbol)
* **Technischer Typ** (z.B. "Lernpfad" oder "Herkömmlicher Kurs")
* **Titel**
* **Ext. ID** (externe ID, die einer anderen Systematik folgen kann als die von OpenOlat automatisch vergebene ID)
* **Kennzeichen**
* **Beginn** (Beginn des Durchführungszeitraums dieses Kurses)
* **Ende** (Ende des Durchführungszeitraums dieses Kurses)
* **Referenzierungen**
* **Status** ("in Review", "Veröffentlicht", "Beendet")
* **Teilnehmer:innen** (Anzahl aller Teilnehmenden)
* **Besucht** (Anzahl der Teilnehmenden, die diesen Kurs schon einmal besucht haben)
* **Nicht besucht** (Anzahl der Teilnehmenden, die diesen Kurs noch nie besucht haben)
* **Letzter Besuch** (Wann wurde dieser Kurs zuletzt von einer/einem Teilnehmenden besucht)
* **durchschnittlicher Fortschritt** (Durchschnitt aus den Fortschrittswerten aller Teilnehmenden, die den Kurs schon einmal besucht haben)
* **Erfolgsstatus** (grafisch und in Zahlen: "Bestanden" | "Nicht bestanden" | "Keine Angabe")
* **Bestanden**
* **Nicht bestanden**
* **Keine Angabe**
* **durchschnittliche Punkte** (durchschnittliche Punktzahl aller Teilnehmenden, die diesen Kurs bereits bearbeitet haben)
* **Zertifikate** (Anzahl der Zertifikate, die in diesem Kurs bereits ausgestellt wurden)
* **Bewertungswerkzeug** (anklickbares Symbol, das direkt zum Bewertungswerkzeug dieses Kurses führt)
* **Informationsseite** (anklickbares Glühbirnen-Symbol, das direkt zu den Informationen führt, die im Kurs unter `Kurs > Administration > Einstellungen` eingegeben wurden)

!!! tip "Genaue Zahlen zum Erfolgsstatus"

    Fahren Sie mit der Maus über den grafischen Balken in der Spalte "Erfolgsstatus". Ein Tooltip zeigt die genauen Zahlen: "Bestanden: X / Nicht bestanden: Y / Keine Angabe: Z" [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9229)" }](https://track.frentix.com/issue/OO-9229){:target="_blank"}.


[Zum Seitenanfang ^](#courses)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Bewertungswerkzeug >](../../manual_user/learningresources/Assessment_tool_overview.de.md)<br>
[Mit Tabellen arbeiten >](../basic_concepts/Table_Concept.de.md)<br>
[Kurse finden >](Courses.de.md)

**Weiterführend**<br>
[Coaching: Personensuche >](../../manual_user/area_modules/Coaching_User_Search.de.md)<br>
[Coaching: Personen >](../../manual_user/area_modules/Coaching_People.de.md)<br>
[Coaching: Bildungsprodukte >](../../manual_user/area_modules/Coaching_Educational_Products.de.md)<br>
[Coaching: Termine / Absenzen >](../../manual_user/area_modules/Coaching_Events_Absences.de.md)<br>
[Coaching: Bewertungsaufträge >](../area_modules/Coaching_Assessment_Orders.de.md)<br>
[Coaching: Reports >](../../manual_user/area_modules/Coaching_Reports.de.md)<br>
[Coaching: Gruppen >](../../manual_user/area_modules/Coaching_Groups.de.md)<br>
[Coaching: Auftragsverwaltung >](../../manual_user/area_modules/Coaching_Order_Management.de.md)<br>
[Rollen >](../../manual_user/basic_concepts/Roles.de.md)

[Zum Seitenanfang ^](#courses)
