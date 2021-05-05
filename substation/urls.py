from django.urls import path

from substation.views import index, number, about

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name='about'),
    path('number/<int:num>', number)
]