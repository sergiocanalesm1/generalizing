from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from generalizing_core.serializers.user_serializer import UserSerializer
from generalizing_core.models.user import User
  
class UserList(APIView):

    def post(self,request,*args,**kwargs):

        user = UserSerializer(data=request.data)
    
        if user.is_valid():
            user.save()
            return Response(user.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,*args,**kwargs):
    

        users = User.objects.all()
    
        if users:
            data = UserSerializer(users,many=True).data
            return Response(data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)