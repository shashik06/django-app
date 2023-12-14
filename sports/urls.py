from django.urls import path

from .import views

urlpatterns = [
    path('sports', views.sports, name ='sports'),
    #path('detail',views.detail),
    path('detail/<str:id>',views.detail,name = 'detail')

   
    
]