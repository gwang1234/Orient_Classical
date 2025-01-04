from django.urls import path

from . import views

app_name='exview'

urlpatterns = [
    # 함수형 뷰
    path('',views.index, name='index'),
    path('get1/', views.get1, name='get1'),
    path('get2/<int:n1>/<int:n2>/<str:n3>/', views.get2, name='get2'),
    path('post1/', views.post1),
    path('post2/<str:msg>/<int:n>/', views.post2),
    path('getpost1/', views.getpost1),
    
    # 클래스형 뷰
    path('get3/', views.ExamGet3.as_view()),
    path('get4/<int:n1>/<int:n2>/<str:n3>/', views.ExamGet4.as_view()),
    path('post3/', views.ExamPost3.as_view()),
    path('post4/<str:msg>/<int:n>/', views.ExamPost4.as_view()),
    path('getpost2/', views.ExamGetPost.as_view()),
]