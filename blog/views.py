from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.defaults import page_not_found



@login_required(login_url='/ingresar')
def post_list(request):
    posts = Post.objects.all
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_list_alumnos(request):
    posts = Post.objects.all().filter(chismes_de="Alumno")
    return render(request, 'blog/alumnos.html', {'posts': posts})

def post_list_profesores(request):
    posts = Post.objects.all().filter(chismes_de="Profesor")
    return render(request, 'blog/profesores.html', {'posts': posts})

def post_list_otros(request):
    posts = Post.objects.all().filter(chismes_de="Otros")
    return render(request, 'blog/otros.html', {'posts': posts})



def post_list_privado(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/post_list_privado.html', {'posts': posts})

def post_list_mejores_semanales(request):
    posts = Post.objects.all
    return render(request, 'blog/mejores_semanales.html', {'posts': posts})

def post_list_mejores_mensuales(request):
    posts = Post.objects.all
    return render(request, 'blog/mejores_mensuales.html', {'posts': posts}) 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('listado')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('listado')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




def nuevo_usuario(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('blog/nuevousuario.html', {'form': form}, context_instance=RequestContext(request))


def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso) 
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('blog/ingresar/noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('blog/nousuario.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('blog/ingresar.html', {'form': form}, context_instance=RequestContext(request))


@login_required (login_url='/ingresar')
def privado (request):
    usuario = request.user
    return render_to_response('blog/privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar (request):
    logout (request)
    return HttpResponseRedirect('/')

def post_detail_privado(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail_privado.html', {'post': post})




