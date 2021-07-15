from django.db import models
class coustmer(models.Model):
    
    name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone =models.IntegerField()
    email =models.EmailField()
    password=models.CharField(max_length=12)
    
    def __str__(self):
        return self.name

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):   
        try:
            
            return coustmer.objects.get(email=email)
        except:
            return False
    

    def isExist(self):
        if coustmer.objects.filter(email=self.email):
            
            return True
        
        return False
    
