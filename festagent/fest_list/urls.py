from django.conf.urls import patterns, url

from fest_list.views import FestList

urlpatterns = patterns('',
    url(r'^$', FestList.as_view(), name='index')
)
