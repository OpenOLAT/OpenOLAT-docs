# Kurseinstellungen - Tab Bewertung:<br>Zertifikate und Rezertifizierung {: #certificate_and_recertification}

Die Konfiguration eines Zertifikates für einen Kurs erfolgt in den Einstellungen des Kurses im Tab "Bewertung".

![course_settings_assessment_certification_config_v1_de.png](assets/course_settings_assessment_certification_config_v1_de.png){ class="lightbox" }


## Zertifikate {: #certificate}

### Was ist ein Zertifikat? {: #certificate_description}

Als Bestätigung für den Besuch eines Kurses bzw. der Erreichung von bestimmten kursbezogenen Aktivitäten kann ein **PDF-Zertifikat** ausgestellt werden. Es ist auch möglich, ohne die Verwendung eines Leistungsnachweises ein Zertifikat auszustellen.

Neben diesen Kurszertifikaten kann mit dem Zertifikatsprogramm auch ein Zertifikat für den Besuch mehrerer Kurse ausgestellt werden. Solche Zertifikate werden innerhalb des Course Planners (Durchführung) vergeben.<br>
[Mehr zum Zertifizierungsprogramm >](../../manual_user/area_modules/Course_Planner_Certification_Programs.de.md) 

**Die nachfolgenden Ausführungen beziehen sich auf das Zertifikat in einem einzelnen Kurs.**


### Von wem wird ein Zertifikat ausgestellt? {: #certificate_issuer}

Als Autor:in wählen Sie aus, ob das Zertifikat **manuell** von Betreuer:innen ausgestellt wird, und/oder **automatisch** nach Bestehen des Kurses.

Die Auswahl "manuell" gestattet die Verwendung von Zertifikaten auch in Kursen ohne bewertbare Kurselemente. Wenn das Zertifikat manuell ausgestellt werden soll, kann der/die Betreuer:in dies **im Bewertungswerkzeug** in der Leistungsübersicht der einzelnen Benutzer:innen vornehmen.

### Wo sind die Zertifikate einsehbar? {: #certificate_view}

Sobald der/die Teilnehmende alle Bedingungen für einen bestandenen Kurs erfüllt hat, ist das Zertifikat in der **Toolbar des jeweiligen Kurses** unter "Mein Kurs" im Leistungsnachweis verfügbar. Die Benutzer:innen erhalten ausserdem automatisch eine **E-Mail-Benachrichtigung**, sobald ein Zertifikat ausgestellt worden ist.

### Wie wird die Gültigkeit überprüft? {: #certificate_validation}

Für das Zertifikat kann eine **Gültigkeitsdauer** festgelegt werden. Sie legen dabei die Gültigkeitsdauer in Tagen, Wochen, Monaten oder Jahren fest. 

Um die Gültigkeit des Zertifikats zu überprüfen, muss der Vorlage das Attribut "certificateVerificationUrl" hinzugefügt werden. Dieses erlaubt es, **mittels QR-Code** das Zertifikat zu einem späteren Zeitpunkt nochmals zu generieren und mit der vorliegenden Version zu vergleichen. Sofern beide Versionen übereinstimmen, kann das Zertifikat als gültig erklärt werden. Der QR-Code zur Validierung ist allerdings nur bei Verwendung eines HTML-Formulars möglich.

### Was geschieht beim Ablauf eines Zertifikats? {: #certificate_expiry}

Anhand des Ausstellungsdatums sowie des Ablaufdatums des Zertifikats können [Erinnerungen](../learningresources/Course_Reminders.de.md) ausgelöst werden. Z.B. können Kursteilnehmer:innen eine Info erhalten, dass das Zertifikat abgelaufen ist oder in wenigen Tagen abläuft oder eine **Rezertifizierung** ab sofort möglich ist.


### Zertifikatsvorlage erstellen {: #certificate_template}

Als Vorlage für das Zertifikat dient in der Regel eine systemweite, vom Administrator festgelegte PDF-Vorlage. Wenn Sie eine eigene Vorlage verwenden möchten, können Sie diese im Kurs unter **Administration > Einstellungen > Bewertung > Abschnitt "Zertifikat" > Zertifikatvorlage** hochladen.

!!! hint "Hinweis"

    Wenn Sie den Button "**Vorschau**" verwenden, wird Ihnen immer nur ein Dummy angezeigt.
    In einer Vorschau werden grundsätzlich nur Dummy-Daten verwendet und keine echten Werte aus der Datenbank. Es steht z.B. überall das aktuelle Datum. Es soll gar nicht der Eindruck entstehen, dass das ein echtes Zertifikat sein könnte. Eine Vorschau muss absichtlich und offensichtlich falsch sein.

Eine PDF-Vorlage ist keine gewöhnliche PDF-Datei, sondern muss mit HTML erzeugt werden, um Layout und Variablen zu gewährleisten.

Mit diesem [Zertifikatsbot](https://tools.vcrp.de/zertifikatsbot/){:target="_blank”} können einfach und schnell Zertifikatsvorlagen im HTML-Format erstellt werden. Wer den Bot an seine Bedürfnisse anpassen möchte, dem steht das [Repository](https://gitlab.vcrp.de/openolat/zertifikatsbot){:target="_blank”} mit dem öffentlich geschalteten Code (MIT Lizenz) zur Verfügung.

Die Formularfelder müssen bestimmte Variablen enthalten, die vom System später durch die spezifischen Daten ersetzt werden. Es können alle Attribute als Variablen verwendet werden. Bei PDF-Vorlagen werden die Variablennamen ohne $-Präfix, bei HTML-Formularen mit $-Präfix verwendet.

Zum Formatieren von Datumsformaten steht das "dateFormatter"-Objekt zur Verfügung. Damit lassen sich die "*Raw" formate mittels "formatDate()" formatieren oder mit formatDateRelative (Date baseLineDate, days, months, years) eine angegebene Periode addieren.

Unterschriften, Logos o.ä. können über die optionalen Variablen als statische Grafiken in das Zertifikat integriert werden. Die entsprechenden Dateien müssen dafür mit der Zertifikatsvorlage zur Verfügung stehen.

???+ note "Übersicht der wichtigsten Variablen:"

    _Benutzer:_

      * $fullName
      * $firstName
      * $lastName
      * $birthDay
      * $institutionalName
      * $orgUnit
      * $studySubject
      * ...

        Sämtliche Userattribute sind als Variable verfügbar.

    _Kurs:_

      * $title
      * $externalReference
      * $authors
      * $from (date)
      * $fromLong (date)
      * $location
      * $to (date)
      * $toLong (date)
      * $expenditureOfWork
      * $mainLanguage

    _Daten zur Leistung (alle Kurstypen):_

      * $score
      * $status
      * $grade
      * $gradeLabel
      * $gradeCutValue

    _Daten zur Leistung (nur Lernpfadkurs):_

      * $maxScore
      * $progress

    _Daten zum Zertifikat:_

      * $dateFirstCertification
      * $dateFirstCertificationLong
      * $dateFirstCertificationRaw
      * $dateCertification
      * $dateCertificationLong
      * $dateCertificationRaw
      * $dateNextRecertification
      * $dateNextRecertificationLong
      * $dateNextRecertificationRaw  

      * $certificateVerificationUrl

    _Relatives Datum:_

      Auf dem Zertifikat können Daten angegeben werden, die relativ zu einem Raw-Datum berechnet werden:

      Methode und Parameter | Beispiel: $dateNextRecertificationRaw = 15.11.2021 
      ---------|----------
      *Relatives Datum kurz* | *Output: 22.09.2031*
      $formatter.formatDateRelative(Originaldatum, "Sprachcode", +/- Tage, +/-  Monate, +/- Jahre) | $formatter.formatDateRelative($dateNextRecertificationRaw, "de", 7, -2, 10)
      *Relatives Datum lang* | *Output: 22. September 2031*
      $formatter.formatDateLongRelative(Originaldatum, "Sprachcode", +/- Tage, +/- Monate, +/- Jahre) | $formatter.formatDateRelative($dateNextRecertificationRaw, "de", 7, -2, 10)
     
    _Daten aus der Kursbeschreibung:_

      * $!description  
      * $!objectives  
      * $!requirements  
      * $!credits

    _Optionale Variablen:_

      * $custom1
      * $custom2
      * $custom3

Sollten Sie eine Zertifikatvorlage wünschen, kontaktieren Sie uns unter [support@frentix.com](mailto:support@frentix.com) für einen Kostenvoranschlag für eine Vorlage gemäss Ihren individuellen Wünschen.

[Zum Seitenanfang ^](#certificate_and_recertification})

---


## Rezertifizierung {: #recertification}

### Voraussetzungen {: #recertification_conditions}

Damit ein Prozess zur Rezertifizierung eingerichtet werden kann, muss vorher die Zertifikatserstellung aktiviert worden sein. Ist ein Zertifikat für einen Kurs abgelaufen, kann allen betroffenen Teilnehmer:innen die Rezertifizierung angeboten werden.

Die Option zur Rezertifizierung ist gekoppelt an

* eine bestehende frühere (Erst-)Zertifizierung
* eine definierte Angabe, ab wann frühestens eine Rezertifizierung möglich ist.

![course_settings_assessment_recertification_v2_de.png](assets/course_settings_assessment_recertification_v2_de.png){ class="shadow lightbox" }


### Rezertifizierung aktivieren  {: #recertification_activation}

Wird die Rezertifizeriung aktiviert, muss eine Angabe gemacht werden, ab wann eine Rezertifizierung möglich sein soll: "frühestens ab ... Tage vor Ablauf Gültigkeit Zertifikat".

(Der Wert muss kleiner als die Gültigkeitsdauer sein.)

Beachten Sie, dass Sie Kursbausteine auch nur bei der ersten Zertifizierung oder nur bei einer der Rezertifizierungen anzeigen können. Dies kann in Lernpfadkursen über Ausnahmen bestimmt werden. [Mehr dazu >](../learningresources/Learning_path_course_Course_editor.de.md#exceptions)


### Erinnerungen einrichten  {: #recertification_reminders}

Bevor die Rezertifizierung endgültig aktiviert wird, werden Sie zur Einrichtung von Erinnerungen aufgefordert. Definieren Sie automatisch verschickte Meldungen an betroffene Teilnehmer:innen, z.B. sobald ihre Rezertifizierung möglich wird und/oder wenn die Gültigkeit des bisherigen Zertifikats abgelaufen ist.

Die Daten der teilnehmenden Personen werden bei der Rezertifizierung zurückgesetzt (Kurs-Reset).

Leistungsnachweise und Zertifikate früherer Durchgänge bleiben erhalten.

[Zum Seitenanfang ^](#certificate_and_recertification})

---


## Weitere Informationen {: #further_information}

[Zertifizierungsprogramm (Zertifikat für mehrere Kurse) >](../../manual_user/area_modules/Course_Planner_Certification_Programs.de.md)

[Zum Seitenanfang ^](#certificate_and_recertification})