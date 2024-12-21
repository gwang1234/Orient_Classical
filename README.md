## 동양 고전 번역 & 데이터 분석 프로젝트 (with 장고)

<br><br>

### 장고 튜토리얼
[장고 튜토리얼](https://docs.djangoproject.com/en/5.1/)

<br>

장고 설치
```
pip install django
py -m django --version # 설치 확인
django-admin startproject mysite # mysite라는 장고 프로젝트 생성
rename mysite tutorial1 # 패키지 이름 바꾸기
```

<br>

### 장고 패키지
- manage.py: 커맨드라인의 유틸리티

- mysite/: 파이썬 패키지들

- mysite/\_\_init__.py: 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

- mysite/settings.py: Django 프로젝트의 환경 및 구성

- mysite/urls.py: Django project 의 URL 선언 저장. `urlconf`다.

- mysite/asgi.py

- mysite/wsgi.py

<br>

### 프로젝트와 앱
- 앱은 단위 작업을 수행하는 웹 애플리케션이다
- 프로젝트는 특정 웹사이트 그 자체, 앱들의 모음이다
- 하나의 앱은 여러프로젝트에 있을 수 있다(재사용)

<br>

polls라는 앱 만드는 명령어
```
py manage.py startapp polls
```

