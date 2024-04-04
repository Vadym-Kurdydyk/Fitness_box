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
from rest_framework import mixins
from rest_framework import generics


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        'GET /api/topics/'
    ]
    return Response(routes)

class RoomList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    '''
    List all rooms, or create a new room.
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RoomDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    '''
    Retrieve, update or delete a room instance.
    '''
    queryset = Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
     

class TopicList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    '''
    List all topics, or create a new topic.
    '''
    queryset = Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MessagesList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    '''
    List all messages, or create a new message.
    '''
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class MessagesDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    '''
    Retrieve, update or delete a message instance.
    '''
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
     

    
