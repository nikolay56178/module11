from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseNotFound


def index(request):
    return render(request,"news/home.html")

def page1(request):
    return render(request, "news/page1.html")

def page2(request):
    return render(request,"news/page2.html")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')
