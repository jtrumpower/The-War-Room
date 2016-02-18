from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class War(models.Model):
  title = models.CharField(max_length=100,null=True,blank=True)
  size = models.IntegerField()
  start_time = models.DateTimeField(auto_now=True,)
  message = models.CharField(max_length=500,null=True,blank=True)
  clan_id = models.CharField(max_length=45)
  enemy_clan_id = models.CharField(max_length=45)
  stars = models.IntegerField(default=0)
  enemy_stars = models.IntegerField(default=0)
  destruction = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
  enemy_destruction = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

  def __str__(self):
    return self.title


@python_2_unicode_compatible  # only if you need to support Python 2
class Member(models.Model):
  full_name = models.CharField(max_length=300,null=True,blank=True)
  game_name = models.CharField(max_length=300)
  thumbnail = models.ImageField(null=True,upload_to="./static/photos",blank=True)
  total_stars = models.IntegerField(default=0)

  def __str__(self):
    return self.game_name

@python_2_unicode_compatible  # only if you need to support Python 2
class Base(models.Model):
  war = models.ForeignKey(War, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Dib(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  base = models.ForeignKey(Base, on_delete=models.CASCADE)
  title = models.CharField(max_length=100,blank=True,null=True)
  stars = models.IntegerField(default=0)
  time = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


@python_2_unicode_compatible  # only if you need to support Python 2
class Comment(models.Model):
  base = models.ForeignKey(Base, on_delete=models.CASCADE)
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  title = models.CharField(max_length=100,blank=True,null=True)
  comment = models.CharField(max_length=3000)
  type = models.CharField(max_length=300,choices=(('comment','comment'), ('review','review')),default='comment')

  def __str__(self):
    return self.title