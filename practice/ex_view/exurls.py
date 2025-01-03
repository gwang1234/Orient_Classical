from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('get1/', views.get1),
    path('get2/<int:n1>/<int:n2>/<str:n3>/', views.get2),
    path('post1/', views.post1),
    path('post2/<str:msg>/<int:n>/', views.post2),
    path('getpost1/', views.getpost1),
]