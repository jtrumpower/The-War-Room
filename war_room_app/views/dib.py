from war_room_app.models import Dib
from war_room_app.serializers import DibSerializer
from rest_framework import generics


class DibList(generics.ListCreateAPIView):
    queryset = Dib.objects.all()
    serializer_class = DibSerializer


class DibDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dib.objects.all()
    serializer_class = DibSerializer
