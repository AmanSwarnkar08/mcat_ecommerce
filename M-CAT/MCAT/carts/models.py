from django.db import models
from products.models import Product
# Create your models here.

class Cart(models.Model):
    """docstring for Cart."""

    products = models.ManyToManyField(Product,  blank = True)
    total = models.DecimalField(max_digits = 100, decimal_places = 2, default = 0.00)
    created_dt = models.DateTimeField(auto_now_add = True, auto_now = False)
    last_modified_dt = models.DateTimeField(auto_now_add = False, auto_now = True)
    active = models.BooleanField(default = True)

    def __init__(self, arg):
        super(Cart, self).__init__()
        self.arg = arg

    def __str__(self):
        return "Cart id: {}".format(self.id)
