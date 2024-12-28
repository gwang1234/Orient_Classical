from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('클라이언트로부터 요청을 받음')
    return HttpResponse("응답 데이터")