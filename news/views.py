from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,"news/home.html")

def page1(request):
    return render(request, "news/page1.html")

def page2(request):
    return render(request,"news/page2.html")


