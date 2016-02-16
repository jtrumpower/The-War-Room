from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bases(models.Model):
	idbases = models.IntegerField(primary_key=True, max_length=11)
	name = models.CharField(max_length=200)
	idwars = models.ForeignKey(Wars, on_delete=models.CASCADE)