from .views import UserLogin, UserLogout, register, account, Password_reset, Password_reset_done, Password_reset_confirm, Password_reset_complete
from django.urls import path

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('account/', account, name='account'),
    path('password/reset/', Password_reset.as_view(), name='password_reset'),
    path('password/reset/done/', Password_reset_done.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', Password_reset_confirm.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', Password_reset_complete.as_view(), name='password_reset_complete')
]
