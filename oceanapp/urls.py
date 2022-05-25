from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='m-home'),
    path('dashboard/home', views.home, name='home'),
    path('auth/login/', views.Login, name='login'),
    path('send/', views.re_send, name='send'),
    path('auth/account-created/', views.created, name='create'),
    path('dashboard/verify/', views.v1, name='v1'),
    path('auth/login/otp/', views.send_otp, name='otp'),
    path('auth/register/', views.Register, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('dashboard/portfolio/', views.portfolio, name='portfolio'),
    path('dashboard/account/', views.account, name='account'),
    path('dashboard/settings/', views.setting, name='setting'),
    path('dashboard/frequently-asked-questions/', views.faq, name='faq'),
    path('dashboard/settings/prefrence/', views.prefrence, name='prefrence'),
    path('dashboard/settings/security/', views.security, name='security'),
    path('dashboard/verify-1/', views.verify1, name='verify1'),
    path('dashboard/verify-2/', views.verify2, name='verify2'),
    path('dashboard/verify-3/', views.thank, name='thank'),
    path('dashboard/email-verification/<str:username>/', views.email_veri, name='email-veri'),
    path('dashboard/portfolio/classic/', views.principal1, name='classic'),
    path('dashboard/portfolio/balanced/', views.principal2, name='balanced'),
    path('dashboard/portfolio/special/', views.principal3, name='special'),
    path('refer/<str:user>/', views.Register2, name='referlin'),
    path('notify', views.notify, name='notify'),
    path('dashbaord/settings/profile/image/', views.profileimg, name='img'),
    path('dashboard/account/withdraw-accured-income/', views.accured_income_withdraw, name='wai'),
    path('dashboard/account/withdraw-referral-credit/', views.withdraw_referral_credit, name='wrc'),
    path('dashboard/account/withdraw-principle/', views.principle_withdraw, name='wp'),
    path('auth/reset-password/', views.email_reset_check, name='reset-form'),
    path('auth/reset-password-form/<str:user>/', views.password_reset_form, name='reset-pass-form'),
    path('auth/password-reset-sent/', views.password_reset_sent, name='reset-sent'),
    path('dashboard/portfolio/wallet-connect/', views.portfolio_wallet_connect, name='wallet-connect'),
    path('dashboard/wc-error', views.wc_error, name='wc.error'),
]