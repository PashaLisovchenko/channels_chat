from django.conf.urls import url
from .views import chat


urlpatterns = [
    url(r'^send/$', chat, name='chat')
]