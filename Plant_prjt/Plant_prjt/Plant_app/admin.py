from django.contrib import admin
from .models import ProductsCategory,Products

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(ProductsCategory,CategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Products,ProductsAdmin)