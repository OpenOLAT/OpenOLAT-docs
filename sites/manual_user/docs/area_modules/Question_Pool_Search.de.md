# Fragenpool: Suchfunktion {: #question_pool_search}

Mit der Suche im Fragenpool finden Sie Frage-Items jeweils in *dem* Pool oder *der* Liste, in der Sie sich gerade befinden. Es ist nicht möglich, über mehrere Fragenpools hinweg Items zu suchen.


## Einfache Suche {: #simple_search}

Die einfache Suche ist eine Volltextsuche, die über alle Elemente der Items sucht. Um die Suche zu optimieren, hier einige Informationen zur Syntax der zugrunde liegenden Lucene-Suche.

|  Syntax    | Beispiel  |
| ---------- | ----------|
| Es werden immer ganze Suchbegriffe erwartet.| \+ Funktioniert: *Indikation* |
| |-  Funktioniert nicht: *Indikati*  |
  
Die Suche nach Teilbegriffen funktioniert daher nur, wenn Wildcards verwendet werden:

* Mit " ? " wird nach genau einem weiteren Zeichen gesucht, 
* Mit " * " wird nach einer beliebigen Anzahl weiterer Zeichen sucht. 

<br>

**Hier ein paar Beispiele:**


*Indikatio?* => Findet *Indikation*

_Indikatio*_  => Findet *Indikation, Indikationen, Indikationsklassen ...*  
  
Mit Hilfe von " " kann nach Phrasen, also einer Gruppe von Wörtern, gesucht werden.

*Hallo Du* => Findet alle Items, die entweder ein *Hallo* oder ein *Du* enthalten
(ODER- Verknüpfung).

*"Hallo Du"* => Findet alle Items die genau diese Phrase enthalten. 
  
Mit Hilfe von " - " und " + " können mehrere Begriffe kombiniert werden. Die
Zeichen werden ohne Leerschlag vor die entsprechenden Begriffe gesetzt.

*+Hallo +Du* => Findet alle Items die beide Begriffe enthalten (UND-Verknüpfung).

*Hallo -Du* => Findet alle Items, die nur den ersten Begriff, auf gar keinen Fall aber den zweiten Begriff enthalten.
  
Es gibt einige gesperrte Sonderzeichen, die von Lucene verwendet werden, wie z.B. "_" und ":".<br> Werden diese Sonderzeichen verwendet, wird die Ergebnisliste vermultlich leer sein.  

[Zum Seitenanfang ^](#question_pool_search)


## Erweiterte Suche {: #advanced_search}

Die erweiterte Suche ermöglicht die Suche über festgelegte Felder. Sie bezieht auch die Metadaten mit ein. Anders als bei der einfachen Suche, die ebenfalls über alle Felder sucht, wird hier aber genau festgelegt, welcher Suchbegriff in welchem Feld gesucht werden soll. Dies erhöht die Trefferquote und die Genauigkeit der Suche. Es können beliebige Felder miteinander kombiniert werden.

  
[Zum Seitenanfang ^](#question_pool_search)
