from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Password(models.Model):
    address = models.CharField(max_length=440)
    password = models.CharField(max_length=55)

    user = models.ForeignKey(user, on_delete=models.CASCADE, default=user, null=False, related_name="user")

    def __str__(self):
        return f"User: {self.user} " \
               f"Adderss: {self.address}"

