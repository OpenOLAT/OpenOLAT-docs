# One Time Code {: #one_time_code}

Wenn Sie sich anmelden und nach Benutzername und Passwort ein zusätzlicher Schritt "Login - Validierung" erscheint, hat Ihre Organisation den One Time Code als zweiten Faktor aktiviert. OpenOlat schickt Ihnen dann einen Bestätigungscode per E-Mail, den Sie eingeben, um die Anmeldung abzuschliessen. Diese Seite erklärt, was ein One Time Code ist und wie die Anmeldung damit abläuft.

## Was ist ein One Time Code? [:octicons-tag-16:{ title="ab Release 21.0 (OO-9509)" }](https://track.frentix.com/issue/OO-9509) {: #about}

Ein One Time Code ist ein 8-stelliger Bestätigungscode, den OpenOlat Ihnen während der Anmeldung per E-Mail zustellt. Er dient als zweiter Faktor (2-Faktoren-Authentifizierung) zusätzlich zu Ihrem Passwort und ist nur für den aktuellen Anmeldevorgang gültig.

Voraussetzung ist eine gültige E-Mail-Adresse an Ihrem Konto, denn ohne sie kann der Code nicht zugestellt werden.

[Zum Seitenanfang ^](#one_time_code)

---

## So melden Sie sich mit One Time Code an {: #login}

1. Geben Sie Ihren Benutzernamen und Ihr Passwort wie gewohnt ein.
2. OpenOlat zeigt den Schritt "Login - Validierung" an und sendet Ihnen eine E-Mail mit dem Betreff "Bestätigungscode für \<Instanzname\> Login".
3. Öffnen Sie die E-Mail und übernehmen Sie den 8-stelligen Code in das Feld "Bestätigungscode".
4. Klicken Sie auf "Login", um die Anmeldung abzuschliessen.

Ist der Code falsch, erscheint der Hinweis "Bestätigungscode (OTP) ist nicht gültig." und Sie können den Code erneut eingeben.

[Zum Seitenanfang ^](#one_time_code)

---

## Ich habe keinen Code erhalten {: #no_code}

Klicken Sie auf der Validierungsseite auf "Email neu versenden". OpenOlat erzeugt einen neuen Code und schickt ihn an die hinterlegte E-Mail-Adresse. Alle früher zugestellten Codes verlieren damit ihre Gültigkeit. Prüfen Sie auch den Spam-Ordner. Falls keine E-Mail-Adresse an Ihrem Konto hinterlegt ist oder der Versand dauerhaft ausbleibt, wenden Sie sich an Ihren Support.

[Zum Seitenanfang ^](#one_time_code)

---

## Verhältnis zu Passkey {: #passkey}

One Time Code und [Passkey](Passkey.de.md) schliessen sich nicht aus:

* Ist nur der One Time Code aktiviert, erfolgt die Anmeldung mit Passwort und Code per E-Mail.
* Ist zusätzlich Passkey aktiviert und Sie haben einen Passkey hinterlegt, übernimmt der Passkey den zweiten Faktor. Der One Time Code dient dann als Ausweichlösung, falls noch kein Passkey vorhanden ist.

Ob und welche Verfahren aktiv sind, legt die Administration fest.

[Zum Seitenanfang ^](#one_time_code)

---

## Weiterführende Informationen {: #further_information}

[Login-Konzept >](Login_Concept.de.md)<br>
[Passkey >](Passkey.de.md)<br>
[Login-Seite >](Login_Page.de.md)<br>

[Zum Seitenanfang ^](#one_time_code)
