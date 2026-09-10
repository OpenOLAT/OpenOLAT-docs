# WebDAV

## Modulkonfiguration

Das WebDAV Modul kann für das gesamte OpenOlat System ein- oder ausgeschaltet
werden. Sie finden die Einstellungen in der System-Administration unter:<br>
`Administration > Core Konfiguration > WebDAV`

Die folgenden Konfigurationen können vorgenommen werden:

#### WebDAV Zugang {: #webdav_access}

Schalten Sie den WebDAV Zugang systemweit ein oder aus. Wenn das Modul eingeschaltet ist, können alle OpenOlat Benutzer das System über WebDAV nutzen (empfohlen).

#### WebDAV Links anzeigen {: #webdav_links}

Unabhängig von der WebDAV Funktion können Sie entscheiden, ob die WebDAV URL in der Ordnerkomponente angezeigt werden soll oder nicht. Wenn diese Funktion ausgeschaltet ist, kann WebDAV immer noch verwendet werden, es wird lediglich der Link nicht angezeigt.

#### Digest Authentication {: #digest_authentication}

!!! warning "Sicherheitshinweis"
    Die Digest-Authentication Verschlüsselung verwendet keine starke Kryptographie und kann mit entsprechendem Aufwand geknackt werden. Bei hohen Sicherheitsanforderungen sollte immer der HTTPS Zugang mit SSL Verschlüsselung verwendet werden.

#### WebDAV Client Verbot {: #webdav_client_exclusion}

Das Ausschliessen von spezifischen WebDAV-Clients ein- / ausschalten.

#### Liste von User-Agent (Komma als Trennzeichen) {: #user_agent_list}

Liste der nicht erlaubten User-Agents.

* * *

#### Kurse nach Semesterdaten gruppieren {: #group_by_semester}

Aktivieren Sie diese Option, um für jedes Semester einen Unterordner zu erstellen, der alle Kurse dieses Semesters enthält. Diese Option erhöht die Nutzbarkeit bei vielen Kursen. Wenn diese Option aktiviert ist, wird für die beendeten Kurse kein Ordner "_finished" erstellt. Sofern diese Option nicht aktiviert ist, sind im WebDAV alle beendeten Kurse im Ordner "_finished" zu finden.

#### Kurse nach CPL Elementen gruppieren {: #group_by_cpl_elements}

Aktivieren Sie diese Option, um für jedes CPL-Element einen Unterordner zu erstellen, der alle Kurse dieses Elements enthält.

#### "Managed" Kurse gruppieren {: #group_managed_courses}

Aktivieren Sie diese Option, um für extern verwaltete ("managed") Kurse einen eigenen Unterordner "_managed" zu erstellen.

#### Kennzeichen dem Titel voranstellen {: #prepend_reference}

Legen Sie fest, ob das [Kennzeichen](../../manual_user/learningresources/Course_Settings_Info.de.md) dem Kurstitel zur besseren Unterscheidung ähnlicher Titel vorangestellt werden soll.

* * *

#### Zugriff für Student:innen / Betreuer:innen Kurse {: #access_courses}

Aktivieren Sie diese Option, um auch Student:innen und Betreuer:innen den Zugriff auf ihre Kursordner zu gestatten. Es werden nur die Ordner der entsprechenden Ordner-Kursbausteine angezeigt, sowie ein eventuell eingebundener Ressourcenordner.

#### Zugriff für Student:innen / Betreuer:innen Favoriten {: #access_favorites}

Aktivieren Sie diese Option, um auch Student:innen und Betreuer:innen den Zugriff auf Kursordner von Kursen zu gestatten, die sich in ihrer Favoritenliste befinden, deren Mitglieder sie aber nicht sind. Dies ist nur möglich mit den entsprechenden Einstellungen in der Zugriffskonfiguration. Es werden nur die Ordner der entsprechenden Ordner-Kursbausteine angezeigt, sowie ein eventuell eingebundener Ressourcenordner.

## Verwendung

Weitere Informationen zur Anwendung von WebDAV in OpenOlat finden Sie unter [Einsatz von WebDAV](../../manual_user/basic_concepts/Using_WebDAV.de.md).

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kurseinstellungen - Tab Info >](../../manual_user/learningresources/Course_Settings_Info.de.md)<br>
[Einsatz von WebDAV >](../../manual_user/basic_concepts/Using_WebDAV.de.md)

**Weiterführend**<br>
[Persönliche Konfiguration: Einstellungen >](../../manual_user/personal_menu/Settings.de.md)

[Zum Seitenanfang ^](#webdav)
