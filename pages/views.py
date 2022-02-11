from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


import magazines
from magazines.models import Magazine
from magazines.models import Static_Texts

# Create your views here.
# http://127.0.0.1:8000/
def index(request):  
    magazines= Magazine.objects.all().order_by('-created_date')
    context = {
        'magazines' : magazines
    }
    return render(request, 'pages/index.html', context)
    

def contact_about(request):
    texts= Static_Texts.objects.all().order_by('name')
    context = {
        'texts' : texts
    }
    return render(request, 'pages/contact_about.html', context) 

def news(request):
    magazines= Magazine.objects.all().order_by('name')
    context = {
        'magazines' : magazines
    }
    return render(request, 'pages/news.html',context)
