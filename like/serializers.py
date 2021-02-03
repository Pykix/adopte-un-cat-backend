from rest_framework import serializers

from like.models import Like
from users.api.serializers import ProfileSerializer
from chat.serializers import MessageSerializer

class LikeSerializer(serializers.ModelSerializer):
    from_user = ProfileSerializer(read_only=True)
    to_user = ProfileSerializer(read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Like
        fields = ["id", "from_user", "to_user", "messages", "is_match"]
        
