from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from war_room_app import views


urlpatterns = [
	url(r'^wars/$', views.WarList.as_view()),
  url(r'^wars/(?P<pk>[0-9]+)/$', views.WarDetail.as_view()),
  url(r'^members/$', views.MemberList.as_view()),
  url(r'^members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
  url(r'^bases/$', views.BaseList.as_view()),
  url(r'^bases/(?P<pk>[0-9]+)/$', views.BaseDetail.as_view()),
  url(r'^dibs/$', views.DibList.as_view()),
  url(r'^dibs/(?P<pk>[0-9]+)/$', views.DibDetail.as_view()),
  url(r'^comments/$', views.CommentList.as_view()),
  url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view())
]