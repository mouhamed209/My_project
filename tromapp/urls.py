from django.urls import path
from .views import *
urlpatterns = [

    path('',welcome),
    path('login',login),
    path('welcome',welcome),
    path('register',register),
    path('addFriend',add_friend),
    path('showProfile',show_profile),
    path('modifyprofile',modify_profile),
   path('update_messages/', update_messages),
   path('inv',invitation),
   path('len_inv/',leninv),
   path('list_friend/',friend_online),
   path('not_online/',not_online),
]
