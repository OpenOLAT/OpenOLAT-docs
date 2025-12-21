# Katalog 1.0 {: #catalog_1}

:octicons-device-camera-video-24: **Video-Einführung**: [Katalog](<https://www.youtube.com/embed/LiqkkT06hWo>){:target="_blank”}

:octicons-device-camera-video-24: **Video-Einführung**: [Kurs in Katalog eintragen](<https://www.youtube.com/embed/hc5yJAPIX9s>){:target="_blank”}

## Funktionsweise des Katalog 1.0

Im Katalog 1.0 können Kursbesitzer:innen ihre Kurse eintragen und diese so inklusive hinterlegter vorab Informationen sichtbar machen. 

Je nach Konfiguration des Kurses können die Kurse im Katalog gebucht werden oder User finden hier Kurse in die sie von den Kursbesitzer:innen eingetragen wurden. 

Der Katalog kann auch verwendet werden um bestimmte Strukturen einer Einrichtung z.B. einer Hochschule abzubilden und die OpenOlat Kurse sinnvoll zuzuordnen und zu strukturieren. User erhalten so schnell einen Überblick über Kurse, die sie buchen können oder in die sie bereits eingetragen wurden.

**Verwaltung durch Katalogverwalter:innen:**

Der Katalog 1.0 wird von OpenOlat Administrator:innen oder Katalogverwalter:innen eingerichtet. 

![Katalogverwaltung](assets/Katalogverwaltung1.png){ class="shadow lightbox" }

Autor:innen können dann ihre Kurse innerhalb der vordefinierten Struktur verknüpfen. Die Reihenfolge der Katalogeinträge wird von Administrator:innen bzw. Katalogverwalter:innen festgelegt.


## Kurs in den Katalog 1.0 eintragen:

Gehen Sie als Kursbesitzer:in in die Kursadministration und wählen Sie den Tab „Katalog“. Klicken Sie auf den Button „In Katalog einfügen“ und navigieren Sie zu der gewünschten Stelle im Katalog. 

![Katalog 1 - in Katalog einfügen](assets/Katalog1a.jpg){ class="shadow lightbox" }

Anschliessend wird angezeigt für wen der Kurs im aktuellen Zustand sichtbar ist.  Sie können den Vorgang auch wierholen und so mehrere Katalogeinträge für einen Kurs vornehmen.  

**Weitere Einstellungen:**

Gehen Sie als Kursbesitzer:in in der Kursadministration in den Tab „Freigabe“ um die gewünschten Einstellungen vorzunehmen. 

![Einstellungen Tab Freigabe](assets/Einstellungen_Tab_Freigabe1.jpg){ class="shadow lightbox" }

!!! Tip „Tipp“

    Häufig ist es sinnvoll den Eintrag in den Katalog als letzten Schritt vorzunehmen. Nämlich dann, wenn der Kurs fertiggestellt und der Zugang für die Lernenden freigegeben werden soll. 
    Setzen Sie den Status des Kurses auf „veröffentlicht“ damit die Teilnehmenden den Kurs auch betreten können. 


## Wer sieht was im Katalog 1.0?

Kurse können jederzeit in den Katalog eingetragen werden, sind aber nicht immer für *jeden* sichtbar bzw. zugänglich. Die Frage ist also wodurch die Sichtbarkeit im Katalgo beeinflusst wird? Zu nennen sind hier: 
* Die Kurs-Rolle der Person, die den Kurs aufruft,
* der Veröffentlichungsstatus des Kurses
* die Art der Freigabe des Kurses (privat oder buchbar). 

Benutzerrolle| Freigabeeinstellung| Publikationsstatus  
---|---|---  
Besitzer der Lernressource| Privat, Buchbar, Offen| immer sichtbar  
Betreuer der Lernressource| Privat, Buchbar, Offen|  "Freigabe Betreuer", "Veröffentlicht" oder "Beendet"  
Teilnehmer der Lernressource| Privat, Buchbar, Offen| "Veröffentlicht" oder "Beendet"  
Alle OpenOlat Benutzer| Buchbar, Offen| "Veröffentlicht" oder "Beendet"  
Gäste| Offen & Gastzugang aktiviert| "Veröffentlicht" oder "Beendet"  

Hier noch zwei Beispiele wie sich die Einstellungen der Konfiguration auf den Katalog auswirken: 

### Beispiel 1: 

Ein Kurs wurde vom Kursbesitzer im Katalog eingetragen. Der Kurs hat den Status „Vorbereitung“ und steht bei der Freigabe auf „Privat Mitgliederverwaltung durch Administration“. 

In diesem Fall erscheint der Kurs für die Kursbesitzer:innen und sämtliche eingetragene Mitglieder im Katalog. Allerdings kommen die Mitglieder noch nicht in den Kurs rein, da dieser noch auf *„Vorbereitung“* steht. 
Sobald der Kurs veröffentlicht wird, können alle Mitglieder der Kurs auch über den Katalog betreten. 

Personen die nicht Mitglied im Kurs sind sehen den Kurs im Katalog *nicht* und können den Kurs nicht betreten, sich nicht eintragen und ihn auch nicht buchen.

### Beispiel 2: 

Ein Kurs wurde von der Kursbesitzerin im Katalog eingetragen und mit einer Buchungsmethode (Angebot mit Zugangscode) versehen. Solange der Kurs noch den Status „Vorbereitung“ hat ist er im Katalog für andere Personen nicht zu finden. 

Setzt man den Status auf „Veröffentlicht“ erscheint der Kurs Im Katalog und die Infos aus der Kursinfo sind für alle OpenOlat User sichtbar. Aber in den Kurs selbst gelangen nur die Personen, die auch über den Zugangscode verfügen und ihn sie buchen können.

### Beispiel 3

Soll ein Kurs im Katalog erscheinen damit sich die Interessenten oder Teilnehmenden in den Kurs eintragen können, sollten Sie ihn wie folgt konfigurieren.   

* Kurs wie oben beschrieben im Tab "Katalog" hinzufügen.
* im Tab Freigabe der Einstellungen ein Angebot "frei verfügbar" hinzufügen. Eventuell bei der Konfiguration des Angebots ein Enddatum eintragen. Hilfreich sind noch eine Angebotsbeschreibung und das Entfernern des Hakens bei "Automatisch Buchen"
* Kurs Status muss auf "Vorbereitung" stehen bzw. sollte nicht auf "Veröffentlicht" gesetzt sein.

So könnnen sich User die Kurs-Info-Seite durchlesen und sich in den Kurs eintragen. Teilnehmenden in den Kurs eintragen und Kursbesitzende sehen alle Personen, die sich eingetragen haben in der Mitgliederverwaltung des Kurses und können hier bei Bedarf auch Personen enternfen oder per Mail kontaktieren. Aber die Teilnehmenden selbst haben noch keinen Zugang zum Kurs mit den Inhalten und Kursbausteinen. Dies erfolgt erst, wenn die Kursbesitzenden den Kurs auf "veröffentlicht" setzen. 

## So gelangen User zum Katalog

User können den Katalog 1.0 über das obere Menü aufrufen und zur gewünschten Stelle navgieren. Die Darstellung ist sowohl als Listen- als auch als Tabellenansicht möglich. Angezeigt werden dabei jeweils weitere Informationen z.B. zum Lernfortschritt in Lernerlebnispfaden, dem Durchführungsformat, dem Zeitabschnitt, ob der Kurs bereits bestanden wurde sowie weitere  Informationen, die in den Kurseinstellungen hinterlegt wurden. Über den Button "Mehr erfahren" gelangen User zur Kursinfo-Seite. 

Verwenden Sie die Suchmaske, wenn Sie den gewünschten Kurs im Katalog nicht finden. Möglicherweise hat der Besitzer bzw. die Besitzerin den Kurs noch nicht in den Katalog eingetragen.

![Katalog Beispiel](assets/Katalog_Lernerlebnispfad.png){ class="shadow lightbox" }

!!! info "Katalog 2.0"

    Informationen zum Erstellen von Angeboten im Katalog 2.0 finden Sie [hier](../area_modules/catalog2.0_angebote.de.md). 