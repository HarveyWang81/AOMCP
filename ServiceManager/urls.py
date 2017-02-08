
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^server_shell/$', server_shell, name='server_shell'),
]
