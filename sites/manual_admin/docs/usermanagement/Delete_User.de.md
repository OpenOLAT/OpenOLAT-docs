# Benutzer:in löschen {: #delete_user}


!!! warning "Attention"

    This article is still under construction.



## Was geschieht beim Löschen eines Kontos?

Wird das Konto eines/einer Benutzer:in gelöscht, ist diese Person in Zukunft nicht mehr als registriert in OpenOlat bekannt und auffindbar.

Für die **Arbeitsergebnisse** dieser Person gelten beim Löschen ihres Kontos eigene Regeln. Siehe unten: [Was wird gelöscht?](#del_properties)


## Wer darf Konten von Benutzer:innen löschen?

Um ein Konto zu löschen, muss ein Zugriff auf die Benutzerverwaltung möglich sein. Diesen Zugriff besitzen die Rollen

* Benutzerverwalter:in
* Administrator:in
* Systemadministrator:in (kein direkter Zugriff auf Benutzerverwaltung, kann jedoch via Konten-Lebenzyklus Löschvorgänge auslösen)

[Zum Seitenanfang ^](#delete_user)

---


## Variante 1 {: #delete_user_var1}

**Schritt 1:**<br>
Suchen Sie in der Benutzerverwaltung mit der Kontensuche die Benutzer:innen, deren Konten gelöscht werden sollen.

**Schritt 2:**<br>
Markieren Sie im Suchergebnis die zu löschenden Benutzer:innen in der Checkbox am Anfang der Zeile. Sobald mindestens 1 Person markiert ist, erscheint u.a. der Button "Konto löschen" über der Liste.

![delete_user_var1_step2_v1_de.png](assets/delete_user_var1_step2_v1_de.png){ class="shadow lightbox" }

**Schritt 3:**<br>
Nach Klick auf diesen Button erscheint nochmals eine Sicherheitsabfrage, die Sie bestätigen müssen.

![delete_user_var1_step3_v1_de.png](assets/delete_user_var1_step3_v1_de.png){ class="shadow lightbox" } 

[Zum Seitenanfang ^](#delete_user)

---

## Variante 2: mit Suche nach Konten ohne Aktivität / dekaktivierten Konten {: #delete_user_var2}

**Schritt 1:**<br>
Auch über den Link "Konten löschen" können Benutzer:innen ausgewählt und deren OpenOlat-Konten gelöscht werden.

![delete_user_var2_step1_v1_de.png](assets/delete_user_var2_step1_v1_de.png){ class="shadow lightbox" }

**Schritt 2:**<br>
Hier finden Sie zunächst die potenziellen Kanditat:innen für eine Löschung in 3 Tabs vorsortiert (dem Lebenszyklus-Mangement entsprechend). Sie finden so schneller alle Benutzer:innen ohne Aktivität oder bereits deaktivierte Benutzer:innen.

**Tab "Konten ohne Aktivität":** Hier werden alle Benutzer:innen angezeigt, die über einen bestimmten Zeitraum nicht mehr in OpenOlat aktiv waren. Der Zeitraum, der zu einer Auflistung hier führt, kann von Administrator:innen festgelegt werden. 

**Tab "Deaktivierte Konten":** Hier werden alle Benutzer:innen angezeigt, deren Konto bereits automatisch oder manuell deaktiviert wurden. Sie können sich auch Konten anzeigen lassen, deren Inaktivierung in einer bestimmten Zeit ansteht.

**Tab "Bereit zu löschen":** tbd

![delete_user_var2_step2_v1_de.png](assets/delete_user_var2_step2_v1_de.png){ class="shadow lightbox" }

**Schritt 3:**<br>
Markieren Sie die zu löschenden Benutzer:innen in der Checkbox am Anfang der Zeile. Sobald mindestens 1 Person markiert ist, erscheint u.a. der Button "Konto löschen" über der Liste.

![delete_user_var2_step3_v1_de.png](assets/delete_user_var2_step3_v1_de.png){ class="shadow lightbox" }

**Schritt 4:**<br>
Nach Klick auf diesen Button erscheint nochmals eine Sicherheitsabfrage, die Sie bestätigen müssen.

[Zum Seitenanfang ^](#delete_user)

---

## Variante 3: Automatisches Löschen {: #delete_user_var3}

Das Löschen von Benutzer:innen kann auch vollautomatisch durch einen aktivierten Benutzer-Lifecycle erfolgen.

[Details zum Benutzer-Lifecycle >](../../manual_admin/administration/Life_cycles_-_Administration.de.md#lifecycle_accounts)<br>
[Wie manage ich Lebenszyklen von Gruppen, Kursen oder Benutzerkonten? >](../../manual_how-to/lifecycle/lifecycle.de.md#benutzerkonten-lifecycle)

[Zum Seitenanfang ^](#delete_user)

---

!!! warning "Attention"

    This article is still under construction.



## Was wird gelöscht? {: #del_properties}

Wird ein/eine Benutzer:in gelöscht,

* sollen manche Information unwiederbringlich gelöscht werden (z.B. Telefonnummer)
* können/sollen manche Informationen ohne Namen erhalten bleiben (z.B. Forumsbeitrag, ohne den ein Diskussionstrang seinen Sinn verlieren würde)
* müssen manche Informationen erhalten bleiben (z.B. Rechnungsadresse -> Aufbewahrungspflicht) 

Dabei muss berücksichtigt werden, dass Informationen programmtechnisch an unterschiedliche Objekte angebunden sind:

:octicons-person-24: = Information ist direkt an die **Person** gebunden<br>
:octicons-package-24: = Information wird zusammen mit einem **Kurs/einer Gruppe/o.a.** gespeichert<br>
:octicons-infinity-24: = Information wird im **OpenOlat-System** gespeichert

|Information|Was geschieht damit?| 
|---| ---------------------------------------- |
|Benutzerverwaltung > **Profil** :octicons-person-24: |**Gelöscht werden:** Anmeldename, Vorname, Nachname, E-Mail, E-Mail-Signatur, Geburtsdatum, Geschlecht, Telefon Privat, Telefon Mobil, Telefon Geschäft, Skype ID, XING Profilname, ICQ, Homepage, Strasse, Adresszusatz, Postfach, Postleitzahl, Region/Kanton, Stadt, Land, Institution, Institutionsnummer (Matrikelnummer), Institutions-E-Mail, Organisationseinheit, Studiengruppe, Studienfach, Persönlicher Text "Über mich", persönliches Profilbild  **Ausnahmen:** Von Personen mit administrativen Berechtigungen bleiben Name und Vorname erhalten um Aktionen weiter nachvollziehen zu können.|
|Benutzerverwaltung > **Visitenkarte** :octicons-person-24:|Alle Angaben auf der Visitenkarte werden aus dem Profil übernommen, deshalb stehen sie nach dem Löschen des Profils auch nicht mehr für die Visitenkarte zur Verfügung. Die Visitenkarte des/der Benutzer:in wird nicht mehr in OpenOlat (z. B. im Forum oder bei Kommentaren) angezeigt.|
|Benutzerverwaltung > **Systemeinstellungen** :octicons-person-24: | Es werden alle Systemeinstellungen gelöscht: Allgemeine Systemeinstellungen (z.B. die Sprache), spezielle Systemeinstellungen (z.B die Startseite) und persönliche Werkzeuge.|
|Benutzerverwaltung > **Konto** :octicons-person-24:| Kontotyp, Erstellungsdatum des Kontos, Letzter Login und Kontoablauf werden gelöscht. Das Konto wird auf den Status "gelöscht" gesetzt. |
|**Rollen** :octicons-person-24: :octicons-package-24: | Die in der Benutzerverwaltung zugeteilten Rollen und Berechtigungen werden gelöscht. |
|Benutzerverwaltung > **Passwort** :octicons-person-24: | Das Passwort gelöschter Benutzer:innen wird unwiderbringlich gelöscht.|
|Benutzerverwaltung > **Authentifizierungen** :octicons-person-24: | Alle Authentifizierungsmöglichkeiten werden gelöscht.|
|Benutzerverwaltung > **Properties** :octicons-person-24: | Properties werden komplett gelöscht.|
|Benutzerverwaltung > **GUI-Einstellungen** :octicons-person-24: | Die GUI-Einstellungen werden komplett gelöscht.|
|**Buchungsaufträge** :octicons-person-24: :octicons-package-24: :octicons-infinity-24: |Sind Buchungsaufträge vorhanden, werden beim Löschen von Benutzer:innen deren Namen in ihren Buchungsaufträgen entfernt, die Buchungsaufträge selbst bleiben jedoch erhalten. **Ausnahme:** ??Buchungsaufträge vom Typ "Rechnung" bleiben ohne Namen erhalten.|
|**Rechnungsadresse** :octicons-person-24: :octicons-package-24: :octicons-infinity-24: |Um Zahlungen nachvollziehen zu können (z.B. für Steuerbehörden), bleiben die Rechnungsadressen erhalten.|
|**Nachteilsausgleich** :octicons-person-24: | tbd |
|**Abonnements** :octicons-person-24: | Abonnemente werden alle gelöscht.|
|**Beziehungen** :octicons-person-24: | tbd|
|**Zugehörigkeit zu Organisationen** :octicons-person-24: | tbd |
|**Quota** :octicons-person-24: | tbd |
|**Lektionen** :octicons-person-24: | Die Teilnahme an Lektionen/Absenzen werden gelöscht.|
|**Kompetenzen** :octicons-person-24: | Kompetenzen werden gelöscht.|
|Benutzerverwaltung > **Curriculum** :octicons-person-24: | tbd |
|**Persönlicher Kalender** :octicons-person-24: | Der persönliche Kalender wird gelöscht|
|**Chatverlauf** :octicons-person-24: | Chats (Nachrichten, Einstellungen) werden anonymisiert.|
|**Persönlicher Ordner** :octicons-person-24: |Der persönliche Ordner wird gelöscht|
|**Portfolio** :octicons-person-24: | In einem ePortfolio erstellte Mappen, Bereiche und Einträge werden gelöscht. Wenn Mappen an andere Benutzer:innen frei gegeben wurden, sind sie auch dort nicht mehr abrufbar.|
|**persönliche To-dos** :octicons-person-24: | tbd (To-dos in Projekten: siehe unten) |
|**Mailbox** :octicons-person-24: |Mails, die in der Mailbox des persönlichen Menüs aufgeführt sind, werden gelöscht. (Die interne E-Mail-Box wird komplett gelöscht.)|
|**Empfänger:in einer Erinnerungsmail** :octicons-package-24: |War der/die gelöschte Benutzer:in potenzieller/potenzielle Empfänger:in einer Erinnerungsmail, wird die Mail nicht mehr an die gelöschte Person geschickt. (Die Empfängerliste wird zum Zeitpunkt der Prüfung der Regeln erstellt, deshalb erscheint eine gelöschte Person gar nicht mehr auf der Versandliste.)|
|**Mitgliedschaft in Gruppen** :octicons-person-24: :octicons-package-24: | Die Mitgliedschaften in Gruppen werden gelöscht. (Die Gruppen selbst werden nicht gelöscht, auch wenn sie von dem/der gelöschten Benutzer:in erstellt wurden und er/sie einziges Mitglied ist. Es wird dann lediglich die gelöschte Benutzer:in als Gruppenmitglied entfernt. Wenn die gelöschte Benutzer:in der/die einzige Gruppenbetreuer:in war, wird ersatzweise der/die Administrator:in als Gruppenbetreuer:in eingetragen. In der Regel werden Gruppen ohne Mitglieder dann aber zu einem späteren Zeitpunkt durch den Group-Life-Cycle-Prozess gelöscht.)|
|**Mitgliedschaft in Projekten** :octicons-person-24: :octicons-package-24: |Die Mitgliedschaft in Projekten wird gelöscht und die Person ist nicht mehr in der Liste der Projektmitglieder zu finden. (Von dem/der gelöschten Benutzer:in in einem Projekt erstellte To-dos bleiben jedoch erhalten.)|
|**To-dos in Projekten** :octicons-person-24: |In Projekten bleiben die To-dos eines/einer gelöschten Benutzer:in erhalten, sind dann allerdings niemandem mehr zugewiesen. Auch bereits erledigte To-dos bleiben erhalten (ohne Angabe des/der Benutzer:in, die dieses To-do zu erledigen hatte). Der Ablauf von Projekten bleibt so weiter ersichtlich. Unerledigte To-dos müssen aber neu zugeordnet werden.|
|**Mitgliedschaft in Kursen** :octicons-person-24: | Kursmitgliedschaften werden gelöscht, auch wenn die Rolle in diesem Kurs "Besitzer:in" und "Betreuer:in" war. Wenn der/die gelöschte Benutzer:in Ersteller:in und einziger Besitzer/einzige Besitzer:in war, wird ersatzweise ein/eine Administrator:in als Besitzer:in des Kurses eingetragen.|
|**Daten im Kursbaustein Aufgabe** :octicons-person-24: :octicons-package-24: |Innerhalb einer Aufgabe von der gelöschten Person erstellte und hochgeladene Dokumente werden gelöscht (z.B. draw.io, Word,Excel, ppt).|
|**Daten des Peer Reviews im Kursbaustein Aufgabe** :octicons-person-24: :octicons-package-24: | tbd |
|**Daten im Kursbaustein Teilnehmerordner** :octicons-person-24: :octicons-package-24: | tbd |
|**Daten im Kursbaustein Forum** :octicons-person-24: :octicons-package-24: |Persönliche Forum-Posts und -Kommentare werden nach der Löschung des Nutzers anonymisiert und mit "unknown user" ausgewiesen.|
|**Daten im Kursbaustein BBB** :octicons-person-24: :octicons-package-24: |Sind Teilnehmer:innen in BBB-Meetings werden sie gelöscht.|
|**Daten im Kursbaustein Adobe Connect** :octicons-person-24: :octicons-package-24: |Alle von OpenOlat im Hintergrund gespeicherte Daten werden gelöscht.|
|**Daten im Kursbaustein Vitero** :octicons-person-24: :octicons-package-24: |Alle von OpenOlat im Hintergrund gespeicherte Daten werden gelöscht.|
|**Office for the web** :octicons-person-24: :octicons-package-24: |Alle von OpenOlat im Hintergrund gespeicherte Daten werden gelöscht.|
|**Testresultate** :octicons-person-24: | tbd |
|**Leistungsnachweise** :octicons-person-24: | tbd |
|**Zertifikate** :octicons-person-24: | Mit QR Code versehene Zertifikate (mit Variable "certificateVerificationUrl") werden nicht gelöscht, damit per URL im Host based verification Verfahren ein Zertifikat weiterhin noch bestätigt werden kann. Im Bewertungswerkzeug des/der Kursbetreuer:in sind die Zertifkate jedoch nicht mehr gelistet. Es ist sinnvoll, die zu löschenden Benutzer:innen vorher darauf hinzuweisen, dass sie im persönlichen Menü ihre erworbenen Zertifikate vor dem Löschen ihres Accounts noch herunterladen. (tbd: Unterschied Zertifikate mit/ohne QR?|
|**extern erworbene Zertifikate** :octicons-person-24: |OpenOlat-Benutzer:innen können auch extern erworbene Zertifikate in OpenOlat hochladen, um ihr Profil zu vervollständigen. Diese extern erworbenen Zertifikate werden mit der Auflösung eines OpenOlat-Kontos ... tbd|
|Benutzerverwaltung > **Badges** :octicons-person-24: | Badges bleiben bestehen, damit die Echtheit bestätigt werden kann (Host based verification, Signed verificsation). Es ist dennoch sinnvoll, die zu löschenden Benutzer:innen vorher darauf hinzuweisen, dass sie im persönlichen Menü ihre erworbenen Badges herunterladen. Wurden **Globale Badges** vergeben, wird in der Liste der vergebenen globalen Badges (durch Administrator:innen abrufbar unter Administration > e-Assessment > OpenBadges > Tab "Vergebene globale Badges") an Stelle des Namens des Empfängers/der Empfängerin nur noch "unknown user" angezeigt. Es bleibt so noch ersichtlich, wann und durch wen ein globaler Badge einmal vergeben wurde. Auch wenn durch Klick auf "Widerrufen" der Badge entzogen wird, bleibt er als Listeneintrag mit dem Status "Widerrufen" in der Liste der vergebenen globalen Badges erhalten. |
|**Rolle Besitzer:in in Lernressourcen und Kurse** :octicons-package-24: | Lernressourcen und Kurse werden nicht gelöscht, wenn deren Besitzer:in gelöscht wird. Unabhängig davon, ob die Lernressource publiziert oder mit anderen Autoren geteilt oder nirgends referenziert/verwendet wurde. Wenn die gelöschte Benutzer:in der/die einzige Besitzer:in war, wird ersatzweise der/die Administrator:in als Besitzer:in eingetragen. Dies gilt auch für Test-Lernressourcen.|
|**im Fragenpool enthaltene Fragen** :octicons-person-24: :octicons-package-24:| tbd |
|**im Media Center erstellte Elemente** :octicons-person-24: :octicons-package-24: | tbd |
|**externe Korrektor:innen** :octicons-package-24:| Werden Konten externer Korrektor:innen gelöscht, so werden diese in den Listen nicht mehr namentlich aufgeführt. Die Korrekturaufträge bleiben jedoch erhalten.|
|**Korrekturaufträge** :octicons-person-24: :octicons-package-24: | Werden Benutzer:innen gelöscht, die Korrekturaufträge als externer/externe Korrektor:in hatten, so gelten folgende Regeln:  1) **Bereits erledigte Korrekturaufträge** erscheinen entsprechend zugeordnet im Bewertungswerkzeug des/der Kursbesitzer:in.  2) **Noch nicht erledigte Korrekturaufträge** erscheinen auf der Liste "Offene Bewertungen" im Bewertungswerkzeug des/der Kursbesitzer:in.  3) Die Kursbesitzer:innen können nach Anwahl des betreffenden Test-Kursbausteins und eines Teilnehmers/einer Teilnehmerin im **Änderungsverlauf** (Link am unteren Rand des Screens) nachsehen, wer eine Korrektur vorgenommen hat. Es sind dort auch die Namen inzwischen gelöschter Benutzer:innen noch ersichtlich.|
|**Statistiken** :octicons-infinity-24: |Gelöschte Benutzer:innen sind in den Statistiken besuchter Kurse nicht mehr berücksichtigt.|
|**Umfrageergebnisse aus dem Qualitätsmanagement** :octicons-infinity-24: |Im Rahmen des Qualitätsmanagements ausgefüllte Formulare werden anonymisiert gespeichert und brauchen deshalb beim Löschen eines Benutzerkontos auch nicht gelöscht werden.|
|**Log-Tabellen** :octicons-infinity-24:| tbd |



[Zum Seitenanfang ^](#delete_user)

---



## Wann kann ein/eine Benutzer:in nicht gelöscht werden? {: #none_deleted_user}


!!! warning "Attention"

    This article is still under construction.


* Haben Benutzer:innen noch ausstehende Korrekturaufträge zu erledigen, können sie nicht gelöscht werden. 

* Wenn noch Abrechnungen ausstehen (z.B. für Korrekturaufträge) können Benutzer:innen ebenfalls nicht gelöscht werden.


[Zum Seitenanfang ^](#delete_user)

