## ���� ���� ���� & ������ �м� ������Ʈ (with ���)

<br><br>

### ��� Ʃ�丮��
[��� Ʃ�丮��](https://docs.djangoproject.com/en/5.1/)

<br>

��� ��ġ
```
pip install django
py -m django --version # ��ġ Ȯ��
django-admin startproject mysite # mysite��� ��� ������Ʈ ����
rename mysite tutorial1 # ��Ű�� �̸� �ٲٱ�
```

<br>

### ��� ��Ű��
- manage.py: Ŀ�ǵ������ ��ƿ��Ƽ

- mysite/: ���̽� ��Ű����

- mysite/\_\_init__.py: �� ���丮�� ��Ű��ó�� �ٷ��� �˷��ִ� �뵵�� �ܼ��� �� ����

- mysite/settings.py: Django ������Ʈ�� ȯ�� �� ����

- mysite/urls.py: Django project �� URL ���� ����. `urlconf`��.

- mysite/asgi.py

- mysite/wsgi.py

<br>

### ������Ʈ�� ��
- ���� ���� �۾��� �����ϴ� �� ���ø��ɼ��̴�
- ������Ʈ�� Ư�� ������Ʈ �� ��ü, �۵��� �����̴�
- �ϳ��� ���� ����������Ʈ�� ���� �� �ִ�(����)

<br>

polls��� �� ����� ��ɾ�
```
py manage.py startapp polls
```

