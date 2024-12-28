from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def index(request):
    now = timezone.now()
    print("현재 시간: ",now)
    return render(request, "ex_view/index.html", {'now':now})