from django.contrib import admin
from . models import *

# ------------------- AdminModels ------------------- #

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'email', 'adress']

    fieldsets = [
        ('Information', {'fields' : ('name', 'number' )}),
        ('Email', {'fields' : ('email', )}),
        ('Adress', {'fields' : ('adress', )}), 
        ('About us', {'fields' : ('about_us', )}), 
    ]

# --------------- AboutUs --------------- #

# ------------------- Register ------------------- #
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(AskUs)
admin.site.register(Link)