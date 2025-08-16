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

# ----------- ImagesInline ----------- #

class ColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0
    fields = ['color', 'price']

# -------------------- AdminModel -------------------- #

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'final_price', 'special_sells', 'created_at', 'is_available']

    inlines = [AttributeInline, ImagesInline, ColorInline]

    fieldsets = [
        ("Information", {'fields' : ('title', 'full_detail', 'description', 'image_1', 'image_2')}),
        ("Price", {'fields' : ('price', 'discount')}),
        ('Category', {'fields' : ('category', )}),
        ("Details", {'fields' : ('is_available', 'special_sells')}),
    ]

# -------------------- ColorModel -------------------- #

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    fieldsets = [
        ("Information", {'fields' : ('name', )}),
    ]

# -------------------- ColorModel -------------------- #

class ProductColorAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Color", {'fields' : ('color', )}),
        ("Price", {'fields' : ('price', )}),
    ]

# -------------------- register -------------------- #
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute)
admin.site.register(ProductImage)
admin.site.register(ProductColor, ProductColorAdmin)