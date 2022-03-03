from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from generalizing_core.serializers.tag_serializer import TagSerializer
from generalizing_core.models.tag import Tag

@api_view(['GET'])
def get_tags(request):
    tags = Tag.objects.all()
    if tags:
        data = TagSerializer(tags,many=True).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)