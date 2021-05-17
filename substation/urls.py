from django.urls import path

from substation.views import TestingHome, about, AddPage, contact, login, TestingCategory, ShowPost

urlpatterns = [
    path('', TestingHome.as_view(), name="home"),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name="add_page"),
    path('contact/', contact, name="contact"),
    path('login/', login, name="login"),
    # path('post/<int:post_id>', show_post, name="post"),
    path('post/<slug:post_slug>', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>', TestingCategory.as_view(), name="category")
]