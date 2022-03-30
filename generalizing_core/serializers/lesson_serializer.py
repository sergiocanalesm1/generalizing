from rest_framework import serializers

from generalizing_core.models.lesson import Lesson
from generalizing_core.serializers.files_serializer import LessonFileSerializer

class LessonSerializer(serializers.ModelSerializer):

    files = LessonFileSerializer( source='lessonfile_set', many=True, required=False )

    class Meta:
        model = Lesson
        fields = '__all__'