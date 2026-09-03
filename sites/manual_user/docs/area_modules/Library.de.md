# Bibliothek {: #library}


## Konzept {: #concept}

* Die Bibliothek kann separat nach Bedarf für die ganze Instanz aktiviert/deaktiviert werden.
* Es gibt nur eine Bibliothek pro OpenOlat-Instanz.
* Sie erscheint in der Regel als Menüpunkt in der obersten Navigationszeile.
* Technisch gesehen verbirgt sich hinter der Bibliothek ein verknüpfter Ressourcenordner, der im Autorenbereich bearbeitet werden kann.
* Dokumente der Bibliothek können von Benutzer:innen kommentiert, heruntergeladen oder direkt als E-Mail verschickt werden.

[Zum Seitenanfang ^](#library)

---

## Struktur der Bibliothek einrichten {: #structure}

Wenn Administrator:innen das Modul aktivieren, muss ein zugehöriger Ressourcenordner angegeben werden.
Um die Struktur der Bibliothek einzurichten, können Besitzer:innen diesen zugeordneten Ressourcenordner im Autorenbereich editieren.

[Zum Seitenanfang ^](#library)

---

## Dokumente hochladen {: #upload}

**Wer kann Dokumente in die Bibliothek hochladen?**<br>

Wenn Administrator:innen das Hochladen erlaubt haben, können alle Benutzer:innen Dokumente in die Bibliothek hochladen. Die Einstellung liegt in der System-Administration unter:<br>
`Administration > Module > Bibliothek`<br>
Allerdings werden die Dokumente erst in die Bibliothek aufgenommen, nachdem eine Prüfung stattgefunden hat.

**Was kann hochgeladen werden?**<br>

Es kann eine Vielzahl von Dateiformaten hochgeladen werden:

* Office-Dokumente, wie docx, xlsx, pdf, u.a.
* Bild-Dateien, wie jpg, png, u.a.
* Video-Dateien (mp4)
* ...

[Zum Seitenanfang ^](#library)

---

## Prüfung beim Upload {: #upload_check}

Nach dem Hochladen eines Dokuments erfolgt zunächst standardmässig eine Prüfung, bevor es in der Bibliothek angezeigt wird.

Besitzer:innen des mit der Bibliothek verknüpften Ressourcenordners werden über einen neuen Upload informiert und müssen das Dokument freigeben.

Alternativ kann eine andere Person für die Prüfung bestimmt werden. Administrator:innen tragen dazu in der System-Administration unter `Administration > Module > Bibliothek` eine Mailadresse ein. Ist dort keine Adresse eingetragen, erhalten die Besitzer:innen der Lernressource den Prüfauftrag.

Administrator:innen können diesen Prüfprozess unter `Administration > Module > Bibliothek` auch deaktivieren. Wenn Sie die Prüfung deaktivieren, sollten Sie sich allerdings bewusst sein, dass so jede Person, die auf die Bibliothek zugreifen kann, Dokumente dort ungeprüft hochladen kann. [:octicons-tag-16:{ title="ab Release 19.1 (OO-8309)" }](https://track.frentix.com/issue/OO-8309)


[Zum Seitenanfang ^](#library)
