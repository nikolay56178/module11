from django.urls import path

from newapp.views import *


urlpatterns = [
    path("products/", product, name="product"),
    path("products/<int:prod_id>/", show_products, name="products-name"),

]
