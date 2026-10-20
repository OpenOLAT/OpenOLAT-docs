# Bewertungswerkzeug: Tab Teilnehmer:innen {: #assessment_tool_users}

Sie haben zwei generelle Möglichkeiten die Bewertung im Bewertungswerkzeug vorzunehmen. Entweder Sie gehen von einer Person aus und bewerten die von dieser Person vorgenommenen Bearbeitungen. Oder Sie gehen von der Kursstruktur und einem konkreten Assessment Baustein aus und bewerten alle Personen für diese Aufgabe, diesen Test bzw. sonstigen Assessment Kursbaustein. 

In der linken Spalte im Bewertungswerkzeug sehen Sie die Kursstruktur mit allen bewertbaren Kursbausteinen. Hier können Sie direkt zu einem der Kursbausteine navigieren um Ihre Bewertung vorzunehmen. Für jeden Kursbaustein wird ein Tab mit der "Übersicht" und ein Tab mit den "Teilnehmer:innen" angezeigt. 

![Links die Kursstruktur, rechts die Tabs Übersicht und Teilnehmer:innen eines Tests, darunter Buttons, Filter und die Liste der Teilnehmenden mit Versuchen, Punkten, Bestanden und Status](assets/assessing_tests_participants_buttons_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen des Kursbausteins Test im Bewertungswerkzeug · 2026.10.07" }

Die genaue Vorgehensweise wird in den Kapiteln [Lernende bewerten](../learningresources/Assessment_of_learners.de.md) und [Bewertung von Kursbausteinen](../learningresources/Assessment_of_course_modules.de.md) beschrieben.

---


## Teilnehmer:innen suchen {: #assessment_tool_participants}

Im Tab "Teilnehmer:innen" werden alle Teilnehmenden aufgelistet, die bewertet werden können. Sie können nach diversen Kriterien gefiltert werden. Z.B. alle Teilnehmenden, die diesen Kursbaustein noch "nicht bestanden" haben oder alle Teilnehmende einer bestimmten Gruppe. Ferner kann nach einzelnen Personen gesucht werden.


### Anzeige und Spaltenauswahl {: #display_column}

Die Informationen, die im Tab "Teilnehmer:innen" angezeigt werden, können über die Auswahl der gewünschten Spalten weiter angepasst werden. Klicken Sie hierfür auf das Zahnrad.

Die konkreten Anzeige-Optionen variieren je nach Assessment-Baustein. Neben Basisinformationen wie Name oder Matrikelnummer, können hier auch Informationen zum Status oder der letzten Aktualisierung eingeblendet werden. Eine Spaltenanpassung ist also hilfreich um einen schnellen Überblick zu erhalten. Besonders die Informationen zu den Punkten, den Versuchen, dem Status, und der letzten Aktualisierung werden häufig benötigt. 

Richten Sie sich die Spalten so ein, wie es für Ihren Kontext sinnvoll ist und schauen Sie in den Einstellungen nach ob diese auch aktiviert ist, wenn Sie mal eine Information vermissen.

Hier Beispiele für die Spaltenauswahl per Zahnrad: 

![Auswählbare Spalten wie Benutzername, Punkte, Status, Letzte Aktualisierung und Zertifikat mit Kontrollkästchen](assets/Bewertungswerkzeug_Struktur_Spalte_172.png){ class="shadow lightbox" title="Spaltenauswahl für den Kursbaustein Struktur" }

Kursbaustein "Struktur"

![Auswählbare Spalten wie Versuche, Freigabe Bewertung, Min., Max., Punkteschwelle, Punkte, Bestanden und Fortschritt mit Kontrollkästchen](assets/Bewertungswerkzeug_test_Spalte_172.png){ class="shadow lightbox" title="Spaltenauswahl für den Kursbaustein Test" }

Kursbaustein "Test"

![Auswählbare Spalten wie Versuche, Freigabe Bewertung, Punkte, Bestanden, Aufgabe und Status mit Kontrollkästchen](assets/Bewertungswerkzeug_aufgabe_Spalte_172.png){ class="shadow lightbox" title="Spaltenauswahl für den Kursbaustein Aufgabe" }

Kursbaustein "Aufgabe"  

[Zum Seitenanfang ^](#assessment_tool_users)

---


### Erreichte Punkte einsehen {: #points}

Um als Betreuer:in nachzuschauen, wie viele Punkte bestimmte Teilnehmer:innen erreicht haben, öffnen Sie im betreffenden Kurs das Bewertungswerkzeug: `Kurs > Administration > Bewertungswerkzeug`. Die Übersicht führt mit einem Klick auf eine der Zahlen zu einer vorgefilterten Liste, zum Beispiel zu allen Personen, die bestanden haben. Ist eine Liste geöffnet, klicken Sie auf den Namen der betreffenden Person.

![Kursstruktur links und die Links zu vorgefilterten Listen wie Anzahl Teilnehmende, Bestanden, Nicht bestanden und Mitglieder hervorgehoben](assets/assessment_tool_tab_users_points1_v1_de.png){ class="shadow lightbox" title="Übersicht des Bewertungswerkzeugs" }


#### Punkte des gesamten Kurses

Um die Punkte für den Gesamtkurs zu sehen, wählen Sie links den Namen des Kurses und dann den Tab "Teilnehmer:innen".

![Spalte Punkte mit den Punkten des Gesamtkurses je Person hervorgehoben](assets/assessment_tool_tab_users_points2_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen des obersten Kursbausteins im Bewertungswerkzeug" }

Vergebene Punkte zählen erst zur Gesamtpunktzahl des Kurses, wenn die Bewertung freigegeben ist. In einem Lernpfadkurs legen die Kurseinstellungen fest, ob Betreuer:innen eine Bewertung selbst freigeben dürfen: `Kurs > Administration > Einstellungen > Tab "Bewertung"`, Abschnitt "Berechtigungen", Option "Bewertung freigeben" unter "Betreuende können". Mehr dazu im [Abschnitt Berechtigungen](Course_Settings_Assessment.de.md#section_assessment_rights).

Damit Betreuer:innen trotzdem sehen, wie viele Punkte eine Person nach der Freigabe hat, stehen in der Bewertung der Person die noch nicht freigegebenen Punkte in Klammern. Diese Ansicht öffnet ein Klick auf den Namen der Person. In einem Lernpfadkurs zeigt die Zeile des Kurses zuerst die Gesamtpunktzahl aus den freigegebenen Bewertungen, dahinter in Klammern die Gesamtpunktzahl nach der Freigabe aller Bewertungen. [:octicons-tag-16:{ title="ab Release 20.1.2 (OO-8839)" }](https://track.frentix.com/issue/OO-8839)

In Klammern stehen auch Punkte, die nicht zur Gesamtpunktzahl zählen. Ein Klick auf einen Wert mit Info-Symbol zeigt, warum er in Klammern steht.

Das folgende Beispiel zeigt die Bewertung einer Person in einem Lernpfadkurs, in dem noch nicht alle Bewertungen freigegeben sind.

![Spalte Punkte mit nicht freigegebenen Punkten in Klammern, beim Kurs die Gesamtpunktzahl nach Freigabe aller Bewertungen](assets/assessment_tool_tab_users_points3_v1_de.png){ class="shadow lightbox" title="Bewertung einer Person im Bewertungswerkzeug" }

Die Werte in der Spalte "Punkte" bedeuten im Beispiel:

* **Musterkurs A** (Zeile des Kurses): "9 (21)" heisst, 9 Punkte sind vergeben und freigegeben. Sind alle vergebenen Punkte freigegeben, hat die Person 21 Punkte.
* **Test**: "(12)" heisst, 12 Punkte sind vergeben, aber noch nicht freigegeben.
* **Aufgabe**: "9" ohne Klammer heisst, 9 Punkte sind vergeben und freigegeben.

#### Punkte eines bestimmten Kursbausteins

Um die Punkte nur für einen bestimmten Kursbaustein zu sehen, wählen Sie links den Kursbaustein und dann im Tab "Teilnehmer:innen" die gewünschte Person.

Bei einem Test öffnet sich damit die Liste der Testversuche dieser Person. Dort zeigt die Spalte "Punkte" das Ergebnis, "Punkte (Auto)" den automatisch errechneten Anteil samt allfälliger Anpassungen und "Punkte (Manuell)" den von Hand vergebenen Anteil. Wie die Liste aufgebaut ist und wie Sie von dort aus korrigieren, steht auf der Seite [Tests bewerten](Assessing_tests.de.md#test_runs). [:octicons-tag-16:{ title="ab Release 21.1 (OO-9599)" }](https://track.frentix.com/issue/OO-9599)

[Zum Seitenanfang ^](#assessment_tool_users)

---


## Weitere Optionen aktivieren {: #further_options}

Nach Auswahl einer oder mehrerer Personen eines Assessment Bausteins erscheinen weitere Funktionen z.B. kann der Status auf abgeschlossen gesetzt werden, die Sichtbarkeit aktiviert werden, eine E-Mail versendet oder ein Test verlängert werden. Je nach Assessment-Kursbaustein variieren die Möglichkeiten.

![Buttons Auf Status abgeschlossen setzen, Sichtbar setzen und E-Mail erscheinen nach Auswahl von zwei Personen](assets/Bewerungswerkzeug_Funktionen_erscheinen.png){ class="shadow lightbox" title="Liste der Teilnehmenden im Bewertungswerkzeug" }

[Zum Seitenanfang ^](#assessment_tool_users)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Lernende bewerten >](Assessment_of_learners.de.md)<br>
[Bewertung von Kursbausteinen >](Assessment_of_course_modules.de.md)<br>
[Kurseinstellungen - Tab Bewertung >](Course_Settings_Assessment.de.md)<br>
[Tests bewerten >](Assessing_tests.de.md)

**Weiterführend**<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview.de.md)<br>
[Das Bewertungsformular >](The_assessment_form.de.md)

[Zum Seitenanfang ^](#assessment_tool_users)

