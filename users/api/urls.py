from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.views import AllProfileViewSet
from users.api.views import InterestedGenderViewSet
from users.api.views import UserProfileViewSet
from users.api.views import AvatarUpdateView
from like.views import LikeViewSet

router = DefaultRouter()
router.register(r"profiles", AllProfileViewSet, basename="profile-list")
router.register(r"discover", InterestedGenderViewSet, basename="profile-discover")
router.register(r"user-profile", UserProfileViewSet, basename="user-profile")
router.register(r"like", LikeViewSet, basename="like")


urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]
