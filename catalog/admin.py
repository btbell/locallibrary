from django.contrib import admin
#from . import models
from .models import Author, Book, BookInstance, Genre

# Register your models here.
# admin.site.register(models.Author)
# admin.site.register(models.Book)
# admin.site.register(models.BookInstance)
# admin.site.register(models.Genre)

"""define the Author admin class"""
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  """set the dates on one line in admin panel"""
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

"""register admin class with the associated model"""
admin.site.register(Author, AuthorAdmin)

"""Register the Admin classes for Book using the decorator"""
"""@register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):"""
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  fieldsets = (
    ('REQUIRED', {
      'fields': ('title', 'author', 'summary', 'isbn', 'genre', )
    }),
    ('OPTIONAL: Dublin Core Metadata Elements - this standard DC set includes the Title, and Author from the Required section', {
      'fields': ('subject', 'publisher', 'contributor', 'date', 'type', 'format', 'source', 'language', 'relation', 'coverage', 'rights',)
    }),
  )


"""Register the Admin classes for BookInstance using the decorator"""
"""setting a class with 'pass' leaves admin behavior unchanged"""
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book', 'status', 'due_back')
  list_filter = ('status', 'due_back')
  # section admin detail view
  fieldsets = (
    (None, {
      'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
      'fields': ('status', 'due_back')
    }),
  )



# Register the Admin classes for Genre using the decorator
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
  pass