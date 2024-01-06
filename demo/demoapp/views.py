from django.shortcuts import render
from django.http import HttpResponse
from .models import place

# Create your views here.
def index(req):
    data=place.objects.all()
    return render(req,'index.html',{'data':data})



def contact(req):
    return render(req,'contact.html')

def destinations(req):
    return render(req,'destinations.html')
def elements(req):
    return render(req,'elements.html')
def news(req):
    return render(req,'news.html')
