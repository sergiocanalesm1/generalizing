from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from generalizing_core.serializers.files_serializer import LessonFileSerializer, RelationFileSerializer
from generalizing_core.models.file import LessonFile, RelationFile
from generalizing_core.models.relation import Relation
from generalizing_core.models.lesson import Lesson
from generalizing_core.api.common.protocols import detail,list

@api_view(['GET', 'POST'])
def lfile_list(request):
    return list(request,LessonFile,LessonFileSerializer,LessonFileSerializer)

@api_view(['GET'])
def lesson_file_list(request, uuid):
    pk = get_object_or_404(Lesson, uuid=uuid).pk
    list = LessonFile.objects.filter(lesson_id = pk)
    serializer = LessonFileSerializer(list, many=True, context={'request':request})
    return Response(serializer.data)

@api_view(['GET'])
def relation_file_list(request, uuid):
    pk = get_object_or_404(Relation, uuid=uuid).pk
    list = RelationFile.objects.filter(relation_id = pk)
    serializer = RelationFileSerializer(list, many=True, context={'request':request})
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def rfile_list(request):
    return list(request,RelationFile,RelationFileSerializer,RelationFileSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def lesson_file_detail(request, uuid):
    return detail(request,uuid,LessonFile,LessonFileSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def relation_file_detail(request, uuid):
    return detail(request,uuid,RelationFile,RelationFileSerializer)