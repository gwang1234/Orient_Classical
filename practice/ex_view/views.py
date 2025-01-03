from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def index(request):
    now = timezone.now()
    print("현재 시간: ",now)
    return render(request, "ex_view/index.html", {'now':now})

def get1(request):
    print(request.GET)
    keys = request.GET.keys()
    for key in keys:
        value = request.GET[key]
        print(f'{key}:{value}')
    
    num = int(request.GET['n1']) + int(request.GET['n2'])
    print(num)
    return HttpResponse('get')

def get2(request, n1, n2, n3):
    print("n1: ",n1)
    print("n2: ",n2)
    print("n3: ",n3)
    print(n1 + n2)
    return HttpResponse('get2')

def post1(request):
    keys = request.POST.keys()
    for key in keys:
        value = request.POST[key]
        print(f'{key}:{value}')
    
    num = int(request.POST['n1']) + int(request.POST['n2'])
    print(num)
    return HttpResponse('post1')

def post2(request, msg, n):
    print("msg: ", msg)
    print("n: ", n)
    keys = request.POST.keys()
    for key in keys:
        value = request.POST[key]
        print(f'{key}:{value}')
    return HttpResponse('post2')

def getpost1(request):
    print(request.method)
    return HttpResponse('getpost1')