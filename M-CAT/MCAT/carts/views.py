from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,View
from django.urls import reverse
from .models import Cart
from products.models import Product
# Create your views here.

class ViewCart(TemplateView):
    template_name = 'cart/view_cart.html'

    def get_context_data(self,**kwargs):
        cart = Cart.objects.all()[0]
        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        return context

class UpdateCart(View):

    """docstring for UpdateCart."""
    def get(self,request,slug):
        cart = Cart.objects.all()[0]
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            pass
        except:
            pass
        if not product in cart.products.all():
            cart.products.add(product)
        else:
            cart.products.remove(product)
        new_total = 0.00
        for item in cart.products.all():
            new_total += float(item.price)
        cart.total =  new_total
        cart.save()

        return HttpResponseRedirect(reverse("carts:view_cart"))
