from django.urls import path

from substation.views import index, number

urlpatterns = [
    path('', index, name="home"),
    path('number/<int:num>', number)
]