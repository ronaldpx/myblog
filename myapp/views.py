from django.shortcuts import render, HttpResponse, get_object_or_404 
from .models import Post
def inicio(request):
    return render(request,'css/inicio.html')

def publicaciones(request):
    datos= Post.objects.all()
    return render(request,'css/publicaciones.html',{'datos':datos})

def detalles(request,id):
    datos= get_object_or_404(Post,id=id)
    return render(request,'css/detalle.html',{'datos':datos})

# Create your views here.
