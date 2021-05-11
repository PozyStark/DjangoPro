from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from substation.forms import *
from substation.models import *


def index(response):
    posts = Testing.objects.all()

    context = {'title': 'Главная страница',
               'posts': posts,
               'cat_selected': 0}
    return render(response, 'substation/index.html', context)


def about(response):
    return render(response, 'substation/about.html', {'title': 'О нас'})


def add_page(response):
    if response.method == 'POST':
        form = AddPostForm(response.POST, response.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                # Testing.objects.create(**form.cleaned_data)
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(response, 'substation/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(response):
    return HttpResponse("contact")


def login(response):
    return HttpResponse("login")


def show_post(response, post_slug):
    post = get_object_or_404(Testing, slug=post_slug)
    context = {'title': post.title,
               'post': post,
               'cat_selected': post.cat_id}
    return render(response, 'substation/post.html', context=context)


def show_category(response, cat_id):
    posts = Testing.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'title': 'Отображение по рубрикам',
               'posts': posts,
               'cat_selected': cat_id}

    return render(response, 'substation/index.html', context)


def page_not_found(response, exception):
    return HttpResponse("<h1>Данной страницы нет на сайте!</h1>")