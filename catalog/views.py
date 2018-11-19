from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
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

  # number of visits to this view - counted in the session variable
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instance_available,
    'num_authors': num_authors,
    'num_visits' : num_visits,
  }

  # render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

# generic class views
class BookListView(generic.ListView):
  model = Book
  # queryset = Book.objects.all()
  template_name = 'catalog/book_list.html'
  paginate_by = 10

class BookDetailView(generic.DetailView):
  model = Book

class AuthorListView(generic.ListView):
  model = Author
  template_name = 'catalog/author_list.html'
  paginate_by = 10

class AuthorDetailView(generic.DetailView):
  model = Author

  #def get_context_data(self, **kwargs):
    #author_bk_list = super().get_context_data(**kwargs)
    #author_bk_list['book_list'] = Book.objects.filter(author_id=" ")
    #return author_bk_list