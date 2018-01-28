from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/signup/
    url('signup/$', views.signup, name='signup'),
    # ex: /accounts/logout/
    url('logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # ex: /accounts/login/
    url(
        'login/$',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
]
