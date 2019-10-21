from django.contrib import admin

# Register your models here.
from .models import Product,ProductImage,ProductCategory

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_dt'
    search_fields = ['title','description']
    list_display = ['title', 'price','active', 'created_dt', 'last_modified_dt']
    list_editable = ['price','active']
    list_filter = ['price','active']
    readonly_fields = ['created_dt','last_modified_dt']
    prepopulated_fields = {"slug" : ("title",)}
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
