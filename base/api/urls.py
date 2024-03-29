from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    
    path('rooms/', views.room_list),
    path('rooms/<str:pk>/', views.room_detail),
    
    path('topics/', views.topic_list),
    
    #  path('messages/', views.getMessages),
    
    
]
