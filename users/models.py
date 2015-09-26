from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import EmbeddedModelField, ListField

class StandardUser(User):
	name = models.CharField(max_length=20)

class Questionnaire(models.Model):
	questions = ListField(EmbeddedModelField('Question'))

class Question(models.Model):


