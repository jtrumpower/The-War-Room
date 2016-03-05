from war_room_app.models import Clan, Member
from war_room_app.serializers import ClanSerializer, MemberSerializer
from rest_framework import generics
from war_room_app.clash_api import clans
from rest_framework.renderers import JSONRenderer
from war_room_app.exceptions import CouldntRetrieveClan
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
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


class ClanMembers(viewsets.ViewSet):
    
    def get_members(self, request, clan_tag):
        queryset = Member.objects.filter(clan_tag=clan_tag)
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

