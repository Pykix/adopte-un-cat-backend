from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q


from chat.models import Message
from chat.serializers import MessageSerializer
from users.models import User

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def filter_queryset(self, queryset):
        queryset = super(MessageViewSet, self).filter_queryset(queryset)
        from_user = self.request.user

        finder = get_object_or_404(
            User, pk=from_user.id
        )
        print(finder)
        queryset = queryset.filter(
            Q(sender=finder.id) |
            Q(receiver=finder.id)
        )

        return queryset