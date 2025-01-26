from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'hanja/main.html')

def upload_pdf(request):
    print('ssssssssssss')
    return HttpResponse("fdgdf")
