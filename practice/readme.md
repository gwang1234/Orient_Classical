# 장고 개념 타파

<br>

## 12월 28일

<br>

### 기본 설정

###### practice/setting.py
```
DEBUG = True

ALLOWED_HOSTS = []
.
.
.
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```
- 실서비스는 디버그 False, 필요에 따라 외부 호스트 설정
- 시간, 장소 한국으로 변경

<br>

기본 세팅 명령어(쉘)
```
py manage.py migrate
py manage.py createsuperuser
py mange.py startapp 앱이름
```

*****

<br>

### url과 view 흐름

###### ex_url 경로설정
```
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index)
]
```

###### ex_url 뷰 
```
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('클라이언트로부터 요청을 받음')
    return HttpResponse("응답 데이터")
```

###### 루트에서 경로 설정
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex_view/', include('ex_view.exurls')),
]
```