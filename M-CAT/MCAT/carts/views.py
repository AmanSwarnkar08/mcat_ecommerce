from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from .models import Cart
# Create your views here.

class ViewCart(TemplateView):
    template_name = 'cart/view.html'

    def get_context_data(self,**kwargs):
        cart = Cart.objects.all()[0]
        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        return context
