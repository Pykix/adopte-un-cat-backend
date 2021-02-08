from django.db import models

from users.models import User
from like.models import Like


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,
                                related_name="receiver")
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    like = models.ForeignKey(Like, on_delete=models.CASCADE, 
                                related_name="messages")
    

    def __str__(self):
        return "{} - {}".format(self.sender, self.receiver)

    class Meta:
        ordering = ('timestamp',)