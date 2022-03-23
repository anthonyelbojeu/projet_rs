from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    # path('register/', views.register, name = "register"),
    path('sign_up/', views.signup_page, name="signup"),
    # path("landing/", views.landing, name="landing"),
    # path("profile/", views.profile, name="profile"),
    # path("Create_question/", views.createquestion, name="create_question"),
    # path("SocialNetwork/", views.sociale, name="Network"),
]
