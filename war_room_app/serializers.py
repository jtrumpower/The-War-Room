from rest_framework import serializers
from war_room_app.models import War,Comment,Dib,Base,Member

class WarSerializer(serializers.ModelSerializer):
  class Meta:
    model = War
    fields = ('id', 'title', 'size', 'message', 'clan_id', 'enemy_clan_id', 'stars', 'enemy_stars', 'destruction', 'enemy_destruction')


class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = Member
    fields = ('id', 'full_name', 'game_name', 'thumbnail', 'total_stars')


class BaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Base
    fields = ('id', 'name', 'war',)


class DibSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dib
    fields = ('id', 'title', 'member', 'base', 'stars')


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'title', 'base', 'member', 'comment', 'type')