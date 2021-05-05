from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from substation.models import Testing

menu = ['баранина', 'говядина', 'кролик', 'рыба', 'курица', 'свинина']
posts = Testing.objects.all()

def index(response):
    return render(response, 'substation/index.html', {'title': 'Главная страница', 'posts': posts, 'menu': menu})


def about(response):
    return render(response, 'substation/about.html', {'title' : 'О нас', 'posts': posts})


def number(response, num):

    if response.POST:
        print(response.POST)

    if num > 5:
        return redirect("home", permanent=False)

    print('Hello')

    return HttpResponse(f"<h1> Number {num} </h1>")


def pageNotFound(response, exception):
    return HttpResponse("<h1>Данной страницы нет на сайте!</h1>")