# Suchfunktion

Mit der Suche im Fragenpool finden Sie Frageitems jeweils in dem Pool oder Liste in der Sie sich gerade befinden. Es ist nicht möglich Fragepoolübergreifend Items zu suchen.

## Einfache Suche

Die einfache Suche ist eine Volltextsuche die über alle Elemente der Items sucht. Um die Suche zu optimieren, hier einige Informationen zur Syntax der zugrunde liegenden Lucene-Suche.

Syntax| Beispiel  
---|---  
Es werden immer ganze Suchbegriffe erwartet.|

\+ Funktioniert: Indikation

 _-  Funktioniert nicht: Indikati_  
  
Die Suche nach Teilbegriffen funktioniert daher nur wenn Wildcards verwendet werden. Mit " ? " wird nach genau einem weiteren Zeichen gesucht, 
während " * " nach einer beliebigen Anzahl weiterer Zeichen sucht. Hier ein paar Beispiele: 


Indikatio? = Indikation

Indikatio* = Indikation, Indikationen, Indikationsklassen....  
  
Mit Hilfe von " " kann nach Phrasen, also einer Gruppe von Wörtern, gesucht werden|

Hallo Du = findet alle Items die entweder ein Hallo oder ein Du enthalten
(ODER- Verknüpfung)

"Hallo Du" findet alle Items die genau diese Phrase enthalten  
  
Mit Hilfe von " - " und " + " können mehrere Begriffe kombiniert werden. Die
Zeichen werden ohne Leerschlag vor die entsprechenden Begriffe gesetzt.|

+Hallo +Du = findet alle Items die beide Begriffe enthalten (UND-Verknüpfung)

Hallo -Du = findet alle Items die nur den ersten Begriff, auf gar keinen Fall aber den zweiten Begriff enthalten  
  
Es gibt einige gesperrte Sonderzeichen die von Lucene verwendet werden, wie z.B. "_" und ":"| Werden diese Sonderzeichen verwendet, wird die Ergebnisliste vermultlich leer sein.  
  
## Erweiterte Suche

Die erweiterte Suche ermöglicht die Suche über festgelegte Felder, und bezieht auch die Metadaten mit ein. Anders als bei der einfachen Suche, die ebenfalls über alle Felder sucht, wird hier aber genau festgelegt welcher Suchbegriff in welchem Feld gesucht werden soll, was die Trefferquote sowie die Genauigkeit der Suche erhöht. Es können beliebige Felder miteinander kombiniert werden.

  

