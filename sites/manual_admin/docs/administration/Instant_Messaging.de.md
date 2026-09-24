# Modul Instant-Messaging {: #instant_messaging}

Mit dem Instant-Messaging schalten Sie die Funktionen "Chat" und
"Kurznachrichten" frei und legen fest, wer wen kontaktieren kann. Die
Einstellungen dazu finden Sie in der System-Administration unter:<br>
`Administration > Module > Instant-Messaging`

Die System-Administration erreichen Administrator:innen und
Systemadministrator:innen. Wie Rollen vergeben werden, beschreibt
[Rollen zuweisen](../usermanagement/Assign_roles.de.md).

### Instant-Messaging Modul [:octicons-tag-16:{ title="ab Release 8.4 (OO-448)" }](https://track.frentix.com/issue/OO-448) {: #im_module }

Hier entscheiden Sie, ob Chat und Kurznachrichten in OpenOlat überhaupt zur
Verfügung stehen.

#### Chat und Kurznachrichten einschalten {: #enable_chat }

Mit dieser Einstellung schalten Sie die gesamte Instant-Messaging-Funktionalität
ein und aus. Ist sie ausgeschaltet, sind Chat und Kurznachrichten deaktiviert,
und alle weiteren Einstellungen dieser Seite lassen sich nicht bearbeiten.

### Chaträume {: #chat_rooms }

Hier legen Sie fest, ob Gruppen und Kurse einen eigenen Chatraum erhalten
können, in dem sich alle Mitglieder gemeinsam austauschen.

#### Chat als Gruppenwerkzeug {: #chat_group_tool }

Ist diese Einstellung eingeschaltet, können Gruppenbetreuer:innen für jede
Gruppe einen Chatraum konfigurieren. Mit "Anonyme Teilnahme ermöglichen" dürfen
die Mitglieder im Chatraum schreiben, ohne ihren richtigen Namen zu zeigen. Mit
"Anonym als Standardeinstellung" betreten sie den Chatraum anonym und blenden
ihren richtigen Namen bei Bedarf selbst ein. "Anonym als Standardeinstellung"
lässt sich nur wählen, wenn "Anonyme Teilnahme ermöglichen" eingeschaltet ist.

#### Chat als Kurswerkzeug {: #chat_course_tool }

Ist diese Einstellung eingeschaltet, können Besitzer:innen eines Kurses in jedem
Kurs einen Chatraum konfigurieren. Die beiden Einstellungen "Anonyme Teilnahme
ermöglichen" und "Anonym als Standardeinstellung" wirken im Kurs gleich wie in
der Gruppe.

### Kurznachrichten an einzelne Personen {: #direct_messages }

Hier legen Sie fest, wen Benutzer:innen direkt anschreiben können, was sie vom
Status der anderen sehen und mit welchen Standardwerten neue Benutzer:innen
starten.

#### Alle Benutzer:innen kontaktierbar {: #all_users_contactable }

Mit dieser Einstellung erlauben Sie das Chatten und Versenden von
Kurznachrichten unter allen Benutzer:innen. Ist sie eingeschaltet, zeigt die
Visitenkarte unterhalb des Profilbildes einen Link, über den sich eine
Kurznachricht versenden lässt. Benutzer:innen können diese Einstellung
individuell mit ihrer persönlichen Konfiguration übersteuern.

#### Gruppenkontakte anzeigen {: #show_group_contacts }

Mit dieser Einstellung erlauben Sie das Chatten und Versenden von
Kurznachrichten unter Gruppenteilnehmer:innen. Ist sie eingeschaltet, erscheint
die Liste aller Gruppenmitglieder der Gruppen, in denen man Mitglied ist. Diese
Personen können für einen Chat oder eine Kurznachricht direkt angewählt werden.
Zusätzlich muss die Gruppe die Anzeige der Mitglieder freigeben:<br>
[Gruppenadministration, Tab Mitglieder](../../manual_user/groups/Group_Administration.de.md#members)

#### Online Status anzeigen {: #show_online_status }

Mit dieser Einstellung wählen Sie, ob die Benutzer:innen den aktuellen
Online-Status der anderen Benutzer:innen oder Gruppenteilnehmer:innen sehen. Ist
sie ausgeschaltet, erscheint anstelle des Statussymbols eine Sprechblase. Die
Benutzer:innen wissen dann nicht, ob ihre Nachricht unmittelbar verschickt
werden kann.

#### Standardstatus für neue Benutzer:innen [:octicons-tag-16:{ title="ab Release 21.0 (OO-9466)" }](https://track.frentix.com/issue/OO-9466) {: #default_status }

Mit dieser Einstellung legen Sie fest, mit welchem Online-Status neue
Benutzer:innen starten. Zur Auswahl stehen "Verfügbar", "Bitte nicht stören" und
"Nicht verfügbar". Voreingestellt ist "Verfügbar".

#### Kurznachrichten von allen Benutzer:innen empfangen (Standard) {: #receive_messages_default }

Mit dieser Einstellung legen Sie fest, ob die persönliche Einstellung
"Kurznachrichten von allen Benutzer:innen empfangen" für neue Benutzer:innen
eingeschaltet ist. Voreingestellt ist sie eingeschaltet.

OpenOlat übernimmt die beiden Standardwerte beim ersten Login einer Person mit
eingeschaltetem Instant-Messaging in deren persönliche Einstellungen für Chat
und Kurznachrichten. Eine spätere Änderung der Standardwerte gilt deshalb nur
für Personen, für die noch keine persönlichen Einstellungen gespeichert sind.
Jede Person kann ihre Einstellungen danach selbst anpassen:<br>
[Persönliche Konfiguration: Einstellungen](../../manual_user/personal_menu/Settings.de.md)

Weitere Informationen zur Anwendung des Instant-Messaging Moduls finden Sie hier: [Chat](../../manual_user/basic_concepts/Chat.de.md)

## Weiterführende Informationen {: #further_information}

[Rollen zuweisen >](../usermanagement/Assign_roles.de.md)<br>
[Gruppenadministration >](../../manual_user/groups/Group_Administration.de.md)<br>
[Persönliche Konfiguration: Einstellungen >](../../manual_user/personal_menu/Settings.de.md)<br>
[Chat >](../../manual_user/basic_concepts/Chat.de.md)<br>
[Gruppenwerkzeuge nutzen >](../../manual_user/groups/Using_Group_Tools.de.md)<br>
[Kurseinstellungen - Tab Toolbar >](../../manual_user/learningresources/Course_Settings_Toolbar.de.md)

[Zum Seitenanfang ^](#instant_messaging)
