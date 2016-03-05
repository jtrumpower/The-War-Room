from rest_framework import serializers
from war_room_app.models import War,Comment,Dib,Base,Member,Clan

class ClanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Clan
    fields = ('name', 'clan_tag', 'war_flag')


class WarSerializer(serializers.ModelSerializer):
  class Meta:
    model = War
    fields = ('id', 'title', 'size', 'message', 'clan_tag', 'enemy_clan_tag', 'stars', 'enemy_stars', 'destruction', 'enemy_destruction', 'start_time', 'clan')


class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    fields = ('id', 'clan_tag', 'full_name', 'game_name', 'thumbnail', 'total_stars')


class BaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Base
    fields = ('id', 'name', 'war',)


class DibSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dib
    fields = ('id', 'member', 'base', 'stars')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'base', 'member', 'comment', 'type')