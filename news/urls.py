from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.page1, name="page1"),
    path("somewhere/", views.page2, name="page2"),

]