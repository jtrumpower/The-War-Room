from war_room_app.models import War
from war_room_app.models import Member
from war_room_app.serializers import WarSerializer
from rest_framework import generics
from war_room_app.clash_api import clans
from rest_framework.renderers import JSONRenderer
import urllib


class WarList(generics.ListCreateAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

    def perform_create(self, serializer):
        clan = clans.get_clan_by_tag(urllib.quote_plus(serializer.validated_data.get('clan_id')))
        members = clan.json().get('memberList')
        for clan_member in members:
            mem = Member.objects.filter(game_name=clan_member.get('name'))
            if len(mem) == 0:
                m = Member(game_name=clan_member.get('name'))
                m.save()
        return serializer.save()


class WarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

    def perform_update(self, serializer):
        return War.objects.all()
