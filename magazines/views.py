from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Magazine

# Create your views here.
# http://127.0.0.1:8000/
def index(request):
    magazines= Magazine.objects.all()
    context = {
        'magazines' : magazines
    }
    return render(request, 'magazines/list.html', context)

def detail(request, magazine_id):

    magazine = get_object_or_404(Magazine, pk = magazine_id)
    context = {
        'magazine': magazine

    }
    return render(request, 'magazines/detail.html',context) 

def search(request):
    return render(request, 'magazines/search.html')  