# -*- coding: utf-8 -*-
from django.conf import os
from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('core.views',
    url(r'^admin/', include(admin.site.urls)),



    url(r'^$', 'indexView'),
)
#
# if settings.DEBUG:
#     urlpatterns += patterns('',
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.STATIC_ROOT}),
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT}),
#         )