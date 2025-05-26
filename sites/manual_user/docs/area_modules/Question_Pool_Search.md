# Question Pool: Search {: #question_pool_search}

When searching in the question pool, you will find question items in *this* pool or *that* list you are currently in. It is not possible to search for items across multiple question pools.

## Simple Search {: #simple_search}

The simple search is a full-text search that searches across all elements of the items. To optimize the search, here is some information on the syntax of the underlying lucene search.

|  Syntax    | Example  |
| ---------- | ----------|
| Whole search terms are always expected.| \+ Works: *Indication* |
| |-  Doesn't work: *Indicati*  |
  
The search for partial terms therefore only works if wildcards are used:

* With " ? " searches for exactly one additional character, 
* Press " * " to search for any number of additional characters. 

<br>

**Here are a few examples:**


*Indicatio?* => Finds *Indication*

_Indicatio*_ => Finds *Indication, Indications, Indication classes ...*
  
You can use " " to search for phrases, i.e. a group of words|

*Hello World* => Finds all items containing either a *Hello* or a *World*
(OR link).

*"Hello World"* => Recalls all items containing exactly this phrase.
  
Several terms can be combined using " - " and " + ". The characters are placed before the corresponding terms without a space.

*+Hello +World* => recalls all items containing both terms (AND operator)

*Hello -World* => recalls all items containing the first term but not the second.
  
Some special characters are barred from using in the search, as they are reserved for Lucene, e.g. "_" and ":"| Using these special characters leads to unpredictable search results.

[To the top of the page ^](#question_pool_search)
  

## Advanced Search {: #advanced_search}

The advanced search provides you with a means to search across a set of defined fields, also including meta data fields. Different to the simple search, which searches over all elements, you decide exactly which term to search for in which field. This increases both recall and precision of the search. You can combine as many search terms/fields as required.

[To the top of the page ^](#question_pool_search)

