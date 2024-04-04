from email.policy import default
from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField
from base.models import Room, Topic, Message

class CurrentUserDefault:
    """
    Returns the current user.
    """
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user
    
class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        
class RoomSerializer(ModelSerializer):
    host = StringRelatedField(many = False,read_only = True, default = CurrentUserDefault)
    topic = TopicSerializer(many = False, read_only = True)
    participants = StringRelatedField(many = True)
    class Meta:
        model = Room
        fields = '__all__'
        

class MessageSerializer(ModelSerializer):
    user = StringRelatedField(many = False,read_only = True, default = CurrentUserDefault)
    room = StringRelatedField(many = False, read_only = True)
    class Meta:
        model = Message
        fields = '__all__'