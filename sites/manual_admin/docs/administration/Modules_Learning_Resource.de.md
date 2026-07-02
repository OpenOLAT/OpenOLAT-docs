# Modul Lernressource {: #learning_resource}

[:octicons-tag-16:{ title="ab Release 20.3 (früher: Repository)" }](https://track.frentix.com/issue/OO-9185){:target="_blank"}

Zum Modul Lernressourcen gehören Einstellungen, die die Kurse und Lernressourcen betreffen, die im Repository gespeichert sind.

![modules_learning_resource_tab_settings_v1_de.png](assets/modules_learning_resource_tab_settings_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#learning_resource)

---


## Tab Einstellungen {: #tab_settings}

### Abschnitt "Einstellungen"

#### Bereich "In Vorbereitung" unter "Kurse"

Mit Aktivierung dieser Checkbox machen Administrator:innen für Teilnehmer:innen die Vorauswahl "In Vorbereitung" im Menü "Kurse" sichtbar.

Ansicht Teilnehmer:in bei Aktivierung:
![modules_learning_resource_tab_settings_section_v1_de.png](assets/modules_learning_resource_tab_settings_section_v1_de.png){ class="shadow lightbox" }

#### Kommentar {: #comment}

In der Kopfzeile eines Kurses kann die Info-Seite zum Kurs aufgerufen werden.

![modules_repository_course_info_v1_de.png](assets/modules_repository_course_info_v1_de.png){ class="shadow lightbox" }

Auf der Infoseite kann dann ein Eingabefeld zur Abgabe eines Kommentars angezeigt werden.

![modules_repository_course_comment_v1_de.png](assets/modules_repository_course_comment_v1_de.png){ class="shadow lightbox" }

Die Verfügbarkeit dieses Eingabefeldes kann von Administrator:innen hier unter `Administration > Module > Lernressource > Kommentar` global ein-/ausgeschaltet werden.

[Zum Seitenanfang ^](#learning_resource)

---


#### Bewertung

Auf der Infoseite zu einem Kurs können ebenfalls anklickbare Sterne zur Beurteilung angezeigt werden.

![modules_repository_course_review_v1_de.png](assets/modules_repository_course_review_v1_de.png){ class="shadow lightbox" }

Die Verfügbarkeit der Sterne zur Beurteilung kann von Administrator:innen hier unter `Administration > Module > Lernressource > Bewertung` global ein-/ausgeschaltet werden.

[Zum Seitenanfang ^](#learning_resource)

---

#### Mitgliedschaft beantragen

Wenn jemand einen Kurs öffnet, auf welchen er keinen Zugriff hat, erscheint ein Screen mit Hinweis. 
Hier gibt es einen Button, mit dem eine Mitgliedschaft beantragt werden kann. Beim Anklicken wird damit eine E-Mail an alle Kursbesitzer:innen verschickt.

![modules_repository_request_membership_v1_de.png](assets/modules_repository_request_membership_v1_de.png){ class="shadow lightbox" }

Diese Funktion kann von Administrator:innen unter `Administration > Module > Lernressource > Mitgliedschaft beantragen` global ein-/ausgeschaltet werden.

[Zum Seitenanfang ^](#learning_resource)

---


#### Taxonomie
**Verwendung von Taxonomie im Katalog** [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9214)" }](https://track.frentix.com/issue/OO-9214){:target="_blank"}

Die Aktivierung von Taxonomie in der Lernressource führt dazu, dass die gewählte "Struktur" im Katalog verfügbar ist. Damit dieser Weg funktioniert, muss die entsprechende Taxonomie zuerst grundsätzlich erarbeitet und integriert sein.

!!! tip "Grundlage"
    Unter `Administration > Module > Taxonomie` können verschiedene Taxonomien erstellt werden.


Eine Taxonomie kann in diesem Bereich nicht abgewählt werden, solange sie in einem Launcher des **Katalogs verwendet wird**. Beim Versuch der Abwahl erscheint die Meldung: «Die Taxonomie wird noch in einem Launcher des Katalogs verwendet und kann daher nicht abgewählt werden.»


!!! info "Modul Taxonomie"
    Wie Taxonomien erstellt und konfiguriert werden.<br>
    [Zum Modul Taxonomie >](Modules_Taxonomy.de.md)

[Zum Seitenanfang ^](#learning_resource)

---

### Abschnitt "Standardeinstellung"

#### Teilnehmer:innen können austreten {: #allow_leaving_courses}

Mit dieser Option wird eine Standardeinstellung für alle neuen Kurse vorgegeben. (Bereits bestehende Kurse sind davon nicht betroffen.) Kursteilnehmer:innen können ggf. dann selbst entscheiden, ob sie einen Kurs verlassen möchten. D.h., sie können selbst die Mitgliedschaft in einem Kurs beenden und sich als Kursmitglied austragen.

Als Default-Option kann gewählt werden zwischen

* Jederzeit
* Nach Kursenddatum oder Status "Beendet"
* Nie

Diese Default-Einstellung kann von Kursbesitzer:innen im Kurs unter `(Kurs-)Administration > Einstellungen > Tab Freigabe` kursspezifisch angepasst werden.

[Zum Seitenanfang ^](#learning_resource)

---

### Abschnitt "Benachrichtigung" {: #notification}

OpenOlat kann an verschiedenen Stellen Benachrichtigungen über Ereignisse versenden. Wenn jemand die Benachrichtigungen erhalten möchte, kann dazu ein Abonnement eingerichtet werden.

Benachrichtigungen über Ereignisse im Repository betreffen aktuell (Release 19) nur das Abonnement "**Besitzer:innen über Statuswechsel für Lernressourcen benachrichtigen**".

#### Abonnenten

A) Voreinstellung<br>
Durch Aktivierung/Deaktivierung des Abonnements wird bestimmt, ob bei Erstellung eines neuen Kurses bzw. einer Lernressource im Repository als Default auch ein Abonnement für die beschriebene Zielgruppe eingerichtet wird. Dies hat keine Auswirkung auf bereits erstellte Abonnements.

B) Bereits bestehende Abonnements können aktualisiert werden mit den Buttons 
"Bestehende Abonnements aktivieren" und "Bestehende Abonnements deaktivieren". 

[Zum Seitenanfang ^](#learning_resource)

---


### Abschnitt "Standard-Rollenpriorität" [:octicons-tag-16:{ title="ab Release 20.1.2 (OO-8795)" }](https://track.frentix.com/issue/OO-8795){:target="_blank"}

Diese Einstellung legt die Reihenfolge fest, in der die Rollen priorisiert werden, wenn ein Mitglied beim Zugriff auf die Lernressource mehrere Rollen hat. Die oberste Rolle in der Liste hat die höchste Priorität. Systemrollen haben immer eine niedrigere Priorität als Mitgliedsrollen.

[Zum Seitenanfang ^](#learning_resource)

---


## Tab Zugang {: #tab_accesss}


![modules_learning_resource_tab_accesss_v1_de.png](assets/modules_learning_resource_tab_access_v1_de.png){ class="shadow lightbox" }


### Abschnitt "Zugang"

#### Zugang Kursbesitzer:innen/Betreuer:innen

Wer in einem Kurs (einer Lernressource) Besitzer:in oder Betreuer:in ist, kann diesen Kurs auf jeden Fall im Coaching Tool finden.
Es kann hier gewählt werden, ob zusätzlich auch unter "Meine Kurse" auf solche Lernressourcen zugegriffen werden kann. 


#### Hinweis in "Kurse" anzeigen

Wird dieser Toggle-Button aktiviert, erhalten die Kursbesitzer:innen/Betreuer:innen Hinweise zu den Auswirkungen der Zugangseinstellung.

#### Übersicht Zugangseinstellungen für Sites

Unter `Administration > Customizing > Sites` können Administrator:innen einstellen, welche Menüpunkte (Sites) in der Hauptnavigation (Kopfzeile) angezeigt werden.

Hier (unter Modul Lernresource) wird angezeigt, was dort betreffend "Meine Kurse" und "Coaching Werkzeug" eingestellt ist. Ob diese Site überhaupt in der Kopfzeile angezeigt werden soll und für welche Rollen es sichtbar ist.

Um die Einstellungen zu ändern, kann direkt mit einem Link zu `Administration > Customizing > Sites` gewechselt werden ("Site Einstellungen öffnen").

[Zum Seitenanfang ^](#learning_resource)

