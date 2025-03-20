from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from books.forms import ReviewForm
from books.models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"

#
class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView,
):
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related('reviews__author',)

    def get(self, request, *args, **kwargs):
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)


class ReviewGet(DetailView):
    model = Book
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context

class ReviewPost(SingleObjectMixin, FormView):
    model = Book
    form_class = ReviewForm
    template_name = 'books/book_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.object
        review.author = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        book = self.object
        return reverse("book_detail", kwargs={"pk": book.pk})


class SearchResultListView(ListView):
    model=Book
    context_object_name="book_list"
    template_name = "books/search_result.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(title__icontains=query)