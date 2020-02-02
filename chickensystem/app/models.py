from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
#     chicken_number = models.IntegerField(default=0)
#     temperature = models.FloatField(default=0.0)
#     humidity = models.FloatField(default=0.0)
    objects = models.Manager()

    def __str__ (self):
        return self.username

