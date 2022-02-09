from django.shortcuts import render
from django.http import HttpResponse
import magazines
from magazines.models import Magazine

# Create your views here.
# http://127.0.0.1:8000/
def index(request):  
    magazines= Magazine.objects.all().order_by('-created_date')
    context = {
        'magazines' : magazines
    }
    return render(request, 'pages/index.html', context)
    

def about(request):
    return render(request, 'pages/about.html') 

def contact(request):
    return render(request, 'pages/contact.html')  

def news(request):
    return render(request, 'pages/news.html') 