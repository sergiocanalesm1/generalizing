from rest_framework import serializers

from generalizing_core.models.lesson import Lesson
from generalizing_core.serializers.files_serializer import LessonFileSerializer

class LessonReadSerializer(serializers.ModelSerializer):

    files = LessonFileSerializer( source='lessonfile_set', many=True, required=False,read_only=True )

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'