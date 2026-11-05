# Persönliche Werkzeuge: Absenzen {: #pers_tools_absences}

![Menü Persönliche Werkzeuge mit dem Eintrag Absenzen, der die eigenen Termine, Absenzen, Abmeldungen, Dispense und Rekurse aller Kurse mit Absenzenmanagement zeigt](assets/pers_menu_absences_v3_de.png){ class="aside-right lightbox"}

![Symbol Absenzen](assets/icon_absences.png)

Ist das Modul Termine und Absenzen eingeschaltet, sehen Sie im persönlichen Menü unter "Absenzen" die Kurse, in denen das Absenzenmanagement verwendet wird. Alle Benutzer:innen können dort ihre eigenen Absenzen ansehen und, soweit erlaubt, bearbeiten.

Angezeigt werden nicht nur Ihre persönlichen Absenzen in diesen Kursen (Termine), sondern der Übersicht halber auch alle Termine, die zum Gesamtprogramm der Kurse gehören und regulär zu besuchen wären.

Ausserdem werden Ihnen Abmeldungen, Dispense und Rekurse angezeigt.

Die Ansichten sind auf bis zu vier Tabs verteilt. Die Tabs "Abmeldung / Dispense" und "Rekurse" erscheinen nur, wenn Systemadministrator:innen Abmeldungen bzw. Rekurse eingeschaltet haben. Oberhalb der Tabs steht der Button "Abmeldung", sofern Teilnehmer:innen sich selbst abmelden dürfen (siehe Tab Abmeldung / Dispense).

![Die vier Tabs Tagesübersicht, Termine und Absenzen, Abmeldung / Dispense und Rekurse sowie rechts oben der Button Abmeldung, beide markiert](assets/pers_menu_absences_tabs_v1_de.png){ class="shadow lightbox" title="Absenzen in den persönlichen Werkzeugen" }

## Tab Tagesübersicht {: #tab_overview}

Im Tab "Tagesübersicht" sehen Sie die Termine und eventuelle Absenzen des aktuellen Tages. Um einen anderen Tag anzuzeigen, wählen Sie rechts oben über der Tabelle den gewünschten Tag aus.

![Lektionen des gewählten Tages nach Zeit, Kurs, Lektionenblock und Ort, rechts oben die markierte Datumsauswahl mit Pfeilen für den Tageswechsel](assets/pers_menu_absences_day_v2_de.png){ class="shadow lightbox" title="Tab Tagesübersicht in den persönlichen Werkzeugen" }

[Zum Seitenanfang ^](#pers_tools_absences)

---

## Tab Termine und Absenzen {: #tab_events_absences}

Sie erfahren hier, wie viele Termine pro Kurs erfasst sind und wie sich Ihre Anwesenheit bzw. Abwesenheit pro Kurs konkret verteilt. Auch der bisherige Fortschritt wird angezeigt. Dabei steht grün für Anwesenheit in einer Einheit, orange für "entschuldigt", rot für "unentschuldigt abwesend" und grau für "dispensiert". Darüber hinaus können über die Option "Details" weitere Einzelheiten angezeigt werden. In der Spalte mit dem Warndreieck erscheint ein rotes Ausrufezeichen, wenn die Anwesenheitsquote unter das geforderte Minimum fällt. Oberhalb der Tabelle finden Sie die Buttons "Drucken" und "Log".

![Eine Zeile pro Kurs mit Einheiten, Anwesend, Unentschuldigt, Entschuldigt, Dispensiert, Fortschrittsbalken und Anwesenheitsquote, darüber die Buttons Drucken und Log](assets/pers_menu_absences_lectures_v2_de.png){ class="shadow lightbox" title="Tab Termine und Absenzen in den persönlichen Werkzeugen" }

Die Liste ist vollständig: Sie führt Ihre Termine unabhängig davon, woher der Kurs kommt. Gehören Kurse zu einem Bildungsprodukt des Course Planners, trennt die Liste sie in die Abschnitte **Absenzen innerhalb eines Produkts** und **Absenzen ausserhalb eines Produkts**. Termine aus Projekten erscheinen hier nicht, sie werden im Projekt selbst geführt.

[Zum Seitenanfang ^](#pers_tools_absences)

---

## Tab Abmeldung / Dispense {: #tab_notices_dispensation}

Systemadministrator:innen können in der System-Administration unter `Administration > Module > Termine / Absenzen`, Tab "Berechtigungen", die Option "Teilnehmer:innen dürfen sich abmelden" einschalten. Dann erscheint rechts oben der Button "Abmeldung", über den Sie sich selbst von Terminen abmelden. Ansonsten zeigt diese Liste nur die Abmeldungen und Dispense, die Dozent:innen oder Absenzenverwalter:innen für Sie erfasst haben.

![Erfasste Abmeldungen und Dispense je Kurs mit Einheiten, Dozenten, Datum, Von, Bis, Begründung und Art, dazu der Filter Anzeige mit Alle oder Unentschuldigt](assets/Abmeldung_Dispense.jpg){ class="shadow lightbox" title="Tab Abmeldung / Dispense in den persönlichen Werkzeugen" }

[Zum Seitenanfang ^](#pers_tools_absences)

---

## Tab Rekurse {: #tab_appeals}

Hier sind die eigenen Rekurse aufgelistet. Wer ausser Ihnen sonst noch Ihre Rekurse einsehen darf (Dozent:innen, Klassenlehrer:innen), legen Systemadministrator:innen in der System-Administration fest: `Administration > Module > Termine / Absenzen`, Tab "Berechtigungen".

![Leere Rekursliste mit der Meldung, dass kein Rekurs den Kriterien entspricht, rechts oben das Filter-Icon](assets/pers_menu_absences_appeals_v2_de.png){ class="shadow lightbox" title="Tab Rekurse in den persönlichen Werkzeugen" }

Sind Sie mit einer eingetragenen Absenz nicht einverstanden, können Sie einen Rekurs einreichen. Nach dem Ende des Termins erscheint das Datum, ab dem der Rekurs möglich ist: die Endzeit des Termins plus die Tage der Sperrfrist. Sobald der Termin automatisch (nach Ablauf der Sperrfrist) oder manuell durch die Dozent:innen auf "Erledigt" gesetzt ist, erscheint das Datum, bis zu dem der Rekurs eingereicht werden kann (Rekursfrist). Anschliessend wird "Geschlossen" angezeigt. Sperrfrist und Rekursfrist legen Systemadministrator:innen systemweit fest, in der System-Administration unter `Administration > Module > Termine / Absenzen`, Tab "Konfiguration". Der Rekurs wird an die Dozent:innen des Termins gesendet.

[Zum Seitenanfang ^](#pers_tools_absences)

---

## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Termine und Absenzen (Basiskonzept) >](../basic_concepts/Events_and_Absences.de.md)<br>
[Modul Termine und Absenzen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Kurseinstellungen - Tab Durchführung >](../learningresources/Course_Settings_Execution.de.md)<br>
[Termine und Absenzen (Kurs) >](../learningresources/Events_and_absences.de.md)<br>
[Toolbar: Termine >](../learningresources/Toolbar_Events.de.md)<br>
[Coaching - Termine und Absenzen >](../area_modules/Coaching_Events_Absences.de.md)<br>
[Coaching - Übersicht >](../area_modules/Coaching.de.md)<br>
[Absenzenverwaltung >](../area_modules/Absence_Management.de.md)

[Zum Seitenanfang ^](#pers_tools_absences)
