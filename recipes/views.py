from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #Função para localiza os documentos html
    return render(request, 'home.html')

def sobre(request):
    return HttpResponse("Sobre")
# Create your views here.
