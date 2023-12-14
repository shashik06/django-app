from django.urls import path

from .import views

urlpatterns = [
    path('movies', views.movies, name ='movies'),
    path('business', views.business, name ='business'),
    path('tech', views.tech, name ='tech'),
    path('list/<str:id>',views.list,name='list')
    #path('detail',views.detail),
   # path('detail/<str:id>',views.detail,name = 'detail')

]