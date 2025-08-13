from django.contrib import admin
from . models import *

# -------------- Inline -------------- #

class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0

# -------------- Inline -------------- #

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views']

    inlines = [AttributeInline, ]

    fieldsets = [
        ('Information', {'fields' : ('title', 'description')}),
        ('Author', {'fields' : ('author', )}),
        ('Category', {'fields' : ('category', )}),
    ]

# -------------- register -------------- #

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Attribute)
