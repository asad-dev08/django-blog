from django.contrib import admin

from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'author__username', 'status', 'category__category_name')
    list_editable = ('status', 'is_featured')

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)