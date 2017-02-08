
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^hostlist$', hostlist, name='hostlist'),
    url(r'^savedata$', savedata, name='savedata'),
    url(r'^details/(?P<host_uid>\w+)$', details, name='details')
]
