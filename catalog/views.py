from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Book, Author, BookInstance, Genre

# Create your views here.

# simple test view to make sure everything's working
def hello(request):
  now = datetime.datetime.now()
  html = "<html><body>TEST PAGE... Howdy! It is %s.</body></html>" % now
  return HttpResponse(html)

def index(request):
  # FBV - generate counts of some main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  # available books
  num_instance_available = BookInstance.objects.filter(status__exact='a').count()

  # the 'all()' is implied by default
  num_authors = Author.objects.count()

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instance_available,
    'num_authors': num_authors,
  }

  # render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

def foo(request):
  return HttpResponse('FOO!')