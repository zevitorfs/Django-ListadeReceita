from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME1 22')

def sobre(request):
    return HttpResponse("Sobre")
# Create your views here.
