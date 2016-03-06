from war_room_app.models import Base
from war_room_app.serializers import BaseSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response


class BaseList(generics.ListCreateAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class BaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class BaseByWar(viewsets.ViewSet):

    def get_all_bases(self, request, war_id):
        queryset = Base.objects.filter(war=war_id)
        serializer = BaseSerializer(queryset, many=True)
        return Response(serializer.data)

