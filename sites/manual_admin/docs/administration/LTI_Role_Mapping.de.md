# LTI - Rollen-Mapping [:octicons-tag-16:{ title="ab Release 20.2 (OO-9003)" }](https://track.frentix.com/issue/OO-9003) {: #LTI_role_mapping}

Beim Aufruf eines externen Tools sendet OpenOlat die LTI-Rollen der aufrufenden Person mit. Welche LTI-Rollen eine Person erhält, hängt von ihrer Kursrolle ab. Kursbesitzer:innen legen diese Zuordnung im Kurseditor fest, im [Kursbaustein "LTI-Seite"](../../manual_user/learningresources/Course_Element_LTI_Page.de.md), Tab "Seiteninhalt". Administrator:innen begrenzen in der System-Administration, welche LTI-Rollen Kursbesitzer:innen dabei zur Wahl haben, und setzen die Standardwerte für neue Kursbausteine.

## Zuordnung im Kurseditor {: #course_editor}

Im Tab "Seiteninhalt" ordnen Kursbesitzer:innen den drei Kursrollen "Besitzer:in", "Betreuer:in" und "Teilnehmer:in" je eine oder mehrere der sechs LTI-Rollen zu: "Lerner", "Instruktor", "Administrator:in", "Assistent Lehrperson", "Inhaltsersteller" und "Mentor". Ein neu angelegter Kursbaustein übernimmt die Standardwerte aus der System-Administration. Beim Kopieren eines Kursbausteins oder eines Kurses bleibt die bestehende Zuordnung erhalten.

LTI-Rollen, die die System-Administration nicht freigegeben hat, sind für Kursbesitzer:innen ausgegraut. Administrator:innen und Lernressourcenverwalter:innen der Organisation, der der Kurs zugeordnet ist, können alle LTI-Rollen zuweisen. Im folgenden Beispiel ist die LTI-Rolle "Administrator:in" für alle drei Kursrollen gesperrt:

![Spalte Administrator:in für die drei Kursrollen ausgegraut und markiert, die übrigen fünf LTI-Rollen bleiben wählbar, im Tab Seiteninhalt des Kursbausteins LTI-Seite im Kurseditor](assets/LTI_role_mapping_course_element_editor_admin_disabled_v1_en.png){ class="shadow lightbox" }

Beim Aufruf des Kursbausteins sendet OpenOlat die LTI-Rollen zusammen mit der Deployment ID und den weiteren konfigurierten Attributen, zum Beispiel der E-Mail-Adresse, an das Tool.

## Einstellungen in der System-Administration {: #administration}

Administrator:innen legen in der System-Administration unter `Administration > Externe Werkzeuge > LTI`, Tab "Rollen-Mapping", die Grenzen und Standardwerte fest:

| Feld | Bemerkung |
|---|---|
| Konfigurierbar durch Kursbesitzer:innen | Die LTI-Rollen, die Kursbesitzer:innen im Kurseditor zuweisen dürfen. Nicht gewählte LTI-Rollen sind im Kurseditor ausgegraut. |
| Standardeinstellungen für Besitzer:innen | Die LTI-Rollen, die ein neuer Kursbaustein "LTI-Seite" der Kursrolle Besitzer:in vorbelegt. |
| Standardeinstellungen für Betreuer:innen | Die Vorbelegung für die Kursrolle Betreuer:in. |
| Standardeinstellungen für Teilnehmer:in | Die Vorbelegung für die Kursrolle Teilnehmer:in. |

![Konfigurierbar durch Kursbesitzer:innen ohne Administrator:in, darunter die Standardeinstellungen je Kursrolle, im Tab Rollen-Mapping der Seite LTI in der System-Administration](assets/LTI_role_mapping_admin_v1_en.png){ class="shadow lightbox" }

Die Standardwerte stehen in der Datei `olat.properties`:

```
# LTI roles (capitalized) that can be assigned to users based on their OpenOlat roles in the course editor by the course owner.
lti13.roles.configurable.by.course.owner=LEARNER,INSTRUCTOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR

# The following is an exhaustive list of possible values for the field above:
lti13.roles.configurable.by.course.owner.values=LEARNER,INSTRUCTOR,ADMINISTRATOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR

# Default LTI roles for given OpenOlat roles in courses:
lti13.default.role.settings.for.owners=INSTRUCTOR,ADMINISTRATOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR
lti13.default.role.settings.for.coaches=INSTRUCTOR,TEACHING_ASSISTANT,MENTOR
lti13.default.role.settings.for.participants=LEARNER

# The following is an exhaustive list of possible values for the fields above:
lti13.default.role.settings.for.xxx.values=LEARNER,INSTRUCTOR,ADMINISTRATOR,TEACHING_ASSISTANT,CONTENT_DEVELOPER,MENTOR
```

Um die Standardwerte zu ändern, tragen Sie die entsprechenden Eigenschaften in der Datei `olat.local.properties` ein oder passen Sie die Werte direkt im Tab "Rollen-Mapping" an. Die Werte in `olat.local.properties` übersteuern `olat.properties`, und die Einstellungen im Tab "Rollen-Mapping" übersteuern `olat.local.properties`.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)

**Weiterführend**<br>
[Learning Tools Interoperability Core Specification (IMS Global Learning Consortium) >](http://www.imsglobal.org/spec/lti/v1p3/)<br>
[LTI 1.3 Integrationen >](../administration/LTI_Integrations.de.md)<br>
[LTI - Externe Werkzeuge >](../administration/LTI_External_tools.de.md)<br>
[LTI - Externe Plattformen >](../administration/LTI_External_platforms.de.md)<br>
[LTI - Deep Linking >](../administration/LTI_Deeplinking.de.md)<br>
[LTI-Zugang zu einem Kurs konfigurieren >](../../manual_user/learningresources/LTI_Share_courses.de.md)<br>
[LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)

[Zum Seitenanfang ^](#LTI_role_mapping)
