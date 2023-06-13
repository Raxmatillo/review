from django.contrib import admin
from django.utils.html import format_html

from .models import Language, Editor, Journal, References, Article



@admin.register(Editor)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('editor', )
    search_fields = tuple('editor')



@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
	list_display = ('name', 'main_editor')
	search_fields = ('name', 'main_editor', 'description')
	ordering = ('created_at', )




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'journal__name',
                     'editor')
    ordering = ('created_at', )

    def download_article(self, obj):
        return format_html(f"<a href='{obj.file.url}'>Ko'rish</a>")
    download_article.short_description = 'Ko\'rish'


admin.site.register([Language, References])