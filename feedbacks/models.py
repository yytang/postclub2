from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import EmbeddedModelField, ListField

class StandardUser(User):
	name = models.CharField(max_length=20)
	localtion

class Questionnaire(models.Model):
	questions = ListField(EmbeddedModelField('Question'))

class Question(models.Model):
	question = models.CharField(max_length=255)

class QuestionAnswers(models.Model):
	question = EmbeddedModelField('Question')
	answer = models.IntegerField()
	user = EmbeddedModelField('User')


