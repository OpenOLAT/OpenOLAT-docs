# Angebotskonzepte {: #offer_concepts}

!!! warning "Achtung"

    Dieser Artikel ist noch in Bearbeitung.



## Was ist ein Angebot? {: #offers}

Um einen Katalogeintrag für einen Kurs oder eine andere Lernressource im Katalog zu erhalten, benötigt es jeweils ein Angebot [Angebot](../../manual_user/area_modules/catalog2.0_angebote.de.md).


gleiche Lernressource/Durchführung/Kurs mit verschiedenen Angeboten für verschiedene Zielgruppen

Angebote nur für best Organisationseinheiten


screen

[zum Seitenanfang ^](#offer_concepts)

---


## Was ist eine Buchung? {: #bookings}



tbd







[zum Seitenanfang ^](#offer_concepts)

---


## Wo können Angebote gezeigt werden? {: #show_offers}

        interner Katalog

        externer Katalog

Anzeige in Katalogbereiche, die nur für Mitglieder bestimmter Organisationseinheiten sichtbar sind.

![offer_concepts_share_org_v1_de.png](assets/offer_concepts_share_org_v1_de.png){ class=" shadow lightbox" }

!!! hint "Hinweis"

    Die Angebote sind im Katalog buchbar, sobald der Status auf "Veröffentlicht" gestellt wurde.

[zum Seitenanfang ^](#offer_concepts)

---


## Wo werden Angebote erstellt? {: #create_offers}

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

[zum Seitenanfang ^](#offer_concepts)

---


## Was kann angeboten werden? {: #what_is_offered}

In den Katalog können Angebote aufgenommen werden für

- Kurse
- Durchführungen
- sonstige Lernressourcen


### Kurse anbieten {: #what_is_offered_courses}


tbd

![offer_types_course1_v1_de.png](assets/offer_types_course1_v1_de.png){ class="shadow lightbox" }

![offer_types_course2_v1_de.png](assets/offer_types_course2_v1_de.png){ class="shadow lightbox" }

[Mehr über das Anbieten von Kursen im Katalog >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>

[zum Seitenanfang ^](#offer_types)

---


### Durchführungen anbieten {: #what_is_offered_implementations}


Im Course Planner können Buchungsaufträge mit Rechnung für Durchführungen erstellt werden. (Stand Release 20.1: Ausschliesslich mit Course Planner möglich.) <br>(**Course Planner > Durchführung > Tab Katalog > Tab Angebote**) <br>
Dazu werden im Course Planner Angebote hinterlegt und z.B. in einem externen Katalog angezeigt (Preise und Anzahl der verfügbaren Plätze).

Benutzer:innen können diese Kurse buchen, in dem sie sich aus dem Katalog heraus anmelden (wenn sie schon Benutzer:in von OpenOlat sind) oder sich registrieren.

Wenn aus dem Course Planner heraus ein Angebot im Katalog gemacht wurde, das mit Rechnung gebucht werden kann, werden die Interessent:innen beim Anmeldevorgang zur Angabe der Rechnungsadresse usw. geführt. Es wird dabei auch eine Buchungsnummer erstellt.

Der Buchungsauftrag kann anschliessend bestätigt werden.

![offer_types_course_planner1_v1_de.png](assets/offer_types_course_planner1_v1_de.png){ class="shadow lightbox" }

![offer_types_course_planner2_v1_de.png](assets/offer_types_course_planner2_v1_de.png){ class="shadow lightbox" }

[Mehr über das Anbieten von Durchführungen im Katalog >](../../manual_user/area_modules/Course_Planner_Implementations.de.md#tab_catalog)


[zum Seitenanfang ^](#offer_concepts)

---


### Sonstige Lernressourcen anbieten {: #what_is_offered_other}

tbd

[zum Seitenanfang ^](#offer_types)

---

## Angebote mit Bezahlung {: #offer_payed}

### PayPal {: #offer_payed_paypal}

tbd

Im Bereich "Paypal" wird Paypal aktiviert. Konfigurieren Sie die PayPal API- Berechtigung für den PayPal Zugang mit den Elementen Client ID und Client Secret. Diese zwei Sicherheitselemente müssen Sie zuerst in Ihrem PayPal Businesskonto erstellen. OpenOlat unterstützt nicht nachträgliche Anderungen am Bestellungen von Ihrem Paypal Konto.



Das PayPal Bezahlungsmodul erlaubt es Autor:innen Kurse und Arbeitsgruppen gegen Geld freizuschalten. Ihre Kunden können dabei entweder mit Kreditkarte oder direkt über PayPal bezahlen sofern sie einen PayPal Account besitzen. Dieser ist aber für Ihre Kunden nicht zwingend notwendig. In der PayPal Konfiguration der Systemadministration können Sie die PayPal Kontoinformationen hinterlegen, die für alle Bezahlprozesse verwendet werden sollen.

Um die PayPal Bezahlmethode verwenden zu können müssen Sie über einen PayPal Firmenkonto verfügen. Einen solches Konto können Sie bei PayPal ohne weitere Kosten erstellen. In Ihrem PayPal Konto können Sie anschliessend eine sogenannte API-Berechtigung erstellen. Diese besteht aus der Client-ID und dem Schlüssel. Diese beiden Sicherheitselemente müssen Sie in der PayPal Konfiguration von OpenOlat hinterlegen, damit das System die Bezahlungen Ihrer Kunden auf Ihr Konto abwickeln kann. Weiter unten finden Sie Hinweise wie Sie diese Sicherheitselemente auf der PayPal Webseite erstellen können.

Verwendung in Kursen und Arbeitsgruppen

Um Kurse und Arbeitsgruppen gegen Geld freizuschalten, können Sie nach erfolgreicher Konfiguration des PayPal Moduls auf der Detailseite des Kurses oder in der Administrationsumgebung der Arbeitsgruppe die PayPal Angebotsart auswählen. Weitere Informationen finden Sie unter Zugangskonfiguration




[Bezahlungsmodul PayPal (Administration) >](../../manual_admin/administration/Payment_PayPal.de.md)<br>


### Rechnung {: #offer_payed_invoice}

nur für Durchführungen im Course Planner

bei Angebot mit Rechnung:<br> 
* Mitgliedschaft ist sofort aktiv oder
* Die Mitgliedschaft ist zunächst ausstehend, bis eine administrative Rolle die Reservierung bestätigt.

(Auch bei sofort aktiver Mitgliedschaft wird in der Regel zunächst noch ein Akzeptieren der Datenschutzbestimmungen und weiterer Nutzungsbedingungen verlangt.)

![offer_concepts_invoice_membership_v1_de.png](assets/offer_concepts_invoice_membership_v1_de.png){ class="shadow lightbox" }


!!! hint "Tipp"

    Im Course Planner unter<br>
    **Durchführungen > Tab Katalog > Tab Buchungsaufträge**<br> 
    sind die Buchungsaufträge gesammelt und können als Excel-Datei exportiert und in einem anderen Programm (z.B. zur Rechnungserstellung) verwendet werden.  


[Bezahlungsmodul Rechnung (Administration) >](../../manual_admin/administration/Payment_Invoice.de.md)<br>



### Kreditpunkte {: #offer_payed_credit_points}


tbd


[Kreditpunkte im persönlichen Menü >](../../manual_user/personal_menu/Credit_Points.de.md)<br>
[Admin Kreditpunkte systemweit aktiveren >](../../manual_admin/administration/e-Assessment_Credit_Points.de.md)<br>
[Kreditpunkte in Kursen vergeben >](../../manual_user/learningresources/Course_Settings_Assessment.de.md#section_credit_points)<br>




[zum Seitenanfang ^](#offer_concepts)

---


## Weiterführende Informationen {: #further_information}

[Mehr zum Katalog >](../../manual_user/area_modules/catalog2.0.de.md)<br>
[Mehr zu Angeboten >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>
[Wie zeige ich meine Kurse im Katalog? >](../../manual_how-to/catalog/catalog.de.md)<br>
[Anbieten von Durchführungen im Katalog >](../../manual_user/area_modules/Course_Planner_Implementations.de.md#tab_catalog)<br>
[Bezahlungsmodul PayPal (Administration) >](../../manual_admin/administration/Payment_PayPal.de.md)<br>
[Bezahlungsmodul Rechnung (Administration) >](../../manual_admin/administration/Payment_Invoice.de.md)<br>
[Kreditpunkte im persönlichen Menü >](../../manual_user/personal_menu/Credit_Points.de.md)<br>
[Kreditpunkte systemweit aktiveren (Administration) >](../../manual_admin/administration/e-Assessment_Credit_Points.de.md)<br>
[Kreditpunkte in Kursen vergeben >](../../manual_user/learningresources/Course_Settings_Assessment.de.md#section_credit_points)<br>

[zum Seitenanfang ^](#offer_concepts)


