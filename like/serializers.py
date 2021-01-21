from rest_framework import serializers

from like.models import Like
from users.api.serializers import ProfileSerializer


class LikeSerializer(serializers.ModelSerializer):
    from_user = ProfileSerializer(read_only=True)
    to_user = ProfileSerializer(read_only=True)

    # to_user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = '__all__'
