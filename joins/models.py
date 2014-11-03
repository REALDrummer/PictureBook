from django.db import models
from django import forms

# Create your models here.

class Join(models.Model):

	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	password =  models.CharField(max_length=32) 
	#password = models.CharField(max_length = 30)
	#e-mail information
	
	#password information
	#pTimestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	#pUpdated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.email