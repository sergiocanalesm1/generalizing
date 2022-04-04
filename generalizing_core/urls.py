from django.urls import path

#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from generalizing_core.api import *

urlpatterns = [

    path('login/', user_login, name='token_obtain_pair'),
    #path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', user_list, name='user-list'),
    #path('users/<uuid>', user_detail, name='user-detail'),

    path('expertises/', expertise_list, name='expertise_list'),
    path('expertises/<uuid>', expertise_detail, name='expertise_detail'),
    path('users/<uuid>/expertises/', expertise_user_list, name='expertise_user_list'),

    path('lessons/', lesson_list, name='lesson-list'),
    path('lessons/<uuid>', lesson_detail, name='lesson-detail'),
    path('users/<uuid>/lessons/', lesson_user_list, name='lesson_user_list'),

    path('relations/', relation_list, name='relation_list'),
    path('relations/<uuid>', relation_detail, name='relation_detail'),
    path('users/<uuid>/relations/', relation_user_list, name='relation_user_list'),

    path('challenges/', challenge_list, name='challenge_list'),
    path('challenges/<uuid>', challenge_detail, name='challenge_detail'),

    path('lessons/<uuid>/files', lesson_file_list, name='lesson_file_list'),
    path('lfiles/', lfile_list, name='lfile_list'),
    path('lfiles/<uuid>', lesson_file_detail, name='lesson_file_detail'),

    path('relations/<uuid>/files', relation_file_list, name='relation_file_list'),
    path('rfiles/', rfile_list, name='rfile_list'),
    path('rfiles/<uuid>', relation_file_detail, name='relation_file_detail'),
]