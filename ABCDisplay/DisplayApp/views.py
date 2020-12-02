from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def disp(request):
    return HttpResponse("Hello Charan R")    
