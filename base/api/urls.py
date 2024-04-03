from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.getRoutes),
    
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<str:pk>/', views.RoomDetail.as_view()),
    
    path('topics/', views.TopicList.as_view()),
    
    path('messages/', views.MessagesList.as_view()),
    path('messages/<str:pk>/', views.MessagesDetail.as_view()),
    
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
