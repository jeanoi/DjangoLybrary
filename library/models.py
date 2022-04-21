from django.db import models
from django.forms import CharField
import uuid
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    Author_name = models.CharField(max_length=800)

    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.Author_name


class Books(models.Model):
    title = models.CharField(max_length=800)
    Book_author = models.ForeignKey(Author,  on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=2000)
    ISBN = models.CharField(max_length=13, help_text='type the ISBN using only digits')
    genre = models.ManyToManyField('Genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title', 'Book_author']

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ''.join([genre.name for genre in self.genre.all()[:3]])


    def __str__(self):
        return self.title


class Genre(models.Model):  
    genre = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.language


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    book = models.ForeignKey(Books, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
    max_length=1,
    choices = LOAN_STATUS,
    blank=True, 
    default='a',
    help_text='book status')

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)