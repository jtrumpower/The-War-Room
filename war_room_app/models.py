from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Clan(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	clan_tag = models.CharField(primary_key=True, max_length=45)
	war_flag = models.BooleanField(default=True)

	def __str__(self):
			return self.name


war_sizes = (
        (10, "10 Vs 10"),
        (15, "15 Vs 15"),
        (20, "20 Vs 20"),
        (25, "25 Vs 25"),
        (30, "30 Vs 30"),
        (35, "35 Vs 35"),
        (40, "40 Vs 40"),
        (45, "45 Vs 45"),
        (50, "50 Vs 50")
    )

@python_2_unicode_compatible  # only if you need to support Python 2
class War(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    size = models.IntegerField(choices=war_sizes, default=10)
    start_time = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=500, null=True, blank=True)
    clan_tag = models.CharField(max_length=45)
    enemy_clan_tag = models.CharField(max_length=45)
    stars = models.IntegerField(default=0, blank=True)
    enemy_stars = models.IntegerField(default=0, blank=True)
    destruction = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    enemy_destruction = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    clan = models.ForeignKey(Clan, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'start_time'


@python_2_unicode_compatible  # only if you need to support Python 2
class Member(models.Model):
    clan_tag = models.ForeignKey(Clan, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300, null=True, blank=True)
    game_name = models.CharField(max_length=300)
    thumbnail = models.ImageField(null=True, upload_to="./static/photos", blank=True)
    total_stars = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.game_name


@python_2_unicode_compatible  # only if you need to support Python 2
class Base(models.Model):
    war = models.ForeignKey(War, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    destruction = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    stars = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Dib(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0, blank=True, null=True)
    destruction = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
      	return self.member.game_name


@python_2_unicode_compatible  # only if you need to support Python 2
class Comment(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000)
    type = models.CharField(max_length=300, choices=(('comment', 'comment'), ('review', 'review')), default='comment')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
