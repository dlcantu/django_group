#models will always be classes
#one return statement per function
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=10)

    def __str__(self): #important for admin (backend)
        return f'{self.name}, {self.description}, {self.price}'

class Cart(models.Model):
    total = models.ForeignKey(Product, on_delete=models.CASCADE) #need to figure out the logic