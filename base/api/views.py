from email import message
from mailbox import MMDFMessage, Message
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room, Topic, Message
from . import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from base.api.permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnly_user
from rest_framework import mixins, generics, permissions, renderers, status
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

@api_view(['GET'])
def api_root(request, format = None):
    routes = {
        'rooms': reverse('room-list', request=request, format=format),
        'topics': reverse('topic-list',request=request,format=format),
        'messages': reverse('message-list', request=request,format=format),
        'users': reverse('user-list', request=request, format=format)
    }
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
     
class RoomHighlight(generics.GenericAPIView):
    queryset = Room.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        room = self.get_object()
        return Response(room)
    
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
     

    
class UserList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    '''
    List all users, or create a new user.
    '''
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class UserDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    '''
    Retrieve, update or delete a user instance.
    '''
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly_user]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)