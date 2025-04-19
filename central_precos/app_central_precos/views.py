from django.shortcuts import render, redirect
from django.contrib import messages  # messages foi usado na verificação de senha
# Create your views here.

def home_view (request):
    return render(request, 'base.html')

def login_view (request):
    return render(request, 'login.html')

def cadastro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        # Simples verificação de senha
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        # Aqui você pode salvar no banco (User, ou seu próprio model)
        # Exemplo simples: printar os dados
        print(f"Novo usuário: {email}, {cidade}, {estado}")

        return redirect('login')  # Redireciona pro login após cadastro

    return render(request, 'register.html')