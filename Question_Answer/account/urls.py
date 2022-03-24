from django.urls import path
from . import views

from .views import (

    UserCreateView,
    UserLoginView,

)


app_name = 'account'

urlpatterns = [
    path('', views.index, name = "index"),
    path('auth/register/', UserCreateView.as_view(), name = "register"),
    path('auth/login/', UserLoginView.as_view(), name="signup"),
    # path("landing/", views.landing, name="landing"),
    # path("profile/", views.profile, name="profile"),
    # path("Create_question/", views.createquestion, name="create_question"),
    # path("SocialNetwork/", views.sociale, name="Network"),
]
