from email import message
from mailbox import Message
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Topic, Message
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/topics/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.RoomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def room_detail(request,pk):
    
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = serializers.RoomSerializer(room, many = False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = serializers.RoomSerializer(room,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = serializers.TopicSerializer(topics, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.TopicSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def messages_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = serializers.MessageSerializer(messages, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.MessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT','DELETE'])
def message_detail(request,pk):
    
    try:
        room = Message.objects.get(id=pk)
    except Room.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = serializers.MessageSerializer(message, many = False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = serializers.MessageSerializer(message, many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
