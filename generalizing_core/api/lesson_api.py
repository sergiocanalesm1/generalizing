from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from generalizing_core.serializers.lesson_serializer import LessonSerializer
from generalizing_core.models.lesson import Lesson
  
class LessonList(APIView):

    def post(self,request,*args,**kwargs):

        lesson = LessonSerializer(data=request.data)
        print(request.data)

        if lesson.is_valid():
            lesson.save()
            return Response(lesson.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def get(self,request,*args,**kwargs):

        lessons = Lesson.objects.all()
    
        if lessons:
            data = LessonSerializer(lessons,many=True).data
            return Response(data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)