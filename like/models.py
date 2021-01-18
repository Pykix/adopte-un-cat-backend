from django.db import models
from users.models import Profile


class Like(models.Model):
    from_profile = models.ForeignKey(Profile,
                                     related_name='from_profile',
                                     on_delete=models.CASCADE,
                                     )
    to_profile = models.ForeignKey(Profile,
                                   related_name="to_profile",
                                   on_delete=models.CASCADE,
                                   )

    def __str__(self):
        return "{} - {}".format(self.from_profile.__str__(), self.to_profile.__str__())
