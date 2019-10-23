from django.contrib import admin
from django.conf.urls import url
from carts import views

#from django.conf import settings

app_name = 'carts'

urlpatterns = [


    url(r'^cart/$',views.ViewCart.as_view(),name='view_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$',views.UpdateCart.as_view(),name='update_cart'),



]
