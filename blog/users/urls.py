from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    # path("logout/", views.register, name="logout"),
    path("lk/", views.lk, name="lk"),
    # path("profile/", views.profile, name="profile"),
]
