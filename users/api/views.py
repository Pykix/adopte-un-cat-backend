from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from users.api.persmissions import IsOwnProfileOrReadOnly

from users.models import Profile, User
from users.api.serializers import ProfileSerializer, ProfileAvatarSerializer


class AllProfileViewSet(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]


class InterestedGenderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    # def get_queryset(self):
    #     current_user = self.get_object()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        user = self.get_object()

        finder = get_object_or_404(
            Profile, user_id=user
        )

        queryset = queryset.filter(
            gender=finder.interested_gender,
            interested_gender=finder.gender
        )

        return queryset


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

    def get_object(self):
        return self.request.user

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        user = self.get_object()

        finder = get_object_or_404(
            Profile, user_id=user
        )
        queryset = queryset.filter(
            user=finder.user,
        )

        return queryset


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object
