# Gruppenmitglied werden {: #group_membership}

Es gibt verschieden Möglichkeiten wie Personen Mitglied in einer Gruppe verwenden können. Dabei tauchen folgende Fragen auf: 

**Wer trägt das Mitglied in die Gruppe ein?**

Möglich sind:

1)	Die Person trägt sich selbst ein 
2)	Der/Die Gruppenbetreuer:in trägt Mitglieder ein
3)	Administrative Rollen wie Benutzerverwalter:innen, Mitgliederverwalter:innen fügen Personen hinzu  
4)	Automatische Zuordnung durch ein externes System

**Wo erfolgt die Zuordnung?**

Möglich sind:

* a)	Direkt in der Gruppe 
* b)	In einem zur Gruppe zugehörigen Kurs 
* c)	In weiteren OpenOlat System-Bereichen  
* d)	Außerhalb von OpenOlat

Beide Aspekte können wie folgt miteinander kombiniert werden:

## 1a) User trägt sich selbst in die konkrete Gruppe ein. {: #by_yourself}

![group_membership_offer_v1_de.png](assets/group_membership_offer_v1_de.png){ class="shadow lightbox" }

Hierfür muss der/die Gruppenbetreuer:in direkt in der Gruppe unter „Administration“ -> Freigabe“ ein **„Angebot“** hinterlegen. 

![Angebot hinzufügen](assets/Gruppe_Freigabe.png){ class="shadow lightbox" }

Für das Angebot stehen mehrere Optionen zur Verfügung: 

**„Frei verfügbar“** erstellt eine Buchung ohne Passwort. Interessierte kommen nach der Buchung direkt in die Gruppe. Bei der Option **„Zugangscode“** wird ein Passwort für den Zugang hinterlegt und der User muss bei der Buchung das zuvor mitgeteiltes Passwort eingeben. Das bietet sich an, wenn nicht jeder Zugang zu einer Gruppe erhalten soll, sich die Personen aber selbst eintragen sollen. Je nach Konfiguration der Systemadministrator:innen steht auch noch die Option **„PayPal Checkout“** zur Verfügung. Mit diesem Angebot ist die Ressource mit PayPal kostenpflichtig buchbar. 

![3 Angebotsvarianten](assets/Gruppe_Angebot_hinzufuegen.png){ class="shadow lightbox" }

**Wo finden Benutzer:innen Gruppen die sie buchen können?**

Gruppen mit Angeboten finden Benutzer:innen unter “Veröffentlichte Gruppen”. Mit Klick auf **“Beitreten”** kann ein Angebot gebucht werden und man wird zum Gruppenmitglied.

![group_membership_offer_v1_de.png](assets/group_membership_offer_v1_de.png){ class="shadow lightbox" }


**Überbuchung** {: #overbooking}

Wurde die Gruppengrösse begrenzt, können Teilnehmer:innen, die sich in eine Gruppe eintragen wollen, in der schon alle Plätze besetzt sind, auf eine Warteliste genommen werden. (Siehe [Gruppen erstellen](Create_Groups.de.md#vorgesehene-anzahl-teilnehmende)).

Bei Überbuchung erscheinen entsprechende Hinweise, z.B.:

![group_membership_overbooking1_v1_de.png](assets/group_membership_overbooking1_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#group_membership)

## 2a)  Gruppen-Betreuende tragen Personen direkt in die Gruppe ein {: #add_groupmember}

Als Gruppen-Betreuer:in wählen oder erstellen Sie die gewünschte Gruppe und gehen in den Tab „Administration“ der Gruppe. Im Tab „Mitglieder“ können dann weitere Teilnehmende und auch Betreuende hinzugefügt werden.

![Gruppenmitglieder in Gruppe hinzufügen](assets/Gruppe_Mitglied_hinzufuegen1.png){ class="shadow lightbox" }

OpenOlat Autor*in steht zusätzlich noch die „Massensuche“ beim Hinzufügen der Mitglieder zur Verfügung. Auf diesem Weg können rasch Personen deren OpenOlat ID oder E-Mailadresse bekannt ist direkt hinzugefügt werden. 
Ferner haben Autor:innen die Möglichkeit auch  „externe Mitglieder“, die aktuell noch keinen OpenOlat Account haben, in die Gruppe einzuladen. Hierfür müssen die konkreten E-Mail-Adressen der Personen eingetragen werden.   

### Eine Person in mehrere Gruppen eintragen  {: #add_several_groupmembers}

Gruppenbetreuer:innen können eine Person auch direkt in mehrere Gruppen eintragen, z.B. wenn zu einem Studiengang eine Zuordnung zu mehreren Gruppen notwendig ist. Gehen Sie dafür in den Gruppen-Bereich und wählen Sie alle Gruppen aus, denen die Person hinzugefügt werden soll. Voraussetzung ist, Sie sind auch Betreuer:in der jeweiligen Gruppen. Es erscheinen mehrere Buttons. 

![Personen in mehrere Gruppen eintragen](assets/Mehrere_Gruppen_waehlen.png){ class="shadow lightbox" }

Wählen Sie hier **„Konten verwalten“**. Es öffnet sich ein Popup-Menü, in dem die Mitglieder aller selektierten Gruppen gemeinsam aufgeführt sind. Nutzen Sie die entsprechenden Buttons um weitere Teilnehmende oder Betreuende allen gewählten Gruppen  hinzuzufügen bzw. diese auf die Warteliste zu setzen. 

![Konten verwalten](assets/Gruppen_Konten_verwalten_TN_hinzufuegen.png){ class="shadow lightbox" }

Die Gruppenmitgliedschaft muss anschliessend evtl. noch bestätigt werden. Wenn Sie in der Mitgliederverwaltung in einem der Kurse nachsehen, finden Sie ggf. einen entsprechenden Hinweis. Ob eine solche Bestätigung durch die neuen Gruppenmitglieder erforderlich ist, kann durch Administrator:innen vorgegeben werden.
![group_membership_confirm_when_several_members_added_v1_de.png](assets/group_membership_confirm_when_several_members_added_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#group_membership)

## 1b) User trägt sich im Rahmen eines Kurses in eine Gruppe ein 

Kurse und Gruppen können miteinander verbunden sein. Ist das der Fall, können sich Personen auch an bestimmten Stellen innerhalb des Kurses in eine Gruppe eintragen. 

Konkret funktioniert das über die Kursbausteine ["Einschreibung"](../learningresources/Course_Element_Enrolment.de.md)  und [„Themenvergabe"](../learningresources/Course_Element_Topic_Assignment.de.md). Bei diesen Kursbausteinen wird automatisch eine OpenOlat Gruppe angelegt. Wählen Personen ein Thema bzw. schreiben Sie sich in eine Gruppe ein, werden sie automatisch der entsprechenden Gruppe hinzugefügt. 

![Kurs Einschreibung in Gruppe](assets/Kurs_Einschreibung.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#group_membership)




## 2b) Kursbesitzer:innen tragen Personen in eine kursbezogene Gruppe ein 

Gruppen können auch mit Kursen verbunden sein. Ist dies der Fall können Kursbesitzer:innen bzw. Personen mit dem Recht die „Mitgliederverwaltung“ des Kurses zu nutzen dort auch Gruppen erstellen und hinzufügen. 

![Kurs Mitgliederverwaltung](assets/Kurs_Mitgliederverwaltung.png){ class="shadow lightbox" }

Über den angezeigten Gruppennamen gelangt man zur Gruppe und kann dann wie unter 2a) beschrieben als Gruppenbetreuer:in Personen hinzufügen. 

Eine andere Möglichkeit im Kurs ist der Weg über die Mitgliederliste des Kurses (Mitgliederverwaltung -> **Mitglieder**). Hier kann man eine oder mehrere Kurs-Mitglieder kursspezifischen Gruppen zuordnen.  

![Mitglied bearbeiten](assets/Mitglied_bearbeiten_Gruppe.png)

Wählt man z.B. mehrere Kurs-Mitglieder aus können sie über den erscheinenden Button „Bearbeiten“ allen im Kurs zur Verfügung stehenden Gruppen als Teilnehmer:in oder als Betreuer:in zugeordnet werden. 

![Mehrere Gruppen wählen](assets/Mehrere_Gruppen_waehlen.png)

![Mehrere Gruppen](assets/MehrereMitglieder_bearbeiten.png)

Die Änderungen werden anschliessend zur Überprüfung noch mal angezeigt und eine E-Mail-Benachrichtigung kann ebenfalls verschickt werden. 
 

[Zum Seitenanfang ^](#group_membership)

## 3c) Von Personen mit OpenOlat System-Rollen zugeordnet 

Auch bestimmte Personen, die nicht selbst Gruppenbetreuer:in einer Gruppe sind können Gruppenmitglieder auf administrativer Ebene Gruppen hinzufügen. Hierzu zählen Personen mit der OpenOlat Rolle Gruppenverwalter:in und Benutzervewalter:in bzw. OpenOlat Administrator:innen mit Zugriff auf diese Bereiche. 

### Gruppenmitgliedschaft in der Benutzerverwaltung hinzufügen {: #add_groupmembers_in usermanagement}

Benutzerverwalter:innen können nach Aufruf der Kartei einer bestimmten Person im Tab „Gruppen“  die vorhandenen Gruppenmitgliedschaften einsehen und neue hinzufügen. 

![group_membership_by_user_management_v1_de.png](assets/group_membership_by_user_management_v1_de.png){ class="shadow lightbox" }

### Gruppenmitgliedschaft in der Gruppenverwaltung hinzufügen

Gruppenverwalter:innen verfügen im Gruppenbereich zusätzlich über den Tab „Gruppenverwaltung“ und sehen dort alle Gruppen. Ähnlich wie bei den eigenen Gruppen können hierüber auch Personen in die Gruppen eingetragen werden.   

![Gruppenverwaltung](assets/Gruppenverwaltung.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#group_membership)


## 4d) Automatisch erstellte Gruppenmitgliedschaften - managed {: #add_groupmembers_automatically}

Werden in einem anderen System (z.B. einer HR-Software) bereits bestimmte Personen in Gruppen zusammengefasst, können diese Gruppenmitgliedschaften auch in OpenOlat abgebildet werden. Dazu benötigt es allerdings eine Middleware (Syncher), die dann automatisiert Benutzer:innen bestimmten OpenOlat-Gruppen zuordnen kann.

Bei Fragen zu automatisch zugewiesener Gruppenmitgliedschaft wenden Sie sich bitte an frentix.

[Zum Seitenanfang ^](#group_membership)


---


## Weitere Informationen {: #further_information}

[Gruppe erstellen >](Create_Groups.de.md)<br>
[Gruppenwerkzeuge nutzen >](Using_Group_Tools.de.md)<br>
[Gruppe verlassen > ](Leave_a_Group.de.md)<br>
[LTI-Zugang zu einer Gruppe konfigurieren > ](LTI_Share_groups.de.md)<br>
Für Administrator:innen: [Systemweite Konfiguration der Gruppen >](../../manual_admin/administration/Modules.de.md)<br>

[Zum Seitenanfang ^](#group_membership)