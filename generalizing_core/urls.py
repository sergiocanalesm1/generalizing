from django.urls import path

from generalizing_core.api import *

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),#POST #GET
    path('tags/', get_tags, name='tags-list'), #GET
    path('lessons/', LessonList.as_view(), name='lesson-list') #POST #GET
]