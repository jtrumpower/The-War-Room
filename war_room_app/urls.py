from django.conf.urls import url
from war_room_app.views import clan
from war_room_app.views import war
from war_room_app.views import member
from war_room_app.views import base
from war_room_app.views import comment
from war_room_app.views import dib

urlpatterns = [
    url(r'^clans/$', clan.ClanList.as_view()),

    # custom War api
    url(ur'^clans/(?P<clan_tag>.*)/wars/latest/$', war.WarByClan.as_view({'get': 'get_latest_by_clan'})),
    url(ur'^clans/(?P<clan_tag>.*)/wars/(?P<war_id>[0-9]+)/$', war.WarByClan.as_view({'get': 'get_by_clan'})),
    url(ur'^clans/(?P<clan_tag>.*)/wars/$', war.WarByClan.as_view({'get': 'get_all_wars'})),

    # custom Base api
    url(ur'^wars/(?P<war_id>.*)/bases/$', base.BaseByWar.as_view({'get': 'get_all_bases'})),


    url(ur'^clans/(?P<clan_tag>.*)/members/$', clan.ClanMembers.as_view({'get': 'get_members'})),
    url(ur'^clans/(?P<pk>.*)/$', clan.ClanDetail.as_view()),
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
