from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('myproject.pbtgames_fa.views',

    url(r'^$', 'index'),
    
    url(r'^games/list/$', 'list_games'),
    url(r'^game/(?P<game_id>[0-9]+)/$', 'view_game'),

    url(r'^games/test/$', 'test'),
    
    url(r'^contact$', 'contact_us'),
    url(r'^about$', 'about_us'),
    url(r'^tools/cpv$', TemplateView.as_view(template_name='cpv.html')),
    url(r'^tools$', 'dev_tools'),
    url(r'^mohsen/fireworks$', 'mohsen_fireworks'),
    url(r'^mohsen/stars$', 'mohsen_stars'),
    url(r'^mohsen/polygonal$', 'mohsen_polygonal'),
    url(r'^mohsen/postprocessing$', 'mohsen_postprocessing_1'),

 	url(r'^pdf$', 'mohsen_pdf_search'),   
)
