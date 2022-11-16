from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=5)

    def __str__(self):
        return self.name
        return self.description
        return self.price

class Cart(models.Model):
    total = models.ForeignKey(Product, on_delete=models.CASCADE) #need to figure out the logic