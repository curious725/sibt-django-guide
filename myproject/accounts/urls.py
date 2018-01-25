from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/signup/
    url('signup/$', views.signup, name='signup'),
]
