from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from generalizing_core.serializers.relation_serializer import RelationReadSerializer, RelationWriteSerializer
from generalizing_core.models.relation import Relation
from generalizing_core.models.user import User
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def relation_list(request):
    return list(request,Relation,RelationReadSerializer, RelationWriteSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def relation_detail(request, uuid):
    return detail(request,uuid,Relation,RelationWriteSerializer)


@api_view(['GET'])
def relation_user_list(request, uuid):
    pk = get_object_or_404(User, uuid=uuid).pk
    list = Relation.objects.filter(user_id = pk)
    serializer = RelationReadSerializer(list, many=True, context={'request':request})
    return Response(serializer.data)