#  직독 한문 번역

<br>

> 개인 프로젝트  
> 개발기간: 2025.01.24 ~ 

<br>

<img src="./hanja/static/img/site.png" width="1000" height="auto">

<br>

### 프로젝트 소개
- 한자가 포함된 PDF 파일을 한 줄씩 번역하여 번역된 PDF 파일로 생성한 후 사용자에게 제공합니다.
- PDF 파일의 한자 빈도수를 분석하여 외워야 할 순위, 빈도 그래프를 PDF로 제공합니다.
- 한자번역, 한자분석을 체크박스로 선택하여 원하는 PDF를 받을 수 있습니다.
- 상용한자 1800제로 게임을 하여 한자를 쉽게 익힐 수 있습니다.

### 개발환경
- 백엔드: python 3.12.8, Django 5.1.4, Mysql 8.0.36
- 프론트: HTML/CSS, JS
- 형상관리: Github

### 프로젝트 구조
```
│   db.sqlite3
│   manage.py
│   readme.md
│
├───hanja
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-312.pyc
│   │
│   ├───static
│   │   ├───css
│   │   │       header.css
│   │   │       main.css
│   │   │
│   │   └───img
│   │           hanji.png
│   │           site.png
│   │
│   ├───templates
│   │   └───hanja
│   │           header.html
│   │           main.html
│   │
│   └───__pycache__
│
└───mysite
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───__pycache__

```

<br><br>

### 트러블 슈팅 

<br>

`오류`
```
RuntimeError: main thread is not in main loop
```
- 문제 원인
  - Matplotlib은 GUI 창을 띄우는 기능을 포함하고 있다.
  - GUI는 메인스레드에서 실행되어야만 함
  - GUI는 한 번에 하나의 작업만 실행할 수 있으며, 만약 다른 스레드에서 GUI를 변경하려고 하면 비정상적인 동작, 오류 발생
  - Python이라는 멀티스레드 환경에서 **메인스레드가 아닌 곳에 실행되어** 오류 발생

- 문제 해결
  - plt.show() 기능을 사용하지 않기 때문에 Matplotlib의 백엔드 환경을 Agg(그래프를 파일로 저장)로 설정

  - ```
    import matplotlib
    matplotlib.use('Agg')
    ```

<br>

`오류`
```
ValueError: Length of values (20) does not match length of index (2)
```
문제 원인
  - 데이터를 가져오는데 **(objdects.get()) 결과값이 2개 이상**일때 나타나는 오류 
  - 분명 한자데이터를 저장하기 전, 판다스로 중복값을 다 제거했고 결과를 확인했다. 그런데 이런 오류가 나와 당황스러웠다.
  - ```
    eigenvalue = df.drop_duplicates(subset=['hanja'], keep="first")
    eigenvalue[eigenvalue.duplicated(subset=['hanja'])]
    ```
  - 판다스가 중복값을 완전히 제거하지 못하나 보다.


문제 해결 
  - fillter 활용: objects.filter(hanja=hanja).first()
  - 예외 처리: except Hanja.MultipleObjectsReturned:

<br>

`오류`
```
django.db.utils.OperationalError: (1054, "Unknown column 'hanja.id' in 'field list'")
```
문제 원인
  - hanja 테이블에 id필드를 만들지 않아 발생한 오류

문제 해결
  - 마이그레이션 초기화 + 한자테이블 id 생성후 마이그레이션 