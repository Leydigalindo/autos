from multiprocessing import context
from django.views.generic import View
from django.shortcuts import render
from django.views.defaults import page_not_found
def home(request):
    context={}
    return render(request, 'pages/index.html', context)

def manual(request):
    context= {}
    return render(request, 'help.html', context)
def error_404(request, exception):
    return render(request, '404.html')