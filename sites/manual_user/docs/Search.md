#  [Search](Search.html)

The question bank search enables you to find items in the pool or database you
are just navigating in. It is not possible to conduct a comprehensive question
bank search.

#### Simple Search

The simple search is a full text search over all item elements / fields. In
order to ensure an opitimized search, please find information on the search
syntax in the table below. The search is based on the lucene search library.

Syntax| Example  
---|---  
Always use complete words, not just word parts.|

Will not work: tes

Will work: test  
  
Searching for word parts thus will only work when using wildcards. Lucene
supports single and multiple character wildcard searches within single terms.

To perform a single character wildcard search use the "?" symbol.

To perform a multiple character wildcard search use the "*" symbol.

|



tes? = test

te*t = test, text, teaist, tent  
  
Phrases, groups of words, can be found when surrounded by double quotes.|

Hello World = recalls all items containing either "Hello" and/or "World" (OR
operator)

"Hello World" recalls all items containing exactly this phrase  
  
Boolean operators allow terms to be combined through logic operators.
Supported are  " - " and " + " as boolean operators. The operators must be
placed in front of the terms without a space.

|

+Hello +World = recalls all items containing both terms  
(AND operator)

Hello -World = recalls all items containing the first term but not the second
(NOT operator)  
  
Some special characters are barred from using in the search, as they are
reserved for Lucene, e.g. "_" and ":"| Using these special characters leads to
unpredictable search results.  
  
#### Advanced Search

The advanced search provides you with a means to search across a set of
defined fields, also including meta data fields. Different to the simple
search, which searches over all elements, you decide exactly which term to
search for in which field. This increases both recall and precision of the
search. You can combine as many search terms/fields as required.

  1. [OpenOlat 16.1 User Manual](../OO161EN.html)
  2. [Seiten](https://confluence.openolat.org/collector/pages.action?key=OO161EN)
  3. [OpenOlat 16.1 User Manual](OpenOLAT+16.1+User+Manual.html)
  4. [Question Bank](Question+Bank.html)
  5. [Search](Search.html)

Sie sind nicht angemeldet. Ihre Änderungen werden mit anonym markiert. Sie
sollten sich
[anmelden](https://confluence.openolat.org/login.action?os_destination=%2Fdisplay%2FOO161EN%2FSearch),
wenn Sie bereits über ein Konto verfügen.

search

attachments

weblink

advanced

image-effects

image-attributes

  * Absatz
    * Absatz
    * Überschrift 1
    * Überschrift 2
    * Überschrift 3
    * Überschrift 4
    * Überschrift 5
    * Überschrift 6
    * Vorformatiert
    * Zitat

  * Fett
  * Kursiv
  * Unterstreichen
  * Farbauswahl

Weitere Farben

    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  
    *  

  * Formate

    * Durchgestrichen 
    * Tiefgestellt 
    * Hochgestellt 
    * Festbreitenschriftart 

    * Formatierung zurücksetzen 

  * Aufzählung
  * Nummerierte Liste

  * Aufgabenliste

  * Einzug verkleinern
  * Einzug vergrößern

  * Linksbündig ausrichten
  * Zentriert ausrichten
  * Rechtsbündig ausrichten

  * Seitenlayout

  * Verknüpfung

  * Tabelle

  * Einfügen

Inhalt einfügen

    * Dateien und Bilder 
    * Verknüpfung 
    * Markup 
    * Horizontale Trennlinie einfügen 
    * Aufgabenliste 
    * Datum 
    * Emoticon 
    * Sonderzeichen 
Makro einfügen

    * Benutzererwähnung 
    * Jira-Vorgang/-Filter 
    * Info 
    * Status 
    * Galerie 
    * Inhalt 

    * Andere Makros 

  * Seitenlayout
    * Kein Layout
    * Zweispaltig (einfach)
    * Zweispaltig (einfach, linke Randleiste)
    * Zweispaltig (einfach, rechte Randleiste)
    * Dreispaltig (einfach)
    * Zweispaltig
    * Zweispaltig (linke Randleiste)
    * Zweispaltig (rechte Randleiste)
    * Dreispaltig
    * Dreispaltig (Randleisten links und rechts)

  * Rückgängig
  * Wiederholen

  * Suchen/Ersetzen

  * Hilfe für Tastenkombinationen

Sie sind nicht angemeldet. Ihre Änderungen werden mit anonym markiert. Sie
sollten sich
[anmelden](https://confluence.openolat.org/login.action?os_destination=%2Fdisplay%2FOO161EN%2FSearch),
wenn Sie bereits über ein Konto verfügen.

Diese Seite wird auch von  bearbeitet. Ihre Änderungen werden mit seinen/ihren
zusammengeführt, wenn Sie speichern.



Bearbeiten

Vorschau

Speichern

Schließen

