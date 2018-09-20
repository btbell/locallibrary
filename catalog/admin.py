from django.contrib import admin
#from . import models
from .models import Author, Book, BookInstance, Genre

# Register your models here.
# admin.site.register(models.Author)
# admin.site.register(models.Book)
# admin.site.register(models.BookInstance)
# admin.site.register(models.Genre)

# define the Author admin class
class AuthorAdmin(admin.ModelAdmin):
  pass

# register admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
# @register decorator to register the models (this does exactly the same thing as the admin.site.register() syntax):
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  pass

# Register the Admin classes for BookInstance using the decorator
# setting a class with 'pass' leaves admin behavior unchanged
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  pass

# Register the Admin classes for Genre using the decorator
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
  pass