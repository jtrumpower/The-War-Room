from __future__ import unicode_literals

from django.db import models


# Create your models here.
class War(models.Model):
  size = models.IntegerField()
  starttime = models.DateTimeField()
  message = models.CharField(max_length=500)
  clanid = models.CharField(max_length=45)
  enemyclanid = models.CharField(max_length=45)
  stars = models.IntegerField()
  enemystars = models.IntegerField()
  destruction = models.DecimalField(max_digits=10, decimal_places=3)
  enemydestruction = models.DecimalField(max_digits=10, decimal_places=3)


class Member(models.Model):
  fullname = models.CharField(max_length=300)
  gamename = models.CharField(max_length=300)
  thumbnail = models.ImageField(null=True)
  totalstars = models.IntegerField()


class Base(models.Model):
  name = models.CharField(max_length=200)
  war = models.ForeignKey(War, on_delete=models.CASCADE)


class Dib(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  base = models.ForeignKey(Base, on_delete=models.CASCADE)
  stars = models.IntegerField()
  time = models.DateTimeField()


class Comment(models.Model):
  base = models.ForeignKey(Base, on_delete=models.CASCADE)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  comment = models.CharField(max_length=3000)
  type = models.CharField(max_length=300)