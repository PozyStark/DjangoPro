from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from substation.models import Testing, Category


def index(response):
    posts = Testing.objects.all()

    context = {'title': 'Главная страница',
               'posts': posts,
               'cat_selected': 0}
    return render(response, 'substation/index.html', context)


def about(response):
    return render(response, 'substation/about.html', {'title': 'О нас'})


def add_page(response):
    return HttpResponse("add_page")


def contact(response):
    return HttpResponse("contact")


def login(response):
    return HttpResponse("login")


def show_post(response, post_id):
    return HttpResponse(f"Post id_{post_id}")


def show_category(response, cat_id):
    posts = Testing.objects.filter(cat_id=cat_id)

    context = {'title': 'Отображение по рубрикам',
               'posts': posts,
               'cat_selected': cat_id}

    return render(response, 'substation/index.html', context)


def page_not_found(response, exception):
    return HttpResponse("<h1>Данной страницы нет на сайте!</h1>")