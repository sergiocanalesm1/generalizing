from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from generalizing_core.serializers.user_serializer import UserSerializer
from generalizing_core.models.user import User
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def user_list(request):
    return list(request,User,UserSerializer,UserSerializer)#fix


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, uuid):
    return detail(request,uuid,User,UserSerializer)

@api_view(['POST'])
def user_login(request):
    #username = request.data['username']
    email = request.data['email']
    password = request.data['password']

    user = get_object_or_404(User, email=email)

    if user.check_password(password):

        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
