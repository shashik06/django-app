from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from sports.models import Sports

# Create your views here.
def home(request):
    postData = Post.objects.all()
    data = {
            'postData' : postData
        }
    return render(request, 'index.html',data)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def post(request,id):
    post = Post.objects.get(id = id)
    data = Post.objects.all()
    item = {
        'post' : post,
        'data' : data,
    }
    return render(request,'post.html',item)

