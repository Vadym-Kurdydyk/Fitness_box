from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    
    path('rooms/', views.RoomList.as_view(), name = 'room-list'),
    path('rooms/<str:pk>/', views.RoomDetail.as_view(), name = 'room-detail'),
    path('rooms/<str:pk>/highlight/', views.RoomHighlight.as_view(),name = 'room-highlight'),
    
    path('topics/', views.TopicList.as_view(),name = 'topic-list'),
    
    path('messages/', views.MessagesList.as_view(), name = 'message-list'),
    path('messages/<str:pk>/', views.MessagesDetail.as_view(), name = 'message-detail' ),
    
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
