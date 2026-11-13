# System {: #system}

![Menü System in der System-Administration mit zehn Bereichen, darunter Info messages, Errors, Caches und Scheduler, für Systeminformationen, Wartung und Diagnose](assets/admin_system_overview_v1_de.png){ class="shadow lightbox aside-left-lg" }

Im Bereich "System" der OpenOlat-Administration erhalten Systemadministrator:innen allgemeine Informationen zur Runtime, wie genutzter Speicher, aktuelle Klickzahlen oder Verzeichnisse.

Die Systemadministrator:innen haben hier Zugriff auf das nebenstehende Menü.

---

## Info messages {: #info_message}

Hier kann im OpenOlat HTML Editor eine Info Message erstellt werden, die auf der **Login-Seite** neben dem eigentlichen Login Zugangsbereich erscheint.

Auch für Meldungen bezüglich **Wartungsarbeiten** gibt es einen eigenen Bereich. Diese Information erscheint auf allen OpenOlat-Seiten und kann ebenfalls im OpenOlat-Editor erstellt werden.

Zusätzlich können Dokumente (z.B. weitere Infos in pdf-Form) verlinkt werden. Hierfür steht ein "Static Ordner" zur Verfügung.

[Zum Seitenanfang ^](#system)



## Aktive Sitzungen {: #active_sessions}

Hier sehen Sie die Sitzungen der aktuell angemeldeten Personen. Die Spalte "Modus" zeigt, über welchen Zugang eine Sitzung entstanden ist, zum Beispiel "WebDAV", "REST" oder "Content". Der Wert "Content" steht für einen Zugriff über die [Inhaltsdomäne](../../manual_user/basic_concepts/Content_Domain.de.md) (separate Adresse für Inhalte). Eine solche Sitzung liefert nur Inhalte aus und erhält keine OpenOlat-Oberfläche. Deshalb kann dieselbe Person zweimal in der Liste stehen: einmal mit ihrer Sitzung in OpenOlat und einmal mit dem Modus "Content".

[Zum Seitenanfang ^](#system)



## Errors {: #errors}

!!! info "frentix-Kund:innen"
    Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix die Einstellung "Log levels".

Im Tab "Fehler" suchen Systemadministrator:innen eine Fehlermeldung nach Fehlernummer und Datum.

Im Tab "Log levels" legen Systemadministrator:innen für jeden Logger fest, wie ausführlich OpenOlat protokolliert: "Error", "Warn", "Info" oder "Debug".

[Zum Seitenanfang ^](#system)



## Log Dateien {: #log_files}

!!! info "frentix-Kund:innen"
    Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix diese Konfiguration.

Hier finden Systemadministrator:innen die Dateien im Log-Verzeichnis des Servers, je mit Dateiname und Grösse. Ein Klick auf einen Dateinamen lädt die Datei herunter. Die Dateien "olat.log", "catalina.out" und "syncher.log" stehen zuoberst, die übrigen folgen nach dem Datum der letzten Änderung, die neueste zuerst.

[Zum Seitenanfang ^](#system)



## Caches {: #caches}

!!! info "frentix-Kund:innen"
    Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix diese Konfiguration.

Hier sehen Systemadministrator:innen die Cache-Einstellungen und leeren die OpenOlat-Caches.

[Zum Seitenanfang ^](#system)



## Locks {: #locks}

Hier sehen Systemadministrator:innen die Objekte, die Benutzer:innen gesperrt haben.

[Zum Seitenanfang ^](#system)



## Database ORM {: #database}

!!! info "frentix-Kund:innen"
    Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix diese Konfiguration.

Die Seite "Database ORM" liefert Statistik-Angaben und listet JPA Queries und JPA Entities.

[Zum Seitenanfang ^](#system)



## Java VM Infos {: #java}

Hier finden Systemadministrator:innen Informationen zum Java Speicher, zu Threads und Umgebungsvariablen und können die Java Garbage Collection starten.

[Zum Seitenanfang ^](#system)



## Scheduler {: #scheduler}

Hier finden Systemadministrator:innen eine Übersicht über Scheduler-Jobs.

[Zum Seitenanfang ^](#system)



## Konfigurationen {: #system_config}

!!! info "frentix-Kund:innen"
    Bei frentix-Kund:innen übernimmt die zuständige Kundenberatung bei frentix diese Konfiguration.

Hier finden Systemadministrator:innen eine Auflistung aller Keys der Standard-Variablen und die Modul-Konfigurationen.

[Zum Seitenanfang ^](#system)


## Weiterführende Informationen {: #further_information}

[Inhaltsdomäne >](../../manual_user/basic_concepts/Content_Domain.de.md)<br>
[WebDAV >](WebDAV.de.md)<br>
[REST API >](REST_API.de.md)

[Zum Seitenanfang ^](#system)
