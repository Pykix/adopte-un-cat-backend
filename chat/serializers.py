from rest_framework import serializers

from chat.models import Message
from users.models import User
from like.models import Like

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', 
                                            queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', 
                                            queryset=User.objects.all())
    like = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Message
        fields = ["id","sender","sender_id", "receiver", "message", "timestamp", "like"]
        