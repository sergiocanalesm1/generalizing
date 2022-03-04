from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view

from generalizing_core.serializers.user_serializer import UserSerializer
from generalizing_core.models.user import User
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def user_list(request):
    if request.data and request.data['password']:
        request.data['password'] = make_password(request.data['password'])
    return list(request,User,UserSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, uuid):
    if request.data and request.data['password']:
        request.data['password'] = make_password(request.data['password'])
    return detail(request,uuid,User,UserSerializer)