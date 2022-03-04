from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from generalizing_core.serializers.lesson_serializer import LessonSerializer
from generalizing_core.models.lesson import Lesson
from generalizing_core.models.user import User
from generalizing_core.models.tag import Tag
from generalizing_core.api.common.protocols import detail,list

def handle_tags(tags):

    real_tags = [t.lower() for t in tags]
    for tag in real_tags:
        if not Tag.objects.filter(pk=tag).exists():
            new_tag = Tag(pk=tag)
            new_tag.save()
    print(real_tags)
    return real_tags

@api_view(['GET', 'POST'])
def lesson_list(request):
    if request.data and request.data['tags']:
        request.data['tags'] = handle_tags(request.data['tags'])
    return list(request,Lesson,LessonSerializer)


@api_view(['GET', 'PUT', 'DELETE'])
def lesson_detail(request, uuid):
    if request.data and request.data['tags']:
        request.data['tags'] = handle_tags(request.data['tags'])
    return detail(request,uuid,Lesson,LessonSerializer)

@api_view(['GET'])
def lesson_user_list(request, uuid):
    pk = get_object_or_404(User, uuid=uuid).pk
    list = Lesson.objects.filter(user_id = pk)
    serializer = LessonSerializer(list, many=True,context={'request':request})
    return Response(serializer.data)