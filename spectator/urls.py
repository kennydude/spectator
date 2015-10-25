"""spectator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.authtoken import views

from spectator.views import (ShowViewSet, ListShowViewSet, StreamItemView,
    ItemViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/auth', views.obtain_auth_token),

    url(r'^api/channels/(?P<channel>[0-9]+)/shows$',
        ListShowViewSet.as_view({
            'get': 'list'
        }), name='api-show-list'),
    url(r'^api/channels/(?P<channel>[0-9]+)/shows/(?P<pk>.+)$',
        ShowViewSet.as_view({
            'get': 'retrieve'
        }), name='api-show'),
    url(r'^api/channels/(?P<channel>[0-9]+)/items/(?P<pk>.+)$',
        ItemViewSet.as_view({
            'get': 'retrieve'
        }), name='api-item'),
    url(r'^api/channels/(?P<channel>[0-9]+)/items/(?P<pk>.+)/stream',
        StreamItemView.as_view({
            'get': 'retrieve'
        }), name='api-stream')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)