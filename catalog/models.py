from django.db import models
from django.urls import reverse # generate URLs by reversing URL pattern
import uuid

# Create your models here.

class Genre(models.Model):
  """model that represents book genre (e.g. Fiction, Non Fiction)"""
  name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction')

  def __str__(self):
    return self.name

class Language(models.Model):
  """model that represents a language (e.g. English, French)"""
  name = models.CharField(max_length=200, help_text="Enter the book's printed language (e.g. English, French)")

  def __str__(self):
    return self.name


class Book(models.Model):
  """model that represents a book"""
  title = models.CharField(max_length=200)
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

  # Foreign key is used as a book can only have one author (in this exercise but can in practice), but authors can have multiple books.
  # Author as a string instead of object because it hasn't been declared yet in the file.
  summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
  isbn = models.CharField('ISBN', max_length=13, help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

  # Many to many field used because genre can contain many books. Books can cover many problems.
  # Genre class has already been defined so we can use the object above.
  genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
  language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    """Returns the url to access a detail record for book"""
    return reverse('book-detail', args=[str(self.id)])

  class BookInstance(models.Model):
    """representation of a specific copy of a book, that can be borrowed from library"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for the particular book within the library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
      ('m', 'Maintenance'),
      ('o', 'On load'),
      ('a', 'Available'),
      ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability',)

    class Meta:
      ordering = ['due_back']

    def __str__(self):
      """string interpolation syntax as of Python 3.6"""
      return f'{self.id} ({self.book.title})'

class Author(models.Model):
  """model tht represents an author"""
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  date_of_birth = models.DateField(null=True, blank=True)
  date_of_death = models.DateField('Died', null=True, blank=True)

  class Meta:
    ordering = ['last_name', 'first_name']

  def get_absolute_url(self):
    """returns the URL to a particular author instance"""
    return reverse('author-detail', args=[str(self.id)])

  def __str__(self):
    return f'{self.last_name}, {self.first_name}'