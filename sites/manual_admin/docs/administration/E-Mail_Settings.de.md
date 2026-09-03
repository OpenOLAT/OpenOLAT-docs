# E-Mail Einstellungen {: #email_settings}

Die E-Mail Einstellungen liegen in der System-Administration unter: `Administration > Core Konfiguration > E-Mail`. Die Seite hat zwei Segmente: "Einstellungen" mit den Vorgaben zur E-Mail-Adresse und zum OpenOlat Postfach, und "E-Mail Vorlage" mit dem Aussehen der versendeten E-Mails.

## E-Mail Adresse [:octicons-tag-16:{ title="ab Release 12.2 (OO-2981)" }](https://track.frentix.com/issue/OO-2981) {: #email_address}

Im Abschnitt "E-Mail Adresse" definieren Sie, welche Einschränkungen für die E-Mail-Adresse der Benutzer:innen gelten. Unter jeder der beiden Optionen nennt ein Link die Anzahl der Konten ohne E-Mail-Adresse bzw. ohne eindeutige E-Mail-Adresse. Der Link öffnet die Liste dieser Konten in der Benutzerverwaltung. Sind die E-Mail-Adresse oder ihre Eindeutigkeit optional, stehen einige Funktionen von OpenOlat nicht zur Verfügung, zum Beispiel die Selbstregistrierung, Vitero und WebDAV.

![Obligatorisch und Eindeutig ausgeschaltet, je ein Link zählt die betroffenen Konten: Abschnitt E-Mail Adresse](assets/Email_DE.png){ class="shadow lightbox" }

### Obligatorisch

Wenn diese Option _nicht_ aktiviert ist, bedeutet dies, dass die E-Mail-Adresse für ein Konto optional ist. Dies führt jedoch zu Einschränkungen, da OpenOlat darauf ausgelegt ist, dass jede Person eine E-Mail-Adresse hinterlegt hat. Folgende Einschränkungen treten auf (Liste nicht abschliessend):

  * Es werden keine realen E-Mails versendet.
  * Es werden keine Benachrichtigungen versendet.
  * Der Login mit der E-Mail-Adresse ist nicht möglich.
  * Das Passwort kann nicht zurückgesetzt werden.

### Eindeutig

Wenn diese Option nicht aktiviert ist, bedeutet dies, dass mehrere Konten dieselbe E-Mail-Adresse haben können. Folgende Einschränkungen treten auf (Liste nicht abschliessend):

  * Der Login mit der E-Mail-Adresse ist generell deaktiviert. Das heisst, es kann sich auf der ganzen Plattform niemand mehr mit der E-Mail-Adresse einloggen, nur noch mit dem Anmeldenamen. Dies gilt auch für Konten mit einer eindeutigen E-Mail-Adresse.
  * Bei Konten ohne eindeutige E-Mail-Adresse funktioniert das Zurücksetzen des Passworts nur noch über die Eingabe des Anmeldenamens, aber nicht mehr über die E-Mail-Adresse.

!!! warning "Achtung"

    In beiden Fällen können entweder keine oder keine eindeutigen E-Mails verschickt werden. Deshalb ist es zwingend empfohlen, das interne OpenOlat Postfach zu aktivieren! Ansonsten können unerwartete Fehler auftreten!

## E-Mail Postfach und Versand {: #e-mail-inbox-and-outbox}

OpenOlat verfügt über ein internes E-Mail-Postfach-System, das alle im System gesendeten und empfangenen E-Mails im persönlichen Postfach jeder Person auflistet: [Persönliche Werkzeuge: E-Mail](../../manual_user/personal_menu/E-Mail.de.md). Das E-Mail-Postfach in OpenOlat ist eine optionale Komponente.

### OpenOlat Postfach aktivieren

  * Ist das OpenOlat Postfach ausgeschaltet, so werden alle in OpenOlat erstellten E-Mails ausschliesslich an die persönliche E-Mail-Adresse versandt. Das OpenOlat Postfach ist in den persönlichen Werkzeugen nicht sichtbar.
  * Ist das OpenOlat Postfach eingeschaltet, so werden alle empfangenen und gesendeten E-Mails im persönlichen Postfach jeder Person aufgelistet.

Jede Person kann zudem in ihren persönlichen [Einstellungen](../../manual_user/personal_menu/Settings.de.md) festlegen, ob empfangene E-Mails nur intern oder auch an die persönliche E-Mail-Adresse zugestellt werden. Als Administrator:in legen Sie das Standardverhalten fest:

  * E-Mails an das interne OpenOlat Postfach zustellen
  * E-Mails an das interne OpenOlat Postfach und die persönliche E-Mail-Adresse zustellen

### Posteingang und Postausgang [:octicons-tag-16:{ title="ab Release 12.2 (OO-2982)" }](https://track.frentix.com/issue/OO-2982)

Für den Posteingang und den Postausgang legen Sie getrennt fest, was eine Person über die weiteren Empfänger:innen einer E-Mail sieht. In beiden Bereichen stehen dieselben zwei Schalter zur Verfügung:

  * "Namen der Empfänger anzeigen"
  * "E-Mail Adressen anzeigen"

## E-Mail Vorlage {: #template}

OpenOlat versendet für verschiedene Ereignisse E-Mails. Um die E-Mails attraktiver zu gestalten, werden diese als HTML-Mails inklusive Formatierung versendet. Mit der E-Mail Vorlage passen Sie das allgemeine Aussehen der E-Mails an.

Die E-Mail Vorlage gilt für alle E-Mails und steuert nur deren Aussehen, nicht deren Text. Den Text einer einzelnen E-Mail legen Sie dort fest, wo die E-Mail entsteht: [Texte einzelner E-Mails](#mail_texts).

Die folgenden Variablen müssen in der Vorlage vorkommen:

  *  **$content**: Wird ersetzt mit dem eigentlichen Inhalt der E-Mail. Der Inhalt ist in der Regel an die Sprache der Empfänger:in angepasst.
  *  **$footer**: Wird ersetzt mit der generischen Fusszeile. Die Fusszeile ist an die Sprache der Empfänger:in angepasst und lässt sich mit dem Sprachanpassungswerkzeug für jede Sprache ändern (Variablen `footer.no.userdata` und `footer.with.userdata` im Paket `org.olat.core.util.mail`).

### Texte einzelner E-Mails {: #mail_texts}

Mehrere Funktionen von OpenOlat bringen einen eigenen Mailtext mit. Diesen Text passen Sie in der jeweiligen Funktion an, nicht in der E-Mail Vorlage:

  * [Erinnerungen im Kurs](../../manual_user/learningresources/Course_Reminders.de.md#text): Betreff und Mailtext jeder Erinnerung, mit eigenen Variablen.
  * [Kursbaustein "E-Mail"](../../manual_user/learningresources/Course_Element_EMail.de.md): Betreff und Nachricht als Vorlage für die E-Mails, die der Kursbaustein versendet.
  * [Kursbaustein "Test"](../../manual_user/learningresources/Course_Element_Test.de.md#tab_email_confirmation): Betreff und Mailtext der Bestätigung nach der Testabgabe, wahlweise aus der Vorlage oder als eigener Text.
  * [Kursbaustein "Aufgabe"](../../manual_user/learningresources/Course_Element_Task.de.md#submission): vorformulierter Text der Bestätigung nach der endgültigen Abgabe, im Tab "Abgabe" anpassbar.
  * [Korrektur-Workflow eines Tests](../../manual_user/learningresources/Test_settings.de.md#correction-workflow): Mailtext für die Benachrichtigung der Korrektor:innen, wahlweise als eigener Text oder aus einer Vorlage.
  * [Zertifikatsprogramm](../../manual_user/area_modules/Course_Planner_Certification_Programs.de.md#config_tab_messages): Vorlagen der vorbereiteten Benachrichtigungen und der Erinnerungen zur Rezertifizierung, im Tab "Meldungen" anpassbar.
  * [Mitgliederverwaltung](../../manual_user/learningresources/Members_management.de.md#add_members): Im letzten Schritt des Assistenten "Mitglieder hinzufügen" formulieren Sie die E-Mail an die neuen Mitglieder, ebenfalls mit Variablen.
  * [e-Assessment Administration: Test](e-Assessment_Test.de.md#tab_correction-workflow): systemweit vorformulierte Texte für die E-Mails an die Beteiligten des Korrektur-Workflows, in mehreren Sprachen.
  * [Lebenszyklen: Konto](Life_cycles_-_Administration.de.md#lifecycle_accounts): Benachrichtigungen vor und nach Kontoablauf, Deaktivierung und Löschung, je Schritt einzeln formulierbar.
  * [Automatischer Gruppenlebenszyklus](Automatic_Group_Lifecycle.de.md): Benachrichtigungen vor und nach der Inaktivierung sowie vor und nach der Löschung einer Gruppe.

### Texte der System-Mails {: #system_mails}

Viele E-Mails entstehen ohne Zutun einer Person: der Validierungscode bei der Registrierung, die Meldung vor dem Ablauf eines Kontos oder die Bestätigung beim Eintritt in eine Gruppe. Für diese System-Mails gibt es kein Textfeld in der System-Administration. Ihr Text ist als Variable im Sprachpaket der jeweiligen Funktion abgelegt.

Anpassen lässt sich der Text mit dem Sprachanpassungswerkzeug in der System-Administration unter:<br>
`Administration > Customizing > Sprachanpassungswerkzeug`

Die Anleitung [Wie verwende ich das Sprachanpassungswerkzeug?](../../manual_how-to/language_adaption_tool/language_adaption_tool.de.md) zeigt Schritt für Schritt, wie Sie die Variable zu einem Text finden und ihren Wert ändern.

Die Hürde liegt dabei nicht im Werkzeug, sondern im Auffinden der Variable: Die Mailtexte verteilen sich über die Sprachpakete aller Funktionen, die E-Mails versenden. Wenn Sie die passende Variable nicht finden, wenden Sie sich an den Support Ihrer OpenOlat-Instanz. Dort erfahren Sie, in welchem Paket die Variable liegt und wie sie heisst.

## E-Mail Signatur [:octicons-tag-16:{ title="ab Release 18.0 (OO-6616)" }](https://track.frentix.com/issue/OO-6616) {: #signature}

Mit der E-Mail Signatur hängt OpenOlat den persönlichen Text einer Person an das Ende der E-Mails, die diese Person aus OpenOlat heraus über ein E-Mail-Formular verschickt, zum Beispiel über den Kursbaustein "E-Mail", den Kursbaustein "Liste der Teilnehmer:innen" oder die Mitgliederverwaltung. Der Text steht im Mailfenster am Ende der Nachricht und lässt sich dort vor dem Versand noch bearbeiten. Die Signatur erfasst jede Person selbst: [Persönliche Konfiguration: Profil](../../manual_user/personal_menu/Profile.de.md).

Damit das Feld für die Signatur im Profil erscheint, aktivieren Sie das Attribut "emailSignature" in der System-Administration unter:<br>
`Administration > Customizing > Benutzer:innen-Attribute`

**Schritt 1: Tab "Properties", Zeile "emailSignature" aktivieren**

<details>
    <summary>Screen</summary>
	<img src="../assets/e-mail_settings_activate1_v1_de.png" alt="Spalte Aktiv gibt emailSignature systemweit frei: Tab Properties der Seite Benutzer:innen-Attribute" />
</details>

**Schritt 2: Tab "Contexts", Kontext "org.olat.user.ProfileFormController" bearbeiten**

<details>
    <summary>Screen</summary>
	<img src="../assets/e-mail_settings_activate2_v1_de.png" alt="Link Bearbeiten öffnet die Attributliste von org.olat.user.ProfileFormController: Tab Contexts der Seite Benutzer:innen-Attribute" />
</details>

Im Kontext schalten Sie für "emailSignature" die Spalte "Verwenden" ein. Erst damit steht das Feld im Profil zur Verfügung.

<details>
    <summary>Screen</summary>
	<img src="../assets/e-mail_settings_activate3_v1_de.png" alt="Spalte Verwenden gibt emailSignature für das persönliche Profil frei: Dialog Context bearbeiten" />
</details>

Die empfohlene Einstellung:

![Nur Verwenden eingeschaltet, Zwingend, Admin only und User readonly aus: Zeile emailSignature im Dialog Context bearbeiten](assets/e-mail_settings_activate4_v1_de.png){ class="shadow lightbox" }

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Persönliche Werkzeuge: E-Mail >](../../manual_user/personal_menu/E-Mail.de.md)<br>
[Persönliche Konfiguration: Einstellungen >](../../manual_user/personal_menu/Settings.de.md)<br>
[Erinnerungen >](../../manual_user/learningresources/Course_Reminders.de.md)<br>
[Kursbaustein "E-Mail" >](../../manual_user/learningresources/Course_Element_EMail.de.md)<br>
[Kursbaustein "Test" >](../../manual_user/learningresources/Course_Element_Test.de.md)<br>
[Kursbaustein "Aufgabe" >](../../manual_user/learningresources/Course_Element_Task.de.md)<br>
[Test Einstellungen - Administration >](../../manual_user/learningresources/Test_settings.de.md)<br>
[Course Planner: Zertifikatsprogramme >](../../manual_user/area_modules/Course_Planner_Certification_Programs.de.md)<br>
[Mitgliederverwaltung >](../../manual_user/learningresources/Members_management.de.md)<br>
[e-Assessment Administration: Test >](e-Assessment_Test.de.md)<br>
[Lebenszyklen: Übersicht >](Life_cycles_-_Administration.de.md)<br>
[Automatischer Gruppenlebenszyklus >](Automatic_Group_Lifecycle.de.md)<br>
[Wie verwende ich das Sprachanpassungswerkzeug? >](../../manual_how-to/language_adaption_tool/language_adaption_tool.de.md)<br>
[Persönliche Konfiguration: Profil >](../../manual_user/personal_menu/Profile.de.md)

[Zum Seitenanfang ^](#email_settings)
