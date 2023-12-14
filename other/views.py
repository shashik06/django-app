from django.shortcuts import render
from other.models import other

def movies(request):
    return render(request,'movies.html')
def business(request):
    item = other.objects.filter(tags='Business').exclude(tags='Technology')
    data = {
        'item':item
    }
    return render(request,'business.html',data)
def tech(request):
    list = other.objects.filter(tags='Technology').exclude(tags='Business')
    data = {
        'list':list
    }
    return render(request,'tech.html',data)
def movies(request):
    return render(request,'movies.html')
def list(request,id):
    lst = other.objects.get(id = id)
    blog = other.objects.all()
    print(blog)
    items = {
        'lst':lst,
        'blog':blog
        
    }
    return render(request,'list.html',items)