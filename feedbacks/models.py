from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField
from users.models import StandardUser
from events.models import Events

class Feedback(models.Model):
	event = EmbeddedModelField('Event');
	reviewer = EmbeddedModelField('StandardUser');
	receiver = EmbeddedModelField('StandardUser');
	score = models.IntegerField();