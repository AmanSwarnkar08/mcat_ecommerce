from django.shortcuts import render,Http404
from django.views.generic import View,TemplateView,ListView,DetailView
from .models import Product

# Create your views here.
'''
def abc(request):
    template = 'products/home.html'
    context = locals()
    return render(request,template,context)

class deff(View):
    def get(self,request):
        template = 'products/home.html'
        context = locals()
        return render(request,template,context)
'''
class Home(TemplateView):
    template_name= 'products/home.html'


class Store(TemplateView):
    template_name = 'products/store.html'

    def get_context_data(self,**kwargs):
        products = Product.objects.all()
        context = super().get_context_data(**kwargs)
        context['product_list'] = products
        return context


class ProductDetail(TemplateView):
    """docstring for .ProductDetail"""
    template_name = 'products/product_details.html'

    def get_context_data(self,slug,**kwargs):
        try:
            product = Product.objects.get(slug=slug)
            images = product.productimage_set.all()
            context = super().get_context_data(**kwargs)
            context['product_detail'] = product
            context['images'] = images
            return context
        except :
            raise Http404

class Search(TemplateView):
    """docstring for Search."""
    template_name = 'products/results.html'

    def get_context_data(self,**kwargs):
        try:
            q= self.request.GET.get('q')
        except:
            q = None
        if q:
            products = Product.objects.filter(title__icontains = q)
            context = super().get_context_data(**kwargs)
            context['query'] = q
            context['products'] = products
            #template_name = 'products/results.html'
        else:
            context = super().get_context_data(**kwargs)
            #template_name = 'products/store.html'
            #context['product_list'] = products
        return context
