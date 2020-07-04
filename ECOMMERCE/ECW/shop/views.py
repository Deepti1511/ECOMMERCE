from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("about us")

def contact(request):
    return HttpResponse("contact us")


def tracker(request):
    return HttpResponse("track")

def productView(request):
    return HttpResponse("have a look at the product")

def search(request):
    return HttpResponse("search")

def checkout(request):
    return HttpResponse("checkout")