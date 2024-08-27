from django.contrib import admin
from django.urls import path, include

# from allauth.socialaccount import views as socialaccount_views

urlpatterns = [
    path("", include("core.urls")),
    path("secret/", include("secret.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("__debug__", include("debug_toolbar.urls")),
]

account_urls = [
    # path('accounts/login/', login_not_required(allauth_views.login), name='account_login'),
    # path('accounts/logout/', allauth_views.logout, name='account_logout'),
    # path('accounts/signup/', login_not_required(allauth_views.signup), name='account_signup'),
    # path('accounts/password/change/', allauth_views.password_change, name='account_change_password'),
    # path('accounts/password/set/', login_not_required(allauth_views.password_set), name='account_set_password'),
    # path('accounts/password/reset/', login_not_required(allauth_views.password_reset), name='account_reset_password'),
    # path('accounts/password/reset/done/', login_not_required(allauth_views.password_reset_done), name='account_reset_password_done'),
    # path('accounts/password/reset/key/<uidb64>/<token>/', login_not_required(allauth_views.password_reset_from_key), name='account_reset_password_from_key'),
    # path('accounts/password/reset/key/done/', login_not_required(allauth_views.password_reset_from_key_done), name='account_reset_password_from_key_done'),
    # path('accounts/email/', login_not_required(allauth_views.email), name='account_email'),
    # path('accounts/confirm-email/', login_not_required(allauth_views.email_verification_sent), name='account_email_verification_sent'),
    # path('accounts/confirm-email/<key>/', login_not_required(allauth_views.confirm_email), name='account_confirm_email'),
    # path('accounts/account-inactive/', login_not_required(allauth_views.account_inactive), name='account_inactive'),
    
    # Social Account Views
    # path('social/connections/', login_not_required(socialaccount_views.connections), name='socialaccount_connections'),
    # path('social/signup/', login_not_required(socialaccount_views.signup), name='socialaccount_signup'),
    # path('social/login/cancelled/', login_not_required(socialaccount_views.login_cancelled), name='socialaccount_login_cancelled'),
    # path('social/login/error/', login_not_required(socialaccount_views.login_error), name='socialaccount_login_error'),
]

urlpatterns += account_urls