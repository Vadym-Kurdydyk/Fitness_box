from email.policy import default
from rest_framework import serializers
from base.models import Room, Topic, Message

class CurrentUserDefault:
    """
    Returns the current user.
    """
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user
    
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    host = serializers.StringRelatedField(many = False,read_only = True, default = CurrentUserDefault)
    topic = TopicSerializer(many = False, read_only = True)
    participants = serializers.StringRelatedField(many = True)
    highlight = serializers.HyperlinkedIdentityField(view_name='room-highlight', format='html')
    class Meta:
        model = Room
        fields = '__all__'
        

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False,read_only = True, default = CurrentUserDefault)
    room = serializers.StringRelatedField(many = False, read_only = True)
    class Meta:
        model = Message
        fields = '__all__'