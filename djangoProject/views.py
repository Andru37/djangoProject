from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def homepage1(request: HttpRequest):
    return render(request, "homepage.html")


def profile1(request: HttpRequest):
    return render(request, "profile.html")


def product1(request: HttpRequest):
    return render(request, "product/product-detail.html", {
        "quantity_null": True
    })


def apple1(request: HttpRequest):
    return render(request, "apple.html")


def milk1(request: HttpRequest):
    return render(request, "milk.html")


def fish1(request: HttpRequest):
    return render(request, "fish.html")
