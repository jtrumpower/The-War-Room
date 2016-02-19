from war_room_app.models import Base
from war_room_app.serializers import BaseSerializer
from rest_framework import generics


class BaseList(generics.ListCreateAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class BaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer
