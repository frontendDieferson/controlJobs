from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.

def cadastro(request):
    if request.method == "GET":
      if request.user.is_authenticated:
        return redirect('/jobs')
      return render(request, 'cadastro.html')
    elif request.method == "POST":
      username = request.POST.get('username')
      senha = request.POST.get('password')
      confirmar_senha = request.POST.get('confirm-password')

      if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas não coicidem')
        return redirect('/auth/cadastro')

      if len(username.strip()) == 0 or len(senha.strip()) ==0:
        messages.add_message(request, constants.WARNING, 'Preencha todos os campos')
        return redirect('/auth/cadastro')

      user = User.objects.filter(username=username)

      if user.exists():
        messages.add_message(request, constants.INFO, 'Já existe um usuário com esse username')
        return redirect('/auth/cadastro')

      try:
        
        user = User.objects.create_user(username=username, password=senha)

        user.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
        return redirect('/auth/login')
      except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/auth/cadastro')




def login(request):
    if request.method == "GET":
      if request.user.is_authenticated:
        return redirect('/perfil')        
      return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
      

        usuario = auth.authenticate(username=username, password=senha)

          
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/jobs/perfil')

def logout(request):
  auth.logout(request)
  return redirect('/auth/login')