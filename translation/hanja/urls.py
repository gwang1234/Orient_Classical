from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
]