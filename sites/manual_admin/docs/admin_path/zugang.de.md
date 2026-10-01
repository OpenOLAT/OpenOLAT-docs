---
title: Zugang
description: Wer hinein darf. Hier entscheiden Sie, wer Ihre Installation erreicht und wie sich Personen anmelden.
---

<!-- Generiert von bin/gen_authoring_path.py aus bin/admin_path_views.yaml. Nicht von Hand bearbeiten. -->

<nav class="oo-mh-nav" aria-label="Navigation: Der Weg zur laufenden Installation" markdown="1">

<span class="oo-mh-nav__label">Navigation: Der Weg zur laufenden Installation</span>
[‹ Menü: Einrichten](einrichten.de.md){ .oo-mh-btn .oo-mh-btn--prev }
[Menü: Rollen ›](rollen.de.md){ .oo-mh-btn .oo-mh-btn--next }

</nav>

# Zugang {: #zugang}

<p class="oo-mh-sub">Wer hinein darf</p>

Hier entscheiden Sie, wer Ihre Installation erreicht und wie sich Personen anmelden. Die Authentifizierung legt die Login-Methoden fest, die Selbstregistrierung öffnet die Instanz für neue Konten, der Gast sieht nur, was ausdrücklich für Gäste freigegeben ist. Der One Time Code ergänzt das Passwort um einen zweiten Faktor.

## Begriffe dieser Station {: #terms}

<div class="oo-mh-terms" markdown>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Bereich</p>

### Login {: #platform_admin_login}

Der Abschnitt der Administration für Anmeldung und Zugang: Password und Authentifizierung, Selbstregistrierung, Gäste und externe Personen, Sicherheit, Cloud Login, LDAP, Shibboleth und Passkey.

??? note "Login im Detail"

    Der Abschnitt der Administration für Anmeldung und Zugang: Password und Authentifizierung, Selbstregistrierung, Gäste und externe Personen, Sicherheit, Cloud Login, LDAP, Shibboleth und Passkey.

    **Englisch:** Login

    [Im Handbuch lesen](../administration/Login.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Login%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Begriff</p>

### Authentifizierung {: #platform_authentication}

Der Nachweis, dass eine Person die ist, die sie zu sein vorgibt.

??? note "Authentifizierung im Detail"

    Der Nachweis, dass eine Person die ist, die sie zu sein vorgibt. OpenOlat unterstützt mehrere Verfahren nebeneinander, und ein Konto kann mehrere davon führen.

    **Englisch:** Authentication

    [Im Handbuch lesen](../../manual_user/login_registration/Login_Concept.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Authentifizierung%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Modul</p>

### Selbstregistrierung {: #platform_self_registration}

Das Modul, mit dem eine Person auf der Anmeldeseite selbst ein Konto anlegt, ohne dass die Kontoverwaltung es erstellt.

??? note "Selbstregistrierung im Detail"

    Das Modul, mit dem eine Person auf der Anmeldeseite selbst ein Konto anlegt, ohne dass die Kontoverwaltung es erstellt. Die Administration bestimmt die Heimatorganisation, die erlaubten E-Mail-Domänen, die Pflichtfelder und ob das Konto sofort aktiv oder ausstehend ist.

    **Englisch:** Self-registration

    **Wie Nutzende es nennen:** Registrierung, Konto selbst erstellen, Account anlegen, sich registrieren

    [Im Handbuch lesen](../administration/Login_Self-Registration.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Selbstregistrierung%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Begriff</p>

### Gastzugang {: #platform_guest_access}

Der Zugang zu OpenOlat ohne Konto über den Link Gastzugang auf der Anmeldeseite.

??? note "Gastzugang im Detail"

    Der Zugang zu OpenOlat ohne Konto über den Link Gastzugang auf der Anmeldeseite. Gäste sehen nur Ressourcen, die ausdrücklich für Gäste freigegeben sind, und nur in herkömmlichen Kursen.

    **Englisch:** Guest access

    **Wie Nutzende es nennen:** als Gast, anonymer Zugang, ohne Login

    **Nicht verwechseln mit «[Gast](../../manual_user/basic_concepts/guest_access.de.md)»:** Gast ist die Zugangsrolle der Person; der Gastzugang ist die Funktion, die die Administration ein- oder ausschaltet.

    [Im Handbuch lesen](../../manual_user/basic_concepts/guest_access.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Gastzugang%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

<p class="oo-mh-partof">Gehört dazu:</p>

??? note "Gast im Detail"

    Zugang ohne Anmeldung, mit Lesezugriff auf die Ressourcen, die ausdrücklich für Gäste freigegeben sind. Gäste haben kein Konto, werden nicht Mitglied und hinterlassen keine Bewertung.

    **Englisch:** Guest

    **Wie Nutzende es nennen:** unregistrierte:r Besucher:in, Besucher:in, Interessent:in, Schnuppernutzer:in, externe:r Benutzer:in

    **Nicht verwechseln mit «[Gastzugang](../../manual_user/basic_concepts/guest_access.de.md)»:** Gast ist die Zugangsrolle der Person; der Gastzugang ist die Funktion, die die Administration ein- oder ausschaltet.

    [Im Handbuch lesen](../../manual_user/basic_concepts/guest_access.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22Gast%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

<div class="oo-mh-term" markdown>

<p class="oo-mh-kind">Begriff</p>

### One Time Code {: #platform_one_time_code}

Ein achtstelliger Bestätigungscode, den OpenOlat nach der Eingabe von Anmeldename und Passwort per E-Mail schickt.

??? note "One Time Code im Detail"

    Ein achtstelliger Bestätigungscode, den OpenOlat nach der Eingabe von Anmeldename und Passwort per E-Mail schickt. Er ist der zweite Faktor für Konten ohne Passkey und standardmässig ausgeschaltet.

    **Englisch:** One time code

    **Wie Nutzende es nennen:** Einmalcode, Einmalpasswort, OTP, Code per E-Mail

    **Nicht verwechseln mit «[Passkey](../../manual_user/login_registration/Passkey.de.md)»:** Der One Time Code kommt per E-Mail und braucht kein Gerät; der Passkey ist an ein Gerät oder einen Sicherheitsschlüssel gebunden.

    [Im Handbuch lesen](../../manual_user/login_registration/One_Time_Code.de.md) · [Sophia fragen](?sophia=Was%20ist%20%22One%20Time%20Code%22%20in%20OpenOlat%20und%20wie%20richte%20ich%20es%20ein%3F)

</div>

</div>

!!! info "Nicht verwechseln: «Gastzugang» und «Gast»"

    Gast ist die Zugangsrolle der Person; der Gastzugang ist die Funktion, die die Administration ein- oder ausschaltet.

## Nachlesen {: #two_doors}

<div class="oo-mh-doors" markdown>

<div class="oo-mh-door" markdown>

<p class="oo-mh-kicker">Nachlesen</p>

[Login](../administration/Login.de.md)

Für die Einrichtung begleitet Sie frentix mit Support und Coaching: [support@frentix.com](mailto:support@frentix.com)

</div>

</div>

## Vertiefen, wenn die Installation läuft {: #deepen}

Die Installation läuft. Jetzt lohnt sich, was beim Einrichten noch nicht wichtig war: Die Begriffe dieser Station haben Teile und Einstellungen, die die Installation genauer steuern.

- **Login:** [Sicherheit](../administration/Login_Security.de.md).
- **Authentifizierung:** [Lokale OpenOlat-Authentifizierung](../../manual_user/login_registration/Login_Concept.de.md), Login für Administratoren, [Cloud Login](../administration/Login.de.md), [Passkey](../../manual_user/login_registration/Passkey.de.md) und weitere.
- **Selbstregistrierung:** [Registrierung](../../manual_user/login_registration/index.de.md). Mehr dazu auf der Seite [Selbstregistration](../administration/Login_Self-Registration.de.md).

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Login: Übersicht >](../administration/Login.de.md)<br>
[Login-Konzept >](../../manual_user/login_registration/Login_Concept.de.md)<br>
[Selbstregistration >](../administration/Login_Self-Registration.de.md)<br>
[Rollen und Rechte: Gastzugang >](../../manual_user/basic_concepts/guest_access.de.md)<br>
[Passkey >](../../manual_user/login_registration/Passkey.de.md)<br>
[One Time Code >](../../manual_user/login_registration/One_Time_Code.de.md)<br>
[Sicherheit >](../administration/Login_Security.de.md)<br>
[Login und Registrierung >](../../manual_user/login_registration/index.de.md)

**Weiterführend**<br>
[Passwort und Authentifizierung >](../administration/Login_Password_and_Authentication.de.md)<br>
[Anonyme Gäste und externe Benutzer:innen >](../administration/Guest_and_invitation.de.md)<br>
[Glossar >](../../reference_glossary/glossary.de.md)

[Zum Seitenanfang ^](#zugang)
