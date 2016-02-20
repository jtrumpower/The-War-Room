from war_room_app.models import Clan
from war_room_app.serializers import ClanSerializer
from rest_framework import generics
from war_room_app.clash_api import clans
from rest_framework.renderers import JSONRenderer
import urllib


class ClanList(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer

    def perform_create(self, serializer):
        return serializer.save()


class ClanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer

    def perform_update(self, serializer):
        return Clan.objects.all()
