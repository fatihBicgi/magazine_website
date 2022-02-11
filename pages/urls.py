from django.urls import URLPattern, path
from . import views

#http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_about', views.contact_about, name='contact_about'),
    path('news', views.news, name='news'),

]



