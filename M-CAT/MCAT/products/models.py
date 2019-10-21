from django.urls import reverse
from django.db import models

# Create your models here.
class Product(models.Model):
    """docstring for Product. """
    title = models.CharField(max_length = 256, null = False, blank = False)
    product_category = models.ForeignKey('ProductCategory', on_delete = models.SET_DEFAULT, default = 'Other')
    description = models.TextField(null = True, blank = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 100, default = 99.99)
    sale_price = models.DecimalField(decimal_places = 2, max_digits = 200, null = True, blank = True)
    slug = models.SlugField(unique = True)
    created_dt = models.DateTimeField(auto_now_add = True, auto_now = False)
    last_modified_dt = models.DateTimeField(auto_now_add = False, auto_now = True)
    active = models.BooleanField(default = True)

    class Meta:
        unique_together = ('title' , 'slug')

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("products:single_product",kwargs = {"slug" : self.slug})



class ProductImage(models.Model):
    """docstring for ProductImage."""
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'products/product_images/')
    featured = models.BooleanField(default = False)
    thumbnail = models.BooleanField(default =False)
    active = models.BooleanField(default = True)
    last_modified_dt = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.product.title


class ProductCategory(models.Model):
    """docstring for ProductCategory."""
    category = models.CharField(max_length = 256, blank = False, null = False, default = 'Other')

    def __str__(self):
        return self.category
