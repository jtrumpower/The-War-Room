from war_room_app.models import War
from war_room_app.models import Member
from war_room_app.models import Clan
from war_room_app.serializers import WarSerializer
from rest_framework import generics
from war_room_app.clash_api import clans
from rest_framework.renderers import JSONRenderer
import urllib


class WarList(generics.ListCreateAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

    def perform_create(self, serializer):
        clan = clans.get_clan_by_tag(urllib.quote_plus(serializer.validated_data.get('clan_tag')))
        enemyClan = clans.get_clan_by_tag(urllib.quote_plus(serializer.validated_data.get('enemy_clan_tag')))

        clanModel = Clan(name=clan.get('name'), clan_tag=serializer.validated_data.get('clan_id'))
        clanModel.save()

        print "{0} Vs {1}".format(clan.get('name'), enemyClan.get('name'))
        print clanModel.get('clan_tag')
        serializer.validated_data['title'] = "{0} Vs {1}".format(clan.get('name'), enemyClan.get('name'))
        serializer.validated_data['clan_id'] = clanModel.clan_tag
        members = clan.get('memberList')
        for clan_member in members:
            mem = Member.objects.filter(game_name=clan_member.get('name'), clan_tag=clanModel.clan_tag)
            if len(mem) == 0:
                m = Member(game_name=clan_member.get('name'), clan_tag=clanModel.clan_tag)
                m.save()

        enemyMembers = enemyClan.get('memberList')
        for clan_member in enemyMembers:
            m = Base(war=serializer.validated_data.get('id'), name = clan_member.get('name'), clan_tag=enemyClan.get('tag'))
            m.save()
        return serializer.save()


class WarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

    def perform_update(self, serializer):
        return War.objects.all()
