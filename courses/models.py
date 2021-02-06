from django.db import models


class Course(models.Model):
    name = models.TextField("Nome do curso")

    def __str__(self):
        return f"Nome do curso: {self.name}"
