from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notification/', include('myproject.pbtgames_notif.urls')),

    url(r'^fa/', include('myproject.pbtgames_fa.urls')),
    # pbtgames_fa handles both languages
    url(r'^en/', include('myproject.pbtgames_fa.urls')),

	url(r'^robots.txt', 'myproject.views.robots'),    
)

handler404 = 'myproject.views.custom_page_not_found_view'
handler500 = 'myproject.views.custom_error_view'
handler403 = 'myproject.views.custom_permission_denied_view'
handler400 = 'myproject.views.custom_bad_request_view'
