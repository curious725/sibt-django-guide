from django.conf.urls import url

from . import views

app_name = 'boards'
urlpatterns = [
    # ex: /boards/
    url(r'^$', views.home, name='home'),
    # ex: /boards/3
    url(r'^(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # ex: /boards/3/new
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]
