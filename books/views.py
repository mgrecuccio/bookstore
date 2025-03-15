from django.views.generic import ListView, DetailView

from books.models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"