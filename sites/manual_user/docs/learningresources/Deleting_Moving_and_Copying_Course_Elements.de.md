# Löschen, Verschieben und Kopieren von Kursbausteinen

Änderungen an Ihrem Kurs nehmen Sie im Kurseditor vor. Sie gelangen dorthin, indem Sie den Kurs starten und `Kurs > Administration > Kurseditor` wählen.

![Menü Administration eines gestarteten Kurses mit dem Eintrag Kurseditor](assets/Kurseditor_link_19.png){ class="shadow lightbox" }

Um einen Kursbaustein zu löschen, zu duplizieren oder zu verschieben, müssen Sie den gewünschten Kursbaustein zunächst auswählen. Anschliessend erscheint rechts oben das entsprechende Menü.

![3-Punkte-Menü eines markierten Kursbausteins mit den Einträgen Verschieben und Duplizieren, neben dem Button Löschen](assets/Kurseditor_verschieben.png){ class="shadow lightbox" }

Die jeweilige Aktion bezieht sich dabei auf den aktuell markierten und alle ihm untergeordneten Kursbausteine. Beide Aktionen öffnen denselben Dialog. Unter **Zielposition** wählen Sie den Kursbaustein aus, an dem Sie den markierten Kursbaustein einsetzen wollen; der zu verschiebende Kursbaustein ist farblich hervorgehoben und lässt sich nicht als Ziel auswählen. Am gewählten Kursbaustein erscheinen die Aktionen **Oben** für die Position oberhalb, **Unten** für die Position unterhalb und **Unterelement** für die untergeordnete Position. Nach der Wahl einer Aktion markiert **Wird hier landen** das Ziel. Erst dann können Sie die Aktion mit **Kursbaustein einfügen** ausführen.
Ebenso ist es möglich, Kursbausteine einfach mittels „Drag&Drop“ in der Kursstruktur links zu verschieben.

![Zielpositionen als Radiobuttons, Aktionen Oben, Unten und Unterelement am gewählten Kursbaustein, im Dialog zur Auswahl der Position im Kurseditor](assets/deleting_moving_copying_move_dialog_v1_de.png){ class="shadow lightbox" }

Das Duplizieren von Kursbausteinen empfiehlt sich beispielsweise, wenn Sie Gruppenaktionen im Kurs anbieten und dieselbe Struktur für mehrere Gruppen verwenden möchten.

Die Änderungen zum Löschen, Verschieben und Kopieren von Kursbausteinen müssen zum Schluss publiziert werden, um sie für die Teilnehmenden wirksam werden zu lassen. Solange Sie diese nicht publiziert haben, können gelöschte Kursbausteine wiederhergestellt werden.


## Kursbausteine importieren [:octicons-tag-16:{ title="ab Release 16.1.0 (OO-5210)" }](https://track.frentix.com/issue/OO-5210)

Haben Sie in einem anderen Kurs bereits eine umfangreiche Kursstruktur angelegt die Sie weiterverwenden wollen, bietet es sich an, diese Kursbausteine über "Kursbausteine importieren" in den gewünschten Kurs zu kopieren.

![Schaltfläche Kursbausteine importieren in der Werkzeugleiste des Kurseditors](assets/KB_importieren.png){ class="shadow lightbox" }

Anschliessend öffnet sich ein Wizard.

### Der Weg:

![Vier Schritte des Wizards Kursbausteine importieren: Kurs auswählen, Kursbausteine auswählen, Kursbausteine bestätigen, Dateien auswählen](assets/Weg_importieren_KB.png){ class="shadow lightbox" }

a) Wählen Sie den gewünschten Kurs in dem sich der oder die zu kopierenden Kursbausteine befinden.

b) Markieren Sie den oder die Kursbausteine, die Sie übertragen wollen. Untergeordnete Kursbausteine werden automatisch mitausgewählt, können aber bei Bedarf durch Entfernung des Hakens wieder abgewählt werden.

c) Es werden alle gewählten Kursbausteine noch einmal angezeigt. Bei einigen Kursbausteinen wie Podcast, Blog, Wiki, Aufgabe, Gruppenaufgabe oder Ordner können noch weitere Einstellungen für den Kopiervorgang vorgenommen werden. Zum Beispiel können die Dateien des Kursbausteins Ordner mitkopiert werden. Ein Blog, Wiki oder Podcast kann entweder wiederverwendet, neu erstellt oder für den Moment erst mal nicht weiter konfiguriert werden. Bei Aufgaben und Gruppenaufgaben kann die hinterlegte Aufgabenstellung und die Musterlösung mitkopiert werden oder nicht.

d) Im nächsten Schritt erscheinen die Dateien, die sich im Ablageordner des zu kopierenden Kurses befinden und können bei Bedarf ausgewählt werden. Dabei sind die Dateien, die mit den ausgewählten Kursbausteinen verbunden sind bereits vorausgewählt. Eine Änderung der Einstellung ist aber an dieser Stelle möglich.

**Bitte beachten:**

* Beim Kopieren der Kursbausteine werden keine Gruppen mitkopiert. Für Gruppenaufgaben, Einschreibungen müssen also entweder neue Gruppen erstellt oder später vorhandene Gruppen verknüpft werden.

* Beim Kopieren von Foren werden die Forenbeiträge nicht mitkopiert. 

* Bei der Kopie von BigBlueButton werden keine Räume und Termine mitkopiert.

## Änderungen am laufenden Kurs

Sie entscheiden über den Zeitpunkt, an dem die Änderungen im laufenden Kurs erscheinen. Alle Benutzer:innen, die zum Zeitpunkt des Publizierens den Kurs bearbeiten, müssen den Kurs neu starten. Nicht gespeicherte Forumsbeiträge oder Testresultate gehen dabei verloren! Wenn Benutzer:innen im Kurs sind und Sie das Publizieren auf einen späteren Zeitpunkt verschieben können, empfehlen wir, den Publiziervorgang abzubrechen und später zu wiederholen.

## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Kursbausteine im Kurseditor >](General_Configuration_of_Course_Elements.de.md)<br>
[Kursbausteine >](Course_Elements.de.md)

[Zum Seitenanfang ^](#loschen-verschieben-und-kopieren-von-kursbausteinen)