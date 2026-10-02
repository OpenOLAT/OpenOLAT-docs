# Wie verwende ich das Sprachanpassungswerkzeug? {: #how_to_use}


??? abstract "Ziel und Inhalt dieser Anleitung"

    Diese Anleitung zeigt Ihnen, wie Sie Texte der OpenOlat-Benutzeroberfläche (GUI, Graphical User Interface) anpassen.

??? abstract "Zielgruppe"

    [ ] Autor:innen [ ] Betreuer:innen  [ ] Teilnehmer:innen  [x] Administrator:innen

    [ ] Anfänger:innen [ ] Fortgeschrittene  [x] Expert:innen


??? abstract "Erwartete Vorkenntnisse"

    * Erfahrung als Administrator:in
    * Erfahrung mit der Verwendung von Variablen in Programmierumgebungen


## Was ist möglich? {: #possibilities}

Oft verwendet eine Organisation eine eigene, interne Ausdrucksweise. Es ist dann erwünscht, dass diese Ausdrucksweise auch in der Lernplattform verwendet wird. Wenn es die **Inhalte** betrifft, können die **Autor:innen** es berücksichtigen. Für spezifische **Anpassungen der OpenOlat-Oberfläche** selbst, kann das **Sprachanpassungswerkzeug** verwendet werden.

**Beispiel:**<br>
Im Titel des Suchfeldes zum Katalog soll nicht "Katalog" stehen, sondern "Unsere Produkte".

=== "Standardtext"

    ![Titel Katalog über dem Suchfeld des Katalogs, markiert](assets/language_adaption_tool_example1a_v1_de.png){ class="shadow lightbox" title="Katalog mit Standardtext" }

=== "Angepasster Text"

    ![Titel Unsere Produkte über dem Suchfeld des Katalogs, markiert](assets/language_adaption_tool_example1b_v1_de.png){ class="shadow lightbox" title="Katalog mit angepasstem Text" }


**Das Prinzip dahinter:**<br>
Alle Texte der OpenOlat-Benutzeroberfläche sind einzeln in Variablen abgespeichert. Der Wert dieser Variablen kann mit dem Sprachanpassungswerkzeug gesetzt werden. So können z.B. für die Verwendung von OpenOlat in einer anderen Sprache die Übersetzungen einfach den entsprechenden Variablen zugeordnet werden. Es wird dann auf der Benutzeroberfläche der Wert der Variable in der anderen Sprache angezeigt. Soll ein Begriff z.B. in der deutschen Sprache abgeändert werden, kann sozusagen "von Deutsch nach Deutsch" übersetzt werden.

**Was nicht möglich ist:**<br>
Eingebundene externe Tools können selbstverständlich nicht angepasst werden. Wenn z.B. Microsoft Word aus OpenOlat heraus aufgerufen wird, kann die Benutzeroberfläche von Word nicht angepasst werden. Dies gilt auch für alle anderen externen Tools.

!!! warning "Nur für Expert:innen!"

    Für normale Setups ist die Änderung der Texte in der OpenOlat-Benutzeroberfläche nicht empfohlen. Ausgenommen sind einige Stellen, die oft an organisationsinterne Sprachgewohnheiten angepasst werden.

    Wenn von Ihnen neu zugewiesene Beschriftungen bereits anderweitig als Begriffe in OpenOlat verwendet werden, kann dies zu sehr viel Verwirrung führen!

    Wenn Schlüsselbegriffe umbenannt werden, finden Sie diese auch nicht mehr in der OpenOlat-Hilfe.

    Sind Sie sich also bewusst, dass Sie für die Sprachanpassung ein sehr mächtiges Werkzeug benutzen und setzen Sie es vorsichtig ein.


## Welche Voraussetzungen muss ich mitbringen? {: #requirements}

  * Sie müssen in OpenOlat die Rolle als **Administrator:in** haben.
  * Es ist hilfreich, wenn Sie etwas Erfahrung im Umgang mit Variablen in Programmierumgebungen mitbringen.


## Wo rufe ich das Sprachanpassungswerkzeug auf? {: #language_adaption_tool}

Sie finden das Werkzeug in der System-Administration unter:<br>
`Administration > Customizing > Sprachanpassungswerkzeug`<br>
Klicken Sie dort auf den Button "Start".

![Menü Customizing mit dem Eintrag Sprachanpassungswerkzeug und dem Button Start](assets/language_adaption_tool_open_v1_de.png){ class="shadow lightbox" title="Sprachanpassungswerkzeug in der System-Administration" }

Das Sprachanpassungswerkzeug öffnet sich in einem neuen Browser-Fenster. Dies ist vorteilhaft, denn so können Sie zur Kontrolle Ihrer Änderungen immer wieder ins Hauptfenster wechseln.

![Felder Sprache und Anpassungen, darunter vier Einstiege: nicht angepasste, angepasste und alle Übersetzungen sowie die Suche](assets/language_adaption_tool_start_v1_de.png){ class="shadow lightbox" title="Startseite des Sprachanpassungswerkzeugs" }


## Schritt 1: Welcher Text soll geändert werden? {: #step1}

An welcher Stelle befindet sich der Begriff, der geändert werden soll? Um herauszufinden, welche Variable dahinter steckt, muss man genau wissen, welcher Begriff gemeint ist. Im Idealfall kennen Sie den Variablennamen (Schlüssel), hinter dem der gesuchte Begriff oder Text in OpenOlat abgelegt wird. Eine Hilfe dazu ist die [Übersicht der Schlüssel](#keys).

**Beispiel:**<br>
Der Begriff "Katalog" soll nur im Titel des Suchfeldes zum Katalog geändert werden.

Kennen Sie den Schlüssel nicht, ist es für Nicht-Expert:innen etwas schwierig, die richtige Variable zu finden. Dann müssen Sie den richtigen Schlüssel suchen.

**a)** Wählen Sie ganz oben im Feld "Sprache" die Sprache, deren Text Sie ändern wollen.

![Auswahllisten Sprache mit German (de) und Anpassungen mit German (de__customizing)](assets/language_adaption_tool_language_v1_de.png){ class="shadow lightbox" title="Sprachwahl im Sprachanpassungswerkzeug" }

**b)** Je nach bereits bekannten Informationen können Sie einen der Einstiege nutzen. In der Regel empfiehlt sich die Suche mit Suchbegriff im Bereich "Suche" rechts unten. Er bietet die folgenden Felder:

![Suche nach Katalog in der Übersetzung der Sprache, über alle Pakete, nach Priorität sortiert](assets/language_adaption_tool_search1_v1_de.png){ class="shadow lightbox aside-right" }

#### Suchbegriff {: #search_term}

Geben Sie das Wort ein, das Sie suchen, zum Beispiel "Katalog".

#### suchen in: Übersetzungsschlüssel oder Übersetzung {: #search_in_key_or_translation}

Mit "Übersetzungsschlüssel" wird der Suchbegriff im Variablennamen gesucht. Mit "Übersetzung" wird im Text der Variable gesucht. Voreingestellt ist "Übersetzung".

**Beispiel:**<br>
Wenn Sie nur den auf dem Bildschirm angezeigten Begriff kennen, suchen Sie in "Übersetzung".<br>
Wenn Sie bereits wissen, dass der Begriff "topnav" im Variablennamen (nicht im Text) enthalten ist, ist Ihre Suche mit der Option "Übersetzungsschlüssel" und Eingabe von "topnav" im Suchfeld erfolgreicher.

#### suchen in: Sprache oder Anpassungen {: #search_in_language_or_adaptations}

Mit "Sprache" wird in den Texten der oben ausgewählten Sprache gesucht. Mit "Anpassungen" beschränkt sich die Suche auf bereits vorgenommene Änderungen innerhalb dieser Sprache. Voreingestellt ist "Anpassungen". Suchen Sie einen Text, den Sie noch nicht angepasst haben, wählen Sie "Sprache".

#### Paket(e) {: #package_selection}

Solange Sie nicht wissen, in welchem Variablenpaket sich der zu ändernde Text befindet, wählen Sie "Alle Pakete". Wenn Sie später genau wissen, zu welchem Paket der gesuchte Text gehört, können Sie gezielt das entsprechende Paket auswählen. Oft kommt innerhalb eines Paketes der Begriff mehrfach vor.

#### Unterpakete berücksichtigen {: #include_subpackages}

Bei "Alle Pakete" ist das Häkchen immer gesetzt und lässt sich nicht ändern. Haben Sie ein einzelnes Paket gewählt, legen Sie damit fest, ob die Suche auch dessen Unterpakete einschliesst. Unterpakete sind Pakete, deren Name mit dem Namen des gewählten Pakets beginnt, zum Beispiel `org.olat.modules.catalog.ui` unter `org.olat.modules.catalog`.

#### Nach Priorität sortieren {: #sort_by_priority}

Mit dem Häkchen stehen Pakete und Übersetzungsschlüssel mit hinterlegter Priorität zuoberst, die übrigen folgen alphabetisch. Ohne Häkchen sind Pakete und Schlüssel rein alphabetisch sortiert.

#### Anzeigen und Anpassen {: #show_and_adapt}

Der Button "Anzeigen" listet die Fundstellen auf (Schritt 2). Der Button "Anpassen" wechselt sofort zu Schritt 3.

!!! tip "Tipp"

    Sie können jederzeit durch Klick in die Krümelnavigation wieder zurück, um einen neuen Suchvorgang mit anderer Sucheinstellung zu starten.

    ![Krümelnavigation mit markiertem Link Start Sprachanpassungswerkzeug über der Übersetzungsliste](assets/lanugage_adaption_tool_searchhint_v1_de.png){ class="shadow lightbox" title="Krümelnavigation im Sprachanpassungswerkzeug" }


## Schritt 2: Zu welchem Variablen-Paket könnte der Begriff gehören? {: #step2}

Die Variablen sind in Paketen zusammengefasst. Die Suche findet Pakete, in denen die im Suchfeld angegebene Variable oder ihr Text enthalten ist. Das Suchergebnis wird dann weiter gefiltert durch die Angabe der anderen Optionen.<br>
Klicken Sie auf den Button "Anpassen" um in die Maske zum Anpassen zu gelangen.

**Beispiel:**<br>
Der Begriff "Katalog" soll nur im Titel des Suchfeldes zum Katalog geändert werden.
Der Katalog ist ein Modul, der Name des gefundenen Paketes ist also plausibel.

![Übersetzungsliste mit zwei Fundstellen im Paket org.olat.modules.catalog.ui und dem Button Anpassen](assets/language_adaption_tool_search2_v1_de.png){ class="shadow lightbox" title="Übersetzungsliste nach der Suche" }

Da die Bezeichnungen der Pakete für Laien manchmal nicht sofort verständlich sind, finden Sie nachstehend eine kleine [Übersicht der wichtigsten Pakete](#packages).


## Schritt 3: Welche Variable gehört zu diesem Text? {: #step3}

Nachdem wir das vermutlich richtige Paket gefunden haben, kann aus einer Dropdown-Liste ein Übersetzungsschlüssel ausgewählt werden. (Eine einzelne Variable, die in diesem Paket enthalten ist.) Hier hilft Probieren weiter.<br>
Sobald ein Übersetzungsschlüssel (Key) gewählt ist, wird der zugehörige Standard-Variablenwert im oberen Textfeld "Sprache: Deutsch" angezeigt (nicht editierbar, da Default-Wert).<br>
Im unteren Textfeld "Anpassungen: Deutsch" kann nun der neue Text eingegeben werden, der zu dieser Variablen gespeichert werden soll. Der Button "Referenzsprache kopieren" übernimmt den Standardtext in dieses Feld, dort ändern Sie ihn ab.<br>
Mit dem Häkchen "Aktivieren" neben "Vergleichssprache" blenden Sie zur Kontrolle den Text einer weiteren Sprache ein.<br>
**Verwenden Sie die Buttons "Weiter" und "Zurück" am unteren Rand, um durch die Schlüssel (Variablen) zu blättern.**

![Übersetzungsschlüssel header.search.title mit dem Standardtext Katalog und der Anpassung Unsere Produkte](assets/language_adaption_tool_search3_v1_de.png){ class="shadow lightbox" title="Bearbeitungsmaske eines Übersetzungsschlüssels" }


!!! tip "Tipp"

    Häufig geänderte Variablen und die Pakete, denen sie zugeordnet sind, finden Sie nachstehend in einer kleinen [Übersicht der Schlüssel](#keys).


## Schritt 4: Muss der Begriff noch an anderen Stellen geändert werden? {: #step4}

Vergessen Sie nicht zu speichern. Kontrollieren Sie dann die gemachte Änderung. Häufig kommt ein Begriff an mehreren Stellen vor. Zu jeder Stelle, an der er auf der OpenOlat-Benutzeroberfläche angezeigt wird, gibt es im Normalfall eine eigene Variable. Das heisst, eventuell müssen die Werte mehrerer Variablen geändert werden.

## Schritt 5: Text in den anderen Sprachen anpassen {: #step5}

OpenOlat-Benutzer:innen können [im persönlichen Menü](../../manual_user/personal_menu/Settings.de.md#language) die Sprache der OpenOlat-Oberfläche ändern. Damit die gemachte Änderung auch nach dem Umstellen auf eine andere Sprache enthalten ist, müssen die betroffenen Variablen auch in den anderen Sprachen entsprechend angepasst werden.

**Beispiel:**<br>
In der deutschsprachigen Version wurde "Katalog" zu "Unsere Produkte". In der englischsprachigen Version soll deshalb auch "Our products" angezeigt werden, statt "Catalog".

Sie kennen bereits die Variable und das Paket, in dem sie sich befindet. Sie müssen also lediglich die gewünschte Sprache wählen und dann Schritt 3 ausführen.


## Welche Anpassungen habe ich bereits gemacht? {: #my_adaptations}

Mit der Zeit sammeln sich Anpassungen an. Das Sprachanpassungswerkzeug zeigt Ihnen jederzeit, welche Übersetzungsschlüssel Sie bereits angepasst haben.

**a)** Öffnen Sie das Sprachanpassungswerkzeug in der System-Administration unter:<br>
`Administration > Customizing > Sprachanpassungswerkzeug`<br>
mit dem Button "Start".

**b)** Wählen Sie oben im Feld "Sprache" die gewünschte Sprache. Das Feld "Anpassungen" darunter folgt automatisch.

**c)** Der Block "Angepasste Übersetzungen (Überarbeiten)" nennt die Anzahl Ihrer Anpassungen. Lassen Sie die Auswahl auf "Alle Pakete" und klicken Sie auf "Anzeigen".

![Block Angepasste Übersetzungen (Überarbeiten) mit 388 Anpassungen, der Button Anzeigen markiert](assets/language_adaption_tool_adaptations1_v1_de.png){ class="shadow lightbox" title="Einstieg Angepasste Übersetzungen auf der Startseite" }

**d)** Die Übersetzungsliste zeigt die Anzahl der Anpassungen und die Pakete, in denen sie liegen. Mit "Anpassen" öffnen Sie die Einträge eines einzelnen Pakets. Mit "Alle anpassen" gehen Sie durch alle Einträge.

![388 angepasste Übersetzungen in 21 Paketen, je Paket ein Button Anpassen](assets/language_adaption_tool_adaptations2_v1_de.png){ class="shadow lightbox" title="Übersetzungsliste der Anpassungen" }

**e)** In der Bearbeitungsmaske sehen Sie den Standardtext und Ihre Anpassung. Mit "Speichern & weiter" springen Sie zum nächsten Eintrag.

![Standardtext SharePoint und Anpassung Mein-SharePoint, darunter die Buttons Speichern & weiter und Weiter](assets/language_adaption_tool_adaptations3_v1_de.png){ class="shadow lightbox" title="Bearbeitungsmaske einer Anpassung" }

Die Liste gilt immer für die Sprache, die im Feld "Sprache" gewählt ist. Rufen Sie die Liste für jede Sprache auf, in der Sie Anpassungen gemacht haben.

Wollen Sie nur innerhalb Ihrer eigenen Anpassungen suchen, wählen Sie im Abschnitt "Suche" bei "suchen in" die Option "Anpassungen".

Einen Export der Übersetzungsliste gibt es nicht, weder als Tabelle noch als Datei. Wollen Sie die Liste festhalten, drucken Sie die angezeigte Übersetzungsliste aus dem Browser, zum Beispiel als PDF. Nach einem Klick auf "Anpassen" gehen Sie mit "Weiter" und "Zurück" durch die gefilterten Einträge, ohne etwas zu ändern. Der Button "Sprachpakete exportieren" in der System-Administration unter `Administration > Core Konfiguration > Sprache und Region` exportiert ganze Systemsprachen als Sprachpaket für eine andere OpenOlat-Instanz. Ihre Anpassungen sind darin nicht enthalten. Mehr dazu finden Sie unter [Sprache und Region](../../manual_admin/administration/Core_functions.de.md).

!!! tip "Tipp"

    Führen Sie zusätzlich eine eigene Liste der angepassten Schlüssel mit dem Grund für die Anpassung. Das hilft Ihnen und Ihren Nachfolger:innen bei der Kontrolle nach einem Update.

[Zum Seitenanfang ^](#how_to_use)


## Variablen-Pakete {: #packages}

Auf programmtechnischer Seite sind die Texte der Screens in Variablen-Paketen zusammengefasst. Nachstehend eine Zusammenstellung der am häufigsten geänderten Pakete.


| Bereich, in dem die Variablen angezeigt werden |  Bezeichnung des Pakets                 |
| ---------------------------------------------- | --------------------------------------- |
| Hauptnavigation                                | org.olat.core.commons.chiefcontrollers  |
| Login                                          | org.olat.login                          |




[Zu Schritt 2: Zu welchem Variablen-Paket könnte der Begriff gehören? ^](#step2)<br>
[Zum Seitenanfang ^](#how_to_use)


## Häufig geänderte Beschriftungen und ihre Variablen {: #keys}

| Standardtext                  | Stelle, an der die Variable angezeigt wird               | Variable/Schlüssel        | im Paket                                |
| ----------------------------- | -------------------------------------------------------- | ------------------------- | --------------------------------------- |
| Katalog                       | Hauptnavigation                                          | topnav.catalog            | org.olat.core.commons.chiefcontrollers  |
| Katalog                       | Hauptnavigation Tooltipp                                 | topnav.catalog.alt        | org.olat.core.commons.chiefcontrollers  |
| Katalog                       | Titel des Suchfeldes                                     | header.search.title       | org.olat.modules.catalog.ui             |
| OpenOlat - infinite learning  | Titel der Loginseite                                     | login.header              | org.olat.login                          |
| Hier registrieren             | Link zur Selbstregistrierung auf der Loginseite          | menu.register             | org.olat.login                          |
| um OpenOlat nutzen zu können  | Text nach dem Link zur Selbstregistrierung               | menu.register.to.use      | org.olat.login                          |

Den Link zur Selbstregistrierung und den Text danach zeigt die Loginseite nur, wenn die Selbstregistrierung eingeschaltet und die Option "Auf Loginseite anzeigen" gesetzt ist.


[Zu Schritt 3: Welche Variable gehört zu diesem Text? ^](#step3)<br>
[Zum Seitenanfang ^](#how_to_use)


## Formatierungen und Umbrüche in einem Text {: #formatting}

Es gibt Variablen, die enthalten nicht nur ein einzelnes Wort, sondern einen Satz oder längeren Text.
Mit Hilfe von HTML-Code können Sie auch bestimmte Wörter fett oder als Überschrift kennzeichnen. Ebenso kann ein Umbruch mit einem HTML-Tag erzwungen werden.



[Zum Seitenanfang ^](#how_to_use)


## Was passiert bei einem OpenOlat-Update? {: #update_behaviour}

Ihre Anpassungen liegen ausserhalb der Applikation und bleiben bei einem Update erhalten. OpenOlat führt sie aber nicht nach. Wenn frentix einen Standardtext überarbeitet, bleibt Ihre Anpassung unverändert stehen. Ihre Nutzer:innen sehen also weiterhin Ihren Text. Umgekehrt erreicht sie eine Verbesserung des Standardtextes nicht.

Bei grösseren Umbauten der Oberfläche kann frentix einen Übersetzungsschlüssel umbenennen oder eine Stelle entfällt. Dann greift Ihre Anpassung nicht mehr und die Stelle erscheint wieder im Standardwortlaut.

Prüfen Sie Ihre Anpassungen deshalb nach einem grösseren Update. Die vollständige Liste finden Sie unter [Welche Anpassungen habe ich bereits gemacht?](#my_adaptations)

[Zum Seitenanfang ^](#how_to_use)


## Weiterführende Informationen {: #further_information}

[Persönliche Konfiguration: Einstellungen >](../../manual_user/personal_menu/Settings.de.md)<br>
[Core Konfiguration: Übersicht >](../../manual_admin/administration/Core_functions.de.md)<br>
[Customizing: Übersicht >](../../manual_admin/administration/Customizing.de.md)

[Zum Seitenanfang ^](#how_to_use)
