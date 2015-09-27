from django.db import models

from djangotoolbox.fields import EmbeddedModelField, ListField
from users.models import StandardUser

class Event(models.Model):
	name = models.CharField(max_length=40)
	date = models.DateField()
	users = ListField(EmbeddedModelField('StandardUser'))