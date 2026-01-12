from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'price', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title','author')