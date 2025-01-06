# coding: utf-8
from newapp.models import *
Category.objects.create(name=vegetables)
Category.objects.create(name="vegetables")
Category.objects.create(name="fruits")
Category.objects.create(name="berries")
Category.objects.create(name="chocolates")
Product.objects.create(name="orange",price=3.33,category_id=2)
Product.objects.create(name="potato",price=1.33,category_id=1)
Product.objects.create(name="strawberry",price=4.50,category_id=3)
Product.objects.create(name="mars",price=1.50,category_id=4)
Product.objects.all()
