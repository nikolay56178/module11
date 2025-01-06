from django.urls import path

from news.views import *


urlpatterns = [
    path("", index, name="home"),
    path("about/", page1, name="page1"),
    path("somewhere/", page2, name="page2"),

]


handler404 = pageNotFound