from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    return render(request, 'generator/index.html')

def password(request):
    return render(request,'generator/password.html')
    
    
