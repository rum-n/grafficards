"""blog_project URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog/$', 'blog.views.post', name='blogpage'),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^card_choice/$', 'blog.views.first_step', name='card_choice'),
    url(r'^message_input/$', 'blog.views.second_step', name='message_input'),
    url(r'^address_input/$', 'blog.views.third_step', name='address_input'),
    url(r'^summary/$', 'blog.views.final_step', name='summary'),
    url(r'^postcard_sent_success/$', 'blog.views.sent_success', name='postcard_sent_success'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
