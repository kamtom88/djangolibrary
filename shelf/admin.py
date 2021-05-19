from django.contrib import admin

from .models import publisher, author, book, rent, book_item, book_edition, book_category, message


class BookItemAdmin(admin.ModelAdmin):
    list_display = ['cover_type']


class BookEditionAdmin(admin.ModelAdmin):
    list_display = ['book', 'publisher', 'isbn']


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['tittle']
    list_display = ['tittle', 'sites']


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


class RentalAdmin(admin.ModelAdmin):
    search_fields = ['who', 'what', 'when']
    list_display = ['who', 'what', 'when']


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email']


admin.site.register(message.Message, MessageAdmin)
admin.site.register(book_category.BookCategory, BookCategoryAdmin)
admin.site.register(book_edition.BookEdition, BookEditionAdmin)
admin.site.register(book_item.BookItem, BookItemAdmin)
admin.site.register(rent.Rental, RentalAdmin)
admin.site.register(book.Book, BookAdmin)
admin.site.register(author.Author, AuthorAdmin)
admin.site.register(publisher.Publisher, PublisherAdmin)
