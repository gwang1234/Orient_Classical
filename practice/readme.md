# 장고 개념 타파

<br>

## 25년 1월 2일

<br>

ㄹㄹ

<br>

## 24년 12월 28일

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

<div style="width: 100%; height: 1px; background-color: #444;"></div>

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

##### setting에 앱 등록
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ex_view.apps.ExViewConfig', # 앱 등록
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
<div style="width: 100%; height: 1px; background-color: #444;"></div>

<br>

- 세션은 각 브라우저들을 구분하기 위해 클라이언트에 전달됨
- 클라이언트에 전달된 세션은 쿠키로 저장 
- render로 템플릿 뷰를 보여줄때, 전달할 값은 딕셔너리 형태로 전달 
- post 방식으로 전달할때, 파라미터로 전달 안됨 

### csrf
- post 방식으로 전달할때 403오류, csrf 검증에 실패했다고 뜸
- 장고는 폼에 `csrf 토큰을 증명`할 수 있는 값을 포함하게 해야지 폼 정상 전달 
- 폼마다 토큰 값이 달라짐