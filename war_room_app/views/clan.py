from war_room_app.models import Clan, Member
from war_room_app.serializers import ClanSerializer
from rest_framework import generics
from war_room_app.clash_api import clans
from rest_framework.renderers import JSONRenderer
from war_room_app.exceptions import CouldntRetrieveClan
import urllib


class ClanList(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer

    def perform_create(self, serializer):
    	clanResponse = clans.get_clan_by_tag(urllib.quote_plus(serializer.validated_data.get('clan_tag')))

    	if clanResponse.status_code == 404:
    		raise CouldntRetrieveClan(detail="No Results for your clan tag")

    	clanJson = clanResponse.json()

    	serializer.validated_data['name'] = clanJson.get('name')
    	serializer.validated_data['clan_tag'] = clanJson.get("tag")[1:]

    	clan = serializer.save()

    	members = clanJson.get('memberList')
        if members != None and len(members) > 0:
            for clan_member in members:
                mem = Member.objects.filter(game_name=clan_member.get('name'), clan_tag=clan)
                if len(mem) == 0:
                    m = Member(game_name=clan_member.get('name'), clan_tag=clan)
                    m.save()
    	
    	return clan


class ClanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer

    def perform_update(self, serializer):
        return Clan.objects.all()
