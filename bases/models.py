from django.db import models

from django.contrib.auth.models import User
class ClaseModelo(models.Model):
    state = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    user_create = models.ForeignKey(User, on_delete=models.CASCADE)
    user_update = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True