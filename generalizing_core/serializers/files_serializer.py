from rest_framework import serializers

from generalizing_core.models.file import LessonFile, RelationFile

class LessonFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonFile
        fields = '__all__'

class RelationFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelationFile
        fields = '__all__'