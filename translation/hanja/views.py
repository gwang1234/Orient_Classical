from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader
import re
from .models import Hanja

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.units import cm
from reportlab.platypus import Spacer

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from urllib.parse import quote

# Create your views here.
def index(request):
    return render(request, 'hanja/main.html')

def upload_pdf(request):
    
    # 폰트 지정 
    pdfmetrics.registerFont(TTFont("맑은고딕", "malgun.ttf"))

    # 프레임 지정 
    text_frame = Frame(
                x1=2.54 * cm ,  # From left
                y1=2.54 * cm ,  # From bottom
                height=24.16 * cm,
                width=15.92 * cm,
                leftPadding=0 * cm,
                bottomPadding=0 * cm,
                rightPadding=0 * cm,
                topPadding=0 * cm,
                showBoundary=0,
                id='text_frame'
            )
    
    L=[]

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
                if line.strip() == "":
                    continue
                    # L.append(Spacer(1, 20))
                else:
                    if (only_hanja == ""):
                        L.append(Paragraph(line, ParagraphStyle(name='fd',fontName='맑은고딕',fontSize=11,leading=20)))
                    else:
                        L.append(Paragraph(line, ParagraphStyle(name='fd',fontName='맑은고딕',fontSize=11,leading=20)))
                        analysis = "[ "
                        
                        for hanja in only_hanja:
                            try:
                                hanja_entry = Hanja.objects.get(hanja=hanja).mean
                                analysis += "( " + hanja + ": " + hanja_entry + ") "
                                
                            except Hanja.DoesNotExist:
                                if hanja.strip() == "" :
                                    hanja_encoded = quote(hanja)
                                    driver = webdriver.Chrome()
                                    driver.get(f'https://hanja.dict.naver.com/#/search?query={hanja_encoded}')
                                    WebDriverWait(driver, 60).until(
                                        ec.presence_of_element_located((By.CSS_SELECTOR, '#searchLetterPage_content'))
                                    )
                                    
                                    html = driver.page_source
                                    soup = BeautifulSoup(html, 'html.parser')
                                    
                                    mean = soup.select_one(".mean").text.strip()
                                    stroke = soup.find('div', string='총 획수').find_next_sibling().text.split("획")[0]
                                    
                                    analysis += "( " + hanja + ": " + mean + ") " 
                                    Hanja.objects.create(hanja=hanja, mean=mean, stroke=stroke)
                                
                            except Hanja.MultipleObjectsReturned:
                                hanja_entry = Hanja.objects.filter(hanja=hanja).first().mean
                                analysis += "( " + hanja + ": " + hanja_entry + ") "
                        
                        analysis += "]"      
                        L.append(Paragraph(analysis, ParagraphStyle(name='fd',fontName='맑은고딕',fontSize=11,leading=20)))
                        L.append(Spacer(1, 20))
                        
            
        doc = BaseDocTemplate(str('만법전.pdf'), pagesize=A4)
        frontpage = PageTemplate(id='FrontPage',
                                frames=[text_frame]    # 4. 프레임 지정 부분에서 text_frame 생성했음
                    )
        doc.addPageTemplates(frontpage)
        doc.build(L)
    
    return HttpResponse("fdgdf")
