from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("logout", views.user_logout, name="logout"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("password_change", views.password_change, name="password_change"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path("hom", views.hom, name="hom"),
    path('login', views.user_login, name="login"),


]