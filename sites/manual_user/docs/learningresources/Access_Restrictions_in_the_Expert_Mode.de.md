# Zugriffsbeschränkungen im Expertenmodus

## Einstieg in die Expertenregeln

!!! info "Wichtig"

    Die Tabs "Sichtbarkeit" und "Zugang" gibt es nur in herkömmlichen Kursen. Den Expertenmodus verwenden Sie deshalb nur dort, nicht in [Lernpfadkursen](Learning_path_course.de.md).

Sie möchten festlegen, wer einen Kursbaustein sieht und öffnet, zum Beispiel erst ab einem Datum oder nur eine bestimmte Gruppe. In herkömmlichen Kursen legen Sie das in den Tabs "Sichtbarkeit" und "Zugang" des Kursbausteins fest. Dort sperren Sie den Kursbaustein zum Beispiel für Teilnehmende, geben ihn nur für bestimmte Gruppen frei oder schalten ihn ab einem Datum frei.

Reichen die Optionen des einfachen Modus nicht aus, wechseln Sie in den Expertenmodus. Dort schreiben Sie die Regel selbst und bestimmen Sichtbarkeit und Zugang genau so, wie Ihr Kurs es verlangt. Sie geben einen Kursbaustein zum Beispiel nur für bestimmte Benutzernamen frei, verknüpfen mehrere Bedingungen miteinander oder arbeiten mit relativen Daten. Ein Beispiel:

??? tip "Beispiel Umfrage"

    Sie möchten eine Umfrage erst in der letzten Kurswoche freischalten und das schon heute einrichten, damit Sie es später nicht vergessen.

    Dazu schalten Sie den Kursbaustein "Umfrage" datumsabhängig frei und müssen sich im Kursverlauf nicht mehr darum kümmern. Im einfachen Modus geben Sie in den Tabs "Sichtbarkeit" und "Zugang" des Kursbausteins das Anfangs- und das Enddatum ein. Soll nur eine bestimmte Gruppe die Umfrage sehen, wählen Sie dort zusätzlich "Gruppenabhängig". So verwenden Sie zum Beispiel in einem Online-Kurs mit Teilnehmenden aus zwei Institutionen zwei verschiedene Umfragen. Voraussetzung ist, dass Sie die Teilnehmenden auf zwei Gruppen verteilt haben, die Sie den Umfragen zuweisen.

Mit Expertenregeln setzen Sie auch Fälle um, die der einfache Modus nicht abdeckt, und sparen sich wiederkehrende Handgriffe im Kursverlauf. Wie eine Sprache folgen Expertenregeln einer festen Syntax. Enthält eine Regel einen Syntaxfehler, meldet OpenOlat den Fehler. Das hilft vor allem am Anfang und ohne Programmierkenntnisse. Eine Expertenregel prüft, ob ein bestimmtes Attribut WAHR oder FALSCH ist.

Die Syntax lernen Sie am einfachsten kennen, wenn Sie zuerst im einfachen Modus eine Regel festlegen. Erstellen Sie dazu einen Kursbaustein, zum Beispiel eine "HTML-Seite", und kreuzen Sie im Tab "Zugang" die Option "Für Teilnehmende gesperrt" an.

Klicken Sie danach auf "Expertenmodus anzeigen". Sie sehen Ihre erste Expertenregel in ihrer Syntax:

    (  ( isCourseCoach(0) | isCourseAdministrator(0) ) )

Der gesamte Ausdruck steht in zwei Klammerpaaren. Das äussere Paar dürfen Sie in diesem Fall weglassen. `isCourseCoach(0)` prüft, ob die Person Betreuer:in des Kurses ist, `isCourseAdministrator(0)`, ob sie Besitzerrechte am Kurs hat. Der senkrechte Strich "|" in der Mitte steht für den booleschen Operator ODER. Die Regel ist also WAHR für Betreuer:innen ODER Personen mit Besitzerrechten. Nur sie öffnen die "HTML-Seite".

Ersetzen Sie nun den Operator "|" durch "&":

    isCourseCoach(0) & isCourseAdministrator(0)

Jetzt öffnen nur Betreuer:innen den Kursbaustein, die zugleich Besitzerrechte am Kurs haben. Diese Regel lässt sich nur im Expertenmodus festlegen.

Auf dieselbe Weise probieren Sie weitere Attribute und Operatoren aus. Die folgenden Abschnitte beschreiben die verfügbaren Attribute und zeigen an Beispielen, was eine Regel bewirkt.

## Konfiguration von Expertenregeln

Eine Expertenregel prüft, ob ein Attribut einen bestimmten Wert hat. Drei einfache Beispiele:

Attribut| Beschreibung| Beispiel Expertenregel
---|---|---
isGuest| nur für Gäste zugänglich| isGuest(0)
isCourseCoach| nur für Betreuer:innen sichtbar| isCourseCoach(0)
isUser| nur für eine bestimmte Benutzer:in verfügbar| isUser("pmuster")

### Arbeiten mit den Konstanten "TRUE" und "FALSE"

Mit den Konstanten "true" und "false" prüfen Sie, ob ein Attribut zutrifft ("true" oder "1") oder nicht zutrifft ("false" oder "0"). Ein solcher Wert heisst boolescher Wert, nach George Boole, dem Begründer der booleschen Algebra. Er kennt nur zwei Zustände: "true" = "1" = wahr oder "false" = "0" = falsch.

Beispiel: Bereiche für Gäste freigeben

Ein praktisches Beispiel ist eine Regel für den Zugang zu einem Kursbaustein.

**Fall 1**: Nur Gäste sollen einen Kursbaustein öffnen, zum Beispiel um Bereiche für Gäste und für registrierte Benutzer:innen zu trennen.<br>
Eine Person erhält also Zugang, wenn das Attribut "isGuest" für sie wahr ist. Die Regel lässt sich auf drei Arten schreiben:

 `isGuest(0)` oder `isGuest(0)=1` oder `isGuest(0)=true`



**Fall 2**: Alle ausser Gästen sollen den Kursbaustein öffnen. Eine Person erhält also Zugang, wenn das Attribut "isGuest" für sie nicht wahr ist. Die Regel lässt sich auf zwei Arten schreiben:

 `isGuest(0)=0` oder `isGuest(0)=false`

Alle Bestandteile, aus denen Sie Expertenregeln bauen, listet die folgende Tabelle auf.

 Funktionen, Operatoren und andere Expertenregel Komponenten

Typ| Syntax| Bedeutung
---|---|---
 **Konstanten**|  _TRUE_ oder _1_|  Wahr
 | _FALSE_ oder _0_|  Falsch
 | _ANY_COURSE_|  Abfrage soll für jeden Kurs gelten (nur für isCourseAdministrator(), isCourseCoach(), isCourseParticipant()) 
 **Variable**|  _now_|  Momentane Server-Systemzeit
 **Funktionen**|  _ _date("_ [date] _")__|  Datum abfragen
 |  _inLearningGroup("_ [string] _")_|  Gibt TRUE zurück, wenn die Person Mitglied der Lerngruppe [string] ist.
 |  _inRightGroup("_ [string] _")_|  Gibt TRUE zurück, wenn die Person Mitglied der Rechtegruppe [string] ist.
 |  _isLearningGroupFull("_ [string] _")_|  Gibt für die angegebene Lerngruppe den Boolean TRUE (= voll) oder FALSE (= nicht voll) zurück.
 |  _isUser("_ [string] _")_|  Gibt TRUE zurück, wenn die Person den Benutzernamen [string] hat.
 |  _inLearningArea("_ [string] _")_|  Gibt TRUE zurück, wenn die Person Mitglied einer Gruppe im Lernbereich [string] ist.
 |  _isGlobalAuthor(0)_|  Gibt TRUE zurück, wenn die Person die Rolle Autor:in hat.
 |  _isCourseAdministrator(0)_|  Gibt TRUE zurück, wenn die Person Besitzerrechte an Ihrem Kurs hat, etwa als Besitzer:in, Lernressourcenverwalter:in oder Administrator:in.
 |  _isCourseAdministrator( _ANY_COURSE_ )_| Gibt TRUE zurück, wenn die Person Besitzer:in eines beliebigen Kurses auf dem System ist (Lernressource) oder die Rolle Lernressourcenverwalter:in oder Administrator:in hat.
 |  _isCourseCoach(0)_|  Gibt TRUE zurück, wenn die Person den Kurs oder eine Gruppe des Kurses betreut.
 |  _isCourseCoach( _ANY_COURSE_ )_| Gibt TRUE zurück, wenn die Person einen beliebigen Kurs oder eine Gruppe eines beliebigen Kurses betreut.
 |  _isCourseParticipant(0)_|  Gibt TRUE zurück, wenn die Person Teilnehmer:in des Kurses ist.
 |  _isCourseParticipant( _ANY_COURSE_ )_| Gibt TRUE zurück, wenn die Person in einem beliebigen Kurs als Teilnehmer:in eingetragen ist.
 |  _isGuest(0)_|  Gibt TRUE zurück, wenn die Person OpenOlat als Gast besucht.
 |  _hasAttribute("_ [AttrName] _","_ [string] _")_| Gibt TRUE zurück, wenn [string] dem Wert des AAI-Attributes [AttrName] der Person entspricht. Siehe auch [AAI - Generelle Informationen](http://www.switch.ch/aai/); AAI-Attribute; [Spezifikation der AAI-Attribute (pdf-Datei)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)
 |  _isInAttribute("_ [AttrName] _","_ [substring] _")_|  Gibt TRUE zurück, wenn [substring] einem Teil des Wertes des AAI-Attributs [AttrName] der Person entspricht.
 | _getUserProperty("_[userPropertyname]_")_| Gibt den Wert des spezifizierten Benutzerattributes zurück. Mit "=" kann dieser Wert mit einem fixen Wert verglichen werden.
 |  _getPassed("_ [integer] _")_|  Gibt vom Kursbaustein mit spezifizierter ID den Boolean TRUE (= Bestanden) oder FALSE (= Nicht bestanden) zurück
 |  _getScore("_ [integer] _")_|  Gibt vom Kursbaustein mit spezifizierter ID die Anzahl Punkte zurück
 |  _getMaxScore("_ [integer] _")_|  Gibt vom Kursbaustein mit spezifizierter ID die maximal erreichbare Anzahl Punkte zurück. Für Kursbausteine ohne konfigurierte Punktzahl gibt die Funktion 0 zurück. Für Kursbausteine mit konfigurierter Punktzahl, aber ohne Angabe einer Maximalpunktzahl, gibt die Funktion [positive Unendlichkeit](https://docs.oracle.com/javase/7/docs/api/java/lang/Double.html#POSITIVE_INFINITY) zurück.
 |  _getAttempts("_ [integer] _")_|  Gibt vom Kursbaustein mit spezifizierter ID die Anzahl abgeschlossener Versuche zurück. Kann auf Kursbausteine vom Typ _Test_ , _Selbsttest_ , _Fragebogen_ angewendet werden.
 |  _getLastAttemptDate("_ [integer] _")_|  Gibt vom Kursbaustein mit spezifizierter ID das Datum des letzten Versuchs zurück. Gilt für dieselben Kursbausteine wie getAttempts.
 |  _getInitialEnrollmentDate("_ [integer] _")_|  Gibt vom Kursbaustein _Einschreibung_ mit spezifizierter ID das Datum zurück, an dem sich die Person zum ersten Mal eingeschrieben hat.
 |  _getRecentEnrollmentDate("_ [integer] _")_|  Gibt vom Kursbaustein _Einschreibung_ mit spezifizierter ID das Datum zurück, an dem sich die Person zuletzt eingeschrieben hat.
 |  _getInitialCourseLaunchDate(0)_|  Gibt das Datum zurück, an dem die Person den Kurs zum ersten Mal geöffnet hat.
 |  _getRecentCourseLaunchDate(0)_|  Gibt das Datum zurück, an dem die Person den Kurs zuletzt geöffnet hat.
 | _getPassedWithCourseId("_ [integer-1] _","_ [integer-2] _")_|  Gibt vom Kursbaustein mit ID=[integer-2] des Kurses mit ID=[integer-1] den Boolean TRUE (=Bestanden) oder FALSE (=Nicht bestanden) zurück
 |  _getScoreWithCourseId("_ [integer-1] _","_ [integer-2] _")_| Gibt vom Kursbaustein mit ID=[integer-2] des Kurses mit ID=[integer-1] die Anzahl Punkte zurück
 | hasUserProperty("[ _userPropertyname]", "[string]")_ | Gibt TRUE zurück, wenn [string] dem Wert des Benutzerattributs [userPropertyname] der Person entspricht.
 | hasUserProperty("[ _userPropertyname]", "[string]" , " , ")_ | Gibt TRUE zurück, wenn [string] einem Wert im Multi-Value-Feld des Benutzerattributs [userPropertyname] der Person entspricht.
 | userPropertyStartswith(" [ _userPropertyname]", "[substring]")_|  Gibt TRUE zurück, wenn das Benutzerattribut [userPropertyname] der Person mit [substring] beginnt.
 | userPropertyEndswith(" [ _userPropertyname]", "[substring]")_| Gibt TRUE zurück, wenn das Benutzerattribut [userPropertyname] der Person mit [substring] endet.
 | isInUserProperty(" [ _userPropertyname]", "[substring]")_| Gibt TRUE zurück, wenn das Benutzerattribut [userPropertyname] der Person [substring] enthält.
 | isNotInUserProperty("[ _userPropertyname]", "[substring]")_|  Gibt TRUE zurück, wenn das Benutzerattribut [userPropertyname] der Person [substring] nicht enthält.
 | hasNotUserProperty("[ _userPropertyname]", "[string]")_|  Gibt TRUE zurück, wenn der Wert des Benutzerattributs [userPropertyname] der Person nicht [string] entspricht.
 | hasLanguage("de")| Gibt TRUE zurück, wenn die Person Deutsch als Systemsprache eingestellt hat. Für Englisch "de" durch "en" ersetzen.
 **Einheiten**|  _min_|  Minuten
 | _h_|  Stunden
 | _d_|  Tage
 | _w_|  Wochen
 | _m_|  Monate
 **Operatoren**|  =| gleich
 | >| grösser als
 | <| kleiner als
 | >=| grösser gleich
 | <=| kleiner gleich
 | *| Multiplikation
 | /| Division
 | +| Addition
 | -| Subtraktion
 **Booleans**|  &| Logisches UND
 | \| | Logisches ODER

### Benutzerattribute (UserProperty) {: #user_properties}

Mit Benutzerattributen schränken Sie den Zugang nach Angaben zur Person ein, zum Beispiel nach Name, Geschlecht, Adresse oder Studienfach. Die Attribute stammen in der Regel aus dem Benutzerprofil. OpenOlat führt für jedes Attribut einen festen Namen (siehe Tabelle unten). Diese Expertenregeln arbeiten mit Benutzerattributen:

  * getUserProperty _(" _[userPropertyname]_ ")_
  * hasUserProperty("[ _userPropertyname]", "[string]")_
  * userPropertyStartswith(" [ _userPropertyname]", "[substring]")_
  * userPropertyEndswith(" [ _userPropertyname]", "[substring]")_
  * isInUserProperty(" [ _userPropertyname]", "[substring]")_
  * isNotInUserProperty("[ _userPropertyname]", "[substring]")_
  * hasNotUserProperty("[ _userPropertyname]", "[string]")_

Enthält ein Attribut mehrere Werte (Multi-Value-Feld), geben Sie bei diesen Expertenregeln im dritten Parameter das Trennzeichen an:

  * hasUserProperty("[ _userPropertyname]", "[string]", " , ")_

  * hasNotUserProperty("[ _userPropertyname]", "[string]", " , ")_

### Verfügbare Benutzerattribute {: #available_user_properties}

Die folgende Tabelle zeigt die Benutzerattribute von OpenOlat. Eine Regel mit Benutzerattributen wirkt nur, wenn Ihre Instanz die Attribute verwendet und sie in den Profilen ausgefüllt sind. Welche Attribute Ihr Profil zeigt, sehen Sie im persönlichen Menü unter "Profil". Bei Fragen wenden Sie sich an die Systemadministrator:innen Ihrer Instanz.

Benutzerdaten| | Kontaktdaten|| Adressdaten ||
---|---|---|---|---|---
nickName| Benutzername| telPrivate| Telefon privat| street| Strasse
firstName| Vorname| telMobile| Telefon Mobil| extendedAddress| Adresszusatz
lastName| Nachname| telOffice| Telefon Geschäft| poBox| Postfach
email| E-Mail-Adresse| skype| Skype ID| zipCode| PLZ
creationDateDisplayProperty| Erstelldatum des Kontos| xing| Xing| region| Region / Kanton
lastloginDateDisplayProperty| Letzte Anmeldung| homepage| Homepage| city| Stadt
birthDay| Geburtsdatum|  || country| Land
gender| Geschlecht|  || countryCode| Länderkürzel
|
Organisation|| Berufliche Kontaktdaten|| Verschiedenes ||
institutionalName| Institution| department| Dienststelle / Firma| typeOfUser| Art von Konto
institutionalUserIdentifier| Institutionsnummer (Matrikelnummer)| officeStreet| Dienstadresse - Strasse| rank| Dienstgrad / Amtsbezeichnung
institutionalEmail| Institutions E-Mail| extendedOfficeAddress| Dienstadresszusatz| socialSecurityNumber| Sozialversicherungs-nummer
orgUnit| Organisationseinheit / Studiengruppe| officeZipCode| Dienst-Postleitzahl| degree| Akademischer Grad
studySubject| Studienfach| officeCity| Dienstadresse - Stadt| position| Funktion / Stellung
graduation| Abschlussjahr| officeCountry| Dienstadresse - Land| userInterests| Expertise
|| | officeMobilePhone| Dienstmobiltelefon|

### Beispiele und Verknüpfung von Expertenregeln {: #rule_examples}

Beispiele für die Anwendung "getUserProperty":

  * Nur Teilnehmende eines bestimmten Studienfachs sollen Zugang erhalten:

        getUserProperty("studySubject") = "Maschinenbau"

Zugang erhält nun, wer im Profil im Feld "Studienfach" den Wert "Maschinenbau" eingetragen hat.

  * Sollen nur Teilnehmende Zugang erhalten, die im Feld "Studienfach" nichts eingetragen haben, lautet die Regel:

        getUserProperty("studySubject") = ""

  * Sollen nur Teilnehmende Zugang erhalten, die im Feld "Studienfach" einen beliebigen Wert eingetragen haben, lautet die Regel:

        getUserProperty("studySubject") = "" = false

oder

        getUserProperty("studySubject") = "" = 0

Mehrere Regeln verknüpfen Sie mit Operatoren. Die beiden wichtigsten sind:

  * UND-Verknüpfung: &
  * ODER-Verknüpfung: |

Mischt eine Regel UND- und ODER-Verknüpfungen, setzen Sie Klammern. So legen Sie selbst fest, welche Verknüpfung zuerst gilt.

Beispiel: Die Expertenregel `(inLearningGroup("Teilnehmende Intensivkurs") | isCourseCoach(0))` gibt den Kursbaustein für die Mitglieder der Lerngruppe "Teilnehmende Intensivkurs" und für alle Betreuer:innen des Kurses frei.

Die folgenden Beispiele zeigen, wie Sie die Syntax einsetzen.

## Beispiele Expertenmodus

 **Beispiele für Expertenregeln in den Tabs «Sichtbarkeit», «Zugang» und «Punkte» (Struktur-Baustein)**

 **inLearningGroup("Anfänger") = 0**<br>
Alle Teilnehmenden ausser den Mitgliedern der Lerngruppe "Anfänger" sehen den Kursbaustein.

 **((now >= date("22.07.2018 12:00")) & (now <= date("23.12.2018 18:00"))) |
inLearningGroup("Betreuer")**<br>
Alle Teilnehmenden sehen den Kursbaustein zwischen dem 22.07.2018 und dem 23.12.2018, die Mitglieder der Lerngruppe "Betreuer" jederzeit.

 **((now >= date("03.09.2018 00:00")) & (now <= date("13.10.2018 00:00")) &
inRightGroup("Assessoren")) | isUser("schmidt")**<br>
Die Mitglieder der Rechtegruppe "Assessoren" sehen den Kursbaustein zwischen dem 03.09.2018 und dem 13.10.2018, die Person mit dem Benutzernamen "schmidt" jederzeit.

 **hasAttribute("swissEduPersonStudyBranch3","6200")**<br>
Ausschliesslich Studierende der Humanmedizin haben Zugriff auf den
Kursbaustein.<br>
Siehe auch:<br>
AAI-Attribute<br>
[Spezifikation der AAI-Attribute (pdf-Datei)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

 **hasAttribute("swissEduPersonHomeOrganization","[uzh.ch](http://uzh.ch/)")**<br>
Ausschliesslich Studierende der Universität Zürich haben Zugriff auf den
Kursbaustein.<br>
Siehe auch:<br>
AAI-Attribute<br>
[Spezifikation der AAI-Attribute (pdf-Datei)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

 **isInAttribute("surname","Mue")**<br>
Gibt TRUE zurück, wenn das Attribut _surname_ der Person die Buchstabenfolge "Mue" enthält, zum Beispiel beim Wert "Mueller" oder "Muehlebacher".<br>
Siehe auch:<br>
AAI-Attribute<br>
[Spezifikation der AAI-Attribute (pdf-Datei)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

**isInAttribute("eduPersonEntitlement","[http://vam.uzh.ch](http://vam.uzh.ch/)")**<br>
Gibt TRUE zurück, wenn das Attribut _eduPersonEntitlement_ der Person den Wert "[http://vam.uzh.ch](http://vam.uzh.ch/)" enthält, zum Beispiel auch beim Wert "<http://vam.uzh.ch/surgery>".<br>
Siehe auch:<br>
AAI-Attribute<br>
[Spezifikation der AAI-Attribute (pdf-Datei)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)

 **(getUserProperty("orgUnit") = "Sales")**<br>
Prüft, ob im Feld "Organisationseinheit / Studiengruppe" der Person der Wert "Sales" steht. Das lohnt sich zum Beispiel, wenn OpenOlat die Profildaten automatisch aus LDAP übernimmt.

**(getPassed("69742969114730") | getPassed("69742969115733") |
getPassed("69742969118009")) * 10**<br>
Sie tragen diese Regel im Tab "Punkte" des Kursbausteins "Struktur" unter "Punkte verarbeiten" ein. Der Kursbaustein "Struktur" zeigt 10 Punkte, wenn die Person einen der Tests (Kursbaustein-IDs "69742969114730", "69742969115733" oder "69742969118009") bestanden hat, sonst 0 Punkte.

**(getScore("69742969114730") + getScore("69742969115733") +
getScore("69742969118009")) >= 140 | getPassed("69978845384688")**<br>
Sie tragen diese Regel im Tab "Punkte" des Kursbausteins "Struktur" unter "Bestanden wenn" ein. Der Kursbaustein "Struktur" zeigt "Bestanden", wenn die Person in den drei Tests zusammen mindestens 140 Punkte erreicht oder wenn sie im Kursbaustein "Bewertung" (ID "69978845384688") von Hand die Bewertung "Bestanden" erhalten hat.

**getAttempts("70323786958847") > 0 **<br>
Gibt TRUE zurück, sobald die Person den Test mit der angegebenen ID einmal abgeschlossen hat, unabhängig von der Punktzahl.

**getLastAttemptDate("70323524635734") + 24h < now **<br>
Gibt TRUE zurück, wenn der letzte Testversuch mehr als 24 Stunden zurückliegt.

**getInitialEnrollmentDate("70323786958847") <= date("26.5.2018 18:00")**<br>
Gibt TRUE zurück, wenn sich die Person bis zum 26. Mai 2018, 18 Uhr, über den Kursbaustein "Einschreibung" mit der angegebenen ID zum ersten Mal in eine Gruppe eingeschrieben hat.

**getInitialEnrollmentDate("70323786958847") + 2h > now**<br>
Gibt in den ersten zwei Stunden TRUE zurück, nachdem sich die Person über den Kursbaustein "Einschreibung" mit der angegebenen ID in eine Gruppe eingeschrieben hat. So bearbeitet jede Person zum Beispiel ein Skript nur während einer festen Zeitspanne.

**(getInitialCourseLaunchDate(0) >= never) | (getInitialCourseLaunchDate(0) +
2h > now)**<br>
Gibt TRUE zurück, solange die Person den Kurs noch nicht geöffnet hat, und danach während zwei Stunden ab dem ersten Kursbesuch. So sieht jede Person den Inhalt nur während einer festen Zeitspanne.

**(getRecentCourseLaunchDate(0) + 10min < now) **<br>
Gibt TRUE zurück, wenn die Person den Kurs zuletzt vor mehr als 10 Minuten geöffnet hat.

**(getCourseBeginDate(0) <= today) & (getCourseEndDate(0) >= today)**<br>
Gibt TRUE zurück, wenn das heutige Datum zwischen Beginn und Ende des Durchführungszeitraums des Kurses liegt.

**isAssessmentMode(0)**<br>
Gibt TRUE zurück, solange für die Person im Kurs eine Prüfung läuft.

 **hasUserProperty("email","john.doe@[openolat.org](http://openolat.org/)")**<br>
Gibt TRUE zurück, wenn die Person in OpenOlat mit dieser E-Mail-Adresse registriert ist.

 **hasUserProperty("typeOfUser","staff", " , ")**<br>
Gibt TRUE zurück, wenn im Feld "Art von Konto" der Person unter anderem der Wert "staff" steht, zum Beispiel "staff, student".

 **userPropertyEndswith("email","@[openolat.org](http://openolat.org/)")**<br>
Gibt TRUE zurück, wenn die E-Mail-Adresse der Person auf _@[openolat.org](http://openolat.org/)_ endet.

 **isInUserProperty("email","doe@openo")**<br>
Gibt TRUE zurück, wenn die E-Mail-Adresse der Person den Text _doe@openo_ enthält.

 **isNotInUserProperty("email","doe@openo")**<br>
Gibt FALSE zurück, wenn die E-Mail-Adresse der Person den Text _doe@openo_ enthält.

!!! warning "Achtung"

    Die Kursbaustein-IDs oben sind Beispiele. In Ihrem Kurs verwenden Sie die ID, die der Tab "Titel und Beschreibung" des jeweiligen Kursbausteins anzeigt.

## Einsatz von AAI-Attributen

Arbeiten Sie an einer Schweizer Hochschule oder an einer anderen Institution mit Zugang zu einer AAI-Infrastruktur, setzen Sie mit AAI-Attributen Zugriffsregeln im Kurs. So öffnen nur Teilnehmende mit bestimmten Attributen das Kursmaterial, zum Beispiel nur Angehörige einer bestimmten Institution. AAI steht für "Authentication and Authorization Infrastructure": Angehörige einer Hochschule melden sich damit mit einem einzigen Benutzernamen und Passwort bei den Systemen aller teilnehmenden Hochschulen an. Weitere Informationen zu AAI finden Sie zum Beispiel bei [Switch](http://www.switch.ch/de/aai/ "Switch") oder beim [Deutschen Forschungsnetz](https://www.aai.dfn.de/ "Deutsches Forschungsnetz").

Welche Attribute und Werte es gibt, beschreiben die AAI Attribute Specification bei [Switch](https://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf "Switch") (Dokument in englischer Sprache) und [DFN-AAI](https://www.aai.dfn.de/der-dienst/attribute/ "DFN-AAI"). Die folgende Tabelle zeigt zwei Attribute, die Schweizer Hochschulen häufig verwenden, mit passenden Expertenregeln:

Attribut| Beschreibung| Beispiel Expertenregel und Erklärung
---|---|---
swissEduPersonHomeOrganization| Universität oder Heimorganisation| hasAttribute ("swissEduPersonHomeOrganization", "[uzh.ch](http://uzh.ch)"): Nur Angehörige der Universität Zürich sind zugelassen.
swissEduPersonStudyBranch3| Studienrichtung 3. Klassifikation| hasAttribute ("swissEduPersonStudyBranch3","6400"): Nur Studierende der Studienrichtung Veterinärmedizin sind zugelassen.

### Anwendung

Sie können AAI-Attribute mit der Syntax

 ** _hasAttribute("_ [AttrName] _","_ [string] _")_**  oder<br>
 ** _isInAttribute("_ [AttrName] _","_ [substring] _")_**  abfragen.

Dabei gilt folgendes:

* **[AttrName]** ist der Name des Attributs. Sie finden ihn in der Tabelle unten und in der Spezifikation der AAI-Attribute (PDF-Datei) auf Seite 5, Spalte _LDAP Namen_.
* **[string]** ist der Wert des AAI-Attributs mit dem Namen [AttrName].
* **[substring]** ist ein beliebiger Teil von [string].

#### AAI Beispiel

_Abfragen für Hans Muster_

Attribut [AttrName]| Beispiel Wert [string]| Beschreibung
---|---|---
swissEduPersonUniqueID| [845938727494@uzh.ch](mailto:845938727494@uzh.ch)| Eindeutige persönliche Identifikationsnummer
surname| Muster| Nachname
givenName| Hans| Vorname
mail| [hans.muster@uzh.ch](mailto:hans.muster@uzh.ch)| Bevorzugte E-Mail-Adresse
swissEduPersonHomeOrganization| [uzh.ch](http://uzh.ch/)|Heimorganisation/Universität
swissEduPersonHomeOrganizationType| university| Art der Heimorganisation
eduPersonAffiliation| student| Funktion innerhalb der Heimorganisation
[swissEduPersonStudyBranch1](http://www.switch.ch/aai/support/documents/attributes/studybranch.html)| 4| Studienrichtung 1. Klassifikation
[swissEduPersonStudyBranch2](http://www.switch.ch/aai/support/documents/attributes/studybranch.html)| 42 (=Naturwissenschaften)| Studienrichtung 2. Klassifikation
[swissEduPersonStudyBranch3](http://www.switch.ch/aai/support/documents/attributes/studybranch.html)| 4600 (=Chemie)| Studienrichtung 3. Klassifikation
swissEduPersonStudyLevel| 15| Beschreibung des Studien-Fortschrittes
eduPersonEntitlement| <http://vam.uzh.ch/surgery>| Zugriffsrecht auf Ressource
employeeNumber| 01-234-567| Matrikelnummer (nur für Studierende der Universität Zürich)
organizationalUnit| 1| Einheit der Heimorganisation z.B. Fakultät (nur für Mitarbeiter)

Für Hans Muster liefern die folgenden Abfragen diese Ergebnisse:

Abfrage | Output
---|---
isInAttribute("surname","ust")|  **true**
hasAttribute("swissEduPersonStudyBranch3","4600")|  **true**
hasAttribute("swissEduPersonStudyBranch3","1200")|  **false**
isInAttribute("eduPersonEntitlement","<http://vam.uzh.ch>")|  **true**
isInAttribute("eduPersonEntitlement","<http://vam.uzh.ch/ophthalmology>")| **false**
hasAttribute("employeeNumber","01-234-567")|  **true**

Die Liste der möglichen Werte steht im Anhang der [Spezifikation der AAI-Attribute (PDF-Datei)](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf) ab Seite 20.

Für weitere Informationen zu Werten oder zur Anwendung von AAI-Attributen wenden Sie sich in der Schweiz an [Switch](http://www.switch.ch/de/aai/ "Switch"), und in Deutschland an das [Deutsche Forschungsnetz](https://www.aai.dfn.de/ "Deutsche Forschungsnetz").

!!! tip "Tipp"

    Verwenden Sie AAI-Attribute nur, wenn sich alle Teilnehmenden Ihres Kurses über AAI anmelden. Bei Personen ohne AAI-Anmeldung fehlen die Attribute, und die Regel wirkt nicht wie geplant.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Lernpfadkurs - Überblick >](Learning_path_course.de.md)<br>
[Spezifikation der AAI-Attribute (PDF) >](http://www.switch.ch/aai/docs/AAI_Attr_Specs.pdf)<br>
[Switch AAI >](http://www.switch.ch/de/aai/)<br>
[Deutsches Forschungsnetz (DFN-AAI) >](https://www.aai.dfn.de/der-dienst/attribute/)

**Weiterführend**<br>
[Kursbausteine im Kurseditor >](General_Configuration_of_Course_Elements.de.md)<br>
[Kursbausteine im Überblick >](Course_Elements.de.md)

[Zum Seitenanfang ^](#zugriffsbeschrankungen-im-expertenmodus)
