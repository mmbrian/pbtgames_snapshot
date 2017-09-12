from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('myproject.pbtgames_notif.views',
    url(r'^latest/(?P<page>[0-9]+)/$', 'get_all_notifs'),
	url(r'^after/(?P<timestamp>.*)/$', 'get_notifs_after'), # yyyy-MM-dd HH:mm:ss
)
