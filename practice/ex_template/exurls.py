from django.urls import path

app_name = 'ex_template'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]