From the Mozilla tutorial 
(https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).
"we will store information about books (title, summary, author, written language, category, ISBN) 
and that we might have multiple copies available (with globally unique id, availability status, 
etc.). We might need to store more information about the author than just their name, and there 
might be multiple authors with the same or similar names. We want to be able to sort information 
based on book title, author, written language, and category.

When designing your models it makes sense to have separate models for every "object" (group of related information). In this 
case the obvious objects are books, book instances and authors."

There are some differences, e.g. I didn't make my urls the same way as the tutorial as I find
the way I did them much easier to understand. But in a nutshell, when I complete this exercise,
it will be working copy of the app from their tutorial.