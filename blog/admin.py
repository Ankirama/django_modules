from django.contrib             import admin
from blog.models                import Post, Tag
from django_markdown.admin      import MarkdownModelAdmin

class PostAdmin(MarkdownModelAdmin):
    # fields display on change list
    list_display = ('title', 'description',)
    # fields to filter the change list with
    list_filter = ('published', 'date_created',)
    # fields to search in change list
    search_fields = ['title', 'description', 'body']
    # enable the date drill down on change list
    date_hierarchy = 'date_created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
