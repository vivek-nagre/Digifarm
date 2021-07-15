from django.db import models
from .category import catergory

class Product(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey(to=catergory, on_delete=models.CASCADE,default=1)
    price=models.IntegerField(default=0)
    disc=models.TextField(default='',null=True ,blank=True)
    img=models.ImageField(upload_to='upload/product/',default=1)
    def __str__(self):
        return self.name
    @staticmethod
    def get_productby_cat_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        
        else:
            return Product.objects.all()
    
    @staticmethod
    def get_proby_id(ids):
        return Product.objects.filter(id__in=ids)
        
