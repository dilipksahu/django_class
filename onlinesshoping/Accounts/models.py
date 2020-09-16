from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cname = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

class Product(models.Model):
    pname = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


class Cart(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


