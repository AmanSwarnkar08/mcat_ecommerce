from django.contrib import admin
from django.conf.urls import url
from carts import views
#from django.conf import settings

app_name = 'carts_app'

urlpatterns = [

    url(r'cart/$',views.View.as_view(),name='view'),


]
