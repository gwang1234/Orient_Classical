from django.shortcuts import render 
from django.utils import timezone

def index(request):
    now = timezone.now()
    context = {
        'now' : now,
        'name' : '홍길동',
    }
    return render(request, 'index.html', context)