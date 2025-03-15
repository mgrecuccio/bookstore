from django.contrib import admin

from books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')

# Register your models here.
admin.site.register(Book, BookAdmin)