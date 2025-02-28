from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField( max_length=50)
    mob=models.BigIntegerField()
    working_domain=models.CharField( max_length=50,null=True)


    def __str__(self):
        return self.name