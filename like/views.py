from rest_framework import viewsets

from rest_framework.response import Response

from like.serializers import LikeSerializer
from like.models import Like
from users.models import Profile


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_object(self):
        return self.request.user.profile

    def create(self, request, *args, **kwargs):
        to_profile = request.data.get('to_profile')
        to_profile = Profile.objects.get(pk=to_profile)
        user = self.get_object()

        new_like = Like.objects.create(from_profile=user, to_profile=to_profile)

        return Response(LikeSerializer(new_like).data)
