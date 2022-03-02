from django.urls import path

from generalizing_core.api import *

urlpatterns = [
    #users
    path('users/', UserList.as_view(), name='user-list'),#POST #GET
]