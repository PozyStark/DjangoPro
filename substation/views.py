from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from substation.forms import *
from substation.models import *
from .utils import *

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


class TestingHome(DataMixin, ListView):
    model = Testing
    template_name = 'substation/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Testing.objects.filter(is_published=True)

# def index(response):
#     posts = Testing.objects.all()
#
#     context = {'title': 'Главная страница',
#                'posts': posts,
#                'cat_selected': 0}
#     return render(response, 'substation/index.html', context)


def about(response):
    return render(response, 'substation/about.html', {'title': 'О нас'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'substation/addpage.html'
    success_url = reverse_lazy('home')
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


# def add_page(response):
#     if response.method == 'POST':
#         form = AddPostForm(response.POST, response.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             try:
#                 # Testing.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(response, 'substation/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(response):
    return HttpResponse("contact")


def login(response):
    return HttpResponse("login")


class ShowPost(DataMixin, DetailView):
    model = Testing
    template_name = 'substation/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = context['post']
        c_def = self.get_user_context(title=context['post'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# def show_post(response, post_slug):
#     post = get_object_or_404(Testing, slug=post_slug)
#     context = {'title': post.title,
#                'post': post,
#                'cat_selected': post.cat_id}
#     return render(response, 'substation/post.html', context=context)


class TestingCategory(DataMixin, ListView):
    model = Testing
    template_name = 'substation/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Категория-' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Testing.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(response, cat_id):
#     posts = Testing.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {'title': 'Отображение по рубрикам',
#                'posts': posts,
#                'cat_selected': cat_id}
#
#     return render(response, 'substation/index.html', context)


def page_not_found(response, exception):
    return HttpResponse("<h1>Данной страницы нет на сайте!</h1>")