from django.contrib import admin
from .models import Category,Product,Cart

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cname'] 

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','pname','price','description','category']

admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['id','Product','user']

admin.site.register(Cart,CartAdmin)
