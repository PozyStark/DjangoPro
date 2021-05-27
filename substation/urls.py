from django.urls import path
from django.views.decorators.cache import cache_page

from substation.views import TestingHome, about, AddPage, contact, TestingCategory, ShowPost, RegisterUser, \
    LoginUser, logout_user

urlpatterns = [
    path('', TestingHome.as_view(), name="home"),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name="add_page"),
    path('contact/', contact, name="contact"),
    path('login/', LoginUser.as_view(), name="login"),
    path('loginout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    # path('post/<int:post_id>', show_post, name="post"),
    path('post/<slug:post_slug>', ShowPost.as_view(), name="post"),
    path('category/<slug:cat_slug>', TestingCategory.as_view(), name="category")
]