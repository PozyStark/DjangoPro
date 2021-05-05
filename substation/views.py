from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from substation.models import Testing

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(response):
    posts = Testing.objects.all()
    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts}
    return render(response, 'substation/index.html', context)


def about(response):
    return render(response, 'substation/about.html', {'title' : 'О нас', 'menu': menu})


def add_page(request):
    return HttpResponse("add_page")


def contact(request):
    return HttpResponse("contact")


def login(request):
    return HttpResponse("login")


def show_post(request, post_id):
    return HttpResponse(f"Post id_{post_id}")


def pageNotFound(response, exception):
    return HttpResponse("<h1>Данной страницы нет на сайте!</h1>")