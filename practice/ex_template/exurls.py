from django.urls import path

app_name = 'ex_template'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ex01/', views.ex01, name='ex01'),
    path('ex02/', views.ex02, name='ex02'),
]