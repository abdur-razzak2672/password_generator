from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse 
import random

def home(request):
    return render(request, 'generator/index.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz0123456789+-.')
    length = 16
    thepassword = ''
    for x in range(length) :
        thepassword +=  random.choice(characters)


    return render(request,'generator/password.html',{'password' : thepassword })
    
    
