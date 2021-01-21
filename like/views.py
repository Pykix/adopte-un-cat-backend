from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from like.serializers import LikeSerializer
from like.models import Like
from users.models import User
from users.models import Profile


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_object(self):
        return self.request.user

    def create(self, request, *args, **kwargs):
        to_user = request.data.get('to_user')
        to_user = User.objects.get(pk=to_user)
        user = self.get_object()

        new_like = Like.objects.create(from_user=user, to_user=to_user)

        return Response(LikeSerializer(new_like).data)


    def filter_queryset(self, queryset):
        queryset = super(LikeViewSet, self).filter_queryset(queryset)
        from_user = self.get_object()

        finder = get_object_or_404(
            Profile, user_id=from_user
        )
        print(finder)
        queryset = queryset.filter(
            Q(from_user=finder.id) |
            Q(to_user=finder.id)
        )

        return queryset
