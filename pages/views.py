from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse #added
def homePageView(request): #added
    return HttpResponse('Hello, World!') #added