from rest_framework import serializers

from like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    liked_user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = '__all__'
