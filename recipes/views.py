from django.shortcuts import render

def home(request):
    #Função para localiza os documentos html
    return render(request, 'recipes/pages/home.html')

#Não esqueça de por o paramentro aqui tambem
def recipes(request, id):
    #Função para localiza os documentos html
    return render(request, 'recipes/pages/home.html')
