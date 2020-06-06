from django.db import models

class TiLoginUserData(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.TextField(blank=True, null=True)
    mark_attandance = models.BooleanField(default=True)


class TiLoginUserData2(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.TextField(blank=True, null=True)
    mark_attandance = models.BooleanField(default=True)
