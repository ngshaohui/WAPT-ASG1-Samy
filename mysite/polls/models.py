from django.db import models


class Profile(models.Model):
    content = models.CharField(max_length=512)
    owner = models.CharField(max_length=64)


class Friendship(models.Model):
    user1 = models.CharField(max_length=64)
    user2 = models.CharField(max_length=64)
    is_pending = models.BooleanField(default=True)
