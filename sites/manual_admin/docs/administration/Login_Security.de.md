# Sicherheit {: #security}


Die Anforderungen an die Sicherheit können je nach Institution variieren. In den **systemweiten Sicherheitseinstellungen** können Sie daher den notwendigen Level an Sicherheit unter Berücksichtigung der damit eingegangenen Risiken einstellen. Die höchste Sicherheitsstufe erreichen Sie, wenn sämtliche Sicherheitsfunktionen eingeschaltet sind.


## Tab Konfiguration {: #tab_config}

![login_security_tab_config_v1_de.png](assets/login_security_tab_config_v1_de.png){ class="shadow lightbox" }


### Dateien in Ordnern {: #files}

**Dateidownload in Ordner erzwingen**: Wählen Sie diese Sicherheitsfunktion, um in der Ordnerkomponente Dateien immer herunterzuladen und nie direkt im Browser zu öffnen. Damit werden allfällige Cross-Site-Scripting (XSS) Attacken verhindert. Ist diese Funktion eingeschaltet werden auch in Ordnern abgelegte HTML-Seiten als Dateien heruntergeladen und nicht mehr direkt im Browser geöffnet. Der Kursbaustein "HTML-Seite" ist von diesem Mechanismus nicht betroffen.


### HTTP-Header {: #headers}

**Frame Einbettung per JavaScript verhindern**: Diese Funktion ist dauerhaft eingeschaltet und lässt sich im Formular nicht ändern. Aus Kompatibilitätsgründen können einige Komponenten von OpenOlat (TinyMCE) nicht in einem Frame dargestellt werden.

**Frame Einbettung mit HTTP header X-FRAME-OPTIONS=SAMEDOMAIN verhindern**: Wählen Sie diese Sicherheitsfunktion, um das Laden von OpenOlat in einem Frame oder iFrame zu verhindern. Damit werden allfällige Cross-Frame-Scripting Attacken verhindert (XFS). Ist diese Funktion eingeschaltet können Sie OpenOlat nicht in eine bestehende Webseite mittels Frames einbetten.

**Verhindern HTTPS zu HTTP downgrade mit HTTP Header**: Der Browser ruft die Plattform ausschliesslich über HTTPS auf, auch wenn ein Link auf HTTP zeigt. OpenOlat sendet dafür den Header `Strict-Transport-Security`, gültig für ein Jahr und einschliesslich Subdomains.

**Verhindert Browser Script und Style Dateien mit HTTP Header zu raten**: Der Browser hält sich an den vom Server gemeldeten Dateityp, statt ihn aus dem Inhalt zu erraten. OpenOlat sendet dafür den Header `X-Content-Type-Options: nosniff`.


### Schutz vor gefälschten Anfragen {: #csrf}

**Cross-Site Request Forgery (CSRF) Schutz**: Diese Konfiguration erhöht die Sicherheit gegen gefälschte Anfragen, die im Namen einer angemeldeten Person von einer fremden Webseite aus gestellt werden.

**SameSite cookie**: Bestimmt, bei welchen Aufrufen von anderen Webseiten das Sitzungscookie mitgesendet wird. Zur Wahl stehen `Strict`, `Lax` und `None`, wobei `Strict` die restriktivste Einstellung ist.


### Content Security Policy {: #csp}

**Content Security Policy (CSP)**: Legt fest, aus welchen Quellen der Browser Inhalte für OpenOlat laden darf.

!!! warning "Auswirkung auf Inhalte"
    Diese Konfiguration kann Inhalte wie den LTI-Kursbaustein, die externe Seite und die HTML-Seite sperren. Die Kursbausteine card2brain, edubase, edubook, GoToTraining, openmeeting, vitero und PayPal werden zurzeit nicht unterstützt.

Ist die Content Security Policy eingeschaltet, erscheinen zusätzlich die Einstellung **Report only** sowie die Eingabefelder der einzelnen Direktiven. Mit **Report only** werden Verstösse nur protokolliert und nicht blockiert; die Meldungen finden Sie im Tab *Content security policy log*.

??? info "Die einzelnen Direktiven"
    Für jede Direktive können Sie eigene Quellen hinterlegen, jeweils als Adresse in der Form `https://example.com`. Unter dem Eingabefeld zeigt OpenOlat den Wert, der immer enthalten ist und durch Ihre Eingabe ergänzt wird.

    | Direktive | Gilt für |
    |---|---|
    | `default-src` | alle Inhaltstypen ohne eigene Direktive |
    | `form-action` | Ziele, an die Formulare gesendet werden |
    | `script-src` | JavaScript |
    | `style-src` | Stylesheets |
    | `img-src` | Bilder |
    | `font-src` | Schriften |
    | `connect-src` | Verbindungen aus dem Browser, etwa für Datenabrufe im Hintergrund |
    | `frame-src` | Seiten, die OpenOlat in einem Frame einbindet |
    | `frame-ancestors` | Seiten, die OpenOlat selbst einbinden dürfen |
    | `media-src` | Audio und Video |
    | `object-src` | eingebettete Objekte |



[Zum Seitenanfang ^](#security)


## Tab Content security policy log {: #tab_csp-log}

Dieser Tab erscheint, sobald die Content Security Policy eingeschaltet ist. Er listet die gemeldeten Verstösse auf.

![login_security_tab_csp-log_v1_de.png](assets/login_security_tab_csp-log_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#security)


## Tab Medien-Server {: #tab_mediaserver}

Hier können die für OpenOlat freigegebenen Medien-Server bestimmt werden.

![login_security_tab_mediaserver_v1_de.png](assets/login_security_tab_mediaserver_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#security)
