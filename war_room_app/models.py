from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Wars(models.Model):
  idwars = models.IntegerField(primary_key=True)
  size = models.IntegerField()
  starttime = models.DateTimeField()
  message = models.CharField(max_length=500)
  clanid = models.CharField(max_length=45)
  enemyclanid = models.CharField(max_length=45)
  stars = models.IntegerField(max_length=11)
  enemystars = models.IntegerField()
  destruction = models.DecimalField(max_digits=10, decimal_places=3)
  enemydestruction = models.DecimalField(max_digits=10, decimal_places=3)


class Members(models.Model):
  idmembers = models.IntegerField(primary_key=True)
  fullname = models.CharField(max_length=300)
  gamename = models.CharField(max_length=300)
  thumbnail = models.ImageField()
  totalstars = models.IntegerField()


class Bases(models.Model):
  idbases = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=200)
  idwars = models.ForeignKey(Wars, on_delete=models.CASCADE)


class Calls(models.Model):
  idcalls = models.IntegerField(primary_key=True)
  idmembers = models.ForeignKey(Members, on_delete=models.CASCADE)
  idbases = models.ForeignKey(Bases, on_delete=models.CASCADE)
  stars = models.IntegerField()
  time = models.DateTimeField()


class Comments(models.Model):
  idcomments = models.IntegerField(primary_key=True)
  idbases = models.ForeignKey(Bases, on_delete=models.CASCADE)
  idmembers = models.ForeignKey(Members, on_delete=models.CASCADE)
  comment = models.CharField(max_length=3000)
  type = models.CharField(max_length=300)