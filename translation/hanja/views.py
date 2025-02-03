from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader
import re
from .models import Hanja
from collections import Counter
import io

import matplotlib
matplotlib.use("Agg")
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Image, Spacer
from reportlab.lib.units import cm

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from urllib.parse import unquote

# Create your views here.
def index(request):
    return render(request, 'hanja/main.html')




# pdf 규격 정의
def pdf_frame():

    return Frame(
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




# pdf 번역 생성
def pdf_generation(L: list):
    doc = BaseDocTemplate(str('7 술이.pdf'), pagesize=A4)
    frontpage = PageTemplate(id='FrontPage',
                                frames=[pdf_frame()]
                    )
    doc.addPageTemplates(frontpage)
    doc.build(L)



# 도넛 그래프 생성 
def pie_graph(df: pd.DataFrame):
    
    labels = df['한자']
    frequency = df['빈도수']
    
    fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
    fig.set_facecolor('white')
    ax = fig.add_subplot()
    
    pie = ax.pie(frequency, ## 파이차트 출력
    startangle=90, ## 시작점을 90도(degree)로 지정
    counterclock=False, ## 시계 방향으로 그린다.
    autopct=lambda p : '{:.2f}%'.format(p), ## 퍼센티지 출력
    wedgeprops=dict(width=0.5) ## 중간의 반지름 0.5만큼 구멍을 뚫어준다.
    )
    
    
    font_path = "C:/Windows/Fonts/malgun.ttf"  # 'Malgun Gothic' 폰트 경로
    font_prop = fm.FontProperties(fname=font_path)
    plt.title("한자 빈도수", fontproperties=font_prop, fontsize=20)
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.legend(pie[0],labels) ## 범례 표시
    
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight')
    img_buffer.seek(0)
    return img_buffer



# pdf 데이터분석 생성 
def pdf_generation(L, df: pd.DataFrame):
    
    img_buffer = pie_graph(df)
    img = Image(img_buffer, width=400, height=400)
        
    doc = BaseDocTemplate(str('데이터분석.pdf'), pagesize=A4)
    frontpage = PageTemplate(id='FrontPage', frames=[pdf_frame()])
    doc.addPageTemplates(frontpage)
    
    elements = []  # PDF에 추가할 요소 리스트
    elements.append(img)
    elements.append(Spacer(1, 20))  # 20pt 간격 추가
    for text in L:
        elements.append(Paragraph(text, ParagraphStyle(name='fd',fontName='맑은고딕',fontSize=11,leading=20)))
    doc.build(elements)  # PDF 생성
    
    img_buffer.close()




# 번역 함수
def traslation(request):
    
    # 폰트 지정 
    pdfmetrics.registerFont(TTFont("맑은고딕", "malgun.ttf"))
    
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
                only_hanja = re.sub(r'[A-z가-힣0-9\s~"!@#$%^&*()_+=\-:;,.<>?/|\\{}[\] ]', '', line)
                if line.strip() == "":
                    continue
                    # L.append(Spacer(1, 20))
                elif unquote(line) == "\u200B":
                    L.append(Spacer(1, 20))
                else:
                    if (only_hanja == ""):
                        L.append(Paragraph(line, ParagraphStyle(name='fd',fontName='맑은고딕',fontSize=11,leading=20)))
                        L.append(Spacer(1, 20))
                    else:
                        L.append(Paragraph(line, ParagraphStyle(name='fd',fontName='맑은고딕',fontSize=11,leading=20)))
                        analysis = "[ "
                        
                        for hanja in only_hanja:
                            try:
                                hanja_entry = Hanja.objects.get(hanja=hanja).mean
                                analysis += "( " + hanja + ": " + hanja_entry + ") "
                                
                            except Hanja.DoesNotExist:
                                print("한자명:" + hanja)
                                
                                driver = webdriver.Chrome()
                                driver.get(f'https://hanja.dict.naver.com/#/search?query={hanja}')
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
                        # L.append(Spacer(1, 20))
            
        pdf_generation(L)




# 한자 분석 
def hanja_analysis(request):
    pdfmetrics.registerFont(TTFont("맑은고딕", "malgun.ttf"))
    
    M=[]
    L=[]
    
    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf = request.FILES.get("pdf")
        reader = PdfReader(pdf)
        pages = reader.pages
        
        for page in pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                # 한글, 숫자, 영어, 특수문자 제거
                hanjas = re.sub(r'[A-z가-힣0-9\s~"!@#$%^&*()_+=\-:;,.<>?/|\\{}[\] ]', '', line)
                for hanja in hanjas:
                    M.append(hanja)
        
        count = Counter(M)
        sorted_desc = sorted(count.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_desc) > 20:
            sorted_desc = sorted_desc[:20]
        df = pd.DataFrame(sorted_desc, columns=['한자', '빈도수'])
        
        
        for i in range(1, len(sorted_desc)+1):
            hanja = sorted_desc[i-1][0]
            mean = ""
            try:
                mean = Hanja.objects.get(hanja=hanja).mean
            except Hanja.MultipleObjectsReturned:
                mean = Hanja.objects.filter(hanja=hanja).first().mean
            except Hanja.DoesNotExist:
                driver = webdriver.Chrome()
                driver.get(f'https://hanja.dict.naver.com/#/search?query={hanja}')
                WebDriverWait(driver, 60).until(
                    ec.presence_of_element_located((By.CSS_SELECTOR, '#searchLetterPage_content'))
                )
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                
                mean = soup.select_one(".mean").text.strip()
                stroke = soup.find('div', string='총 획수').find_next_sibling().text.split("획")[0]
                
                Hanja.objects.create(hanja=hanja, mean=mean, stroke=stroke)
            texts = str(i)+"위  " + hanja+": " + mean
            L.append(texts)
            
        pdf_generation(L, df)




# pdf 업로드 
def upload_pdf(request):
    # traslation(request)
    hanja_analysis(request)
    return HttpResponse("fdgdf")
