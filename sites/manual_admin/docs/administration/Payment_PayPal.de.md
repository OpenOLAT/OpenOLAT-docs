# PayPal Konfiguration {: #PayPal}

Das PayPal Bezahlungsmodul erlaubt es Autor:innen, Kurse und Arbeitsgruppen gegen Geld freizuschalten. Ihre Kunden können dabei entweder mit Kreditkarte oder direkt über PayPal bezahlen, sofern sie einen PayPal Account besitzen. Dieser ist aber für Ihre Kunden nicht zwingend notwendig. In der PayPal Konfiguration der Systemadministration können Sie die PayPal Kontoinformationen hinterlegen, die für alle Bezahlprozesse verwendet werden sollen.

Um die PayPal Bezahlmethode verwenden zu können, müssen Sie über ein PayPal Firmenkonto verfügen. Ein solches Konto können Sie bei PayPal ohne weitere Kosten erstellen. In Ihrem PayPal Konto können Sie anschliessend eine sogenannte API-Berechtigung erstellen. Diese besteht aus der Client-ID und dem Schlüssel. Diese beiden Sicherheitselemente müssen Sie in der PayPal Konfiguration von OpenOlat hinterlegen, damit das System die Bezahlungen Ihrer Kunden auf Ihr Konto abwickeln kann. Weiter unten finden Sie Hinweise, wie Sie diese Sicherheitselemente auf der PayPal Webseite erstellen können.

## Verwendung in Kursen und Arbeitsgruppen

Um Kurse und Arbeitsgruppen gegen Geld freizuschalten, können Sie nach
erfolgreicher Konfiguration des PayPal Moduls auf der Detailseite des Kurses oder in der Administrationsumgebung der Arbeitsgruppe die PayPal Angebotsart auswählen. Weitere Informationen finden Sie unter [Zugangskonfiguration / Freigabe](../../manual_user/learningresources/Access_configuration.de.md).

!!! warning "Achtung"
	Je nach Währung, Land und Betrag verlangt PayPal eine Transaktionsgebühr.
	Diese beträgt ca. 5% des Betrages und wird von dem jeweiligen Betrag
	abgezogen.

[Zum Seitenanfang ^](#PayPal)

---


## PayPal API Berechtigung erstellen

Loggen Sie sich in Ihr PayPal Firmenkonto ein und vollziehen Sie Einstellungen zur Verbindung mit OpenOlat.

!!! note "Hinweis"
    Bitte berücksichtigen Sie, dass wir keine Anleitung für Drittanbieter pflegen. Nachfolgend finden Sie die Fixpunkte, damit Sie sich entsprechend orientieren können. Eine Schritt-für-Schritt-Anleitung bietet Ihnen möglicherweise die Anleitung des gewählten Tools.

- [x] Richten Sie eine Onlinezahlung in Ihrem Geschäftskonto ein.
- [x] Lassen Sie sich eine API-Berechtigung ausstellen.
- [x] Speichern Sie sich sowohl die Client-ID als auch den Schlüssel.
- [x] Stellen Sie sicher, dass die richtige Währung eingestellt ist.
- [x] Tipp:
a) "Zahlungseingänge in einer anderen Währung zulassen und umrechnen in Schweizer Franken".
b) "Doppelte Zahlungen sollten sie vermeiden".
- [x] loggen Sie sich nun mit einem Systemadministrator-Account bei Ihrem OpenOlat System ein.
a) Klicken Sie auf den Tab "Administration"
b) Klicken Sie links in der Navigation auf "Bezahlungsmodule" und dann auf "PayPal".
c) Aktivieren Sie das PayPal-Modul in OpenOlat, indem Sie PayPal einschalten.
d) Wählen Sie als Integration den Wert "PayPal Smart Buttons". Nur mit dieser Variante ist ein Bezahlen mit Kreditkarte möglich, ohne dass der Käufer ein PayPal-Konto eröffnen muss.
e) Wählen Sie die Währung und geben anschliessend die "Client ID" sowie den "Client secret" (=Schlüssel) ein, den Sie zuvor zwischengespeichert haben.

[Zum Seitenanfang ^](#PayPal)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Zugangskonfiguration / Freigabe >](../../manual_user/learningresources/Access_configuration.de.md)

[Zum Seitenanfang ^](#PayPal)