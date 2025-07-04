# Wie zeige ich meine Kurse im OpenOlat-Katalog? {: #catalog}

??? abstract "Ziel und Inhalt dieser Anleitung"

    Die folgende Anleitung zeigt Ihnen, wie Sie einen fertigen Kurs in den Katalog aufnehmen und anbieten können.

??? abstract "Zielgruppe"

    [x] Autor:innen [ ] Betreuer:innen  [ ] Teilnehmer:innen

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * Sie haben bereits einen Kurs erstellt.
    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    

---

## Wo finde ich den OpenOlat-Katalog? {: #catalog_where}

### a) Als registrierte:r Benutzer:in

OpenOlat-Benutzer:innen sehen in der Kopfzeile meistens "Kurse" und "Gruppen", wenn sie Teilnehmer:innen sind. Autor:innen sehen zusätzlich den "Autorenbereich". Aber die Optionen in der Kopfzeile können variieren. Je nach Rolle oder aktivierten Modulen, können weitere Einträge in der Kopfzeile dazu kommen. So z.B. auch der Katalog. Wurde von Ihrem/Ihrer Administrator:in der [Katalog (Version 2.0)](../../manual_user/area_modules/catalog2.0.de.md) aktiviert, finden Sie den Eintrag "Katalog" im Menü der Kopfzeile. Wird kein Katalog im Menü angezeigt, wenden Sie sich bitte an Ihren/Ihre Administrator:in.

![katalog_menu_kopfzeile_v1_de.png](assets/katalog_menu_kopfzeile_v1_de.png){ class="shadow lightbox" }  


### b) Ohne Registrierung

In OpenOlat können auch Angebote hinterlegt werden, die in einem externen Katalog angezeigt werden. "Extern" bedeutet, dass der Katalog nach ausserhalb der "Registrierungsmauer" gespiegelt wird und dort ohne Registrierung aufgerufen werden kann. Die Ausgangsversion des Katalogs (innerhalb der "Registrierungsmauer"), die nur von registrierten Benutzer:innen aufgerufen werden kann, muss ein Katalog V2 sein. Ein Katalog V1 kann nicht als externer Katalog angezeigt werden.

Benutzer:innen können dann diese Kurse auswählen und buchen. Sie werden erst nach einer getroffenen Wahl durch den Registrierungsprozess geführt (um Arbeitsergebnisse speichern zu können).

Bei bereits in OpenOlat registrierten Benutzer:innen wird die Buchung ihrem bestehenden Konto zugeordnet. Die Buchung wird anschliessend bestätigt.

Der externe Katalog kann auf dem Login-Screen angeboten werden.
Der Link kann aber auch an anderer Stelle z.B. in eine Website eingebaut oder per Mail verschickt werden. 
Auch [direkte Links zu einem bestimmten Angebot](../../manual_user/area_modules/catalog2.0_web.de.md#web_catalog_direct_link) können verschickt werden.

![catalog20_ext_catalog_login_v1_de.png](assets/catalog20_ext_catalog_login_v1_de.png){ class="shadow lightbox" } 


!!! tip "Hinweis"

    In OpenOlat gibt es 2 Versionen des Katalogs: [Katalog 1.0](../../manual_user/area_modules/catalog1.0.de.md) und [Katalog 2.0](../../manual_user/area_modules/catalog2.0.de.md).
	Die nachstehenden Ausführungen beschreiben das Vorgehen im **Katalog 2.0**.


[zum Seitenanfang ^](#catalog)

---


## Was kann ich im OpenOlat-Katalog anzeigen?  {: #catalog_what}

Der OpenOlat-Katalog listet **Kurzbeschreibungen zu Kursen und Lernressourcen** auf. Es können bereits auf der Startseite einzelne Kacheln angezeigt werden. Unter den **Kategorien** befinden sich **Microsites**, auf denen dann weitere Einzelbeschreibungen (Kacheln) zu finden sind. 

![katalog_community_v1_de.png](assets/katalog_community_v1_de.png){ class="shadow lightbox" } 

Die Angaben in den Kurzbeschreibungen werden jeweils den Angaben entnommen, die Autoren beim Erstellen eines Kurses oder einer Lernressource in den [Einstellungen](../../manual_user/learningresources/Course_Settings.de.md) (Tab "Info" + Tab "Metadaten"). Meistens sind es Angaben, die Kursteilnehmenden auch auf der Infoseite zu einem Kurs finden.

Die **Gestaltung** des Katalogs wird vom [Administrator](../../manual_admin/administration/Modules_Catalog_2.0.de.md) festgelegt. Wurde z.B. bestimmt, dass in den Katalogeinträgen eine Angabe zum Durchführungsformat angezeigt werden soll, holt sich OpenOlat diese Information aus den Angaben der Autorin / des Autors unter "Einstellungen" und zeigt sie an der vorgesehenen Stelle auf der Katalogkachel an.

![kurs_einstellungen_v1_de.png](assets/kurs_einstellungen_v1_de.png){ class="shadow lightbox" } 

Angaben, die im Katalog-Layout nicht vorgesehen sind, können also beim Katalog 2.0 nicht von den Autor:innen völlig frei ergänzt werden. Das garantiert aber andererseits ein einheitliches geordnetes Aussehen des Katalogs. Wenden Sie sich an Ihren Administrator, wenn Sie Wünsche zur Gestaltung der Katalog-Kacheln haben.


[zum Seitenanfang ^](#catalog)

---

## Wie wird entschieden, was im Katalog angezeigt wird? {: #catalog_decision}

Es werden nicht automatisch alle vorhandenen Kurse und Lernressourcen im Katalog aufgeführt. Ob ein Katalogeintrag erzeugt wird, entscheidet die Autorin oder der Autor des Kurses.

Die Autorin / der Autor  muss dazu

a) den Kurs für den Katalog **frei geben** und

b) ein [Angebot formulieren](../../manual_user/learningresources/Access_configuration.de.md), mit dem der Kurs oder die Lernressource im Katalog beworben wird.

Gehen Sie in die Administration Ihres Kurses. Dort finden Sie unter "Einstellungen" auch den Reiter "Freigabe".

![kurs_freigabe_v1_de.png](assets/kurs_freigabe_v1_de.png){ class="shadow lightbox" }

Enthält Ihr Kurs als Buchungsmethode "privat" bedeutet das auch, dass er nirgends im Katalog erscheinen soll. Im ersten Schritt müssen Sie also die Buchungsmethode "Buchbare und offene Angebote - Buchbar für Benutzer*innen im Katalog" wählen und so die Anzeige Ihres Kurses im Katalog prinzipiell ermöglichen.

![kurs_freigabe_buchbar_v1_de.png](assets/kurs_freigabe_buchbar_v1_de.png){ class="shadow lightbox" }

Ob und wo der Kurs im Katalog erscheint, wird dann im zweiten Schritt durch die Erstellung von Angeboten festgelegt. Im unteren Bereich können Sie ein oder mehrere Angebote für den Katalog erstellen.

![catalog_course_offer_new_v2_de.png](assets/catalog_course_offer_new_v2_de.png){ class="shadow lightbox" }


!!! tip "Hinweis"

    Man könnte annehmen, dass nur Kurse mit dem Status "Veröffentlicht" im Katalog enthalten sein können. Im Katalog 2.0 können jedoch auch bereits Angebote angezeigt werden, wenn die Kurse noch nicht veröffentlicht sind und erst ab einem bestimmten Zeitpunkt zugänglich werden!


[zum Seitenanfang ^](#catalog)

---

## Angebote erstellen  {: #catalog_create_offer}

!!! tip "Hinweis"

    Vor OpenOlat 17 und generell bei der Verwendung des Katalog 1.0 ist in den Einstellungen ein Reiter "Katalog" enthalten und es konnten noch keine Angebote erstellt werden. 
    Bei Verwendung des Katalog 2.0 ab OpenOlat 17 werden die Einstellungen für die Anzeige im Katalog im Reiter "Freigabe" gemacht (in Form von Angeboten).

Klicken Sie auf den Button "Angebot hinzufügen", erhalten Sie eine Vorauswahl möglicher Angebotstypen.

![catalog_course_offer_add_v2_de.png](assets/catalog_course_offer_add_v2_de.png){ class="shadow lightbox" }

!!! tip "Hinweis"

    Ist der Button "Angebot hinzufügen" inaktiv, ist die Buchungsmethode noch als "privat" eingestellt.

Wählen Sie den gewünschten Angebotstyp.

Sie können mehrere Angebote erstellen. Sie können z.B. für eine bestimmte Organisationseinheit einen Kurs frei zugänglich machen, während er mit einem zweiten Angebot für andere kostenpflichtig angeboten wird.

![catalog_offer_freely_available_v2_de.png](assets/catalog_offer_freely_available_v2_de.png){ class="shadow lightbox" }
![catalog_offer_access_code_v2_de.png](assets/catalog_offer_access_code_v2_de.png){ class="shadow lightbox" }
![catalog_offers_v2_de.png](assets/catalog_offers_v2_de.png){ class="shadow lightbox" }

!!! tip "Hinweis"

    Die Angebote sind im Katalog buchbar, sobald der Status auf "Veröffentlicht" gestellt wurde.


[zum Seitenanfang ^](#catalog)

---

## Der Katalogaufbau {: #catalog_structure}

Die Gestaltung des Katalogs wird einerseits durch die Angebote der Autor:innen bestimmt und andererseits durch die Vorgaben der Administratorin / des Administrators.

![katalog_prozess_erstellung_v1_de.png](assets/katalog_prozess_erstellung_v1_de.png){ class="lightbox" }

Im Katalog V2 werden Abschnitte mit Katalogeinträgen (Kacheln, Karten) als Launcher bezeichnet.

![katalog_launcher_v1_de.png](assets/katalog_launcher_v1_de.png){ class="shadow lightbox" }

Innerhalb der Launcher (diesen Abschnitten im Katalog) können die Katalogeinträge nach bestimmten Kriterien zusammengestellt werden (je nach Launchertyp und Launcherkonfiguration).
Sie werden deshalb als Launcher (engl. Starter, Startrampe) bezeichnet, weil in ihnen die Katalogeinträge (Kacheln, Karten) meistens dynamisch zusammengestellt werden.

[zum Seitenanfang ^](#catalog)

---

## Wie beeinflusse ich als Autorin/Autor, in welchem Launcher mein Kurs angezeigt wird? {: #catalog_launcher_decision}

Alle Angebote, die die Kriterien für einen bestimmten Launcher erfüllen, werden in diesem Launcher angezeigt. Als Autorin oder Autor beeinflussen Sie also die Anzeige, indem Sie 

* die entsprechenden **Anzeigekriterien** in Ihrem Kurs angeben (Angaben unter Administration > Einstellungen)
* und entsprechende **Angebote** erstellen.

**Beispiel 1:**

Ein Launcher ist (vom Administrator) nur für Mitglieder einer bestimmten Organisationseinheit vorgesehen und wird nur diesen angezeigt. Erstellen Sie als Autor:in ein Angebot, das nur für diese bestimmte Organisationseinheit gilt, erscheint es in diesem Launcher.


**Beispiel 2:**

In einem Launcher werden (vom Administrator so festgelegt) nur Angebote angezeigt, die ein bestimmtes Stichwort der Taxonomie enthalten. Als Autor tragen Sie in den Metadaten Ihres Kurses den Taxonomiebegriff ein. Beim Erstellen eines Angebots sehen Sie, dass dieser Taxonomiebegriff zugeordnet ist. Das Angebot erscheint also automatisch in Launchern, die für Kurse mit diesem Taxonomiebegriff vorgesehen sind.

[zum Seitenanfang ^](#catalog)

---

## Weitere Informationen {: #further_information}

[Übersicht zum Katalog V2 >](../../manual_user/area_modules/catalog2.0.de.md)<br>
[Angebote erstellen >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>
[Katalog-Design >](../../manual_user/area_modules/catalog2.0_design.de.md)<br>
[Der externe Katalog >](../../manual_user/area_modules/catalog2.0_web.de.md)<br>
[Externen Katalog einrichten (Administrationshandbuch) >](../../manual_admin/administration/Modules_Catalog_2.0.de.md)<br>

[zum Seitenanfang ^](#catalog)
