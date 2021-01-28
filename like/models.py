from django.db import models
from users.models import User
from users.models import Profile


class Like(models.Model):
    from_user = models.ForeignKey(Profile,
                                     related_name='from_user',
                                     on_delete=models.CASCADE,
                                     )
    to_user = models.ForeignKey(Profile,
                                   related_name="to_user",
                                   on_delete=models.CASCADE,
                                   )
    is_match = models.BooleanField(default=False)

    
    def __str__(self):
        return "{} - {}".format(self.from_user.__str__(), self.to_user.__str__())
