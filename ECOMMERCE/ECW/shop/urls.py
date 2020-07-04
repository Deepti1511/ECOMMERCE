#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Shop"),
    path("about/", views.about, name="about us"),
    path("contact/", views.contact, name="Contact us"),
    path("tracker/", views.tracker, name="tracker"),
    path("productView", views.productView, name="productview"),
    path("search", views.search, name="search"),
    path("checkout", views.checkout, name="checkout")
]