from war_room_app.models import Member
from war_room_app.serializers import MemberSerializer
from rest_framework import generics


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
