from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Livros,Carrinho, Vote
from django.contrib import messages
import requests

# Create your views here.





def produto(request, id):
    livros = requests.get(f'http://127.0.0.1:8000/livro/').json()

    livro = {}

    for l1 in livros:
        if l1["id"] == id:
            livro = l1

    #livros = get_object_or_404(Livros,id)
    if request.method == 'POST' and "btn-form1" in request.POST:
        rate = request.POST.get('rating')
        avaliacao = Vote.objects.all().filter(usuario = request.user, livros = livros )
        if len(avaliacao) == 0:
            livros.qtd_avaliation += 1 
            livros.aval +=  int(rate)
            livros.total_stars = livros.aval / livros.qtd_avaliation
            livros.media = livros.aval / livros.qtd_avaliation
            livro_media_final = round(livros.media)
            livros.media = livro_media_final
            livros.save()

            avaliacao = Vote.objects.create(usuario = request.user, livros = livros)
            avaliacao.save()

            return render(request, 'produto.html', {'livros':livros})
        
        else:
            messages.info(request,'Você pode avaliar cada livro apenas uma vez')
            return redirect('produto', id)

    elif request.method == 'POST' and "btn-form2" in request.POST:
        quant = request.POST.get('quantidade')
        livros = Carrinho.objects.all().filter(usuario=request.user, livros__id=id)
        if len(livros) == 0:
            tot = 0
            tot += int(quant)
            book=Livros.objects.get(id=id)
            livros = Carrinho.objects.create(usuario=request.user, livros=book, quantidade = quant, total=tot)
            livros.save()
        else:
            livros[0].quantidade += int(quant)
            livros[0].save()
        return redirect('carrinho')
    else:
        return render (request, 'produto.html',{'livros':livro})




def index(request):
    melhores = requests.get('http://127.0.0.1:8000/livro/').json()
    #melhores = Livros.objects.all().order_by('-total_stars')
    paginator=Paginator(melhores,3)
    page=request.GET.get('page')
    melhores=paginator.get_page(page)
    todos = requests.get('http://127.0.0.1:8000/livro/').json()
    #todos = Livros.objects.all()
    paginate=Paginator(todos,6)
    pag=request.GET.get('pag')
    todos=paginate.get_page(pag)
    avaliados = {}
    print(melhores)


    aval=sorted(avaliados)
    print(aval)
    return render(request, 'index.html', {'melhores': melhores, 'todos':todos,'aval':aval})

def deletar(request,id):
    excluir = Carrinho.objects.all().filter(usuario=request.user,livros__id=id)
    excluir.delete()
    return redirect('carrinho')

def checkout(request):
    excluir = Carrinho.objects.all().filter(usuario=request.user)
    excluir.delete()
    return redirect('carrinho')

@login_required(redirect_field_name='/accounts/login/')    
def carrinho(request):
    kart_objects = Carrinho.objects.all().filter(usuario=request.user)
    kart=[]
    for x in kart_objects:
        dic={'usuario':x.usuario,'livros':x.livros,'quantidade':x.quantidade,'total':x.quantidade*x.livros.valor}
        kart.append(dic)
       
    return render(request, 'carrinho.html',{'kart':kart})






