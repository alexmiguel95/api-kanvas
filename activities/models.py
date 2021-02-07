from django.db import models
from accounts.models import User


class Activity(models.Model):
    repo = models.TextField("Url do repositório")
    grade = models.FloatField("Nota")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
