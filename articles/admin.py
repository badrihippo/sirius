from articles.models import Article, Series, Section, Tag
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Publication', {'fields': ['issue', 'section', 'series', 'part_number','part_name','pages']}),
        ('For web-only content', {'fields': ['date','edit_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['title','title_show','slug','content','tags']}),
        ('Credits', {'fields': ['persons', 'sources'], 'classes':['collapse']}),
        ('Display', {'fields': ['header_image', 'thumbnail', 'blurb', 'show_blurb' ,'footer'], 'classes':['collapse']}),
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Series)
admin.site.register(Section)
admin.site.register(Tag)
