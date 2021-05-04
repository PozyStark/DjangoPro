from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(response):
    return HttpResponse("<h1>Hello</h1>")


def number(response, num):

    if response.POST:
        print(response.POST)

    if num > 5:
        return redirect("home", permanent=False)

    return HttpResponse(f"<h1> Number {num} </h1>")


def pageNotFound(response, exception):
    return HttpResponse("<h1>Данной страницы нет на сайте!</h1>")