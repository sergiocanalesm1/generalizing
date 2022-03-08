from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from generalizing_core.serializers.expertise_serializer import ExpertiseSerializer
from generalizing_core.models.expertise import Expertise
from generalizing_core.models.user import User
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def expertise_list(request):
    return list(request,Expertise,ExpertiseSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def expertise_detail(request, uuid):
    return detail(request,uuid,Expertise,ExpertiseSerializer)


@api_view(['GET'])
def expertise_user_list(request, uuid):
    pk = get_object_or_404(User, uuid=uuid).pk
    list = Expertise.objects.filter(user_id = pk)
    serializer = ExpertiseSerializer(list, many=True,context={'request':request})
    return Response(serializer.data)