from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ex_template/index.html')

def ex01(request):
    n1 = 100
    lst = [1,2,3]
    tup = (4,5,6)
    dic = {'a':1, 'b':2, 'c':3}
    
    context = {
        'n1' : n1,
        'lst' : lst,
        'tup' : tup,
        'dic' : dic,
    }
    
    return render(request, 'ex_template/ex01.html', context)

def ex02(request):
    val1 = 'hello<world><br>'
    lst = [ 'h0', 'Hi', 'weLCome']
    tup = (1,2,3)
    dic = {'aa':10, 'bb':20, 'cc':30, }
    bio = 'hi1 hi2 hi3 hi4 hi5 hi6 hi7 hi8 hi9 hi10'
    ls = [100]
    lss = [100, 200]
    data = { 'val1': val1, 'lst':lst, 'tup':tup, 'dic':dic, 
            'bio':bio, 'ls':ls, 'lss':lss }
    return render(request, 'ex_template/ex02.html', data)