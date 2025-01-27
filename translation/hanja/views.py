from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader, PdfWriter

# Create your views here.
def index(request):
    return render(request, 'hanja/main.html')

def upload_pdf(request):
    hanja = {'學' : 1,'而' : 2,'編' : 3}
    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf_file = request.FILES.get('pdf')
        reader = PdfReader(pdf_file)
        
        page = reader.pages[0]
        text = page.extract_text()
        lines = text.split('\n')
            
        for line in lines:
            print(line)
            
        print(lines[1])
        
    
    return HttpResponse("fdgdf")
