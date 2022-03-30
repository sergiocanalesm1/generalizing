from rest_framework import serializers

from generalizing_core.models.relation import Relation
from generalizing_core.serializers.files_serializer import RelationFileSerializer
from generalizing_core.serializers.lesson_serializer import LessonSerializer

class RelationSerializer(serializers.ModelSerializer):

    files = RelationFileSerializer( source='relationfile_set', many=True, required=False )
    lessons = LessonSerializer( many=True )

    class Meta:
        model = Relation
        fields = '__all__'