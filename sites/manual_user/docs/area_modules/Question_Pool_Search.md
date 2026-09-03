# Question Pool: Search {: #question_pool_search}

When searching in the question bank, you will find question items in *the* pool or *the* list you are currently in. It is not possible to search for items across multiple question pools.


## Simple Search {: #simple_search}

The simple search is a full-text search that searches across all elements of the items. To optimize the search, here is some information on the syntax of the underlying Lucene search.

|  Syntax    | Example  |
| ---------- | ----------|
| Whole search terms are always expected.| \+ Works: *Indication* |
| |-  Doesn't work: *Indicati*  |

The search for partial terms therefore only works if wildcards are used:

* With " ? " you search for exactly one additional character,
* With " * " you search for any number of additional characters.

<br>

**Here are a few examples:**


*Indicatio?* => Finds *Indication*

_Indicatio*_ => Finds *Indication, Indications, Indication classes ...*

You can use " " to search for phrases, i.e. a group of words.

*Hello World* => Finds all items containing either a *Hello* or a *World*
(OR operator).

*"Hello World"* => Finds all items containing exactly this phrase.

Several terms can be combined using " - " and " + ". The characters are placed before the corresponding terms without a space.

*+Hello +World* => Finds all items containing both terms (AND operator).

*Hello -World* => Finds all items containing the first term but under no circumstances the second term.

Some special characters are reserved for Lucene and cannot be used, e.g. "_" and ":".<br> If these special characters are used, the result list will probably be empty.

[To the top of the page ^](#question_pool_search)


## Advanced Search {: #advanced_search}

The advanced search allows you to search across defined fields. It also includes the metadata. Unlike the simple search, which also searches across all fields, here you define exactly which search term is searched for in which field. This increases both recall and precision of the search. Any fields can be combined with each other.

[To the top of the page ^](#question_pool_search)
