# Angebotskonzepte {: #offer_concepts}

## Was ist ein Angebot? {: #offers}

Sind Kurse und andere Lerninhalte in OpenOlat erstellt, muss bestimmt werden, **welche** Benutzer:innen **wann** darauf Zugriff haben sollen. Die Gewährung des Zugriffs (Freigabe) kann auf 2 Arten erfolgen:

* **Privat:** Durch Eintrag in der Mitgliederverwaltung der (Kurs-)Administration werden registrierte OpenOlat-Benutzer:innen zu Mitgliedern des Kurses oder der Lernressource und können dann darauf zugreifen.

* **Buchbare und offene Angebote:** Einem Kurs wird von dem/der Besitzer:in (Autor:in) ein Angebot hinzugefügt. Dieses Angebot finden Benutzer:innen dann im Katalog und können dort die Mitgliedschaft durch eine Buchung des Angebots selbst initiieren.<br>
Für den gleichen Kurs können auch mehrere verschiedene Angebote für verschiedene Zielgruppen erstellt werden.<br>
So kann z.B. für interne Benutzer:innen ein Kurs kostenlos angeboten werden, während ein zweites Angebot den gleichen Kurs kostenpflichtig für Externe anbietet.
Angebote können auch nur für bestimmte Organisationseinheiten im Katalog angezeigt werden. Ebenso aber auch für alle offen, es muss nicht einmal eine Mitgliedschaft geben.

**Beispiel für Kursangebote im Katalog:**
![offer_concepts_example_v1_de.png](assets/offer_concepts_example_v1_de.png){ class=" shadow lightbox" }

[Mehr zu Angeboten >](../../manual_user/area_modules/catalog2.0_angebote.de.md)

[zum Seitenanfang ^](#offer_concepts)

---


## Was kann in Angeboten gezeigt werden? {: #offers_card}

Der sichtbare Teil des Angebots wird als Karte im Katalog sichtbar (bzw. in der Listenansicht).
(Der unsichtbare Teil eines Angebots umfasst die Regeln: Wann wird das Angebot wo angezeigt?)

Was auf einer Karte im Katalog angezeigt wird, kann (für alle Karten einheitlich) von Administrator:innen festgelegt werden unter<br>
**Administration > Module > Katalog > Tab Layout > Abschnitt Launchers**

* Durchführungsformat
* Zertifikat
* Kreditpunkte
* Kennzeichen
* Typ
* Titel
* Teaser
* Autor:innen
* Zeitaufwand
* Hauptsprache
* Durchführungszeitraum
* Durchführungsort
* Fachbereiche /Katalog

[zum Seitenanfang ^](#offer_concepts)

---


## Wo können Angebote gezeigt werden? {: #show_offers}

In OpenOlat gibt es einen **internen** und einen **externen** Katalog. Es kann bestimmt werden, ob ein Angebot nur in einem oder in beiden Katalogen angezeigt wird.

Innerhalb des Katalogs gibt es Abschnitte, sogenannte **Launcher**. Als Besitzer:in eines Kurses oder einer Durchführung können Sie bestimmen, in welchem Launcher Ihr Angebot erscheinen soll. Vom Katalog (V2) werden die Angebote dann dynamisch zusammengestellt und den verschiedenen Launchern zugeordnet. 

Eine Anzeige kann auch **in mehreren verschiedenen Launchern des Katalogs** (V2) erfolgen. Z.B. in einem Launcher "Beliebte Kurse" und einem Launcher, der thematisch Kurse anhand einer bestimmten Taxonomie zusammenstellt. 

Angebote können auch in Katalogbereichen (Launchern) angezeigt werden, die **nur für Mitglieder bestimmter Organisationseinheiten** sichtbar sind. (Voraussetzung ist, dass das Modul "Organisationen" aktiviert ist.)

Die Freigabe-Einstellungen können vorgenommen werden unter<br>
**Kurs/Durchführung > Administration > Einstellungen > Freigabe > Abschnitt Angebote > Link "Angebot editieren"**

![offer_concepts_share_org_v1_de.png](assets/offer_concepts_share_org_v1_de.png){ class=" shadow lightbox" }

!!! hint "Hinweis"

    Die Angebote sind im Katalog buchbar, sobald der Status auf "Veröffentlicht" gestellt wurde.

!!! tip "Tipp"

    Innerhalb eines Launchers kann auch eine Sortierung vorgenommen werden. 
    [Mehr dazu >](../../manual_user/area_modules/catalog2.0_sort_offers.de.md)

[zum Seitenanfang ^](#offer_concepts)

---


## Wo werden Angebote erstellt? {: #create_offers}

Angebote werden erstellt

* im Kurs <br>oder
* in einer Durchführung (innerhalb des Course Planners) 

### Angebotserstellung im Kurs {: #create_offers_course}

Um einen **Kurs** im Katalog anzubieten, wählen Sie den betreffenden Kurs und dann<br> 
**Administration > Einstellungen > Freigabe > Bereich "Angebote"**

![offer_concepts_create_offer_course_v1_de.png](assets/offer_concepts_create_offer_course_v1_de.png){ class=" shadow lightbox" }

!!! hint "Tipp"

    Sind Angebote erstellt worden, können sie auch in der **(Kurs-)Administration unter "Angebotsarten"** nachgesehen werden.


### Angebotserstellung im Course Planner {: #create_offers_implementation}

Um eine **Durchführung** im Katalog anzubieten, wählen Sie die betreffende Durchführung im Course Planner und dann den<br>
**Tab Katalog > Button Angebote**

![offer_concepts_create_offer_implementation_v1_de.png](assets/offer_concepts_create_offer_implementation_v1_de.png){ class=" shadow lightbox" }

[zum Seitenanfang ^](#offer_concepts)

---


## Die Angebotsarten/-typen {: #offer_types}

Es können die folgenden Angebotsarten/-typen erstellt werden:

|                       | Mitgliedstatus  |                                 | verfügbar in |
| --------------------- | --------------- |-------------------------------- | --- |
| <b>Ohne Buchung</b>    | ohne  |Mit diesem Angebot ist die Ressource ohne eine Mitgliedschaft für Benutzer:innen zugänglich. | Einzelkurs |
| <b>Frei verfügbar</b>  | Mitgliedschaft | Mit diesem Angebot ist die Ressource buchbar. Die Benutzer:innen erhalten eine entsprechende Mitgliedschaft, die ihnen den Zugang zur Ressource ermöglicht. | Einzelkurs und Durchführung |
| <b>Zugangscode</b> | Mitgliedschaft | Mit diesem Angebot ist die Ressource mit einem Zugangscode buchbar. Die Benutzer:innen erhalten eine entsprechende Mitgliedschaft, die ihnen den Zugang zur Ressource ermöglicht. | Einzelkurs und Durchführung |
| <b>PayPal Checkout</b> | Mitgliedschaft | Mit diesem Angebot ist die Ressource mit PayPal kostenpflichtig buchbar. Die Benutzer:innen erhalten eine entsprechende Mitgliedschaft, die ihnen den Zugang zur Ressource ermöglicht. | Einzelkurs und Durchführung |
| <b>Rechnung</b> | Mitgliedschaft | Mit diesem Angebot ist die Ressource per Rechnung kostenpflichtig buchbar. Die Benutzer:innen erhalten eine entsprechende Mitgliedschaft, die ihnen den Zugang zur Ressource ermöglicht. | Durchführung |

[Mehr über die Angebotstypen >](../../manual_user/learningresources/Access_configuration.de.md#angebotsoptionen)

[zum Seitenanfang ^](#offer_concepts)

---


## Was kann angeboten werden? {: #what_is_offered}

In den Katalog können Angebote aufgenommen werden für

- Kurse
- Durchführungen
- sonstige Lernressourcen


### Kurse anbieten {: #what_is_offered_courses}

Angebote zu einem Kurs werden erstellt unter<br>
**(Kurs-)Administration > Einstellungen > Freigabe > Abschnitt "Angebote"**<br>
Beachten Sie, dass zuvor bei "Zugang für Teilnehmer:innen" die Option "Buchbare und offene Angebote" gewählt werden muss.

![offer_concepts_types_course1_v1_de.png](assets/offer_concepts_types_course1_v1_de.png){ class="shadow lightbox" }

![offer_concepts_types_course2_v1_de.png](assets/offer_concepts_types_course2_v1_de.png){ class="shadow lightbox" }

Ausführliche Informationen über das [Anbieten von Kursen im Katalog finden Sie hier >](../../manual_user/area_modules/catalog2.0_angebote.de.md)

[zum Seitenanfang ^](#offer_types)

---


### Durchführungen anbieten {: #what_is_offered_implementations}

Soll der gleiche Kurs mehrmals zu verschiedenen Terminen angeboten werden, kann dies im **Course Planner** mit **Durchführungen** bewerkstelligt werden.

Durchführungen können auch im Katalog ausgeschrieben werden, wenn noch unklar ist, ob die Durchführung überhaupt stattfinden wird. (Z.B. weil sie von der Zahl der Anmeldungen/Buchungen abhängig ist). Ein Angebot für eine Durchführung muss deshalb immer im Course Planner in der jeweiligen Durchführung erstellt werden und nicht in einem Kurs, der für diese Durchführung vorgesehen ist. Kurse können dazu speziell für die Verwendung in Durchführungen vorgesehen werden und haben dann keine eigene Mitgliederverwaltung.

Benutzer:innen können diese Durchführungen buchen, indem sie sich aus dem Katalog heraus anmelden (wenn sie schon OpenOlat-Benutzer:in sind) oder sich neu registrieren (wenn sie eine passende Kursdurchführung im externen Katalog gefunden haben, den sie ohne Registrierung ansehen können).

Wenn aus dem Course Planner heraus ein Angebot im Katalog gemacht wurde, das **mit Rechnung** gebucht werden kann, werden die Interessent:innen beim Anmeldevorgang zur Angabe der Rechnungsadresse usw. geführt. Es wird dabei auch eine Buchungsnummer erstellt. (Stand Release 20.1 ist dies ausschliesslich mit Course Planner möglich.)

Der Buchungsauftrag kann anschliessend bestätigt werden.

Angebote für Durchführungen werden im Course Planner erstellt unter:<br>
(**Course Planner > Durchführung > Tab Katalog > Tab Angebote**)

![offer_concepts_types_course_planner1_v1_de.png](assets/offer_concepts_types_course_planner1_v1_de.png){ class="shadow lightbox" }

![offer_concepts_types_course_planner2_v1_de.png](assets/offer_concepts_types_course_planner2_v1_de.png){ class="shadow lightbox" }

[Mehr über das Anbieten von Durchführungen im Katalog >](../../manual_user/area_modules/Course_Planner_Implementations.de.md#tab_catalog)

[zum Seitenanfang ^](#offer_concepts)

---


### Sonstige Lernressourcen anbieten {: #what_is_offered_other}

Sollen einzelne Videos oder Dokumente im Katalog angeboten werden, können dazu Kurse mit jeweils nur 1 Kursbaustein eingerichtet werden (z.B Kursbaustein Video oder Kursbaustein Dokument). Es ist darauf zu achten, dass beim Aufruf automatisch zum ersten Kursbaustein gewechselt wird.

Das Vorgehen zum Erstellen eines Angebots ist dann identisch mit den Angeboten für andere eigenständige Kurse.

Die Metadaten und Beschreibungen eines solchen "Kurses" können entsprechend nur auf diese enthaltene Lernressource angepasst werden, so dass im Katalog dann z.B. "Video xy" als Angebot erscheint.


[zum Seitenanfang ^](#offer_types)

---

## Angebote mit Bezahlung {: #offer_payed}

### PayPal {: #offer_payed_paypal}

Das PayPal Bezahlungsmodul erlaubt es Autor:innen Lerninhalte gegen Geld freizuschalten. Es muss vorgängig in der Adminstration eingerichtet und freigeschaltet werden.

Nach erfolgreicher Konfiguration des PayPal Moduls können Sie auf der Detailseite des Kurses oder in der Administrationsumgebung der Arbeitsgruppe die PayPal Angebotsart auswählen. 

[Einrichtung des Bezahlungmoduls PayPal (Administration) >](../../manual_admin/administration/Payment_PayPal.de.md)


### Rechnung {: #offer_payed_invoice}

Eine Bezahlung per Rechnung ist derzeit nur für Durchführungen im Course Planner möglich. (Stand Februar 2026)

Bei Angebot mit Rechnung ist

* die Mitgliedschaft sofort aktiv oder
* die Mitgliedschaft ist zunächst ausstehend, bis eine administrative Rolle die Reservierung bestätigt.


![offer_concepts_invoice_membership_v1_de.png](assets/offer_concepts_invoice_membership_v1_de.png){ class="shadow lightbox" }


!!! hint "Tipp"

    Im Course Planner unter<br>
    **Durchführungen > Tab Katalog > Tab Buchungsaufträge**<br> 
    sind die Buchungsaufträge gesammelt und können als Excel-Datei exportiert und in einem anderen Programm (z.B. zur Rechnungserstellung) verwendet werden.  


[Einrichtung des Bezahlungmoduls Rechnung (Administration) >](../../manual_admin/administration/Payment_Invoice.de.md)



### Kreditpunkte {: #offer_payed_credit_points}

Seit Release 20.1 können in OpenOlat Kreditpunktsysteme eingerichtet werden. Ein Kreditpunktesystem ermöglicht das Sammeln von Kreditpunkten über verschiedene Lernangebote hinweg. Über das Modul "Kreditpunkte" können eigene Kreditpunktesysteme global definiert werden. Diese ermöglichen später den Teilnehmenden für das Bestehen von Kursen Bildungspunkte/Credits, wie zum Beispiel ECTS oder LearnCoins, zu sammeln.

Diese Punkte können z.B. auch in Zertifikatsprogrammen für Rezertifizierungen eingesetzt werden. Teilnehmer:innen können mit jedem erfolgreichen Absolvieren eines Kurses Kreditpunkte sammeln. Mit diesen Kreditpunkten können sie dann einen weiteren Kurs kaufen.

Organisationen können eigene Kreditpunktesysteme definieren und benennen, sowie bei Bedarf einschränken. Etwa nach Rollen oder organisatorischen Bereichen. Nach dem erfolgreichen Abschluss eines Lernangebots lassen sich Kreditpunkte gezielt zuweisen, sodass eine langfristige Nutzung für Rezertifizierungen unterstützt wird.


[Kreditpunkte systemweit aktiveren (Administration) >](../../manual_admin/administration/e-Assessment_Credit_Points.de.md)<br>
[Kreditpunkte in Kursen vergeben >](../../manual_user/learningresources/Course_Settings_Assessment.de.md#section_credit_points)<br>
[Kreditpunkte im persönlichen Menü >](../../manual_user/personal_menu/Credit_Points.de.md)<br>

[zum Seitenanfang ^](#offer_concepts)

---

## Weitere Randbedingungen für Angebote {: #further_boundary_conditions}   

Für Angebote können weitere Bedingungen eingestellt werden. Die meisten Konfigurationsoptionen geben Sie direkt während der Erstellung eines neuen Angebots ein.

![offer_concepts_example1_v1_de.png](assets/offer_concepts_example1_v1_de.png){ class="shadow lightbox" }

* **Verfügbar wenn der Durchführungsstatus "provisorisch" und "bestätigt" ist:**<br>
Eine Durchführung muss noch nicht vollständig geplant sein, um bereits ein Angebot veröffentlichen zu können.

* **Verfügbar in einem bestimmten Zeitraum:**<br>
Das Angebot wird im angegebenen Zeitfenster unabhängig vom Status angezeigt und kann gebucht werden.

* **Mitgliedschaft Standard:**<br>
Die Mitgliedschaft ist sofort nach der Buchung des Angebots aktiv. 

* **Mitgliedschaft mit Bestätigung:**<br>
Die Mitgliedschaft ist zunächst ausstehend. Rie Reservierung muss von einer administrativen Rolle bestätigt werden.

* **Automatisches Buchen:**<br> 
Die Mitgliedschaft wird automatisch erstellt, wenn der Kurs geöffnet wird.
Beim automatischen buchen wird die Angebotsbeschreibung nicht angezeigt und den Benutzer:innen wird nur die Aktion "Öffnen" abgeboten. Diese Option sollte nicht gleichzeitig mit anderen Angeboten verwendet werden.

* Auch bei sofort aktiver Mitgliedschaft (Durchführungen, Angebot mit Rechnung) wird in der Regel zunächst noch ein **Akzeptieren der Datenschutzbestimmungen und weiterer Nutzungsbedingungen** verlangt. In den Nutzungsbedingungen können ggf. weitere Rahmenbedingungen festgelegt werden.

* Eine Ausschreibung/ein Angebot für eine Durchführung kann erfolgen, wenn noch unklar ist, ob die Durchführung stattfindet. Es muss zum Zeitpunkt der Angebotserstellung noch nicht einmal ein Kurs existieren. Wird dagegen ein eigenständiger Kurs angeboten, muss das Angebot im Kurs erstellt werden und erscheint nur bei veröffentlichtem Kurs im Katalog.

* Mit einem **Angebot des Typs "Zugangscode"** ist die Ressource mit einem Zugangscode buchbar. Die Benutzer:innen erhalten eine entsprechende Mitgliedschaft, die ihnen den Zugang zur Ressource ermöglicht.

[zum Seitenanfang ^](#offer_concepts)

---


## Weiterführende Informationen {: #further_information}

[Mehr zum Katalog >](../../manual_user/area_modules/catalog2.0.de.md)<br>
[Mehr zu Angeboten >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>
[Wie zeige ich meine Kurse im Katalog? >](../../manual_how-to/catalog/catalog.de.md)<br>
[Zugangskonfiguration/Freigabe >](../../manual_user/learningresources/Access_configuration.de.md)<br>
[Anbieten von Durchführungen im Katalog >](../../manual_user/area_modules/Course_Planner_Implementations.de.md#tab_catalog)<br>
[Bezahlungsmodul PayPal (Administration) >](../../manual_admin/administration/Payment_PayPal.de.md)<br>
[Bezahlungsmodul Rechnung (Administration) >](../../manual_admin/administration/Payment_Invoice.de.md)<br>
[Kreditpunkte im persönlichen Menü >](../../manual_user/personal_menu/Credit_Points.de.md)<br>
[Kreditpunkte systemweit aktiveren (Administration) >](../../manual_admin/administration/e-Assessment_Credit_Points.de.md)<br>
[Kreditpunkte in Kursen vergeben >](../../manual_user/learningresources/Course_Settings_Assessment.de.md#section_credit_points)<br>

[zum Seitenanfang ^](#offer_concepts)


