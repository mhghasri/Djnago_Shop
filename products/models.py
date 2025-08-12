from django.db import models
from django.utils.text import slugify
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
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):

        self.final_price = int(self.price - (self.price * self.discount / 100))

        if not self.slug:
            self.slug = slugify(self.title)
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

colors = [
    ("r", "قرمز"),
    ("b", "آبی"),
    ("m", "مشکی"),
    ("w", "سفید"),
    ("g", "سبز"),
]

class ProductColor(models.Model):
    color = models.CharField(max_length=2, choices=colors)
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")

    @property #-> call to template
    def final_price(self)->int:
        final_price = int(self.price - (self.product.discount * self.price / 100))
        return final_price
    
    def __str__(self):
        return f"Product | {self.product.title}"
    
    class Meta:
        verbose_name_plural = "ProductColor List"