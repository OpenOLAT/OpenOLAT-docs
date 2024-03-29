# Search

The question bank search enables you to find items in the pool or database you are just navigating in. It is not possible to conduct a comprehensive question bank search.

## Simple Search

The simple search is a full-text search that searches across all elements of the items. To optimize the search, here is some information on the syntax of the underlying Lucene search.

Syntax| Example  
---|---  
Always use complete words, not just word parts.

\+ Will work: Indication

 _-  Will not work: Indicati_  
  
The search for partial terms therefore only works if wildcards are used. With " ? " is used to search for exactly one additional character while " * " searches for any number of additional characters. Here are a few examples:

Indicatio? = Indication

Indicatio* = Indication, Indications, Indication classes....
  
You can use " " to search for phrases, i.e. a group of words|

Hello World = recalls all items containing either "Hello" and/or "World" (OR operator)

"Hello World" recalls all items containing exactly this phrase  
  
Supported are  " - " and " + " as boolean operators. The operators must be
placed in front of the terms without a space.|

+Hello +World = recalls all items containing both terms (AND operator)

Hello -World = recalls all items containing the first term but not the second (NOT operator)  
  
Some special characters are barred from using in the search, as they are reserved for Lucene, e.g. "_" and ":"| Using these special characters leads to unpredictable search results.  
  
## Advanced Search

The advanced search provides you with a means to search across a set of defined fields, also including meta data fields. Different to the simple search, which searches over all elements, you decide exactly which term to search for in which field. This increases both recall and precision of the search. You can combine as many search terms/fields as required.

