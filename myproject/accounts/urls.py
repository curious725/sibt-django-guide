from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


from . import views

app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/signup/
    url('signup/$', views.signup, name='signup'),
    # ex: /accounts/logout/
    url('logout/$', LogoutView.as_view(), name='logout'),
    # ex: /accounts/login/
    url(
        'login/$',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    url(r'^password_reset/$',
        PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            success_url=reverse_lazy('accounts:password_reset_done'),
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^password_reset/done/$',
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html',
        ),
        name='password_reset_done'),

    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete'),
        ),

        name='password_reset_confirm'),

    url(r'^password_reset/complete/$',
        PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'),

]
