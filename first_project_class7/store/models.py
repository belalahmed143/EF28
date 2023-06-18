from django.db import models
from random import randint
import uuid

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.id)

class Personx(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name  = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.id) + ' / ' + str(self.unique_id)
    



