from django.urls import path
from login import views

urlpatterns = [
    path('',views.home,name="home"),
    path('loggedin/',views.loggedin,name="loggedin"),
    path('profile/',views.profile,name="profile"),
]
