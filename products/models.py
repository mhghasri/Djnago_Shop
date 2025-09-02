from django.db import models
from django.utils.text import slugify
from django.db.models import Q, Min, Max        # for aggrigate price
import os
import random
import string

# ------------------------ function ------------------------ #

# --------- uploads to --------- #

def product_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    random_string = ''.join(random.choices(string.ascii_letters, k=10))
    return f"products/django-image-{random_string}{ext}"

def product_gallery_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    random_string = ''.join(random.choices(string.ascii_letters, k=10))
    return f"products/gallery/django-image-{random_string}{ext}"

# ------------------------ Models ------------------------ #

# --------- Brand Model --------- #

class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# --------- Category Model --------- #

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Category | {self.name}"

# --------- Product Model --------- #
class Product(models.Model):
    title = models.CharField(max_length=200)
    full_detail = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    special_sells = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    image_1 = models.ImageField(upload_to=product_image_path)
    image_2 = models.ImageField(upload_to=product_image_path)
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
    categories = models.ManyToManyField(Category, related_name="products")
    brand = models.ForeignKey(Brand,  on_delete=models.CASCADE, related_name='product_brnad', null=True, blank=True)

    def save(self, *args, **kwargs):

        # this feture update price after changing discount all final_price changed

        if self.pk:     # mean if it was existed

            # select the old discount by query               # this method just return the value of list and flat=True just return a list not a tuple of list
            old_discount = Product.objects.filter(pk=self.pk).values_list('discount', flat=True).first()    # this first help us to return a value not a queryset

            if old_discount != self.discount:
                for color in self.colors.all():
                    color.final_price = int(color.price - (color.price * self.discount / 100))
                    color.save(update_fields=['final_price'])

        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Product | {self.title}"
    
    class Meta:
        verbose_name_plural = "Product List"

# --------- Attribute Model --------- #
class Attribute(models.Model):
    name = models.CharField(max_length=200)         # name -> cpu
    value = models.CharField(max_length=200)        # value -> 14900k
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="attribute") 

    def __str__(self):
        return f"Product | {self.name} --- {self.product.title}"
    
    class Meta:
        verbose_name_plural = "Atribute List"

# --------- ImagesGallery Model --------- #
class ProductImage(models.Model):
    image = models.ImageField(upload_to=product_gallery_path)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="gallery")

    def __str__(self):
        return f"Product | {self.product.title}"
    
    class Meta:
        verbose_name_plural = "ProductImage List"

# --------- ProductColor Model --------- #

# -- colors -- #

class ProductColor(models.Model):
    color_hex = models.CharField(max_length=10)
    price = models.IntegerField()
    color_name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")
    final_price = models.IntegerField(default=0)
    

    def save(self, *args, **kwargs):
        self.final_price = int(self.price - (self.price * self.product.discount / 100))
        super().save(*args, **kwargs)

        min_price = self.product.colors.aggregate(min=Min('final_price'))['min']

        if min_price != None and min_price != self.product.final_price:
            self.product.price = self.price
            self.product.final_price = min_price
            self.product.save()
    
    def __str__(self):
        return f"Product | {self.product.title}"
    
    class Meta:
        verbose_name_plural = "ProductColor List"