from django.urls import URLPattern, path
from . import views

#http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='magazines'),
    path('alfabetik', views.alfabetik, name='alfabetik'),
    path('date', views.date, name='date'),
    path('<int:magazine_id>', views.detail, name='detail'),
    
]