from django.shortcuts import render
from django.http import HttpResponse
from sports.models import Sports
from blog.models  import Post

# Create your views here.
def sports(request):
    posts = Sports.objects.all()
    data = {
        'posts' : posts
    }
    return render(request,'sports.html',data)

def detail(request,id):
    list = Sports.objects.get(id = id)
    items = Sports.objects.all()
    print(items)
    blog ={
        'list':list,
        'items':items
    }
    return render(request,'detail.html',blog)
   