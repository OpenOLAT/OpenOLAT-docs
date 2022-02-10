# Tips and tricks for authors

We use the Material theme for MkDocs. See the [Material for MkDocs Reference](https://squidfunk.github.io/mkdocs-material/reference/) for a complete reference. 

The following are a list of things we use commonly: 

## Admonitions
!!! tip
    This is an admonition

See the list of [supported types / icons and styles](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types)

### Details

Details are the same as admonitions but expandable / collapsable. Use Just use ??? for initially collapsed and ???+ for initially opened details. Use the same image classes as with the admonitions

??? info
    Also available as collapsable items. Just use ??? instead of !!!

See [the pymdown extension page](https://facelessuser.github.io/pymdown-extensions/extensions/details/) to learn how this works in detail. 


## In-Page references Just use {: #anchor-example}

Add `{: #anchor-example}` to any title element to create an anchor that can be referenced by other pages or in an external link. Make sure you use the same anchor name for all languages of the same page. 
 
Here an example link to [this chapter](#anchor-example) 

## Image width and alignment

Add `{ align=left}` or `{ align=right}` to format images left or right of text. More on this [here](https://squidfunk.github.io/mkdocs-material/reference/images/)

Add `{ width=200px}` for the size. This can also be combiend like this: `{ align=left width=200px}`