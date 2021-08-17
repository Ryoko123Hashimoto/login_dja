from django.urls import path

from . import views

app_name="newapp"

urlpatterns = [
    path("",views.index,name="index"),
    path("home/",views.home,name="home"), #追加
    path("signup/",views.signup,name="signup"), #追加
]