from django.conf.urls import url
from war_room_app.views import war
from war_room_app.views import member
from war_room_app.views import base
from war_room_app.views import comment
from war_room_app.views import dib

urlpatterns = [
    url(r'^wars/$', war.WarList.as_view()),
    url(r'^wars/(?P<pk>[0-9]+)/$', war.WarDetail.as_view()),
    url(r'^members/$', member.MemberList.as_view()),
    url(r'^members/(?P<pk>[0-9]+)/$', member.MemberDetail.as_view()),
    url(r'^bases/$', base.BaseList.as_view()),
    url(r'^bases/(?P<pk>[0-9]+)/$', base.BaseDetail.as_view()),
    url(r'^dibs/$', dib.DibList.as_view()),
    url(r'^dibs/(?P<pk>[0-9]+)/$', dib.DibDetail.as_view()),
    url(r'^comments/$', comment.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', comment.CommentDetail.as_view())
]
