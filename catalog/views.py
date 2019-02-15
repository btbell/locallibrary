from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime

from .models import Book, Author, BookInstance, Genre
from catalog.forms import RenewBookForm

# Create your views here.

# simple test view to make sure everything's working
def hello(request):
  now = datetime.datetime.now()
  html = "<html><body>TEST PAGE... Howdy! It is %s.</body></html>" % now
  return HttpResponse(html)

@login_required
def index(request):
  # FBV - generate counts of some main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()

  # available books
  num_instance_available = BookInstance.objects.filter(status__exact='a').count()

  # borrowed books
  num_instance_borrowed = BookInstance.objects.filter(status__exact='o').count()

  # the 'all()' is implied by default
  num_authors = Author.objects.count()

  # number of visits to this view - counted in the session variable
  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1

  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instance_available': num_instance_available,
    'num_instance_borrowed': num_instance_borrowed,
    'num_authors': num_authors,
    'num_visits' : num_visits,
  }

  # render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

# generic class views
class BookListView(LoginRequiredMixin, generic.ListView):
  model = Book
  # queryset = Book.objects.all()
  template_name = 'catalog/book_list.html'
  paginate_by = 10

class BookDetailView(LoginRequiredMixin, generic.DetailView):
  model = Book

class AuthorListView(LoginRequiredMixin, generic.ListView):
  model = Author
  template_name = 'catalog/author_list.html'
  paginate_by = 10

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
  #model = Author

  context_object_name = 'author'
  queryset = Author.objects.all()

  def get_context_data(self, **kwargs):
    # call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # add Queryset of All books
    context['book_list'] = Book.objects.all()
    return context

"""class AuthorBookListView(LoginRequiredMixin, generic.ListView):
  template_name = 'catalog/author_book_list.html'

  def get_queryset(self):
    self.author.id = get_object_or_404(Author, name=self.kwargs['pk'])
    return Book.objects.filter(author=self.author.id)"""



class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
  """ Generic class-based view listing books on loan to current user. """
  model = BookInstance
  template_name = 'catalog/bookinstance_list_borrowed_user.html'
  paginate_by = 10

  def get_queryset(self):
    return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class BorrowedBooksLibrarianListView(PermissionRequiredMixin, generic.ListView):
  """ Generic class-based view listing all books on loan AND only viewable by librarians. """
  model = BookInstance
  template_name = 'catalog/bookinstance_list_all_borrowed.html'
  paginate_by = 10
  permission_required = 'catalog.can_change_book_instance'

  def get_queryset(self):
    return BookInstance.objects.filter(status__exact='o').order_by('due_back')
  #def get_context_data(self, **kwargs):
    #author_bk_list = super().get_context_data(**kwargs)
    #author_bk_list['book_list'] = Book.objects.filter(author_id=" ")
    #return author_bk_list

@login_required
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)