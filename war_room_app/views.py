from django.shortcuts import render

# Create your views here.
from war_room_app.models import War,Member,Base,Dib,Comment
from war_room_app.serializers import WarSerializer,MemberSerializer,BaseSerializer,DibSerializer,CommentSerializer
from rest_framework import generics


class WarList(generics.ListCreateAPIView):
  queryset = War.objects.all()
  serializer_class = WarSerializer


class WarDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = War.objects.all()
  serializer_class = WarSerializer


class MemberList(generics.ListCreateAPIView):
  queryset = Member.objects.all()
  serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Member.objects.all()
  serializer_class = MemberSerializer


class BaseList(generics.ListCreateAPIView):
  queryset = Base.objects.all()
  serializer_class = BaseSerializer


class BaseDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Base.objects.all()
  serializer_class = BaseSerializer


class DibList(generics.ListCreateAPIView):
  queryset = Dib.objects.all()
  serializer_class = DibSerializer


class DibDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dib.objects.all()
  serializer_class = DibSerializer


class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer