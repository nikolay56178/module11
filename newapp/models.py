from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,db_index=False)
    stock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('categoryes', kwargs={'prod_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
