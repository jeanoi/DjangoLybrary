from re import template
from typing import List
from django.views.generic import TemplateView, ListView, DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BookInstance

class HomePage(TemplateView):
    template_name='index.html'


class BookList(ListView):
    context_object_name = 'books'
    model = models.Books
    template_name='book_list.html'

class BookDetail(DetailView):
    context_object_name = 'books_detail'
    model = models.Books
    template_name = 'book_detail.html'

class AuthorList(ListView):
    context_object_name = 'authors_list'
    model = models.Author
    template_name = 'author_list.html'

class AuthorDetail(DetailView):
    context_object_name = 'authors_detail'
    model = models.Author
    template_name = 'author_detail.html'

class LoanedBooksByUser(LoginRequiredMixin, ListView):
    model = models.BookInstance
    template_name = 'registration/bookinstance_list_borrowed_user.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
