from django.db import models

# Create your models here.
class Home(models.Model):
	email= models.CharField(max_length=20)
	pass1=models.CharField(max_length=20)
	repass=models.CharField(max_length=20)