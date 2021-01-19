from django.db import models
from users.models import User


class Like(models.Model):
    from_user = models.ForeignKey(User,
                                     related_name='from_user',
                                     on_delete=models.CASCADE,
                                     )
    to_user = models.ForeignKey(User,
                                   related_name="to_user",
                                   on_delete=models.CASCADE,
                                   )

    def __str__(self):
        return "{} - {}".format(self.from_user.__str__(), self.to_user.__str__())
