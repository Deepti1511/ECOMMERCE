from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods}
    for cat in categories:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

        # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
        # allProds = [[products, range(1, nSlides), nSlides],
        #             [products, range(1, nSlides), nSlides]]
       # params={ 'No_of_slides' : Nslides ,  'range': range(Nslides) ,   'product': products}
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method== "POST":
        print(request)
        name= request.POST.get('name', '')
        print(name)
        email= request.POST.get('email' , '')
        phone= request.POST.get('phone', '')
        desc= request.POST.get('desc', '')
       # contact = contact(name=name, email=email, phone=phone, desc=desc)
        #contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def productView(request,myid):
    prod = Product.objects.filter(id=myid)
    print(prod)

    return render(request, 'shop/productView.html', {'product':prod[0]})

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

