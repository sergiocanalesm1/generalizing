from generalizing_core.api.common.protocols import list
from generalizing_core.models.tag import Tag
from generalizing_core.serializers.tags_serializer import TagsReadSerializer

from rest_framework.decorators import api_view

@api_view(['GET'])
def tags_list(request):
    return list(request,Tag,TagsReadSerializer)