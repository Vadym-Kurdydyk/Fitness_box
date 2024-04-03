from email import message
from mailbox import MMDFMessage, Message
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Topic, Message
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from base.api.permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/topics/'
    ]
    return Response(routes)

class RoomList(APIView):
    '''
    List all rooms, or create a new rooms.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self,request,format = None):
        rooms = Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many = True)
        return Response(serializer.data)
    def post(self, request, format = None):
        serializer = serializers.RoomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RoomDetail(APIView):
    '''
    Retrieve, update or delete a room instance.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self,pk):
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        room = Room.objects.get(id=pk)
        serializer = serializers.RoomSerializer(room, many = False)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        room = Room.objects.get(id=pk)
        serializer = serializers.RoomSerializer(room,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        room = Room.objects.get(id=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class TopicList(APIView):
    '''
    List all topics, or create a new topic.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, format = None):
        topics = Topic.objects.all()
        serializer = serializers.TopicSerializer(topics, many = True)
        return Response(serializer.data)
    def post(self, request, format = None):
        serializer = serializers.TopicSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesList(APIView):
    '''
    List all messages, or create a new message.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, format = None):
        messages = Message.objects.all()
        serializer = serializers.MessageSerializer(messages, many = True)
        return Response(serializer.data)
    def post(self, request, format = None):
        serializer = serializers.MessageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MessagesDetail(APIView):
    '''
    Retrieve, update or delete a message instance.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self,pk):
        try:
            message = Message.objects.get(id=pk)
        except Message.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        message = Message.objects.get(id=pk)
        serializer = serializers.MessageSerializer(message, many = False)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        message = Message.objects.get(id=pk)
        serializer = serializers.MessageSerializer(message,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        message= Message.objects.get(id=pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
