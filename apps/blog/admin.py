from django.contrib import admin
from .models import Blog, Category, Tag


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
