from django.shortcuts import render

# Create your views here.

def home_view (request):
    context = {
        'titulo': 'Título Teste',
        'mensagem': 'teste view'
    }
    
    return render(request, 'base.html', context)