from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def index(request):
    now = timezone.now()
    print("현재 시간: ",now)
    print(reverse('exview:index'))
    print(reverse('exview:get1'))
    print(reverse('exview:get2', args=(11,22,'hello')))
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


# 클래스형 뷰 
from django.views.generic import View

class ExamGet3(View):
    def get(self, request):
        print('get3/ 요청이 들어옴 ')
        keys = request.GET.keys()
        for key in keys:
            value = request.GET[key]
            print(f'{key}:{value}')
        
        num = int(request.GET['n1']) + int(request.GET['n2'])
        print(num)
        return HttpResponse('get3')
    
class ExamGet4(View):
    def get(self, request, n1, n2, n3):
        print("n1: ",n1)
        print("n2: ",n2)
        print("n3: ",n3)
        print(n1 + n2)
        return HttpResponse('get4')
    
class ExamPost3(View):
    def post(self, request):
        keys = request.POST.keys()
        for key in keys:
            value = request.POST[key]
            print(f'{key}:{value}')
        
        num = int(request.POST['n1']) + int(request.POST['n2'])
        print(num)
        return HttpResponse('post3')
    
class ExamPost4(View):
    def post(self, request, msg, n):
        print("msg: ", msg)
        print("n: ", n)
        keys = request.POST.keys()
        for key in keys:
            value = request.POST[key]
            print(f'{key}:{value}')
        return HttpResponse('post4')
    
class ExamGetPost(View):
    def get(self, request):
        print("get요청 동작")
        return HttpResponse('getpost2/(get)')
    
    def post(self, request):
        print("Post요청 동작")
        user = request.POST['user']
        pwd = request.POST['pwd']
        if user == pwd:
            print('로그인 성공')
            return HttpResponse('getpost2/(Post)')
        else:
            print('로그인 실패')
            # return HttpResponseRedirect('/ex_view/')
            return HttpResponseRedirect(reverse('exview:index'))