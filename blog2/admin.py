from django.contrib import admin
from .models import Post, Tag, Comment

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['author', 'body', 'created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'tags']
    search_fields = ['title', 'body']
    filter_horizontal = ['tags']
    inlines = [CommentInline]


admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)