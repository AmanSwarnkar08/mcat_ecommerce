from django.contrib import admin
from django.conf.urls import url
from products import views
from django.conf import settings

app_name = 'products'

urlpatterns = [

    url(r'^$',views.Home.as_view(),name='home'),
    url(r'^s/$',views.Search.as_view(),name='search'),
    url(r'^store/$',views.Store.as_view(),name='store'),
    url(r'^store/(?P<slug>[\w-]+)/$',views.ProductDetail.as_view(),name='single_product'),



]
