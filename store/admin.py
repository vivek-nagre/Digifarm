from django.contrib import admin
from .models.product import Product
from .models.category import catergory
from .models.coustmer import coustmer
from .models.order import order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category','img']
class Admincatergory(admin.ModelAdmin):
    list_display=('id','name')
class Admincoustmer(admin.ModelAdmin):
    list_display=('id','name','last_name','email','phone')
class Adminorder(admin.ModelAdmin):
    list_display=('id','product','custmer','quantity','price','date')
           
admin.site.register(Product,ProductAdmin)
admin.site.register(order,Adminorder)
admin.site.register(catergory,Admincatergory)
admin.site.register(coustmer,Admincoustmer)
