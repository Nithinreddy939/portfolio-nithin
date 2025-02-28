from django.urls import path
from . import views
urlpatterns=[
    path("",views.index ,name="index"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("about/", views.about, name="about"),

    path("display_details/", views.display_details, name="display_details"),
    path("get_persondetails/<str:username>", views.get_persondetails, name="get_persondetails"),
    path("certificate/", views.certificate, name="certificate"),
    path("projects/", views.projects, name="projects"),
    path("qualification/", views.qualification, name="qualification"),

    # membership users login and registration
    path("login/", views.login, name="login"),
]