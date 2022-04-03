from rest_framework import serializers

from generalizing_core.models.relation import Relation
from generalizing_core.serializers.files_serializer import RelationFileSerializer
from generalizing_core.serializers.lesson_serializer import LessonReadSerializer

class RelationReadSerializer(serializers.ModelSerializer):

    files = RelationFileSerializer( source='relationfile_set', many=True, required=False )
    lessons = LessonReadSerializer( many=True, read_only=True )

    class Meta:
        model = Relation
        fields = '__all__'

class RelationWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relation
        fields = '__all__'