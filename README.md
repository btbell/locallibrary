From the Mozilla tutorial 
(https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).
"we will store information about books (title, summary, author, written language, category, ISBN) 
and that we might have multiple copies available (with globally unique id, availability status, 
etc.). We might need to store more information about the author than just their name, and there 
might be multiple authors with the same or similar names. We want to be able to sort information 
based on book title, author, written language, and category.

When designing your models it makes sense to have separate models for every "object" 
(group of related information). In this case the obvious objects are books, book instances and authors."

There are some differences, e.g. I didn't make my urls the same way as the tutorial as I find
the way I did them much easier to understand. But in a nutshell, when I complete this exercise,
it will be working copy of the app from their tutorial.

The URLs that we'll need for our pages are:

catalog/ — The home (index) page.
catalog/books/ — A list of all books.
catalog/authors/ — A list of all authors.
catalog/book/<id> — The detail view for a particular book, with a field primary key of <id> 
(the default). For example, the URL for the third book added to the list will be /catalog/book/3.
catalog/author/<id> — The detail view for the specific author with a primary key field of <id>.  For example, 
the URL for the 11th author added to the list will be  /catalog/author/11.