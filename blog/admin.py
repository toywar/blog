from django.contrib import admin
from blog.models import BlogPost, Comments




class BlogPostInline(admin.StackedInline):
    model = Comments
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    fields = ['blogpost_title', 'blogpost_text', 'blogpost_date']
    inlines = [BlogPostInline]
    list_display = ['blogpost_title', 'blogpost_text', 'blogpost_date']
    list_filter = ['blogpost_date']

admin.site.register(BlogPost, BlogPostAdmin)