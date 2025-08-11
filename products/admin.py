from django.contrib import admin
from . models import *

# -------------------- TabularInline -------------------- #

# ----------- AtributeInline ----------- #

class AttributeInline(admin.TabularInline):
    model = Attribute
    extra = 0

# ----------- ImagesInline ----------- #

class ImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 0

# -------------------- AdminModel -------------------- #

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'final_price', 'special_sells', 'created_at', 'is_available']

    inlines = [AttributeInline, ImagesInline]

    fieldsets = [
        ("Information", {'fields' : ('title', 'full_detail', 'description', 'image_1', 'image_2')}),
        ("Price", {'fields' : ('price', 'discount')}),
        ("Details", {'fields' : ('is_available', 'special_sells')}),
    ]


# -------------------- register -------------------- #
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute)
admin.site.register(ProductImage)