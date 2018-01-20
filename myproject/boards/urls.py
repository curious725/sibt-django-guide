from django.conf.urls import url

from . import views

app_name = 'boards'
urlpatterns = [
    # ex: /boards/
    url(r'^$', views.home, name='home'),
]
