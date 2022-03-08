from rest_framework.decorators import api_view

from generalizing_core.serializers.challenge_serializer import ChallengeSerializer
from generalizing_core.models.challenge import Challenge
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def challenge_list(request):
    return list(request,Challenge,ChallengeSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def challenge_detail(request, uuid):
    return detail(request,uuid,Challenge,ChallengeSerializer)