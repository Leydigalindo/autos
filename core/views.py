from multiprocessing import context
from django.views.generic import View
from django.shortcuts import render

def home(request):
    context={}
    return render(request, 'pages/index.html', context)

def manual(request):
    context= {}
    return render(request, 'help.html', context)
