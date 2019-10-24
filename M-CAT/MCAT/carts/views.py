from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import TemplateView,View
from django.urls import reverse
from .models import Cart
from products.models import Product
# Create your views here.

class ViewCart(TemplateView):
    template_name = 'cart/view_cart.html'

    def get_context_data(self,**kwargs):
        try:
            the_id = self.request.session['cart_id']
        except:
            the_id =None
        if the_id:
            cart = Cart.objects.get(id = the_id)
            context = super().get_context_data(**kwargs)
            context['cart'] = cart
        else:
            empty_message = 'Your Cart is Sad! Keep Shopping.'
            context = super().get_context_data(**kwargs)
            context['empty'] = True
            context['empty_message'] = empty_message

        return context

class UpdateCart(View):

    """docstring for UpdateCart."""
    def get(self,request,slug):
        request.session.expi
        try:
            the_id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
            request.session['cart_id'] = new_cart.id
            the_id  = new_cart.id

        cart = Cart.objects.get(id = the_id)
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
        request.session['total_items'] = cart.products.count()
        cart.total =  new_total
        cart.save()

        return HttpResponseRedirect(reverse("carts:view_cart"))
