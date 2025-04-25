from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout



def user_login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        check = auth.authenticate(request,username=usuario, password=senha)

        if check is None:
            messages.info(request,'Nome de Usuário ou senha inválidos')
            return redirect('login')
        else:
            login(request, check)
            return redirect('index')
    else:
        return render(request,'login.html')

def logout(request):
    django_logout(request)
    return redirect('login')

def adc_conta(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        repeat_senha = request.POST.get('repeat_senha')

        usuarios = User.objects.all()


        for sla in usuarios:
            if sla.username == usuario:
                messages.info(request,'Nome de usuário já está sendo usado')
                return redirect('cadastro')
            elif senha != repeat_senha:
                messages.info(request,'as senha informadas são diferentes')
                return redirect('cadastro')
            elif usuario == '' or senha == '' or repeat_senha == '':
                messages.info(request,'Preencha todos os campos para efetuar o Cadastro')
                return redirect('cadastro')
            else:
                user = User.objects.create_user(usuario, password=senha)
                user.save()
                return redirect('index')
    else:

        return render(request,'cadastro.html')


'''def trocar_senha(request):
    if request.method == 'POST':
        senha = request.POST.GET('senha')
        repeat_senha = request.POST.GET('repeat_senha')

        id_do_usuario = request.usuario.id
        usuario = User.objects.GET(id=id_do_usuario)

        if senha == repeat_senha:
            usuario.set_password(senha)
            usuario.save()
            return redirect('index')
        else:
            return redirect ('trocarsenha')'''





