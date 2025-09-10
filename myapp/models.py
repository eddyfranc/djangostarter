from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

# Create your models here.
