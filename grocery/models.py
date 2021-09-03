from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	comments = models.CharField(max_length=200,blank=True)
	price = models.FloatField()
	odate = models.DateTimeField()
