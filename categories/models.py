from django.db import models
from djangotoolbox.fields import ListField

class Category(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

