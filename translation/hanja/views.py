from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader, PdfWriter
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Create your views here.
def index(request):
    return render(request, 'hanja/main.html')

def upload_pdf(request):

    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf_file = request.FILES.get('pdf')
        reader = PdfReader(pdf_file)
        
        pages = reader.pages
        for page in pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                # 한글, 숫자, 영어, 특수문자 제거
                only_hanja = re.sub(r'[A-z가-힣0-9\s!@#$%^&*()_+=\-:;,.<>?/|\\{}[\] ]', '', line)
                if (only_hanja == ""):
                    continue
                else:
                    print(only_hanja)
            
        
    
    return HttpResponse("fdgdf")
