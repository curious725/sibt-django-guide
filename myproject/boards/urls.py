from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /boards/
    url(r'^$', views.home, name='home'),
]
