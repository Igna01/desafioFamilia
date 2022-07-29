from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def template_familia(request):
    hoy = datetime.today().date()
    context ={
        'name': 'Ignacio',  
        'last_name': 'Miranda',
        'day': hoy
    }
    return render(request, 'template_f.html', context=context)gi