from war_room_app.models import War
from war_room_app.models import Member
from war_room_app.models import Clan
from war_room_app.models import Base
from war_room_app.serializers import WarSerializer
from rest_framework import generics
from war_room_app.clash_api import clans
from rest_framework.renderers import JSONRenderer
from war_room_app.exceptions import CouldntRetrieveClan
import urllib


class WarList(generics.ListCreateAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

    def perform_create(self, serializer):
        clanResponse = clans.get_clan_by_tag(urllib.quote_plus(serializer.validated_data.get('clan_tag')))
        enemyClanResponse = clans.get_clan_by_tag(urllib.quote_plus(serializer.validated_data.get('enemy_clan_tag')))

        if(clanResponse.status_code == 404):
            raise CouldntRetrieveClan(detail="No Results for your clan tag")

        if(enemyClans.status_code == 404):
            raise CouldntRetrieveClan(detail="No Results for enemy clan tag")

        clan = clanResponse.json()
        enemyClans = enemyClanResponse.json()

        myClan = Clan(name=clan.get('name'), clan_tag=serializer.validated_data.get('clan_id'))
        myClan.save()
        
        serializer.validated_data['title'] = "{0} Vs {1}".format(clan.get('name'), enemyClan.get('name'))
        serializer.validated_data['clan_id'] = myClan.clan_tag
        members = clan.get('memberList')
        if members != None:
            for clan_member in members:
                mem = Member.objects.filter(game_name=clan_member.get('name'), clan_tag=myClan)
                if len(mem) == 0:
                    m = Member(game_name=clan_member.get('name'), clan_tag=myClan)
                    m.save()
        return serializer.save()


class WarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = War.objects.all()
    serializer_class = WarSerializer

    def perform_update(self, serializer):
        return War.objects.all()
