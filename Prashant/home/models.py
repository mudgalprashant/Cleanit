from django.db import models
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
	username = models.CharField(max_length = 100)
	name = models.CharField( max_length = 50, default= 'New User')
	email = models.EmailField(max_length = 100)
	bio = models.TextField( max_length = 150, default = 'Lets make some effort')
	age = models.IntegerField(default = 18)
	gender = models.CharField( max_length = 15,null = True)
	address = models.TextField(null = True)
	contact = models.BigIntegerField(null = True)
	profession = models.CharField(max_length = 100, null = True)
	my_drives = ArrayField(models.CharField(max_length = 100, null=True), size = 50, null = True)
	image = models.ImageField(upload_to='images/', blank = True)

class Drives(models.Model):
	creator = models.CharField(max_length = 50, null = True)
	city = models.CharField(max_length = 50, null = True)
	place = models.TextField(null = True)
	contributers = ArrayField(models.CharField(max_length = 100, null= True), size = 50, null = True)
	date = models.DateField(null = True)
	
