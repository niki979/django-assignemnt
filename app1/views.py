from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
from django.http import JsonResponse
import os
# Create your views here.


'''
def index(request):
    sleepy.delay(10)
    return render(request,'template.html')
'''

def index(request):
    
    if request.method == 'POST':
        #path = request.POST['csv_path']
        path = request.POST.get('csv_path', '')
        
        result = read_csv.apply_async(args=[path])
        result2 = display_csv.apply_async(args=[path])
        
        return render(request, 'template.html',{'result': result.get(),'result2':result2.get()})
    else:
        return render(request, 'template.html')
    

