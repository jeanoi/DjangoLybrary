from django.contrib import admin
from .models import Author, Genre, Books, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)

class BooksInLine(admin.TabularInline):
    model = Books

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'Book_author')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back', 'borrower')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
admin.site.register(Books, BookAdmin)
